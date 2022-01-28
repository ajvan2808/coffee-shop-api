from CoffeeShop.thu_vien.xl_chung import *
from CoffeeShop.thu_vien.xl_sp import *


@app.route('/', methods=['GET', 'POST'])
def index():
	# Đọc danh sách
	danh_sach_san_pham = doc_danh_sach_san_pham_tu_api()
	danh_sach_san_pham_hien_thi = danh_sach_san_pham 	# tạo biến phụ cho tìm kiếm 

	# tìm kiếm 
	tu_khoa = ''
	if request.form.get('TimKiem'):
		tu_khoa = request.form.get('TimKiem')
		danh_sach_san_pham_hien_thi = tra_cuu_san_pham(tu_khoa, danh_sach_san_pham)

	# truy xuất
	chuoi_html_danh_sach_san_pham = tao_chuoi_html_danh_sach_sp(danh_sach_san_pham_hien_thi)

	return render_template('Trang_chu.html', ChuoiHTMLDanhSachSanPham=chuoi_html_danh_sach_san_pham, TimKiem=tu_khoa)