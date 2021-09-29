## IMPORTS GO HERE
from scipy.constants import c
## END OF IMPORTS 


#### YOUR CODE FOR calculate_force GOES HERE ####

def calculate_force(m,a):
    if type(a)==float and type(m)==float :
        f=m*a
        return (f)
    else:
        return None
#### End OF MARKER


#### YOUR CODE FOR find_and_print_energy GOES HERE ####
def find_print_energy(m):
    if type(m)==float:
	    e=m*pow(c,2)
	    print('The energy equivalent of mass',m,'is:',e)
	    return (e)
    else:
        return None
#### End OF MARKER  




if __name__ == '__main__': 
    print(calculate_force(1.0, 0.2))
    print(find_and_print_energy(0.0009))  

