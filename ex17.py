from sys import argv
from os.path import exists  # check whether the thing exists, return True or False

script, from_file, to_file = argv

print ("Copying from %s to %s" % (from_file, to_file))

indata = open(from_file).read()  # open a file and read it

print ("The input file is %d bytes long" % len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready,hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file,'w')   #open to_file with the write model, and rename it as out_file
out_file.write(indata)

print ("Alright, all done.")

out_file.close()    #remember to close the file

