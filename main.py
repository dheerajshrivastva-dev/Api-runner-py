import subprocess
import sys
import os

venv_name = "API-AUTOMATION"

python_executable = "python3"


def create_virtualenv():
    try:
        subprocess.run([python_executable, "-m", "venv", venv_name], check=True)
    except subprocess.CalledProcessError:
        print("\033[91mError: Failed to create virtual environment.\033[0m")



def generate_requirements():
    try:
        subprocess.run(f"{python_executable} -m pip freeze > requirements.txt", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("\033[91mError: Failed to generate requirements.txt.\033[0m")

def activate_virtualenv():
    venv_activate_cmd = f"source {venv_name}/bin/activate" if os.name != "nt" else f"{venv_name}\\Scripts\\activate"
    try:
        subprocess.run([venv_activate_cmd], shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"\033[91m>: {venv_activate_cmd}\033[0m")
        print("\033[91mError: Failed to activate the virtual environment. use above command to manualy activate the venv.\033[0m")
        return False
    
    return True

def install_dependencies():
    
    try:
        subprocess.run([python_executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
    except subprocess.CalledProcessError:
        print("\033[91mError: Failed to install dependencies.\033[0m")
        return False
    
    return True

def start_application():
    # Check if the virtual environment is already activated
    if os.environ.get("VIRTUAL_ENV"):
        print("\033[92mVirtual environment is already activated.\033[0m")
    else:
        if not os.path.exists(venv_name):
            create_virtualenv()
            
            if not activate_virtualenv():
                return

            if not install_dependencies():
                return
        
        else:
            if not activate_virtualenv():
                print('Please activate the venv')
                return

    # Start your Python application
    try:
        print('I am try to run this')
        subprocess.run([python_executable, "index.py"], check=True)
    except subprocess.CalledProcessError:
        print("\033[91mError: Failed to start the Python application.\033[0m")

if __name__ == "__main__":
    start_application()
