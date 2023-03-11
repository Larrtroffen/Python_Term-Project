# 7_神奇的日子
def main():
    for year in range(1901, 2001):
        for month in range(1, 13):
            for day in range(1, 32):
                if day * month == year % 100:
                    print(year, month, day)                
main()