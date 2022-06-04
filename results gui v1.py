"""Results Gui V1
No Gui INcorporporated yet just performs the neccesary calculations to work out average, latest and best score
4/06/2022
By Caleb Giddy"""

# program to simulate working out scores for results
best_score = 0
rounds = 0
total_points = 0
for i in range(1,6):
    num = int(input(":"))
    score = str("{} out of 10".format(num))
    if num > best_score:
        best_score = num
    rounds += 1
    total_points += num
average_score = total_points/rounds
print("the average score is {} out of 10\n"
      "the best score is {} out of 10\n"
      "the latest score is {} out of 10\n".format(average_score,best_score,num))

