# NexGen ERP

A lightweight, professional Mini ERP system built with Python, designed for efficient management of internal company resources, including human capital and physical/digital assets.

## Overview

NexGen ERP is a modular management system that provides small to medium-sized enterprises with a streamlined interface for handling day-to-day operations. The system emphasizes data integrity, object-oriented design patterns, and simplified financial reporting.

## Key Features

- **HR & Employee Management**: Lifecycle management of employees and managers, including role-based salary and bonus configurations.
- **Asset Lifecycle Tracking**: Manage both Hardware (physical) and Software (digital) assets with built-in depreciation logic.
- **Financial Analytics**: Real-time calculation of salary expenditures and total asset valuation.
- **Data Persistence**: Automated flat-file storage mechanism to ensure data is retained across sessions without the need for complex database overhead.
- **Input Validation**: Robust terminal-based validation system to prevent data entry errors.

## Tech Stack

- **Core**: Python 3.x
- **Persistence**: Flat-file storage (`.txt`)
- **Architecture**: Modular Object-Oriented Programming (OOP) using Abstract Base Classes (ABC)
- **Validation**: Custom `Validator` module for secure terminal I/O

## System Architecture

NexGen ERP follows a modular architecture centered around shared entities:

1.  **Core Entity Layer (`Employees.py`, `Assets.py`)**: Defines the base templates using Python's `abc` module. Implements encapsulation and inheritance for Managers, Employees, Hardware, and Software.
2.  **Service/Module Layer (`EmployeesMenu.py`, `AssetsMenu.py`)**: Contains the business logic for manipulating entities.
3.  **Persistence Layer (`app.py`)**: Handles the serialization and deserialization of data to the local filesystem.
4.  **Reporting Layer (`CompanyFinancial.py`)**: Aggregates data from multiple modules to generate business insights.

## Project Structure

```text
erpM7/
├── app.py                # Main application entry point & Database logic
├── Employees.py         # HR Data Models (Employee, Manager)
├── EmployessMenu.py     # HR Business Logic & UI
├── Assets.py            # Asset Data Models (Hardware, Software)
├── AssetsMenu.py        # Asset Business Logic & UI
├── CompanyFinancial.py  # Financial Reporting Module
├── Validator.py         # Utility for Input Data Validation
├── employees.txt        # Persisted HR Data
└── assets.txt           # Persisted Asset Data
```

## Installation

1.  **Prerequisites**: Ensure Python 3.8+ is installed.
2.  **Clone/Extract**: Download the repository to your local machine.
3.  **Environment**: No external dependencies are required. A virtual environment is recommended but optional.
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

## Running the Application

Launch the system via the main entry point:

```bash
python app.py
```

### Access Credentials
*  Check app.py for default credentials

## ERP Modules

### 1. HR Management
Manage the organizational hierarchy.
*   **Add Employee/Manager**: Specialized fields for bonuses (Managers only).
*   **Update Records**: Dynamic updates to names, salaries, and bonuses.
*   **Asset Assignment**: Directly link company assets to specific employees.

### 2. Asset Management
Track hardware and software inventory.
*   **Hardware**: Track physical condition.
*   **Software**: Monitor license expiration dates.
*   **Depreciation**: Logic for calculating asset value over time.

### 3. Financials
*   **Payroll Summary**: Calculate total monthly salary expenditure.
*   **Asset Valuation**: Institutional view of total equity held in assets.
*   **Full Report**: Comprehensive dump of all system entities.

## Development

To extend the system:
1.  **Define Model**: Inherit from `Entity` in `Employees.py` or create a new base class.
2.  **Modularize UI**: Create a new `Menu.py` file for your module's logic.
3.  **Register Module**: Import and call your menu in `app.py`.

### Known Issues & Roadmap
- [ ] Implement `Delete Employee` logic in `EmployessMenu.py`.
- [ ] Implement `Calculate Depreciation` UI in `AssetsMenu.py`.
- [ ] Refactor `load_data` to ensure robust type-checking for software assets.

## License

This project is licensed under the MIT License - see the LICENSE file for details.