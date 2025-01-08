RKD Bank System
A banking system implemented using Python with a Tkinter GUI. This system allows users to perform various banking operations like account creation, balance check, deposit, withdrawal, transaction history, and more.

Features
Manager Login: Access manager-level functionalities like balance check, transaction history, and account management.
Customer Account Signup: Customers can sign up for a new bank account with essential details such as name, aadhar number, mobile number, etc.
Transaction History: Managers can view transaction history for a customer.
Balance Check: Both managers and customers can check their account balance.
Deposit and Withdraw: Managers can deposit and withdraw money from customer accounts.
Sign-up for Bank Application: Allows customers to sign up for the bank application.
Technologies Used
Python: The primary programming language.
Tkinter: For building the graphical user interface.
Pillow (PIL): For image handling in the GUI.
MySQL: To store customer data and transactions.
CSV: To log transaction details.
datetime: For handling time and date information.
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/rkd-bank.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database using MySQL:

Create a database named bank.
Create a table bank with appropriate fields (Account_No, First_Name, Last_Name, etc.).
Ensure that your MySQL username and password are correctly configured in the code.
Usage
Run the main application:

bash
Copy code
python main.py
The user can then:

Log in as a Manager or User.
Managers have access to account and transaction management.
Users can view their balance and perform transactions.
Screenshots
Main Screen

Account Creation

Deposit Window

Contribution
If you would like to contribute to this project, feel free to fork it, create a new branch, and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
