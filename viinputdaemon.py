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
def F1(inProgram):
	print termcolour.PINK + 'F1 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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
		device.emit_click(uinput.KEY_D)
		device.emit_click(uinput.KEY_ENTER)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Home'

def F2(inProgram):
	print termcolour.PINK + 'F2 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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
		device.emit_click(uinput.KEY_L)
		device.emit_click(uinput.KEY_A)
		device.emit_click(uinput.KEY_Y)
		device.emit_click(uinput.KEY_SPACE)
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'play '

def F3(inProgram):
	print termcolour.PINK + 'F3 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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
	if inProgram == 'zsh':
		device.emit_combo([
			uinput.KEY_LEFTCTRL,
			uinput.KEY_C,
			])
		print termcolour.GREEN + 'Command:' + termcolour.WHITE, 'Cancel'

def F4(inProgram):
	print termcolour.PINK + 'F4 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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

def F5(inProgram):
	print termcolour.PINK + 'F5 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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

def F6(inProgram):
	print termcolour.PINK + 'F6 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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

def F7(inProgram):
	print termcolour.PINK + 'F7 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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

def F8(inProgram):
	print termcolour.PINK + 'F8 Pressed' + termcolour.WHITE
	print termcolour.GREEN + 'Program:' + termcolour.WHITE, inProgram
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

# Python-uinput is a quality Interface
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
    ])

# Open serial decice
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 1)
print termcolour.GREEN + 'Serial device opened:' + termcolour.WHITE, ser.name

# Mad Hacks go here

# Polling for input
while 1:
	sbuf = ser.read()
	print 'Buffer Queue =', ser.inWaiting()
	print 'Read =', sbuf
	
	if sbuf == '\x81': #129
		F1(program)
	if sbuf == '\x82': #130
		F2(program)
	if sbuf == '\x83': #131
		F3(program)
	if sbuf == '\x84': #132
		F4(program)
	if sbuf == '\x85': #133
		F5(program)
	if sbuf == '\x86': #134
		F6(program)
	if sbuf == '\x87': #135
		F7(program)
	if sbuf == '\x88': #136
		F8(program)

