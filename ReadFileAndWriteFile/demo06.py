'''
练习题2:
    编写一个Python程序，从当前目录的文本文件words.txt中读取所有内容(全都是英文单词)，
并统计其中每一个英文单词出现的次数。单词之间用逗号(,)、分号(;)、或空格分隔，也可能时这3
个分隔符一起分隔单词。将统计结果保存到字典中，并输出统计结果。

假设words.txt文件内容如下:
test star test star star;bus test bill ,  new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero , fuck bill , fuck ;
new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero ,new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero ,new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero , and,and,and sex,six  sex  ;;
; hero ,new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero ,new yeah bill,book, database ; dad,  mom,father ;; mother
parent,  ; friend ; star bus, test John ,father , list ,hello ,how ; hero , and,and,and sex,six  sex  ;;       new yeah bill,book,
'''

import re
f = open('./files/words.txt','r')
words = f.read()
wordList = re.split('[ ,;\n]+',words)
# print(wordList)
countDict = {}
for word in wordList:
    if word:
        countDict[word] = countDict.setdefault(word,0) + 1
        # if countDict.get(word) == None:
        #     countDict[word] = 1
        # else:
        #     countDict[word] = countDict[word] + 1

for key,value in countDict.items():
    print(key,'=',value)
f.close()