# MentorClass

## Description
This class represents a Mentor in real life.

## Parent class
Person

## Attributes

* ```Attributes from the Parent class: first_name, last_name, year_of_birth, gender```
* ```nickname```
  * data type: string
  * description: stores the mentor's secret nickname between the students

## Instance methods

### ```___init__```
The constructor of the object.

#### Attributes
ALL of the arguments of the Person class (Parent class) itself and the nickname.
Should raise an error, if empty.

#### Return value
None

### ```create_by_csv```

Gives back a list of mentors from a csv file.
#### Attributes
* ```a csv file path```
  * data type: csv file
  * description: the csv contains all the data needed to instantiate a mentor object

#### Return value
```Mentors``` list 