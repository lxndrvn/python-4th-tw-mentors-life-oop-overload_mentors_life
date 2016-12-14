# Mentor

## Description
This class contains the data of the mentors.

## Parent class
Person

## Attribute 
soft_skill

soft_skill = [0]  - [20] low.level print('')  
soft_skill = [21] - [80]  mid.level print('')  
soft_skill = [81] - [100] max.level print('')
    
## Class method
create_by_csv

It reads the mentor's data from the csv file.

### Argument
file_name

### Return value
list which contains the mentor objects

## Instance methods

### ```__init__``
The constructor of the object.

### Arguments
All of the arguments of the class itself.

### Return value
None

### ```soft_skill_level_changer```

### Arguments
    data type: integer
    
### Return value
The new soft skill level. 


### ```teach```
Increase the knowledge level of the students.
Changes the project's grade.

### ```grade_project```

### Arguments
project
grade

### Return value