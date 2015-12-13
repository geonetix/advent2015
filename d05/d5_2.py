def nice_word(word):
    return all((has_pattern(word),
                has_sandwich(word)))


def has_pattern(word):
    maxlen = len(word)
    for idx, c in enumerate(word):
        if idx + 2 >= maxlen:
            return False
        set_ = c + word[idx+1]
        if set_ in word[idx+2:]:
            return True
    return False


def has_sandwich(word):
    maxlen = len(word)
    for idx, c in enumerate(word):
        if idx + 2 >= maxlen:
            return False
        if c != word[idx + 1] and c == word[idx + 2]:
            return True
    return False


def main():
    with open("data.txt", "rb") as rd:
        words = filter(nice_word, [x.strip() for x in rd])
    print "nice words:", len(words)


if __name__ == "__main__":
    main()
