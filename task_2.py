
def interaction():
    a = int(input('Vvedite A: '))
    b = int(input('Vvedite B: '))
    print(f"Result = {summa(a,b)}")

def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a

interaction()