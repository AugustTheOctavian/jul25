import json
with open("books.json", "r") as file:
  books = json.load(file)


for book, author in books.items():
  print(book.lower(), author.title())