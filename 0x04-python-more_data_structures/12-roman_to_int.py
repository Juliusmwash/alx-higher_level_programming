#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    str = "IVXLCDM"
    indx1 = 0
    indx2 = 0
    sum = 0
    count = len(roman_string) - 1
    if count == 0:
        return 0
    while count >= 0:
        if roman_string[count] in roman_dict:
            indx1 = str.index(roman_string[count])
            if count != 0:
                if roman_string[count - 1] in roman_dict:
                    indx2 = str.index(roman_string[count - 1])
                else:
                    return 0
                if indx1 <= indx2:
                    sum += roman_dict.get(roman_string[count])
                    #print("sum = {:d}".format(sum))
                else:
                    tmp = roman_dict.get(roman_string[count])
                    tmp2 = roman_dict.get(roman_string[count - 1])
                    sum += (tmp - tmp2)
                    count -= 1
                    #print("sum = {:d}".format(sum))
            else:
                sum += roman_dict.get(roman_string[count])
                #print("sum = {:d}".format(sum))
        else:
            print("not found")
            return 0;
        count -= 1
    return sum
"""
print(roman_to_int("CCCLXXIII"))
print(roman_to_int("DCCXXXIII"))
print(roman_to_int("MMDCCCLXII"))
print(roman_to_int("MDCCLXIV"))
print(roman_to_int("DCCCLXII"))
"""
print(roman_to_int("CMJXXXVI"))
"""
print("000 = CCCLXXIII, 733 = DCCXXXIII, 2862 = MMDCCCLXII, 1764 = MDCCLXIV, 862 = DCCCLXII, 936 = CMXXXVI")
"""
