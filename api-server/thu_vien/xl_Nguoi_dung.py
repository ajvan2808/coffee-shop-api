from thu_vien.xl_chung import *

def doc_danh_sach_nguoi_dung():   # function không cần tham số vì đã import function đọc file json
	danh_sach_nguoi_dung = doc_file_json(tap_tin_nguoi_dung) 
	return danh_sach_nguoi_dung