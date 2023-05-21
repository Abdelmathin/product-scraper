#encoding: UTF-8

from Scraper import Scraper

if (__name__ == '__main__'):
	for product in ['shoes', 'bags', 'acc']:
		link = 'http://' + product + '.ygshoes188.com/'
		s = Scraper(product, link)
		s.run()
