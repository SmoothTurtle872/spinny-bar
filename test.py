import spinny_bar
import time
import multiprocessing

def defaults():
    spinner = spinny_bar.spinners.spinner(message="A Regular Spinner")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    