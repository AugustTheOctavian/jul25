import json
with open("books.json", "r") as file:
  books = json.load(file)

print(type(books))
for book, author in books.items():
  print(book.upper() , author.title())