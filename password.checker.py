def check_strength(password):

    specials = "!@#$%^&*"
    rules = []
    
    rules.append(len(password)>= 8)

    rules.append(any(c.islower() for c in password) and any(c.isupper() for c in password))

    rules.append(any(c.isdigit() for c in password)) 
 

    rules.append(any(c in specials for c in password))
   
    true_count = rules.count(True)

    if true_count < 2:
        return "weak"
    elif true_count == 2 or true_count == 3:
        return "medium"
    else:
        return "strong"


password = input("Insert your password: ")
result = check_strength(password)

print(f"Password is: {result}")
