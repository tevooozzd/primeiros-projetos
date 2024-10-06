# ================================
#        Creating Variables
# ================================

# - Uppercase and lowercase letters make a difference
store_one = 0
storeOne = 1
print(store_one, storeOne)  # Output: 0 1

# ================================
#        Naming Conventions
# ================================

# - Spaces cannot be used in variable names
# - To solve this, we use underscores (_), allowing us to combine different words
#   (An error message appears when attempting to create a variable with spaces: 
#   'store one = 0' will result in an error)

store_one = 0
print(store_one)  # Output: 0

# ================================
#      Avoiding Keywords
# ================================

# - Keywords cannot be used as variable names (e.g., False, True, break, etc.)
# - The following will result in an error: 
#   False = 'hello'  # This will raise a SyntaxError

