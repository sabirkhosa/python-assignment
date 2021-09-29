## IMPORTS GO HERE if required

## END OF IMPORTS 


#### YOUR CODE FOR saddle_points GOES HERE ####
def saddle_points(matrix):
    for j in range(len(matrix) - 1):
        x = j + 1
        if len(matrix[j]) != len(matrix[x]):
            print("invalid syntax")
    results = set()
    for index, row in enumerate(matrix):
        candidates = [(i, x) for i, x in enumerate(row) if x == max(row)]
        for i, n in candidates:
            column = [row[i] for row in matrix]
            if n == min(column):
                results |= {(index, i)}
    return results


#### End OF MARKER


