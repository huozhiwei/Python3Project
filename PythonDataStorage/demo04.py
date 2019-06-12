# JSON字符串与字典互相转换
# json <--> dict

# dict -> json: 使用json模块的dumps函数，该函数通过参数传入字典，
# 并返回json格式的字符串

# json -> dict
'''
1. 使用json模块的loads函数，该函数通过参数传入json字符串，然后返回与该字符串对应的字典
2. 使用eval函数将json格式字符串当作普通的Python代码执行，eval函数会直接返回与json格式
字符串对应的字典
'''

# dict->json: 会将名为data的字典转换为json字符串，然后将json字符串s通过eval函数转换为字典
# json->dict(2种方法): 最后从products.json文件中读取json字符串，并使用loads函数和eval函数两种方法
# 将json字符串转换为字典

import json
data = [
    'names',
    20,
    'Billy',
    {
        'status':1
    },
    {
        'persons':
            [
                {
                'name':'Bill',
                'company':'MicroSoft',
                'age':34
                },
                {
                    'name': '钟志炜',
                    'company': 'MicroSoft',
                    'age': 22
                }
            ]
    }
]
# 将字典转换为json字符串,ensure_ascii参数表示不使用ascii编码,这时会使用相应设置的编码,例如:utf-8
jsonstr = json.dumps(data,ensure_ascii=False)
print(type(jsonstr))
print(jsonstr)

# 将json字符串转换为字典1:
data = json.loads(jsonstr)
print(type(data))
print(data)

# 定义一个json字符串
s = '''
{
    'name':'Bill',
    'company':'MicroSoft',
    'age':20
}
'''
# 使用eval函数将json字符串转换为字典
data = eval(s)
print(type(data))
print(data)

print(data['company'])

with open('./files/products.json','rt',encoding='utf-8') as f:
     jsonStr = f.read()
     json1 = eval(jsonStr) # json->dict方法1
     json2 = json.loads(jsonStr) # json->dict方法2
     print(json1)
     print(json2)
     print(json2['data']['products'][0]['name'])
     print(json2['data']['products'][1]['name'])