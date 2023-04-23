import numpy as np
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)
import numpy as np
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
print ("Largest element is:", arr.max())
print ("Row-wise maximum elements:",
                    arr.max(axis = 1))
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))
print ("Sum of all array elements:",
                            arr.sum())
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))
import numpy as np
a = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]])
print ("Array elements in sorted order:\n",
                    np.sort(a, axis = None))
print ("Row-wise sorted array:\n",
                np.sort(a, axis = 1))
print ("Column wise sort by applying merge-sort:\n",
            np.sort(a, axis = 0, kind = 'mergesort'))
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))
import pandas as pd
import numpy as np
ser = pd.Series()   
print(ser)
data = np.array(['g', 'e', 'e', 'k', 's'])
ser = pd.Series(data)
print(ser)
import pandas as pd
df = pd.DataFrame()
print(df)
lst = ['kuldeep', 'jaydeep', 'mahendra', 'kunal', 
            'nikhilesh', 'himanshu']
df = pd.DataFrame(lst)
print(df)
Matplotlib
from matplotlib import pyplot as plt
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.plot(x,y)
plt.show()
Bar plot : 
from matplotlib import pyplot as plt
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.bar(x,y)
plt.show()
Histogram:
from matplotlib import pyplot as plt
y = [10, 5, 8, 4, 2]
plt.hist(y)
plt.show()
Scatter Plot:
from matplotlib import pyplot as plt
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]
plt.scatter(x, y)
plt.show()