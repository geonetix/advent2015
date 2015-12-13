def nice_word(word):
    return all((has_vowels(word),
                has_doubles(word),
                has_no_naughty_combinations(word)))


def has_vowels(word):
    vowels = "aeiou"
    return len(filter(lambda x: x in vowels, word)) >= 3


def has_doubles(word):
    maxlen = len(word)
    for idx, c in enumerate(word):
        if idx + 1 >= maxlen:
            return False
        if c == word[idx + 1]:
            return True
    return False


def has_no_naughty_combinations(word):
    naughty_words = ('ab', 'cd', 'pq', 'xy')
    for naughty_word in naughty_words:
        if naughty_word in word:
            return False
    return True


def main():
    with open("data.txt", "rb") as rd:
        words = filter(nice_word, [x.strip() for x in rd])
        print words
    print "nice words:", len(words)


if __name__ == "__main__":
    main()
