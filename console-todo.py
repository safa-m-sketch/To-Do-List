### List of goals
goals=[]

### Function to add a goal
def addGoal():
  goal = input("Enter goal: ")
  goals.append(goal)
  print("Your task has been added to the list")

### Outputs the list of goals to accomplish for the day
def outputGoals():
  if len(goals) == 0:
    print("You have no goals")
  else:
    print("Goals for today")
    print("----------------------------------------")
    for i in range(len(goals)):
      print(str(i+1)+". "+goals[i])
    
### Function to mark a goal as done (in other words removes goal)
def markGoal():
  outputGoals()
  done_goal=int(input("Enter goal number to mark as done: "))
  if done_goal <= len(goals) and done_goal >= 1:
    goals.pop(done_goal-1)
    print("Goal marked as done")
  else:
    print("Invalid goal number")

if __name__ == "__main__":
  ### Create a loop to run the app
  print("Welcome to the To-Do List App")
  while True:
    print("\n")
    print("Choose an option")
    print("------------------------------------------")
    print("1. Add a goal")
    print("2. Mark a goal as completed")
    print("3. Goal overview")
    print("4. Exit")
    choice = input("Enter your choice: ")
    print("")
    if(choice == "1"):
      addGoal()
    elif(choice == "2"):
      markGoal()
    elif(choice == "3"):
      outputGoals()
    elif(choice == "4"):
      check=input("Are you sure you want to exit? Your progress will not be saved ")
      if check=="Yes" or check=="yes":
        break
    else:
      print("Error")
  print("Thank you for using the To-Do List App")