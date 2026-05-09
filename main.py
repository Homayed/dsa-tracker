from tracker import add_problem, view_all_problems

def menu():
    while True:
        print("\n===============================")
        print("           DSA TRACKER")
        print("===============================")
        print("1.Add Problem")
        print("2.View All Problems")
        print("3.Exit")

        choice = input("\n Enter choice: 1/2/3")
        if choice == '1':
            add_problem()
            break
        if choice == '2':
            view_all_problems()
            break
        if choice == '3':
            print("Thanks, Keep Grinding")
            break
        else:
            print("\n Invalid choice. Try again")


if __name__ == "__main__":
    menu()


