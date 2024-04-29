word = input("Please insert a sentence: ")
empty_list = []
new_word = word.lower()
for num in range(0, len(new_word)):
    if new_word[num] == 'a':
        empty_list.append('0')
    elif new_word[num] == 'b':
        empty_list.append(1)
    elif new_word[num] == 'c':
        empty_list.append(2)
    elif new_word[num] == 'd':
        empty_list.append(3)
    elif new_word[num] == 'e':
        empty_list.append(4)
    elif new_word[num] == 'f':
        empty_list.append(5)
    elif new_word[num] == 'g':
        empty_list.append(6)
    elif new_word[num] == 'h':
        empty_list.append(7)
    elif new_word[num] == 'i':
        empty_list.append(8)
    elif new_word[num] == 'j':
        empty_list.append(9)
    elif new_word[num] == 'k':
        empty_list.append(10)
    elif new_word[num] == 'l':
        empty_list.append(11)
    elif new_word[num] == 'm':
        empty_list.append(12)
    elif new_word[num] == 'n':
        empty_list.append(13)
    elif new_word[num] == 'o':
        empty_list.append(14)
    elif new_word[num] == 'p':
        empty_list.append(15)
    elif new_word[num] == 'q':
        empty_list.append(16)
    elif new_word[num] == 'r':
        empty_list.append(17)
    elif new_word[num] == 's':
        empty_list.append(18)
    elif new_word[num] == 't':
        empty_list.append(19)
    elif new_word[num] == 'u':
        empty_list.append(20)
    elif new_word[num] == 'v':
        empty_list.append(21)
    elif new_word[num] == 'w':
        empty_list.append(22)
    elif new_word[num] == 'x':
        empty_list.append(23)
    elif new_word[num] == 'y':
        empty_list.append(24)
    elif new_word[num] == 'z':
        empty_list.append(25)

key = (input("Please input the key: ")).lower()
key_list = []
def key_list_updater(coordinate):
    if key[coordinate] == 'a':
        key_list.append('0')
    elif key[coordinate] == 'b':
        key_list.append(1)
    elif key[coordinate] == 'c':
        key_list.append(2)
    elif key[coordinate] == 'd':
        key_list.append(3)
    elif key[coordinate] == 'e':
        key_list.append(4)
    elif key[coordinate] == 'f':
        key_list.append(5)
    elif key[coordinate] == 'g':
        key_list.append(6)
    elif key[coordinate] == 'h':
        key_list.append(7)
    elif key[coordinate] == 'i':
        key_list.append(8)
    elif key[coordinate] == 'j':
        key_list.append(9)
    elif key[coordinate] == 'k':
        key_list.append(10)
    elif key[coordinate] == 'l':
        key_list.append(11)
    elif key[coordinate] == 'm':
        key_list.append(12)
    elif key[coordinate] == 'n':
        key_list.append(13)
    elif key[coordinate] == 'o':
        key_list.append(14)
    elif key[coordinate] == 'p':
        key_list.append(15)
    elif key[coordinate] == 'q':
        key_list.append(16)
    elif key[coordinate] == 'r':
        key_list.append(17)
    elif key[coordinate] == 's':
        key_list.append(18)
    elif key[coordinate] == 't':
        key_list.append(19)
    elif key[coordinate] == 'u':
        key_list.append(20)
    elif key[coordinate] == 'v':
        key_list.append(21)
    elif key[coordinate] == 'w':
        key_list.append(22)
    elif key[coordinate] == 'x':
        key_list.append(23)
    elif key[coordinate] == 'y':
        key_list.append(24)
    elif key[coordinate] == 'z':
        key_list.append(25)

for num2 in range(0,len(new_word)):
    if num2 >= len(key):
        key_list_updater(num2%len(key))
    if num2 < len(key):
        key_list_updater(num2)

new_list = []
def new_list_updater(coordinate):
    if coordinate == 0:
        new_list.append('A')
    elif coordinate == 1:
        new_list.append('B')
    elif coordinate == 2:
        new_list.append('C')
    elif coordinate == 3:
        new_list.append('D')
    elif coordinate == 4:
        new_list.append('E')
    elif coordinate == 5:
        new_list.append('F')
    elif coordinate == 6:
        new_list.append('G')
    elif coordinate == 7:
        new_list.append('H')
    elif coordinate == 8:
        new_list.append('I')
    elif coordinate == 9:
        new_list.append('J')
    elif coordinate == 10:
        new_list.append('K')
    elif coordinate == 11:
        new_list.append('L')
    elif coordinate == 12:
        new_list.append('M')
    elif coordinate == 13:
        new_list.append('N')
    elif coordinate == 14:
        new_list.append('O')
    elif coordinate == 15:
        new_list.append('P')
    elif coordinate == 16:
        new_list.append('Q')
    elif coordinate == 17:
        new_list.append('R')
    elif coordinate == 18:
        new_list.append('S')
    elif coordinate == 19:
        new_list.append('T')
    elif coordinate == 20:
        new_list.append('U')
    elif coordinate == 21:
        new_list.append('V')
    elif coordinate == 22:
        new_list.append('W')
    elif coordinate == 23:
        new_list.append('X')
    elif coordinate == 24:
        new_list.append('Y')
    elif coordinate == 25:
        new_list.append('Z')

for elem in range(0, len(new_word)):
    new_elem = int(empty_list[elem]) + int(key_list[elem])
    if new_elem >= 26:
        coords = new_elem-26
        new_list_updater(coords)
    if new_elem < 26:
        new_list_updater(new_elem)
print(*new_list)