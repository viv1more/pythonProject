def format_name(firstname, lastname):
    if firstname == '' or lastname == '':
        return 'Nothing to format'
    First = firstname.title()
    Last = lastname.title()
    return f"{First} {Last}"


# f= format_name("vIvEk","more")
f = format_name(input("enter first name - "), input("enter last name- "))
print(f)
