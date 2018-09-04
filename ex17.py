'''
we are doing all these in 1 line 
'''

from sys import argv
# from os.path import exists

script, from_file, to_file = argv

# print(f'Copying from {from_file} to {to_file}')

# in_file = open(from_file)
# indata = in_file.read()
# we could do these two on one line

# indata = open(from_file).read()


# print(f"the input file is {len(indata)} bytes long")
# print(f"Does the output file exit? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort")

# input()

# out_file = open(to_file, 'w')

open(to_file, 'w').write(str(open(from_file).read()))

# print("Alright, all done.")

# open(to_file).close()
# open(from_file).close()
