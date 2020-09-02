def no_dups(s):
    webster = {}

    # Edge case (see the first test)
    if s == "":
        return ""

    # Split on spaces
    s = s.split(" ")

    # Add to webster only the words that don't exist in webster
    # (NO DUPLICATES)
    for i in s:
        if i not in webster:
            webster[i] = i

    # Get just the words from the dictionary
    lst = list(webster.keys())

    # Make into a string seperated by spaces
    s = " ".join(lst)

    # Fulfill MVP
    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
