# 작업 인수인계 — 선물 가이드 큐레이션 파이프라인 + 사이트 성장

**대상**: 이 작업을 이어받는 AI 에이전트 (Claude·Hermes·Copilot·ChatGPT 무관)
**작성일**: 2026-07-03
**프로젝트**: gift.infoepic.com (Astro 5 + Notion CMS, Cloudflare Pages 배포)
**저장소**: https://github.com/hanamanajun-sudo/gift-infoepic
**로컬 경로**: `C:\dev\justdoit\gift-infoepic` (또는 이 문서가 있는 폴더)
**작업 위치**: 이 저장소 루트 (`gift.infoepic/`)

---

## 0. 이 문서의 목적

이 문서를 읽은 **어떤 AI 도구든** 바로 큐레이션·배포 작업을 시작할 수 있게 하는 게 목적이다. Claude 전용 기능(메모리, 프로젝트 설정)에 전혀 의존하지 않고, 저장소 파일만으로 실행 가능한 절차서다.

**먼저 읽을 것**: 함께 있는 `CONTENT-PLAYBOOK.md` (완료 현황, 본문 템플릿, 리서치 로그)

---

## 1. 지금 무슨 상황인가

이 사이트는 **96개** 선물 추천 가이드 페이지(총 **148개** HTML 페이지, 필터·카테고리 포함)를 갖고 있다. 문제:

1. **본문이 평균 372자짜리 뼈대** — 검색 노출은 되는데 내용이 얇아서 클릭이 거의 0에 수렴
2. **상품 데이터는 이미 300개+ 채워져 있음** (자동화 스크립트로 채운 Products DB) → 그러나 큐레이션(사람 손을 거친 선별)이 아님
3. **해결책**: 가이드 하나씩 **재큐레이션 파이프라인**으로 돌리기

**현재까지 큐레이션 완료**: 2개 가이드
- 12세-여자아이-생일선물 ✅ (5개 상품, 라이브)
- 13세-여자아이-생일선물 ✅ (6개 상품, 라이브)
- 10세-남자아이-생일선물 ⬜ **다음 순서**

---

## 2. 사이트 현황 스냅샷 (2026-07-03)

| 지표 | 값 | 비고 |
|------|-----|------|
| 총 가이드(슬러그) | 96개 | `dist/선물/` 폴더 수 |
| 전체 페이지 | 148개 | 필터·카테고리 포함 |
| 큐레이션 완료 | 2개 | 12세여아, 13세여아 |
| Products DB | 300개+ 자동 채워짐 | 수동 선별 아님 |
| 배포 | Cloudflare Pages | GitHub Actions 자동 / wrangler 수동 |
| GA4 | G-NQTCBQDJF5 | BaseLayout.astro에 이미 적용됨 |
| Google Search Console | 등록 완료 | sitemap-index.xml 제출됨 |
| 네이버 서치콘솔 | 등록 완료 | naver94376...html 소유확인 |
| RSS | 있음 | `/rss.xml` |
| 사이트맵 | 있음 | `/sitemap-index.xml` |
| 검색 | Pagefind | `npm run build` 시 자동 인덱싱 |
| 쿠팡 파트너스 API | 비활성화 | `.env` 키 비움 (트래픽 부족으로 저품질 우려) |

---

## 3. 파일 지도

