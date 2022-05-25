import subprocess

with open("stdout.txt", "wb") as out, open("stderr.txt", "wb") as err:
    main = subprocess.Popen(["python3", "main.py"], stdout=out, stderr=err)