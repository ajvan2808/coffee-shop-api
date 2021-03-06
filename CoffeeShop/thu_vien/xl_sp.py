from CoffeeShop.thu_vien.xl_chung import *
import os 

def doc_danh_sach_san_pham():
	danh_sach_sp = []
	for tap_tin in os.listdir(thu_muc_san_pham):
		duong_dan = thu_muc_san_pham + tap_tin
		san_pham = doc_file_json(duong_dan)
		danh_sach_sp.append(san_pham)
		
	return danh_sach_sp

# Tạo chuỗi html danh sách sản phẩm 
def tao_chuoi_html_danh_sach_sp(danh_sach_sp):
	chuoi_html = '<div class="row">'

	for san_pham in danh_sach_sp:  # vòng lặp display các sp có trong list 
		chuoi_html += '''
        <div class="col-md-4" style="margin-bottom: 30px;">
            <div class="card">
                <img src="/static/san-pham/''' + san_pham['Hinh_anh'] + '''" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">''' + san_pham['Ten'] + '''</h5>
                    <p class="card-text">
                        Giá: ''' + '{:,}'.format(san_pham['Don_gia']).replace(',', '.') + '''
                    </p>
                    <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#sp''' + str(san_pham['Ma_so']) + '''">Thêm vào giỏ hàng</a>
                </div>
            </div>
        </div>


		<!-- Modal -->
        <div class="modal fade" id="sp''' + str(san_pham['Ma_so']) + '''" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg">

                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">''' + san_pham['Ten'] + '''</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>

                    <div class="modal-body">
                         <div class="container-fluid">
                            <div class="row">
                                <div class="col-md-4">
                                    <img src="/static/san-pham/''' + san_pham['Hinh_anh'] + '''" class="img-fluid" alt="Responsive image">
                                </div>

                                <div class="col-md-8">
                                    <h4>''' + san_pham['Ten'] + '''</h4>
                                    <p><strong>Giá: ''' + '{:,}'.format(san_pham['Don_gia']).format(',', '.') + '''</strong></p>
                                    <p>''' + san_pham['Mo_ta'] + '''</p>
                                </div>

                            </div>
                        </div>
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">OK</button>
                    </div>

                </div>
            </div>
        </div>
        '''


	chuoi_html += '</div>'
	return Markup(chuoi_html)