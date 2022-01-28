from flask import request, render_template, Markup, url_for, redirect, session, flash
import json 
from CoffeeShop import app 
import requests 
# The requests module allows you to send HTTP requests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

# Đã tạo biến chung cho đường dẫn ở API_SERVER/thu_vien/xl_chung.py
url_dang_xuat = '/admin/dang-xuat'
url_api = 'http://127.0.0.1:5001/'

# Loại bỏ hàm xử lý file json doc_file_json và ghi_file_json vì đã có bên API_SERVER