from peewee import *
from datetime import date
db = PostgresqlDatabase('flashcards', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class FlashCardModel(BaseModel):
    answer = CharField()
    question = CharField()
    answered_correctly = FloatField()
    answered_incorrectly =  FloatField()


class FlashCard:
    def __init__(self, question, answer, psql):
        self.answer = answer
        self.question = question
        self.answered_correctly: 0
        self.answered_incorrectly: 0

    def answered_right():
        self.answered_correctly += 1

    def answered_wrong():
        self.answered_incorrectly += 1


class FlashCardGame:
    def __init__(self):
        self.cards = []
        self.answered_correctly = []
        self.answered_incorrectly = []
        self.session_cards = []

    def create_card(self, question, answer):
        card = FlashCardModel(
            answer=answer,
            question=question,
            answered_correctly= 0,
            answered_incorrectly=0 )
        card.save()
        self.cards.append(card)

    def add_card(self, card):
        self.cards.append(card)

    def start_session(self, number_of_cards):
        self.session_cards = self.cards[0:number_of_cards]
        while len(self.session_cards) > 0:
            self.answer_question()
            print("Questions left to review: "+str(len(self.session_cards)))
        print(' \n \n \n------ Game Over ------- \n \n \n')
        cards = FlashCardModel.select()
        for card in cards:
             print(card.question,card.answered_correctly, card.answered_incorrectly)

    def answer_question(self):
        question = self.session_cards[0]
        attempt = input(question.question)
        if attempt == "!stop":
            print("Ending Game...")
            self.session_cards = []
        elif attempt == question.answer:

            self.session_cards[0].answered_correctly += 1
            self.session_cards[0].save()
            self.answered_correctly.append(self.session_cards.pop(0))


        elif attempt != question.answer:
            self.session_cards[0].answered_incorrectly +=1
            self.session_cards[0].save()
            self.session_cards.append(self.session_cards.pop(0))




game = FlashCardGame()
#FlashCardModel.delete().where(FlashCardModel.answer!='').execute()
cards = FlashCardModel.select()
if len(cards) == 0:
    db.create_tables([FlashCardModel])
    game.create_card("What color is the sky?: ","blue")
    game.create_card("What color are fire trucks?: ","red")
    game.create_card("What color are leaves in the summer?: ","green")
    game.create_card("What color is the sun?: ","orange")
    game.create_card("what is a girly color?: ","pink")
    game.create_card("what is a toxic masculine color?: ","yellow")
    game.create_card("Is Hiltler alive?: ","maybe")
else:
    for card in cards:
        game.add_card(card)




game.start_session(6)
