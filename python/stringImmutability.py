# to check if a character is present inside a string python provide (in) 
# operator thorugh this operator we can check if a character is present inside a string or not

my_str = 'Hello Alice'
print('Alice' in my_str )

# The output will be True as the in operator return either true or false 

#To check the length of any string we use the len function 

var = 'How is the weather today'
print(len(var))

# The output will be 24 

# We can also access the character at any index in a string as there is something called indexing so 
# through the index we can access which character is the which index we can also use negative index 
# to check from the end of the string

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

print(my_str[-1])  # d
print(my_str[-2]) # l


# Now immutable mean that once it is declared its value cannot be changed we can reassign the value but
#  we can not direcly modify the string

greeting = 'hi'
greeting = 'hello'
# Correct
print(greeting) # hello
# Incorrect
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment


# To combine two string we use concatination by the help of (+) operator we can combine two strings 

name ='Ayush'
surname = 'Tripathi'

fullname = name + ' ' + surname

# But we can only combine two string with this we cannot combine string with integer it will throw an Typeerror 

name = 'Ayush Tripathi'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# To solve this we can convert age into string with InBuilt function str() without modifiying the original value 

name_and_age = name + str(age)
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

