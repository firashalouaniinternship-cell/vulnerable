# vulnerable.py
import subprocess

     # Exemple vulnérable : injection possible
    subprocess.run(["echo", user_input], check=True)