```
gift.infoepic/
├── CONTENT-PLAYBOOK.md          ← 본문 템플릿·완료현황·리서치 로그 (필독)
├── HANDOFF.md                    ← 이 문서
├── PROGRESS.md                   ← 과거 작업 로그 (참고용)
├── ROADMAP.md                    ← 초기 로드맵 (참고용)
├── .env                          ← API 키 전부 이미 설정됨 (아래 4번 참고)
├── astro.config.mjs              ← Astro 설정 (trailingSlash: 'ignore')
├── wrangler.toml                 ← Cloudflare Pages 설정
├── package.json                  ← npm scripts:
│   ├── dev          → astro dev
│   ├── build        → astro build && pagefind --site dist
│   └── collect      → node --env-file=.env scripts/research/collect.mjs
├── scripts/
│   ├── research/
│   │   ├── collect.mjs           ← 여론 수집 CLI 진입점
│   │   ├── naver-blog.mjs        ← 네이버 블로그 검색 API
│   │   └── youtube.mjs           ← 유튜브 검색+댓글 API
│   ├── content/
│   │   ├── lib.mjs               ← Notion 블록 빌더(h2/h3/p/bullet/table) + pushGuide()
│   │   ├── push.mjs              ← Notion 반영 CLI (node --env-file=.env push.mjs {슬러그})
│   │   └── guides/
│   │       ├── 12세-여자아이-생일선물.mjs   ← 완료 사례 (템플릿으로 참고)
│   │       └── 13세-여자아이-생일선물.mjs   ← 완료 사례
│   ├── *.py                      ← 과거 일괄 채우기 스크립트들 (지금은 쓰지 않음, 참고만)
├── src/
│   ├── data/research/            ← 수집된 원본 여론 데이터 (JSON)
│   ├── lib/notion.ts             ← Notion 읽기 레이어 (getGuideContent, parseProduct 등)
│   │   ※ getGuideContent: 재시도 3회 + 전체 페이지네이션 로직 있음
│   │   ※ parseProduct: p.Name이 아니라 p.Title을 읽음 (버그 수정 완료)
│   └── lib/coupang.ts            ← 쿠팡 파트너스 API (현재 비활성, 건드릴 일 없음)
├── public/                       ← 정적 파일 (naver 소유확인 파일, robots.txt, favicon)
├── dist/                         ← `npm run build` 결과물 (git 추적 안 됨)
└── .github/workflows/            ← GitHub Actions CI/CD
```

---

## 4. 환경 준비

```bash
npm install   # node_modules 없으면 먼저
```

`.env`에 다음 키가 전부 이미 채워져 있다 (재발급 불필요):
- `NOTION_API_KEY`, `NOTION_GUIDES_DB_ID`, `NOTION_PRODUCTS_DB_ID`
- `NAVER_CLIENT_ID`, `NAVER_CLIENT_SECRET` (블로그 검색 + 쇼핑 검색 API 공용)
- `YOUTUBE_API_KEY`
- `COUPANG_ACCESS_KEY` / `COUPANG_SECRET_KEY` — **비어있음**. 큐레이션 파이프라인과 무관하니 무시

Node.js 스크립트는 전부 `node --env-file=.env <경로>` 형태로 실행한다 (Node 20.6+ 내장 기능).

---

## 5. 가이드 1개 처리하는 절차 (반복 실행용)

`CONTENT-PLAYBOOK.md` 6절과 같은 내용이지만 실제 명령어를 붙여서 여기에도 적는다.

### 5-1. 다음 대상 정하기

`CONTENT-PLAYBOOK.md` 8절 "완료된 가이드 현황" 표에서 다음 순서 확인.

**현재 우선순위**: Google Search Console 노출 기준 "7~13세 자녀 선물" 클러스터가 1순위.
- `10세-남자아이-생일선물` ← **다음 대상**
- `10-12세-남자아이-생일선물` ← 카니발라이제이션 후보 (10세 완료 후 병합 여부 재검토)

가이드 존재 확인: `dist/선물/` 하위 폴더명으로 가능. 또는 Notion GiftGuides DB 직접 조회.

### 5-2. 여론 수집

```bash
npm run collect -- "10세 남아 생일선물 후기" "초등학생 남자 갖고싶은 선물"
```

결과는 `src/data/research/{키워드}.json`에 저장된다.

**키워드 실측 노하우**:
- 나이 숫자만 넣으면(`13세 여아 선물`) 육아용품 사이즈표 노이즈에 낚인다
- **"후기"**, **"찐"**, **"받고싶은"** 같은 수식어를 넣을 것
- 초등 고학년 이상은 **"나이" 키워드보다 "초등학생"/"중학생" 키워드**가 낫다
- 결과 JSON을 열어서 `naverBlog[].title`/`.description`과 `youtube[].comments[].text`를 직접 읽고 **사람이 신호와 노이즈를 걸러야 한다**
- 광고 쇼츠(댓글이 전부 "이거 어디서 사요")는 무신호 — 위시리스트/댓글모음 포맷이 신호 밀도 압도적

