from transformers import pipeline,Conversation
import feedparser
import morss 
import numpy as np


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM




news_sites =[
    "https://www.independent.co.uk/news/uk/rss",
    "https://feeds.bbci.co.uk/news/uk/rss.xml",
    "https://feeds.skynews.com/feeds/rss/uk.xml"
    ]




#LLMprompt = "Following is a list of news articles in the format <Title> \n <Link>\n<Text>\n(---). Task is to summarise the given articles, give title and associated link, and to classify them. If the same news content appears in multiple articles, you are to take the most important parts from all duplicated articles, and in such a scenario, you may output any of the given links from the duplicated articles in your response. You may only classify an article into 3 categories: Sports, Politics and General. Give your response in the following manner: <Title>\n<Link>\n<Classification>\n<Summary>\n Input:"

Outputs = ["Summarise and Categorise:"]

options = morss.Options(csv=True) # arguments

generator  = pipeline("text-classification", model="wesleyacheng/news-topic-classification-with-bert")


#print(generator("Summarise and Categorise:"))


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

            LLMprompt += title+" "+content
            Outputs.append(LLMprompt)

            print(LLMprompt)

            print(generator(LLMprompt ))
            print("###########")



