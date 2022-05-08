# ################################## HW4 ################################## #
"""
Zadani:
Vytvorte program hrajici hru "Padajici piskvorky" uzivatele proti pocitaci
(na planu zadane velikosti). Tato variace piskvorek se hraje na dvourozmernem
hracim planu. Hra je podobna klasickym piskvorkam s tim rozdilem, ze pokud
jste na tahu, nevolite konkretni ctverecek, do ktereho byste umistili svuj
symbol, ale sloupec. Symbol v danem sloupci spadne dolu (nejvice, co to jde).
Vyhrava ten, kdo posklada 4 sve symboly v rade, sloupci nebo diagonale.

Zadani:
Vasim ukolem je implementovat:
1) Funkci show_state(state), ktera vypise dany plan na standardni vystup.
Plan je reprezentovan seznamem seznamu stejne delky, ktere obsahuji znaky
X (krizek), O (kolecko) nebo mezera pro neobsazene pole.
>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'O'],
         [' ', ' ', ' ', ' ', 'X'], [' ', 'O', ' ', ' ', 'X']]
>> show_state(state)

        O
        X
  O     X
- - - - -
0 1 2 3 4

2) Funkci strategy(state, symbol), ktera pro dany plan a symbol vrati pozici
(sloupec) tahu pocitace. Neni nutne aby byla nejak sofistikovana, muze
vracet nahodny sloupec v danem rozsahu.

>> state = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', 'X', ' ']]
>> strategy(state, 'O')
2

3) Funkci tictactoe(rows, cols, human_starts=True), ktera umoznuje hrat hru
padajicich piskvorek na planu o danem poctu radku a sloupcu. Muzete
predpokladat, ze zadana velikost planu je rozumna (alespon 4 a mene nez 26
sloupcu a radku). Parametr human_starts urcuje, zda zacina hrac nebo pocitac.
Vypis prubehu hry by mel vypadat stejne, jako v nasledujicich prikladech.
Funkce kontroluje, zda jsou tahy zadane hracem a pocitacem platne a pokud
nejsou, vyzve ho k novemu zadani. Pro hru pocitace volejte vyse uvedene
funkce show_state(state) a strategy(state, symbol). Nezapomente, ze hra muze
skoncit i remizou

Priklad hry, v nemz zacina hrac:

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 5

          X
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 9

          X       O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 6

          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 5

          O
          X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 4

          O
        X X X     O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je pocitac
Pocitac hraje do sloupce cislo 7

          O
        X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9

Na tahu je hrac
Do jakeho sloupce chces hrat? (do 0 do 9)? 3

          O
      X X X X O   O
- - - - - - - - - -
0 1 2 3 4 5 6 7 8 9
Vyhral jsi!
"""

from random import randint
from typing import List
from time import sleep


# Funkce vypise dany plan na standardni vystup. Plan je reprezentovan seznamem
#  seznamu stejne delky, ktere obsahuji znaky X (krizek), O (kolecko) nebo
#  mezera pro neobsazene pole.

# :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera
def show_state(state: List[List[str]]) -> None:
    '''Funkce vypíše stav hry na obrazovku'''
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end=" ")
        print()

    for _ in range(len(state[0])):
        print("-", end=" ")
    print()

    for k in range(len(state[0])):
        print(k, end=" ")
    print()
    print()



# Funkce pro dany plan state a symbol chr vrati pozici (sloupec) tahu
# pocitace.

def valid_move(move: int, state: List[List[str]]) -> bool:
    '''vrací, zda je konkrétní sloupec plný nebo ne 
    (zda může být umístěn znak na zadané místo)'''
    for i in range(len(state[0])):
        for j in range(len(state)):
            if i == move and state[j][i] == " ":
                return True
    return False

#    :param state:  Seznam seznamu obsahujici znaky X, 0, a mezera
#    :param chr:    Znak, ktery se ma vlozit
#    :return:       Sloupec, do ktereho se ma vlozit znak chr
def strategy(state: List[List[str]], chr: str) -> int:
    '''Náhodná strategie pc -> vybírá náhodně číslo sloupce a 
    vrací číslo sloupce, do kterého je možné značku umístit'''
    move = randint(0, len(state[0]))
    while not valid_move(move, state):
        move = randint(0, len(state[0]))
    return move  


def human_picks_column(state: List[List[str]]) -> int:
    '''Zeptá se, do jakého sloupce chce člověk hrát a vrací číslo sloupce'''
    num_of_columns = len(state)
    move = int(input(f'Do jakého sloupce chcete hrát: (0 - {num_of_columns - 1}) '))
    while not valid_move(move, state):
        move = int(input(f'Sloupec už je plný nebo jste zadal číslo mimo rozsah, vyberte si jiný sloupec.\nDo jakého sloupce chcete hrát: (0 - {num_of_columns - 1}) '))
    return move


