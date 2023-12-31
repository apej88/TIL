def check_palindrome(text):
    p1, p2 = 0, len(text)-1

    while(p1 < p2):
        if(text[p1] != text[p2]):
            return False
        
        p1, p2 = p1 + 1, p2 -1
    
    return True