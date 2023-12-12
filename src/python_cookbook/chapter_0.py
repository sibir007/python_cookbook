str_plasholder = '-'
str_plasholder_count = 5
plasholder = str_plasholder * str_plasholder_count
str_templat = plasholder + '{}' + plasholder + '\n'
count_print: int = 20




def get_plach1(num):
    return str_templat.format(num)




def prn_tem(tem):
    print('\n\n--------------', tem, '--------------\n\n')
