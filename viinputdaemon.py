# Input Daemon for the Visually Impared
# For use with a device that outputs serial

import uinput 	#interface between python and the uinput kernel module
import time 	#for time.sleep()
import serial 	#the keyboard this program interfaces with uses serial
import os
import sys

# Easier debugging :^)
class termcolour:
    PINK = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[0m'

# Figure out what to do on the keypresses
def sendLetter(letter): 
	global caps
	global numb
	print termcolour.GREEN + 'Sent ASCII Char:' + termcolour.WHITE
	if numb == True:
		if letter == 'KEY_A':
			device.emit_click(uinput.KEY_1)
		if letter == 'KEY_B':
			device.emit_click(uinput.KEY_2)		
		if letter == 'KEY_C':
			device.emit_click(uinput.KEY_3)	
		if letter == 'KEY_D':
			device.emit_click(uinput.KEY_4)
		if letter == 'KEY_E':
			device.emit_click(uinput.KEY_5)
		if letter == 'KEY_F':
			device.emit_click(uinput.KEY_6)
		if letter == 'KEY_G':
			device.emit_click(uinput.KEY_7)
		if letter == 'KEY_H':
			device.emit_click(uinput.KEY_8)
		if letter == 'KEY_I':
			device.emit_click(uinput.KEY_9)
		if letter == 'KEY_J':
			device.emit_click(uinput.KEY_0)
	else:
		if caps == 0:
			device.emit_click(getattr(uinput,letter))
		if caps == 1:
			caps = 0
			device.emit_combo([
				uinput.KEY_LEFTSHIFT,
				getattr(uinput,letter),
				])
		if caps == 2:
				device.emit_combo([
				uinput.KEY_LEFTSHIFT,
				getattr(uinput,letter),
				])

def f1(inProgram):
	print termcolour.PINK + 'F1 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Open Help
		device.emit_click(uinput.KEY_1)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F1'
	if inProgram == 'nano':  # Open Help
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_G,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Help'
	if inProgram == 'newsbeuter':
		device.emit_combo([
			uinput.KEY_LEFTSHIFT,
			uinput.KEY_SLASH,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Help'
	if inProgram == 'alpine':
		device.emit_combo([
			uinput.KEY_LEFTSHIFT,
			uinput.KEY_SLASH,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Help'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_F9)
		time.sleep(0.1)
		device.emit_click(uinput.KEY_H)
		time.sleep(0.1)
		device.emit_click(uinput.KEY_M)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Help'
	if inProgram == 'zsh':
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_C,
			])
		device.emit_click(uinput.KEY_C)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_D)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Home'

def f2(inProgram):
	print termcolour.PINK + 'F2 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_2)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F2'
	if inProgram == 'nano':  # Open File
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_R,
			])
		time.sleep(0.1)
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_T,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Open File'
	if inProgram == 'newsbeuter':
		device.emit_click(uinput.KEY_ENTER)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Open'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_I)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Index'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_G)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Go To'
	if inProgram == 'zsh':
		device.emit_click(uinput.KEY_P)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_L)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_A)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_Y)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_SPACE)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'play '

def f3(inProgram):
	print termcolour.PINK + 'F3 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_3)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F3'	
	if inProgram == 'nano': # Save file
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_O,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Save File'
	if inProgram == 'newsbeuter':
		device.emit_click(uinput.KEY_S)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Save Story'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_C)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Compose'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_F9)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Menu'

def f4(inProgram):
	print termcolour.PINK + 'F4 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_4)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F4'	
	if inProgram == 'nano': # Cancel
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_C,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Cancel'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_M)
		time.sleep(0.1)
		device.emit_click(uinput.KEY_COMMA)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Back'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_ESC)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Cancel'
	if inProgram == 'zsh':
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_C,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Cancel'

def f5(inProgram):
	print termcolour.PINK + 'F5 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_5)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F5'	
	if inProgram == 'nano': # Cut
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_K,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Cut'
	if inProgram == 'newsbeuter':
		device.emit_click(uinput.KEY_R)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Reload'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_J)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Journal'

def f6(inProgram):
	print termcolour.PINK + 'F6 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_6)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F6'
	if inProgram == 'nano': # Uncut
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_U,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Uncut'
	if inProgram == 'newsbeuter':
		uinput.KEY_N,
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Next Unread'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_A)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Address'

