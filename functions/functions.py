# functions are block of code that perform a specific task
# allows to break down code into smaller modular pieces
# promote code reusability (through function call)

# function definition - 'def' keyword is used followed by function's name and () containing parameters
# if no parameter needed, we use ()
# function call - function_name(arguments) - calls the function to perform the action


# parameters - variables or placeholders in () in function definition
# arguments - values passed into the function when it is called

def greet(name):
    return f"Hello, {name}!"

result = greet("Sahil")
print(result)


