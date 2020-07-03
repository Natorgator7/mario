get_int = input("How tall should the pyramids be, from 1 hash to 8?\n")
while True:
	if get_int.isdigit():
		get_int = int(get_int)
		kinda_inverse = get_int+1
		if get_int >=1 and get_int <=8:
			for x in range(0, get_int):
				print((" "*(get_int-1)+"#"*(kinda_inverse-get_int)+"  ")+("#"*(kinda_inverse-get_int)))
				get_int=get_int-1
			break
		else: 
			get_int = input("INVALID INPUT; enter a positive integer in the range, s'il vous plai\u0302t.\n")
	else: 
		get_int = input("INVALID INPUT; enter a positive integer in the range, s'il vous plai\u0302t.\n")