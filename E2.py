import serial
from time import sleep
import time
def recv(serial):
	while True:
		data = serial.read_all()
		if data == '':
			continue
		else:
			break
		sleep(0.02)
	return data

if __name__ == '__main__':
	COM=input("请输入要连接的串口:")
	BAUD=input("请输入波特率:")
	serial = serial.Serial(COM,BAUD, timeout=0.5)  #/dev/ttyUSB0
	if serial.isOpen() :
		print("open success")
	else :
		print("open failed")
	while True:
		str1 = input("请输入要发送到串口的话：")
		a=str1+"\n"
		nowtime='<'+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'>'
		serial.write((nowtime+'Send From'+' '+COM+':').encode("gbk"))
		serial.write((a).encode("gbk"))
		sleep(0.1)

		data =recv(serial)
		if data != b'' :
			print(nowtime+"receive : "+data.decode("gbk"))
