-- =====================================================
-- Customers Table
-- =====================================================

CREATE TABLE IF NOT EXISTS ecommerce.customers (

    customer_id INT PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    email VARCHAR(150) UNIQUE NOT NULL,

    phone VARCHAR(15),

    city VARCHAR(50),

    state VARCHAR(50),

    country VARCHAR(50),

    registration_date DATE

);

-- =====================================================
-- Products Table
-- =====================================================

CREATE TABLE IF NOT EXISTS ecommerce.products (

    product_id INT PRIMARY KEY,

    product_name VARCHAR(100),

    category VARCHAR(50),

    brand VARCHAR(50),

    price NUMERIC(10,2),

    stock_quantity INT

);

-- =====================================================
-- Orders Table
-- =====================================================

CREATE TABLE IF NOT EXISTS ecommerce.orders (

    order_id INT PRIMARY KEY,

    customer_id INT
        REFERENCES ecommerce.customers(customer_id),

    order_date DATE,

    payment_method VARCHAR(50),

    status VARCHAR(50),

    total_amount NUMERIC(10,2)

);

-- =====================================================
-- Order Items Table
-- =====================================================

CREATE TABLE IF NOT EXISTS ecommerce.order_items (

    order_item_id INT PRIMARY KEY,

    order_id INT
        REFERENCES ecommerce.orders(order_id),

    product_id INT
        REFERENCES ecommerce.products(product_id),

    quantity INT

);