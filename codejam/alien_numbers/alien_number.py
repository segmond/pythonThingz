#!/usr/bin/python

def translate_aux(input):
    i = input.split()
    return translate(i[0], i[1], i[2])

def translate(num, source_lang, target_lang):
    #print "converting %s from source %s to target %s ", (num, source_lang, target_lang)
    return translate_from_base10(translate_to_base10(num, source_lang), target_lang)

def translate_to_base10(num, source_lang):
    source_lang_base = len(source_lang)

    sb = source_lang_base 
    sp = len(num) - 1
    src_num = 0
    for alien_digit in num:
        digit = source_lang.index(alien_digit)
        src_num = src_num + ((sb**sp)*digit)
        sp = sp - 1
    return src_num

def get_largest_exp(target_lang_base, num):
    exp = 0
    while (target_lang_base ** exp) <= num:
        exp = exp + 1
    return exp-1

def translate_from_base10(num, target_lang):
    target_lang_base = len(target_lang)

    exp = get_largest_exp(target_lang_base, num)
    alien_digits = ""
    while exp >= 0:
        alien_digit = num / (target_lang_base ** exp)
        alien_digits = alien_digits + target_lang[alien_digit]
        num = num % (target_lang_base ** exp)
        exp = exp-1

    return alien_digits


def read_data_file(input_file):
    f = open(input_file)
    n_inputs = int(f.readline().strip())
    #print "number of lines is ", n_inputs
    case_num = 1
    while n_inputs > 0:
        line = f.readline().strip()
        #print line
        print "Case #%d:" % case_num,
        print translate_aux(line)
        n_inputs = n_inputs - 1
        case_num = case_num + 1

read_data_file("input.txt")

"""
print translate("209", "0123456789", "01234567")
print translate("9", "0123456789", "oF8")
print translate("dcb", "abcdefgh", "01")
print translate("321", "01234567", "01")
print translate("13", "0123456789abcdef", "01")
print translate("CODE", "O!CDE?", "A?JM!.")
print translate("32", "0123456789", "01")
"""
