"""
This is a shortened version of the binomial expansion code
that I created for fun :D

This is purely the function so running this file will not
have any result!
"""
from math import factorial as f
def expand(expr):
    eqn, exp = expr[1:expr.index(")")], int(expr.split("^")[-1])
    for ind, i in enumerate(eqn):
        if i.isalpha(): a, b, var = eqn[:ind], int(eqn[ind + 1:]), i; break
    a = {"-":-1,"":1}[a] if a in ("-", "") else int(a); ret = "".join([f"+{(lambda n,r: f(n) // (f(r) * f(n - r)) if r != 0 else 1)(exp, i) * b**i * a**(exp-i)}{var}^{exp-i}" for i in range(exp+1)]).replace(f"{var}^0", "").replace(f"^1", "").replace("+-", "-").replace(f"-1{var}", f"-{var}").replace(f"+1{var}", f"{var}"); return ret[1:] if ret[0] == "+" else ret