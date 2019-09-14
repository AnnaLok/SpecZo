from goose3 import Goose
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# beta stuff for topic identifier
from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums as enums_topic
from google.cloud.language_v1beta2 import types as types_topic

## url from server which gets from chrome extension

# urls = ['https://www.cbc.ca/news/politics/cabinet-confidence-trudeau-scheer-1.5283175',"https://www.bbc.com/news/science-environment-49567197", 'https://www.economist.com/leaders/2019/09/12/how-the-world-will-change-as-computers-spread-into-everyday-objects']
# urls = ['https://www.foxnews.com/politics/pension-funds-in-iran-on-brink-of-collapse-amid-us-maximum-pressure-campaign']
urls=['https://www.reddit.com/']
article_data = []
need_npl_topic = []

with Goose() as g:
    for link in urls:
        article = g.extract(url=link)
        ## opengraph gets author, source, title, topic (article:section), description and others, but some articles don't have everything
        article_extraction = article.opengraph
        article_extraction['cleaned_text'] = article.cleaned_text
        article_data.append(article_extraction)

        # Instantiates a client
        client = language.LanguageServiceClient()

        # The text to analyze
        text = (u'{}').format(article.cleaned_text)
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        print(article_extraction["title"])
        print(article.opengraph['type'])
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

        ## TOPIC IDENTIFIER
        if 'article:section' not in article.opengraph:
            language_client = language_v1beta2.LanguageServiceClient()
            document = types_topic.Document(
                content=f"{article_extraction['cleaned_text']}",
                type=enums_topic.Document.Type.PLAIN_TEXT
            )
            result = language_client.classify_text(document)
            for category in result.categories:
                print('category name: ', category.name)
                print('category confidence: ', category.confidence)
                ## maybe take category with most confidence and the first of the slashed list
        else:
            print(article.opengraph['article:section'])
                
        print( )