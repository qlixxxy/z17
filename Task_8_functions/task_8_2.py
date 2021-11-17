
words = ['шалаш', 'лещ', 'казак', 'шапка']

def palindrome(text):
    new_text = [i for i in text]
    new_text.reverse()
    reversed_text = ''.join(new_text)
    if reversed_text == text:
        return True
    return False

for i in words:
    print(palindrome(i))
