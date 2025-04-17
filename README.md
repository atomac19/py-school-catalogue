# School Catalogue project
Putting my knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education
## Description
The Department of Education wants the catalog to hold quick reference material for each school in the city.
I need to create classes for primary, middle and high schools. 
### Features
These classes share properties and methods, each will inherit from a parent School class. My parent and three child classes have the following properties, getters, setters, and methods:
1. School

    -Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
    -Getters: all properties have getters
    -Setters: the numberOfStudents property has a setter
    -Methods: A __repr__ method that displays information about the school.

2. Primary

    -Includes everything in the School class, plus one additional property
    -Properties: pickupPolicy (string, like "Pickup after 3pm")

3. Middle

    -Does not include any additional properties or methods

4. High

    -Includes everything in the School class, plus one additional property
    -Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

### Tehnologies
Python

### Collaborators
www.codecademy.com
