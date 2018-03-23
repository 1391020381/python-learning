# windows和linux的目录结构
  * windows有分盘,linux没有,linux直接对应文件夹
  * bin
  * boot与开机有关
  * etc配置有关
  * dev和设备有关
  * lib与库有关
  * home<家目录,登录后的路径>
  * /home/ubuntu<根目录下的home文件夹下的ubuntu文件夹>
  * touch
  * mkdir
# 命令使用方法
  * Linux命令格式
     * command [-options] [parameter]  
     * ls /home(在对应文件夹下的东西)
     * ls -[选项]
     * 以.开头的文件是隐藏文件
     * ls -a (显示所有文件)
     * ls -l (以列表的格式显示)
     * ls -h -l -a等同于<ls -lah>
     * ls --help
     * man<manual> ls
     * gedit
     * cat<查看>
     * history
     * !40
     * clear
     * 通配符 *.js  ?.js
     * rm<删除>
        * -r 就是向下递归，不管有多少级目录，一并删除
        * -f 就是直接强行删除，不作任何提示的意思
        * 删除文件夹实例：
        * rm -rf /var/log/httpd/access
        * 将会删除/var/log/httpd/access目录以及其下所有文件、文件夹
        * 删除文件使用实例：
        * rm -f /var/log/httpd/access.log
        * 将会强制删除/var/log/httpd/access.log这个文件
  # 重定向  
    * ls > xxx.txt  
    * ls >> xxx.txt(重定向,ls命令的显示内容,会写到xxx.txt中, >>是追加)
    * ls -alh /bin | more
    * 管道 |
 # 相对路径和绝对路径
   * 相对路径<以pwd为基准 ./  ../>
   * 绝对路径(以 / 根目录为基准)
   * cd -
   * cd ~ <家目录>
   * 按两次 tab  键会显示有可以不全的结果
 # 文件夹
   * mkdir  
   * mkdir A/B/C -p  <自动创建  B再自动创建 C>
   * rmdir
   * rm 
 # 链接 
   * mv a.txt b.txt<重命名>
   * mv 111.txt laowang/
   * cp A  B<拷贝   -r 可以拷贝文件夹>
   * ln -s 1.txt 2.txt<软链接>
   * ln 1.txt 2.txt
   * cat 1.txt 2.txt > xxx.txt<合并> 
   * grep "ntfs" xxx.txt<搜索>
   * grip "^ntfs$" xxx.txt<正则匹配>


* find
# 归档管理 tar  
 * tar -cvf  test.tar *.js
 * tar -xvf test.tar 
 ## 压缩
  * ll <ls -la>
  *  tar -zcvf xxx.tar.gz *.js
  * tar -zxvf xxx.tar.gz
  * tar -cvJf yyy.tar.bz2  *.js
  * zip
  * which
# 系统管理
 * cal -y 2008
 * date
 * date > test.txt
 * date "+Y年%m月%n日"  
 * ps
   * ps -aux  <进程>
   * top
   * htop
   * kill -9 <pid>
  * reboot<重启> shutdown<关机> init  
# 磁盘
  * df
  * du<当前路径的情况>
# 网络相关
  * ipconfig
  * ping  
# 用户权限 
  * sudo useradd username -m
  * cat /etc/passwd  (sm32VcIRdwAf)
  * su justdoit <切换用户>
  *  sudo passwd justdoit<设置密码,密码设置成功后可以使用 su justdoit 登录 ,发现 ubuntu@VM变成了 justdoit@VM>
  * whoami<当前用户> 
  * exit<退出>
  * ctr  + shift  + t<新开一个标签> alt
  * sudo userdel justdoit
  * sudo userdel -r justdoit 
  * sudo -s <切换超级管理员 以  # 号开头>
  * 用户组 ll 命令中会显示 <文件拥有者,用户组>
  * groupadd YYY / groupdel YYY
  * groupmod 多次单击table出先所有组 cat /etc/group
  * 添加用户到某个组<添加到某个组,就该组的权限>
    * sudo usermod -a -G sudo justdoit
    * sudo usermod -a -G adm justdoit
  * chgrp<修改组>
  * chown<修改文件拥有者> 
  * ll命令的显示
    * 第一个字母是d这个文件是  文件夹
    * 文件拥有者的权限/同组的权限/其他人的权限 rwx<可读可写可执行>
