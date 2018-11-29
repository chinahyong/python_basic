#4.1.1
# spam = ['Alice','Elvis','Bob','Mary']
# print(spam[0])
# print(spam[3])
# spam = [['Cat','Dog'],[1,2,3,4]]
# print(spam[0])
# print(spam[0][1])
# print(spam[1][3])
# # 下标从后往前-1开始计算
# print(spam[-1][-2])

#4.2.1
# catNames = []
# while True:
# 	print('Enter the name of cat ' + str(len(catNames)+1) +'Or enter noting to stop.:')
# 	name = input()
# 	if not name:
# 		break
# 	catNames = catNames + [name]
# print('The cat names are')
# for name in catNames:
# 	print(' '+name)

#4.4.4
# spam = ['Yollo','Cary','annie','blue','Andy','Cidy','Mara','Zippo']
# #ASCII 排序
# spam.sort()
# print(spam)
# spam.sort(reverse=True)
# print(spam)
# spam.sort(key=str.lower)
# print(spam)
# print('yollo' in spam)
# print('Cary' in spam)
# print('yollo' not in spam)
# print(spam)
# print(spam.index('Cary'))
# print(spam.index('Mara'))
# spam.append('Last')
# print(spam)
# spam.insert(2,'InsertName')
# print(spam)
# spam.remove('Mara')
# print(spam)
# del spam[0]
# print(spam)

#4.6.2 元组 类似列表数据，但不可变
# print(type((1,)))
# print(tuple([1,2,3,4]))
# print(list((1,2,3)))
# print(list('I am a string'))
# print(tuple('I am a string'))

#4.7.2  copy:赋值集合值到新的变量  deepcopy:赋值元素为列表的列表到新的变量
# import copy
# spam = [1,2,3,4,5]
# chesse = copy.copy(spam)
# print(chesse)
# chesse[0] = 'update'
# print(chesse)
# print(spam)
# deep = [[1,2],[2,3,4,5]]
# deep2 = copy.deepcopy(deep)
# deep2[1][1]='update'
# print(deep)
# print(deep2)

#4.10.1
# spam = ['apples','bananas','tofu','cates']
# def listToStr(spam):
# 	for num in range(len(spam)):
# 		if(num == len(spam) -1):
# 			print('and'+spam[num])	
# 		else :
# 			print(spam[num]+',',end='')
# listToStr(spam)

#4.10.2
# grid = [['.', '.', '.', '.', '.', '.'],
# 		['.', 'O', 'O', '.', '.', '.'],
# 		['O', 'O', 'O', 'O', '.', '.'],
# 		['O', 'O', 'O', 'O', 'O', '.'],
# 		['.', 'O', 'O', 'O', 'O', 'O'],
# 		['O', 'O', 'O', 'O', 'O', '.'],
# 		['O', 'O', 'O', 'O', '.', '.'],
# 		['.', 'O', 'O', '.', '.', '.'],
# 		['.', '.', '.', '.', '.', '.']]
# for x in range(len(grid[0])):
# 	for i in range(len(grid)):
# 		print(grid[i][x],end='')
# 	print()
