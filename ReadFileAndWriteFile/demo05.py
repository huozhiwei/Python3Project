'''
练习题1：
    编写一个Python程序,从控制台输入一个奇数，
然后生成奇数行的星号(*)菱形，并将该菱形保存到当前目录下
的stars.txt文件中。
'''

line = input('请输入行数(必须时奇数)：')
line = int(line)

if line % 2:
    f = open('./files/stars.txt','w')
    import os
    # 取整
    spaceNum = line // 2 # 每行的最大空格数
    i = 1
    lineSpaceNum = spaceNum # 当前行的前后空格数
    # 生成上三角形
    while lineSpaceNum >= 0:
        f.write(' ' * lineSpaceNum)
        f.write('*' * (2 * i - 1))
        f.write(' ' * lineSpaceNum + os.linesep)
        lineSpaceNum -= 1
        i += 1

    # 生成下三角形前一行比后一行总'*'数多2，即最左边一个'*',最右边一个'*'
    i -= 2
    # 此时lineSpaceNum = -1
    lineSpaceNum += 2
    # 生成下三角形
    while lineSpaceNum <= spaceNum:
        f.write(' ' * lineSpaceNum)
        f.write("*" * (2 * i - 1))
        f.write(' ' * lineSpaceNum + os.linesep)
        lineSpaceNum += 1
        i -= 1
    f.close()
else:
    print('必须输入奇数')
