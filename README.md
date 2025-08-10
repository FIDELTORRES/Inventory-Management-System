# Inventory Management System

A web-based inventory management application built with **Flask**, **MySQL**, and **SQLAlchemy**.  
Supports CRUD operations for managing products, with search, pagination, and supplier details.

## Features
- Add, edit, delete, and view product records
- Search by name, SKU, or supplier
- Pagination for large datasets
- Bootstrap UI for clean design

## Tech Stack
- **Backend:** Python, Flask, SQLAlchemy
- **Database:** MySQL (SQLite for quick testing)
- **Frontend:** HTML, CSS, Bootstrap

## Installation
1. Clone this repository  
   ```bash
   git clone https://github.com/your-username/inventory-management.git
   cd inventory-management
   ```
2. Create and activate virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
4. Set up `.env` file with your database URI:
   ```
   SECRET_KEY=your_secret_here
   DATABASE_URI=mysql+mysqldb://root:password@localhost/inventory_db
   ```
   *(or use SQLite: `sqlite:///inventory.db`)*

5. Initialize the database:  
   ```bash
   mysql -u root -p < schema.sql
   ```
6. Run the app:  
   ```bash
   python app.py
   ```
7. Open in browser:  
   ```
   http://127.0.0.1:5000/
   ```

## License
MIT License
