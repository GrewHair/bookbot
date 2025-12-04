def get_num_words(text):
    return len(text.split())

def get_char_counts(text):
    char_counts = {}
    for char in "abcdefghijklmnopqrstuvwxyz ":
        char_counts[char] = 0
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
    return char_counts

def sort_on(items):
    return items["num"]

def get_sorted_char_counts(char_counts):
    char_counts = [{"char": k, "num": v} for k, v in char_counts.items()]
    char_counts.sort(reverse=True, key=sort_on)
    return char_counts
