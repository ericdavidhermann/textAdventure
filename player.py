
# Custom modules
from classes.player import Player
from support.helpers import sleep, clear_screen


def character_creation(start_point=None):
    """
    Recursive function which can be rerun at different points to get character created

    :param start_point: integer to control where to start function
    :return: Nothing
    """
    if start_point is None or start_point < 1:
        # Only show this welcome the first time through
        clear_screen()
        print("\n\nWelcome, SysRunner.  Please create your character!\n\n")

    if start_point is None or start_point <= 2:
        print("You walk up to a hunched over person in a decon suit, who pays you absolutely no attention.")
        print("'Sign in.' the person gruffly says as they toss a translucent datapad your way")
        print("\nThe datapad is flashing a terminal prompt:")
        sex = input("\nEnter your sex: (M)ale, (F)emale, (O)ther\n:_> ").upper()
        got_sex = check_sex(sex)

        if got_sex:
            name = input("\nEnter your handle.\n:_> ")

            print("\nEnter your technology specialty from the following:")
            print("(1): Phreaker  (STR/CON) [Warrior/Barbarian]")
            print("(2): Slicer    (INT/WIL) [Wizard/Mage]")
            print("(3): Gh0st     (DEX/STR) [Archer/Ranger]")
            print("(4): Stalker   (DEX/SPD) [Thief/Rogue]")
            specialty = input("\nEnter your specialty.\n:_> ")

            got_specialty = check_specialty(specialty)
            if got_specialty:
                print("\nConfirm registration details")
                print("Name: " + name)
                print("Sex: " + sex)
                print("Specialty: " + got_specialty)
                print("\nIs this correct? (Y/N)")
                register_acknowledge = input("\n:_> ").upper()
                go_register = check_register(register_acknowledge)
                if go_register:
                    registration_status = register_player(name, sex, got_specialty)
                    if registration_status:
                        print("Uploading memory core to archive.  Please stand by . . .")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(".")
                        sleep(1)
                        print(". . . Upload complete.")
                        print("\n\nThe hunched over figure barely acknowledges the confirmation beep from the datapad"
                              " as they eagerly snatch it from your hands.")
                        print("'Alright, get out of here \"" + name + "\"'.")
                        print("'Don't flatline on us!' the figure mocks derisively, tossing a small black box your way")
                    else:
                        print("\nError in registration process!  Let's try that again...")
                        character_creation(1)
                else:
                    print("\nAlright, let's try this one more time then...")
                    character_creation(1)
            else:
                print("\nThe intake agent huffs when he hears the error tone the datapad emits.")
                print("'Woah woah woah, Whatever you're selling, we ain't buying.  Do it again, and do it right.'")
                print("They leave a smudge on the screen as they jab their finger on the display")
                character_creation(1)

        else:
            print("\nThe hunched over figure hears the error tone emanating from the datapad and scowls.")
            print("'Look, I ain't asking for much, ya got three choices - don't like it?  Take it up with management'")
            character_creation(1)


def check_sex(sex):
    """
    Ensures input for character sex is valid
    Valid sex is one of M, F, or O.  All other entries invalid

    :param sex:
    :return: Boolean True/False
    """
    if sex in ('M', 'F', 'O'):
        return True
    else:
        return False


def check_specialty(specialty):
    """
    Checks the specialty of the player.
    Specialty can be considered the class or archetype the character is personifying as illustrated here:
        1: Phreaker  (STR/CON) [Warrior/Barbarian]
        2: Slicer    (INT/WIL) [Wizard/Mage]
        3: Gh0st     (DEX/STR) [Archer/Ranger]
        4: Stalker   (DEX/SPD) [Thief/Rogue]

    :param specialty: The specialty, as an integer, to be translated to its named counterpart in this function
    :return: The specialty, in plain text (Phreaker, Slicer, Gh0st, Stalker) or False if improper selection made
    """
    specialties = {"1": "Phreaker", "2": "Slicer", "3": "Gh0st", "4": "Stalker"}
    specialty = specialties.get(specialty)

    if specialty is None:
        return False
    else:
        return specialty


def check_register(register):
    """
    Confirms registration acknowledgement of player

    :param register:
    :return: Boolean True/False
    """
    if register not in ('Y', 'N') or register == "N":
        return False
    else:
        return True


def register_player(name, sex, specialty):
    """
    Instantiates the player class with the provided details
    :param name:  The player's chosen name
    :param sex:  The player's chosen sex
    :param specialty:  The player's chosen specialty

    :return: An instantiated Player Object
    """
    player = Player(name, sex, specialty)
    return player
