from flask import request, render_template, Markup
import json 
from CoffeeShop import app 

# Tạo biến chung cho đường dẫn
thu_muc_san_pham = 'CoffeeShop/du_lieu/san_pham/'  # đường dẫn chung cho nhiều file sp khác nhau

# Tạo hàm xử lý file json

def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='UTF-8')
	du_lieu = json.load(f)
	f.close()
	return du_lieu

def ghi_file_json(duong_dan, noi_dung):
	f = open(duong_dan, 'w', encoding='UTF-8')
	json.dump(noi_dung, f, ensure_ascii=False, indent=4)
	f.close()
	return True 
