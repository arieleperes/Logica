def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

print(soma(1,2,3,5,6))