def palindrome_number(num):
    num = str(num)
    for x in range(len(num)):
        ls = len(num) - 1 - x 
        if num[x] != num[ls]:
            return False
    
    return True

palindrome_number(-121)
palindrome_number(121)
palindrome_number(12)