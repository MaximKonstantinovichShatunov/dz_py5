board =[0,1,2,3,4,5,6,7,8,9]

def print_ar(array):
   print(*array[1::])


def check(array):

   if array[1]==array[2]==array[3]:
      return  print(f'выиграли "{array[1]}"')

   elif array[4]==array[5]==array[6]:
      return print(f'выиграли "{array[3]}"')

   elif array[7]==array[8]==array[9]:
      return print(f'выиграли "{array[5]}"')

   elif array[1]==array[4]==array[7]:
      return print(f'выиграли "{array[1]}"')
   elif array[2]==array[5]==array[8]:
      return print(f'выиграли {array[2]}"')
   elif array[3]==array[6]==array[9]:
      return print(f'выиграли "{array[3]}"')

   elif array[1]==array[5]==array[9]:
      return print(f'выиграли "{array[1]}"')
   elif array[3]==array[5]==array[7]:
      return print(f'выиграли "{array[3]}"')
   else:
      return print_ar(board)
user=('X')
count=0
while count!=9:
   
   n=input(f'Куда поставите {user} ?')
   n=int(n)
   board[n]=user
   if user=="X":
      user="O"
   else:
      user='X'
   check(board)