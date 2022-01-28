from flask import Flask, request, Markup, jsonify, render_template, abort
from thu_vien.xl_sp import *
from thu_vien.xl_Nguoi_dung import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = app.static_folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return 'Dịch vụ đang hoạt động...'

# upload file 
@app.route('/', methods=['POST'])
def upload_file():
	if request.method=='POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/san-pham/', secure_filename(f.filename)))
		return jsonify({"Response": 'Success'})
	

# --- Đọc danh sách sản phẩm --- 
@app.route('/danh-sach-san-pham', methods=['GET'])	# sử dụng methods theo phương thức REST: GET, POST, PUT, DELETE
def ds_san_pham():
	ds_san_pham = doc_danh_sach_san_pham()
	d = {"Danh_sach_San_pham": ds_san_pham}
	return jsonify(d)

''' 
jsonify là một hàm của flask, chuẩn hoá dữ liệu chuyển nó về list json và trả về trong response object (phản hồi yêu cầu)
d lúc này là dict nằm trong list
'''

# --- Đọc danh sách người dùng ---
@app.route('/danh-sach-nguoi-dung', methods=['GET'])
def ds_nguoi_dung():
	danh_sach_nguoi_dung = doc_danh_sach_nguoi_dung()
	d = {"Danh_sach_Nguoi_dung": danh_sach_nguoi_dung}
	return jsonify(d)
	# api get thông tin request từ web_server và trả về resonse object đã được chuẩn hoá dữ liệu thành json

# --- Cập nhật sản phẩm trang Admin --- 
@app.route('/danh-sach-san-pham/<int:ma_so>', methods=['PUT'])
def cap_nhat_san_pham(ma_so):
	danh_sach_san_pham = doc_danh_sach_san_pham()
	san_pham = [san_pham for san_pham in danh_sach_san_pham if san_pham['Ma_so']==ma_so] # list có 1 phần tử là thoả điều kiện 
	print(san_pham[0])
	
	# Kiểm tra thông tin gửi về từ WEB_SERVER
	if 'Ten' in request.json:
		san_pham[0]['Ten'] = request.json['Ten']
	if 'Don_gia' in request.json:
		san_pham[0]['Don_gia'] = request.json['Don_gia']
	if 'Mo_ta' in request.json:
		san_pham[0]['Mo_ta'] = request.json['Mo_ta']
	
	# Ghi thông tin vào CSDL
	duong_dan = thu_muc_san_pham + 'San_pham_' + str(ma_so) + '.json'
	ghi_file_json(duong_dan, san_pham[0])
	return jsonify(san_pham[0])

@app.route('/danh-sach-san-pham/<int:ma_so>', methods=['DELETE'])
def xoa_san_pham(ma_so):
	duong_dan = thu_muc_san_pham + 'San_pham_' + str(ma_so) + '.json'
	os.remove(duong_dan)
	return jsonify({"Response": "Success"})


@app.route('/danh-sach-san-pham', methods=['POST'])
def them_san_pham():
	if not request.json:
		abort(400) 
	
	# Nhận thông tin sản phẩm từ web server
	san_pham = request.json['San_pham']
	danh_sach_san_pham = doc_danh_sach_san_pham()
	ma_san_pham = tim_ma_san_pham_lon_nhat(danh_sach_san_pham) + 1 
	duong_dan = thu_muc_san_pham + 'San_pham_' + str(ma_san_pham) + '.json'
	ghi_file_json(duong_dan, san_pham)
	return san_pham, 201



if __name__=='__main__':
	app.run(debug=True, port=5001)
	# đặt port khác với web_server để chạy 2 bên 
