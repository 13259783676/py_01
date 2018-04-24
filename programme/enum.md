### 枚举
```
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以直接使用Month.Jan来引用一个常量
for name,nn in Month.__members__.items():
    print(name,nn.value,'月')
```
value属性则是自动赋给成员的int常量，默认从1开始计数。
