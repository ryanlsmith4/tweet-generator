import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '22f23f9b9db66079bf4180f15d91b60b'


def get_article(article_url):
    # set request params for API request
    params = { 'token': DIFFBOT_DEV_TOKEN,
               'url': article_url,
               'discussion': 'false' }

    res = requests.get(DIFFBOT_API_URL, params) # hit the Diffbot API
    res_obj = res.json()['objects'][0]          # parse the response object

    return res_obj['text']                      # pull out the text

if __name__ == '__main__':
    import sys
    urls_file = open('/Users/ryansmith/Documents/dev/cs/tweet-generator/pages.txt')
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        url = line.strip() # remove leading/trailing whitespace
        article = get_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
