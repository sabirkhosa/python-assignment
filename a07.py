## IMPORTS GO HERE
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###
def split_safe(line):
    if line=="":
        ist1=[]
        return ist1
    ist1=['']
    index=0
    bol=False
    blank=False
    for i in line:
        if i =="," and bol==False:
            ist1.append('')
            index=index+1
            blank=True
        elif i=="'" and bol==False:
            bol=True
        elif i=="'" and bol==True:
            bol=False 
        elif i=="" and blank==False:
            ist1[index]=ist1[index]+i
        elif i !='':
            ist1[index] = ist1[index]+i
            blank=False
    ist1 = list


### YOUR CODE FOR read_data() FUNCTION GOES HERE ###
def  read_data(k,l):
	r=[]
	import os
	filename=os.path.join(k,l)
	with open(filename , "r") as i:
		for line in i:
			e=split_safe(line)
			r.append(e)
		return(r)
	

#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass
