# smart-store-sowers

## Purpose  
Practice completing a business intelligence project for a client. 

## Step 1: New Project Setup
1. Initialize Repository: Create a new GitHub repository with this format **smart-store-sowers** with a default `README.md`
2. Clone the repository to your local machine in the **Projects** folder
3. Open the project folder in **VS Code**

## Step 2: Add Essential Files
1. **.gitignore**: Add a `.gitignore` file to specify files and folders to exclude from version control. You can reference an existing `.gitignore` template for Python projects.
2. **requirements.txt**: This file lists all necessary packages for the project. Review and adjust it to include or exclude packages based on your project’s needs.
3. **README.md**: Edit README.md to record commands, process, and notes so far as the project progresses.
4. 5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Step 3: Create and Manage Virtual Environment
1. Run command: `git pull` first, to make sure the current project contents are on the machine.
2. Windows PowerShell: `python -m venv .venv` to create a new .venv environment in the project repo.
3. Activate the Virtual Environment: `.\.venv\Scripts\activate`

## Step 4: Install Required Packages
1. `pip install -r requirements.txt` to install all packages at one time from a file
2. `py -m pip install` to add packages on the go (e.g. `py -m pip install pandas`)
3. `pip install numpy pandas matplotlib seaborn` for multiple packages

## Step 5: Select Python Interpreter in VS Code
1. Ensure VS Code is set to use the .venv environment.
2. Open the command palette using (Windows) Ctrl + Shift + P.
3. Type "Python: Select Interpreter".
4. Choose the interpreter inside the .venv folder located in the project root directory.
5. This is good time to `git add .`, `git commit -m "Message"`, `git push -u origin main` files to GitHub

## Git Commands Reminders 
1. Pull Latest Changes:  `git pull`
2. Add Changes: `git add .`
3. Commit Changes: 5. `git commit -m "Update message"` update commit message a present tense verb
4. Push Changes to GitHub: `git push -u origin main` and then afterwards `git push`
   
## Verify Git Configuration: Check that both user.name and user.email are correctly configured
1. git config --list

## VS Code Extensions:
1. SQLite
2. SQLite Viewer
3. Jupyter
4. Prettier
5. Markdown All in One
6. Rainbow CSV

## Running a Python file (ex: data_prep.py stored in the scripts subfolder of project directory)
1. py scripts\data_prep.py

# Dimension Table: customers
| column_name             | data_type | description               |
|-------------------------|-----------|---------------------------|
| customer_id             | TEXT      | Primary key               |
| name                    | TEXT      | Customer’s full name      |
| region                  | TEXT      | Customer's region         |
| join_date               | DATE      | Join date                 |
| loyalty_points          | INTEGER   | Loyalty program points    |
| preferred_contact_method| TEXT      | Contact preference        |

# Dimension Table: products
| column_name    | data_type | description              |
|----------------|-----------|--------------------------|
| product_id     | TEXT      | Primary key              |
| product_name   | TEXT      | Name of the product      |
| category       | TEXT      | Product category         |
| unit_price     | REAL      | Price per unit           |
| stock_quantity | INTEGER   | Product stock quantity   |
| store_section  | TEXT      | Store section location   |

# Fact Table: sales
| column_name      | data_type | description                     |
|------------------|-----------|---------------------------------|
| transaction_id   | TEXT      | Primary key                     |
| sale_date        | DATE      | Date of the transaction         |
| customer_id      | TEXT      | Foreign key to customers        |
| product_id       | TEXT      | Foreign key to products         |
| store_id         | TEXT      | Store where purchase occurred   |
| campaign_id      | TEXT      | Marketing campaign ID           |
| sale_amount      | REAL      | Total sale amount               |
| discount_percent | REAL      | Discount applied to the sale    |
| payment_type     | TEXT      | Type of payment (e.g., credit)  |