import time

## 変数の定義 ##
interval = 60 # 計測時間
text_input_path = r"C:\Users\mitssato\Cisco\docomo MoBills - Documents\次世代NW_SD-WAN支援サービス\400_Delivery\加盟店PoC\性能試験\事前検証\20220507-10途中経過\A0\stability_ping_A0_20220507-10.txt"
excel_output_path = r"C:\Users\mitssato\Cisco\docomo MoBills - Documents\次世代NW_SD-WAN支援サービス\400_Delivery\加盟店PoC\性能試験\事前検証\20220507-10途中経過\A0\stability_ping_A0_20220507-10.xlsx"
###############

if __name__ == '__main__':
    import data_handle
#     import plot