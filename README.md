# FastAPI Todo App

## Overview
This project is a simple yet comprehensive Todo application built using FastAPI and ScyllaDB. It serves as an excellent starting point for developers looking to familiarize themselves with FastAPI's capabilities and the NoSQL database ScyllaDB. This application allows users to create, read, update, and delete Todo items, demonstrating RESTful API principles.

## Features
- **CRUD Operations**: Create, Read, Update, and Delete Todo items.
- **User Authentication**: Secure endpoints with user authentication.
- **Asynchronous Support**: Fully asynchronous implementation for better performance.
- **Docker Support**: Easy deployment with Docker.
- **API Documentation**: Automatically generated interactive API documentation using Swagger UI.

## Tech Stack
- **Backend**: FastAPI
- **Database**: ScyllaDB
- **Containerization**: Docker
- **Documentation**: Swagger UI
- **Language**: Python

## Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdelbar472/fastapi_todo.git
   cd fastapi_todo
   ```
2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up ScyllaDB**:
   - Make sure you have ScyllaDB running locally or use a cloud instance.
   - Update the database connection settings in the `config.py` file.

## Usage Guidelines
1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```
2. **Access the API**:
   - Open your browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation.
3. **Use the API**:
   - You can use tools like Postman or curl to interact with the API endpoints.

## Contributing
Contributions are welcome! If you wish to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, please reach out to the author at [k.abdelbar128@gmail.com].

---

Thank you for checking out the FastAPI Todo App!