### 5-3. 일본 커뮤니티 교차검증 (건너뛰지 말 것)

Yahoo!知恵袋 무료 API는 없음(2017년 유료화). 대신 웹 검색 사용:

1. 웹 검색: `{연령} {성별} 誕生日プレゼント 知恵袋` 형태로 검색
2. 개별 스레드 URL 열어서 질문/답변 내용 확인
3. 한일 양쪽 독립 신호로 나오는 카테고리 = 신뢰도 상승
4. **브랜드명 이식 금지** → 한국 대체 브랜드로 치환
5. **금액 맥락 확인 필수** — 생일선물 vs 사은품/답례품은 자릿수가 다름
6. **`blog.naver.com`은 웹페이지 읽기 도구로 열리지 않음** (차단) — 검색 API 스니펫만으로 판단

### 5-4. 상품 교차매칭

여론 수집에서 뽑은 카테고리를 네이버쇼핑 API로 재검색:

```javascript
const url = 'https://openapi.naver.com/v1/search/shop.json?query=' +
  encodeURIComponent(keyword) + '&display=5&sort=sim';
fetch(url, {
  headers: {
    'X-Naver-Client-Id': clientId,
    'X-Naver-Client-Secret': clientSecret
  }
});
```

응답 필드: `title`(HTML태그 제거 필요), `lprice`, `link`, `image`, `mallName`.

**⚠️ 이걸로 여러 번 틀렸다 — 반드시 확인할 것**:
- `title`에 HTML 태그(`<b>`)가 포함돼 있음 → 반드시 제거
- 검색 결과 여러 개 중 **상품명과 가격이 1:1로 매칭되는지 재확인**
  - 실제 사고: "크래프트 크러쉬 팔찌 메이커" 이름에 다른 상품(27,300원) 가격을 잘못 붙임
  - 실제 사고: "에어팟4 ANC" 이름에 ANC 없는 기본형 가격(170,640원)을 잘못 붙임
- **확정 전에 검색 결과 원본을 다시 한번 대조하는 습관**

**리뷰수·평점**: 네이버쇼핑/쿠팡 API 모두 리뷰수·평점을 주지 않는다. "리뷰 2,500개, 평점 4.8" 같은 건 **자동 수집 불가** — 만들어내지 말 것. 항상 실제 블로그/유튜브 수집 데이터에 기반해야 함.

### 5-5. 큐레이션 승인 세션

후보 5~7개를 다음 형식의 표로 정리해서 **사용자에게 승인받는다.**

| 순위 | 상품명 | 가격 | 근거(출처) | 추천 이유 |
|------|--------|------|-----------|----------|
| 1 | ... | ... | 네이버 블로그 O곳, 유튜브 댓글 O건 | ... |

**제외한 후보와 그 이유도 같이 보여줄 것.** 이 단계가 "사람이 골랐다"는 느낌을 주는 핵심.

> **⚠️ 함정: Python push 스크립트에서 설명을 `...`으로 축약하지 말 것**
> `.mjs` 파일의 원문을 그대로 복사해서 `p('...')`에 넣어야 한다.
> 줄여서 쓰면 Notion에 짧은 내용만 들어가서 라이브에 반영된다.
> push 전에 `.mjs` 파일의 description 길이와 push 스크립트의 description 길이를 비교할 것.
> 사용자가 승인하면 그 즉시 5-6(본문작성) → 5-7(검증) → 5-8(배포)까지 전부 실행한다.
> "푸시할까요?" 같은 확인을 다시 묻지 않고 한 번에 끝까지 간다.

### 5-6. 본문 작성 + Notion 반영

`scripts/content/guides/13세-여자아이-생일선물.mjs`를 열어 구조 참고해서 새 파일 생성:

```javascript
// scripts/content/guides/{슬러그}.mjs
import { h2, h3, p, bullet, table } from '../lib.mjs';

export const slug = '{슬러그}';
export const intro = '...';        // 리드문 200자 내외, Notion intro 속성
export const blocks = [ ... ];      // 본문 블록 배열 (PLAYBOOK 5절 템플릿)
export const products = [ ... ];    // { name, price, naverUrl, coupangUrl?, imageUrl, rank, pros }
```

