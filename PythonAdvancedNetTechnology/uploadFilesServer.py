# 上传文件服务器

# os.path.join(path1[, path2[, ...]])
# 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。
#
# >> > os.path.join('c:\\', 'csv', 'test.csv')
# 'c:\\csv\\test.csv'
# >> > os.path.join('windows\temp', 'c:\\', 'csv', 'test.csv')
# 'c:\\csv\\test.csv'
# >> > os.path.join('/home/aa', '/home/aa/bb', '/home/aa/bb/c')
# '/home/aa/bb/c'

# import os
# path = "F:/gts/gtsdate/"
# b = os.path.join(path,"/abc")
# 输出结果是：'F:/abc'
# 并不是我期望的："F:/gts/gtsdate/abc"
# 原因是在os.path.join()第二个参数"/abc"起始字符是/。
# 删除该字符即可，也就是：
# b = os.path.join(path,"abc")

import os
from flask import Flask,request
from werkzeug.datastructures import FileStorage,ImmutableMultiDict

ImmutableMultiDict.get()
# FileStorage.filename

UPDATE_FOLDER = 'uploads'

app = Flask(__name__)

@app.route('/',methods=['POST'])
def upload_file():
    file = request.files.get('file1') # request.files['file1']
    print(type(request.files)) # <class 'werkzeug.datastructures.ImmutableMultiDict'>
    print(type(file)) # class 'werkzeug.datastructures.FileStorage'>
    if file:
        file.save(os.path.join(UPDATE_FOLDER,file.filename))
        return '文件上传成功!'

if __name__ == '__main__':
    app.run()

