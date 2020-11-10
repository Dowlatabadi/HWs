#python code for question no1

import time
dict1 = {}
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 

count = 0
tic = time.perf_counter()
for line in Lines:
	line=''.join(filter(str.isalpha, line))
	count=count+1
	sorted_string=''.join(sorted(sorted( line.strip()), key=str.upper))
	# print("Line[{}]: sorted= {}".format(count,sorted_string))

	if sorted_string not in dict1:
		dict1[sorted_string]=1
	else:
		dict1[sorted_string] =dict1[sorted_string]+1


#order by freq
sorted_dict = sorted(dict1.items(), key=lambda kv: kv[1])

	
toc = time.perf_counter()

# for x,freq in sorted_dict:
# 	print(x,freq)

print(f"Read and Scan(Grouping by dictionary) in {toc - tic:0.4f} seconds")
print(len(sorted_dict))


#improving the grouping
dict2 = {}

tic1 = time.perf_counter()
for line in Lines:
	
	map1=""
	#len of 26 string coresponding to freq of each char
	alphab_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
	
	for ch1 in line.strip():
		if (ch1.isalpha()==False):
			continue
	
		alphab_dict[ch1] =alphab_dict[ch1]+1
		
	map1=''.join(map(str, alphab_dict.values()) )
	# print("Line[{}]: sorted= {}".format(count,sorted_string))
	decimal=int(map1)
	if decimal not in dict2:
		dict2[decimal]=1
	else:
		dict2[decimal] =dict2[decimal]+1
toc1 = time.perf_counter()

sorted_dict2 = sorted(dict2.items(), key=lambda kv: kv[1])
# for x,freq in sorted_dict2:
# 	print(x,freq)

print(f"2-Read and Scan(Grouping by dictionary) in {toc1 - tic1:0.4f} seconds")
print(len(sorted_dict2))