본문 템플릿 구조(가격대별 표 → 고르는 법 유형분기 → 사지 마세요 → FAQ)는 `CONTENT-PLAYBOOK.md` 5절 참고.

작성 후 실행:
```bash
node scripts/content/push.mjs {슬러그}
```

> **참고**: `--env-file` 플래그 없이 실행한다 (`push.mjs`가 내부에서 .env를 직접 읽음).

**push.mjs가 하는 일**: Notion GiftGuides에서 슬러그로 페이지 찾기 → intro 갱신 → 기존 본문 블록 전부 삭제 → 새 블록 추가 → 기존 연결 Products 아카이브 → 새 상품 생성.

**재실행 안전**: 기존 블록/상품을 지우고 새로 채우는 방식이므로 여러 번 실행해도 문제없음.

### 5-6b. 캐시 갱신 (필수 — 빌드가 캐시를 사용함)

```bash
python scripts/_dump_notion_cache.py
```

> 이 프로젝트는 `@notionhq/client` 라이브러리가 Windows 환경에서 Notion API 연결에 실패하는 문제가 있다.
> 해결책으로 `src/data/notion-cache.json`(Python으로 생성)을 빌드 시 읽어서 fallback한다.
> **Notion에 가이드를 반영한 후에는 반드시 캐시를 재생성해야 빌드가 최신 데이터를 반영한다.**
> Note: 이 스크립트는 임시 디버그용이며, 다음 작업자가 `scripts/` 내에 캐시 생성 전용 스크립트를 만들 예정.

### 5-7. 검증

```bash
npm run build
```

빌드 후 `dist/선물/{슬러그}/index.html`을 열어서 확인:
- `class="product-card"` 개수 == `products` 배열 길이
- `<table>` 태그 존재 확인 (가격대별 표 렌더링)
- 본문 텍스트가 의도대로 나왔는지 스크롤 확인

확인 명령어:
```bash
grep -c 'product-card' dist/선물/{슬러그}/index.html
grep -c '<table' dist/선물/{슬러그}/index.html
wc -c dist/선물/{슬러그}/index.html
```
2000바이트 미만이면 본문이 너무 얇은 것 — 재점검.

### 5-8. 배포

```bash
# 1) GitHub 푸시 (GitHub Actions 자동 배포 트리거)
git add -A -- ':!.env'
git commit -m "{슬러그} 큐레이션 완료: 상품 N개, 본문 재작성"

# 2) 원격 커밋 확인 (절대 건너뛰지 말 것!)
git fetch origin && git log --oneline master..origin/master
# ← 낯선 커밋이 보이면 아래 "비상 대응" 절차 따를 것

# 3) push (자동 배포 트리거)
git push origin master
```

**비상 대응 — 원격에 낯선 커밋이 있을 때:**
1. 절대 `git push --force` 하지 않음
2. `git merge origin/master` 로컬에서 먼저 병합 시도
3. 충돌 발생 시 두 세션의 의도 파악 (같은 파일의 다른 부분을 고친 거면 단순 병합)
4. 사용자에게 "다른 세션에서 작업한 커밋이 있습니다. 병합해도 될까요?" 확인
5. 실제 사례: 원격에 70개+ 커밋(98개 가이드 쿠팡 상품 채우기)이 쌓여 있었고, 충돌은 `src/lib/notion.ts` 한 곳(재시도 로직 vs 테이블 지원)뿐이었음

### 5-9. wrangler 직접 배포 (GitHub Actions 실패 시 Fallback)

```bash
npx wrangler pages deploy dist --project-name=gift-infoepic --branch=master
```

**⚠️ 중요**: `--branch` 플래그 없이 배포하면 **프리뷰 배포**만 생성됨. 반드시 `--branch=master`를 붙여서 프로덕션에 배포할 것. (5월에 실제로 이 문제로 하루 동안 프로덕션 업데이트 안 됐음)

---

