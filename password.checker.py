def check_strength(password):

    specials = "!@#$%^&*"
    rules = []
    #prima regula trebuie sa verifice daca parola are mai mult sau egal cu 8 caractere introduse. Mai jos avem o comparatie prin len(passowrd >= 8) care returneaza o valoare booleana.
    rules.append(len(password)>= 8)

    #regula ca parola sa contina minim un lowercase si un uppercase
    rules.append(any(c.islower() for c in password) and any(c.isupper() for c in password))

    #regula ca parola sa contina cel putin o cifra
    rules.append(any(c.isdigit() for c in password)) #functia isdigit returneaza true dupa ce itereaza in stringul password daca gaseste o cifra.
    #regula care sa testeze daca contine sau nu un caracter special

    rules.append(any(c in specials for c in password))
    #cu asta am terminat de implementat regulile de filtrare ale parolei, acum trebuie sa returnam un output in functie de valorile din lista pe care le indepineste inputul userului in parola.
   
    #pentru a tine evidenta trebuie sa definim variabile unde tinem minte numarul de valori indeplinite.
    true_count = rules.count(True)

    if true_count < 2:
        return "weak"
    elif true_count == 2 or true_count == 3:
        return "medium"
    else:
        return "strong"

#Am terminat de implementat functia de verificare a puterii parolei, acum trebuie implementat user input pt ca nu vreau sa testez cu print.
parola = input("Introduceti parola: ")
rezultatul = check_strength(parola)

print(f"Parola este: {rezultatul}")
