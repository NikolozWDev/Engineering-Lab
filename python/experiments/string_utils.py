def reverse_words(text):
    words = text.split()
    return ' '.join(words[::-1])

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for c in text.lower() if c in vowels)

def capitalize_sentences(text):
    sentences = text.split('. ')
    capitalized = [s[0].upper() + s[1:] if s else s for s in sentences]
    return '. '.join(capitalized)

def remove_duplicates(text):
    seen = set()
    result = []
    for char in text:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def truncate(text, max_length, suffix='...'):
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def slugify(text):
    slug = text.lower().strip()
    slug = ''.join(c if c.isalnum() else '-' for c in slug)
    slug = '-'.join([part for part in slug.split('-') if part])
    return slug

def word_count(text):
    return len(text.split())

def character_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalnum():
            freq[char] = freq.get(char, 0) + 1
    return freq

if __name__ == "__main__":
    sample = "Hello World! This is a Test String."
