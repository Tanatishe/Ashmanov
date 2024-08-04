from src.task3.app.services.test_request import redirect

from src.task3.app.services.parser import parse_google_results




respons = redirect('Мишка гений cerf')


# with open('test.html', 'w', encoding='UTF-8') as f:
#     f.write(respons.text)


answer = parse_google_results(respons.text)



print(answer)


