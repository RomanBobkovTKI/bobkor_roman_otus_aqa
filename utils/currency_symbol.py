import re


def extract_currency_symbol(text):
    match = re.match(r"^([\$€£¥₽])", text.strip())
    return match.group(1) if match else None
