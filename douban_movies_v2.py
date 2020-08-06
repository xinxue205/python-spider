# -*- coding: utf-8 -*-
import requests
from html.parser import HTMLParser


class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'a' :
            print(_attr(attrs, 'onclick'))
            # movie = {}
            # movie['title'] = _attr.text
            # self.movies.append(movie)
            # print('%(title)s' % movie)
            # self.in_movies = True

        # if tag == 'img' and self.in_movies:
        #     self.in_movies = False
        #     movie = self.movies[len(self.movies) - 1]
        #     movie['cover-url'] = _attr(attrs, 'src')
        #     _download_poster_cover(movie)


def _download_poster_cover(movie):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'}
    url = movie['cover-url']
    print('downloading post cover from %s' % url)
    s = requests.get(url, headers=headers)
    fname = url.split('/')[-1]
    with open(fname, 'wb') as f:
        f.write(s.content)
    movie['cover-file'] = fname


def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
               }
    s = str(requests.get(url, headers=headers).content)
    print(s)
    parser = MovieParser()
    parser.feed(s)
    print(parser.movies)
    return parser.movies


if __name__ == '__main__':
    url = 'https://movie.douban.com/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': ')))
