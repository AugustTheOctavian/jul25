# def add(*numbers):
#   a = 0
#   while a == 0:
#     numbers = float(input("enter number: "))
#   a+=1
#   print(" : ")

#   sum = 0
#   for number in numbers:
#     sum += number

  
# add()


def add():
  sum = 0
  while True:
    number = input("enter number: [enter 'q' to quit] ")
    if number == 'q':
      break
    sum += float(number)
    print(sum)

add()
    