def creating_state(rows: int, cols: int) -> List[List[str]]:
    '''Na začátku hry vytváří prázdný plán hry'''
    state = []
    for _ in range(rows):
        state.append([" " for j in range(cols)])
    return state


def changing_state(state: List[List[str]], column: int, char: str) -> List[List[str]]:
    '''fce slouží na změnu stavu hry 
    (vrací plán se zapsanou značkou na daném místě)'''
    for i in range(len(state[0])):
        for j in range(len(state) - 1, -1, -1): # bere to listy v rámci listů
            # pozpátku (aby piškvorka spadla na nejnižší pozici). 
            # Do -1 je to proto, aby byl zahrnut i seznam č. 0
            if i == column and state[j][i] == " ":
                state[j][i] = char
                return state

def check_row(state: List[List[str]]) -> bool:
    '''Kontroluje, zda v řádku nejsou tři stejné znaky'''
    for i in range(len(state)):
        for j in range(len(state[i])):
            char = state[i][j]

            if char != " ":
                if j + 3 < len(state[i]) and state[i][j + 1] == char and \
                state[i][j + 2] == char and state[i][j + 3] == char:
                    return True
    return False


def check_column(state: List[List[str]]) -> bool:
    '''Kontroluje, zda se ve sloupci nenachází tři stejné znaky pod sebou'''
    for i in range(len(state)):
        for j in range(len(state[i])):
            char = state[i][j]

            if char != " ":
                if i + 3 < len(state) and state[i + 1][j] == char and \
                state[i + 2][j] == char and state[i + 3][j] == char:
                    return True
    return False


def check_diagonals(state: List[List[str]]) -> bool:
    '''Kontroluje, zda nejsou umístěny 4 stejné znaky diagonálně'''
    for i in range(len(state)):
        for j in range(len(state[i])):
            char = state[i][j]

            if char != " ":
                if i + 3 < len(state) and j + 3 < len(state[i]) and \
                    state[i + 1][j + 1] == char and state[i + 2][j + 2] == char \
                        and state[i + 3][j + 3] == char:
                        return True

                elif i + 3 < len(state) and j - 3 >= 0 and \
                    state[i + 1][j - 1] == char and state[i + 2][j - 2] == char \
                        and state[i + 3][j - 3] == char:
                        return True
    return False


def is_end(state: List[List[str]]) -> bool:
    '''Hlídá, zda již někdo neumístil 4 symboly - a tedy nevyhrál'''
    if check_row(state) or check_column(state) or check_diagonals(state):
        return True
    return False


def is_full(state: List[List[str]]) -> bool:
    '''Ověřuje, zda je herní plán již zaplněný'''
    for i in range(len(state)):
        if " " in state[i]:
            return False
    return True


def pc_move(state: List[List[str]]) -> List[List[str]]:
    '''Zajišťuje vše ohledně požadavků na tah PC - výpis, 
    zápis 'O' do plánu hry a výpis stavu hry'''

    print("Na tahu je počítač")
    pc_move = strategy(state, "O")

    print("Počítač přemýšlí ")
    for _ in range(2):
        print("▼")
        sleep(0.5)

    print("Počítač hraje do sloupce číslo", pc_move)
    state = changing_state(state, pc_move, "O")
    show_state(state)
    return state


def human_move(state: List[List[str]]) -> List[List[str]]:
    '''Zajišťuje vše ohledně požadavků tahu hráče - výpis, 
    zápis 'X' do plánu hry a výpis stavu hry'''

    print("Na tahu je hráč")
    human_move = human_picks_column(state)
    state = changing_state(state, human_move, "X")
    show_state(state)
    return state


# Funkce umoznuje hrat hru padajicich piskvorek na planu o danem poctu radku
# a sloupcu.

#   :param rows:    Pocet radku (4..25)
#   :param cols:    Pocet sloupcu (4..25)
#   :param human_starts: True, pokud zacina hrac, False jinak
def tictactoe(rows: int, cols: int, human_starts: bool = True) -> None:
    '''Hlavní funkce, řídící hru'''
    state = creating_state(rows, cols)
    while not is_end(state):
        if human_starts:
            state = human_move(state)
            human_starts = False
            if is_end(state):
                print("Vyhrál jste.")
                break
        elif not human_starts:
            state = pc_move(state)
            human_starts = True
            if is_end(state):
                print("Vyhrál počítač.")
                break
        if is_full(state):
            print("Hrací pole je plné - hra končí remízou.")
            break


if __name__ == '__main__':
    tictactoe(4, 4)