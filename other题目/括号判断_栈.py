import os
import sys

# *(代表蓝, [代表黄, {代表红
# * 输入一串由({[构成的括号序列, 判断是否左右成对
# * 是, 输出颜色, 如
# *     输入: "{()}[]"
# *     输出: "红蓝蓝红黄黄"
# * 否, 输出"输入错误"
#
# *解题思路: 运用栈, 遇到左括号就入栈一个对应的右括号;
#           遇到右括号就看栈顶是不是和他一样的右括号, 不是就说明不成对.
#           最后判断栈是否为空, 不为空就说明最后入栈的是左括号, 且后没有配对的右括号入栈


def is_valid(st):
    if len(st) == 1:
        return False
    stack = list()
    for i in range(len(st)):
        ch_t = st[i]
        if '(' == ch_t:
            stack.append(')')
        elif '[' == ch_t:
            stack.append(']')
        elif '{' == ch_t:
            stack.append('}')
        else:  # 那就是右括号
            if len(stack) == 0:  # 栈中没有括号, 不能弹出栈顶值
                return False
            r = stack.pop()
            if ch_t != r:  # 或者不能够配对
                return False
    if stack:  # 栈不为空, 剩下左括号未匹配,无效
        return False
    else:
        return True


def color(st):
    res = []
    for i in range(len(st)):
        if st[i] == '(' or st[i]== ')':
            res.append('蓝')
        elif st[i] == '[' or st[i]== ']':
            res.append('黄')
        elif st[i] == '{' or st[i]== '}':
            res.append('红')
    print(''.join(res))


str_in = input()
flag = is_valid(str_in)
if flag:
    color(str_in)
else:
    print("输入错误")

