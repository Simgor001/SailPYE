import sys
import os
import requests
import zipfile
from pathlib import Path
update_path = 'D:/SailPYE'
new_path = update_path + '/1.1.1'
temp_path = update_path + '/temp'
update_file = temp_path + '/1.1.1.zip'


def get_upgrade():
    print('正在获取更新...')

    try:
    
        with open(update_file, 'w+', encoding='UTF-8') as f:
            f.write(requests.get(
                'http://sailpye.eace.top/dist/1.1.1.zip'))
        print('正在安装更新...')


        z = zipfile.ZipFile(update_file, 'r')
        z.extractall(new_path)
        with open(update_path + '/Version', 'w+', encoding='UTF-8') as f:
            f.write('1.1.1')
    except:
        print('更新失败！')


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

    get_upgrade()
