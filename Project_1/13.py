# 噪声音量判断
try:
    db = float(input())
except:
    print("输入的不是数字！")
if db < 40:
    print("小于安静房间")
elif db == 40:
    print("安静房间")
elif db < 70:
    print("小于闹钟大于安静房间")
elif db == 70:
    print("闹钟")
elif db < 106:
    print("小于割草机大于闹钟")
elif db == 106:
    print("割草机")
elif db < 130:
    print("小于手提钻大于割草机")
elif db == 130:
    print("手提钻")
elif db > 130:
    print("大于手提钻")
else:
    print("输入有误")