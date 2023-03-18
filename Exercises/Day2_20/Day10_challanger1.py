first_name = input('please, write your first name.\n')
last_name = input('please, write your last name.\n')

def format_name(first,last):
    combined_name = first + ' ' + last
    format = combined_name.title()
    return format
print(format_name(first_name, last_name))