ino1 = 0
ino2 = 1
ino3 = 0
print(ino1)
print(ino2)

for i in range(2,5):
	ino3 = ino1 + ino2
	print(ino3)
	ino1 = ino2
	ino2 = ino3
	

