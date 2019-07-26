import os
import subprocess
import sys
sys.path.append(r'D:\JetBrains\PycharmProjects\test\ffmpeg\bin')


def amr2mp3(amr_path, mp3_path=None):
    path, name = os.path.split(amr_path)
    if name.split('.')[-1] != 'amr':
        print('not a amr file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1] != 'mp3':
        mp3_path = os.path.join(path, name.split('.')[0] + '.mp3')
    error = subprocess.call(['ffmpeg/bin/ffmpeg', '-i', amr_path, mp3_path])
    print(error)

    if error:
        return 0
    print('success')
    return mp3_path

def avi2mp3(amr_path, mp3_path=None):
    path, name = os.path.split(amr_path)
    if name.split('.')[-1] != 'avi':
        print('not a avi file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1] != 'mp3':
        mp3_path = os.path.join(path, name.split('.')[0] + '.mp3')
    error = subprocess.call(['ffmpeg/bin/ffmpeg', '-i', amr_path, mp3_path])
    print(error)

    if error:
        return 0
    print('success')
    return mp3_path

def vedio2mp3(amr_path, mp3_path=None):
    path, name = os.path.split(amr_path)
    if name.split('.')[-1] not in ['avi', 'f4v', 'mp4']:
        print('not satisfied file')
        return 0
    if mp3_path is None or mp3_path.split('.')[-1] != 'mp3':
        mp3_path = os.path.join(path, name.split('.')[0] + '.mp3')
    error = subprocess.call(['ffmpeg/bin/ffmpeg', '-i', amr_path, mp3_path])
    print(error)

    if error:
        return 0
    print('success')
    return mp3_path
if __name__ == '__main__':
    # amr_path = 'Young.Sheldon.S02E04.720p.mp4'
    # vedio2mp3(amr_path, r'D:\JetBrains\PycharmProjects\test\YoungSheldon')
    amr_path=r'E:\BaiduNetdiskDownload\Elite class 01\DesperateHousewives5.avi'
    mp3_path=r'E:\BaiduNetdiskDownload\Elite class 01\E05MarthaHuper.mp3'
    vedio2mp3(amr_path, mp3_path)
