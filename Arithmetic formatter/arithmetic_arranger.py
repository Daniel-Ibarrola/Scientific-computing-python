
def arithmetic_arranger(problems, display_answer=False):

    if not type(problems) is list:
        raise TypeError("Problems must be in a list")

    if len(problems) > 5:
        raise Exception('Error: Too many problems.')

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for problem in problems:
        numbers = problem.split()
        
        top_number = numbers[0]
        operator = numbers[1]
        bottom_number = numbers[2]

        if not top_number.isnumeric() or not bottom_number.isnumeric():
            raise Exception("Error: Numbers must only contain digits.")

        if operator != '+' and operator != '-':
            raise Exception("Error: Operator must be '+' or '-'.")

        if len(top_number) > 4 or len(bottom_number) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")

        #Set lenght of top, and bottom lines
        lenght = max(len(top_number), len(bottom_number)) + 2

        top = top_number.rjust(lenght)
        bottom = operator + bottom_number.rjust(lenght - 1)

        dashes = ('-' * (lenght)).rjust(lenght)
        
        #Add the correct number of dashes based on the largest number
        dashes = '-' * (lenght)

        first_line += top + '    '
        second_line += bottom + '    '
        third_line += dashes + '    '

        answer = str(int(top_number) + int(operator + bottom_number)).rjust(lenght)
        fourth_line += answer + '    '

    first_line = first_line.rstrip() 
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()

    if display_answer == True:
        arranged_problems = first_line + '\n' + second_line + '\n' + third_line + '\n'+ fourth_line
    else:
        arranged_problems = first_line + '\n' + second_line + '\n' + third_line

    # print(first_line)
    # print(second_line)
    # print(third_line)
    # print(fourth_line)

    return arranged_problems


# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print('\n')
# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))