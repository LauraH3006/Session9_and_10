fp = open("text.txt", "r") # this is open for reading
print(fp.read()) # read () method gets the entire file content
fp.close() # this is good practice

# sane thing using a context manager!
# this is more pythonic!
with open("text.txt", "r") as f:
    print(f.read())
 # no need to close

# read the file line by line
print("Now we read it line by line")
with open("text.txt", "r") as f:
    for line in f: # f is iterable
        print(line, end="")
        print(line.rstrip())

