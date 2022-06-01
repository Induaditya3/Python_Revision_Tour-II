months={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
a=input('Enter the month: ').capitalize()
#a)
print(f'{a} has {months[a]} days.')
#b)
print('\n'*5,'Months sorted in ASCIIBETICALLY')
for month in sorted(months.keys()):
  print(month)
#c)
print('The months with 31 days are')
for month in months.keys():
  if months[month]==31:
    print('\t'*3,month)
#d)
for i in sorted(months.values()):
	for key in months:
		if months[key]==i:
			print(key,':',i)
			del months[key]
			break