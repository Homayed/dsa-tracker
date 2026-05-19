from utils import load_data,save_data
from datetime import datetime

def add_problem():
    data = load_data() #read data
    problem = input("Problem name: ")
    topic = input("Topic(Arrays/Graph/DP/Trees): ")
    difficulty = input("difficulty(Easy/Medium/hard): ")
    time_taken = int(input("Time Taken(minutes): "))
    solved_alone = input("Solved alone?(Yes/No): ")
    pattern = input("Whats the Pattern?")
    time_complexity = input("Whats the time complexity of the problem")
    space_complexity = input("whats the space complexity of the problem")
    note_file = input("Note file path: ")

#dict
    entry = {
        "date": str(datetime.now().date()),
        "problem": problem,
        "topic": topic,
        "difficulty": difficulty,
        "time_taken": time_taken,
        "solved_alone": solved_alone,
        "pattern": pattern,
        "time_complexity": time_complexity,
        "space_complexity": space_complexity,
        "note_file": note_file

    }
    data.append(entry)#add new entry

    save_data(data) #write in JSON
    print("\nProblem added successfully.\n")

def view_all_problems():
    data = load_data()
    if not data:
        print("\n No problems found.\n")
        return
    print("\n DSA Practice Log:\n")
    for i, item in enumerate(data,1): #loop through index and value where index starts from 1
        print(f"{i}.{item['date']}| {item['problem']} | {item['topic']} | {item['difficulty']} | {item['time_taken']} | {item['solved_alone']} | {item.get('pattern', 'Not added yet')} | {item.get('time_complexity', 'Not added yet')}| {item.get('space_complexity', 'Not added yet')} | {item.get('note_file', 'Not added yet')}")




def delete_problem():
    data = load_data()
    sequence_to_del = int(input("Give me the number of the problem set you want to delete?"))
    if sequence_to_del:
        deleted_item = data.pop(sequence_to_del-1)
        print(f"{deleted_item} is deleted")
        save_data(data)

def search_problem():
    data = load_data()
    searching = input("Which problem u want to search?")
    if not data:
        print("\n No problems found.\n")
        return
    found = False


    for item in data:
        if "problem" in item:
            if item["problem"].lower().strip() == searching.lower().strip():
                print(item)
                found = True

    if found == False:
        print("\nNo problem named this is found while searching\n")

def show_stats():
    data = load_data()

    total = len(data)
    easy = 0
    medium = 0
    hard = 0

    for item in data:
        difficulty = item.get("difficulty", "").lower().strip()

        if difficulty == "easy":
            easy += 1
        elif difficulty == "medium":
            medium += 1
        elif difficulty == "hard":
            hard += 1

    print("\n===== DSA Tracker Stats =====")
    print("Total Solved:", total)
    print("Easy:", easy)
    print("Medium:", medium)
    print("Hard:", hard)
    print("=============================\n")











