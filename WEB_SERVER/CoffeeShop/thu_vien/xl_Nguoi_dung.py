from CoffeeShop.thu_vien.xl_chung import *
from urllib.request import urlopen

def doc_danh_sach_nguoi_dung_tu_api():
	url = url_api + 'danh-sach-nguoi-dung'
	url_response = urlopen(url)
	du_lieu = json.loads(url_response.read().decode())
	return du_lieu['Danh_sach_Nguoi_dung']
	# sau khi gửi request đến api, app_api trả về response object là json (list có 1 dict, 1 key). Web server read và decode rồi display giá trị của key Danh_sach_Nguoi_dung (là list ds nguoi dung)


def nguoi_dung_dang_nhap(danh_sach_nguoi_dung, ten_dang_nhap, mat_khau):
	nguoi_dang_nhap = list(filter(lambda nguoi_dung: nguoi_dung['Ten_dang_nhap'] == ten_dang_nhap and nguoi_dung['Mat_khau'] == mat_khau,
									danh_sach_nguoi_dung))
	ket_qua = nguoi_dang_nhap[0] if len(nguoi_dang_nhap) ==1 else None

	return ket_qua


def tao_chuoi_html_thong_tin_nguoi_dung(ho_ten, nhom_nguoi_dung, url_dang_xuat):
	chuoi_html = '''
	<p>
		<div class="btn-group">
			<button type="button" class="btn btn-link dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				<strong> Xin Chào ''' + ho_ten + ''' </strong>
			</button>
			
			<div class="dropdown-menu">
				<a class="dropdown-item" href=" '''+ url_dang_xuat +''' ">Đăng xuất</a>
			</div>
		</div>
	</p>
	<p style="padding-left: 15px;"> '''+ nhom_nguoi_dung +''' </p>'
'''
	return Markup(chuoi_html)