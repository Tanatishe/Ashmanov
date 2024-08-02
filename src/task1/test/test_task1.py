
import re

def mask_string(input_string):
    # Функция для маскировки текста
    def mask_text(text):
        # Символы, которые не будут заменяться
        allowed_chars = set(",.()<>[]`'\":;@!?-+=/|~")
        # Маскируем символы
        return ''.join(char if char in allowed_chars else '*' for char in text)

    # Регулярное выражение для поиска блоков [mask][/mask]
    pattern = re.compile(r'\[mask\](.*?)\[/mask\]', re.IGNORECASE)
    
    # Функция замены, которая будет вызываться для каждого найденного блока
    def replacement(match):
        return '[mask]' + mask_text(match.group(1)) + '[/mask]'
    
    # Замена всех найденных блоков в строке
    masked_string = pattern.sub(replacement, input_string)
    return masked_string

# Пример использования
input_string = "Это тестовая строка [mask]Тест! 1234, пример.[/mask] И еще текст."
masked_output = mask_string(input_string)
print(masked_output)
