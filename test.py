print( "Крестики-нолики")

доска = list(range(1,10))

def draw_board(доска):
   print("-" * 13)
   for i in range(3):
      print("|", доска[0+i*3], "|", доска[1+i*3], "|", доска[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      ответ_игрока = input("Выберите клетку " + player_token+"? ")
      try:
         ответ_игрока = int(ответ_игрока)
      except:
         print("Ошибка! Вы уверены, что ввели корректное число?")
         continue
      if ответ_игрока >= 1 and ответ_игрока <= 9:
         if(str(доска[ответ_игрока-1]) not in "XO"):
            доска[ответ_игрока-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(доска):
   условия_для_победы = ((1,4,7), (0,4,8), (2,4,6), (0,3,6), (0,1,2), (2,5,8), (3,4,5), (6,7,8))
   for each in условия_для_победы:
       if доска[each[0]] == доска[each[1]] == доска[each[2]]:
          return доска[each[0]]
   return False

def main(доска):
    count = 0
    win = False
    while not win:
        draw_board(доска)
        if count % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        count += 1
        if count > 4:
           tmp = check_win(доска)
           if tmp:
              print(tmp, "Ура,Победа!")
              win = True
              break
        if count == 9:
            print("Ничья!")
            break
    draw_board(доска)
main(доска)

input("Нажмите Enter для выхода!")