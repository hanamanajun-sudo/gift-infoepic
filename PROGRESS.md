# PROGRESS

## 2026-06-25

### 오늘 한 일

**네이버 서치콘솔 소유 확인 문제 해결**

- HTML 파일(`public/naver...html`) 소유 확인 시도 시 커스텀 도메인(`gift.infoepic.com`)에서 404, `main.gift-infoepic.pages.dev` 서브도메인에서는 정상 접근되는 현상 확인
- `astro.config.mjs`의 `trailingSlash: 'always'` → `'ignore'` 변경, 캐시 삭제 등 시도했으나 미해결
- 근본 원인 파악: `wrangler pages deploy --branch=main`으로 배포하면 **프리뷰 배포**만 생성되어 `main.xxx.pages.dev`에는 반영되지만, 커스텀 도메인이 서빙하는 **프로덕션 배포**는 갱신되지 않음
- 브랜치 플래그 없이 재배포(`wrangler pages deploy dist --project-name=gift-infoepic`)하여 프로덕션 갱신, 네이버 확인 파일 200 OK 확인
- 네이버 서치콘솔 소유 확인 완료, `sitemap-index.xml` 제출 안내

---

### 완료된 항목

- [x] gift.infoepic.com 네이버 서치콘솔 소유 확인 완료
- [x] 프로덕션 미반영 원인 파악 (`--branch` 플래그 문제)
- [x] sitemap-index.xml 서치콘솔 제출 안내

---

### 다음에 할 일

- [ ] 앞으로 배포 시 `--branch` 플래그 없이 배포하고, 커스텀 도메인에서 반영 여부를 직접 확인하는 습관화
- [ ] 서치콘솔 색인 현황 주기적 확인

---

## 2026-05-27

### 오늘 한 일

**쿠팡 파트너스 API 연동 구현 (보류 상태로 완성)**

- `src/lib/coupang.ts` 생성
  - HMAC-SHA256 인증 구현 (2자리 연도 형식 `YYMMDDTHHmmssZ`)
  - 검색 API 호출 (`/products/search`)
  - 분당 50회 제한 대응: 1.5초 간격 직렬 큐 구현
  - 빌드 간 재사용을 위한 7일 캐시 (`src/data/coupang-cache.json`)

- `src/pages/선물/[slug].astro` 수정
  - 가이드 키워드(관계 + 상황 + "선물") 기반 자동 검색
  - 빌드 시점에 쿠팡 상품 fetch → "쿠팡 실시간 추천 상품" 그리드 섹션 추가

- API 키 제거 결정
  - 트래픽 없는 상태에서 어필리에이트 링크 과다 → 구글 저품질 위험
  - `.env`의 키값 비움 → 쿠팡 섹션 자동 비활성화 상태

---

### 완료된 항목

- [x] 쿠팡 API HMAC 인증 완성 (401 해결)
- [x] Rate limit 대응 큐 구현 (403 대응)
- [x] 캐시 레이어 구현 (반복 빌드 시 API 호출 0회)
- [x] 가이드 페이지 쿠팡 상품 섹션 UI 완성
- [x] 현재 가이드 총 86개 확인

---

### 다음에 할 일

**콘텐츠 우선 (트래픽 확보 전까지)**

- [ ] 가이드 100개 목표 달성 (현재 86개 → 14개 추가 필요)
- [ ] 기존 가이드 본문 콘텐츠 충실하게 채우기 (Notion 편집)
- [ ] 구글 서치 콘솔 색인 상태 점검

**쿠팡 API 활성화 (트래픽 확보 후)**

- [ ] `.env`에 API 키 재입력
- [ ] `npm run build` 실행 (첫 빌드 약 2분, 이후 캐시 사용)
- [ ] 쿠팡 Search API Rate limit 주의: 분당 50회, 위반 1회 누적 중 (3회 시 계정 제한)
  - 다음 빌드 가능 시각: 2026-05-28 오후 3시 25분 이후
