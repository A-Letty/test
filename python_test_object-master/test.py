

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













#lst = literal_eval(List)
#print(lst[0])

#text = r'[{"id": "3", "name": "Jone", "age": "23"}, {"id": "1", "name": "Anne", "age": "17"}, {"id": "2", "name": "Ken", "age": "21"}]'
#lst = literal_eval(text)

#pprint(lst)
#print(type(lst), type(lst[0]))



