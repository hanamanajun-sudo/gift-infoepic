# 작업 인수인계 — 선물 가이드 큐레이션 파이프라인

**대상**: 이 작업을 이어받는 AI 에이전트 (Claude 여부 무관)
**작성일**: 2026-07-03
**프로젝트**: gift.infoepic.com (Astro + Notion CMS, Cloudflare Pages 배포)
**작업 위치**: 이 저장소 루트 (`gift.infoepic/`)

---

## 1. 지금 무슨 상황인가

이 사이트는 96개+ 선물 추천 가이드 페이지를 갖고 있는데, 최근 실측 결과 본문이 평균 372자짜리 뼈대에 상품 추천도 부실하다는 게 드러났다. Google Search Console에서 노출은 되는데 클릭이 0에 수렴하는 문제의 원인이었다.

해결책으로 **가이드 하나씩 재큐레이션하는 파이프라인**을 만들었고, 지금까지 2개 가이드(12세-여자아이-생일선물, 13세-여자아이-생일선물)를 이 파이프라인으로 완료해서 라이브에 배포했다. 나머지 가이드들을 같은 방식으로 하나씩 처리하는 게 남은 작업이다.

**먼저 읽을 것**: `CONTENT-PLAYBOOK.md` (프로젝트 루트) — 본문 템플릿, 일본 벤치마킹 근거, 완료 현황표, 리서치 로그가 전부 여기 있다. 이 문서는 "어떻게 실행하는지"를 다루고, PLAYBOOK은 "왜 이런 구조인지"를 다룬다. 두 문서는 서로를 참조하므로 같이 봐야 한다.

---

## 2. 파일 지도

```
gift.infoepic/
├── CONTENT-PLAYBOOK.md          ← 본문 템플릿·완료현황·리서치 로그 (필독)
├── HANDOFF.md                    ← 이 문서
├── .env                          ← API 키 전부 이미 설정됨 (아래 3번 참고)
├── scripts/
│   ├── research/
│   │   ├── collect.mjs           ← 여론 수집 CLI 진입점
│   │   ├── naver-blog.mjs        ← 네이버 블로그 검색 API
│   │   └── youtube.mjs           ← 유튜브 검색+댓글 API
│   └── content/
│       ├── lib.mjs               ← Notion 블록 빌더 + push 함수 (공용)
│       ├── push.mjs              ← Notion 반영 CLI 진입점
│       └── guides/
│           ├── 12세-여자아이-생일선물.mjs   ← 완료 사례 (템플릿으로 참고)
│           └── 13세-여자아이-생일선물.mjs   ← 완료 사례
├── src/
│   ├── data/research/            ← 수집된 원본 여론 데이터 (JSON, 재사용 가능)
│   ├── lib/notion.ts             ← Notion 읽기 레이어 (건드릴 일 거의 없음)
│   └── lib/coupang.ts            ← 쿠팡 파트너스 API (빌드 시 실시간 추천용, 큐레이션과 별개)
└── dist/                         ← `npm run build` 결과물 (검증용, git 추적 안 됨)
```

---

## 3. 환경 준비

`.env`에 다음 키가 전부 이미 채워져 있다 (재발급 불필요):
- `NOTION_API_KEY`, `NOTION_GUIDES_DB_ID`, `NOTION_PRODUCTS_DB_ID`
- `NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET` (블로그 검색 + 쇼핑 검색 API 공용)
- `YOUTUBE_API_KEY`
- `COUPANG_ACCESS_KEY`/`SECRET` — 비어있음, 큐레이션 파이프라인과 무관하니 무시해도 됨

Node.js 스크립트는 전부 `node --env-file=.env <경로>` 형태로 실행한다 (Node 20.6+ 내장 기능, dotenv 패키지 없음).

```bash
npm install   # node_modules 없으면 먼저
```

---

## 4. 가이드 1개 처리하는 절차 (반복 실행용)

`CONTENT-PLAYBOOK.md` 6절과 동일한 내용이지만, 실제 명령어까지 붙여서 여기 다시 적는다.

### 4-1. 다음 대상 정하기
`CONTENT-PLAYBOOK.md` 8절 "완료된 가이드 현황" 표에서 다음 순서를 확인한다. 우선순위는 Google Search Console 노출 기준 "7~13세 자녀 선물" 클러스터가 1순위다. 다음 대상: **10세-남자아이-생일선물** (그 다음 10-12세-남자아이-생일선물은 카니발라이제이션 후보라 10세 완료 후 병합 여부 재검토).

가이드가 실제로 존재하는지는 `dist/선물/` 하위 폴더명으로 확인 가능하다 (빌드를 한 번 돌려야 생성됨). 또는 Notion GiftGuides DB를 직접 조회.

