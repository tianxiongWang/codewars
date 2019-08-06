def first_non_repeating_letter(string):
    s1 = string.lower()
    for letter in string:
        if letter == " ":
            continue
        if 97 <= ord(letter) <= 122:
            if s1.count(letter) == 1:
                return letter
        if 65 <= ord(letter) <= 90:
            if s1.count(chr(ord(letter)+32)) == 1:
                return letter
        else:
            if s1.count(letter) == 1:
                return letter
    return ""
    

if __name__ == "__main__":
    string =  'd5KHHd MuyJGW;Wj25,2A5z1Pa7697H5fg16cKXKtBenCVfku77mx49qKE'
    print(first_non_repeating_letter(string))