from fastapi import APIRouter

from src.task3.app.services.test_request import redirect
from src.task3.app.services.parser import parse_google_results


router = APIRouter()




@router.get('/')
async def get_request(q):
    query = q
    response = redirect(query)
    html = response.text
    with open('test.html', 'w', encoding='UTF-8') as f:
        f.write(html)
    answer = parse_google_results(html)
    return answer


