numbers = []

def is_even(num):
    return num % 2 == 0

def smallest_even():
    print("write 3 numbers")
    num1 = int(input())
    numbers.append(num1)
    
    num2 = int(input())
    numbers.append(num2)
    
    num3 = int(input())
    numbers.append(num3)
    
    even_numbers = filter(is_even, numbers)
    sorted_even_numbers = sorted(even_numbers)
    
    if len(sorted_even_numbers) > 0:
        smallest = min(sorted_even_numbers)
        print(smallest)
    else:
         print(None)
   
smallest_even()




# -------------



def team():
    players = 0
    names = ""

    while players < 5:
        name = str(input("enter player: "))
        names += name + " "
        players += 1
        
    print(names)    
    
team()

# In the line names += name + " ", names is a string variable that is being updated on each iteration of the while loop.
# The += operator is used to concatenate the current value of name with a space character " " and then add it to the end of the current value of names.
# So, for example, if the first name entered is "John", then names would become "John ". If the second name entered is "Mary", then names would become "John Mary ". And so on, until all 5 names have been entered.

# -------------------------

saludo = "multiplo de 5"

for i in range(10+1):
    if not i % 5:
        print(f"{i} {saludo}")
    elif i % 2:
        print(f"{i} impar")
    elif not i % 2:
        print(f"{i} par")


# ----------------


todas_notas = []

def add_nota():
    nota_input = str(input("write a note: "))
    todas_notas.append(nota_input)
#     global num
    
   
        

def initiate():
    add_nota()
    seguir = str(input("quieres seguir? si o no? "))
    if seguir == "si":
       initiate()
    elif seguir == "no":
       add_notassss = False 
        
    
initiate()


def imprimir_notas():
    print("sus notas son: ")
    num = 1
    for nota in todas_notas:
        print(f"{num} {nota}")
        num += 1

imprimir_notas()
    

eli = str(input("quieres eliminar una nota? "))
if eli == "si":
    numero = int(input("seleccione un numero: "))
    todas_notas.pop(numero - 1)
    print(todas_notas)

# ------------------------------------------------

num_to_guess = []

def game():
    first_person_num = int(input("Give me a number between 1 and 10: "))
    if first_person_num > 0 and first_person_num <= 10:
        num_to_guess.append(first_person_num)
        
    num_of_guesses = 3
    while num_of_guesses > 0:
        num_attempt = int(input("guess the num8er: "))
        if num_attempt in num_to_guess:
            print("you guessed!!")
            break
        
        num_of_guesses -= 1
        
    if num_of_guesses == 0:
       print(f"you lost!! the num8er was: {first_person_num}") 
            
game()


# -----------------------------------------------------------------------

# Write a function that takes a list of integers as a parameter
# and returns the max element in the list. Do NOT use the built-in max() function.

array = [2, 56, 90, 23, 100]

def max_num(arr):
    position = 0
    value_1 = arr[0]
    while position < len(arr):
        current_value = arr[position]
        if value_1 > current_value:
            position += 1
        else:
            value_1 = current_value
            position += 1
    print(value_1)
            
max_num(array)



# -----------------------------------------------------------------------

# Write a function my_len that takes as input a list a_list and returns the number
# of elements in that list (do not use the original len function, but implement your own way of counting the elements!).

array = [1, 4, 56, 2, 3, 4, 6]

def arr_length(arr):
    acumulator = 0
    for i in arr:
        acumulator += 1
    print(acumulator)
    
    
      
arr_length(array) 




# sum of all num8ers in an array

array = [10, 4, 6, 2, 10, 4, 6]

def arr_length(arr):
    acumulator = 0
    for i in arr:
        acumulator += i
    print(acumulator)
    
    
      
arr_length(array)