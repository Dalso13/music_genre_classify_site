import requests
import os
from dotenv import load_dotenv
import shutil

load_dotenv()


def file_save(before_path):
    print(">> file save")
    after_path = os.environ.get("VOLUME_PATH")
    name = shutil.copy(before_path, after_path)
    return os.path.basename(name)


# 도커 볼륨을 활용해서 처리할 예정
def socket(filename):
    try:
        print(">> predict...")
        server_url = os.environ.get("SERVER_URL")
        headers = {
            "User-Agent": "JDW"
        }
        data = requests.post(f"http://{server_url}", json={'filename': filename}, headers=headers)
        if data.status_code == 200:
            return data.json()
        else:
            return None
    except Exception as e:
        print(e)
        return None
