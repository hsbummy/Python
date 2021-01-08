def insert(**a):
    id = a['id']
    pwd = a['pwd']
    name = a['name']
    age = a['age']
    print('%s %s %s %d inserted.....' %(id, pwd,name,age))



def select(**a):
    id = a['id']
    data = []
    data.append(id)
    data.append('pw01')
    data.append('kim')
    data.append(25)
    return data

def allselect():
    data= [];
    data.append(['id01','pw01','kim',25])
    data.append(['id02', 'pw02', 'kim2',26])
    data.append(['id03', 'pw03', 'kim3',27])
    data.append(['id04', 'pw04', 'kim4',28])
    data.append(['id05', 'pw05', 'kim5',29])
    return data

# my = insert(id='tkdqja8', pwd= 'qwer1234', name='한상범')
# print(my)