#encoding: UTF-8
#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 08:09:40 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/21 08:09:59 by ahabachi         ###   ########.fr        #
#                                                                              #
#  **************************************************************************  #
#                                                                              #
#   █████████            ██████████         ██████████         ██████████      #
#   ██     ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██         ██      ██      #
#          ██                    ██                 ██                 ██      #
#          ██            ██████████         ██████████                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#          ██                    ██                 ██                 ██      #
#       ████████         ██████████         ██████████                 ██      #
#                                                                              #
#  **************************************************************************  #

from Scraper import Scraper

if (__name__ == '__main__'):
	for product in ['shoes', 'bags', 'acc']:
		link = 'http://' + product + '.ygshoes188.com/'
		s = Scraper(product, link)
		s.run()