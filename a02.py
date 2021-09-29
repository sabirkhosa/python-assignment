## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR jobOffer GOES HERE ####
def jobOffer (salary,location="peshswar"):
    if location=="Peshawar" and salary>40000:
        return "I’ll take it!"
    elif location=="Karachi" and salary<100000:
        return "No way"
    elif salary>=60000:
        return "I’ll take it!"
    else:
        return "No thanks, I can find something better."
    
#### End OF MARKER


