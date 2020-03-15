# 목적 :
#       국어, 수학, 영어, 과학 과목을 듣는 학생들의 총점과 평균을
#       구하는 성적 관리 프로그램 절차 지향 방식을 사용하여 만들어 보자.
#
# 테스트 데이터
#       {'이름': '윤인성', '국어': 87, '수학': 98, '영어': 88, '과학': 95},
#       {'이름': '연하진', '국어': 92, '수학': 98, '영어': 96, '과학': 98},
#       {'이름': '구지연', '국어': 76, '수학': 96, '영어': 94, '과학': 90},
#       {'이름': '나선주', '국어': 98, '수학': 92, '영어': 96, '과학': 92},
#       {'이름': '윤아린', '국어': 95, '수학': 98, '영어': 98, '과학': 98},
#       {'이름': '윤명월', '국어': 64, '수학': 88, '영어': 92, '과학': 92},
#       {'이름': '김미화', '국어': 82, '수학': 86, '영어': 98, '과학': 88},
#       {'이름': '김연화', '국어': 88, '수학': 74, '영어': 78, '과학': 92},
#       {'이름': '박아현', '국어': 97, '수학': 92, '영어': 88, '과학': 95},
#       {'이름': '서준서', '국어': 45, '수학': 52, '영어': 72, '과학': 78},
#
# 출력 결과 예시
#       이름    총점    평균
#       윤인성  368     92.0
#       연하진  384     96.0
#       구지연  356     89.0
#       나선주  378     94.5
#       윤아린  389     97.25
#       윤명월  336     84.0
#       김미화  354     88.5
#       김연화  332     83.0
#       박아현  372     93.0
#       서준서  247     61.75


# 작업 순서
# 딕셔너리를 리턴하는 함수를 선언합니다.create_student(이름, 국어,수학,영어,과학)
# 학생을 처리하는 함수를 선언합니다. student_get_sum(student)
# 학생 리스트를을 선언합니다.student_get_average(student)
# 학생을 한 명씩 반복합니다.student_to_string(student)
# main() 함수를 정의한다.
# 1. 학생 리스트를 선언합니다.
# 2. 학생을 한 명씩 반복하면서 이름, 합계, 평균을 출력한다.
# main() 함수 호출

# 코딩 하기

def create_student(이름, 국어성적, 수학성적, 영어성적, 과학성적):
    return {"이름": 이름,
            "국어": 국어성적,
            "수학": 수학성적,
            "영어": 영어성적,
            "과학": 과학성적}


def student_get_sum(student):
    val = student["국어"] + student["수학"] + student["영어"] + student["과학"]
    return val


def student_get_average(student):
    val = student_get_sum(student)
    arg = val/4
    return arg


def student_to_string(student):
    sum = student_get_sum(student)
    arg = student_get_average(student)
    str = "이름: %s, 국어: %s, 수학: %s, 영어: %s, 과학: %s, 총점: %s, 평균: %s" % (
        student["이름"], student["국어"], student["수학"], student["영어"], student["과학"], sum, arg)
    return str


def main():
    students = [
        create_student('윤인성',  87,  98,  88, 95),
        create_student('연하진',  92,  98,  96,  98),
        create_student('구지연',  76,  96,  94,  90),
        create_student('나선주',  98,  92,  96,  92),
        create_student('윤아린',  95,  98,  98,  98),
        create_student('윤명월',  64,  88,  92,  92),
        create_student('김미화',  82,  86,  98,  88),
        create_student('김연화',  88,  74,  78,  92),
        create_student('박아현',  97,  92,  88,  95),
        create_student('서준서',  45,  52,  72,  78)
    ]

    for student in students:
        str = student_to_string(student)
        print(str)


if __name__ == "__main__":
    main()
