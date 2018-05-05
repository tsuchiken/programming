#人数入力
numOfChildren = int(input("children(under 18s) "))
numOfAdult = int(input("adult "))
numOfElder = int(input("elder(over 65s) "))

#計算
total_num = numOfChildren + numOfAdult + numOfElder

child_prc = 500
adult_prc = 1000
elder_prc = 850

total_prc = child_prc * numOfChildren + adult_prc * numOfAdult + elder_prc * numOfElder

#割引処理
if total_num >= 10:
	print("10% discount")
	total_prc = round(total_prc * 0.8)

#出力
print("children:\t{0} persons * {1} $ = {2} $".format(numOfChildren,child_prc,numOfChildren*child_prc))
print("adult:\t\t{0} persons * {1} $ = {2} $".format(numOfAdult, adult_prc, numOfAdult*adult_prc))
print("elder:\t\t{0} persons * {1} $ = {2} $".format(numOfElder, elder_prc, numOfElder*elder_prc))
print("sum:\t\t{0} persons {1} $".format(total_num, total_prc))
