# XML字符串转换为字典
# 安装第三方模块: pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple xmltodict

import xmltodict
from collections import OrderedDict

'''
w,r,wt,rt都是python里面文件操作的模式。
w是写模式，r是读模式。
t是windows平台特有的所谓text mode(文本模式）,区别在于会自动识别windows平台的换行符
'''
with open('files/products.xml','rt',encoding='utf8') as f:
    xml = f.read()
    d = xmltodict.parse(xml)
    # print(d)
    # print(type(d)) # collections.OrderedDict的类对象,从字典(dict)类继承过来的
    # 可以看成字典中嵌套字典，一层层嵌套
    for value in d['root']['products']['product']:
        print('uuid',':',value['@uuid'])
        print('id',":",value['id'])
        print('name',':',value['name'])
        print('price',':',value['price'])
        print('-'*40)
    print(d['root']['products']['product'][0]['@uuid'])

    import pprint
    # indent:缩进
    pp = pprint.PrettyPrinter(indent=1)
    pp.pprint(d)
