### 快捷键
double shift 在所有文件（包括各种第三方库）搜素，可以用于快速搜素函数，类
。结合pycharm 左上册的类似‘瞄准器’的按钮快速定位其所在的Python文件位置,最左边下方还有个Structure命令，它能给出该文件的框架结构


### 技术
* from flask_session import Session 引入插件Session
把cookie持久化存储在redis里面
* 需要安装redis服务器（不是pip install redis），而是安装在主机的redis数据库，并且需要redis-server启动服务器
* 如果不想用redis做cookie持久化：
    *   1.把App/exts.py 如下代码删除：
        ```sess.init_app(app)```
    *   2.把APP/config.py与SESSION有关的代码删除
        ```
         SESSION_TYPE = 'redis'
	     SESSION_COOKIE_SECURE = True
        ``` 
### 问题

* Can't locate revision identified by 'a35957c88abb'  
之前一个项目使用migrate创建了数据库表未删除，用另一个项目链接同一个数据库会出现migrate 版本不一致问题
删除了之前的表重新执行一遍就行了

* session 配置问题
    * SESSION_TYPE='sqlchemy'会有数据库问题
    * SESSION_USE_SIGNER = True 会导致session失效
* [配置Flask html 补全问题](https://blog.csdn.net/weixin_30491641/article/details/95857585?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)

* 如何下载bootstrap中的css、js等源代码保存到本地项目  
    * 直接复制文件地址（国外的），然后到浏览器打开，全选后保存到自己命名的文件内就行了

### 数据库问题
* db.session.execute(sql)
    * int 类型占位符 %s 不需要加单引号
    * string类型占位符 %s 要 加单引号 '%s'
### 关于前端页面的问题
* 如何基于原有的bootstrap样式修改（覆盖+增加）
    * 以设置container最大宽度为例子
    * 在外面自定义calss='auth-container'
    * 在css 文件设置 .auth-container .container {...}
    
* 浏览器缓存问题导致css/js文件不能即使生效
    * Ctrl + F5 强制刷新页面（最简单快捷方式）
    * 清除cache
* sr-only 属性
    * 对正常人不可见，给’屏幕‘看的
    * 可以用在label上
    
### 相关网站
* [bootstrap icons](https://icons.getbootstrap.com/)