### 4-2. 여론 수집
```bash
npm run collect -- "10세 남아 생일선물 후기" "초등학생 남자 갖고싶은 선물"
```
결과는 `src/data/research/{키워드}.json`에 저장된다. **키워드 팁** (실측 근거는 PLAYBOOK 9절):
- 나이 숫자만 넣으면(`13세 여아 선물`) 육아용품 사이즈표에 낚여 노이즈 위주로 나올 수 있다. "후기", "찐", "받고싶은" 같은 수식어를 넣거나, 초등 고학년 이상이면 "초등학생"/"중학생" 같은 학년 표현으로 바꿔본다.
- 결과 JSON을 열어서 `naverBlog[].title`/`.description`과 `youtube[].comments[].text`를 직접 읽고 신호와 노이즈를 사람이 걸러야 한다. 자동 필터링 로직은 없다 — 광고 쇼츠(댓글이 전부 "이거 어디서 사요")와 실제 위시리스트/후기 콘텐츠를 구분하는 게 핵심 작업이다.

### 4-3. 일본 커뮤니티 교차검증 (건너뛰지 말 것)
Yahoo!知恵袋 무료 API는 없다(2017년 유료화). 대신:
1. 웹 검색: `{연령} {성별} 誕生日プレゼント 知恵袋` 형태로 검색해서 관련 스레드 URL 찾기
2. 개별 스레드 URL을 웹 페이지 읽기 도구로 열어서 질문/답변 내용 확인
3. 한일 양쪽에서 독립적으로 나오는 카테고리는 신뢰도가 올라간 것으로 취급, 일본에만 있는 카테고리는 후보로 검토
4. **주의**: 브랜드명은 그대로 옮기지 말 것(한국 대체 브랜드로 치환). 금액도 맥락 확인 필수 — 생일선물 예산인지 답례품/사은품 예산인지 반드시 구분(자릿수가 다름, PLAYBOOK 9절 "함정" 참고)
5. `blog.naver.com`은 웹 페이지 읽기 도구로 열리지 않는다(차단됨) — 검색 API 스니펫(title+description)만으로 판단해야 한다. 이건 도구 제약이지 작업 실수가 아니다.

### 4-4. 상품 교차매칭
여론 수집에서 뽑은 카테고리를, 네이버쇼핑 검색 API로 재검색해서 실제 가격·이미지·구매링크를 확보한다:

```javascript
const url = 'https://openapi.naver.com/v1/search/shop.json?query=' + encodeURIComponent(keyword) + '&display=5&sort=sim';
fetch(url, { headers: { 'X-Naver-Client-Id': clientId, 'X-Naver-Client-Secret': clientSecret } })
```
(`NAVER_CLIENT_ID`/`SECRET`는 `.env`에서 `process.env`로 읽는다.) 응답 필드: `title`(HTML태그 포함, 제거 필요), `lprice`, `link`, `image`, `mallName`.

**중요한 함정**: 검색 결과에서 상품명과 가격을 짝지을 때, 여러 후보가 나오면 이름과 가격을 반드시 재확인할 것. 실제로 이 작업 중 "크래프트 크러쉬 팔찌 메이커"라는 이름에 다른 상품(27,300원짜리)의 가격을 잘못 붙인 적이 있고, "에어팟4 ANC"라는 이름에 ANC 없는 기본형 가격(170,640원)을 잘못 붙인 적도 있다. 최종 확정 전에 검색 결과 원본을 다시 한번 대조하는 습관을 들일 것.

네이버쇼핑/쿠팡 API 둘 다 **리뷰수·평점 필드를 주지 않는다**. "리뷰 2,500개, 평점 4.8" 같은 근거는 자동 수집이 안 되므로 만들어내지 말 것 — 근거는 항상 "블로그/유튜브에서 반복 언급됨" 같은 실제 수집 데이터에 기반해야 한다.

### 4-5. 큐레이션 승인 세션
후보 5~7개를 상품명·가격·근거(어느 블로그/유튜브/일본 스레드에서 나온 신호인지) 표로 정리해서 **사용자에게 승인받는다.** 이 단계를 건너뛰지 말 것 — "사람이 골랐다는 느낌"이 나오는 지점이 여기다. 제외한 후보와 이유도 같이 보여주면 판단 근거가 더 명확해진다.

### 4-6. 본문 작성 + Notion 반영
`scripts/content/guides/13세-여자아이-생일선물.mjs`를 열어서 구조를 그대로 참고해 새 파일을 만든다:

```javascript
// scripts/content/guides/{슬러그}.mjs
import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '{슬러그}';
export const intro = '...';        // 리드문 200자 내외, Notion intro 속성에 들어감
export const blocks = [ ... ];      // 본문 블록 배열 (PLAYBOOK 5절 템플릿 구조)
export const products = [ ... ];    // { name, price, naverUrl, coupangUrl?, imageUrl, rank, pros }
```

본문 템플릿 구조(가격대별 표 → 고르는 법 유형분기 → 사지 마세요 → FAQ)는 `CONTENT-PLAYBOOK.md` 5절 참고. 작성 후 실행:

```bash
node --env-file=.env scripts/content/push.mjs {슬러그}
```

