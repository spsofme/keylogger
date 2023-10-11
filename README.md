# Keylogger
- Sızma testleri için kullanılabilecek keylogger programı.
- Diğer keylogger ların aksine bu program depolanan veriyi e-posta yoluyla değil, dinlenilen bir porta gönderir.

## Kurulum
- kurulumu yapacağınız dizine gidin (```cd <yol>```)
- ```git clone https://github.com/spsofme/keylogger``` komutu ile projeyi indirin
- ```pip install -r requirements.txt``` komutu ile gerekli kütüphaneleri kurun

## Kullanım
1. KeyLogger sınıfı içerisinde host, port ve sendTime değişkenlerinin değerini kendinize göre değiştirin.
	- host : sizin ip adresiniz
	- port : dinlediğiniz port numarası (varsayılan: 4444)
	- sendTime : bilgilerin kaç saniyede bir gönderileceği (varsayılan: 30)
2. Her hangi bir bilgisayardan bir portu dinlemeye başlayın. (örn: ```nc -nvlp 4444```)
3. programı çalıştırın.
