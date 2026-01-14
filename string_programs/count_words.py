def count_words(text):
    words = text.split()
    return len(words)

sentence = "  Hello world! This is   a Python program.  "
word_count = count_words(sentence)

print(f"String: '{sentence.strip()}'")
print(f"Word Count: {word_count}")