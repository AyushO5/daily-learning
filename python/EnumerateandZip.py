languages = ["Hindi" , "English" , "Spanish" , "French" , "German"] 

index = 0 
for language in languages :
    print(f'Index {index} and language {language}')
    index += 1 

# So instead of this we can use enumerate function that tracks the index 
# automatically instead of we doing it manually  


list(enumerate(languages))

# So here we are passing the languages list to the enumerate function
# and then convert its return value into a list with the help of list function 
# so the output will be [(0, 'Hindi'), (1, 'English'), (2, 'Spanish'), (3, 'French') , (4, 'German')]


# Now lets refactor the enumerate function we used above 

for index , language in enumerate (languages) : 
    print(f'Index {index} and language {language}')

# So here we unpack the count and value of each tuple in the 
# enumerate object into variables named index and language respectively 
# so the output will be  "Index 0 and language Hindi"
# This removes the need for manually creating and updating an index variable




# Now to iterate over multiple iterables in parallel we use zip() function

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# the output will be [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# Now using for loop 

for name , id in zip (developers , ids) : 
    print(f'Name : {name}')
    print(f'Id : {id}')


# In this example, zip() combines the two lists into pairs of elements and returns an iterator of tuples. 
# The for loop then unpacks each tuple into name and id. Finally,for each print statement, we are printing 
# each name and id from the ids and developers lists respectively. The output will be 

# Name: Naomi 
# ID: 1 
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4





