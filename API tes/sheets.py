import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

chp = ServiceAccountCredentials.from_json_keyfile_name("chp.json", scope)

client = gspread.authorize(chp)

sheet = client.open("kaikai").sheet1

data = sheet.get_all_records()
row_num = 2
while True:
    shoe_size = []
    shoes_number = []
    infoput = [1,2,3,4,5]
    Item_No= input("货号：")
    infoput[0] = Item_No
    shoe_name = input("鞋子名称：")
    infoput[1] = shoe_name
    while True:
        size = input("鞋码：")
        if size == '0':
            break
        shoe_size.append(size)
    num = len(shoe_size)
    num2 = num
    i = 0
    while num > 0:
        number = input(shoe_size[i] + "鞋码数量：")
        shoes_number.append(number)
        i = i + 1
        num = num - 1
    purchase_price = input("进货价格：")
    infoput[4] = purchase_price

    while num < num2:
        infoput[2] = shoe_size[num]
        infoput[3] = shoes_number[num]
        sheet.insert_row(infoput, row_num)
        num = num + 1
        row_num = row_num + 1
