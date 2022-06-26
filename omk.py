from os import system
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
system("git clone https://github.com/kaal0408/KAAL && cd KAAL && python3 -m System")
print("lul got error")
