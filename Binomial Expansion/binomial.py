from math import factorial as f
def c(n: int, r: int) -> int:
    """Calculates n choose r (nCr)"""
    if r == 0: return 1
    return f(n) // (f(r) * f(n - r))

def expand(expr: str) -> str:
    eqn, exp = expr[1:expr.index(")")], int(expr.split("^")[-1])

    for ind, i in enumerate(eqn):
        # If i is a letter, we have located the variable!
        if i.isalpha():
            a, b, var = eqn[:ind], eqn[ind + 1:], i
            break

    a = {"-":-1,"":1}[a] if a in ("-", "") else int(a)
    b = int(b)

    # do expansion algorithm
    if exp == 0: return "1"
    ret = ""
    for i in range(exp+1):
        coeff = c(exp, i) * b**i * a**(exp-i)
        ret += f"+{coeff}{var}^{exp-i}"

    # Remove unneeded stuff like x^0 and coefficients of 1
    ret = ret.replace(f"{var}^0", "").replace(f"^1", "").replace("+-", "-").replace(f"-1{var}", f"-{var}").replace(f"+1{var}", f"{var}")
    ret = ret[1:] if ret[0] == "+" else ret
  
    return ret

if __name__ == "__main__":
    expression = input("Enter an expression in the form (ax+b)^n: ")
    try:
        print(expand(expression))
    except Exception as err:
        print(f"An error occured. Make sure you are the format of (ax+b)^n. \nError: {err}")