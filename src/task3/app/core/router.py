from fastapi import APIRouter

from src.task3.app.services.test_request import redirect
from src.task3.app.services.parser import parse_google_results


router = APIRouter()




@router.get('/')
async def get_request():
    response = redirect('vbirf')
    answer = parse_google_results(response)
    return answer


