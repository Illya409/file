with open("quotes.txt", "w", encoding = "UTF-8") as file:
    file.write(f"Садок вишневий коло хати,\n")
              (f"Хрущі над вишнями гудуть,\n")
              (f"Плугатарі з плугами йдуть,\n")
              (f"Співають ідучі дівчата,\n")
              (f"А матері вечерять ждуть.\n")
              
               


with open("quotes.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)

author = input("Хто написав ці рядки?")
with open("quotes.txt", "a", encoding = "UTF-8") as file:
    file.write(f"({author})\n")

while True:
    ans = input("Бажаєте додати цитату?  (так/ні)")
    if ans.lower() == "так":
        quote = input("Введіть цитату")
        author = input("Введіть автора")
        file = open("quotes.txt", "a", encoding = "UTF-8")
        file.write(f"{quote}\n{author}\n")
        file.close()
    else:
        break

with open("quotes.txt", "r", encoding = "UTF-8") as file:
    for line in file:
        print(line)









