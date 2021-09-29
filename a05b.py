## IMPORTS GO HERE IF REQUIRED

## END OF IMPORTS


### YOUR CODE FOR writeMissingEntries FUNCTION GOES HERE ###


def  writeMissingEntries(x):
    with open(x,"r") as f:
        for line in f:
            a=line.strip().split(",")
            try:
                a[4]
            except IndexError:
                with open('logfile.log',"a")as f:
                    a=str(a)
                    f.write(a+'\n')





#### End OF MARKER







#if __name__ == '__main__':
    
    #data = ['18P-0006,Ahmed Khan,1,8','18P-0130,Ali Hassan,A,2,4','18P-6061,Ikram Durrani,12,4','18P-6089,Muhammad,14','18P-6154,Syed Shahid Khaqani,1,2,3','18P-6064,Hamza Arif,6.5,7,2.5','18P-6065,MuhammadAli,2,3.2,4']

    #writeMissingEntries(data)

    #"""
    # output of logfile.log:
    #[18P-0006,Ahmed Khan,1,8]
    #[18P-0006,Ahmed Khan,1,8]
    #[18P-6061,Ikram Durrani,12,4]
    #[18P-6089,Muhammad,14]

   # """
