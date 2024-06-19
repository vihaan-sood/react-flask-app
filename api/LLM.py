from transformers import pipeline
import feedparser
import morss
import re
from init_db import create_app
from populate_db import addto_news, addto_summaries,addto_classification
import random



news_sites =[
    "https://www.independent.co.uk/news/uk/rss",
    "https://feeds.bbci.co.uk/news/uk/rss.xml",
    "https://feeds.skynews.com/feeds/rss/uk.xml"
    ]




#LLMprompt = "Following is a list of news articles in the format <Title> \n <Link>\n<Text>\n(---). Task is to summarise the given articles, give title and associated link, and to classify them. If the same news content appears in multiple articles, you are to take the most important parts from all duplicated articles, and in such a scenario, you may output any of the given links from the duplicated articles in your response. You may only classify an article into 3 categories: Sports, Politics and General. Give your response in the following manner: <Title>\n<Link>\n<Classification>\n<Summary>\n Input:"

Outputs = []

options = morss.Options(csv=True) # arguments

generator  = pipeline("summarization", model="facebook/bart-large",max_length = 30)


#print(generator("Summarise and Categorise:"))

entry_number = 0

app = create_app()

with app.app_context():
    addto_classification()
    for site in news_sites:

        url, rss = morss.FeedFetch(site, options) 
        rss = morss.FeedGather(rss, url, options) 

        output = morss.FeedFormat(rss, options, 'unicode') 
    
        feed = feedparser.parse(output)



        for entry in feed.entries:
            
                LLMprompt = ""

                title = entry.title
                link = entry.link
                content =  str(entry.summary)

                content = re.sub(r'<[^>]*>', "",content)
                #content = re.sub("\</.>", "",content)

                classificationID = random.choice(["1","2","3"])

                entry_number += 1

                addto_news(entry_number, content,title,link)

                #print(title+"\n"+link+"\n"+content)

                LLMprompt += content

                output = generator(LLMprompt)[0]
                output = output["summary_text"]

                addto_summaries(output,entry_number,classificationID)

                Outputs.append(output)

                #print(LLMprompt)

                print("output\n",output)
                print("###########")

    print(Outputs)

