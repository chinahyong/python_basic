#6.2.2
# str = 'Hellow false'
# print(str.isalpha())#是否全部是字母，非空
# print(str.isalnum())#只包含数字字母，非空
# print(str.isdecimal())#只包含数字，非空
# print(str.isspace())#只包含空格、制表符、换行、非空
# print(str.istitle())#只包含大写字母开头，后面全小写

# while True:
# 	print('Enter your age:')
# 	age = input()
# 	if age.isdecimal():
# 		break
# 	print('Please enter a nubmer for your age')
# while True:
# 	print('Select a new password (letters and numbers only):')
# 	password = input()
# 	if password.isalnum():
# 		break;
# 	print('Please can only have letters and numbers')

#6.2.3  开始、结尾
# str = 'Hello false'
# print(str.startswith('He'))
# print(str.endswith('ss'))

#6.2.4  列表转为字符串join，字符串转为列表split
# print(','.join(['cats','dogs','bats']))
# print(' '.join(['My','name','is','Ali']))
# print('My name is Alices'.split())
# print('My name is Alices'.split('a'))

#6.2.5 字符串左对齐，右对齐，指定符号填充;居中
# print('hello'.ljust(20))
# print('hello'.rjust(20))
# print('hello'.ljust(20,'*'))
# print('hello'.rjust(20,'-'))
# print('hello'.center(20))
# print('hello'.center(20,'+'))

#6.2.6 对齐
# def printPicnic(itemsDict, leftWidth, rightWidth):
# 	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
# 	for k, v in itemsDict.items():
# 		print(k.ljust(leftWidth, '.') +  str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

#6.2.7 去除前后空白
# spam = ' Hello world'
# print(spam.strip())
# print(spam.lstrip())
# print(spam.rstrip())
# print(spam.strip('d'))
# import  pyperclip
# pyperclip.copy('Hello world')
# pyperclip.paste()

#6.4
# import pyperclip,pprint
# #粘贴 剪切板内容
# text = pyperclip.paste()
# pprint.pprint(text)
# # 将多行文本按换行分割
# lines = text.split('，')
# # 遍历元素，字符串前面加*特殊符号
# for item in lines:
# 	item = '* '+item
# 	pprint.pprint(item)
# # 通过换行连接lines每个元素
# text = '，'.join(lines)
# pyperclip.copy(text)
# pprint.pprint(text)

#6.6 split 不传参数默认按空格来分割
# print('Remember, remember, the fifth of November.'.split())

#6.7
tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
for i in range(len(tableData[0])):
	for item in tableData:
		print(item[i],end='  ')
	print()

