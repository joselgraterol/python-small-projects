# ask for 3 numbers
# print only the even numbers
# look for the smallest even

# version 1

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

# version 2

numbers = []
num_even = []


def create_array():
    num_asked = 3
    while num_asked > 0:
        num_input = int(input("give me 3 num8ers: "))
        numbers.append(num_input) 
        num_asked -= 1
    


def filter_even(arr_num, arr_even):
    for i in arr_num:
        if i % 2 == 0:
            arr_even.append(i)
            
def smallest_even(arr_even):
    position = 0
    value_1 = arr_even[0]
    while position < len(arr_even):
        current_value = arr_even[position]
        if value_1 < current_value:
            position += 1
        else:
            value_1 = current_value
            position += 1
    print(f"the smallest even num8er is {value_1}")
    
    
def app():
    create_array()
    filter_even(numbers, num_even)
    if len(num_even) > 0:
        smallest_even(num_even)
    
    
app()



# -------------

# ask for the name of 5 players and print them in a single line

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





# reverse an array

arr = [10, 200, -3, 40, 5]
reverse = []
negative = -1

for i in arr:
    reverse.append(arr[negative])
    negative -= 1

print(reverse)


# reverse a string


name = "jose"
name_reversed = ""
negative = -1

for i in name:
    name_reversed += name[negative]
    negative -= 1
    
print(name_reversed)


# factorial number

def factorial(num):
    multiply_num = []
    factorial_num = 1
    is_negative = False
    if num < 0:
        factorial_num = -1
        is_negative = True
    
    for i in range(num * factorial_num):
        multiply_num.append(i + 1)
    
    acumulator = 1
    for i in multiply_num:
        acumulator *= i
    if is_negative == True:
        print(acumulator * -1)
    else:
        print(acumulator)

factorial(-5)


