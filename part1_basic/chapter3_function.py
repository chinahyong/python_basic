# def hello():
# 	print('Howdy!')
# 	print('Howdy!!')
# 	print('Hello there!!!')
# hello()
# hello()
# def hello(name):
# 	print('Hello:'+name)
# hello('Elvis')
# hello('Alice')

#3.2
# import random
# def getAnswer(answerNumber):
# 	if answerNumber == 1:
# 		return 'It is certain'
# 	elif answerNumber == 2:
# 		return 'It is decidely so'
# 	elif answerNumber == 3:
# 		return 'Yes'
# 	elif answerNumber == 4:
# 		return 'Reply hazy try again'
# 	elif answerNumber == 5:
# 		return 'Ask again later'
# 	elif answerNumber == 6:
# 		return 'Concentrate and ask again'
# 	elif answerNumber == 7:
# 		return 'My reply is no'
# 	elif answerNumber == 8:
# 		return 'Outlook not so good'
# 	elif answerNumber == 9:
# 		return 'Very doubtful'
# r = random.randint(1,9)
# print(getAnswer(r))

#3.6
# def spam():
# 	global eggs
# 	eggs = 'spam'
# eggs = 'global'
# spam()
# print(eggs)

#3.7
# def spam(divideBy):
# 	try:
# 		return 42/divideBy
# 	except ZeroDivisionError:
# 		print('Error:Invalid argument.')
# print(spam(2))
# print(spam(42))
# print(spam(0))
# print(spam(3))

#3.8
# import random
# secretNumber = random.randint(1,20)
# print('I am thinking of a number betwenn 1 and 20.')
# for i in range(1,7):
# 	print('Take a guess')
# 	try:
# 		guess =int(input())
# 	except ValueError:
# 		print('请输入整数')
# 		guess = int(input())
# 	if guess < secretNumber:
# 		print('Your guess is too low.')
# 	elif guess > secretNumber:
# 		print('Your guess is too large.')
# 	else :
# 		break
# if guess == guess:
# 	print('Good Job!You guessed my number in ' + str(secretNumber) + ' guesses!')
# else :
# 	print('Nope.The number I was thinking of was' + str(secretNumber))

#3.11.1
# def collatz(number):
# 	# if number / 2 ==1:
# 	if number % 2 ==0:
# 		print(number // 2 )
# 	# else:
# 	elif number % 2 ==1:
# 		print(3 * number + 1)
# 		return 3 * number + 1
# while True:
# 	collatz(int(input()))
