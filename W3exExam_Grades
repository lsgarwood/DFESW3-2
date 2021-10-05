def score_total(home,assess,final):
    answer = round(((home + assess + final)/175)*100)
    return answer

name = str(input('Please enter your name:'))
home = int(input('Please enter your homework score:'))
while home > 25:
    print('Please enter a score between 0-25')
    home = int(input('Please enter your homework score:'))
assess = int(input('Please enter your assessment score:'))
while assess > 50:
    print('Please enter a score between 0-50')
    assess = int(input('Please enter your assessment score:'))
final = int(input('Please enter your Final exam score:'))

while final > 100:
    print('Please enter a score between 0-100')
    final = int(input('Please enter your Final exam score:'))

percentage = (score_total(home,assess,final))
print(f'{name} your final ICT score is {percentage}%')