while True:
    w = input("請問你想把哪個數字轉換成羅馬數字？")
    w = w.strip()
    try:
        n = int(w)
        if not 0 < n < 4000:
            print("請輸入範圍1~3999內的整數！")
            continue
        break
    except ValueError:
        print("請輸入範圍1~3999內的整數！")
        continue

# rn = Roman numerals 
def int_to_rn(n):
    rn = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4),
        ("I", 1)
    ]
    ans = ""
    for roman, value in rn:
        ans += roman * (n // value)
        n %= value
    return ans

print(int_to_rn(n))