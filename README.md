# Python Flashcard Game with SQL Backend

This project is a command line based flashcard game

### Prerequisites
The following librarys/langagues/databases are required to properly setup software

`Python`, `pip`, `PostgreSQL`, `peewee`


### Installing

In order to run the project, execute the following steps:

**clone repo**

> git clone https://github.com/clarknoah/ga-python-cmd.git

**Enter Root Project Directory**

> cd ga-python-cmd

**Install Dependencies**

> pip install peewee

**Run Project**

> python flash.py

```
python flash.py
Is Hiltler alive?: maybe
Questions left to review: 5
What color is the sky?:
```


## Getting Started

The following code describes how to use the FlashCardGame class

```python
#Start Flashcard Game

game = FlashCardGame()

#Create new FlashCard

game.create_card(question, answer)

#Start Flash Card Game

game.start_session(numberOfCardsToPractice)

```