def f7(inProgram):
	print termcolour.PINK + 'F7 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_7)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F7'	
	if inProgram == 'nano': # Find
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_W,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Find'
	if inProgram == 'newsbeuter':
		device.emit_click(uinput.KEY_O)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Open in Browser'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_S)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Setup'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_SLASH)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Find'

def f8(inProgram):
	print termcolour.PINK + 'F8 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
	if inProgram == 'viui':  # Menu Select
		device.emit_click(uinput.KEY_8)
		time.sleep(0.01)
		device.emit_click(uinput.KEY_ENTER)
		time.sleep(0.01)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'F8'	
	if inProgram == 'nano': # Exit menu or program
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_X,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Quit'
	if inProgram == 'newsbeuter':
		device.emit_click(uinput.KEY_Q)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Quit'
	if inProgram == 'alpine':
		device.emit_click(uinput.KEY_Q)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Quit'
	if inProgram == 'links':
		device.emit_click(uinput.KEY_Q)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Quit'
	if inProgram == 'zsh':
		device.emit_combo([
				uinput.KEY_LEFTCTRL,
				uinput.KEY_D,
				])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Quit'

# Main Program
print termcolour.PINK + '~ Daemon initialising ~' + termcolour.WHITE

# Check if program was run with an arguement
if len(sys.argv) > 1:
	print termcolour.GREEN + 'Argument:' + termcolour.WHITE, str(sys.argv[1])
	program = str(sys.argv[1])
else:
	print termcolour.YELLOW + 'No args, what are you even doing?' + termcolour.WHITE
	program = ''

# Python-uinput is a quality Interface, To find key codes check /usr/include/linux/input.h
device = uinput.Device([
	uinput.KEY_A,
	uinput.KEY_B,
	uinput.KEY_C,
	uinput.KEY_D,
	uinput.KEY_E,
	uinput.KEY_F,
	uinput.KEY_G,
	uinput.KEY_H,
	uinput.KEY_I,
	uinput.KEY_J,
	uinput.KEY_K,
	uinput.KEY_L,
	uinput.KEY_M,
	uinput.KEY_N,
	uinput.KEY_O,
	uinput.KEY_P,
	uinput.KEY_Q,
	uinput.KEY_R,
	uinput.KEY_S,
	uinput.KEY_T,
	uinput.KEY_U,
	uinput.KEY_V,
	uinput.KEY_W,
	uinput.KEY_X,
	uinput.KEY_Y,
	uinput.KEY_Z,
	uinput.KEY_1,
	uinput.KEY_2,
	uinput.KEY_3,
	uinput.KEY_4,
	uinput.KEY_5,
	uinput.KEY_6,
	uinput.KEY_7,
	uinput.KEY_8,
	uinput.KEY_9,
	uinput.KEY_0,
	uinput.KEY_TAB,
	uinput.KEY_ENTER,
	uinput.KEY_SPACE,
	uinput.KEY_DOT,
	uinput.KEY_COMMA,
	uinput.KEY_SLASH,
	uinput.KEY_BACKSLASH,
	uinput.KEY_LEFTCTRL,
	uinput.KEY_LEFTALT,
	uinput.KEY_LEFTSHIFT,
	uinput.KEY_BACKSPACE,
	uinput.KEY_UP,
	uinput.KEY_LEFT,
	uinput.KEY_RIGHT,
	uinput.KEY_DOWN,
	uinput.KEY_ESC,
	uinput.KEY_F1,
	uinput.KEY_F2,
	uinput.KEY_F3,
	uinput.KEY_F4,
	uinput.KEY_F5,
	uinput.KEY_F6,
	uinput.KEY_F7,
	uinput.KEY_F8,
	uinput.KEY_F9,
	uinput.KEY_F10,
	uinput.KEY_F11,
	uinput.KEY_F12,
	uinput.KEY_1,
	uinput.KEY_2,
	uinput.KEY_3,
	uinput.KEY_4,
	uinput.KEY_5,
	uinput.KEY_6,
	uinput.KEY_7,
	uinput.KEY_8,
	uinput.KEY_9,
	uinput.KEY_0,	
    ])

