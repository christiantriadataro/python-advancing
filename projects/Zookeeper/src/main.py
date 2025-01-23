from Animal import Bat, Lion, Deer
from constants import ANIMAL_INTRO_MESSAGE, ANIMAL_CHECK_MESSAGE

if __name__ == "__main__":
    print(ANIMAL_INTRO_MESSAGE)
    print(ANIMAL_CHECK_MESSAGE)
    deer = Deer()
    bat = Bat()
    lion = Lion()
    print(deer)
    print(bat)
    print(lion)
