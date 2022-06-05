# Work with four-digit natural number

input_natural_number = int(input("What is your number?: "))
# because of int is immutable I need to create list as storage of imputed number
number = [input_natural_number]
# Find the product of the digits of this number
print('Find the product of the digits of this number')

num = 1
natural_number1= input_natural_number
while input_natural_number > 0:
    num = num * (input_natural_number % 10)
    input_natural_number = input_natural_number // 10
print('digits of this number is: ' + str(num))

# Write number in the reverse order
print('Write number in the reverse order')
print('reverse order is: '+ str(number[0])[::-1])

# Sort number
print("Sorted number is: ")
print(sorted(list(str(number[0]))))
