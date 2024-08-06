from fastapi import APIRouter

from src.task3.app.services.redirect import redirect
from src.task3.app.services.parser import parse_google_results


router = APIRouter()


@router.get("/")
async def get_request(q) -> int:
    query = q
    html = await redirect(query)
    answer = parse_google_results(html)
    return answer
