import encounter_display
import encounter_input
import encounter_generator

def main():
    import ecnounter_finder
    import load
    print("select the encounter you want to choose from below: ")
    enc = ecnounter_finder.main()
    enc_num = int(input("encounter number: "))
    path = enc[enc_num]
    split = path.split("\\") #enc[enum] is encounter\"name", when only "name" is needed. Therefore, Encounter.load would break if using it
    playable_encounter = encounter_generator.PlayableEncouter.from_encounter(
        load.load_files(),
        encounter_generator.Encounter.load(split[1])
    )
    display = encounter_display.Display(playable_encounter)
    inp = encounter_input.EncounterInput(playable_encounter, display)
    while not inp.ended:
        display.draw()
        inp.read()


if __name__ == '__main__':
    main()