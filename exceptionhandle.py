even_numbers = [0,2,4,6,8]
ind=int(input("enter the index position="))
try:
    
    print(even_numbers[ind])
    print(10/even_numbers[ind])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")