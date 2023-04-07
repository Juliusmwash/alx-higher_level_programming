#!/usr/bin/python3
""" Defines the function ''matrix_mul''
This function multiplies two matrixes
"""


def matrix_mul(m_a, m_b):
    """ Function for multiplying two matrixes """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    for lst in m_a:
        if not isinstance(lst, list):
            raise TypeError('m_a must be a list of lists')
    for lst in m_b:
        if not isinstance(lst, list):
            raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    num = 0
    for i in range(0, 2):
        check = 0
        if i == 0:
            lsts = m_a
        else:
            lsts = m_b
        for lst in lsts:
            if check == 0:
                num = len(lst)
                check = 1
            if len(lst) != num:
                if i == 0:
                    raise TypeError('each row of m_a must be of the same size')
                else:
                    raise TypeError('each row of m_b must be of the same size')
            for item in lst:
                if type(item) != int and type(item) != float:
                    if i == 0:
                        raise TypeError('m_a \
should contain only integers or floats')
                    else:
                        raise TypeError('m_b \
should contain only integers or floats')
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    """
    main_result = []
    result = 0
    count = 0
    for lst in m_a:
        a = []
        for j in range(0, len(lst)):
            for i in range(0, len(lst)):
                result += lst[i] * m_b[i][count]
            a.append(result)
            count += 1
            result = 0
        main_result.append(a)
    return main_result"""
    rows_A = len(m_a)
    cols_A = len(m_a[0])
    rows_B = len(m_b)
    cols_B = len(m_b[0])
    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += m_a[i][k] * m_b[k][j]

    return C
