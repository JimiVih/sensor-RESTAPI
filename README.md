Guide to get you started!
-

!_GOOD TO KNOW BEFORE INSTALLATION_!
-Python version used was 3.13.x

**Installation & Setup**
1) Download the .zip file and extract the content in to the folder of your choice
2) Open the/Navigate to the folder in *Konsole/cmd*, or open the folder in *vscode* and use the terminal inside vscode
3) Create a virtual environment `python -m venv <folder name (ex. .venv)>`
4) **!GOOD TO KNOW!** if you have, let's say Python version 3.14.x installed and want to, OR have to, use an older version inside the venv (in this case version 3.13.x);
you can write `python3.13 -m venv <folder name>`. Ofc first you need to have 3.13 installed :)
5) Change your current python to the python of the venv (or activate the virtual environment) `source ~/<folder_name>/bin/activate`
6) Install the required libraries `pip install -r requirements.txt`
7) Done installing and setting up

**Running the app**
1) To run the app use `fastapi dev` inside the vscode terminal

**Using the interactive documentation**
1) Open the documentation by clicking the '127.0.0.1:8000/docs' link in the terminal OR by manually opening up you preferred browser and typing '127.0.0.1:8000/docs'

YOU'RE ALL SET!


Troubleshooting
-


