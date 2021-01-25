class Classwhat:
    def __init__(self, getquestions, getanswers):
        self.getquestions = getquestions
        self.getanswers = getanswers

Choicequestions = [
    '1. How many wheels does the car have?\na) 2Wheels\nb) 8Wheels\nc) 4Wheels\n',
    '2. What is the color of a crow?\na) Red\nb) Black\nc) Blue\n',
    '3. How many legs do cat have?\na) 4Legs\nb) 3Legs\nc) 6Legs\n'
]

questions = [
    Classwhat(Choicequestions[0], 'c'),
    Classwhat(Choicequestions[1], 'b'),
    Classwhat(Choicequestions[2], 'a'),
]
def main(questions):
    score = 0
    for okay in questions:
        answer = input(okay.getquestions)
        if answer == okay.getanswers:
            score += 1
    print('Your score is: ',len(Choicequestions), '/', score)
main(questions)