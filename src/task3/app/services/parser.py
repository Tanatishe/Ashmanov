from bs4 import BeautifulSoup


def parse_google_results(html: str) -> int:
    soup = BeautifulSoup(html, "html.parser")
    result_stat = soup.find("div", {"id": "result-stats"})

    if result_stat:
        text = result_stat.text
        ind = text.find("(")
        srez = text[:ind]
        answer = int("".join(i for i in srez if i.isdigit()))
        return answer
    return 0
