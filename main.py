import logic.connect_4 as con
import UI_basic.connect_4_UI as conUI


if __name__ == '__main__':

    print("Main Running")

    gameUI = conUI.connect4UI(mode="human")


    while True:
        gameUI.update()
        gameUI.check_event()





    print("Main Finished")


