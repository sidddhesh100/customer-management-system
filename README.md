# Customer Management Platform

The Customer Management Platform is a web application built using Python, Django, MySQL, HTML, CSS, and Bootstrap. It is designed to provide functionalities similar to CRM platforms like Zoho. This platform allows users to store customer information in a database, create, delete, and update customer records, search for customer information using a multi-parameter search form, place and cancel orders, and includes login authentication and password reset functionality.

## Technologies Used

- Python
- Django
- MySQL
- HTML
- CSS
- Bootstrap

## Features

1. **Customer Information Storage**: The platform enables users to store customer information in the database, providing a centralized repository for easy access and management of customer data.

2. **Create, Update, and Delete Customers**: Users have the ability to create new customer records, update existing records, and delete customer records when necessary. This ensures accurate and up-to-date customer information.

3. **Multi-Parameter Search**: The platform includes a search form that allows users to search for customer information using multiple parameters such as name, email, phone number, etc. This makes it convenient to retrieve specific customer data based on various criteria.

4. **Order Placement and Cancellation**: Customers can place orders through the platform. They also have the ability to cancel their orders if needed, providing flexibility and convenience.

5. **Login Authentication**: The platform incorporates a secure login authentication system to control access and protect customer data from unauthorized users.

6. **Password Reset Functionality**: Users can easily reset their passwords in case they forget them, ensuring seamless access to the platform while maintaining security.

## Getting Started

To set up and run the Customer Management Platform, follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Configure the database settings in the `settings.py` file to connect to your MySQL database.

4. Apply the database migrations by running the following commands:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser account using the following command and follow the prompts:
   ```
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

7. Access the platform by visiting `http://localhost:8000` in your web browser.

## Usage

Once the Customer Management Platform is set up and running, users can perform the following actions:

- **Create Customer**: Users can add a new customer record to the database by clicking on the "Create Customer" button. They need to fill in the required information and submit the form to create the customer entry.

- **Update Customer**: To update customer information, users can click on the "Edit" button next to a customer's record. They can make the necessary changes and save the updated record.

- **Delete Customer**: If a customer needs to be removed from the database, users can click on the "Delete" button next to the customer's information and confirm the deletion.

- **Search Customers**: The search form allows users to search for customer information using multiple parameters. Users can enter the desired search criteria (e.g., name, email, phone number) and click the "Search" button to retrieve matching customer records.

- **Place Order**: Customers can place orders by following the designated process within the platform. They can provide the necessary order details and submit the order.

- **Cancel Order**: If customers wish to cancel an order, they can do so by accessing the order details and following the cancellation procedure.

- **Login**: Users need to log in to the platform using their credentials to access its features and functionalities. If

 they forget their password, they can utilize the password reset functionality to regain access.

## Contributions

Contributions to the Customer Management Platform are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## Acknowledgments

We would like to express our gratitude to the developers and contributors of Python, Django, MySQL, HTML, CSS, and Bootstrap for their remarkable work and support, which made the development of this platform possible.