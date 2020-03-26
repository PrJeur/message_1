findings = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("\nIf you could visit one place in the world,where would you go? ")
	findings[name] = response
	repeat = input("\nWould you like to let another person respond? (yes/no) ")
	if repeat =='no':
		polling_active = False
print("\n          poll results        ")
for name,response in findings.items():
	print("\n"+name + " would like to visit "+ response + ".")
	 
