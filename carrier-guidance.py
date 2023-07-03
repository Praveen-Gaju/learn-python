"""
. App Developer
a. Native • You can learn Java, Swift
b. Hybrid • You can learn Flutter, React Native 
2. Web Developer
a. Frontend
• You can learn HTML & CSS, Javascript
b. Backend
• You can learn Python, Javascript, Ruby, Java
3. Data Science
a. You can learn Python 
4. Cyber Security
a. You can learn Networking 
"""

field = input("What field you want to opt for = ").lower()
if field == "app developer":
    app_dev = input("What type of app developer you want to become = ").lower()
    if app_dev == "hybrid":
        print("You can learn Flutter, React Native")
    elif app_dev == "native":
        print("You can learn Java, Swift")
    else:
        print("Invalid")
elif field == "web developer":
    web_dev = input("What type of web developer you want to become = ").lower()
    if web_dev == "frontend":
        print("You can learn HTML & CSS, Javascript")
    elif web_dev == "backend":
        print("You can learn Python, Javascript, Ruby, Java")
    else:
        print("Invalid")
elif field == "data science":
    print("You can learn Python")
elif field == "cyber security":
    print("You can learn Networking")
else:
    print("Invalid choice")