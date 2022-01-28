import json 

# Tạo biến chung cho đường dẫn, bỏ đi CoffeeShop
thu_muc_san_pham = 'du_lieu/san_pham/'  # đường dẫn chung cho nhiều file sp khác nhau
tap_tin_nguoi_dung = 'du_lieu/Nguoi_dung/Nguoi_dung.json' 


# Tạo hàm xử lý file json
def doc_file_json(duong_dan):
	f = open(duong_dan, encoding='utf-8')
	du_lieu = json.load(f)
	f.close()
	return du_lieu

def ghi_file_json(duong_dan, noi_dung):
	f = open(duong_dan, 'w', encoding='utf-8')
	json.dump(noi_dung, f, ensure_ascii=False, indent=4)
	f.close()
	return True