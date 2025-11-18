DROP_STATEMENTS = [
    "DROP TABLE Maintenance CASCADE CONSTRAINTS",
    "DROP TABLE InsurancePolicy CASCADE CONSTRAINTS",
    "DROP TABLE Payment CASCADE CONSTRAINTS",
    "DROP TABLE Rental CASCADE CONSTRAINTS",
    "DROP TABLE Reservation CASCADE CONSTRAINTS",
    "DROP TABLE Vehicle CASCADE CONSTRAINTS",
    "DROP TABLE VehicleType CASCADE CONSTRAINTS",
    "DROP TABLE Customer CASCADE CONSTRAINTS",
    "DROP TABLE Employee CASCADE CONSTRAINTS",
]

CREATE_STATEMENTS = [
    # Customer
    """
    CREATE TABLE Customer (
        customer_id     NUMBER            PRIMARY KEY NOT NULL,
        driver_license  VARCHAR2(30)      UNIQUE NOT NULL,
        name            VARCHAR2(100)     NOT NULL,
        phone_number    VARCHAR2(20),
        email           VARCHAR2(100)     UNIQUE
    )
    """,
    # VehicleType
    """
    CREATE TABLE VehicleType (
        vehicletype_id  NUMBER            PRIMARY KEY NOT NULL,
        category        VARCHAR2(50)      NOT NULL,
        seats_num       NUMBER            CHECK (seats_num >= 1),
        daily_rate      NUMBER(5,2)       CHECK (daily_rate >= 0)
    )
    """,
    # Employee
    """
    CREATE TABLE Employee (
        employee_id     NUMBER            PRIMARY KEY NOT NULL,
        role            VARCHAR2(50)      NOT NULL,
        name            VARCHAR2(100)     NOT NULL
    )
    """,
    # Vehicle
    """
    CREATE TABLE Vehicle (
        vehicle_id      NUMBER            PRIMARY KEY NOT NULL,
        make            VARCHAR2(50)      NOT NULL,
        model           VARCHAR2(50)      NOT NULL,
        year            NUMBER            CHECK (year >= 1900),
        mileage         NUMBER            CHECK (mileage >= 0),
        plate           VARCHAR2(30)      UNIQUE NOT NULL,
        vehicletype_id  NUMBER            NOT NULL,
        CONSTRAINT fk_vehicle_type FOREIGN KEY (vehicletype_id) REFERENCES VehicleType (vehicletype_id)
    )
    """,
    # Reservation
    """
    CREATE TABLE Reservation (
        reservation_id      NUMBER         PRIMARY KEY NOT NULL,
        start_date          DATE           NOT NULL,
        end_date            DATE,
        reservation_date    DATE           DEFAULT SYSDATE NOT NULL,
        availability_status VARCHAR2(30),
        customer_id         NUMBER         NOT NULL,
        vehicle_id          NUMBER         NOT NULL,
        CONSTRAINT fk_res_customer FOREIGN KEY (customer_id) REFERENCES Customer (customer_id),
        CONSTRAINT fk_res_vehicle FOREIGN KEY (vehicle_id) REFERENCES Vehicle (vehicle_id)
    )
    """,
    # Rental
    """
    CREATE TABLE Rental (
        rental_id      NUMBER            PRIMARY KEY NOT NULL,
        rental_date    DATE              NOT NULL,
        return_date    DATE,
        total_amount   NUMBER(10,2)      CHECK (total_amount >= 0),
        reservation_id NUMBER            NOT NULL,
        CONSTRAINT fk_rental_res FOREIGN KEY (reservation_id) REFERENCES Reservation (reservation_id)
    )
    """,
    # Payment
    """
    CREATE TABLE Payment (
        payment_id     NUMBER            PRIMARY KEY NOT NULL,
        charge_due     NUMBER(10,2)      CHECK (charge_due >= 0),
        method         VARCHAR2(30),
        payment_date   DATE              DEFAULT SYSDATE,
        rental_id      NUMBER            NOT NULL,
        CONSTRAINT fk_payment_rental FOREIGN KEY (rental_id) REFERENCES Rental (rental_id)
    )
    """,
    # Maintenance
    """
    CREATE TABLE Maintenance (
        maintenance_id NUMBER            PRIMARY KEY NOT NULL,
        service_date   DATE              NOT NULL,
        description    VARCHAR2(400),
        cost           NUMBER(12,2)      CHECK (cost >= 0),
        vehicle_id     NUMBER            NOT NULL,
        employee_id    NUMBER            NOT NULL,
        CONSTRAINT fk_maint_vehicle FOREIGN KEY (vehicle_id) REFERENCES Vehicle (vehicle_id),
        CONSTRAINT fk_maint_employee FOREIGN KEY (employee_id) REFERENCES Employee (employee_id)
    )
    """,
    # InsurancePolicy
    """
    CREATE TABLE InsurancePolicy (
        insurance_id   NUMBER            PRIMARY KEY NOT NULL,
        policy_number  VARCHAR2(50)      UNIQUE NOT NULL,
        coverage_type  VARCHAR2(100),
        provider       VARCHAR2(100),
        vehicle_id     NUMBER            NOT NULL,
        CONSTRAINT fk_insurance_vehicle FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id)
    )
    """,
]

