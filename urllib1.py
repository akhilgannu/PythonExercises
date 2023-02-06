import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://en.wikipedia.org/wiki/A")
for line in fhand:
	print(line.decode().strip())