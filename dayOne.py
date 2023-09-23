## Write a function called divide_or_square that takes one argument (a number) and 
## returns the square root of the number if it is divisible by 5, or its remainder if it is not divisible by 5. 
## For example, if you pass 10 as an argument, then your function should return 3.16 as the square root.

def divide_or_square(x):
    if x % 5 == 0:
        return x**(1/2)
    else:
        return x % 5
    
solution = divide_or_square(20)

print(solution)

## Extra Challenge: Longest Value
## Write a function called longest_value that takes a dictionary as an argument and returns the first longest value of the dictionary. For example, the following dictionary should return "apple" as the longest value.
## fruits = {'fruit': 'apple', 'color': 'green'}
