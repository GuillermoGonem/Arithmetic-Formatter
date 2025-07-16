def arithmetic_arranger(problems, show_answers=False):
    # Validaciones iniciales
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_row, bottom_row, lines, answers = [], [], [], []
    
    for problem in problems:
        # Dividir en componentes
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."
        
        num1, operator, num2 = parts
        
        # Validar operador
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validar que sean números y su longitud
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calcular ancho del problema
        width = max(len(num1), len(num2)) + 2  # +2 para el operador y un espacio
        top_row.append(num1.rjust(width))
        bottom_row.append(operator + num2.rjust(width - 1))
        lines.append('-' * width)
        
        # Calcular respuesta si es necesario
        if show_answers:
            answer = str(eval(problem))
            answers.append(answer.rjust(width))
    
    # Combinar las filas en la salida final
    arranged_problems = '\n'.join([
        '    '.join(top_row),
        '    '.join(bottom_row),
        '    '.join(lines)
    ])
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
# print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
# print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
# print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
# print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')