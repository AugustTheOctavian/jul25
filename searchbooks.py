# create a list of dictionaries of bookname and title and return the index of the book title on user's input 


# searchTerm = input("enter the book name: ")
bookList = [
  {"title":"python"},
  {"title": "c"},
  {"title": "c k&r"},
  {"title": "cpp the hard way"},
  {"title": "Dune messiah"},
  {"title": "plato's republic"},
  {"title": "dune"},
  {"title": "pride and prejudice"},
  {"title": "Sophie's world"},
  {"title": "Moby Dick"},
]

titles = []
for book in bookList:
  titles.append(book['title'].lower())
""" for name in titles:
  print(name)
name = 'dune'

if name in titles:

  print(name)
  print(titles.index(n ame)-1)"""
bookname = input("enter book name : ").lower()

def searchbook(bookname):
  if bookname in titles:
    print("yes in "+str(titles.index(bookname) - 1)+"th place.")
  else:
    print("not found")
    print("here are the all available books")
    print('-'*50)
    for book in titles:
      print(book)

searchbook(bookname)







# for book in bookList:
#   if seachTerm in book["title"].lower():
#     print()
#   print(book["title"])

# for book in bookList:
#   while book["title"].contains == "dune":
#     print(book["title".index()])

# searchTerm = searchTerm.lower()
# def searchBook(searchTerm):
#   if searchTerm in bookList:
#     print("book was found")
#   else:
#     print("book wasn't found")

    
# searchBook(searchTerm)
