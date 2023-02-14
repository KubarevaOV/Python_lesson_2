def interaction():
    a = int(input('Vvedite A: '))
    b = int(input('Vvedite stepen: '))
    print(f"Result = {stepen(a,b)}")

def stepen(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * stepen(a, b-1)


interaction()