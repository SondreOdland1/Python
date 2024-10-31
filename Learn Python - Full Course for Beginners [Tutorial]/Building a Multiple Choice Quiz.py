from question import question

question_promts = [
    'What color are apples?\n(a) Red/green\n(b) purple\n(c) Orange\n\n',
    'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
    'What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n'
]


questions = [
    question(question_promts[0], 'a'),
    question(question_promts[1], 'c'),
    question(question_promts[2], 'b')
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print('You got ' + str(score) + '/' + str(len(questions)) + 'correct')


run_test(questions)



