import sys
import os
import requests
import zipfile
import threading
from pathlib import Path
update_path = 'D:/SailPYE'
new_path = update_path + '/1.1.1'
temp_path = update_path + '/temp'
update_file = temp_path + '/1.1.1.zip'


def get_upgrade():
    try:
        print('正在自动更新版本1.1.1')
        r = requests.get(
            'https://sailpye.eace.top/dist/1.1.1.zip')
        with open(update_file, 'w+b') as f:
            f.write(r.content)
        z = zipfile.ZipFile(update_file, 'r')
        z.extractall(new_path)
        with open(update_path + '/Version', 'w+', encoding='UTF-8') as f:
            f.write('1.1.1')
    except Exception:
        print('更新失败！')
        exit()


if __name__ == "__main__":
    os.chdir(sys.argv[0] + '/../')

    if not Path(update_path).is_dir():
        os.makedirs(update_path)

    isExists = os.path.exists(new_path)
    if not isExists:
        os.makedirs(new_path)

    isExists = os.path.exists(temp_path)
    if not isExists:
        os.makedirs(temp_path)

    upgrade = threading.Thread(target=get_upgrade, daemon=True)
    upgrade.start()
    upgrade.join()
