
def calcLogic(exp1: bool, and0Or1: int, exp2: bool) -> bool:
    if and0Or1 == 0:
        return exp1 and exp2
    elif and0Or1 == 1:
        return exp1 or exp2
