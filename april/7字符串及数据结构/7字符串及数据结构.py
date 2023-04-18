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


if __name__ == '__main__':
    # string()
    list_test()
