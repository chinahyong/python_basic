#导入粘贴板库、正则表达式库
import pyperclip,re
# phoneRegex = re.compile(r'1\d{2} \d{4} \d{4}')
# emailRegex = re.compile(r'\w|\d@\w|\d.\w')
phoneRegex = re.compile(r'''
	(\d{3}|\(\d{3}\))?  # 3个数字（可没有）
	(\s|-|\.)?          # 分割：空格、-、.
	(\d{3})				# 3个数字
	(\s|-|\.)           # 分割：空格、-、.
	(\d{4})				# 4个数字
	(\s*(ext|x|ext.)\s*(\d{2,5}))? #扩展可没有
	''',re.VERBOSE)
#A-Z 用大小写忽略进行匹配
emailRegex = re.compile(r'''
	[a-z0-9._%+-]+
	@
	[a-z0-9.-]+
	(\.[a-zA-Z]{2,4})
	''',re.VERBOSE|re.I)
matches = []
for groups in phoneRegex.findall(pyperclip.paste()):
	phoneNumber = '-'.join(groups[1],groups[3],groups[5])
	if(groups[8] != ''):
		phoneNumber += ' x'+groups[8]
	matches.append(phoneNumber)
for email in emailRegex.findall(pyperclip.paste()):
	matches.append(email)
if len(matches)>0:
	print('\n'.join(matches))
else:
	print('No PhoneNubmer And Email Found.')

