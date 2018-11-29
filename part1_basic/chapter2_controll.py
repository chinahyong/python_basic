#2.6 if----else
# print('请输入姓名：')
# name =input()
# if name == 'Mary':
# 	print('Hello Mary')
# print('请输入密码：')
# password = input()
# if password == 'swordfish':
# 	print('Access granted')
# else:
	# print('Wrong password')

#2.7.3 if----elif
# print('请输入年龄：')
# age = input()
# if name == 'Alice':
# 	print('Hi,Alice')
# elif int(age) < 12:
# 	print('You are not Alice,Kiddo.')
# elif int(age) >2000:
# 	print('Unlike you,Alice is not undead,immortal vampire.')
# elif int(age) > 100:
# 	print('You are not Alice,grannie.')

#2.7.5 while
# name = ''
# while name != 'Elvis':
# 	print('Please type your name:')
# 	name = input()
# print('Thank you!')

#2.7.6  break
# while True:
# 	print('Please type your name:')
# 	name = input()
# 	if(name == 'Elvis'):
# 		break
# print('break end')

#2.7.7  continue
# while True:
# 	print('Who are you?')
# 	name = input()
# 	if(name != 'Elvis'):
# 		continue
# 	print('Hello,Elvis.What is the password?(It is a fish.)')
# 	password = input()
# 	if password == '1214':
# 		break
# print('Access Granted')

#2.7.8 for
# print('My name is')
# for i in range(5):
# 	print('Jimmy Five times ('+ str(i) +')')
# total = 0
# for num in range(101):
# 	total +=num
# print(total)

#2.7.10
# for i in range(12,16):	# 12开始，到16(不包含)
# 	print(i)
# for num in range(0,10,2):	# 0开始 每个2打印一次，一直到10(不包含)
# 	print(num)

#2.8  module import
# import random #这种方式导入需要使用random.函数名
# from random import * #这种方式可以直接使用户数，不需要点
# for i in range(5):
# 	print(random.randint(1,10))

#2.9 终止程序
# import sys
# while True:
# 	print('Type exit to exit')
# 	response = input()
# 	if response == 'exit':
# 		sys.exit()
# 	print('You typed '+ response +'.')

#2.11
# spam = input()
# if spam == '1':
# 	print('Hello')
# elif spam == '2':
# 	print('Howdy')
# else:
# 	print('Greetings')
# for i in range(1,11):
# 	print(i)
num = 1
while num <= 10:
	print(num)
	num+=1