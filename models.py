# models.py
from sqlalchemy import Table, Column, Integer, Text
from sqlalchemy.orm import mapper
from database import metadata, db_session

class BlogPost(object):
    query = db_session.query_property()
    def __init__(self, id=None, title=None, post=None):
        self.id = id
        self.title = title
        self.post = post

blog_posts = Table('blog_posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', Text),
    Column('post', Text)
)

mapper(BlogPost, blog_posts)
