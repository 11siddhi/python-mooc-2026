# Write your solution here

def print_grade_distribution(distribution_list):
    length = len(distribution_list)
    max_grade = length
    print("Grade distribution:")
    for i in range(length):
        num = distribution_list[max_grade-1]
        pattern = "*"
        print(f"{max_grade-1}: {pattern*num}")
        max_grade -= 1


def main():
    grade_dist = [0, 0, 0, 0, 0, 0]   # initializing grade
    sum_of_pnts = 0
    total_students = 0

    while True:
        exam_input= input("Exam points and exercises completed: ")
        if not exam_input:
            break

        exam_pnts , ex_done = exam_input.split(" ")
        exam_pnts = int(exam_pnts)  
        ex_done = int(ex_done)
        total_students += 1
        
        ex_pnts = ex_done // 10
        total_pnts = exam_pnts + ex_pnts
        sum_of_pnts += total_pnts

        if exam_pnts < 10 or total_pnts <= 14:
            grade = 0
        elif total_pnts <= 17:
            grade = 1
        elif total_pnts <= 20:
            grade = 2
        elif total_pnts <= 23:
            grade = 3
        elif total_pnts <= 27:
            grade = 4
        else:
            grade = 5

        grade_dist[grade] += 1

    print("Statistics:") 
    average_pnts = sum_of_pnts / total_students
    print(f"Points average: {average_pnts:.1f}")

    pass_percent = (100/total_students) * (total_students - grade_dist[0])
    print(f"Pass percentage: {pass_percent:.1f}")

    print_grade_distribution(grade_dist)

main()

