from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'a')

print("Truncating the file. Goodbye!")
# target.truncate() no need to use trancate function if use open(filename,'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
str = line1 + "\n" + line2 +'\n' + line3 +'\n'
'''target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")'''
# target.write(str)
target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close()
