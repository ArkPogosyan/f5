def is_palindrome(text):
    cleaned_text = "".join(i for i in text.lower() if i.isalpha())

    return cleaned_text == cleaned_text[::-1]


txt = input()

print(is_palindrome(txt))
