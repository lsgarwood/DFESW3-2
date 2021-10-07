class Students:

    def __init__(self, name, age, class_ = 'student'):
        self.name = name
        self.age = age
        self.class_ = class_

    def gettestscore(self, score1, score2, score3):
        return (score1 + score2 + score3) / 3

John = Students('John', 18)
Sally = Students('Sally', 19)
Bob = Students('Bob', 18)

avrg_score_John = John.gettestscore(45,38,43)
avrg_score_Sally = Sally.gettestscore(37,42,49)
avrg_score_Bob = Bob.gettestscore(48,49,32)

print(avrg_score_John)
print(avrg_score_Sally)
print(avrg_score_Bob)
