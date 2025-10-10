def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_sorted_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if not lowered.isalpha():
            continue
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    chars = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

    for k, v in chars.items():
        print(f"{k}: {v}")
    return chars
