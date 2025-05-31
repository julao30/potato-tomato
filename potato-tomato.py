print()
print("Witaj drogi użytkowniku!")

imie= input("Podaj swoje imię: ")
print("Nazywasz się", imie,". Bardzo mi miło!")

print("Jedyne, o co Cię poproszę w tym programie, to o podanie swojego wieku.")
print()

def sprawdz_wiek(wiek):
    if wiek < 18:
        return "Jesteś niepełnoletni? A to Ci zaskoczenie :)"
    elif wiek < 65:
        return "Jesteś pełnoletni. Gratuluję!"
    else:
        return "Jesteś seniorem. To teraz masz luksus :)"

wiek = int(input("Podaj swój wiek: "))
print(sprawdz_wiek(wiek))

print()
print("To tyle z mojej strony. Dzięki za wypróbowanie mojego programu!")
