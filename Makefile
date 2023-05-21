#  **************************************************************************  #
#                                                                              #
#                                                          :::      ::::::::   #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ahabachi <ahabachi@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/05/21 09:10:31 by ahabachi          #+#    #+#              #
#    Updated: 2023/05/21 09:12:58 by ahabachi         ###   ########.fr        #
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

all:
	curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
	python get-pip.py && rm -rf get-pip.py
	python -m pip install --upgrade pip
	python -m pip install requests
	clear
	python main.py

fclean:
	rm -rf assets

push:
	@git add .
	@git commit -m "committed on '`date`' by '`whoami`', hostname = '`hostname`'"
	@git push