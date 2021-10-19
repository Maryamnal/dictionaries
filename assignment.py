#mapping a dictionary

familylist = {'Name':'Mariam','Brother':'Ryan' }

print(type(familylist))

print(list(familylist.keys()))

# update

familylist.update({'Age':'21'})
print(familylist)

#iteration
for z in familylist.keys():
    print(z,familylist[z])

