import random 

def user_guess(x): 
    number = random.randint(0,x)
    guess = -1 
    while guess != number: 
        guess = int(input(f"Adivinhe um número de 1 a {x}: "))
        if guess < number: 
            print("Você chutou um número muito baixo, tente novamente!")
        elif guess > number: 
            print("Você chutou um número muito alto, tente novamente!")

    print(f"PARABÉNS! VOCÊ CONSEGUIU ACERTAR O NÚMERO! ERA O NÚMERO {number}")

user_guess(500)

def computer_guess(x): 
    lower = 1
    higher = x
    answer = ""
    while answer != "c":
        if lower != higher:  
            number = random.randint(lower,higher)
        else: number = higher
        answer = input(f"O número {number} está correto (C)? Muito alto (A)? Ou Muito baixo (B)?: ").lower()
        if answer == "b": 
            lower = number + 1 
        elif answer == "a": 
            higher = number - 1
    print(f"UAU! CONSEGUI ACERTAR O NÚMERO {number}! PARABÉNS PRA MIM EU ACHO HAHA!")

computer_guess(500)
