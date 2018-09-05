from sys import argv
# to run this script, need to input 2 arguments
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(),end = '') # to avoid adding double \n to every line.

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")
print("First line: ")
current_line = 1
print_a_line(current_line, current_file)
print("Second line: ")
current_line += 1
print_a_line(current_line, current_file)
print("Last line: ")
current_line += 1
print_a_line(current_line, current_file)
print ('Rewind again\nTry printing a line again:')
rewind(current_file)
print_a_line(1,current_file)
print ("If no rewinding, same command does like this:")
print_a_line(1,current_file) # no rewinding the f.readline() continues from last time

# Close the file when we are done
current_file.close()
