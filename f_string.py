# 主要是记录 f_string 的使用方法
n: int = 10000
print(n)

# 用 f_string 来输出

print(f'{n:,}') # 在千分位上打上逗号

print(f'{n:_}') # 在千分位上打上_

var: chr = 'kkk'
print(var)

print(f'{var : >20}') #一直到var的最后一个数字一共输出20位数字

var_2 : chr = 'hhhhhhhhhhhhhhhhhhhhhhh'
print(f'{var_2 : >20}') # 如果输出字符串大于20个字符，则输出原来的字符串

print(f'{var:|^20}') 
print(f'{var:<^20}') # 将var居中输出并一共输出20个字符串

# 软编码
print(f'{var=}') #直接输出var='kkk'，避免变量改动时候对于输出的影响
