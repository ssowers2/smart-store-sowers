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

# Dimension Table: customer
| column_name             | data_type | description               |
|-------------------------|-----------|---------------------------|
| customer_id             | TEXT      | Primary key               |
| name                    | TEXT      | Customer’s full name      |
| region                  | TEXT      | Customer's region         |
| join_date               | DATE      | Join date                 |
| loyalty_points          | INTEGER   | Loyalty program points    |
| preferred_contact_method| TEXT      | Contact preference        |

# Dimension Table: product
| column_name    | data_type | description              |
|----------------|-----------|--------------------------|
| product_id     | TEXT      | Primary key              |
| product_name   | TEXT      | Name of the product      |
| category       | TEXT      | Product category         |
| unit_price     | REAL      | Price per unit           |
| stock_quantity | INTEGER   | Product stock quantity   |
| store_section  | TEXT      | Store section location   |

# Fact Table: sale
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


# The database consists of three main tables with a star schema structure:
- customer (dimension)
- product (dimension)
- sale (fact)

# The sale table includes foreign keys referencing the customer and product tables to ensure each sale is tied to valid dimension data.
- All primary keys are TEXT to match the data in the CSVs.
- Foreign key constraints were enabled with PRAGMA foreign_keys = ON.
- The schema enforces referential integrity between related records.

# The screenshots below shows that all three tables in the `smart_sales.db` file were successfully populated:
![Tables Verified - Customer](docs/customer.png)
![Tables Verified - Product](docs/product.png)
![Tables Verified - Sale](docs/sale.png)

# Challenge Encountered: Foreign key constraint errors
- Issue: Some records in the sales dataset referenced customer_ids or product_ids that were missing from the cleaned customers or products tables.
- Solution: Added filtering logic to the etl_to_dw.py script to exclude any sales records where the customer_id or product_id was missing in the corresponding dimension tables.
This ensured that foreign key constraints would not be violated during insertion into the sale table.
  
# Challenge Encountered: Column mismatches after cleaning
- Issue: The original CSVs had PascalCase headers that needed to be converted to snake_case to match the database schema.
- Solution: Converted all headers to  match the database schema. 

# Power BI Sales Dashboard Report
This Power BI dashboard provides an overview of product revenue and customer spending over a selected date range. It allows for slicing, dicing, and analysis of sales trends by product, customer, category, region, and time.
![Power BI Dashboard](image.png)

## Date Filter
**Sales Date Slicer (Top Left)**  
A range slicer is used to filter the entire dashboard by sales date. This allows users to view performance metrics within a specific time period.
![Sales Date Slicer](image-2.png)

## Regional Sales Table
**Category Sales by Region (Top Left Table)**  
This matrix visual breaks down total sales by product category (Clothing, Electronics, Sports) across four geographic regions (East, North, South, West). It includes row-level totals and a grand total to show cumulative sales performance.
![Regional Sales Table](image-3.png)

## Customer Spending
**Total Amount Spent by Customer (Top Right Bar Chart)**  
A horizontal bar chart displaying the total amount spent by each customer in descending order. This chart highlights top customers and helps identify key revenue drivers.
![Total Amount Spent by Customer](image-7.png)

## Monthly Sales Trend
**Total Sale Amount by Month (Bottom Left Column Chart)**  
A column chart showing the total sales amount grouped by month. The x-axis is sorted by calendar order and also displays the quarter and year. This helps visualize monthly fluctuations in sales performance.
![Monthly Sales Trend](image-5.png)

## Top Products by Revenue
**Top Revenue Products (Bottom Right Line and Area Chart)**  
A combined line and area chart ranking products by total revenue in descending order. This visual highlights the highest-grossing products and helps prioritize inventory or promotional strategies.
![Top Products by Revenuet](image-6.png)

## Dashboard Notes
- All visuals respond to the selected Sales Date filter.
- The data has been transformed in Power Query to extract Year, Quarter, Month Name, and Month Number from the sale date field.
- Month Name is sorted by Month Number to ensure correct chronological display.

----
# Smart Sales OLAP Analysis Project

## Section 1: The Business Goal

### Business Objective:
**Identify the top-performing customer segments based on total sales and loyalty points, broken down by region and contact preference to guide targeted promotions.**

