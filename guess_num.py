#文件名取random會和内置的random模組冲突
#產生一個隨機數1-100
#讓使用者重複去猜
#猜對印出"終於猜對"#
#猜錯要告訴比答案大還小

#前置條件
import random
start = int(input('請決定隨機數字開始範圍：'))#同時轉換資料型態
end = int(input('請決定隨機數字結束範圍：'))

r = random.randint(start, end)
count = 0 #已猜次數

#猜數字
while True:
    count += 1#count = count + 1
    num = int(input('請猜數字： '))#input會把輸入的東西存成字串 同時轉換資料型態
    if num == r:
         print('終於猜對')
         print('已猜', count, '次')
         break
    else:
        if num > r:
            print('小於', num)
        else:
            print('大於', num)
    print('已猜', count, '次')#避免重複性太高