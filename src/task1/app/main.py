import re


def mask_string(input_string: str) -> str:
    # Функция для маскировки текста
    def mask_text(text: str) -> str:
        # Символы, которые не будут заменяться
        allowed_chars = ",.()<>[]`'\":;@!?-+=/|~ "
        # Маскируем символы
        return "".join(char if char in allowed_chars else "*" for char in text)

    # Регулярное выражение для поиска блоков [mask][/mask]
    pattern = re.compile(r"\[mask\](.*?)\[/mask\]", re.IGNORECASE)

    # Функция замены, которая будет вызываться для каждого найденного блока
    def replacement(match):
        st = match.group(0)
        return st[:6] + mask_text(st[6:-7]) + st[-7:]

    # Замена всех найденных блоков в строке
    masked_string = pattern.sub(replacement, input_string)
    return masked_string


if __name__ == "__main__":
    input_string = (
        "[mask][/mask], a[mask][/mask], [mask][/mask]b, a[mask][/mask]b, [MASK][/MASK]"
    )
    masked_output = mask_string(input_string)
    print(masked_output)
