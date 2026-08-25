import re
from collections import Counter

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

def find_phone_numbers(text):
    pattern = r'\b(\+\d{1,3}[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b'
    return re.findall(pattern, text)

def find_urls(text):
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*'
    return re.findall(pattern, text)

def find_dates(text):
    pattern = r'\b\d{4}[-/]\d{2}[-/]\d{2}\b|\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def extract_numbers(text):
    pattern = r'-?\d+\.?\d*'
    return [float(x) for x in re.findall(pattern, text)]

def find_ip_addresses(text):
    pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(pattern, text)

def find_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

def find_mentions(text):
    pattern = r'@\w+'
    return re.findall(pattern, text)

def mask_sensitive_info(text):
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', text)
    text = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', text)
    text = re.sub(r'\b\d{3}[- ]?\d{2}[- ]?\d{4}\b', '[SSN]', text)
    return text

if __name__ == "__main__":
    sample_text = """
    Contact us at john.doe@example.com or support@company.org
    Call 555-123-4567 or (555) 987-6543
    Visit https://www.example.com/page?id=123
    Meeting on 2024-01-15 or 12/25/2024
    Server IP: 192.168.1.100
    Follow #python and @developer
    """
