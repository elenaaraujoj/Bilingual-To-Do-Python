import os

# Nombre del archivo donde se guardarán tus metas
FILENAME = "my_goals.txt"

# Función para cargar tareas al iniciar
def load_goals():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Función para guardar tareas
def save_goals(goals_list):
    with open(FILENAME, "w") as file:
        for goal in goals_list:
            file.write(goal + "\n")

# Iniciar la lista con lo que haya en el archivo
goals = load_goals()

while True:
    print("\n--- TRACK YOUR PROGRESS (Level 2) ---")
    print("1. View my current objectives")
    print("2. Add a new step to success")
    print("3. Delete a goal (Achieved!)") # ¡Nueva opción!
    print("4. Close and start working")
    
    option = input("Choose an option (1-4): ")

    if option == "1":
        if not goals:
            print("Your list is empty. Start your journey!")
        else:
            print("\nYour current objectives:")
            for i, goal in enumerate(goals, 1):
                print(f"{i}. {goal}")
    
    elif option == "2":
        new_goal = input("Write your new goal: ")
        goals.append(new_goal)
        save_goals(goals) # Guardamos en el archivo .txt
        print("Step added and saved to disk!")
    
    elif option == "3":
        if not goals:
            print("Nothing to delete.")
        else:
            try:
                num = int(input("Enter the number of the goal achieved: "))
                removed = goals.pop(num - 1)
                save_goals(goals) # Actualizamos el archivo
                print(f"Great job! '{removed}' has been achieved.")
            except:
                print("Invalid number.")
    
    elif option == "4":
        print("Closing... Your goals are safe in 'my_goals.txt'.")
        break
    else:
        print("Invalid option.")