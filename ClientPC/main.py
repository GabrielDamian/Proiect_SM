import bluetooth

MAX_NUMBER_OF_LINES = 3


def append_line(line, file):
    lines = open(file, 'r').readlines()
    if len(lines) >= MAX_NUMBER_OF_LINES:
        del lines[0]
    lines.append(line)
    open(file, 'w').writelines(lines)


sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

bt_addr = '98:D3:31:F9:E5:70'
port = 0x1001

print("Trying to connect to {} on PSM 0x{}...".format(bt_addr, port))

sock.connect((bt_addr, port))

while True:
    try:
        message = (sock.recv(1024) + sock.recv(1024)).decode()
        print("Data received:", message)
        temp, hum = message.split(' ', 1)
        append_line(temp+'\n', 'temp.txt')
        append_line(hum+'\n', 'hum.txt')
    except:
        break

sock.close()
