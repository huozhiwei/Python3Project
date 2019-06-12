# 文件和流
'''
1. 读文件和写文件
2. 管道输出
3. 读行和写行
4. 使用FileInput对象读取文件
'''
# 读文件和写文件
# r,w,r+,w+，a+
# r+: 文件可读写，如果文件不存在，会抛出文件不存在异常。如果文件存在，会从当前位置开始
# 写入新内容，通过seek函数可以改变当前光标的位置，也就是改变文件的指针。
# w+: 文件可读写，如果文件不存在，会创建一个新的文件，如果文件存在，会清空整个文件，并
# 写入新内容。
# a+ (append): 文件可读写，如果文件不存在，会创建一个新文件，如果文件存在，会将要写入
# 的内容添加到原文件的末尾。也就是说，使用a+打开已经存在的文件，文件指针已经在文件的末尾
# 了。

'''
write(str): 向文件写入内容，该函数会返回写入文件的字节数。
read([n]): 读取文件的内容，n是一个整数，表示从文件指针的位置开始读取的n个字节。
如果不指定n,该函数会读取从当前位置往后的所有的字节。该函数会返回读取的数据。

seek(n):重新设置文件指针，也就是改变文件指针的当前位置。如果使用write函数写入内容
后，需要使用seek(0)重置文件指针。
close(): 关闭文件，对文件进行读写操作后，关闭文件是一个好习惯。
'''

# 以写模式打开test.txt文件
f = open('./files/test.txt','w',encoding='utf-8')

# 向test.txt文件中写入'I love you.'
print(f.write('I love '))
print(f.write('Python'))
f.close()

# 以读模式打开test.txt文件
f = open('./files/test.txt','r',encoding='utf8')
print(f.read(7))
print(f.read(6))
f.close()

# 'r+'
try:
    f = open('./files/test1.txt','r+')
except Exception as e:
    print(e)

# (append)a+:
f = open('./files/test1.txt','a+')
print(f.write('hello'))
f.close()

f = open('./files/test1.txt','a+')
print('------1------')
print(f.read())
f.seek(0)
print('------2------')
print(f.read())
f.close()

# w+
try:
    f = open('./files/test1.txt','w+')
    # 什么也不会读出来，因为以w+模式打开文件时，会先清空文件里面的所有内容
    print(f.read())
    f.write('How are you.')
    # 文件写完后文件指针在文件末尾，所以需要重新将文件指针定位到文件的开头
    f.seek(0)
    print(f.read())
finally:
    f.close()