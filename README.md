# ie_pandas 
ie_pandas Group Project.

#This is DataFrame Project for MBD Advanced Python course: Group 2
-	Alan Carton
-	Leon Junique
-	Federico Loguercio
-	Scott Pan

# Datatypes Supported
int, float, bool columns.  All others are converted to String.
Rows, Arrays / Lists use Zero-based index.

# Required for use:
numpy
matplotlib
pytest

#Installation: (Library Developer and User)
Download directory structure to location on drive.
From the code directory
Install using pip install .

#Uninstallation:
pip uninstall ie_pandas

# Library Developer:
If making amendments to the code:
Install both pytest and black for testing.
- Ensure the code complies with black / pep8
- Validate both src and tests directories.

# Validates which files to be changed
> black --check src tests 

# Will perform the changes required to the files.
> black src tests 

# Check code style.
# will show if files conform to requirements
> pycodestyle src tests 

#Lines of code cannot exceed 79 characters
#Cannot be mix of Tabs and Spaces in code
Cannot have trailing whitespace after code.

# Testing by Developers.
# To test functionality
> pytest

# To test Code coverage
> pytest --cov

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
It calculates the sum of the underlying numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#max():
It shows the biggest element of the numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#min():
It shows the smallest element of the numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#mean():
It calculates the mean of the elements in the numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#median():
It caculates the median of the elements in the numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#percentile():
It calculates the 25th, 50th, and 75th percentile of the numeric columns.
Returns an array of values for the columns, None for non numeric columns.

#unique_element():
It shows all the unique elements in the columns.
Returns an array of values for the columns, None for all columns.

#std():
It shows the standard deviation of the numeric columns.
Returns an array of values for the columns, None for non numeric columns. 

