def swap(a,b):
	return b,a

a = input("Enter number of processes you want?")

readyq = []

for i in range(0,a):

	process=[]

	b = input("Enter process name?")

	process.append(b)

	c = input("Enter arrival time?")

	process.append(c)

	d = input("Enter burst time?")

	process.append(d)

  readyq.append(process)

print("Ready queue before scheduling")

print(readyq)
 

print("Ready queue according to FIRST IN FIRST OUT is:")


for i in range(0,a):

	j=i+1

	while j<a:

 		if readyq[j][1]<readyq[i][1]:
			readyq[i],readyq[j] = swap(readyq[i],readyq[j])

		j+=1
    
print(readyq)

