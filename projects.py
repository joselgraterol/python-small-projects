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


