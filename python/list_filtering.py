# ------------------------- Instruction --------------------------
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# ------------------------- Example ------------------------------
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# ------------------------- Approach -----------------------------
# 1. Make a function called filter_list that takes a parameter aas a list
# 2. create a variable called non_string_type in the function to store the data type that is not string
# 3. Loop through the list using for ... in
# 4. Check if the type each item in the list is not string, if so, push or append the item to the non_string_type variable
# 4. Then, return non_string_type

# ------------------------ Solution ------------------------------
def filter_list(l):
    'return a new list with the strings filtered out'
    non_string_type = []
    for item in l:
        if not isinstance(item, str):
            non_string_type.append(item)
            
    return non_string_type
