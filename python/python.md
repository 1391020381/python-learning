# Python基础
* 以 # 号 开头的语句是注释,可以是任意内容。
* '''  '''    """  """  多行注释
* #coding=utf-8
* #-*- coding:utf-8 -*-
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
 ## 定义函数
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
## 函数的参数
  * 位置参数
  * 默认参数
    * Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    * 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
  * 可变参数  
    * 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数     
    * *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。 
  * 关键字参数
    * 可变参数允许你传入0个或任意个参数,这些参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数数名的参数,这个关键字参数在函数内部自动组装为一个dict
    * def person(name,age,***kw)   
  * 命名关键字参数
    * def person (name,age,*,city,job)  
    * 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    *  person('Jack', 24, city='Beijing', job='Engineer')
    * 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
    *  def person(name, age, *args, city, job):
  * 参数组合
    * 在Python中定义函数,可以用 必选参数 默认参数,可以变参数,关键字参数 都可以组合使用  
  * 小结
    * 默认参数一定要用不可变对象
    *  *args  可变参数 args接受的是一个 tuple
    *  **kw 关键字参数 kw 接受的是一个dict 
    * 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    * 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。 
    * 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
    ## 递归函数
  # 高级特性  
   ## 切片 取一个list或 tuple的部分元素是非常常见的操作
   * L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
   * L = [1,2,3,4]
   * L[:10]
   * L[-10:]
   * L[10:20]
   * L[:10:2] 前10个数,每两个取一个
   * L[:] 复制一个L
   * tuple也可以用切片操作，只是操作的结果仍是tuple：
## 迭代
 * list tuple dict set str
 * generator 
 * isinstance()判断一个对象是否 Iterable对象
 * form collection import Iterable
 * isinstance([],Iterable)
# 函数式编程
  * 函数式编程的一个特点就是,允许把函数本身作为参数传入另一个函数,还允许返回一个函数
  * 高阶函数
     * map() reduce()     list() 
     * filter() sorted()
     * lambda x: x%n>0  
     * 返回函数
       * 高阶函数除了可以接受函数作为参数外,还可以把函数作为结果值返回
       * 闭包 
       * 返回的函数并没有立刻执行,而是知道调用了f()才执行
       * 
  ```
           def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
     
  ```
* 匿名函数
 * lambda x:x*x
 * 匿名函数有个限制,就是只能有一个表达式,不用写return 返回值就是该表达式的结果
 * 可以把一个匿名函数赋值给一个变量,再利用变量调用该函数
* 装饰器
  * 函数对象有一个__name__ 属性可以拿到函数的名字 
  * 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'
  * functools.wraps
 * 偏函数 
  *  Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。要注意，这里的偏函数和数学意义上的偏函数不一样。   
  * functools.partial就是帮助我们创建一个偏函数的
  * 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
  * 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
 # 模块 
  * 内置模块 第三方模块
  * 如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
  * 
 ```
 mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
 ```
 * 引入了包以后只要顶层的包名不与别人冲突,那所有模块都不会与别人冲突。现在,abc.py 模块的名字就变成了mycompany.abc 类似的,xyz.py的模块变成了mycompany.xyz
 * 请注意,每个包目录下面都会有一个__init__.py的文件,这个文件必须存在,否则,Python就把这个目录当成普通目录,而不是一个包 。__init__py 可以是空文件,也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。 
 * 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。   
 * 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
 ## 作用域
  * 在一个模块中,通过_ 前缀来实现私有变量
  * 类似 __xxx__这样的变量是特殊变量,可以被直接引用,但有特殊用途,比如上面的__author__
  * private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
##安装第三方模块
 * 在Python中,安装第三方模块,是通过包管理工具pip完成的。
 * 在 Mac或者 Linux安装 pip本身这个步骤就可以跳过了。
 * 如果你在使用Windows，确保安装时勾选了pip和 Add python.exe to path 
 * 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip
 * Anaconda
 * 模块搜索路径
   * 默认情况下,Python解释器会搜索当前目录,所有已安装的内置模块和第三方模块,搜索路径存放在sys模块的path变量中 
   *  Python版本的控制和第三方模块的管理
