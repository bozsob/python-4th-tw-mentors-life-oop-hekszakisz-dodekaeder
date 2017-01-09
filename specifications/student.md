# Student

## Description
This class represents a student in real life.

## Parent class
Person

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the knowledge level of the student in programming
* ```energy_level```
  * data type: integer
  * description: current energy level

## Instance method

### ```__init__```
The constructor of the object.

#### Arguments
The constructor should call the parent class's constructor

### Return value
ValueError if the attributes are empty

### ```create_by_csv```
Gives back a list of students.

### Arguments
Gets a csv file path as an argument (the csv contains all the data needed to instantiate a student object).

### Return value
List of students
