#!/usr/bin/python3
for i in range(1,21):
	for a in range(1,31):
		for b in range(1,41):
			for c in range(1,51):
				if(i%2==0 & a%3==0 & b%4==0 & c%5==0):
					print(i,"\t",a,"\t",b,"\t",c,"\t",)
