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