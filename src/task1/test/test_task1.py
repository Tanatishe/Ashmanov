import pytest
from src.task1.app.main import mask_string




def test_task1_1():
    test_string = "Спасибо за вопрос, [Mask]ваш pin(секрет): 123-412.[/mask]. Приятных покупок!')"
    assert mask_string(test_string) == "Спасибо за вопрос, [Mask]*** ***(******): ***-***.[/mask]. Приятных покупок!')"


def test_task1_2():
    test_string = ""
    assert mask_string(test_string) == ""