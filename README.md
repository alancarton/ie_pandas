# ie_pandas 
ie_pandas Group Project.

#This is DataFrame Project for MBD Advanced Python course: Group 2
-	Alan Carton
-	Leon Junique
-	Federico Loguercio
-	Scott Pan

#Installation:
#From the code directory
Install using pip install .

#Uninstallation:
pip uninstall ie_pandas

# If making amendments to the code:
Ensure the code complies with black / pep8
Validate both src and tests directories.
black --check src tests # Validates which files to be changed
black src tests # Will perform the changes required to the files.
Check code style.
pycodestyle src tests # will show if files conform to requirements
Lines of code cannot exceed 79 characters
Cannot be mix of Tabs and Spaces in code
Cannot have trailing whitespace after code.

# To use the code.
from ie_pandas import DataFrame
df = DataFrame(data=<use dictionary>)
# or
df = DataFrame(data=<use array>, columns=<list>)

# To change column names
df.columns = [list of columns]
# to change the data use the data property.
df.data = {data dictionary to replace}

# Functions descriptions:
#sum():
It calculates the sum of the underlying column.

#max():
It shows the biggest element of the column.

#min():
It shows the smallest element of the column.

#mean():
It calculates the mean of the elements in the column.

#median():
It caculates the median of the elements in the column.

#percentile():
It calculates the 25th, 50th, and 75th percentile of the column.

#unique():
It shows all the unique elements in the column.

#std():
It shows the standard deviation of the column. 

