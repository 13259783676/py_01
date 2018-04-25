### 1.datetime
from datetime import datetime
- 获取当前日期和时间  
```
now=datetime.now()
print(now)
print(type(now))
```
- 获取指定日期和时间
```
dt=datetime(2018,1,15,10,10,10)
print(dt)
2015-04-19 12:20:00 
```

- datetime timestamp互转
```
dt1=datetime(2018,1,15)
t=dt1.timestamp()
print(t)
dt2=datetime.fromtimestamp(t)
print(dt2)
```

- str datetime 互转
```
cday=datetime.strptime('2018-01-05 12:00:12','%Y-%m-%d %H:%M:%S')
print(cday)
print(type(cday))
strday=cday.strftime('%a, %b %d %H:%M')
strday=cday.strftime('%Y-%m-%d %H:%M:%S')
print(strday)
```
- 时间加减
```
now_time=datetime.now()
print(now_time)
now_time = now_time + timedelta(days=1, hours=10)
print(now_time)
```


### 2.collections
- namedtuple
```
point=namedtuple('point',['x','y'])
p=point(1,2)
print(p.x)
```

- deque
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了。deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
```
dq=deque(['a', 'b', 'c'])
dq.append('d')
dq.appendleft('0')
```

- defaultdict
使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
```
dd = defaultdict(lambda : 'N/A')
dd['name']='bill'
print(dd['name'])
print(dd['grade'])
```

- OrderedDict  
使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。如果要保持Key的顺序，可以用OrderedDict
  OrderedDict的Key会按照插入的顺序排列，不是Key本身排序

- Counter  
Counter是一个简单的计数器，例如，统计字符出现的个数
```
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)
```

### 3.base64
```
b_en=base64.b64encode(b'binary\x00string')
print(b_en)
b_de=base64.b64decode(b_en)
print(b_en)
```

### 4.struct



### 5.hashlib


### 6.hmac
hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
```
message = b'keys'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())
```

### 7.itertools
- count()
```
natuals = itertools.count(1)
for n in natuals:
    print(n)
```

- cycle()  
cycle()会把传入的一个序列无限重复下去
```
ce = itertools.cycle('ABC')
for n in ce:
    print(n)
```

- repeat()  
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
```
rt = itertools.repeat('ABC',3)
for n in rt:
    print(n)
```

- takewhile()   
```
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<99,natuals)
for n in ns:
    print(n)
```

- chain()  
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
```
ch = itertools.chain('ABC','XYZ')
for n in ch:
    print(n)
```

- groupby()  
groupby()把迭代器中相邻的重复元素挑出来放在一起
```
for key,group in itertools.groupby('AAABBBCCDDD'):
    print(key, list(group))
```


### 8.contextlib


### 9.urllib
- get  
发送
```
with request.urlopen('https://api.douban.com/v2/book/1220562') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s'% (k, v))
    print('Data:',data.decode('utf-8'))
```
模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头(模拟iPhone 6)
```
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
```
- post
```
with request.urlopen(req,data.encode('utf-8')) as f:
```

### 10.XML

### 11.HTMLParser
