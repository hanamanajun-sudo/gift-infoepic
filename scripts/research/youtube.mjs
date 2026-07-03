import { sleep } from './lib.mjs';

const API_BASE = 'https://www.googleapis.com/youtube/v3';

// 영상 검색 (search.list = 100 유닛/호출 — 일 10,000 유닛 한도이므로 maxVideos를 낮게 유지)
async function searchVideos(keyword, apiKey, maxVideos = 5) {
  const url = `${API_BASE}/search?part=snippet&type=video&order=relevance&relevanceLanguage=ko&regionCode=KR&maxResults=${maxVideos}&q=${encodeURIComponent(keyword)}&key=${apiKey}`;

  const res = await fetch(url);
  if (!res.ok) {
    console.warn(`[youtube] search ${res.status} ${res.statusText}`);
    return [];
  }
  const data = await res.json();
  return (data.items ?? []).map((item) => ({
    videoId: item.id.videoId,
    title: item.snippet.title,
    channelTitle: item.snippet.channelTitle,
  }));
}

// 댓글 수집 (commentThreads.list = 1 유닛/호출)
async function fetchComments(videoId, apiKey, maxComments = 30) {
  const url = `${API_BASE}/commentThreads?part=snippet&order=relevance&maxResults=${maxComments}&videoId=${videoId}&key=${apiKey}`;

  const res = await fetch(url);
  if (!res.ok) {
    // 댓글 비활성 영상은 403 반환 — 정상 흐름이므로 조용히 스킵
    if (res.status !== 403) console.warn(`[youtube] comments ${res.status} ${res.statusText} (video ${videoId})`);
    return [];
  }
  const data = await res.json();
  return (data.items ?? []).map((item) => {
    const c = item.snippet.topLevelComment.snippet;
    return { text: c.textDisplay, likeCount: c.likeCount };
  });
}

export async function collectYoutubeOpinions(keyword, { maxVideos = 5, maxComments = 30 } = {}) {
  const apiKey = process.env.YOUTUBE_API_KEY;
  if (!apiKey) {
    console.warn('[youtube] YOUTUBE_API_KEY 없음 — 건너뜀');
    return [];
  }

  const videos = await searchVideos(keyword, apiKey, maxVideos);
  const results = [];

  for (const video of videos) {
    await sleep(300);
    const comments = await fetchComments(video.videoId, apiKey, maxComments);
    results.push({ ...video, comments });
  }

  return results;
}
