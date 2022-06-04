"""Results Gui V2
No Gui INcorporporated yet just performs the neccesary calculations to work out average, latest and best score
using a function and list instead of independant variables
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



def get_results(latest,rounds,best, total):
    if rounds != 0:
        average = total/rounds
    else:
        average = 0
    results_list = [latest,average,best]
    return results_list

results_list = get_results(num,rounds,best_score,total_points)

print("the average score is {} out of 10\n"
      "the best score is {} out of 10\n"
      "the latest score is {} out of 10\n".format(results_list[1],results_list[2],results_list[0]))

