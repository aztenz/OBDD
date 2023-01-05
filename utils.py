import string
import re


def getVars(expression: str) -> list:

    expression = expression.replace(
        ' ', '').replace(
            '!', '').replace(
                '+', '')
    
    varsList = [*expression]
    res = list(set(varsList))
    res.sort()
    return res


def getRules(expression: str) -> list:
    expression = expression.replace(
        ' ', '')
    return expression.split('+')


def parseExp() -> list:
    exp: str = input(
        "Enter your expression in the form (a + !b + a!b!c + ... ):")
    parseCheck = re.match(
        '^([A-Za-z]|![A-Za-z])+( \+ {1}([A-Za-z]|![A-Za-z])+)*$', exp)
    while (not parseCheck):
        print("\nExpression syntax Error!\n")
        exp = input("Please Enter your expression again:")
        parseCheck = re.match(
            '^([A-Za-z]|![A-Za-z])+( \+ {1}([A-Za-z]|![A-Za-z])+)*$', exp)
    return [getVars(exp), getRules(exp)]
