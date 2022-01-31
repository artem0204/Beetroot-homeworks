from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1:
        return True
    elif looking_str[0] == looking_str[-1] and len(looking_str) <= 3:
        return True
    elif looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False
