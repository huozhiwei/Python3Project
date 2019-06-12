# 使用FileInput对象读取文件

# readlines

import fileinput
fileobj = fileinput.input('./files/urls.txt')
print(type(fileobj))

print(fileobj.readline().rstrip())


# fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
# fileinput.filelineno()  #返回当前读取的行的行号
# 读取所有的行
for line in fileobj:
    line = line.rstrip()
    # lineno: 返回当前已经读取的行的数量（或者序号）
    if fileobj.lineno() == 2:
        print(type(line))

    if line != '' and not line.isspace():
        print(fileobj.filelineno(),':',line)

    else:
        print(fileobj.filename())