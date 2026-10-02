import json
FILENAME = "students.json"
def load_students():
    try:
        with open(FILENAME,"r",encoding="utf-8")as file:
            return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def save_students(students):
    with open(FILENAME,"w",encoding="utf-8")as file:
        json.dump(students,file,ensure_ascii=False,indent=4)