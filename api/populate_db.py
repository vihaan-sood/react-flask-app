from database import db,news,classification,summaries


def init_db(app):
    with app.app_context():
        db.create_all()
        addto_classification()
        


def addto_classification():
    with db.session.begin():
        class1 = classification(Class = "Sports")
        class2 = classification(Class = "Politics")
        class3 = classification(Class = "General")
        db.session.add_all([class1,class2,class3])
        db.session.commit()


def addto_news(entry_number,article,heading,link):
    with db.session.begin():
        news_object = news(NewsID = entry_number ,Article = article,Heading = heading,Link = link)
        db.session.add(news_object)
        db.session.commit()

def addto_summaries(summary,entry_number):
    with db.session.begin():
        summary_object = summaries(Summary = summary, NewsID = entry_number)
        db.session.add(summary_object)
        db.session.commit()