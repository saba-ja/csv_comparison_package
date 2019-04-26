# header_validator module

This module validates the header of the csv file.

## Parameters

From the ```Compare``` class header_validator module will use the following instance variables:

1. ```original_header```
2. ```header```
3. ```header_row```
4. ```index_column_name```
5. ```compare_only_mapped_columns```

And class variable:
1. ```map_columns``` 

#### original_header and header parameter
The ```original_header``` and ```header``` parameter are used to keep the file header information.
The ```header``` parameter will initially be the copy of the ```original_header```, but it will be 
modified to be used in the pandas and the application. 
The structure of the ```original_header``` and ```header``` is the following:

```
[
    {
    "column_name": "name of a column with type string (i.e first_name)", 
    "column_location": an integer greater than 0, 
    "column_type": "index|mapped|unnamed|duplicate|disjunctive|not_checked|"
    },
    ...    
]
``` 

* The ```column_name``` will keep the name of the column
* The ```column_location``` will keep the location of the header.  
* The ```column_type``` will keep the flags that will be used to
identify the different types of the column.

**Note** The column_location is a ```1``` based. The first column of the file is located at ```1``` 
and not ```0```.


There are ```7``` different types of column where ```5``` of them have flags:

1. ```index```: header that contains the primary key (index) of each row
2. ```mapped```: headers that user has explicitly requested to be checked with each other
3. ```unnamed```: headers that are empty
4. ```duplicate```: headers that have exactly the same value
5. ```disjunctive```: headers that are only in one file and not in the other
6. ```not_checked```: headers that user does not need to check
7. ```checked```: headers that need to be checked for string differences



#### header_row
The parameter used for setting the location of the header row is ```header_row``` with the default 
value of ```1```

**Note**: The location of the header row is ```1``` base and not ```0``` base.

#### index_column_name

The index_column_name keeps the column name and column location of the column that has the 
index data. It has the following structure:
```
[
    {
    "column_name": "name of a column with type string (i.e first_name)", 
    "column_location": an integer greater than 0, 
    },
    ...    
]

```
**Note**: Although index_column_name can take multiple values currently only the first value will be
used as the index column. 

#### map_columns
In many cases user needs to compare two columns that do not have the same header name. To identify
these columns mapping can be used. Mapping allows user to define two columns to be compared with
each other.

The ```map_columns``` is a class variable in ```Compare``` class. It is an array of tuples
with the following structure:
```
[
    (
    {
    "column_name": "name of a column in first file", 
    "column_location": an integer greater than 0, 
    },
    {
    "column_name": "name of a column in second file", 
    "column_location": an integer greater than 0, 
    }
    ),
    ...    
]
```
The first value in the tuple will be a name and location of a column in the first file and the
second value of the tuple will be the name and location of a column in the second file.
These two columns will be compared with each other.


## Functions
```
check_for_negative_header_row(comparable)
```
The location of the header can not be be zero or negative. The function will simply check if the 
value of the ```header_row``` is greater than 0
```
check_for_header_row_location(comparable)
```
The row in which the header is located can not be 
greater than the number of the lines in the csv file. The function will count the number of lines
in the file and compare the result with the value of ```header_row```
```
set_original_header(comparable)
```
The function will go to the line in which the header is located. It will read the header line 
and will record the value and location of the column into the ```header``` instance variable.

```
set_header(comparable)
```
To prepare the column names to be imported into pandas we need to manipulate
the data. To keep the original data we make a copy of the ```original_header``` and keep it in 
```header``` with the ```set_header``` function

```
strip_header(comparable)
```
In many cases the column names in the csv file have extra white spaces (space, tab, newline)
in and around them. This can prevent the program from detecting identical column names in the files.
To avoid this problem we strip any white space in the column names.

**Note**: This will remove all the white spaces in the column name even if they are in the 
middle of the name.

TODO need to add auto detect the location of indices if the location is not given

```
check_for_index_column(comparable)
```
The function will verify the ```column_name``` and ```column_location``` of the given 
```index_column_names``` in the new generated ```header``` dictionary. 
To pass this function both the ```column_name``` and ```column_location``` of the 
```index_column_names``` must exist in ```header```

TODO need to add auto detect the location of mapped columns if the location is not given  

```
check_for_map_column(comparable)
```
To pass this function both the column_name and column_location of the 
mapped column must exist in the ```header```. Since the ```map_columns``` has list of tuples
the function needs to know which file we are trying to check. The function will use instance 
variable ```order``` to identify the file. The ```order``` variable for file one has value
```0``` and it will have value of ```1``` for file two. The function will get the correct
tuple value based on the ```order``` of the file. For example if the file is the first file
it will have ```order``` of ```0```. Therefore we know that the first value of the tuple must
be used.

```
format_map_column(comparable)
```
If the mapped columns have different names the function will format the names of the
columns to the following:
```
[column1]-[column2]
```
This will help the user to see which columns have been compared with each other if
the names are different. This format will be applied to all mapped columns in the
```header``` for both files.

```
format_unnamed_column(comparable)
```
Unnamed (empty) header names will be changed to ```@unnamed.n``` where ```n``` is the 
location of the original column in the file

```
format_duplicate_column(comparable)
```
Duplicate header names will be changed to ```header_name(@duplicate.n)``` where ```header_name```
is the original name of the header and ```n``` is the location of the header
in the original file

```
format_disjunctive_column(comparable)
```
Disjunctive headers are the one that are only in one file and not in the
other file. For columns to be compared with each other they have to either be mapped 
with each other or must have the same header. 
Disjunctive header names will be changed to ```header_name(@notFound.n)```
```
format_not_for_checked_column(comparable)
```
If user needs to compare the mapped columns only then the program will flag
any column that does not any unnamed, duplicate, or disjunctive flag as ```not_checked```
These columns will not be checked for differences
