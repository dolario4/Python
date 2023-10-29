def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha() and char.islower():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency = {}
    for letter, count in letter_count.items():
        freq = round(count / total_letters, 2)
        frequency[letter] = freq
    return frequency



text = "оставь надежду всяк сюда входящий"
letters = count_letters(text)
frequency = calculate_frequency(letters)

for letter, freq in frequency.items():
    print(f"{letter}: {freq}")
