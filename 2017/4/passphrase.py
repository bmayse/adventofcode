def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line


def passphrase_contains_no_duplicates(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))


def passphrase_contains_no_anagrams(passphrase):
    words = passphrase.split()
    return len(words) == len(set(str(sorted(word)) for word in words))


def count_passphrases_from_file_that_meet_criteria(filename, meets_criteria):
    return len(list(filter(meets_criteria, (line for line in read_file(filename)))))


def count_passphrases_without_duplicates(filename):
    return count_passphrases_from_file_that_meet_criteria(filename, passphrase_contains_no_duplicates)


def count_valid_passphrases(filename):
    return count_passphrases_from_file_that_meet_criteria(filename, passphrase_contains_no_anagrams)
