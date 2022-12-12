from main2 import *

tasks = []
participant1 = Participant('RENATA', [AllOrNothing('Math', True, 10),
                                    AllOrNothing('Math', False, 15),
                                    AllOrNothing('English', True, 15),
                                    FasterIsBetter('Python', True, 15, 12, 5, 12, 4),
                                    FasterIsBetter('Algorithms', False, 5, 6, 10, 14, 5)], 0)


participant2 = Participant('POLINA', [AllOrNothing('Math', False, 15),
                                    AllOrNothing('Math', True, 10), # 10
                                    AllOrNothing('English', False, 15),
                                    FasterIsBetter('Python', True, 80, 12, 0, 10, 7), # 56
                                    FasterIsBetter('Algorithms', True, 20, 10, 0, 10, 5)], 0) # 18


participants = [participant2, participant1]

set_score_FasterIsBetter(participants)

ans_list = []
check_sum = 0

for i in participants:
    i.total_score()
    # print(i.name + ': ' + str(i.total))
    ans_list.append([i.total, i])
    check_sum += i.total

for i in sorted(ans_list):
    print(i[-1].name)

print(check_sum)