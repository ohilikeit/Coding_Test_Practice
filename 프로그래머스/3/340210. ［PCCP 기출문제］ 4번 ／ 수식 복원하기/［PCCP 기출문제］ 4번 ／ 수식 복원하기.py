def solution(expressions):
    def is_valid_number(num_str, base):
        for ch in num_str:
            digit = int(ch)
            if digit >= base:
                return False
        return True

    def str_to_int(num_str, base):
        return int(num_str, base)

    def int_to_str(num_int, base):
        if num_int == 0:
            return '0'
        digits = []
        while num_int > 0:
            digits.append(str(num_int % base))
            num_int //= base
        return ''.join(reversed(digits))

    known_expressions = []
    unknown_expressions = []
    digits_in_numbers = set()
    for expr in expressions:
        A_str, op, B_str, eq, C_str = expr.split()
        # Collect digits
        for ch in A_str + B_str + (C_str if C_str != 'X' else ''):
            digits_in_numbers.add(int(ch))
        if C_str == 'X':
            unknown_expressions.append((A_str, op, B_str, eq, C_str))
        else:
            known_expressions.append((A_str, op, B_str, eq, C_str))

    max_digit = max(digits_in_numbers)
    possible_bases = []
    for base in range(max(max_digit + 1, 2), 10):
        valid = True
        for A_str, op, B_str, eq, C_str in known_expressions:
            # Check if all digits are valid in this base
            if not (is_valid_number(A_str, base) and is_valid_number(B_str, base) and is_valid_number(C_str, base)):
                valid = False
                break
            try:
                A = int(A_str, base)
                B = int(B_str, base)
                C = int(C_str, base)
            except ValueError:
                valid = False
                break

            if op == '+':
                result = A + B
            elif op == '-':
                result = A - B
            else:
                valid = False
                break
            if result < 0:
                valid = False
                break
            if result != C:
                valid = False
                break
        if valid:
            possible_bases.append(base)

    result_expressions = []
    for A_str, op, B_str, eq, C_str in unknown_expressions:
        possible_results = set()
        for base in possible_bases:
            if not (is_valid_number(A_str, base) and is_valid_number(B_str, base)):
                continue
            try:
                A = int(A_str, base)
                B = int(B_str, base)
            except ValueError:
                continue
            if op == '+':
                result = A + B
            elif op == '-':
                result = A - B
            else:
                continue
            if result < 0:
                continue
            result_str = int_to_str(result, base)
            # Check if result_str is valid in this base
            if is_valid_number(result_str, base):
                possible_results.add(result_str)
        if len(possible_results) == 1:
            result_value = possible_results.pop()
            filled_expr = f"{A_str} {op} {B_str} = {result_value}"
        else:
            filled_expr = f"{A_str} {op} {B_str} = ?"
        result_expressions.append(filled_expr)
    return result_expressions
