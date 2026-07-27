def isPalindrome(string):
    left_pos = 0
    right_pos = len(string)

    while right_pos > left_pos:
        if string[left_pos] != string[right_pos - 1]:
            return False
        left_pos += 1
        right_pos -= 1
    return True

print("Is this a palindrome?")
print(isPalindrome("racecar"))