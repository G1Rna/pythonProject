# int  +-*/ // % **(幂)
# bit_length() 一个int数的二进制长度
a = 4
print(a.bit_length())

# bool
#类型转换后，所有空的集合都是False，0，null'也是False

# str
#索引从0开始
#str[x] 可以取道String下X位的字母 X可以用负，即倒数
#str[start,end，step]切片  包括start不包括end start<=end  str[start,end,1/-1] 1为从左往右读，-1为从右往左 同样包括start不包括end
#回文
s=input("请输入：")
if s == s[::-1]:
    print("是回文")
else:
    print("不是回文")
    print("不是回文")
#方法都是返回，不对原字符串进行改变
s1 = s.capitalize()#规范化  #s.upper()大写 s.lower()小写 swapcase()大小写互换 title()被特殊字符隔开首字符大写(中文也算特殊字符)
print(s)
print(s1)
#str.center(10,"*")在长度为10的字符串中居中，并且其他位置用*代替
#str.strip()去除左右两侧的空字符
#str.replace(xxx,yyy)替换字符串中的xxx变成yyy
#.split()切割
s2 = s.split(" ")
print(s2[1])
#str.startwith()开头存在 return bool，endwith() 结尾存在 return bool，count() 计数 return int，find()寻找，没有则返回-1
#.index() 找索引位置同find,但是不存在时会报错

len(s)
print(len(s2))
#return 返回长度  内置函数
#循环字符串
for si in s:
    print(si)

print("--------------list----------------")
# list 列表
lst = ["aaa","bbb"]
# lst.append("")最后一位
# lst.insert("xxx",step)按照step位置插入
#lst.remove("aaa")

#lst.pop(0)#从后开始取出
# del lst[1]# list 直接删除
#lst[0] = 'ccc' 根据索引直接修改
print(lst)
#循环列表
for el in lst:
    print(el)
# lst.sort(reverse=True) #排序(倒叙)

# dict 字典 类似map
print("--------------dict----------------")
d = {"x":"xx","y":"yy"}
# d["x"] ="zz"#替换
print(d.get("x"))
# dic.update(dic2)#根据dic2中相同的key更新dic中的value dic2中不存在dic的key-value会直接添加到dic中

# set 集合 只存放数字
# tuple 元祖 同列表，但不可变，不可增不可减，不可改变
tu = ("aaa","bbb")
#[]创建list ()创建tuple
#tu = tuple() 空元祖创建


