from csv import reader

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = []

    readFile = reader(open(csv_file_path))

    #Check if there is number if yes change to integer else keep as string
    for row in readFile:
        list_row = []
        for val in row:
            if val.isdigit():
                list_row.append(int(val))
            else:
                list_row.append(val)
        res.append(list_row)
    
    return res
