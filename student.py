def add_student(students):
    while True:
        name = input("이름을 입력해주세요: ").strip()
        for student in students:
            if name == student["name"]:
                print("이미 저장된 이름입니다.")
                return
        while True:
            try:
                score = int(input("점수를 입력해주세요: "))
                if score < 0 or score > 100:
                    print("0부터 100사이의 점수를 입력해주세요:")
                    continue
                student = {"name" : name , "score" : score}
                students.append(student)
                return
            except ValueError:
                print("잘못된 입력입니다.")

def show_student(students):
    if not students:
        print("저장된 학생이 없습니다.")
        return
    for index,student in enumerate(students,1):
        print(f"{index} . {student['name']} : {student['score']}")

def find_student(students):
    if not students:
        print("저장된 학생이 없습니다.")
        return
    name = input("검색할 이름을 입력해주세요: ").strip()
    found = False
    for student in students:
        if name in student['name']:
            score = student['score']
            print(f"{student['name']} : {score}점")
            found = True
    if not found:
        print("일치하는 이름이 없습니다.")

def average(students):
    scores = []
    if not students:
        print("저장된 학생이 없습니다.")
        return
    for student in students:
        score = student['score']
        scores.append(score)
    return print(f"학생들의 평균점수: {round(sum(scores) / len(scores),2)}")

def max_student(students):
    if not students:
        print("저장된 학생이 없습니다.")
        return
    max_student = students[0]
    for student in students:
        if max_student['score'] < student['score']:
            max_student = student
    print(f"최고점 학생 : {max_student['name']}  라는 학생이 {max_student['score']}점으로 최고 점수입니다.")

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def score_grade(students):
    if not students:
        print("저장된 학생이 없습니다.")
        return
    print("====== 점수 등급 ======")
    for index,student in enumerate(students,1):
        score = student['score']
        grade = get_grade(score) 
        print(f"{index}. {student['name']} : {student['score']}점 - {grade}")