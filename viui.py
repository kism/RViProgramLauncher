#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Based on: http://blog.skeltonnetworks.com/2010/03/python-curses-custom-menu/ by Matthew Bennett with changes by Andrew Scheller
# A tonne of changes and optimisations for speakup done by Kieran Gee
# No idea what license, probably compatable with MIT ¯\_(ツ)_/¯

import time
import curses
import os
import psutil
import subprocess

# Curses init
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.start_color()
screen.keypad(1)
curses.curs_set(0) # try to fix issues with espeakup

# Highlighting
curses.init_pair(1,curses.COLOR_WHITE, curses.COLOR_BLACK) # fix issues with espeakup
h = curses.color_pair(1)
n = curses.A_NORMAL

MENU = "menu"
COMMAND = "command"
EXITMENU = "exitmenu"

menu_data = {
'title': "VIUI Launcher", 'type': MENU, 'subtitle': "Please select an option...",'options':[

	{ 'title': "Open Help", 'type': MENU, 'subtitle': "Select shutdown option",'options': [
		{'title': "viui Manual", 'type': COMMAND, 'command': 'man viui' },
		{'title': "nano Manual", 'type': COMMAND, 'command': 'man nano' },
		{'title': "alpine Manual", 'type': COMMAND, 'command': 'man alpine' },
		{'title': "newsbeuter Manual", 'type': COMMAND, 'command': 'man newsbeuter' },
		{'title': "links Manual", 'type': COMMAND, 'command': 'man links' },
		{'title': "irssi Manual", 'type': COMMAND, 'command': 'man irssi' },
		{'title': "piespeakup Manual", 'type': COMMAND, 'command': 'man piespeakup' },
	]},

	{ 'title': "nano", 'type': COMMAND, 'command': 'nano' },
	{ 'title': "alpine", 'type': COMMAND, 'command': 'alpine' },
	
	{ 'title': "newsbeuter", 'type': MENU, 'subtitle': "Select RSS feed to read",'options': [
		{ 'title': "ABC Perth", 'type': COMMAND, 'command': 'rm ~/rss.txt && echo "http://www.abc.net.au/local/rss/perth/all.xml" >> ~/rss.txt && newsbeuter -u ~/rss.txt' },
		{ 'title': "ABC Politics", 'type': COMMAND, 'command': 'rm ~/rss.txt && echo "http://www.abc.net.au/news/feed/1534/rss.xml" >> ~/rss.txt && newsbeuter -u ~/rss.txt' },
		{ 'title': "ABC Sport", 'type': COMMAND, 'command': 'rm ~/rss.txt && echo "http://abc.net.au/sport/syndicate/sport_all.xml" >> ~/rss.txt && newsbeuter -u ~/rss.txt' },
		{ 'title': "Huffington Post", 'type': COMMAND, 'command': 'rm ~/rss.txt && echo "http://www.huffingtonpost.com/feeds/news.xml" >> ~/rss.txt && newsbeuter -u ~/rss.txt' },
		{ 'title': "CNN", 'type': COMMAND, 'command': 'rm ~/rss.txt && echo "http://rss.cnn.com/rss/edition.rss" >> ~/rss.txt && newsbeuter -u ~/rss.txt' },
	]},
	
	{ 'title': "links", 'type': COMMAND, 'command': 'links' },
	{ 'title': "irssi", 'type': COMMAND, 'command': 'irssi' },
	{ 'title': "zsh", 'type': COMMAND, 'command': 'zsh' },
	
	{ 'title': "Options & Shutdown", 'type': MENU, 'subtitle': "Select shutdown option",'options': [
		{'title': "Update System Packages", 'type': COMMAND, 'command': 'sudo apt-get update && sudo apt-get upgrade' },
		{'title': "Shutdown", 'type': COMMAND, 'command': 'sudo shutdown -h now' },
		{'title': "Restart", 'type': COMMAND, 'command': 'sudo shutdown -r now' },
	]},
]}

# Menu loop
def runmenu(menu, parent):
	if parent is None:
		lastoption = "Exit"
	else:
		lastoption = "Return to %s menu" % parent['title']

	optioncount = len(menu['options']) # find number of items in menu
	pos=0
	oldpos=None
	x = None

	# While enter key is not pressed
	while x !=ord('\n'):
		if pos != oldpos:
			oldpos = pos
			screen.addstr(2,2, menu['title'], curses.A_STANDOUT) # Title for this menu
			screen.addstr(4,2, menu['subtitle'], curses.A_BOLD) # Subtitle for this menu

		# Display menu, pos is highlighted
		for index in range(optioncount):
			textstyle = n
			if pos==index:
				textstyle = h
			screen.addstr(5+index,4, "%d - %s" % (index+1, menu['options'][index]['title']), textstyle)
		
		# Add last option (exit)
		textstyle = n
		if pos==optioncount:
			textstyle = h
		screen.addstr(5+optioncount,4, "%d - %s" % (optioncount+1, lastoption), textstyle)
		screen.refresh()

		x = screen.getch() # Get user input

		# Check user input
		if x >= ord('1') and x <= ord(str(optioncount+1)):
			pos = x - ord('0') - 1 # If the user presses a number
	
	return pos # returnposition of curser

# This function calls showmenu and then acts on the selected item
def processmenu(menu, parent=None):
	optioncount = len(menu['options'])
	exitmenu = False
	while not exitmenu: #Loop until the user exits the menu
		getin = runmenu(menu, parent)
		if getin == optioncount:
			exitmenu = True
		elif menu['options'][getin]['type'] == COMMAND:
			# Prepare for command
			os.system("sudo pkill -f python\ viinputdaemon"); # Stop daemon
			curses.def_prog_mode() # Save menu status
			os.system('reset')
			screen.clear()
	
			# Run input daemon with new parameters
			if 'newsbeuter' in menu['options'][getin]['command']:
				subprocess.Popen(["nohup","sudo","python","viinputdaemon.py","newsbeuter","&"])
			elif 'man ' in menu['options'][getin]['command']:
				subprocess.Popen(["nohup","sudo","python","viinputdaemon.py","man","&"])
			else:
				subprocess.Popen(["nohup","sudo","python","viinputdaemon.py",menu['options'][getin]['command'],"&"])
	
			# Run Program
			os.system(menu['options'][getin]['command'])
			
			# Reset Daemon
			os.system("sudo pkill -f python\ viinputdaemon"); 
			subprocess.Popen(["nohup","sudo","python","viinputdaemon.py","viui","&"])
			os.system('clear')

			# Cleanup
			screen.clear()
			curses.reset_prog_mode()
			curses.curs_set(1)
			curses.curs_set(0)
		elif menu['options'][getin]['type'] == MENU:
			screen.clear()
			processmenu(menu['options'][getin], menu) # display the submenu
			screen.clear()
		elif menu['options'][getin]['type'] == EXITMENU:
			exitmenu = True

# Main program
# Setup
os.system('touch ~/rss.txt')
subprocess.Popen(["nohup","sudo","python","viinputdaemon.py","viui","&"])
os.system('clear')
# Run Menu
processmenu(menu_data)
# Cleanup
curses.endwin() # Exits the cursers menu
os.system("sudo pkill -f python\ viinputdaemon"); 
os.system('touch nohup.out && rm nohup.out') # Fix for sisuation where no program was run, remove the nohup output
os.system('clear')
