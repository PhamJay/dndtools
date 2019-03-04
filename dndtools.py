

if __name__ == '__main__':
    import monsterfinder
    import misc
    import encounter_generator
    import ecnounter_finder
    import sandbox
    print("Welcome to DnDTools, enter a number for the function you want to execute")
    f = "{}  {:<20}|" + (" " * 10) + "{:<20}"
    fns = [
        (1, "Find Monster", "Allows you to search for a monster", monsterfinder.main),
        (2, "Start Encounter", "Start an encounter from the encounters you have created", sandbox.main),
        (3, "Create encounter", "Create an encounter which can then be played", encounter_generator.generate_ecnounter_io),
        (4, "Generate loot", "Generates random loot", misc.loot_fn),
        (5, "Create monster", "Creates a monster that can then be added to an encounter", 0),
        (6, "view encounter", "Shows the available encounters", ecnounter_finder.display)
    ]
    def print_fns():
        print(f.format("#", "Name", "Description"))
        for fn in fns:
            print(f.format(*fn[0:-1]))

    while True:
        print("")
        print_fns()
        inp = input("select option or type ! to quit: ")
        if inp == "!":
            break
        try:
            option = int(inp)
            selected = False
            for fn in fns:
                if fn[0] == option:
                    selected = True
                    print("selected option", option)
                    funct = fn[-1]
                    funct()
            if not selected:
                print("option was not found try again")
        except Exception as e:
            print("error while reading input")
            print(e)
