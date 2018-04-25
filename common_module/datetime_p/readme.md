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


