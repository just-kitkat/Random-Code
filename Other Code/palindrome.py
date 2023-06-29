def check(s: str) -> str:
    s = s.lower().replace(" ", "")
    if len(s)%2==0:
        check = s[:len(s)//2] == (s[len(s)//2:])[::-1]
    else:
        check = s[:len(s)//2+1] == (s[len(s)//2:])[::-1]
    return "It's a palindrome" if check else "It's not a palindrome"

"""
Better way to check:
# Check s == s[::-1] (s reversed) instead of splitting str in half
return s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]
"""

print(check("Ten animals I slam in a net"))
print(check("Eleven animals i slam in a net"))
print(check("arlra"), check("araa"))