# 面向对象
  * 面向对象编程,简称 OOP,是一种程序设计思想。OOP把对象作为程序的基本单元,一个对象包含了数据和操作数据的函数。
  * class后面紧跟着是类名,即Student 类名通常是大写开头的单词,紧接着是(object)表示该类是从哪个类继承下来的,通常,如果没有合适的继承类就是使用 objec类这是所有类最终都会继承的类 
  * 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
  * 注意：特殊方法“__init__”前后分别有两个下划线！！！ 
  * 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
  * 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
  * 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
  ## 数据封装
  ## 小结
   * 类是创建实例的模板而实例则是一个一个具体的对象,各个实例拥有的数据都相互独立,互不影响；
   * 方法就是与实例绑定的函数,和普通函数不同,方法可以直接访问实例的数据
   * 通过在实例上调用方法,我们就直接操作了对象内部的数据,但无需知道方法内部的实现细节。
   * 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
  ## 访问限制
  * 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
  * def get_name  deg set_name
  * 需要注意的是,在Python中,变量名类似__xxx__的也就是以双下划线开头,并且以双下划线结尾的,是特殊变量,特殊变量是可以直接访问的,不是private变量,所以不能用 __name__ __score__这样的变量名。
  * 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
  * 双下划线开头的实例变量,其实是Python解释器对外把 __name 变量改成了 _Student_name 所以可以通过 -Student_name来访问_name变量
  * 一个下划线与两个下划线的区别。  privaite是双下划线开头   特殊变量是 双下划线开头并结尾    一个下划线,外面可以访问<但是这样变量的思意是,请把我视为私有变量,不要随意访问。>
  ## 继承和多太
   * 多态的好处就是,当我们需要传入Dog Cat Tortoise 时 我们只需要接受Animal 类型就可以了,因为Dog Cat Tortoise 都是Animal类型,然后,按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型,只要是Animal类或者子类,就会自动调用实际类型的run方法，这就是多态的意思:
   * 对于一个变量,我们只需知道它是Animal类型,无需确切地知道它的子类型,就可以放心地调用run()方法,而具体调用的run()方法作用在Animal Dog  Cat还是 Tortoise 对象上,由于运行时该对象的确切类型决定,这就是多态真正的威力:调用方只管调用,不管细节,而当我们新增一种Animal的子类时,只要确保run()方法编写正确,不用来管原来的代码是如何调用的。这就是著名的 开闭 原则
   ## 小结
   * 继承可以把父类的所有功能都直接拿过来,这样就不必重零做起,子类只需要新增自己持有的方法,也可以把父类不合适的方法覆盖重写。
   * 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
   ## 获取对象信息
   * type() 返回对应的Class类型
   * 使用isinstance()
   * 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
   * 使用dir()  获取一个对象的所有属性和方法  getattr()  setattr() hasattr()
   * 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。
   ## 实例属性和类属性
   * 由于Python是动态语言,根据类型创建的实例可以任意绑定属性。
   * 实例属性属于各个实例所有,互不干扰
   * 类属性属于类所有,所有实例共享一个属性
   * 不要对实例属性和类属性使用相同的名字,否则将产生难以发现的错误。
