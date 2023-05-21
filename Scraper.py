#encoding: UTF-8

import os
import requests

class Scraper:
	def __init__(self, product, url):
		while (url.endswith('/')):
			url = url[:-1]
		self.url = url
		self.product = product

	def fix_url(self, url):
		if (url.startswith("http:") or url.startswith("https:")):
			return (url)
		while (url.startswith('/')):
			url = url[1:]
		return (self.url + '/' + url)

	def unpack(self, url, olddata = {}, entry = 0):
		req = requests.get(url)
		text = req.text

		text = text[text.index('<div class="home_ul_img">'):]

		produects = text.split('\n                                        <')
		produects = produects[1:]
		for i in range(len(produects)):
			produect = produects[i]
			if (entry == 0):
				olddata = {}
			data = {}
			if ('<div class="' in produect) and ('<a title="' in produect):
				key = '<a title="'
				produect = produect[produect.index(key) + len(key):]
				key = '" href="'

				keyname = 'title-' + str(entry)
				if (keyname == 'title-0'):
					keyname = 'category'
				data[keyname] = produect.split(key)[0]

				produect = produect[produect.index(key) + len(key):]
				data['href-' + str(entry)] = self.fix_url(produect.split('">')[0])
				key = '" data-original="'
				produect = produect[produect.index(key) + len(key):]
				key = '" class="'
				
				keyname = 'image-' + str(entry)
				if (keyname == 'image-0'):
					keyname = 'category-image'
				data[keyname] = self.fix_url(produect.split(key)[0])
				
				produect = produect[produect.index(key) + len(key):]
				for k, v in data.items():
					olddata[k] = v
				data = olddata
				if (entry < 2):
					self.unpack(data['href-' + str(entry)], olddata, entry + 1)
				else:
					req2 = requests.get(data['href-' + str(entry)])
					text2 = req2.text
					self.extract(text2, data)
		return data

	def extract(self, text, data = {}):

		comment = text.split('<!--  <ul>')[1].split('</ul>')[0].strip()
		for line in comment.split('</li>'):
			line = line.strip()
			if ('<a href="' in line):
				line = line[line.index('<a href="') + 9:].split('" target="_blank">')[0]
				data['image'] = self.fix_url(line)
				continue
			if (not line.startswith('<li>')):
				continue
			line = line[4:];
			key = line
			for k in [' ', ':', '：']:
				key = key.split(k)[0]
			value = line[len(key):]
			for k in [' ', ':', '：']:
				if (k in value):
					value = value[value.index(k) + len(k):]
			data[key] = value

		self.save(data)

	def dict2text(self, data):
		text = '{\n'
		inital_length = 15;
		for key, value in data.items():
			line = ('\t"' + key + '"')
			line +=  ((" " * (inital_length - len(key))) + ' : ')
			line += '"' + value + '",'
			text += (line + '\n')
		text += '}'
		return (text)

	def mkdir(self, dirname):
		path = ''
		for i in dirname.split('/'):
			path = path + i + '/'
			try:
				os.mkdir(path)
			except:
				pass
	def save(self, data):
		dirname = ('assets/' + self.product + '/' + data['category'] + '/' + data['ID'])
		self.mkdir(dirname)
		req = requests.get(data['image'])
		filename = (dirname + '/' + data['image'].split('/')[-1])
		with open(filename, 'wb') as fp:
			fp.write(req.content)
		with open(dirname + '/index.json', 'w') as fp:
			fp.write(self.dict2text(data))	

	def run(self):
		self.unpack(self.url)
