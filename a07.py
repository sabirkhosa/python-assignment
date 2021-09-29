## IMPORTS GO HERE
## END OF IMPORTS


### YOUR CODE FOR split_safe() FUNCTION GOES HERE ###
def split_safe(line):
    if line=="":
        ist1=[]
        return ist1
    ist1=['']
    index=0
    bool=False
    blank=False
    for i in line:
        if i =="," and bool ==False:
            ist1.append('')
            index=index +1
            blank=True
        elif i=="'" and bool ==False:
            bool=True
        elif i=="" and bool==True:
            bool=False
        elif i =="" and blank==False:
            ist1[index] =ist1[index]+i
        elif i !='':
            ist1[index] = ist1[index]+i
            blank=False
return ist1
#### End OF MARKER



### YOUR CODE FOR read_data() FUNCTION GOES HERE ###

#### End OF MARKER

if __name__ == '__main__':
    print(split_safe("Name,'Father Name',Address,Age"))
    print(split_safe("Ali,Tariq,'House 10, Street 20',30"))

    print(read_data('', 'file.csv'))
    pass
