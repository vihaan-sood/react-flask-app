from init_db import db

class news (db.Model):

    __tablename__ = 'news'

    NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Article = db.Column(db.String(),unique=False, nullable=False)
    Heading = db.Column(db.String(),unique=False, nullable=False)
    Link = db.Column(db.String(),unique=False, nullable=False)



class classification (db.Model):

    __tablename__ = 'classification'

    ClassID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Class = db.Column(db.String(),unique=True, nullable=False)




class summaries (db.Model):

    __tablename__ = 'summaries'

    SumId = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Summary = db.Column(db.String(),unique=False, nullable=False)
    NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),db.ForeignKey("news.NewsID"))
    ClassID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),db.ForeignKey("classification.ClassID"))
    news_table_access = db.relationship("news", backref="news")





