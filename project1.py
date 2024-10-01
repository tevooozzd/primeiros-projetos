# - Creating variables
# - Uppercase and lowercase letters make a difference

store_one = 0
storeOne = 1
print(store_one, storeOne) ## - Output = 0 1

# - Spaces cannot be used
# - To solve this, we use _, allowing us to combine different words
# (An error message appears when attempting to create a variable: 'store one = 0')

store_one = 0
print(store_one)  ## - Output = 0

# - Keywords cannot be used as variables (false, true, break, etc...)
# - Output with error message in the example: False = 'hello'
