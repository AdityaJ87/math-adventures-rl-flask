import random

def generate_puzzle(difficulty: int):
    ops = ['+', '-', '*', '/']
    if difficulty == 1:
        ops = ['+', '-']
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    elif difficulty == 2:
        ops = ['+', '-', '*']
        a = random.randint(1, 20)
        b = random.randint(1, 12)
    else:
        a = random.randint(5, 50)
        b = random.randint(2, 20)

    op = random.choice(ops)
    if op == '-':
        a, b = max(a, b), min(a, b)
    elif op == '/':
        b = random.randint(2, 10)
        a = b * random.randint(2, 12)

    question = f"{a} {op} {b}"
    if op == '+': ans = a + b
    elif op == '-': ans = a - b
    elif op == '*': ans = a * b
    else: ans = a // b

    return question, ans