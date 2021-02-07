#文件名取random會和内置的random模組冲突
#產生一個隨機數1-100
#讓使用者重複去猜
#猜對印出"終於猜對"#
#猜錯要告訴比答案大還小

#前置條件
import random
r = random.randint(1, 100)

#猜數字
while True:
    num = input('請猜數字（1-100）： ')#input會把輸入的東西存成字串
    num = int(num)#記得轉換資料型態
    if num == r:
         print('終於猜對')
         break
    else:
    	
        if num > r:
            print('小於', num)
        else:
            print('大於', num)