POPULATE_STATEMENTS = [
    # Customers
    "INSERT INTO Customer VALUES (1, 'D1234567', 'Alice Johnson', '416-555-1234', 'alice@email.com')",
    "INSERT INTO Customer VALUES (2, 'D7654321', 'John Doe', '647-555-5678', 'john.doe@email.com')",
    "INSERT INTO Customer VALUES (3, 'D9876543', 'Maria Lopez', '905-555-1122', 'maria.lopez@email.com')",
    # Vehicle Types
    "INSERT INTO VehicleType VALUES (1, 'Economy', 4, 29.99)",
    "INSERT INTO VehicleType VALUES (2, 'SUV', 5, 59.99)",
    "INSERT INTO VehicleType VALUES (3, 'Luxury', 4, 99.99)",
    # Employees
    "INSERT INTO Employee VALUES (501, 'Technician', 'John Smith')",
    "INSERT INTO Employee VALUES (502, 'Manager', 'Sarah Lee')",
    # Vehicles
    "INSERT INTO Vehicle VALUES (101, 'Toyota', 'Corolla', 2021, 20000, 'ABC123', 1)",
    "INSERT INTO Vehicle VALUES (102, 'Honda', 'Civic', 2020, 30000, 'XYZ789', 1)",
    "INSERT INTO Vehicle VALUES (103, 'Ford', 'Explorer', 2022, 15000, 'SUV456', 2)",
    "INSERT INTO Vehicle VALUES (104, 'BMW', 'X5', 2021, 10000, 'LUX999', 3)",
    # Reservations
    "INSERT INTO Reservation VALUES (201, DATE '2025-09-01', DATE '2025-09-05', DATE '2025-08-25', 'Reserved', 1, 101)",
    "INSERT INTO Reservation VALUES (202, DATE '2025-09-03', DATE '2025-09-07', DATE '2025-08-28', 'Reserved', 2, 102)",
    "INSERT INTO Reservation VALUES (203, DATE '2025-09-10', DATE '2025-09-15', DATE '2025-09-01', 'Reserved', 3, 103)",
    # Rentals
    "INSERT INTO Rental VALUES (301, DATE '2025-09-01', DATE '2025-09-05', 199.99, 201)",
    "INSERT INTO Rental VALUES (302, DATE '2025-09-03', DATE '2025-09-07', 249.99, 202)",
    "INSERT INTO Rental VALUES (303, DATE '2025-09-10', DATE '2025-09-14', 399.99, 203)",
    # Payments
    "INSERT INTO Payment VALUES (401, 199.99, 'Card', DATE '2025-09-01', 301)",
    "INSERT INTO Payment VALUES (402, 249.99, 'Cash', DATE '2025-09-03', 302)",
    "INSERT INTO Payment VALUES (403, 399.99, 'Card', DATE '2025-09-10', 303)",
    # Maintenance
    "INSERT INTO Maintenance VALUES (601, DATE '2025-08-15', 'Oil change', 49.99, 101, 501)",
    "INSERT INTO Maintenance VALUES (602, DATE '2025-08-20', 'Tire rotation', 79.99, 102, 502)",
    "INSERT INTO Maintenance VALUES (603, DATE '2025-09-01', 'Brake inspection', 129.99, 103, 501)",
    # Insurance Policies
    "INSERT INTO InsurancePolicy VALUES (701, 'POL12345', 'Comprehensive', 'ABC Insurance', 101)",
    "INSERT INTO InsurancePolicy VALUES (702, 'POL67890', 'Collision', 'XYZ Insurance', 102)",
    "INSERT INTO InsurancePolicy VALUES (703, 'POL54321', 'Comprehensive', 'SecureAuto', 103)",
    "INSERT INTO InsurancePolicy VALUES (704, 'POL99999', 'Liability', 'TrustInsure', 104)",
]