이 명령이 하는 일: Notion GiftGuides에서 슬러그로 페이지 찾기 → intro 갱신 → 기존 본문 블록 전부 삭제 → 새 블록 추가 → 기존에 연결된 Products는 아카이브 처리 → 새 상품 생성. **재실행해도 안전하다** (기존 블록/상품을 지우고 새로 채우는 방식).

### 4-7. 검증
```bash
npx astro build
```
빌드 후 `dist/선물/{슬러그}/index.html`을 열어서 상품 카드 개수, 표 렌더링, 본문 텍스트가 의도대로 나왔는지 확인한다. Python 등으로 HTML 파싱해서 자동 확인하는 방법은 이전 작업 로그(대화 기록 없으면 생략 가능) 참고 — 핵심 체크포인트만 적으면:
```python
'class="product-card"' 개수 == products 배열 길이
'<table>' in html  # Notion 테이블 블록이 렌더링됐는지
```

### 4-8. 커밋 & 푸시
```bash
git add -A -- ':!.env'
git commit -m "..."
git fetch origin && git log --oneline master..origin/master   # 반드시 먼저 확인
git push origin master
```

**절대 건너뛰면 안 되는 것**: push 전에 `git fetch` + `git log master..origin/master`로 원격에 낯선 커밋이 있는지 확인할 것. 이 프로젝트는 여러 세션(사람이 다른 창에서 돌린 자동화 포함)이 동시에 작업할 수 있는 환경이다. 실제로 한 번, 원격에 70개+ 커밋이 쌓여 있던 걸 모르고 push하려다 발견한 적이 있다(자동화 파이프라인이 98개 가이드에 쿠팡 상품 300개+를 이미 채워둔 상태였음). 그때는:
1. 절대 강제 push 하지 않았고
2. 임시 브랜치에서 병합을 시험해 충돌 범위를 먼저 확인했고
3. 충돌이 나면 두 세션의 의도를 각각 파악해서 합쳤다(코드 충돌은 `src/lib/notion.ts` 한 곳뿐이었고, 재시도 로직 vs 테이블 지원처럼 서로 다른 이유로 같은 함수를 고친 경우였다)
4. 그리고 사용자에게 "이거 사용자님이 다른 데서 시킨 작업 맞나요?"부터 확인했다

낯선 원격 커밋을 발견하면 최소한 사용자에게 보고하고, 가능하면 위 순서를 따를 것.

---

## 5. 알아두면 좋은 배경 지식

- **Notion Products DB의 타이틀 속성명은 `Title`이지 `Name`이 아니다.** `src/lib/notion.ts`의 `parseProduct`가 예전엔 `p.Name`을 읽어서 상품명이 항상 빈 문자열이었던 버그가 있었는데, 이번 작업 중 발견해서 고쳤다. 이미 고쳐져 있으니 다시 건드릴 필요는 없지만, Notion 속성명을 코드에 하드코딩할 때는 실제 DB 스키마를 먼저 확인하는 습관을 들일 것 (`notion.databases.retrieve`가 이 워크스페이스에서 deprecated 에러를 내서, 대신 raw fetch로 `Notion-Version: 2022-06-28` 헤더를 명시해서 스키마를 조회했다).
- **Notion 테이블 블록 렌더링을 `src/lib/notion.ts`에 새로 추가했다.** 예전엔 표를 Notion에 넣어도 사이트에서 무시됐다. 지금은 정상 렌더링되니, 본문에 표를 적극 활용해도 된다.
- **`getGuideContent`에 재시도(3회, 지수 백오프) + 전체 페이지네이션 로직이 있다.** 다른 세션이 레이트리밋 대응으로 추가한 것을 병합 시 살려뒀다. 블록 100개 넘는 가이드도 안전하게 읽힌다.
- 쿠팡 파트너스 API(`src/lib/coupang.ts`)는 큐레이션 파이프라인과 별개로, 빌드 시점에 "쿠팡 실시간 추천 상품" 섹션을 채우는 용도다. 리뷰수/평점 필드가 없고, 분당 호출 제한(50회)이 있어 캐시(`src/data/coupang-cache.json`, 7일 TTL)를 쓴다. 큐레이션 상품(Products DB)과는 별개 시스템이니 혼동하지 말 것.
- 사이트 라이브 URL 패턴: `https://gift.infoepic.com/선물/{슬러그}/`

---

## 6. 다음에 할 일 (우선순위)

1. 10세-남자아이-생일선물 (위 절차 그대로)
2. 10-12세-남자아이-생일선물 — 10세 완료 후, 두 페이지가 같은 검색 의도를 나눠 갖는 카니발라이제이션 문제가 있는지 판단(병합 또는 canonical 처리 검토)
3. 이후 GSC 노출 상위 키즈 클러스터 나머지 순회
4. 전체 순회 끝나면 `/나이/`, `/관계/` 같은 필터 페이지 본문 보강 (`CONTENT-PLAYBOOK.md` 7절)
