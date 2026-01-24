# So in this i am going to understand what dictionarie is and what kind of operations i can perform on it 
# So dictionarie is a built in Data-Structure that stores collection of key-value pairs Dictionarie is useful 
# when we need to find value based on a key as it is very fast compared to normal lookup

dictionary = {
   "name": 'Ayush' ,
   "age" : 23 ,
   "city" : 'Indore'
}

# In dictionary each key is associated with a value so we can access any value easily and fast 

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# for example above name is associated with Margherite Pizza and price with 8.9 
# To access the value of dictionarie we can use the bracket notation t's the name 
# of the variable that holds the dictionary, followed by square brackets, and the 
# key you want to access within the square brackets:

pizza['price']

# To update the value we need just to add assignment operator and assign the new value

pizza['name'] = "Framhouse"

# The .get() method retrieves the value associated with a key. It's similar to the bracket 
# notation that we just used, but its advantage is that you can set a default value, so you 
# won't get an error if the key doesn't exist:

pizza.get('toppings', []) # ['mozzarella', 'basil']

# The .pop() method removes the key-value pair with the key that you specify as the first argument
#  and returns its value. If the key doesn't exist, it returns the default value that you specify 
# as the second argument. If the key doesn't exist and you don't pass a default value, a KeyError is raised:

pizza.pop('price', 10)
pizza.pop('total_price') # KeyError

# the .update() method updates the key-value pairs with the key-value pairs of another dictionary. If they have
#  keys in common, their values are overwritten. In this example, we are updating the pizza dictionary. The price
#  key exists in both of them, so its value will be replaced with 15. But total_time is new, so it will be added
#  to the pizza dictionary as a new key-value pair:

pizza.update({ 'price': 15, 'total_time': 25 })



