from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class BookInput(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Python Journey", "author": "A. Developer"},
    {"id": 2, "title": "APIs Made Simple", "author": "B. Engineer"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Books API"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(new_book: BookInput):
    next_id = max((book["id"] for book in books), default=0) + 1
    created_book = {
        "id": next_id,
        "title": new_book.title,
        "author": new_book.author,
    }
    books.append(created_book)
    return {"message": "Book created", "book": created_book}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            removed = books.pop(index)
            return {"message": "Book deleted", "book": removed}
    raise HTTPException(status_code=404, detail="Book not found")
