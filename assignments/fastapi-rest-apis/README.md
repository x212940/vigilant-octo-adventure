# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a REST API using FastAPI and practice creating endpoints, validating request data, and returning structured JSON responses. By the end, you will have a small API service that supports core CRUD-style operations.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints for managing a simple in-memory list of books.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Implement `GET /` that returns a welcome message.
- Implement `GET /books` that returns all books as JSON.
- Implement `GET /books/{book_id}` that returns a single book by ID.
- Return a clear error message when a book ID is not found.


### 🛠️	Add Create and Delete Operations

#### Description
Expand your API by adding endpoints to create and delete books while validating incoming data.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data.
- Implement `POST /books` to add a new book with an auto-generated ID.
- Implement `DELETE /books/{book_id}` to remove a book by ID.
- Return appropriate JSON responses for successful create/delete actions.
- Keep all API responses clear and consistent for users.
