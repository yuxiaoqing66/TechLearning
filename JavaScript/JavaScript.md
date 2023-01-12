# JavaScript

## 使用

HTML中 `<script></script>`标签内使用JavaScript
多个 `<script></script>`按先后顺序依次执行

允许外链，`<script src="xxx.js"></script>`

## 基本语法

### 与c相似的部分

和c一样的语法有：

- 表达式，以;结尾
- if,else if结构
- for循环结构
  - 遍历json对象时有区别
- while,do while结构
- 布尔表达式
  - 新增===判断符：与==的区别是，==会自动做类型转换，===为真当且仅当类型相同且值相同

### 区别于c的部分

#### 数据结构

- Number
  - 除了int, float, 指数之外（javascript中不对这些做区分，都是number类型）
  - 新增NaN: 无法计算结果时表示为NaN
    - NaN===NaN为false，判断为NaN只能使用isNaN()函数
  - 新增Infinity: 超出javascript能表达的最大值时表示为Infinity
- 字符串
  - ES6新标准
    - 反引号（ `此为字符串内容`）括起来，可以表示多行字符串（`这是多行字符串 这是第一行 这是第二行`），可以插入变量（`你好，{name}!`）
  - 字符串方法
    - substring(): 生成子串，例如（substring(7):从序号为7的字符开始到结束的子串（序号从0计算）；substring(0,5):序号从0到5的子串）
    - indexOf()：查找子串，例如（var hello_str = "hello world"; hello_str.indexOf('world')值为7）
      - 有多个结果时只返回第一个匹配项的序号
      - 没有找到结果时返回-1
- 布尔值
  - 只有两个false,true
  - 布尔表达式会被计算为false或者true
- null：空类型，与[],""不是同一类型，表示对象值未定义
  - 可以用于赋值，`var a=null;`
  - 可以参与运算，值为0
- undefined: 例如 `var m;`此时m就是一个undefined类型
  - 已声明赋值的变量
  - 不存在的数组索引或者对象属性
  - 未提供的参数
  - 未返回的返回值
  - 无法参与计算，计算结果为NaN
- 数组
  - 定义方法

例如：
