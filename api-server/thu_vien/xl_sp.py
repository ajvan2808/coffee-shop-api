from thu_vien.xl_chung import *
import os 

def doc_danh_sach_san_pham():
    danh_sach_san_pham = []
    for tap_tin in os.listdir(thu_muc_san_pham):
        duong_dan = thu_muc_san_pham + tap_tin
        san_pham = doc_file_json(duong_dan)
        danh_sach_san_pham.append(san_pham)
    return danh_sach_san_pham

def tim_ma_san_pham_lon_nhat(danh_sach_san_pham):
    ds_ma_so = []
    for san_pham in danh_sach_san_pham:
        ds_ma_so.append(san_pham['Ma_so'])
    return max(ds_ma_so)