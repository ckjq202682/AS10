# AS10

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

string = input("Input string").lower()

def vowel(string):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(string)):
        if string[i] in vowels:
            count = count + 1
    if count >= 3:
        return True
    else:
        return False

def double(string):
    count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count = count + 1
    if count >= 1:
        return True
    else:
        return False

def illegal(string):
    count = 0
    bad = ["ab", "cd", "pq", "xy"]
    for i in range(len(string)):
        if string[i:i + 2] in bad:
            count = count + 1
    if count >= 1:
        return False
    else:
        return True


if vowel(string) is True and double(string) is True and illegal(string) is True:
    print("Nice string")
else:
    print("Naughty string")
