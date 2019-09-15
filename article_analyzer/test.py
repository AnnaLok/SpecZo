import json

from goose3 import Goose
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
# beta stuff for topic identifier
from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums as enums_topic
from google.cloud.language_v1beta2 import types as types_topic

urls=[
'https://www.npr.org/2019/09/14/760837355/houthi-drone-strikes-disrupt-almost-half-of-saudi-oil-exports',
    'https://www.washingtonpost.com/politics/more-united-vsa-house-divided-gop-goes-all-in-on-trump-while-democrats-clash-over-ideology-and-tactics/2019/09/14/264ab7de-d704-11e9-ab26-e6dbebac45d3_story.html',
    'https://www.theatlantic.com/entertainment/archive/2019/09/charli-xcx-charli-album-review-playful-not-visionary/598018/',
    'https://www.vox.com/2019/9/14/20865775/hamza-bin-laden-osama-son-killed-counterterrorism-operation-white-house-confirms',
    'https://www.nytimes.com/2019/09/14/world/middleeast/saudi-arabia-refineries-drone-attack.html?action=click&module=Top%20Stories&pgtype=Homepage',
    'https://www.nbcnews.com/news/us-news/couples-virginia-will-no-longer-have-disclose-race-obtain-marriage-n1054531',
    'https://ca.reuters.com/article/topNews/idCAKBN1VZ0LQ-OCATP',
    'https://www.apnews.com/b84ad10648e6418d8b95c3fe6657035c',
    'https://www-m.cnn.com/2019/09/14/politics/andrew-yang-shane-gillis-racist-comments/index.html?r=https%3A%2F%2Fwww.google.com%2F',
    'https://www.usatoday.com/story/news/nation/2019/09/11/church-held-homeless-people-hostage-forced-them-beg-feds-say/2285143001/',
    'https://www.wsj.com/articles/house-committee-requests-tech-executives-emails-in-antitrust-probe-11568377800?mod=hp_lead_pos3',
    'https://www.thefiscaltimes.com/2019/09/13/Trump-Touts-Inspirational-Middle-Class-Tax-Cut',
    'https://www.foxnews.com/politics/pompeo-condemns-iran-saudi-oil',
    'https://dailycaller.com/2019/09/14/eric-holder-says-borders-mean-something/',
    'https://www.redstate.com/bonchie/2019/09/14/obama-bro-ben-rhodes-bursts-like-kool-aid-man-shill-iran-deadly-attacks/',
    'https://www.theblaze.com/news/top-dem-senator-warns-betos-gun-confiscation-threat-will-backfire-badly-on-democrats',
    'https://www.breitbart.com/politics/2019/09/14/bernie-sanders-we-are-going-to-impose-a-moratorium-on-deportations/',
    'https://www.infowars.com/heres-the-former-nbc-exec-whos-pushing-trump-on-using-google-to-determine-who-owns-a-gun/',
    'https://www.theguardian.com/politics/2019/sep/15/david-cameron-slammed-for-horrendous-mistake-brexit-referendum',
    'https://slate.com/news-and-politics/2019/09/joshua-geltzer-election-peaceful-transition-of-power-donald-trump.html',
    'https://www.huffpost.com/entry/nyt-reporters-uncover-new-sexual-misconduct-claim-kavanaugh_n_5d7d7ccde4b077dcbd5f6e7c',
    'https://occupydemocrats.com/2019/09/14/ten-month-investigation-uncovers-credible-new-sexual-misconduct-allegation-against-justice-kavanaugh/',
    'http://addictinginfo.com/2019/05/19/trump-unleashes-an-unhinged-rant-after-republican-lawmaker-calls-for-his-impeachment/'
]

def get_json(json_file):
    with open(json_file) as file:
        return json.loads(file.read())

def filter_articles(urls: list) -> list:
    ## return list of dicts with the info
    article_data = []
    with Goose() as g:
        for link in urls:
            article = g.extract(url=link)
            try:
                if article.opengraph['type'] == 'article':
                    ## opengraph gets author, source, title, topic (article:section), description and others, but some articles don't have everything
                    article_extraction = article.opengraph
                    article_extraction['cleaned_text'] = article.cleaned_text
                    article_data.append(article_extraction)
                    if 'site_name' in article.opengraph:
                        print(article.opengraph['site_name'])
            except:
                print(article.opengraph['url'])
    return article_data

def create_score(article):
    filename = 'news_sources.json'
    news_sources_scores = get_json((filename))

    ## multiply by -1 to work with the scale created
    sentiment_total = article['sentiment']['sentiment_score'] * article['sentiment']['sentiment_magnitude'] * -1

    site_score = news_sources_scores[article['site_name']]

    return site_score + sentiment_total


def main():
    filename = 'news_sources.json'
    news_sources_scores = get_json((filename))

    # articles = filter_articles(urls=urls)


if __name__ == "__main__":
    main()

