#5.1.1
# mycat = {'size':'fat','color':'red','disposition':'loud'}
# print(mycat)
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while True:
# 	print('Enter a name:(blank to quit)')
# 	name  =input()
# 	if name == '':
# 		break
# 	if name in birthdays:
# 		print(birthdays[name] + 'is the birthday of '+name)
# 	else :
# 		print('I do not have birthday information for'+name)
# 		print('what is their birthday?')		
# 		bd = input()
# 		birthdays[name] = bd
# 		print('Birthday database updated.')

#5.1.2
# spam = {'color':'red','size':'lat'}
# for num in spam.values():
# 	print(num,end='')
# print()
# for num in spam.keys():
# 	print(num,end='')
# print()
# for num in spam.items():
# 	print(num,end='')

#5.1.5
# import pprint
# spam = {'color':'red','size':'lat'}
# print(spam['color'])
# print(spam.get('size'))
# print(spam.get('sizes',0))
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
# 	count.setdefault(character,0)
# 	count[character] +=1
# print(count)
# pprint.pprint(count)

#5.3.1
# theBoard =  {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
# 			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# theBoard =  {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
# 			'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
# 			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# theBoard =  {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
# 			'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
# 			'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
# def printBoard(board):
# 	print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
# 	print('-+-+-')
# 	print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
# 	print('-+-+-')
# 	print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
# turn = 'X'
# for i in range(9):
# 	printBoard(theBoard)
# 	print('Turn for'+turn+'.Move on which space?')
# 	move = input()
# 	theBoard[move]=turn
# 	if turn == 'X':
# 		turn = 'O'
# 	else :
# 		turn = 'X'
# printBoard(theBoard)

#5.4
# allGuests = {
# 	'Alice':{'apples':5,'pretzeles':12},
# 	'Bob':{'ham sandwiches':3,'apples':2},
# 	'Carol':{'cups':3,'apple pies':1}
# }
# def totalBrought(guests,item):
# 	numBrought = 0
# 	for k,v in guests.items():
# 		numBrought = numBrought+v.get(item,0)
# 	return numBrought
# print('Number of things being brought:')
# print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
# print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
# print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
# print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))
# print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))

#5.6.1
# things = {
# 	'rope': 1, 
# 	'torch': 6, 
# 	'gold coin': 42, 
# 	'dagger': 1,
# 	'arrow': 12}
# def printDict(things):
# 	total = 0
# 	for x in things.keys():
# 		print(str(things.get(x))+' '+x)
# 		total+=things.get(x)
# 	print('total num of item:'+str(total))
# printDict(things)

#5.6.2
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def add(dict,list):
	for i in inv.keys():
		for item in dragonLoot:
			if item == i:
				inv[i]+=1
			#不存在key的时候进行插入，插入不能放到遍历过程内
			# else :
			# 	inv.get(item,1)
def display(dict):
	for i in inv.keys():
		print(str(inv[i])+' '+i)
add(inv,dragonLoot)
display(inv)


