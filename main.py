from tracker import add_problem, view_all_problems, delete_problem, search_problem


def menu():
    while True:
        print("\n===============================")
        print("           DSA TRACKER")
        print("===============================")
        print("1.Add Problem")
        print("2.View All Problems")
        print("3.Delete Problem")
        print("4.Search Problem")
        print("5.Exit")

        choice = input("\n Enter choice: 1/2/3/4/5")
        if choice == '1':
            add_problem()
            break
        if choice == '2':
            view_all_problems()
            break
        if choice == '3':
            delete_problem()
            break
        if choice == '4':
            search_problem()
            break
        else:
            print("\n Invalid choice. Try again")


if __name__ == "__main__": #built in
    menu()


