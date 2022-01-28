from flask import Flask

app = Flask(__name__)
app.secret_key = 'QLCoffeeShop'		# app.secret_key lưu thông tin đăng nhập trong cookies ngay tại browser 
									
import CoffeeShop.app_trang_chu
import CoffeeShop.app_Admin


# secret_key nên được đặt phức tạp và mã hoá để tránh attackers. 
# session chỉ hoạt động khi có secret key

''' 
Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering. 
It's very important that an attacker doesn't know the value of this secret key. 
Your application is using a weak/known secret key and Acunetix managed to guess this key.'''