import os
from loguru import logger
from dotenv import load_dotenv
import json

def load_env():
    load_dotenv()
    cookies_str = os.getenv('COOKIES')
    return cookies_str

def get_list_cookies():
    with open("network_cookies.json", "r") as f:
        list_cookies = json.load(f)
    return list_cookies

def init():
    media_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../datas/media_datas'))
    excel_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../datas/excel_datas'))
    for base_path in [media_base_path, excel_base_path]:
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            logger.info(f'创建目录 {base_path}')
    cookies_str = load_env()
    list_cookies = get_list_cookies()
    base_path = {
        'media': media_base_path,
        'excel': excel_base_path,
    }
    return cookies_str, base_path
