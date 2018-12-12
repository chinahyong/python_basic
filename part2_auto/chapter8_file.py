#-*- coding:UTF-8 -*-
# os 文件相关处理，类似java中的(IO)
import os
# 连接多个子目录组成 path地址(可以忽略OS 、 Windows中使用不同斜杠)
# print(os.path.join('D:','workspace','workspace_python'))

#8.1.2
# getcwd 获取当前工作目录
# print(os.getcwd())
# os.chdir('')		# 修改当前目录到指定目录
# os.makedirs('')  # 创建 新文件夹
# print(os.path.abspath('.'))	#输出绝对路径,当前文件夹的
# print(os.path.isabs(os.path.abspath('.')))	#是否是绝对路径
# os.path.relpath('path','start')	#返回从start到path的相对位置,如果没有默认为当前位置到path
# print(os.path.dirname(os.getcwd()))	#dirname 当前所在文件夹
# print(os.path.basename(os.getcwd()))	#basename 当前根目录
# print(os.path.split(os.getcwd()))
# print(os.getcwd().split(os.path.sep))	#分隔每一层
# print(os.path.getsize(os.getcwd()+'\\chapter8_file.py'))	#获取文件大小 字节
# print(os.listdir(os.getcwd()))	#指定文件夹下面的文件列表
# totalSize = 0
# for file in os.listdir(os.getcwd()):
# 	totalSize +=os.path.getsize(file)
# print(os.getcwd()+'文件大小：',totalSize)
# print(os.path.exists(os.getcwd()))	#该地址文件、文件夹是否存在
# print(os.path.isfile(os.getcwd()))	#该地址是否为文件
# print(os.path.isdir(os.getcwd()))	#该地址是否为文件夹

#8.2.1   open(path)  read() write('')  close()
# thisFile = open('D:\\workspace_python\\python_basic\\README.md')
# print(thisFile.readlines())	#按行读取是个数组
# # print(thisFile.read())	#读取数据是个字符串
# thisFile.close()

#8.2.3  write() read()
# baconFile = open('bacon.txt','w')	#覆盖写入
# print(baconFile.write('Hello world! \n'))
# baconFile.close()
# baconFile = open('bacon.txt','a')	# 插入写入
# print(baconFile.write('Bacon is not a vegetable.'))
# baconFile.close()
# baconFile = open('bacon.txt')
# print(baconFile.read())
# baconFile.close()

#8.3 shelve:书写二进制文件，保存变量  二次shelve.open 会有问题 IndentationError: unexpected indent
# import shelve
# shelfFile = shelve.open('myData')
# cats = ['Zophie','Alice','Dodb']
# shelfFile['cats'] = cats
# shelfFile.close()

# shelfFile = shelve.open('myData')
# type(shelfFile)
# print(shelfFile['cats'])
# shelfFile.close()

# shelfFile = shelve.open('myData')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))
# shelfFile.close()

#8.4 pprint.pformat()
# import pprint
# cats = [{'name':'dag','desc':'dsds'},{'name':'dsf','desc':'dfsjkdsaf'}]
# print(pprint.pformat(cats))
# fileObj = open('chapter8_myCats.py','w')
# print(fileObj.write('cats= ' + pprint.pformat(cats)+'\n'))
# fileObj.close()

# import chapter8_myCats
# print(chapter8_myCats.cats)

#8.5


