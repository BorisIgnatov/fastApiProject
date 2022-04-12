from fastapi import FastAPI
from sql.database import db_fetch, db_get_row, db_execute
from models import Book, Tag, Author
from sql.Serializers import BookSerializer
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books")
async def get_books(author_id: int | None, tag):
    query = "SELECT * FROM Book"
    books = await db_fetch(query)
    return books


@app.get("/books/{book_id}")
async def get_books(book_id: int):
    query = f"SELECT Book.id, Book.name, Book.author_id, Book.rating, Author.name as author_name FROM Book JOIN Author ON" \
            f" Author.id=Book.author_id WHERE Book.id = {book_id}"
    book = await db_get_row(query)
    serializer = BookSerializer(book)

    return serializer.to_representation()


@app.post("/books")
async def get_books(book: Book):
    query = f"INSERT INTO Book(name, author_id) VALUES('{book.name}', {book.author_id})"
    result = await db_fetch(query)
    return {"result": bool(result), "response": "ok" if result else "error"}


@app.put("/books/{book_id}")
async def update_books(book_id: int, book: Book):
    query = f"UPDATE Book SET name = '{book.name}', rating = {book.rating}, author_id = {book.author_id}" \
            f" WHERE id = {book_id}"
    result = await db_execute(query)
    return {"result": bool(result), "response": "ok" if result else "error"}

