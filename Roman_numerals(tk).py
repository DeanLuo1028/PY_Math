RN = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4),
        ("I", 1)
    ]

def int_to_rn(n):
    ans = ""
    for roman, value in RN:
        ans += roman * (n // value)
        n %= value
    return ans

def rn_to_int(rn):
    n = 0
    i = 0
    while i < len(rn):  # 逐步處理 rn 的每個字母
        for roman, value in RN:  # 嘗試從最大數值開始匹配
            if rn[i:i+len(roman)] == roman:  # 如果找到匹配的羅馬數字
                n += value   # 加到結果 n
                i += len(roman)  # 移動索引 i
                break  # 找到匹配後，跳出 for 迴圈，繼續處理下一部分
        else:  # 當 for 迴圈跑完 **都沒有匹配成功**，才執行這裡
            raise ValueError("Invalid Roman numeral: " + rn)  # 無效的羅馬數字

    return n