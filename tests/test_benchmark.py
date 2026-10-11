from benchmark import normalize


def test_uppercase():
    assert normalize("abc123") == "ABC123"


def test_whitespace_and_punctuation():
    assert normalize("7 ABC-123") == "7ABC123"


def test_chinese_plate():
    assert normalize("京 A·12345") == "京A12345"


def test_sign_text():
    assert normalize("ROAD WORK AHEAD") == "ROADWORKAHEAD"
