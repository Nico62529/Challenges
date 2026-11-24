# Ejercicio 1

def al_menos_una_verdadera(PrimerValor: bool, SegundoValor: bool):
    if PrimerValor == True or SegundoValor == True:
        return True

    return False

# Ejercicio 2

def multiply_by_scalar(numbers: list[int], scalar: int) -> list[int]:
    Answers = []
    for i in numbers:
        Answers.append(i*scalar)

    return Answers

# Ejercicio 3

def get_digits(number: int) -> list[int]:
    digits = []

    text = str(number)
    for i in text:
        digits.append(int(i))
    return digits

# Ejercicio 4

def utils(a: float, b: float, op: str) -> float:
    # Implementa add, sub, mul y div según el valor de op

    if op == "add":
        return a+b
    elif op == "sub":
        return a-b
    elif op == "mul":
        return a*b
    elif op == "div":
        return a/b
    else:
        ValueError

    
    pass

# Ejercicio 5

def is_positive(value: int) -> bool:
    
    if value > 0:
        print(f"El numero {value} es mayor que 0")
        return True
    else:
        print(f"El numero {value} es menor que 0")
        return False

# Ejercicio 6

def starts_with(text: str, prefix: str) -> bool:

    if prefix == "":
        return True
    
    if len(text) < len(prefix):
        return False

    Constante = 0
    for i in text:
        for a in prefix:
            if i == a:
                Constante += 1
            elif i != a and Constante >= 1:
                return True
            else: 
                return False
            if i != a:
                return False

# Ejercicio 7

def is_integer(value: float) -> bool:

    if type(value) == int:
        return True
    else:
        return False



    


                    
