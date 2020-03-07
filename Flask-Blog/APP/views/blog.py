# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:58
# @Author : Bravezhangw
# @File : blog.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Blueprint, render_template, url_for, request, session, abort, flash, redirect, g
from sqlalchemy import text

from APP.exts import db,login_required
from APP.models import User,Post
bp2 = Blueprint("blog",__name__,url_prefix="/blog")

@bp2.route("/home/")
def home():
    # posts = db.session.execute(
    #     "SELECT p.id, title, body, created, author_id, username"
    #     " FROM post p JOIN user u ON p.author_id = u.id"
    #     " ORDER BY created DESC"
    # ).fetchall()
    # print(posts)
    # page = request.args.get("page", 1,type=int)
    # posts = Post.query.offset(per_page*(page-1)).limit(per_page)
    # posts = Post.query.paginate() # 返回一个对象提供迭代方法
    per_page = request.args.get("per_page", 5, type=int)
    pagination = Post.query.order_by(text('-created')).paginate(per_page=per_page) # 可以直接取元素

    return render_template('blog/home.html',pagination=pagination,per_page=per_page)

@bp2.route("/author/")
def author():
    username = session.get('username')
    password = session.get('password')
    print(session)
    # username = request.cookies.get('username')
    # password = request.cookies.get('password')
    return render_template('blog/author.html',username=username,password=password)



@bp2.route("/create/",methods=['GET','POST'])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            '''
                这里不能使用db.session.execute(sql
                原因：
                Post表中有created时间是默认时间，这里的默认时间实际上是sqlchemy在事务提交的时候插入的
                并非真正的默认，如果使用自己写的sql语句，也就必须把时间一同提交，否则sql表中没有数据
            '''
            post = Post(title=title,body=body,author_id=g.user.id)
            db.session.add(post)
            db.session.commit()

            return redirect(url_for("blog.home"))

    return render_template("blog/create.html")


@bp2.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            post = Post.query.filter_by(id=id).first()
            post.title = title
            post.body = body
            db.session.add(post)
            db.session.commit()
            # db.session.execute(
            #     "UPDATE post SET title = %s, body = %s WHERE id = %s"% (title, body, id,)
            # )
            # db.session.commit()
            return redirect(url_for("blog.home"))

    return render_template("blog/update.html", post=post)

@bp2.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a post.
    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db.session.execute("DELETE FROM post WHERE id = %s" % (id,))
    db.session.commit()
    return redirect(url_for("blog.home"))


'''
    function
'''
def get_post(id, check_author=True):
    # 验证该Blog是否存在同时验证是否是当前用户发布的blog
    """Get a post and its author by id.
    Checks that the id exists and optionally that the current user is
    the author.
    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """

    post = (
        db.session.execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = %s" % (id,)
        ).fetchone()
    )

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post["author_id"] != g.user.id:
        abort(403)

    return post




'''
    测试分页路由
'''
@bp2.route("/addblog/")
def add_blog():
    title = "Alice"
    content = 'Be sure to have your pages set up with the latest design and development standards. That means using an HTML5 doctype and including a viewport meta tag for proper responsive behaviors. Put it all together and your pages should look like this:'
    for i in range(30):
        post = Post(author_id=1,title=title,body=content)
        db.session.add(post)
        db.session.commit()
    return "Add blog success."

@bp2.route("/getblog/")
def get_blog():
    page = request.args.get("page",1,type=int)
    per_page = request.args.get("per_page",4,type=int)
    dogs = Post.query.offset(per_page*(page-1)).limit(per_page)
    pass