### Why It Matters:
By identifying high-value customers and understanding their preferred communication channels, the business can tailor loyalty rewards, marketing strategies, and outreach efforts. This enhances engagement, boosts sales, and strengthens customer retention.

---

## Section 2: Data Source

### Source Type: 
I worked from prepared data tables. The data was initially cleaned and structured using Python and then stored in a SQLite database. I connected Power BI directly to this SQLite database to perform my OLAP analysis. 

### Tables and Key Columns Used:
**Customer Table**
- `name`
- `region`
- `loyalty_points`
- `preferred_contact_method`
- `region`

**Product Table**
- `product category`

**Sale Table**
- `sale_date` (used to extract `Month Name`, `MonthNumber`, `Year`)
- `sale_amount`

---

## Section 3: Tools

### Tool Used:
**Microsoft Power BI was selected due to:**
- Easy-to-use drag-and-drop interface
- Ideal for building interactive dashboards
- Supports slicing, dicing, and OLAP-style analysis
- Built-in support for custom measures (DAX)
- Easy sharing with business users and stakeholders
  
---

## Section 4: Workflow & Logic

### Dimensions Used:
- Customer Name (Capitalized)
- Region
- Preferred Contact Method
- Month (extracted from `sale_date`)

### Numeric Metrics:
- `Total Sales` (Sum of `sale_amount`)
- `Loyalty Points` (Sum per customer)
- `Average Sale` (Average of `sale_amount`)

### Aggregations:
- Sales aggregated by customer, region, and month
- Loyalty points aggregated by customer and region
- Grouped by Region, Customer, Preferred Contact Method

### Slicing:
- Filter by Region
- Filter by Preferred Contact Method
- Filter by Month/Year
- Filter by Product Purchased
- The slicer format was a dropdown menu with the "Select all" option for easier user navigation

### Dicing:
- Break down by Customer and Region

### Drilldowns:
- Year → Month
- Region → Customer → Products Purchased

---

## Section 5: Plan Your OLAP Analysis

### Output Title:
**"Top Customer Segments by Sales and Loyalty Points"**

### Visual Types:
- **Clustered Column Chart** (Total Sales by Customer, segmented by Region)
- **KPI Cards** (Total Sales, Average Sale, Top Loyalty Points)
- **Matrix Table** (Sales and Loyalty Points by Region and Contact Method)

### Axis Labels:
- **X-axis:** Customer Name
- **Y-axis:** Total Sales Amount
- **Legend:** Region

### Visual Features:
- Distinct region colors for bars
- Data labels showing total sales per customer
- Tooltip showing loyalty points
- Slicers for Region, Preferred Contact Method, Product Category, and Purchase Month

### Measures Created (DAX):
Total Sales = SUM(Transactions[sale_amount])
Average Sale = AVERAGE(Transactions[sale_amount])
Top Loyalty Points = MAX(Customers[loyalty_points])

## Visualizations
![Total Sales Customer and Region Dashboard](images/power_bi_dashboard.png)  
![Slicer By Email Preferred Contact Method](images/power_bi_by_email.png)  
![Slicer By Region](images/slicer_by_region.png)  
![Slicer By Product](images/slicer_by_product.png)
---
## Section 6: Business Actions
Based on the dashboard insights, I would recommend the following actions:

- **Reward Top-Performing Customers:**  
  Customers such as Hermione Grager, Dr Who, and Jason Bourne generated the highest total sales. These customers should be enrolled in a VIP loyalty program or offered exclusive rewards to encourage retention and continued spending.

- **Personalize Outreach by Contact Method:**  
  Text and email were the most common contact methods among top-spending customers. Promotions should be tailored using these preferences to improve engagement and response rates.

- **Leverage High-Value Regions:**  
  The East and West regions produced the highest sales and loyalty point totals. Regional campaigns or localized promotions should be prioritized in these areas to drive and sustain continued success.

- **Engage Low-Activity Segments:**  
  Customers such as Tony Stark and Tiffany James showed lower purchase activity. These segments could be targeted with reactivation campaigns or personalized incentives to boost participation and sales.


# Sales Insight Dashboard – Analyzing Product Trends Over Time
## Section 1. The Business Goal
The goal of this project is to analyze sales trends by product category over time. This helps stakeholders identify which product lines are growing or declining, so resources can be better allocated to marketing, inventory, or discontinuations.

---