# Open serial decice
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
print termcolour.GREEN + 'Serial device opened:' + termcolour.WHITE, ser.name

# Mad Hacks go here
caps = 0
numb = False
if program == 'newsbeuter':
	time.sleep(2.0)
	device.emit_click(uinput.KEY_R)
	time.sleep(3.0)
	device.emit_click(uinput.KEY_ENTER)

# Polling for input
while 1:
	sbuf = ser.read()
	print 'Buffer Queue =', ser.inWaiting()
	print 'Read =', sbuf
	
	# Function Keys, All values are in hex
	if sbuf == '\x81': #129
		f1(program)
	if sbuf == '\x82': #130
		f2(program)
	if sbuf == '\x83': #131
		f3(program)
	if sbuf == '\x84': #132
		f4(program)
	if sbuf == '\x85': #133
		f5(program)
	if sbuf == '\x86': #134
		f6(program)
	if sbuf == '\x87': #135
		f7(program)
	if sbuf == '\x88': #136
		f8(program)
	
	# Regular Keys, All values are in hex
	if sbuf == '\x20':
		sendLetter('KEY_A')
	if sbuf == '\x30':
		sendLetter('KEY_B')
	if sbuf == '\x24':
		sendLetter('KEY_C')
	if sbuf == '\x26':
		sendLetter('KEY_D')
	if sbuf == '\x22':
		sendLetter('KEY_E')
	if sbuf == '\x34':
		sendLetter('KEY_F')
	if sbuf == '\x36':
		sendLetter('KEY_G')
	if sbuf == '\x32':
		sendLetter('KEY_H')
	if sbuf == '\x14':
		sendLetter('KEY_I')
	if sbuf == '\x16':
		sendLetter('KEY_J')
	if sbuf == '\x28':
		sendLetter('KEY_K')
	if sbuf == '\x38':
		sendLetter('KEY_L')
	if sbuf == '\x2C':
		sendLetter('KEY_M')
	if sbuf == '\x2E':
		sendLetter('KEY_N')
	if sbuf == '\x2A':
		sendLetter('KEY_O')
	if sbuf == '\x3C':
		sendLetter('KEY_P')
	if sbuf == '\x3E':
		sendLetter('KEY_Q')
	if sbuf == '\x3A':
		sendLetter('KEY_R')
	if sbuf == '\x1C':
		sendLetter('KEY_S')
	if sbuf == '\x1E':
		sendLetter('KEY_T')
	if sbuf == '\x29':
		sendLetter('KEY_U')
	if sbuf == '\x39':
		sendLetter('KEY_V')
	if sbuf == '\x17':
		sendLetter('KEY_W')
	if sbuf == '\x2D':
		sendLetter('KEY_X')
	if sbuf == '\x2F':
		sendLetter('KEY_Y')
	if sbuf == '\x2B':
		sendLetter('KEY_Z')
	if sbuf == '\x10':
		device.emit_click(uinput.KEY_COMMA)
	if sbuf == '\x13':
		device.emit_click(uinput.KEY_DOT)
	if sbuf == '\x0C':
		device.emit_click(uinput.KEY_SLASH)
	if sbuf == '\x60':
		device.emit_click(uinput.KEY_SPACE)
		caps = 0
		numb = 0

	# Special Keys, All values are in hex
	if sbuf == '\x40':
		device.emit_click(uinput.KEY_ESC)
	if sbuf == '\x41':
		device.emit_click(uinput.KEY_UP)
	if sbuf == '\x42':
		device.emit_click(uinput.KEY_LEFT)
	if sbuf == '\x43':
		device.emit_click(uinput.KEY_RIGHT)
	if sbuf == '\x44':
		device.emit_click(uinput.KEY_DOWN)
	if sbuf == '\x45':
		device.emit_click(uinput.KEY_ENTER)
	if sbuf == '\x46':
		device.emit_click(uinput.KEY_BACKSPACE)
	if sbuf == '\x01':
		if caps > 1:
			caps = 2
		else:
			caps = caps + 1
		print termcolour.GREEN + 'Caps:' + termcolour.WHITE, caps
	if sbuf == '\x0F':
		if numb == True:
			numb = False
		else:
			numb = True
		print termcolour.GREEN + 'Numb:' + termcolour.WHITE, numb