import { stripHtml } from './lib.mjs';

// 네이버 블로그 검색 API — 공식 API, 스니펫(제목+요약)만 반환
export async function searchNaverBlog(keyword, display = 20) {
  const clientId = process.env.NAVER_CLIENT_ID;
  const clientSecret = process.env.NAVER_CLIENT_SECRET;

  if (!clientId || !clientSecret) {
    console.warn('[naver-blog] NAVER_CLIENT_ID/SECRET 없음 — 건너뜀');
    return [];
  }

  const url = `https://openapi.naver.com/v1/search/blog.json?query=${encodeURIComponent(keyword)}&display=${display}&sort=sim`;

  const res = await fetch(url, {
    headers: {
      'X-Naver-Client-Id': clientId,
      'X-Naver-Client-Secret': clientSecret,
    },
  });

  if (!res.ok) {
    console.warn(`[naver-blog] ${res.status} ${res.statusText}`);
    return [];
  }

  const data = await res.json();
  return (data.items ?? []).map((item) => ({
    title: stripHtml(item.title),
    description: stripHtml(item.description),
    link: item.link,
    bloggerName: item.bloggername,
    postDate: item.postdate,
  }));
}
