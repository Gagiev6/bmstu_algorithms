def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1

    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))
string3 = "hello"
string4 = "world"
print(are_anagrams(string3, string4))