# smart-store-sowers

## Purpose  
Practice completing a business intelligence project for a client. 

## Goals

## Step 1: New Project Setup
1. Initialize Repository: Create a new GitHub repository with this format **smart-store-sowers** with a default `README.md`.
2. Clone the repository to your local machine in the **Projects** folder.
3. Open the project folder in **VS Code**.

## Step 2: Add Essential Files
1. **.gitignore**  
   Add a `.gitignore` file to specify files and folders to exclude from version control. You can reference an existing `.gitignore` template for Python projects.
2. **requirements.txt**  
   This file lists all necessary packages for the project. Review and adjust it to include or exclude packages based on your project’s needs.
3. **README.md**  
   Edit README.md to record commands, process, and notes so far as the project progresses.
4. 5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Step 3: Create and Manage Virtual Environment
1. Run command `git pull` first, to make sure the current project contents are on the machine.
2. Windows PowerShell: `python -m venv .venv` to create a new .venv environment in the project repo.
3. Activate the Virtual Environment: `.\.venv\Scripts\activate`

## Step 4: Install Required Packages
`pip install -r requirements.txt` to install all packages at once OR use `py -m pip install` commands to add packages on the go (e.g. `py -m pip install pandas` or group installs `pip install numpy pandas matplotlib seaborn`)

## Step 5: Select Python Interpreter in VS Code
1. Ensure VS Code is set to use the .venv environment.
2. Open the command palette using (Windows) Ctrl + Shift + P.
3. Type "Python: Select Interpreter".
4. Choose the interpreter inside the .venv folder located in the project root directory.
5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Git Commands Reminders 
1. Add Changes: `git add .`
2. Commit Changes: 5. `git commit -m "Message"`
3. Push Changes to GitHub: `git commit -m "Message"`
4. Pull Latest Changes:  `git push -u origin main`

## Verify Git Configuration: Check that both user.name and user.email are correctly configured
1. git config --list

## VS code Extension:
1. SQLite
2. SQLite Viewer
3. Jupyter
4. Prettier
5. Markdown All in One
6. Rainbow CSV

## Running a Python file (ex: data_prep.py stored in the scripts subfolder of project directory)
1. py scripts\data_prep.py