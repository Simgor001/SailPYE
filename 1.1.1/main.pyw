import SailPYE
import sys
import os
from pathlib import Path
update_path = 'D:/SailPYE'
temp_path = update_path + '/temp'
if __name__ == "__main__":
    argv = ''
    if len(sys.argv) > 1:
        argv = sys.argv[1]
    if Path(update_path).is_dir():
        if Path(update_path + '/Version').is_file():
            with open(update_path + '/Version', 'r', encoding='UTF-8') as f:
                version = f.read()
            if Path(update_path+'/'+version).is_dir():
                print('找到已更新的版本:' + version)
                os.system('start pythonw '+update_path+'/' +
                          version+'/SailPYE.py ' + argv)
                exit(0)
    os.chdir(sys.argv[0] + '/../')
    SailPYE.main()
