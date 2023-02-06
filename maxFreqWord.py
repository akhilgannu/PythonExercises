#Max frequency word in a file

fhandle = open("sample.txt")
words_count = {}
for line in fhandle:
    words = line.split()
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1
#count = 0
#print(words_count	)
#for word in words_count:
#    if words_count[word] > count:
#        count = words_count[word]
#        max_value = word
#print(max_value)

max_word = None
max_count = None

for key,value in words_count.items():
	if max_count is None or value > max_count:
		max_word = key
		max_count = value
print(max_word, max_count)