## 修改权限
* u<user> g<group> o<other>
* chmod u=rwx 2.js   
* chmod u=r,g=r,o=r 2.js 
* r-4 w-2 x-1
  * chmod 137 2.js
# 编辑器  
## vim
1. 默认命令模式<任何模式,输入esc 切换 命令模式>
   * i / I 
   * a  /  A
   * o  / O 换行
   * yy(4yy) 复制   P 粘贴
   * dd(2dd)  剪切
   * D 剪切从当前光标到行尾   
   * h左 j k l
   * M当前屏幕的中间  H 当前上方   L 当前下面
   *  ctr + f<向下翻一页>  ctr+ b(向上翻)  
   * 20G<快速定位第20行代码>   
   * G <快速回到  整个代码的最后一行>
   * gg  <快速 回到第一行> 
   * w 向后跳一个单词的长度 
   * b  向前跳一个单词长度 
   * u 撤回
   * ctr + r 反撤销
   * 选中   V  v
   * >> 右移  << 左移
2. 编辑(插入模式),点击 i/a 键 切换到 编辑模式  esc  切换 命令模式  输入 英文冒号(:) 进入末行模式 ,再输入 wq保存退出。
3. 末行模式 

# ubuntu软件安装与卸载的方法
  1. 寻找国内镜像源
     * 清华大学TUNA镜像源
     * 点击  问号
     * 点击选择版本
     * 复制 版本的下的代码
  2. 备份Ubuntu默认的源地址
    * sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup<备份 系统自带的 sources.list>   
  3. 更新源服务器列表
    * sudo gedit /etc/apt/sources.list   <将源选择的 版本下的 地址  复制(先要删除掉原来的)到打开的框>
  4. 更新源  
    * sudo apt-get update 

  # Ubuntu软件操作的相关命令
  * sudo apt-get update 更新源
  * sudo apt-get install package 安装包
  * sudo apt-get remove package 删除包
  * sudo apt-cache search package 搜索软件包
  * sudo apt-get install package --reinstall 重新安装包
  * sudo apt-get build-dep package 安装相关的编译环境
  * sudo apt-get upgrade 更新已安装的包
  * sudo apt-get dist-upgrade 升级系统
  * sudo apt-cahe depends package  了解使用该包依赖哪些包
#  Linux常用服务器构建
1. ftp 服务器
* FTP是 File Transfer Protocol(文件传输协议)的英文简称。用于Internet上的控制文件的双向传输。同时，它也是一个应用程序（Application）。基于不同的操作系统有不同的FTP应用程序，而所有这些应用程序都遵守同一种协议以传输文件。
* 在FTP的使用当中，用户经常遇到两个概念："下载"（Download）和"上传"（Upload）。 
* FTP客户端 / FTP服务器
* sudo apt-get install vsftpd <安装vsftpd服务器>
* sudo vim /etc/vsftpd.conf  <配置 vsftpd.conf文件>
   * anonymous_enable = NO <不允许匿名用户登录>
   * local_root = /home/python/ftp  <指定ftp上传下载的目录>
   * local_enable = YES <允许本机登录>
   * chroot_list_file = /etc/vsftpd.chroot_list<允许  vsftpd_chroot_list文件中的用户进行登录FTP服务器>
   * write_enable = YES <允许上传文件到 FTP服务器>
   * sudo vim /etc/vsftpd.chroot_list <建立此文件 ,将 Ubuntu的一个用户名放到此文件中。放登录FTP服务器时的用户名。>
   * 将此 文件夹的拥有这的权限 减去 w
   * 在  家目录中  建立 一个文件夹<就是使用ftp客户端进行下载、上传时的文件夹>
