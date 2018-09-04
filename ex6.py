# define variable: types_of_people
types_of_people = 10
# define variable x (is a string with variable)
x = f"There are {types_of_people} types of people."
# variable binary is a string "binary"
binary = "binary"
# variable do_not is a string "don't"
do_not = "don't"
# y is a string with 2 variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
# variable hilarious is a boolean
hilarious = False
# joke_evaluation is a string with a variable
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation)
print(joke_evaluation.format(hilarious))
print(joke_evaluation.format(binary))
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
