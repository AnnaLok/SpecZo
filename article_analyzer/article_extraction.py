from goose3 import Goose
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# beta stuff for topic identifier
from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums as enums_topic
from google.cloud.language_v1beta2 import types as types_topic

import config

urls = [
    'https://www.cbc.ca/news/politics/cabinet-confidence-trudeau-scheer-1.5283175',
    "https://www.bbc.com/news/science-environment-49567197", 
    'https://www.economist.com/leaders/2019/09/12/how-the-world-will-change-as-computers-spread-into-everyday-objects'
]
# urls = ['https://www.foxnews.com/politics/pension-funds-in-iran-on-brink-of-collapse-amid-us-maximum-pressure-campaign']
# urls=['https://www.reddit.com/']


def filter_articles(urls: list) -> list:
    ## return list of dicts with the info
    article_data = []
    with Goose() as g:
        for link in urls:
            article = g.extract(url=link)
            if article.opengraph['type'] == 'article':
                ## opengraph gets author, source, title, topic (article:section), description and others, but some articles don't have everything
                article_extraction = article.opengraph
                article_extraction['cleaned_text'] = article.cleaned_text
                article_data.append(article_extraction)
    return article_data

def filter_topic(topic_list: str) -> str:
    topic = topic_list
    ## this gets rid of first slash
    topic = topic[1:]
    ## this gets rid of stuff after the second slash
    news_index = topic.find('News')
    if news_index == 0:
        topic = topic[5:]

    slash_index = topic.find('/')
    if slash_index != -1:
        topic = topic[:slash_index]

    return topic

def get_topic(article):
    language_client = language_v1beta2.LanguageServiceClient()
    document = types_topic.Document(
        content=f"{article['cleaned_text']}",
        type=enums_topic.Document.Type.PLAIN_TEXT
    )
    result = language_client.classify_text(document)
    highest_confidence = []
    for category in result.categories:
        highest_confidence.append({'category': category.name, 'confidence': category.confidence})

    highest = max(highest_confidence, key=lambda x: x['confidence'])
    return filter_topic(highest['category'])

def get_sentiment(article):
    client = language.LanguageServiceClient()
    text = (u'{}').format(article['cleaned_text'])
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(document).document_sentiment
    return sentiment

def main():
    articles = filter_articles(urls=urls)
    for article in articles:
        print(get_topic(article))
        print(get_sentiment(article))


if __name__ == "__main__":
    main()

