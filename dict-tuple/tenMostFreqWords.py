fname = input("enter fname, existing sample1.txt:")
try:
	fhandle = open(fname)
except:
	fhandle = open("sample1.txt")
words = {}
for line in fhandle:
    line = line.split()
    for word in line:
        words[word] = words.get(word, 0) + 1
#print(words)

lst = []
for k,v in words.items():
    newtup = (v,k)
    lst.append(newtup)
lst.sort(reverse= True)
print("Top 10 most frequent words are: ",lst[:10])