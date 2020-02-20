int_inputCount = input()
ary_logList = []
ary_logListFiltered = []

for i in range(int(int_inputCount)):
    ary_logList.append(input())

for j in ary_logList:
    if(j in "ai"):
        print("OK")
        ary_logListFiltered.append(j)

if(len(ary_logListFiltered) != 0):
    print("test")
    for k in ary_logListFiltered:
        print(k)
else:
    print("None")
