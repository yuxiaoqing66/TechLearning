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
  - for ...in...有区别
    - for(var key in o)
    - 若o是json对象，key是o的键值
    - 若o是数组，则key是序列号
  - ES6新标准
    - 对于Array,Map,Set等iterable类型：for...of..
    - for..of..与for...in..区别：
      - for..of..直接循环元素
      - for..in..循环属性
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
  - '',0,NaN,null,undefined被视为false
- null：空类型，与[],""不是同一类型，表示对象值未定义
  - 可以用于赋值，`var a=null;`
  - 可以参与运算，值为0
  - 参与布尔运算时视为false
- undefined: 例如 `var m;`此时m就是一个undefined类型
  - 已声明赋值的变量
  - 不存在的数组索引或者对象属性
  - 未提供的参数
  - 未返回的返回值
  - 无法参与计算，计算结果为NaN
- 数组
  - 定义方法

    - `var a=[1,2,"san",null,true]`
    - `var arr = new Array(1,2,3)`
    - ```javascript
      var arr =[1,2,3,"hello",null];
      arr.splice(2,3,"hi","Lily");	//返回[3,"hello"],arr变为[1,2,"hi","Lily",null]
      arr.splice(2,2);	//返回["hi"],arr变为[1,2,"Lily",null]
      arr.splice(2,0,'Good','Morning')	//返回[],arr变为[1,2,"Lily",null,'Good','Morning']
      ```
    - ```javascript
      var arr=[1,2,3,"hello",null];
      var arr1 = arr.slice(0,3);     //[1,2,3]
      var arr2 = arr.slice(3); 	//["hello",null]
      var arr3 = arr.slice();		//[1,2,3,"hello",null]
      //使用slice()复制的数组是一个新的数组，与原本的数组不共用存储空间
      ```
    - concat():向数组后面连接另一个数组
  - 使用方法

    - `a[0]`（从0开始）
    - `a.length`
    - 当给array的length赋值时会使得array长度变化，新增的元素为undefined,多的元素则被删去
    - 当通过索引赋值，且索引超出范围时，array大小也会变化，新增元素为undefined
    - `a.sort()`会对数组元素进行排序生成一个新的数组
    - `a.reverse()`会对数组元素做反转
    - a.join('-'):返回一个用-连接各元素的字符串
- 对象
  - 定义方法
    - `var person={name:'Bob',age:20,tags:['tall','strong','brown'],"foot-size":45};`
  - 使用方法
    - `person.name`
    - `person["foot-size"]`
    - 访问不存在的属性时返回undefined
    - 判断某个属性是否在对象中：
      - `'name' in person  //true`
      - in判断的属性可能是继承得到的
      - `hasOwnProperty('name')`可以判断本身拥有的属性，继承来的属性不计算在内
- 变量
  - 定义方法
    - var
      - 不被域限制({})
      - 被函数体限制，函数体内则为函数内局部变量，函数体外则为全局变量
    - let
      - 被域限制
    - const
      - 定义时赋值，一旦赋值，无法再次赋值
      - 被赋予的值能够更改，只是无法再用赋值罢了
- ES6引入
  - Map: 键值对的数组
    - `var m = new Map([['Bob',177],['Miseal',175],['Brownth',188]]);`
    - `m.get('Brownth') 	//188`
    - `m.set('Alice',166);	//添加新的键值对`
    - `m.set('Bob',176);	//修改已有键值对`
    - `m.has('Bob');	//true`
    - `m.delete('Bob');	//删除Bob这组键值对`
  - Set: key的集合，不能重复，无序
    - `var s = new Set([1,2,2,3,'3']);	//s=[1,2,3,'3']`
    - `s.add(4);	//向s中添加新的key`
    - `s.delete(3);	//删除s中的key`
  - iterable类型，下属有Array,Map.Set，方法有：
    - for...of...
    - ES5.1标准：forEach()
    - ```javascript
      var s = new Set(['a','b','c'])
      s.forEach(function(element,sameElement,set){
      	//element是元素；
      	//set是set本身
      })

      var a=['a','b','c'];
      a.forEach(function(element,index,array){
      	//element是元素；index是索引；array是数组本身
      })

      var m = new Map([['alice',155],['bob',177],['Lily',172]]);
      m.forEach(function(value,key,map){
      	//value是键值对的第二个元素,key是键值对的第一个元素，map是map本身
      })
      ```

#### 函数

- 定义
  - `function 函数名(参数列表){函数体}`
  - `var func1 = function(参数列表){函数体};	//这里func1就是函数名`
- 传参
  - 参数多于所需参数，则多的参数会被忽略，不报错
  - 参数少于所需参数，有时返回NaN，也不报错
  - function内部默认定义了一个数组，名称为arguments，内部存了所有的参数
  - ES6引入rest参数：`function(a,b,...rest){};//rest就是除了a,b以外传入的参数数组`
