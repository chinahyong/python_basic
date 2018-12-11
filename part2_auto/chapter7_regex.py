#7.2.1
# import re
# phoneNumRegex = re.compile(r'1\d{2}\d{3}\d{3}')
# text = phoneNumRegex.search('My phone Num is 18229099596')
# print('Phone number is:'+text.group())

#7.3.1  re:正则表达式库
import re 
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group())
# print(mo.groups())
# areaCode,mainNumber = mo.groups()
# print(areaCode)
# print(mainNumber)

#7.3.2  | 或者的意思，优先查找最先出现的
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo = heroRegex.search('Batman and Tina Fey')
# print(mo.group())
# mo = heroRegex.search('Tina Fey and Batman')
# print(mo.group())
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo=batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))

#7.3.3 ()? : 括号内为可选分组，可以有，也可以没有。括号中出现 0次或者1次
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())

#7.3.4 ()* : 括号内为可选分组，可以有，也可以没有。括号中出现 0次或者多次
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())
# mo = batRegex.search('The Adventures of Batwowowowoman')
# print(mo.group())

#7.3.5 ()+ : 括号内为可选分组，至少出现1次
# batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The Adventures of Batman')
# print(mo == None)
# mo = batRegex.search('The Adventures of Batwoman')
# print(mo.group())
# mo = batRegex.search('The Adventures of Batwowowowoman')
# print(mo.group())

#7.3.6 {3}:指定()显示几次。{,5}:0-5次，{3,}：至少3次；{3,5}：3-5次
# haRegex = re.compile(r'(Ha){3}')
# mo = haRegex.search('HaHaHa')
# print(mo.group())

#7.4 {3,5}：默认优先匹配最多，贪心；；{3,5}?：默认优先匹配最少，非贪心
# greedyRegex = re.compile(r'(Ha){3,5}')
# mo = greedyRegex.search('HaHaHaHaHa')
# print(mo.group())
# greedyRegex = re.compile(r'(Ha){3,5}?')
# mo = greedyRegex.search('HaHaHaHaHa')
# print(mo.group())

#7.5 findall()
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') 
# print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

#7.6  \d:0-9  \D:\d除外 \w:字母数字下划线(单词) \W:\w除外 \s:空格、制表符、换行符 \S:\s除外
# xmasRegex = re.compile(r'\d+\s\w+')#至少一个数字，至少一个单词
# print(xmasRegex.findall('''12 drummers,11 pipers, 10 lords, 9 ladies, 8 maids, 7
# swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'''))

#7.7  []指定字符 [^]出去指定字符
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

#7.8 '^'：开头，'$'：结尾
# beginsWithHello = re.compile(r'^Hello')
# print(beginsWithHello.search('Hello world!'))
# print(beginsWithHello.search('He said Hello!') == None)
# endsWithNumber = re.compile(r'\d$')
# print(endsWithNumber.search('Your number is 42'))
# print(endsWithNumber.search('Your number is Two') ==None)

#7.9  '.'匹配换行之外的所有字符 '.*':表示任意文本 '.*?'非贪心
# atRegex = re.compile(r'.at')
# print(atRegex.findall('The cat in the hat sat on the flat mat.'))
# atRegex = re.compile(r'First Name:.*Last Name:.*')
# print(atRegex.search('First Name:WongLast Name:Elvis'))
# atRegex = re.compile(r'First Name:(.*)Last Name:(.*)')
# print(atRegex.search('First Name:WongLast Name:Elvis').group(1))
# newlineRegex = re.compile('.*')
# print(newlineRegex.search('Serve the public trust.\nProtect the innocent.').group())
# newlineRegex = re.compile('.*', re.DOTALL) #re.DOTALL  包含换行
# print(newlineRegex.search('Serve the public trust.\nProtect the innocent.').group())

#7.11 re.compile('',re.IGNORECASE) re.IGNORECASE或re.I 都表示忽略大小写

#7.12 sub() 匹配到内容替换成指定字符串
namesRegex = re.compile(r'Agent \w+')
print()