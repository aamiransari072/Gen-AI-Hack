import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


part1 = "textSumarizer"
part2 = 'chatbot'

list_of_files = [
    "./github/wrokflows/.gitkeep",
    f"src/{part1}/__init__.py",
    f"src/{part1}/components/__init__.py",
    f"src/{part1}/utils/__init__.py",
    f"src/{part1}/utils/common.py",
    f"src/{part1}/logging/__init__.py",
    f"src/{part1}/config/__init__.py",
    f"src/{part1}/config/configuration.py",
    f"src/{part1}/pipeline/__init__.py",
    f"src/{part1}/entity/__init__.py",
    f"src/{part1}/constants/__init__.py",
    f"src/{part2}/__init__.py",
    f"src/{part2}/components/__init__.py",
    f"src/{part2}/utils/__init__.py",
    f"src/{part2}/utils/common.py",
    f"src/{part2}/logging/__init__.py",
    f"src/{part2}/config/__init__.py",
    f"src/{part2}/config/configuration.py",
    f"src/{part2}/pipeline/__init__.py",
    f"src/{part2}/entity/__init__.py",
    f"src/{part2}/constants/__init__.py",
    
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb",
    "requirements.txt"


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    logging.info(f"Processing {filepath}")

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file : {filepath}")
    else:
        logging.info(f"File already eixists: {filename}")





