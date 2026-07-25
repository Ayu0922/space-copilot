from fastapi import APIRouter
import httpx

router = APIRouter()

SPACEFLIGHT_API = "https://api.spaceflightnewsapi.net/v4/articles/"

@router.get("/news")
async def get_space_news(limit: int = 10):
    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
        resp = await client.get(SPACEFLIGHT_API, params={"limit": limit, "ordering": "-published_at"})
        resp.raise_for_status()
        data = resp.json()

    articles = []
    for item in data.get("results", []):
        articles.append({
            "title": item.get("title"),
            "summary": item.get("summary"),
            "url": item.get("url"),
            "image_url": item.get("image_url"),
            "published_at": item.get("published_at"),
            "news_site": item.get("news_site"),
        })

    return {"articles": articles, "total": len(articles)}