# -*- coding: utf-8 -*-
'''
一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。(
# （要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)
'''


def count_factory(num):
    def count(fn):
        def wrapper(*args, **kwargs):
            success = 0
            fail = 0
            for i in range(num):
                print("第{}次".format(i + 1))
                sex = input('请输入您的性别：')
                age = int(input('请输入您的年龄：'))

                re = fn(sex, age, *args, **kwargs)
                if re:
                    success += 1
                else:
                    fail += 1

            print('success={},fail={}'.format(success, fail))

        return wrapper

    return count


@count_factory(num=3)
def sxw_ball(sex, age):
    if sex == '女' and 15 <= age <= 22:
        print('恭喜加入球队！')
        return 1
    else:
        print('很遗憾！！！')
        return 0


if __name__ == '__main__':
    sxw_ball()

# if __name__ == '__main__':
#     success = 0
#     fail = 0
#     for i in range(2):
#         print("第{}次".format(i + 1))
#         sex = input('请输入您的性别：')
#         age = int(input('请输入您的年龄：'))
#
#         re = sxw_ball(sex, age)
#         if re:
#             success += 1
#         else:
#             fail += 1
#
#     print('success={},fail={}'.format(success, fail))
