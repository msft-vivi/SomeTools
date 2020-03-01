### 命令
* 启动服务器  
```python manage.py runserver [-r -d --host --port --threaded]```

* 数据迁移
```
$ python manage.py db init 迁移数据库，会在项目根目录生成migrations文件夹
$ python manage.py db migrate 
$ python manage.py db upgrade
$ python manage.py db --help
```
经过试验发现，不运行db.create_all，直接运行迁移命令也可以创建相应的表
### 遇到的一些问题
* db.create_all() 或者 数据迁移migrate 无效？  
需要在manage.py文件导入models里面定义的ORM对象

* db.create_all执行报错  
运行命令前面需要给出当前的应用上下文
```python
with app.app_context():
    db.create_all()
```

 
