# CSV Comparison Package
#### Developed by Saba Janamian
**Last README update: 5/8/2018**
**Current release 1.1**

**See the following for an example:**
*The followings can be executed in a linux/Mac terminal*

1. First create a folder for the project
```shell
  mkdir my_proj
```
2. Go to the project folder
```shell
  cd my_proj
```
3. Create a python virtual environment
```shell
  python3 -m venv dev-python-env
  ```
4. Activate the virtual environment
```shell
  source ./dev-python-env/bin/activate
```
5. (optional) upgrade the pip to the latest version
```shell
  pip install --upgrade pip
```
6. Install Jupyter notebook
```shell
  pip install jupyter
```
7. Clone the csv comparison package into the project folder
```shell
  git clone https://github.com/saba-ja/csv_comparison_package.git
```
8. Go to the csv_comparison_package folder
```shell
  cd csv_comparison_package
```
9. Install the csv_comparison_package into the virtual environment
```shell
  pip install .
```
10. (optional) You can remove the original folder since it is not needed any more
```shell
  sudo rm -R csv_comparison_package/
```
11. Run jupyter notebook
```shell
 jupyter notebook
```

-----------------
-----------------
### To use the package include it in your project by using the following:
 ```python
 from csv_comparison_package import csv_compare_module as cc
```

### The parameters for setup are as the following:

```python
 parameters = {
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~ FILE SETUP ~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    "file_1_name"                     :"/PATH/TO/FIRST/FILE",
    "file_2_name"                     :"/PATH/TO/SECOND/FILE",

    "file_1_index_column_name"        : [{"column_name":"<a colum name form file 1>",}],
    "file_2_index_column_name"        : [{"column_name":"a colum name form file 2"}],

    "file_1_2_map_columns":[(
        {"column_name": "<index column in file 1>"},
        {"column_name": "<index column in file 2>"},
        )],

    "file_1_2_compare_only_mapped_columns"     : True,
    "file_1_header_row"                  : 1,
    "file_2_header_row"                  : 1,
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~ HIDE AND SHOW SETUP ~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    "file_1_hide_modified_columns"       : False,
    "file_2_hide_modified_columns"       : False,

    "file_1_hide_not_checked_columns"    : True,
    "file_2_hide_not_checked_columns"    : True,

    "file_1_hide_disjunctive_columns"    : True,
    "file_2_hide_disjunctive_columns"    : True,

    "file_1_hide_duplicate_columns"      : True,
    "file_2_hide_duplicate_columns"      : True,

    "file_1_hide_unnamed_columns"        : True,
    "file_2_hide_unnamed_columns"        : True,

    "file_1_2_hide_not_modified_rows"    : True,

    "file_1_2_output_path" : './'


}
```

### Use the following function call to run the script
```python
cc.export_to_excel(parameters)
```

-----------------
-----------------

**See the following for an example:**

*The jupyter notebook file and two dummy CSV files are available in the example folder*

```python
from csv_comparison_package import csv_compare_module as cc
```

```python
parameters = {
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~ FILE SETUP ~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    "file_1_name"                     :"./sheet_1.csv",
    "file_2_name"                     :"./sheet_2.csv",

    "file_1_index_column_name"        : [{"column_name":"Social Security ID"}],
    "file_2_index_column_name"        : [{"column_name":"Social Security ID"}],

    "file_1_2_map_columns":[({"column_name":"First Name"},{"column_name":"First Name"})],

    "file_1_2_compare_only_mapped_columns"     : True,
    "file_1_header_row"                  : 1,
    "file_2_header_row"                  : 1,
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~ HIDE AND SHOW SETUP ~~~~~~~~~~~~~~~
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    "file_1_hide_modified_columns"       : False,
    "file_2_hide_modified_columns"       : False,

    "file_1_hide_not_checked_columns"    : True,
    "file_2_hide_not_checked_columns"    : True,

    "file_1_hide_disjunctive_columns"    : True,
    "file_2_hide_disjunctive_columns"    : True,

    "file_1_hide_duplicate_columns"      : True,
    "file_2_hide_duplicate_columns"      : True,

    "file_1_hide_unnamed_columns"        : True,
    "file_2_hide_unnamed_columns"        : True,

    "file_1_2_hide_not_modified_rows"    : True,

    "file_1_2_output_path" : './'

}

```

```python
cc.export_to_excel(parameters)
```
## parameters description:
- ```file_1_name```: Full address to the first CSV file.
- ```file_2_name```: Full address to the seond CSV file.
Note:
If the file is in the same folder jupyter notebook ./ can be used

- ```file_1_index_column_name```: name of the column holding the primary key for the first CSV file. It should be in the following format ```[{"column_name":"a column name form file 1",}]```
- ```file_2_index_column_name```: name of the column holding the primary key for the second CSV file.

- ```file_1_2_map_columns```: map the columns that need to be compared with each other. It should be in the following format ```[({"column_name":"a column in the first file"},{"column_name":"a column in the second file"})]```,
- ```file_1_2_compare_only_mapped_columns```: If the value is True it will only compare the mapped columns
