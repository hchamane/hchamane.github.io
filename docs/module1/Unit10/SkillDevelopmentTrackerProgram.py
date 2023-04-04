#Skill Development Tracker Program
skill_list = {}  #Skill List to store skills and all related data.

#Function to add a new skills
def add_skill():
    """Add a new skill and its data to the Skill List"""
    print("\nAdd a new skill:")
    skill_name = input("Enter skill name: ")
    experience = input("Enter level of experience: ")
    achievement = input("Enter achievement status: ")
    skill_list[skill_name] = {"experience": experience, "achievement": achievement}

#Function to delete skills
def delete_skill():
    """Delete a skill and its data from the Skill List"""
    print("\nDelete a skill:")
    skill_name = input("Enter skill name: ")
    if skill_name in skill_list:
        del skill_list[skill_name]
        print(f"{skill_name} and all data have been deleted.")
    else:
        print(f"{skill_name} not found in the Skill List.")

#Function to search skills
def search_skill():
    """Search for a skill in the Skill List"""
    print("\nSearch for a skill:")
    skill_name = input("Enter skill name: ")
    if skill_name in skill_list:
        print(f"{skill_name} is in the Skill List with the following data: {skill_list[skill_name]}")
    else:
        print(f"{skill_name} not found in the Skill List.")

#Function to sort skills
def sort_skills():
    """Sort the skills in the Skill List by name"""
    sorted_skills = sorted(skill_list.items())
    print("\nSorted skills:")
    for skill in sorted_skills:
        print(f"Skill: {skill[0]}, experience: {skill[1]['experience']}, achievement: {skill[1]['achievement']}")


#Main program loop
while True:
    print("\nSelect an option:")
    print("1. Add a skill")
    print("2. Delete a skill")
    print("3. Search for a skill")
    print("4. Sort skills by name")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_skill()
    elif choice == "2":
        delete_skill()
    elif choice == "3":
        search_skill()
    elif choice == "4":
        sort_skills()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice, please enter a number from 1 to 5.")