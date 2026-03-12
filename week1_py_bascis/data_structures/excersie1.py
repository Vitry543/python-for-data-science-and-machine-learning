# manipulating dictionaries
person={'name':'John','age':25,'course':'CS','grade':'A','subject':'Math'}
print(person)
print(person['name'])
print(person['age'])
print(person['course'])
print(person['grade'])
print(person['subject'])

person['grade']='B'
print(person)
person['subject']='Physics'
print(person)

person.update({'grade':'A','subject':'Math'})
print(person)

person['mail']='john@gmail.com'
print(person)

if 'grade' in person:
    del person['grade']
    print(person)
else:
    print("Key not found")

for i,j in person.items():
    print(i,j)