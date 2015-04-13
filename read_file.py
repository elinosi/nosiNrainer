import re
import sys
file_name=sys.argv[1]
fobj=open(file_name)
#fobj=open("SIMA.txt")
cpu=[]
jit=[]
task=[]
processIDs=[]
timeSlices=[]
i=0

#with open("SIMA.txt") as f:
#	content=f.readlines()

#print content


for line in fobj:
	b=line.rstrip()
	a=b.split()
	cpu.append(a[0])
	jit.append(a[1])
	task.append(a[2])
	#cpu[],jit[i],task[i]=a[0],a[1],a[2]
	#i=i+1
fobj.close()


myset=set(task)
processIDs=list(myset)

#len(cpu) #returns number of elements

#for idx, val in enumerate(jit):
#    print idx, val



#jit.append(jit[(len(jit))])

print len(processIDs)
print len(task)
print len(jit)

list_item=[]

for i in range(len(processIDs)):
	timeSlices.append(i)
	# list_item.append(i)
#print timeSlices

#print len(timeSlices)

post_item=()
dict_item=()

for proc in processIDs:
	for ta in task:
		if proc==ta:
			#print proc
			#print ta
			#print "yes"
			#print int(jit[task.index(ta)+1])
			#print int(jit[task.index(ta)])
			#print int(jit[task.index(ta)+1])-int(jit[task.index(ta)])
			#if int(jit[task.index(ta)-1]) > 0:
			timeSlices[processIDs.index(proc)]+=int(jit[task.index(ta)+1])-int(jit[task.index(ta)])
			#list_item.append(processIDs.index(proc),timeSlices[processIDs.index(proc)])
			#list_item.append(processIDs.index(proc),timeSlices[processIDs.index(proc)])
		        #list_item[processIDs.index(proc)]=("%s %s" % (processIDs.index(proc) ,timeSlices[processIDs.index(proc)]))

			#dict_item={processIDs.index(proc),timeSlices[processIDs.index(proc)]}
			#list_item.append(post_item)	



#print dict_item.keys()

fout = open("output.dat", "w")
#print len(timeSlices)

#dict_item=list(zip(processIDs,timeSlices))

#print sorted(list_item,key=lambda x:x[1])

#dict_item.sort(key=lambbda x : x[0]) 

#dict_item=sorted(dict_item.key())

#print dict_item

#for key in sorted(dict_item):
#	print "%s %s" % (key, int(dict_item[key]))

#print dict_item



#for i in range(len(timeSlices)):

	#list_item.append("%s %s\n" % (processIDs[i] , timeSlices[i])) 

#list_item=sorted(list_item, key=lambda x:x[0])

#print list_item

#for i in range(len(timeSlices)):
	#print list_item[i], list_item[i]

################list_item.append("%s\t %s\n" % (processIDs[i] , timeSlices[i])) 
#fout.write('%s' % list_item)

l=sorted(zip(processIDs,timeSlices), key=lambda x:x[0])
list1,list2=zip(*l)
##print list1 , list2



for i in range(len(timeSlices)):
	#print processIDs[i], timeSlices[i]
	print list1[i], list2[i]
	list_item.append("%s\t %s\n" % (i , list2[i]))
	fout.write(list_item[i])
	########	#fout.write  ("%s %s\n" % (i , timeSlices[i])
#	list_item.append("%s\t %s\n" % (processIDs[i] , timeSlices[i])) 
#	fout.write(list_item[i])
	#s=i,timeSlices[i]
	#print s
	#print list_item[i]
	#print post_item
	    #fout.write("%s %s\n" % (i , timeSlices[i]))
	#fout.write(s)
	#value=i,timeSlices[i]
	#s=str(value)
	#print value
fout.close()
	

#print list_item