# 面向对象高级编程
   * 数据封装、继承和多态只是面向程序设计中最基础的3个概念。在Python中,面向对象还有很多特性,允许我们写出非常强大的功能。
   ## 使用 __slots__
  * 为了达到限制的目的,Python允许在定义class的时候，定义一个特殊的__slot__ 变量，来限制该class实例能添加的属性
  ```
  class Student(object):
        __slots__ = ('name','age')   # 用tuple定义允许绑定的属性名称
  ```
  * 使用__slots__ 要注意,__slots___定义的属性仅对当前的实例起作用,对继承的子类不起作用的。
  ## 使用 @property
  * 装饰器 decorator可以给函数动态加上功能。对与类的方法,装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
  # 多重继承
   * 通过多继承,一个子类就可以同时获得多个父类的所有功能。
   * class DogO(Manmal,Runnable)
   ## MixIn
   * 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

  * 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：
  * class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
 ## 定制类   
 ## 使用枚举类
 ## 使用元类
 # 错误、调试和测试
   ## 错误处理
   * 当我们认为某些代码可能出现错误时，就可以用try来运行这段代码,如果执行出错,则后续代码不会继续执行,而是直接跳转至错误处理代码,即except语句块,执行完except后,如果有finally语句块,则执行finall语句块,至此，执行完毕。
   * 没有错误发生,所以except语句块不会被执行,但是finally如果有,则一定会被执行(可以没有finall语句)
   * 错误应该有多种类,如果发生了不同类型的错误,应该由不同的except语句块处理。没错,可以有多个except来捕获不同类型额错误。
   * Python的错误其实也是class,所有的错误类型都是继承自BaseException,所以在使用except时需要注意的是,它不但捕获该类型的错误,还把其子类也'一网打尽'
   * 不需要在每个可能出错的地方出捕获错误,只要在合适的层次出捕获错误就可以了。这样可以减少写try...except....finally的麻烦。
   * 调用栈
   * 记录错误
     * 如果不捕获错误,自然可以让Python解释器打印出错误堆栈,但是程序也被结束了。既然我们能捕获错误,就可以把错误堆栈打印出来,然后分析错误原因,同时,让程序继续执行下去。
     * Python内置的logging模块可以非常容易第记录错误信息。通过配置,loggin还可以把错误记录到日志文件里,方便事后排查。
   * 抛出错误
     * 如果要抛出错误,首先根据需要,可以定义一个错误的class选择继承关系,然后用raise语句抛出一个错误的实例。  
     * Python内置的try...except..finally 用来处理错误十分方便。出错时,会分析错误信息并定位错误发生的代码位置才是关键的。
     * 程序也可以主动抛出错误,让调用者来处理相应的错误。但是,应该文档中写清楚可能抛出哪些错误,以及错误产生的原因
   ## 调试
   * print
   * 断言
     * 凡是用print()来辅助查看的地方,都可以用断言(assert)来代替,如果断言失败 assert语句本身就会抛出AssertionError
   * logging 把print()替换为logging是第三中方式,和assert比,logging不会抛出错误，而且可以输出到文件
     * import logging   logging basicConfig(level=logging.INFO)
     * logging的好处,它允许你指记录信息的级别,有debug，info，waring ,error等几个级别
     * logging的另一个好处是通过简单的配置,一条语句可以同时输出到不同的地方,比如console和文件。
   * Pdb pad.set_trace()
   * IDE
   ## 单元测试
     * 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检测的测试工作。
     * 单元测试通过后的意义,如果对某个函数代码做了修改,只需要再跑一遍单元测试,如果通过了,说明我们的修改不会对 该函数的原有的行为造成影响。如果测试不通过,说明我们的修改与原有行为不一致,要么修改代码，要么修改测试
 # IO编程    
  * IO在计算机中指的Input/Output,也就是输入和输出。由于程序和运行时的数据是在内存中驻留,由于CPU这个超快的计算机核心来执行,涉及到数据交换的地方,通常是磁盘、网络等,就需要IO接口。
  * IO编程中,Stream(流)是一个很重要的概念,可以把流想象成一个水管,数据就是水管里的水,但是只能单向流动。Input Stream就是数据从外面(磁盘网络)流进内存,Output Stream就是数据从内存流到外面去。
  * 由于CPU和内存的速度远远高于外设的速度,所以,在IO编程中,就存在严重不匹配的问题。比如要把100M的数据写入磁盘,CPU输出100M,CPU输出100M的数据只需要0.01秒,可是磁盘要接受这100M数据可能需要10秒
  * 同步IOds
  * 异步Io
  * 操作IO的能力都是由操作系统提供的,每一种编程语言都会把操作系统提供的低级C接口封装起来方便使用,Python也不例外。
  ## 文件读写
   * 读写文件是最常见的IO操作。Python内置了读写文件的函数,用法和C兼容的。
   * 读写文件前,我们先必须了解一下,在磁盘上读写文件的功能都是有操作系统提供的,现代操作系统不允许普通的程序直接操作磁盘,所以,读写文件就是请求操作系统打开一个文件对象(通常称为文件描述符)，然后,通过操作系统提供的接口从这个文件对象读取数据(读取文件),或者把数据读写入这个文件对象中(写文件)
   * 文件使用完毕后必须关闭,因为文件对象占用操作系统的资源,并且操作系统同一时间能打开的文件数据量也是有限的。
   * 调用read()会一次性读取文件的全部内容，如果文件有10G,内存就爆了,所以,要保险起见,可以反复调用read(size)方法,每次最多读取size个字节的内容。另外,调用readline()可以每次读取一行内容,调用readlines()一次读取所有内容并安行返回list
   ## file-like Object
   * 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
   ## 二进制文件
   * 前面讲的默认都是读取文本文件,并且是UTF-8编码的文本文件。要读取二进制文件,比如图片、视频等等,用'rb'模式打开文件即可
   ## 字符编码
   * 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
   * f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
   ## 写文件
  * 写文件和读取文件是一样的,唯一区别是调用open()函数时,传入标识符 'w'或者'wb'表示写文本文件或写二进制文件
  *  f = open('text/txt,'w')
  * 你可以反复调用write()来写入文件,但是务必调用f.close()来关闭文件。当我们写文件时,操作系统往往不会立即把数据写入磁盘,而是放到内存缓存起来,空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘,剩下的丢失了。所以，还是用with语句来得保险
  * width open(text.txt) as f: f.write('hello,world')
  * 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
  * 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
  ## StringIO
  * 数据读写不一定是文件,也可以在内存中读写。
  * StringIO顾名思义就是在内存中读写str
  ```
  from io import StringIO
  f = StringIO()
  f.write('hello')
  f.write('')
  f.write('world')
  print(f.getvalue())
  ```
  ## BytesIO
  * StringIO操作额只能是st如果要操作二进制数据,就需要使用BytesIO
  ## 操作文件和目录
  * Python内置的os模块也可以直接调用操作系统提供的接口函数
   * os.name 是posis说明系统是Linux、Unix或者Mac OS X如果是nt就是Windows系统
   ## 环境变量
   * 在操作系统中定义的环境变量,全部保存在os。environ这个变量中。
   * os.environ.get('key')
   ## 操作文件和目录
   * os.path.abspath('.')  # 查看当前目录的绝对路径
   * os.path.join('/user/a','textdir')   '/usser/a/textdir'
   * os.mkdir('/users/a/testdir')
   * os.rmdir('/user/a/testdir')
   * os.path.split('/user/a/testdir/file.txt')   ('user/a/testdir',file.txt)
   * os.path.splitext()  # 获取扩展名
   * os.renname('')
   * os.remove()
   ## shutil
   * copyfile(s)
   ## 序列化
   * 我们把变量从内存中变成可存储或传输的过程称为序列化。序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
   * 把变量内容从序列化的对象重新读到内存里称为反序列化
   * 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
   * d = dict(name='Bob', age=20, score=88)
   * 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'
   ## JSON
   * import json
   * dumps()
   ##小结
   * Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
   * json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
   # 进程和线程
  * 多任务就是操作系统可以同时运行多个任务。
  * CPU执行代码都是顺序执行的,操作系统轮流让各个任务交替执行。由于CPU的执行速度实在太快了,感觉就是同时执行一样。
  * 对于操作系统来说,一个任务就是一个进程(Process),在一个进程内部,要同时干多件事,就要同时运行多个 子任务,我们把进程内的这些子任务称为线程。
  * 由于每个进程至少要干一件事,所以,一个进程至少有一个线程。多个线程可以同时执行,多线程的执行方式和多进程是一样的,也是由操作系统在多个线程之间快速切换,让每个线程都短暂的交替运行,看起来就像同时执行一样。当然,真正同时执行多个线程学啊哟多核CPU才能实现。
  # 同时执行多个任务
   * 一种是启动多个进程，每个进程虽然只有一个线程,但多个进程可以一块执行多个任务。
   * 启动一个进程,在一个进程内启动多个线程,这样,多个线程也可以一块执行多个任务。
   * 综合以上
   ## 小结
  * 线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程,完全由操作系统决定,程序自己不能决定什么时候执行,执行多长时间。
  * 多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂。
  ## 多进程
  * Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
  * 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
  * 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
  * multiprocessing
     * 创建子进程时,只需要传入一个执行函数和函数的参数,创建一个Process实例,用start方法启动
     * p = Process(target=run_proc,args=('test'))
     * p.start()
     * p.join() 可以等待子进程结束后再继续往下执行,通常用于进程间的同步。