# TODO Найдите количество книг, которое можно разместить на дискете
one_sim = 4
sym_stroka = 25
strok_str = 50
str_book = 100
bayt = 1509376
kod_stroka = one_sim * sym_stroka
kod_stanica = kod_stroka * strok_str
one_book = kod_stanica * str_book
kolichectvo = round(bayt/one_book,)


print("Количество книг, помещающихся на дискету:", kolichectvo)