## 6. GSC(Google Search Console) 모니터링 절차

> **왜 필요한가**: 큐레이션 우선순위를 GSC 데이터로 결정하기 때문. 노출은 되는데 클릭 안 되는 가이드가 1순위.

### 6-1. GSC 데이터 읽는 법 (수동)
1. https://search.google.com/search-console 접속 → gift.infoepic.com 선택
2. **성과 → 검색결과** 탭
3. **쿼리 탭**: 어떤 검색어로 노출되는지 확인 (데이터 내보내기 가능)
4. **페이지 탭**: 어떤 페이지가 노출/클릭 많은지 확인
5. 필터: `날짜=최근 3개월`, `국가=대한민국`

### 6-2. GSC 기반 우선순위 결정
- **노출↑ 클릭↓** (CTR < 2%): 본문이 얇아서 검색결과에서 선택받지 못함 → **1순위 큐레이션**
- **노출↑ 클릭↑**: 잘 나가는 페이지 — 유지보수만
- **노출↓ 클릭↓**: 검색어 볼륨 자체가 적음 — 후순위
- **CTR 5%+**: 제목·설명이 잘 최적화된 페이지 — 좋은 신호

### 6-3. 키워드 발견 → 신규 가이드 기획
GSC에서 **기존 가이드에 없는 키워드**로 노출이 발생하면:
1. 해당 키워드로 새 가이드를 만들 가치가 있는지 판단
2. 기존 가이드와 카니발라이제이션(검색어 잠식)이 발생할지 검토
3. 신규 가이드 작성은 별도 승인 필요 (사용자 확인)

### 6-4. 큐레이션 효과 측정
- 큐레이션 완료 후 **2주~1개월 후 GSC 재확인**
- 해당 페이지의 노출 유지 + CTR 상승 = 효과 있음
- 노출 감소 = 뭔가 잘못됨 (본문 변경으로 검색 순위 하락 가능)

---

## 7. 사이트 성장 전략 로드맵

### Phase A: 콘텐츠 퀄리티 (지금)
큐레이션 파이프라인으로 96개 가이드를 전환하는 게 현재 유일한 우선순위.

**목표**: 1순위 가이드(키즈 클러스터 12~14개) → 2순위(검색량 높은 나머지) → 전수

### Phase B: 트래픽 확보 (큐레이션 20개+ 완료 후)
- [ ] 쿠팡 파트너스 API 활성화 (`.env` 키 채우기 + `npm run build`)
- [ ] Google Search Console 주기적 확인 (월 1회)
- [ ] 네이버 웹마스터도구에서 sitemap 재제출
- [ ] GA4로 방문자 트래픽 모니터링 시작

### Phase C: 수익화 (월 방문자 1K+ 도달 시)
- [ ] 구글 애드센스 신청 (또는 카카오 애드핏)
- [ ] 쿠팡 파트너스 링크 활성화 (상품 링크에 자동 추적 파라미터)
- [ ] 수익 데이터 기반으로 상위 트래픽 가이드 추가 큐레이션

### Phase D: 확장 (월 방문자 10K+ 도달 시)
- [ ] 계절·시즌 가이드 추가 (추석, 설날, 발렌타인데이 — 현재 존재하나 본문 보강 필요)
- [ ] 아이템별 가이드 확장 (책, 향수 등 — 현재 있음)
- [ ] Firebase 댓글·위시리스트 기능
- [ ] 인스타그램/핀터레스트 채널 개설

**성장 지표 목표**:
| 지표 | 현재 | 1개월 | 3개월 |
|------|------|-------|-------|
| 큐레이션 완료 | 2/96 | 20/96 | 60/96 |
| GSC 색인 페이지 | — | 전체 | 전체 |
| 평균 본문 길이 | 372자 | 1,500자+ | 2,000자+ |

---

## 8. 알아두면 좋은 배경 지식

