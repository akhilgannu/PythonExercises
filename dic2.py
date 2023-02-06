# usage of get() in dicts
# dict.get(key, default_value)

colors = ['red','green','blue','red','green']
counts = {}
for color in colors:
	# counts[color] = counts[color] + 1 
    # This throws error as the value for the colors is not initialized

    # if color not in counts:
    #	counts[color] = 1
    # else:
    #	counts[color] = counts[color] + 1
    counts[color] = counts.get(color,0) +1
print(counts)
