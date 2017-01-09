# Kitchen

## Description
The Kitchen is a class that represents the hub of knowledge, food source, coffee source and gossips source for the students.

## Parent class
None

## Attributes

* ```coffee_amount```
  * data type: integer
  * description: represents the amount of coffee available for the students
* ```fridge_space```
  * data type: integer
  * description: represents the volume of free space in the refridgerator

## Instance method

### ```__init__```
The constructor of the object.

#### Arguments
All of the arguments of the class itself.

### Return value
ValueError if attributes are empty.

### ```pakkos_phrases```
Random selected funny phrases from Pakko's brain storming periods in the kitchen.

### Arguments
None

### Return value
A random selected phrase from a pre-loaded list of phrases.

### ```coffee_amount_left```
Calculates the amount of coffee left after the consumed amount of coffee

### Arguments
* ```consumed_amount```
  * data type: integer

### Return value
An integer, representing the amount of coffe left in the kitchen.
ValueError, if the coffe ran out in the kitchen

### ```fridge_space_left```
Calculates the free space in the fridge_space

### Arguments
* ```food_amount```
  * data type: integer