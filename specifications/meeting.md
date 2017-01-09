# MeetingClass

## Description
This class contains all the important informations about the meetings.

## Parent class
None

## Attributes

* ```meeting_time```
  * data type: float
  * description: Contains the starting time of the meeting.
* ```topics```
  * data type: list
  * description: A list about the meting topics.

## Class methods
None

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```Next_meeting```

Returns the time remaining to the next meeting.

#### Arguments
* ```meeting_time```
  * data type: float
  * description: Contains the starting time of the meeting.

#### Return value

```String```

### ```Topic_generator```

Return a single topic from the available list of topics.

#### Arguments
None

#### Return value
String