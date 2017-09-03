from sys import argv

script, input_file = argv

def print_all(f):
    # print all the content of file f
    print (f.read())

def rewind(f):
    #the first line left shift 2 offsets
    f.seek(2)

def print_a_line(line_count, f):
    #line_count: the order of the line
    #print No.(line_count) line in f
    print (line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

#print all the content in current_file
print_all(current_file)

print("Now let's rewind, kind of like a tape")

rewind(current_file)

print("let's print three lines:")

#print line 1
current_line = 1
print_a_line(current_line,current_file)

#print line 2
current_line = current_line + 1
print_a_line(current_line,current_file)

#print line 3
current_line = current_line + 1
print_a_line(current_line,current_file)