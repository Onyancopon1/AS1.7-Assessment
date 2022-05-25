import random
quizzes ={}
quizzes={'question':'What is 1 in Maori?','choices':['Tahi','Rua','Ono'],'Answer':'Tahi'}
quizzes={'question':'What is 5 in Maori?','choices':['Toru','Rima','Whitu'],'Answer':'Rima'}
quizzes={'question': 'what is 9 in Maori?','choices':['Iwa','Ono','Whitu'],'Answer':'Iwa'}
quizzes={'question': 'what is 10 in Maori?','choices':['Tahi','Tekau','Wha'],'Answer':'Tekau'}

#Random
key,value=random.choice(list(quizzes.items()))
print(key,value['question'])
print('choice',end='')#
for i in range (len(value['choice'])):
    print(f"{i+1}.'{value['choice'][i]}'",end=")
          

print()

#answer
answer=int(input('Please enter the word from the list>'))

#answer check
if value['choice'][answer-1]==value['Correct']:
    print("CORRECT")
else:
    print(f"you are wrong.Answer was {value['CORRECT']}")
