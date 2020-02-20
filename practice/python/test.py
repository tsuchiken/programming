# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
xc = 0
yc = 0
r_1 = 0
r_2 = 0
point = 0
ary_distances = []

input_lines = input().split(" ")
xc = int(input_lines[0])
yc = int(input_lines[1])
r_1 = int(input_lines[2])
r_2 = int(input_lines[3])

Point_Cnt = int(input())
for i in range(Point_Cnt):
    point = input().split(" ")
    sq_dist_c = (int(point[0]) - xc)**2 + (int(point[1]) - yc)**2
    print(str(sq_dist_c))
    ary_distances.append(sq_dist_c)

for j in ary_distances:
    print(j)
    if r_1**2 <= j and j <= r_2**2:
        print("yes")
    elif not(r_1**2 <= j and j <= r_2**2):
        print("no")
