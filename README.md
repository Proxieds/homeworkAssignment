# Granify Homework Assignment

Run Instructions

- Git clone this repository and change directories to the folder.
- Can run the three files below using python or within any IDE terminal.
- python3 main.py
- python3 petShop.py
- python3 unitTests.py

## Project / File Structure
- Tried to keep everything within this local directory.
- Imported the required .py files whenever needed.
- Added comments wherever needed for functions and class definitions.

## Implementations
- Added getters/setters for most class attributes.
- If a cat/dog object was constructed with an initial name, it would be added to the previousNames collection on __init__.
- setName() will only set and add the new name to the collection of previous names if it is not None or empty character.
- Chose to use sets instead of list for tracking previous names as it handles duplicate names and didn't require manually check for membership like with a list.
- Decided to have the Dog class inherits attributes and methods from Cat class and only other change done was overriding default speak from "meow" to "woof" since they had fairly similar attributes and implementions otherwise.
- Keep tracked of every fifth speak of an animal by having an additional attribute and incrementing the age by one every time the total number of speaks was divisible evenly by 5, i.e: (% 5).
- GetAverageNameLength() is got the float length of all names within the previous names and divided by the count of previous names, the reason why I used float for getting the sum of letters since otherwise it would result in integer division and loss of precision.
- For testing the database for saving data, used transactions whenever possible, after successfully performing all inserts, commit the changes, else if the try statement resulted in an error, revert any changes by rolling back the database and return.
- For logStats(), I decided to print execution times of the other two methods.

## SQL Tasks
- Queries were written and tested in PostgreSQL
- Included some additional columns along with the base definition in with respect to part 2 of the assignment.

## Any Requirement disagreements or things I would do differently
- Was not sure if we had to make a .rb file for the petShop portion of the assignment or stick with the current translated files.
- Have cat and dog objects inherit from an Animal parent class, and store type of animal within an Animal table instead of a Cat/Dog table.
- I did not implement the cat/dog object like above as it would have changed the provided code too much.
- More clarification on the logStats() method.
- Otherwise I thought the requirements were good and to the point. 


