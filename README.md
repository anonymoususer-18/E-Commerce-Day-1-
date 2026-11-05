# 🛒 E-Commerce System (Day 1 Project)

## Project Overview

This project is a Python-based E-Commerce Backend System developed as part of Day 1 learning activities. The application simulates the core functionalities of an online shopping platform using Python, Pandas, and NumPy without any frontend interface.

All operations are performed through a Command Line Interface (CLI), allowing users to interact with products, carts, orders, and shipment services.

---

## Day 1 Task

### Objective

Build an E-Commerce application using Python with the following services:

- Products Service
- Catalog Service
- Cart Service
- Shipping Service

### Technologies Used

- Python
- Pandas
- NumPy
- CSV Files for Data Storage

### Design Approach

- Backend only application
- No frontend/UI involved
- Service-based modular structure
- CSV files used as lightweight database
- Separate modules for each business functionality

---

## Extended Enhancements

The initial implementation was further enhanced by introducing a dedicated User Module and additional e-commerce capabilities.

### User Features

Users can:

- Register as a new user
- Login using username and password
- View personal profile
- Browse products
- Search products by category
- Search products by product name
- Add products to cart
- View saved cart
- Checkout products
- View previous orders
- Track shipment status
- Logout securely

---

## Features

### Product Service

- Store product details
- Maintain product inventory
- Manage product information using CSV files

### Catalog Service

- Display all available products
- Search products by category
- Search products by product name

### Cart Service

- Add items to cart
- View cart contents
- Calculate total cart value

### Checkout Service

- Generate customer orders
- Save order history
- Process purchases

### Order Management

- View past orders
- Maintain order records for each user

### Shipping Service

- Track shipment status
- Display delivery information
- Provide shipping policy details

### Analytics Service

Implemented using Pandas and NumPy.

Includes:

- Product Price Analysis
- Stock Analysis
- Category Distribution Analysis
- Shipment Trend Analysis

---

## Project Structure

```text
E-Commerce-Day-1
│
├── main.py
├── products.py
├── catalog.py
├── cart.py
├── shipping.py
├── user.py
├── analytics.py
│
├── products.csv
├── Users.csv
├── Orders.csv
│
└── README.md
```

---

## Application Flow

```text
User Registration/Login
          │
          ▼
      View Products
          │
          ▼
     Add Items To Cart
          │
          ▼
        Checkout
          │
          ▼
       Place Order
          │
          ▼
     Track Shipment
```

---

## Menu Options

```text
1. My Profile
2. View Products
3. Search By Category
4. Search By Product Name
5. Add Product To Cart
6. View Cart
7. Checkout
8. My Orders
9. Track Shipment
10. Shipping Policy
11. Product Price Analysis
12. Stock Analysis
13. Category Distribution
14. Shipment Trend
15. Logout
```

---

## How to Run the Project

### Clone Repository

```bash
git clone https://github.com/anonymoususer-18/E-Commerce-Day-1.git
```

### Move to Project Directory

```bash
cd E-Commerce-Day-1
```

### Install Required Libraries

```bash
pip install pandas numpy
```

### Run Application

```bash
python main.py
```

---

## Sample User Credentials

```text
Username: arivu
Password: pass123
```

---

## Concepts Used

- Python Modules
- Functions
- CSV File Handling
- User Authentication
- Data Persistence
- Pandas Data Analysis
- NumPy Operations
- Service-Based Modular Design
- CLI Application Development

---

## Learning Outcomes

Through this project, I learned:

- Python project structuring
- Modular application development
- CSV-based data management
- Pandas for analyzing data
- NumPy for calculations and numerical operations
- User authentication implementation
- Cart and order management workflows
- Shipment tracking workflows
- Backend service integration

---

## Future Enhancements

- MySQL Database Integration
- FastAPI REST APIs
- Flask Web Application
- Payment Gateway Integration
- Admin Dashboard
- Inventory Management
- Docker Containerization
- Cloud Deployment

---

## Author

**Arivananthan M**

Day 1 Project - Python-Based E-Commerce Backend System developed using Python, Pandas, and NumPy with Product, Catalog, Cart, Shipping, Analytics, and User Management modules.
``
