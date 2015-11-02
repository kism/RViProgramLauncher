# VI Program Launcher Serial Documentation

## Connecting

The serial connection will need to be 115200 baud, No Parity, 8 Data Bits, 1 Stop Bit, No Flow control. On the device running the daemon /dev/ttyUSB0 will be used.

## Braille Characters

These characters are literal translations of Braille cells to the 6 least significant bits of a byte.

Start at 00000000, End at 00111111

### Braille Modifier Characters

| Key / Mod   | Hex  | Binary   | Decimal |
|-------------|------|----------|---------|
| Capital Mod | 0x01 | 00000001 | 1       |
| Number Mod  | 0x0F | 00001111 | 15      |


### Regular Braille Characters

| Key / Mod   | Hex  | Binary   | Decimal |
|-------------|------|----------|---------|
| A/1         | 0x20 | 00100000 | 32      |
| B/2         | 0x30 | 00110000 | 48      |
| C/3         | 0x24 | 00100100 | 36      |
| D/4         | 0x26 | 00100110 | 38      |
| E/5         | 0x22 | 00100010 | 34      |
| F/6         | 0x34 | 00110100 | 52      |
| G/7         | 0x36 | 00110110 | 54      |
| H/8         | 0x32 | 00110010 | 50      |
| I/9         | 0x14 | 00010100 | 20      |
| J/0         | 0x16 | 00010110 | 22      |
| K           | 0x28 | 00101000 | 40      |
| L           | 0x38 | 00111000 | 56      |
| M           | 0x2C | 00101100 | 44      |
| N           | 0x2E | 00101110 | 46      |
| O           | 0x2A | 00101010 | 42      |
| P           | 0x3C | 00111100 | 60      |
| Q           | 0x3E | 00111110 | 62      |
| R           | 0x3A | 00111010 | 58      |
| S           | 0x1C | 00011100 | 28      |
| T           | 0x1E | 00011110 | 30      |
| U           | 0x29 | 00101001 | 41      |
| V           | 0x39 | 00111001 | 57      |
| W           | 0x17 | 00010111 | 23      |
| X           | 0x2D | 00101101 | 45      |
| Y           | 0x2F | 00101111 | 47      |
| Z           | 0x2B | 00101011 | 43      |
| , (comma)   | 0x10 | 00010000 | 16      |
| . (period)  | 0x13 | 00010011 | 19      |
| / (slash)   | 0x0C | 00001100 | 12      |
|   (space)   | 0x60 | 01100000 | 96      |

## Other Keys

### IBM Compatable PC Keys

Start at 01000000, End at 01111111

| Key       | Hex  | Binary   | Decimal |
|-----------|------|----------|---------|
| Esc       | 0x40 | 01000000 | 64      |
| Up        | 0x41 | 01000001 | 65      |
| Left      | 0x42 | 01000010 | 66      |
| Right     | 0x43 | 01000011 | 67      |
| Down      | 0x44 | 01000100 | 68      |
| Enter     | 0x45 | 01000101 | 69      |
| Backspace | 0x46 | 01000110 | 70      |
| Page Up   | 0x47 | 01000111 | 71      |
| Page Down | 0x47 | 01001000 | 72      |


### Macro Keys

| Key         | Hex  | Binary   | Decimal |
|-------------|------|----------|---------|
| F1          | 0x81 | 10000001 | 129     |
| F2          | 0x82 | 10010010 | 130     |
| F3          | 0x83 | 10000011 | 131     |
| F4          | 0x84 | 10000100 | 132     |
| F5          | 0x85 | 10000101 | 133     |
| F6          | 0x86 | 10000110 | 134     |
| F7          | 0x87 | 10000111 | 135     |
| F8          | 0x88 | 10001000 | 136     |