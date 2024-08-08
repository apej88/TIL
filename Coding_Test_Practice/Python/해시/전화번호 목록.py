def solution(phone_book):
    phone_book.sort()
    phone_map = {}
    for number in phone_book:
        temp = ""
        for digit in number:
            temp += digit
            if temp in phone_map:
                return False
        phone_map[number] = True
    return True