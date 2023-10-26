# This script gets rid of logs every week so we don't blow up the disk space
import os

if __name__ == '__main__':
    log_dir = 'logs'
    for root, dirs, files in os.walk(log_dir):
        for fid in files:
            try:
                os.remove(fid)
            except Exception as e:
                print('Unable to remove log file!', e)
