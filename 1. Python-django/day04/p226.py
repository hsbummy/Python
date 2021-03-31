score = (1,2,3,4,5)
item = ['item1', 1000, 1]

item2 = {'name':'item1', 'price': 1000 , 'count': 1}

print(item2['price'])
print(item2.get('price'))

#print(item2['pri'])
print(item2.get('pri','empty'))

if 'count' in item2:
    print(item2.get('count')*100)

item2['date'] = '20210105'
print(item2)

del item2['date']
print(item2)