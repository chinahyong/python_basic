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
import pprint
spam = {'color':'red','size':'lat'}
print(spam['color'])
print(spam.get('size'))
print(spam.get('sizes',0))
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
	count.setdefault(character,0)
	count[character] +=1
print(count)
pprint.pprint(count)