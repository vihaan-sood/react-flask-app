import sqlalchemy
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = sqlalchemy(app)

class news (db.Model):

    __tablename__ = 'news'

    NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Article = db.Column(db.String(),unique=False, nullable=False)
    Heading = db.Column(db.String(),unique=False, nullable=False)
    Link = Heading = db.Column(db.String(),unique=False, nullable=False)




# class links (db.Model):

#     __tablename__ = 'links'

    
#     LinkID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
#     Link = db.Column(db.String(),unique=False, nullable=False)
#     NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),db.ForeignKey("news.NewsID"))
#     news_table_access = db.relationship("news", backref="news")



class classification (db.Model):

    __tablename__ = 'classification'

    ClassId = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Class = db.Column(db.String(),unique=True, nullable=False)




class summaries (db.Model):

    __tablename__ = 'summaries'

    SumId = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Summary = db.Column(db.String(),unique=False, nullable=False)
    NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),db.ForeignKey("news.NewsID"))
    news_table_access = db.relationship("news", backref="news")