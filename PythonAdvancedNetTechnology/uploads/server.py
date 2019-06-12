# 服务端程序
from flask import Flask,request

# __name__: 当前模块的名字
app = Flask(__name__)

@app.route('/register',methods=['POST'])
def register_1():
    print(request.form.get('name'))
    print(request.form.get('age'))
    return '注册成功！'

if __name__ == '__main__':
    app.run()