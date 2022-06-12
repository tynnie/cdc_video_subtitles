# CDC 直播影片字幕與清單
> 影片清單紀錄時間： 2020-01-22 - 2021-03-10

## 字幕檔來源

| 來源         | 檔案格式 | 說明                      |
|--------------|----------|-------------------------|
| youtube-dl   | `.vtt`   | 此為影片附帶的字幕               |
| cdc 合作單位 | `.srt`   | 此為雲端語音辨識軟體初步辨識結果，未經人工校正 |


## 利用youtube-dl下載字幕檔方式
可參考 `main.py`，建議操作：
1. clone this repository
2. install packages
`python3 -m pip install -r requirements.txt`

3. add your source file: 將 `main.py` 中 `SOURCE_FILE` 替換成你的檔案
- 此處以 `csv`檔案為例，可自行調整檔案格式與讀取檔案的方式
- 此檔案至少須包含 `videoId`（也就是提供video_id）

4. run `main.py`: 開始下載