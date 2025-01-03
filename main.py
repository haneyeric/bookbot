def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = count_words(file_contents)
    chars = count_chars(file_contents)
    sorted_chars = dict_to_list(chars)
    print("Number of words: ", words)
    for char in sorted_chars:
        if char["ch"].isalpha():
            print(char["ch"], " occured ", char["count"], " times")

def count_words(words):
    words = words.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    for ch in text:
        if ch.lower() not in char_counts:
            char_counts[ch.lower()] = 1
        else:
            char_counts[ch.lower()] += 1
    return char_counts

def sort_on(cdict):
    return cdict["count"]

def dict_to_list(cdict):
    clist = []
    for ch in cdict:
        clist.append({"ch": ch, "count": cdict[ch]})
    clist.sort(reverse = True, key=sort_on)
    return clist


main()

