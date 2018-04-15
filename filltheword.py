from random import randint

choice= 1

v= []
indices= []
val= 0
j= 0
datadict= {1:('beer', 'wine', 'spirit', 'cider'), 2:('eggs', 'beef', 'chicken', 'honey'), 3:('lion', 'tiger', 'dog', 'cat'), 4:('eminem', 'mohit', 'sunjay', 'amitabh'), 5:('lamborghini', 'porche', 'bmw', 'audi')}

def play(choice):
	c= []
	data= datadict.get(choice)
	v= randint(0, len(data)-1)
	v= data[v]
	v= list(v)
	i= 0
	while i<len(v):
		c.append("_")
		i=i+1
	for i in range(0, int(len(v)/3)):
		val=randint(0, len(v)-1)
		c[val]= v[val]
	print("\nComplete this: ", end="")
	print('%s' % ' '.join(map(str, c)))
	while(c!=v):
		guess= input("Your guess: ")
		if(guess in v):
			if(guess not in c):
				j= v.index(guess)
				c[j]= v[j]
				print('%s' % ' '.join(map(str, c)))
			if(guess in c and c.count(guess) < v.count(guess)):
				indices = [k for k, x in enumerate(v) if x == guess]
				for j in indices:
					if(v[j]!=c[j]):
						c[j]= v[j]
						print('%s' % ' '.join(map(str, c)))
		else:
			print("Wrong guess!")
	if(c==v):
		print("\nYou completed: ", end="")
		print('%s' % ''.join(map(str, c)), end="")
		print("!")
	c= []

while(choice!=6):
	print("\n\nLet's play fill the words")
	print("\nChoices available:\n1. Drinks\n2. Foods\n3. Animals\n4. Celebrities\n5. Cars\n6. Exit")
	choice= int(input("Enter your choice(number): "))
	if(choice in datadict):
		print("\nYour choice is "+str(choice)+". So let's play now!")
		play(choice)
	elif(choice==6):
		exit()
	else:
		print("\nWrong choice!")
