from task3.app.services.redirect import redirect
from src.task3.app.services.parser import parse_google_results


respons = redirect("test")

answer = parse_google_results(respons.text)


print(answer)
