goals = [55, 60]
start_min = 0
end_min = 90

goals_for = 0
goals_against = 0  


for goal in goals: 
    print(goal)
    if start_min < goal < end_min:
        goals_for = goals_for + 1
# for goal in goals:
#     if start_min < goal > end_min:
#         goals_against = goals_against + 1

print(goals_for)
