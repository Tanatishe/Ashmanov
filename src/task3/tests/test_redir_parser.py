from src.task3.app.services.test_request import redirect
from src.task3.app.services.parser import parse_google_results


respons = redirect("Мишка гений cerf")

answer = parse_google_results(respons.text)


print(answer)
