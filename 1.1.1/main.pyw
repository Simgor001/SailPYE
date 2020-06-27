import SailPYE
import sys
import os
from pathlib import Path
up_path = 'D:/SailPYE'
if __name__ == "__main__":
    argv = ''
    if len(sys.argv) > 1:
        argv = sys.argv[1]
    if Path(up_path).is_dir():
        if Path(up_path + '/Version').is_file():
            with open(up_path + '/Version', 'r', encoding='UTF-8') as f:
                version = f.read()
            if Path(up_path+'/'+version).is_dir():
                print('找到已更新的版本:' + version)
                os.system('start pythonw '+up_path+'/' +
                          version+'/SailPYE.py ' + argv)
                exit(0)
    os.chdir(sys.argv[0] + '/../')
    SailPYE.main()
