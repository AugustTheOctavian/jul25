import json
with open("books.json", "r") as file:
  books = json.load(file)

  
# booksearch = input("enter book name: ").lower()
# if booksearch in books:
#   print(booksearch, books["booksearch"])

lowercasebooks = []
  
for book in books:
  lowercasebooks.append(book)
print(lowercasebooks)

searchbook = input("enter book: ").lower()
if searchbook in lowercasebooks:
  print(f"yes, found  at {lowercasebooks.index(searchbook)+1}.")

# # print(books)
# for book in books:
#   print(book.lower().replace(' ',''))

# searchbook = input("enter a book: ").lower()
# if searchbook in books:
#   print(searchbook)

  
