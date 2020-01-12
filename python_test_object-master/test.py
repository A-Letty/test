

path='python_test_object-master/input.txt'
with open(path) as f:
    List = [s.strip().split(':') for s in f.readlines()]


#読み込んだファイルの中からmを取り出し、数字に変換、残りのリストをそーと

m=List[len(List)-1]
m=m[0]
m=int(m)
del List[len(List)-1]
List.sort()

j=0
for i in range (len(List)): 
    if m% int(List[i][0]) == 0:
       print(List[i][1])
       j =j+1

if j==0:
    print(m)

