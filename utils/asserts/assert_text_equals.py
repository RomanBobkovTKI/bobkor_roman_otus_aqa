def assert_element_text_equals(text, expected_text):
    actual = text.strip().lower()
    assert actual == expected_text.lower(), f"Ожидалось '{expected_text}', получено '{actual}'"