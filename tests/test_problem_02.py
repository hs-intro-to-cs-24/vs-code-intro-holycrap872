from problems.problem_02 import first_and_last_letter


def test_first_and_last_letter_1() -> None:
    assert first_and_last_letter("y") == "too short"


def test_first_and_last_letter_2() -> None:
    assert first_and_last_letter("") == "too short"


def test_first_and_last_letter_3() -> None:
    assert first_and_last_letter("umbrella") == "ua"


def test_first_and_last_letter_4() -> None:
    assert first_and_last_letter("yolo") == "yo"
