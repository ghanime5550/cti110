def main():
    total = 0;avg = 0;abc_grade = 0
def calc_average(total):
    return total / 5

def determine_grade(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'

while(True):
    grade = int(input('Enter grade: '))
    total += grade
    avg = calc_average(total)
    abc_grade = determine_grade(grade)

    print('Average grade is: ' + str(avg))
    print('Letter grades for entered grades are: ' + str(abc_grade))

