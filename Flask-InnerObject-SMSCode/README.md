# 四大内置对象
### 钩子函数 

* app 级别优先级高于蓝图级别
* app级别
    * @app.before_request
        * 统计
        * 优先级
        * 反爬
            * 频率
        * 用户认证
        * 用户权限
        * 从session加载信息（加载信息保存到g）
        * 打开数据库连接
    * @app.before_first_request
        * 只在第一个请求触发
        
    * @app.after_request
        * 需要返回response
        
    * @app.teardown_request
        * 请求上下文被pop时执行
     
    * g 在before_request中设置值
    
* 蓝图级别
    * @bp1.before_request
        * 对此蓝图下的视图函数有用
    * @bp1.before_app_first_request
        * 等同于app.before_first_request
    * @bp1.before_app_request
        * 等同于app.before_request
    * @bp1.after_app_request
        * 等同于app.after_request
    * @bp1.after_request
        * 对此蓝图下的视图函数有用
  
### config 对象

* app 启动之后调用
* 调用方法
    * 在templates里面直接调用config
    * current_app.config 获取config对象
    
### g 对象

* 跨函数传递数据
* 间接传递数据

### request

# 短信邮箱验证登录
### 邮箱验证
* 发邮件之前需要配置客户端邮箱服务器，从网易或者QQ邮箱获得授权码
* 异步发送邮件
* 在邮件中包含发送地址
    * 接受一次性的token
    * token是用户注册的时候生成的,存储在cache中
    * key-value形式的token
        * key是token
        * value 用户的一个唯一表示
            * id
            * 用户名
            * 邮箱地址

### 短信
* 同步操作
* 步骤
    * 发送验证码请求
    * 缓存用户信息
        * key value 形式
        * key 可以是用户名
        * value 是获取的验证码
    * 用户获取验证码，在注册界面验证
         
