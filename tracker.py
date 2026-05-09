from utils import load_data,save_data
from datetime import datetime

def add_problem():
    data = load_data() #read data
    problem = input("Problem name: ")
    topic = input("Topic(Arrays/Graph/DP/Trees): ")
    difficulty = input("difficulty(Easy/Medium/hard): ")
    time_taken = int(input("Time Taken(minutes): "))
    solved_alone = input("Solved alone?(Yes/No): ")
#dict
    entry = {
        "date": str(datetime.now().date()),
        "problem": problem,
        "topic": topic,
        "difficulty": difficulty,
        "time_taken": time_taken,
        "solved_alone": solved_alone
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
        print(f"{i}.{item['date']}| {item['problem']} | {item['topic']} | {item['difficulty']} | {item['time_taken']} | {item['solved_alone']}")
