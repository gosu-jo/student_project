from student import (
    add_student,
    show_student,
    find_student,
    average,
    max_student,
    score_grade
)
from storage import (
    load_students,
    save_students
)
def main():
    students = load_students()
    print("===== 학생 성적 관리=====")
    while True:
        print("1.학생등록")
        print("2.학생목록")
        print("3.학생검색")
        print("4.평균점수")
        print("5.최고점수학생")
        print("6.점수등급조회")
        print("7.종료")
        choice = input("메뉴번호를 입력해주세요: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_student(students)
        elif choice == "3":
            find_student(students)
        elif choice == "4":
            average(students)
        elif choice == "5":
            max_student(students)
        elif choice == "6":
            score_grade(students)
        elif choice == "7":
            print("프로그램을 종료합니다.")
            save_students(students)
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()