import youtube_dl
import time
import pandas as pd
import os
import glob
import numpy as np

# setup output path
dir_path = os.path.dirname(__file__)
if not os.path.exists(dir_path + '/subtitles'):
    os.mkdir(dir_path + '/subtitles')

OUT_PATH = dir_path + '/subtitles'
SOURCE_FILE = 'video_list_cdc.csv'


def get_video_info():
    df = pd.read_csv(SOURCE_FILE)

    return df


def get_video_subtitles(yt_video_id):
    ydl_opts = {
        'skip_download': True,
        'outtmpl': f'{OUT_PATH}/%(id)s',
        'writesubtitles': True,
        # download chinese subtitle
        'subtitle': '--write-sub sub-lang zh-TW'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            url = f'https://www.youtube.com/watch?v={yt_video_id}'
            ydl.download([url])

        except Exception as err:
            print(str(err))

        time.sleep(1)


def check_download_files():
    video_meta = get_video_info()

    # get file name
    files_ytdl = glob.glob(OUT_PATH + '/*.vtt')
    files_asr = glob.glob(OUT_PATH + '/asr_result/*.srt')

    # check with video id
    files = files_ytdl + files_asr
    files = [d.split('/')[-1] for d in files]
    files = [d.split('.')[0] for d in files]
    video_meta['check'] = np.where(video_meta['videoId'].isin(files), 'y', 'n')

    # save file
    video_meta.to_csv(dir_path + '/vdown_check.csv', index=False)


if __name__ == '__main__':
    targets = get_video_info()['videoId'].to_list()

    for i in targets:
        get_video_subtitles(i)

    check_download_files()
