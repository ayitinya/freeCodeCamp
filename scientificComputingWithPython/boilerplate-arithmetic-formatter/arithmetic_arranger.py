
def arithmetic_arranger(problems, result=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        first_line = True
        line_1 = line_2 = line_3 = line_4 = ''
        for problem in problems:
            problem = problem.split()
            if len(problem) > 3:
                return 'Operands greater than 2'
            else:
                if problem[0].isdigit() and problem[2].isdigit():
                    if len(problem[0]) > 4 or len(problem[2]) > 4:
                        return 'Error: Numbers cannot be more than four digits.'
                    else:
                        num_1 = problem[0]
                        num_2 = problem[2]
                        operation = problem[1]

                        if operation == '+' or operation == '-':
                            pass
                        else:
                            return "Error: Operator must be '+' or '-'."

                        length = max(len(num_1), len(num_2)) + 2

                        if first_line:
                            line_1 += num_1.rjust(length)
                            line_2 += operation + num_2.rjust(length - 1)
                            line_3 += '-' * length
                            if result:
                                if operation == '+':
                                    result = int(num_1) + int(num_2)
                                    line_4 += str(result).rjust(length)
                                else:
                                    result = int(num_1) - int(num_2)
                                    line_4 += str(result).rjust(length)

                            first_line = False

                        else:
                            line_1 += num_1.rjust(length + 4)
                            line_2 += ' ' + operation.rjust(4) + num_2.rjust(length - 1)
                            line_3 += ' ' * 4 + '-' * length
                            if result:
                                if operation == '+':
                                    result = int(num_1) + int(num_2)
                                    line_4 += str(result).rjust(length + 4)
                                else:
                                    result = int(num_1) - int(num_2)
                                    line_4 += str(result).rjust(length + 4)

                else:
                    return 'Error: Numbers must only contain digits.'
    if result:

        return line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4
    else:
        return line_1 + '\n' + line_2 + '\n' + line_3


if __name__ == '__main__':

    print(arithmetic_arranger(['4895 - 54', '43 - 5645', '4 + 5'], result=True))
