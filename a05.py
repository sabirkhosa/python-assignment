## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(n):
    if n==1:
        return False
    elif type(n)==float:
        return False
    else:
        for i in range (2,n):
            if (n%i)==0:
                return False
            else:
                return True
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    
    for i in range (1,x+1):
        if x%i==0:
            print(i)
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####

#### End OF MARKER



if __name__ == '__main__':
    print(is_prime(499))  # should return True

    print(get_largest_prime(10))  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
