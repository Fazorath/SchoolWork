-- Create Customers table
CREATE TABLE Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Create Orders table
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Create Categories table
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Create Manufacturers table
CREATE TABLE Manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_name VARCHAR(100) NOT NULL
);

-- Create Brands table
CREATE TABLE Brands (
    brand_id INT AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(50) NOT NULL
);

-- Create Models table
CREATE TABLE Models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    model_name VARCHAR(50) NOT NULL
);

-- Create Products table
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    manufacturer_id INT NOT NULL,
    brand_id INT NOT NULL,
    model_id INT NOT NULL,
    CONSTRAINT fk_products_categories FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE,
    CONSTRAINT fk_products_manufacturers FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id) ON DELETE CASCADE,
    CONSTRAINT fk_products_brands FOREIGN KEY (brand_id) REFERENCES Brands(brand_id) ON DELETE CASCADE,
    CONSTRAINT fk_products_models FOREIGN KEY (model_id) REFERENCES Models(model_id) ON DELETE CASCADE
);

-- Create Order_Items table
CREATE TABLE Order_Items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    item_price DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_order_items_orders FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    CONSTRAINT fk_order_items_products FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Create Reviews table
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    rating INT NOT NULL,
    review_text TEXT,
    review_date DATE NOT NULL,
    CONSTRAINT fk_reviews_products FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE,
    CONSTRAINT fk_reviews_customers FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

-- Create Product_Images table
CREATE TABLE Product_Images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    CONSTRAINT fk_product_images_products FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);


-- Populate Brands table
INSERT INTO Brands (brand_name) VALUES
('Honda'),
('Yamaha'),
('Kawasaki'),
('Suzuki'),
('Ducati'),
('Harley-Davidson'),
('BMW'),
('Triumph'),
('KTM'),
('Aprilia');

-- Populate Models table
INSERT INTO Models (model_name) VALUES
('CB500X'),
('YZF-R6'),
('Ninja 650'),
('GSX-R750'),
('Panigale V4'),
('Sportster Iron 883'),
('S1000RR'),
('Street Triple'),
('Duke 390'),
('RSV4');

-- Populate Categories table
INSERT INTO Categories (category_name) VALUES
('Street Bikes'),
('Sport Bikes'),
('Cruisers'),
('Adventure Bikes'),
('Touring Bikes');

-- Populate Manufacturers table
INSERT INTO Manufacturers (manufacturer_name) VALUES
('Honda Motor Co.'),
('Yamaha Corporation'),
('Kawasaki Heavy Industries'),
('Suzuki Motor Corporation'),
('Ducati Motor Holding'),
('Harley-Davidson'),
('Bayerische Motoren Werke AG'),
('Triumph Motorcycles'),
('KTM AG'),
('Aprilia');

-- Populate Customers table
INSERT INTO Customers (first_name, last_name, email, address) VALUES
('John', 'Doe', 'john@example.com', '123 Main St'),
('Jane', 'Smith', 'jane@example.com', '456 Elm St'),
('Michael', 'Johnson', 'michael@example.com', '789 Oak St');

-- Populate Orders table
INSERT INTO Orders (customer_id, order_date, total_price, status) VALUES
(1, '2024-04-25', 2399.00, 'Shipped'),
(2, '2024-04-26', 4599.00, 'Pending'),
(3, '2024-04-27', 3299.00, 'Delivered');

-- Populate Products table
INSERT INTO Products (product_name, category_id, manufacturer_id, brand_id, model_id) VALUES
('CB500X', 4, 1, 1, 1),
('YZF-R6', 2, 2, 2, 2),
('Ninja 650', 1, 3, 3, 3);


-- Populate Order_Items table
INSERT INTO Order_Items (order_id, product_id, quantity, item_price) VALUES
(1, 1, 1, 7999.00),
(2, 2, 1, 8999.00),
(3, 3, 1, 6799.00);

-- Populate Reviews table
INSERT INTO Reviews (product_id, customer_id, rating, review_text, review_date) VALUES
(1, 1, 5, 'Great bike!', '2024-04-25'),
(2, 2, 4, 'Amazing performance', '2024-04-26'),
(3, 3, 3, 'Good value for money', '2024-04-27');

-- Populate Product_Images table
INSERT INTO Product_Images (product_id, image_url) VALUES
(1, 'image1.jpg'),
(2, 'image2.jpg'),
(3, 'image3.jpg');
