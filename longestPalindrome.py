def longest_palindrome(s):
    s1 = s.lower()
    for length in range(len(s), -1, -1):
        for times in range(len(s) - length + 1):
            string = s1[times:times+length]
            if string == string[::-1]:
                return string
    return 0

print("返回值")
print(longest_palindrome("$aaabbbccddd_!jJpqlQx_.///yYabababhii_"))
