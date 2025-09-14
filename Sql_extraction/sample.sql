-- Sample SQL: Users table
CREATE TABLE users (
    id INT,
    name VARCHAR(50),
    email VARCHAR(100),
    postalZip VARCHAR(10),
    phone VARCHAR(20)
);

-- Insert sample data
INSERT INTO users (id, name, email, postalZip, phone) VALUES
(1, 'Alice', 'alice123@yahoo.com', '560001', '(816) 530-4269'),
(2, 'Bob', 'bob_smith@outlook.com', '560002', '1-811-920-9732'),
(3, 'Charlie', 'charlie@company.org', '56A003', '(123) 456-7890'),
(4, 'David', 'david.456@random.com', '560004', '9876543210'),
(5, 'Eve', 'eve99@domain.co', '560005', '(321) 654-0987');
