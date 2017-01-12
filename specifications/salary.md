## Description
This class contains information about the salary of the mentors.

## Parent class
None

## Attributes

* ```payday```
  * data type: integer
  * description: Contains the numeric date of the payday(day).


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself.

#### Return value
ValueError if the argument is greater than 31 or less than 1.

### ```days_until_payday```
Gives back the remaining days until the next payday

#### Arguments
None

#### Return value
Print out message showing the pay date and the days left until the pay date.

### ```warning_messages```
Gives back a warning message based on the days left until the next pay day.

#### Arguments
None

#### Return value
Print out message.
