from CoffeeShop.thu_vien.xl_chung import *
from urllib.request import urlopen
import os

def doc_danh_sach_san_pham_tu_api():
    url = url_api + 'danh-sach-san-pham'
    url_response = urlopen(url)
    du_lieu = json.loads(url_response.read().decode())
    return du_lieu['Danh_sach_San_pham']
# du_lieu được gán giá trị của d (bên API_SERVER/app_API) d chỉ có 1 phần tử là dict {"Danh_sach_San_pham": danh_sach_san_pham}

def tra_cuu_san_pham(chuoi_tra_cuu, danh_sach_san_pham):
    danh_sach_ket_qua = list(filter(lambda san_pham: chuoi_tra_cuu.lower() in san_pham['Ten'].lower(), danh_sach_san_pham))
    return danh_sach_ket_qua


def lay_chi_tiet_san_pham(danh_sach_san_pham, ma_so):
    danh_sach = list(filter(lambda sp: sp["Ma_so"] == ma_so, danh_sach_san_pham))
    san_pham = danh_sach[0] if len(danh_sach) == 1 else None
    return san_pham


def lay_thong_tin_danh_muc(danh_sach_san_pham):
    ds_danh_muc = {}
    for san_pham in danh_sach_san_pham:
        danh_muc = san_pham['Danh_muc']
        ds_danh_muc[danh_muc['Ma_so']] = danh_muc
    return ds_danh_muc


def tim_ma_san_pham_moi_nhat(danh_sach_san_pham):
    ds_ma_so = []
    for san_pham in danh_sach_san_pham:
        ds_ma_so.append(san_pham['Ma_so'])
    return max(ds_ma_so)



# =========== Tạo chuỗi html hiển thị danh sách sản phẩm Dành cho KHÁCH HÀNG ============
def tao_chuoi_html_danh_sach_sp(danh_sach_san_pham):
    chuoi_html = '<div style="text-align: center; margin-bottom: 20px;"> <h3>DANH SÁCH SẢN PHẨM (' + str(len(danh_sach_san_pham)) + ')</h3> </div>'
    chuoi_html += '<div class="row">'

    for san_pham in danh_sach_san_pham:  # san_pham: dict,   danh_sach_san_pham: list
        chuoi_html += '''
        <div class="col-md-4" style="margin-bottom: 30px;">
            <div class="card">
                <img src="''' + url_api + '''static/san-pham/''' + san_pham['Hinh_anh'] + '''" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">''' + san_pham['Ten'] + '''</h5>
                    <p class="card-text">
                        Giá: ''' + '{:,}'.format(san_pham['Don_gia']).replace(',', '.') + '''
                    </p>
                    <a href="#" class="btn btn-primary" data-toggle="modal" data-target="#sp''' + str(san_pham['Ma_so']) + '''">Chi tiết >></a>
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
                                    <img src="''' + url_api + '''static/san-pham/''' + san_pham['Hinh_anh'] + '''" class="img-fluid" alt="''' + san_pham['Hinh_anh'] + '''">
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
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Đóng</button>
                    </div>
                </div>
            </div>
        </div>
        '''
        
    chuoi_html += '</div>'
    return Markup(chuoi_html)





# =========== Tạo chuỗi html hiển thị danh sách sản phẩm Dành cho ADMIN ============
def tao_chuoi_html_danh_sach_sp_admin(danh_sach_san_pham):
    chuoi_html = '<div style=" text-align: center; margin-bottom: 20px;"> <h3> DANH SÁCH SẢN PHẨM (' + str(len(danh_sach_san_pham)) + ')</h3></div>'
    chuoi_html += ''' 
    <table class="table">
		<thead>
			<tr>
				<th scope="col">No</th>
				<th scope="col"> Hình ảnh </th>
				<th scope="col"> Tên sản phẩm </th>
				<th scope="col"> Đơn giá </th>
                <th scope="col"> Danh mục </th>
                <th scope="col"> Tác vụ </th>
			</tr>
		</thead>
		<tbody>'''

    for san_pham in danh_sach_san_pham:
        chuoi_html += '''
			<tr>
				<th scope="row"> '''+ str(danh_sach_san_pham.index(san_pham) + 1) +''' </th>
				<td>
                    <img src="''' + url_api + '''static/san-pham/''' + san_pham['Hinh_anh'] + '''" height="80" alt=" '''+ san_pham['Hinh_anh'] +''' ">
                    <!-- ở những đoạn ghép giá trị dynamic vào đường dẫn nên chú ý khoảng trắng -->
                </td>
				<td>'''+ san_pham['Ten']+'''</td>
                <td>'''+ '{:,}'.format(san_pham['Don_gia']) +'''</td>
                <td>'''+ san_pham['Danh_muc']['Ten']+'''</td>
				<td>
                    <a href="/admin/cap-nhat-san-pham/'''+ str(san_pham['Ma_so'])+ ''' "> Cập nhật </a> |
                    <a href="#" data-toggle="modal" data-target="#sp'''+ str(san_pham['Ma_so']) + '''"> Xóa </a>
                </td>
			</tr>
            
            <!-- Modal -->
            <div class="modal fade" id="sp''' + str(san_pham['Ma_so']) + '''" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
	            <div class="modal-dialog" role="document">

		            <div class="modal-content">
			            <div class="modal-header">
				            <h5 class="modal-title" id="exampleModalLabel"> Xoá sản phẩm <strong>'''+ san_pham['Ten'] +'''</strong></h5>
				            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
					            <span aria-hidden="true">&times;</span>
				            </button>
			            </div>
			        
                        <div class="modal-body">
				        Bạn chắc chắn muốn xoá sản phẩm này ? 
			            </div>
			        
                        <div class="modal-footer">
                        <!-- cần nhớ bỏ trong form POST và type là submit dành cho button Đồng ý -->
    
                            <form method="POST">
				                <button type="button" class="btn btn-primary" data-dismiss="modal">Huỷ</button>
				                <button type="submit" class="btn btn-danger">Đồng ý</button>
                                <input hidden type="text" name="MaSo_Xoa" value="''' + str(san_pham['Ma_so']) + '''" />
                            </form>
                        </div>

		            </div>
	            </div>
            </div>
            '''

    chuoi_html += '''
		</tbody>
	</table>
    '''

    return Markup(chuoi_html)
