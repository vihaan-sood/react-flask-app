from init_db import db

class news (db.Model):

    __tablename__ = 'news'

    NewsID = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),primary_key = True)
    Article = db.Column(db.String(),unique=False, nullable=False)
    Heading = db.Column(db.String(),unique=False, nullable=False)
    Link = db.Column(db.String(),unique=False, nullable=False)



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



if __name__ == "__main__":
    with app.app_context():
        db.create_all()


def addto_classification():
    with app.app_context():
        class1 = classification(Class = "Sports")
        class2 = classification(Class = "Politics")
        class3 = classification(Class = "General")
        db.session.add_all([class1,class2,class3])
        db.session.commit()


def addto_news(entry_number,article,heading,link):
    with app.app_context():
        news_object = news(NewsID = entry_number ,Article = article,Heading = heading,Link = link)
        db.session.add(news_object)
        db.session.commit()

def addto_summaries(summary,entry_number):
    with app.app_context():
        summary_object = summaries(Summary = summary, NewsID = entry_number)
        db.session.add(summary_object)
        db.session.commit()


if __name__ == "__main__":
    db.init_app()
    app.run(debug=True)