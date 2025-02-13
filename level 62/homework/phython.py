my_dict = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    }

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age <= 14 and age <=18:
        return "drink coke"
    elif age >=18 and age <21:
        return "drink beer"
    elif age >=21:
        return "drink whisky"
        
    