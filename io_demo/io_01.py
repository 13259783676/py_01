#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

#r只读
f = open('foo.txt','r')
print("文件名: ", f.name)
print("是否关闭", f.closed)
str = f.read()
print(str)
f.close()

#rb
f1 = open('fo.txt','rb')
print("文件名: ", f1.name)
print("是否关闭", f1.closed)
# str = f1.read().decode('utf-8')
print(str)
f1.close()

#w只写（会清除以前）
f2 = open('foo.txt','w')
f2.write("hello,python\n")
f2.close()

#x 创建文件，存在则不会再创建
# f3 = open('fo.txt','x')
# f3.write("hello,python\n")
# f3.close()

#a 追加模式【不可读；不存在则创建；存在则只追加内容；】
f4 = open('fo1o.txt', 'a')
f4.write('666\n')

#wb
f5 = open('foo.txt', 'wb')
f5.write(bytes)