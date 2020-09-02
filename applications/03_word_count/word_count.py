def word_count(s):
    webster = {}
    ignore_punc = '":;,.-+=/\|[]{}()*^&'

    # Chain strip of special characters
    s = s.lower().replace("\r", " ").replace("\n", " ").replace("\t", " ").split()

    for i in s:
        i = i.strip(ignore_punc)
        if i not in webster and i != "":
            webster[i] = 1
        elif i != "":
            webster[i] += 1
    return webster


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

