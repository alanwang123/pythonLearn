name = input("what's your name ? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("slytherin")
    case _:
        print("who?")
