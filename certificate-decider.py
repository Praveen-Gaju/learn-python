"""
Criteria of having certificate:
1. Student should be a part of CWS.
2. Student has attended at least 3 or more classes. 
3. Student has submitted at least 3 or more
assignments. 
"""
cws_part = input("Are you part of CWS = ").lower()
if cws_part == "yes":
    classes_attended = int(input("Enter classes attented = "))
    if classes_attended >= 3:
        assignments = int(input("Enter number of assignment submitted = "))
        if assignments >= 3:
            print("You are eligible")
        else:
            print("Less assignment submitted. You are not eligible")
    else:
        print("You attented less classes. You are not eligible")
else:
    print("You are not eligible. You are not part of CWS")