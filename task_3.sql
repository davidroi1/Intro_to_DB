CREATE DATABASE IF NOT EXISTS alx_book_store


CREATE TABLE Books (
    book_id INT PRIMARY_KEY,
    title VARCHAR(130)
    author_id (Foreign Key (author_id) REFERENCES Authors(author_id)),
    price DOUBLE,
    publication_date DATE
);


CREATE TABLE Authors (
    author_id INT PRIMARY_KEY,
    author_name VARCHAR(215)
):


CREATE TABLE Customers (
    customer_id INT PRIMARY_KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);


CREATE TABLE Orders (
    order_id INT PRIMARY_KEY,
    customer_id (Foreign Key (customer_id) REFERENCES Customers(customer_id)),
    order_date DATE
);


CREATE TABLE Order_Details (
    orderdetail_id INT PRIMARY_KEY,
    order_id (Foreign Key (order_id) REFERENCES Orders(order_id)),
    book_id (Foreign Key (book_id) REFERENCES Books(book_id)),
    quantity DOUBLE
);
