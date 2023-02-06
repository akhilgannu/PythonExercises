fhandle = open('sample.txt')
for line in fhandle:
    line = line.rstrip() # to strip all the empty spaces(\n)
    if line.startswith("H"):
    	print(line) # print by default adds new line