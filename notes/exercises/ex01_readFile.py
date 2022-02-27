# MIT License
# Copyright (c) 2022 Mahmoud Harmouch

f = open("file.txt")
line = f.readline()

while line:
	print(line,end='')
	line = f.readline()
f.close()

with open("file.txt") as f :
	line = f.readline()
	while line:
		print(line,end='\n')
		line = f.readline()	
# always use the following method, much faster 
for line in open("file.txt"):
	print(line,end='')
