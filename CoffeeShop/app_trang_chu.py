from CoffeeShop.thu_vien.xl_chung import *
from CoffeeShop.thu_vien.xl_sp import *


@app.route('/', methods=['GET', 'POST'])
def trang_chu():
	danh_sach_san_pham = doc_danh_sach_san_pham()
	chuoi_html_danh_sach_sp = tao_chuoi_html_danh_sach_sp(danh_sach_san_pham)

	return render_template('Trang_chu.html', ChuoiHTMLDanhSachSanPham=chuoi_html_danh_sach_sp)