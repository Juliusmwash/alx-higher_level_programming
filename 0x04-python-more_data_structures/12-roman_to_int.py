#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6,
                  "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XI": 11, "XII": 12, "XIII": 13,
                  "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20, "XXI": 21,
                  "XXII": 22, "XXIII": 23, "XXIV": 24, "XXX": 30, "XL": 40, "L": 50, "LX": 60,
                  "LXX": 70, "LXXX": 80, "XC": 90, "C": 100, "CI": 101, "CII": 102, "CC": 200,
                  "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
                  "M": 1000, "MI": 1001, "MII": 1002, "MIII": 1003, "MCM": 1900, "MM": 2000,
                  "MMI": 2001, "MMII": 2002, "MMC": 2100, "MMM": 3000, "MMMM": 4000, "V": 5000}
    for i in roman_dict:
        if i == roman_string:
            return roman_dict.get(i)
    return 0
