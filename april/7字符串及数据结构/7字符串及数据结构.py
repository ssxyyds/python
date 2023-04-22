def string():
    """
    字符串
    :return:
    """
    s1 = 'ssx ' * 3
    s2 = '\n'
    s2 += s1
    print(s1, s2, end='123\n')
    print(f's1 in s2: {s1 in s2}')
    print(f's2 in s1: {s2 in s1}')

    s3 = 'abcdef12345678910'
    print(s3[-1])
    # 从第二位截取
    print(s3[2:])
    # 截取前三位
    print(s3[:3])
    # 从第0位开始截取 每隔5位截取一个 af51
    print(s3[::5])
    # be2580
    print(s3[1::3])
    # 0852eb
    print(s3[-1::-3])
    # 反转字符串 01987654321fedcba
    print(s3[::-1])

    # 字符串常用方法
    s4 = 'hello word'
    print(len(s4))
    # 字符串单词首字母大写  Hello Word
    print(s4.title())
    # 检查字符串是否以xx开头  True
    print(s4.startswith('he'))
    # 清空字符串xx    llo word
    print(s4.strip('he'))
    print(s4.isdigit())
    # 检查字符串是否以字母构成 True
    print('hhhh'.isalpha())


def list_test():
    """
    列表
    :return:
    """
    list1 = [1, 3, 5, 7, 9]
    list2 = ['s', 'x', 'z']
    # 合并两个列表  [1, 3, 5, 7, 9, 's', 'x', 'z']
    list3 = list1 + list2
    print(len(list1))
    for v in list1:
        print(v)
    for i, v in enumerate(list1):
        print(f"index:{i},value:{v}")

    # 删除元素 [1, 3, 5, 7, 9, 'x']
    if 's' in list3:
        list3.pop(len(list3) - 1)
        list3.remove('s')
        print(list3)

    # 浅拷贝 True
    list4 = list3
    list4[0] = '100'
    print(f'list3 == list4 :{list3 == list4}')

    # 深拷贝 False
    list4 = list3[:]
    list4[0] = '200'
    print(f'list3 == list4 :{list3 == list4}')

    # 列表切片 与字符串相同
    print(list3[2:])
    # 排序
    print(sorted(list2))


def set_test():
    """
    集合(set)操作
    :return:
    """
    # 创建集合set1，包含1、2、3、4、3这五个元素
    set1 = {1, 2, 3, 4, 3}
    # 创建一个range对象，包含1到4这四个元素
    set2 = range(1, 5)
    # 创建一个元组，包含1、2、3、5、6这五个元素
    set3 = (1, 2, 3, 5, 6)

    # 创建集合set4的推导式语法
    # 包含1到99中小于10的整数
    set4 = set([num for num in range(1, 100) if num < 10])

    # 输出各集合的数据类型
    # set1为集合类型set，set2为range类型，set3为tuple类型
    print(f'set1:{type(set1)},set2:{type(set2)},set3:{type(set3)}')

    # 使用集合运算符&、|、-、^对集合进行操作
    # &运算符求交集，输出set1和set2的交集
    print(f'set1 & set(set2) :{set1 & set(set2)}')  # {1, 2, 3, 4}
    # |运算符求并集，输出set1和set3的并集
    print(f'set1 | set(set3) :{set1 | set(set3)}')  # {1, 2, 3, 4, 5, 6}
    # -运算符求差集，输出set1和set2的差集
    # 即在set1中出现但不在set2中出现的元素
    print(f'set1 - set(set2) :{set1 - set(set2)}')  # {3, 4}
    # ^运算符求对称差集，输出set1和set4的对称差集
    # 即在set1和set4中出现，但不同时在两者中出现的元素
    print(f'set1 ^ set4 :{set1 & set4}')  # {1, 2, 3, 4}


def tuple_test():
    """
    元组
    :return:
    """
    t = ("ssx", 123, "hhh")
    for i in t:
        print(i)
    # 元组转换为列表
    ls = list(t)
    # 列表转换为元组
    t = tuple(ls)


def dict_test():
    # 创建一个字典d1
    d1 = {"k1": "v1", "k2": "v2"}
    print(d1.items())
    # 获取d1中键为'k3'的值，如果键不存在则返回默认值'v3'
    print(d1.get('k3', 'v3'))
    print(d1)

    # 创建一个字典d2
    d2 = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9, ten=10)
    # 修改d2中键为'one'的值为1111
    d2.update(one=1111)
    print(d2)


if __name__ == '__main__':
    # string()
    # list_test()
    # set_test()
    # tuple_test()
    dict_test()
