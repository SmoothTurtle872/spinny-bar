import spinny_bar
import time
import multiprocessing
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def defaults():
    spinner = spinny_bar.spinners.spinner(message="A Default Spinner")
    spinnerBar = spinny_bar.spinners.spinnerBar(message="A Default Spinnerbar")
    progressBar = spinny_bar.progressBars.progressBar(message="A Default Progress bar")
    
    spinner.start()
    time.sleep(2)
    spinner.stop()
    spinnerBar.start()
    time.sleep(2)
    spinnerBar.stop()
    while progressBar.value < progressBar.maxValue:
        progressBar.addToValue(1)
        progressBar.displayBar()
        time.sleep(0.1)
    progressBar.endBar()

def customising():
    customSpinner = spinny_bar.spinners.spinner(message="A Customised Spinner Spinner", chars=["+","x"], speed=0.2)
    customSpinnerBar = spinny_bar.spinners.spinnerBar(message="A Customised Spinnerbar", barCaps=["]", "["], barEmpty="|", barFilled="█", barLen=10, filledLen=4)
    customProgressBar = spinny_bar.progressBars.progressBar(message="A Customised Progress bar", caps=["",""], empty=f"{Fore.RED}─", full=f"{Fore.GREEN}─")
    
    customSpinner.start()
    time.sleep(2)
    customSpinner.stop()
    customSpinnerBar.start()
    time.sleep(2)
    customSpinnerBar.stop()
    while customProgressBar.value < customProgressBar.maxValue:
        customProgressBar.addToValue(1)
        customProgressBar.displayBar()
        time.sleep(0.1)
    customProgressBar.endBar()
    
def clearAtEnd():
    clearSpinner  = spinny_bar.spinners.spinner(message="A clearing Spinner", clearAtEnd=True)
    clearSpinnerBar  = spinny_bar.spinners.spinnerBar(message="A clearing Spinnerbar", clearAtEnd=True)
    clearProgressBar  = spinny_bar.progressBars.progressBar(message="A clearing Progress bar", clearAtEnd=True)
    
    clearSpinner.start()
    time.sleep(2)
    clearSpinner.stop()
    print("Your Print Statement Here Spinner Complete")
    
    clearSpinnerBar.start()
    time.sleep(2)
    clearSpinnerBar.stop()
    print("Your Print Statement Here Spinner Bar Complete")
    
    while clearProgressBar.value < clearProgressBar.maxValue:
        clearProgressBar.addToValue(1)
        clearProgressBar.displayBar()
        time.sleep(0.1)
    clearProgressBar.endBar()
    
    print("Your Print Statement Here Progress Bar Complete")
    
    

if __name__ == "__main__":
    multiprocessing.freeze_support()
    defaults()
    customising()
    clearAtEnd()