## Section 2. Data Source
The dataset includes three main tables:
- **Sale Table**: Contains transaction details including date, amount, product ID, and payment type.
- **Product Table**: Includes category, product name, unit price, and product ID.
- **Customer Table**: Contains region and join date.

---

## Section 3. Tools Used
- **Power BI**: Used for data modeling, visualizations, and dashboard creation.
- **Data Analysis Expressions (DAX)**: Used for calculating total sales and average sales by category.
- **Power Query Editor**: Used to clean, format, and prepare data (e.g., capitalization of text fields, formatting dates).

---

## Section 4. Workflow & Logic
- Loaded and related the sale, product, and customer tables using Power BI's model view.
- Added date fields (`Month`, `Year`, `MonthYear`) using calculated columns for trend analysis.
- Manually formatted `product_category` and `payment_type` for consistent capitalization.
- Created custom DAX measures such as: Total Sales = SUM(Sale[sale_amount])

## Section 5. Results
### Visualizations

- **KPI Cards**: Total Sales and Average Sales by Category  
- **Line Chart**: Sales trends by product category (MonthYear)  
- **Pie Chart**: Proportion of sales by payment type  
- **Stacked Bar Chart**: Monthly sales breakdown by category  
- **Bar Chart**: Top 3 selling products per selected month  

2024 Product Category Sales Insights Dashboard
![Product Category Sales Insights Dashboard](images/power_bi_sales_insights.png)

Highest Sales By Month and Category
![Highest Sales By Month and Category](images/highest_sales_month_category.png)

Highest Sales By Region
![Highest Sales By Region](images/highest_sales_region.png)

### Key Insights
- **Electronics** generated the highest sales.  
- **Sports** had the lowest sales across all months.  
- Most sales were made via **Credit** and **Debit** payment types.  
- The **Top 3 products** drove the majority of monthly sales which were jackets, controllers, and hoodies.

---
## Section 6. Suggested Business Actions
- **Increase inventory for high-performing categories/products**:  
  Clothing and Electronics both generated high revenue, with products like the "Jacket" and "Controller" appearing among the Top 3 selling items. I would recommned increasing inventory for these categories especially around February since that was a high selling month. 

- **Reevaluate or discontinue low-performing product categories**:  
  The Sports category showed very low sales in all months and had no representation in the Top 3 products. I think the business may want to reassess demand for this category by promoting clearance sales or consider phasing these products out altogether.

- **Launch targeted promotions during lower-sales months**:  
  January and March reflected lower total sales volume. Targeted promotions such as limited-time discounts, bundle deals, or loyalty point incentives during these slower months could boost revenue.

- **Offer checkout incentives aligned with popular payment types**:  
  Credit and Debit were the most popular payment methods (75% combined). Offering double loyalty points or higher percent discounts to use these payment methods could increase sales.

---

## Section 7. Challenges
- **The dataset was small, limiting broader trend views**:  
  With only three months of data, it's difficult to identify strong seasonal patterns or make confident long-term decisions. While February saw a significant spike, it's unclear whether this trend recurs yearly.

- **Small sales values sometimes made data labels difficult to display clearly**:  
  Challenge: Dealing with small sales values that caused data labels to disappear on stacked bar and pie charts. This made it difficult to visualize the performance of low-performing categories. I also had to manually clean and reformat data fields like payment_type and product_category for consistent capitalization and readability in visuals.

  Solution: I addressed the label issue by switching from vertical to horizontal bar charts, which gave more space for labels to display. I also used tooltips to ensure all values could still be accessed even if they weren’t visually labeled. In Power Query, I capitalized category and payment values.

---

## Section 8. Ethical Considerations
- **No AI or predictive modeling was used; the project remained descriptive**:  
  One ethical consideration I accounted for was the potential for unintentional bias in how the data is presented or interpreted. For instance, highlighting certain product categories or payment types could influence stakeholder decisions without considering external factors like marketing efforts or regional preferences. To address this, I focused on presenting transparent, descriptive metrics without making assumptions about customer behavior. By sticking to actual sales data and avoiding predictive claims, I aimed to minimize bias.

- **Stakeholders should avoid making critical decisions without further data validation**:  
  The dataset is limited in both time (just three months of data) and volume. This makes it difficult to draw long-term conclusions or identify true seasonal trends. Therefore, any suggested business actions should be considered preliminary and validated against larger, more complete datasets before implementation.