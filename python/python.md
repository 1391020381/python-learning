# Python基础
* 以 # 号 开头的语句是注释,可以是任意内容。
* 一个语句以冒号 ：结尾时,缩进的语句视为代码块
* 大小写敏感
## 数据类型和变量
 1. 数据类型
   * 整数
   * 浮点数
   * 字符串  转义符 \  input()输入的是字符串
      * print('''line1
...line2
....line3''')
   * 布尔值  True False   
      *  and or not运算
   * 空值 None   
  2. 变量 
    * 同一个变量可以反复赋值,而且可以是不同的类型的变量。
    * a = 'ABC'
      * 在内存中创建一个 'ABC'的字符串
      * 在内存中创建一个名为 a的变量,并把它指向 'ABC'
  3. 常量    
     * 通常用全部大写的变量名表示常量
  ## 小结
   * Python 支持多种数据类型,在计算机内部,可以把任意数据都看成一个'对象',而变量就是在程序中用来指向这些数据对象的， 对变量赋值就是把数据和变量给关联起来。
   * 对变量赋值 x =y 是把变量 x指向真正的对象,该对象是变量y所指向的。  随后对变量 y的赋值不影响变量 x的指向。
   * python 的整数没有大小限制,浮点数也没有但超出一定范围直接限时inf
 ## 字符编码和编码   
 * 因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。
 * ASCII  GB    2312  Unicode  UTF-8
   * 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
   * Python对bytes类型的数据用带b前缀的单引号或双引号表示：x = b'ABC'要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
   *  #!/usr/bin/env python3 为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
   *  # -*- coding: utf-8 -*-  告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
   * 格式化输出
     * %
     * format()
## 使用list和 tuple
1. list是一种有序的集合，可以随时添加和删除其中的元素   
   * list 是一个可变的有序表，list 里面的元素的数据类型也可以不同,也可以是个List
   * items.append('a') 追加
   * items.insert(1,'a')   插入
   * items.pop() 删除List末尾的元素
   * itmems.pop(i) 删除指定位置的元素
   * 都改变原来的List
 2. 元组 tuple 一旦初始化就不能修改.
   * 无 append() insert方法  
   * oTuple = (1,2,3) 
   * 只有一个元素的tuple定义时必须加个逗号  oTuple = （1,）
   * 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
## 条件判断 
   * if else elif  
   * input() 返回的数据类型是str  str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
## 循环   
  * for in
  * while
  * break 在循环中，break语句可以提前退出循环
  * continue 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
## 使用dict和set  
1. dict <字典  {a:1,b:3}>  
  * in判断Key是否
  * d.get('a') 通过dict提供的get()方法，如果key不存在，可以返回None
  * d.pop('a')
  * dict内部存放顺序和Key放入的顺序是没有关系的
  * dict的key必须是不可变对象。
  *  通过key计算位置的算法称为哈希算法（Hash）。
# 函数
  * 在Python中定义一个函数要使用def语句,一次写出函数名、括号、括号中的参数冒号：然后,在缩进中编写函数体,函数的返回值用retrun 语句返回
  ```
  # -*- coding: utf-8 -*-
  def my_abs(x):
      if x >=0:
          return x
      else:
          return -x    
  ```  
   * 空函数  
      * pass
   * 参数的检查
      * raise TypeError('bad operand type')
   * 返回多个值
      * 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple   
      * 函数执行完毕也没有return 语句时,自动return None
