import numpy as np

def list_transpose(a:list):

    new_array = np.array(a)
    lst = new_array.T.tolist()
    return lst

a = [[1,2,3],[4,5,6]]
lst = list_transpose(a)
print(lst)
