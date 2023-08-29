# Write a Python program to count the number of even and odd numbers from a series of numbers.
def countEvenAndOdd(numbers):
    a = []
    b = []
    for i in range(len(numbers)+1):
        # print(i)
        if i % 2 == 0:
            # print("It is an even number")
            a.append(i)
        elif i % 2 != 0:
            # print ("It is an even number", i)
            b.append(i)
        else: 
            break
        
    return print(f"List of even number {a}\nList of odd number {b}")
    # print()
        






#driver code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = countEvenAndOdd(numbers)