### Notion 관련
- **Products DB의 타이틀 속성명은 `Title`이지 `Name`이 아니다.** `parseProduct`에서 `p.Name`을 읽다가 상품명이 항상 빈 문자열이었던 버그 — 이미 고침.
- Notion 속성명을 코드에 하드코딩할 때는 실제 DB 스키마를 먼저 확인할 것. `notion.databases.retrieve`가 이 워크스페이스에서 deprecated 에러를 내므로, raw fetch에 `Notion-Version: 2022-06-28` 헤더를 명시해서 스키마 조회.
- **Notion 테이블 블록 렌더링**을 `src/lib/notion.ts`에 새로 추가함. 예전엔 표가 사이트에서 무시됐는데 지금은 정상 렌더링.
- `getGuideContent`에 **재시도(3회, 지수 백오프) + 전체 페이지네이션** 로직 있음. 블록 100개 넘어도 안전.

### 배포 관련
- GitHub Actions (`.github/workflows/`)가 master push 시 자동 빌드+배포
- wrangler 직접 배포는 fallback용
- `dist/`는 `.gitignore`에 포함됨 (git 추적 안 됨)

### 콘텐츠 관련
- 사이트 URL 패턴: `https://gift.infoepic.com/선물/{슬러그}/`
- RSS: `https://gift.infoepic.com/rss.xml`
- 사이트맵: `https://gift.infoepic.com/sitemap-index.xml`
- `/나이/`, `/관계/`, `/상황/`, `/예산/`, `/아이템/`, `/초보/` 필터 페이지 존재 — 각각 필터링된 가이드 목록

### ⚠️ 함정 모음 (이미 겪은 것들)

| 함정 | 설명 | 해결/회피 |
|------|------|----------|
| **원격 커밋 충돌** | 다른 세션(사람 자동화 등)이 먼저 푸시한 커밋을 모르고 push하려다 발견 | push 전 `git fetch + git log master..origin/master` **필수** |
| **상품명-가격 오매칭** | 네이버쇼핑 검색 결과에서 상품명과 가격이 다른 상품 것일 수 있음 | 검색 결과 원본 재확인 습관 |
| **Notion 속성명 불일치** | `Name` vs `Title` | DB 스키마 먼저 조회 |
| **blog.naver.com 차단** | 웹 페이지 읽기 도구로 못 읽음 | 검색 API 스니펫만으로 판단 |
| **금액 맥락 혼동** | 일본 知恵袋에서 생일선물 vs 사은품 예산 자릿수 다름 | 스레드 제목+질문 내용 반드시 확인 |
| **wrangler 배포 브랜치** | `--branch` 없으면 프리뷰 배포만 됨 | `--branch=master` 명시 |
| **`.env` git 추적** | `.env`는 커밋하면 안 됨 | `git add -A -- ':!.env'` 패턴 고정 |
| **에어팟 모델명 혼동** | "에어팟4 ANC"와 "에어팟4"는 다른 제품, 다른 가격 | 검색 결과에서 정확한 모델명 확인 |
| **연령 키워드 노이즈** | "13세" 검색 시 육아용품 사이즈표에 낚임 | "중학생" 같은 학년 키워드로 대체 |

---

## 9. 다음에 할 일 (우선순위)

1. **10세-남자아이-생일선물** — 위 5절 절차 그대로 실행
2. **10-12세-남자아이-생일선물** — 10세 완료 후 카니발라이제이션 판단 (병합 or canonical)
3. **이후 GSC 노출 상위 키즈 클러스터** 나머지 순회 (7-9세, 14-15세, 16-19세 등)
4. **필터 페이지 본문 보강** — `/나이/`, `/관계/` 등에 500자+ 선택법 텍스트 추가 (모든 큐레이션 완료 후)
5. **전체 큐레이션 완료 후** — 쿠팡 API 활성화 + GA4 분석 시작

---

> **마지막으로**: 이 문서는 Claude뿐 아니라 어떤 AI 도구(Copilot, ChatGPT, Gemini 등)로도 실행할 수 있게 쓰여졌다. 설정·메모리·프로젝트 규칙에 의존하지 않고, 저장소의 파일만으로 작업 재개가 가능하다.
>
> 다음 작업자는 `CONTENT-PLAYBOOK.md` 8절 표에서 다음 순서를 확인하고, 위 5절 절차(5-1 ~ 5-9)를 따라가면 된다.
