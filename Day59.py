word = input("check if palindrome: ")


def checkPalindrome(word):
    if len(word) <= 1:
        return True
 
    if word[0] != word[-1]:
        return False
    
    return checkPalindrome(word[1:-1])
    


print(checkPalindrome(word))