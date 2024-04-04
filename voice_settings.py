import os
import subprocess

def module_exists(name):
    try:
        subprocess.check_call(["pip", "show", name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Module '{name}' is installed.")
        return True
    except subprocess.CalledProcessError:
        print(f"Module '{name}' is not installed.")
        return False

def requirements(install=True):
    os.system("cls")
    if install:    
        print(">> Begin install...")
        os.system("pip install -r requirements.txt")
        print(">> End install.")
    os.system("cls")