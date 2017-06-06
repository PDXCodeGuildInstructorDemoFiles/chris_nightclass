fizz = lambda x: ((x % 3) == 0)
buzz = lambda x: ((x % 5) == 0)

def fiz_buzz(n):
    if fizz(n) or buzz(n):
        return (fizz(n) * 'fizz') + (buzz(n) * 'buzz')
    else:
        return n

print(fizz(3))
