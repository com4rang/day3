person={'name':'Nick', 'address':'cheonan', 'email':'com4rang@naver.com'}
print(person)
print(person['address'])
person['Phone']='010-2032-2029'
print(person)

print(person.items())

for key, value in person.items() :
    print("\nkey \\" + "'"+key+"'")
    print("\nValue \\" + "'"+value+"'")