'''import robdd as ROBDD

if __name__ == "__main__":
    #bdd = ROBDD.BDD()

'''

import re
import robdd as ROBDD

# define a regular expression that matches variables, constants, and operators
token_pattern = re.compile(r'\bTrue\b|\bFalse\b|\b[A-Za-z]+\b|\S')

# tokenize the expression
expression = "((x & y) | (y ^ z) & (x | z))"
tokens = token_pattern.findall(expression)
#print(tokens)
bdd = ROBDD.BDD()
