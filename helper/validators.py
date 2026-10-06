import re

def is_email(value):
    return bool(re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', value or ''))

def is_phone(value):
    digits = re.sub(r'\D', '', value or '')
    return 7 <= len(digits) <= 15

def is_url(value):
    return bool(re.match(r'^https?://[^\s]+$', value or ''))

def is_ipv4(value):
    parts = (value or '').split('.')
    if len(parts) != 4:
        return False
    return all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

def is_strong_password(value):
    if not value or len(value) < 8:
        return False
    return (any(c.isupper() for c in value)
            and any(c.islower() for c in value)
            and any(c.isdigit() for c in value))
