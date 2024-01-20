def convert():
    inches = [150, 155, 145, 148]
    cms = []
    for item in inches:
        cms.append(item * 2.5)
    print("List in Inches", inches)
    print("List in cm's", [item * 2.5 for item in inches])

convert()