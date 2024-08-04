from fastapi import APIRouter

from src.task3.app.services.test_request import redirect
from src.task3.app.services.parser import parse_google_results


router = APIRouter()




@router.get('/')
def get_request(q) -> int:
    print(type(q))
    print(q)
    query = q
    res = redirect(query)
    html = res.text
    # with open('test.html', 'w', encoding='UTF-8') as f:
    #     f.write(html)
    answer = parse_google_results(html)
    return answer


