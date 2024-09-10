from time import sleep
import datetime
import os
import string
from random import randint

class Coder():
    def __init__(self, chars):
        self.chars = str(chars)
        self.code = string.ascii_letters + string.digits
    def Encode(self):
        key = ""
        rezult = ""
        for i in self.chars:
            key = self.code[randint(0, len(self.code) - 1)]
            rezult = rezult + i + key
        return rezult
    def Decode(self):
        y = 0
        rezult = ""
        for i in self.chars:
            if y % 2 == 0:
                rezult = rezult + i
            else:
                rezult = rezult
            y += 1
        return rezult
    
class Main():
    def FirstStart():
        os.makedirs("data/money")
        os.makedirs("data/account")
        f = open("data/account/user.txt", "w")
        f2 = open("data/money/value.txt", "w")
        f3 = open("data/money/history.txt", "x")

        print("Projektowanie folderow i plikow.", end="\r")
        print("Pomyslnie utworzono pliki i foldery", end="\n")
        sleep(3)

        os.system("cls")

        print("Utworz konto:", end="\n")
        user = str(input("Login: "))
        password = str(input("Haslo: "))
        f.write(f"{Coder(user).Encode()}\n{Coder(password).Encode()}")
        print("Pomyslnie utworzono i zaszyfrowano dane.")
        sleep(3)

        os.system("cls")
        f2.write("0")
        f.close()
        f2.close()
        f3.close()

        print("Program zamknie sie za 3s.")
        sleep(3)
    
    def LogIn() -> bool:
        with open("data/account/user.txt", "r") as f:
            userData = f.read().split("\n")
            user = Coder(userData[0]).Decode()
            password = Coder(userData[1]).Decode()
        user_logging = str(input("Podaj login: "))
        password_logging = str(input("Podaj haslo: "))

        if user_logging == user and password_logging == password:
            print("Zalogowano pomyslnie")
            sleep(3)
            return True
        else:
            print("Nie zalogowano pomyslnie")
            sleep(3)
            return False
        
class Bizness():
    def Menu(logged):
        if logged:
            os.system("cls")
            print("Aplikacja Konsolowa Biznes")
            with open("data/money/value.txt", "r") as f:
                print(f"Kwota: {f.read()} zl")
            print("[1] Dodaj pieniadze.")
            print("[2] Odejmij pieniadze.")
            print("[3] Pokaż historie.")

            command = input("Operacja: ")
            if command == "1":
                Bizness.AddValue()
            elif command == "2":
                Bizness.SubstractValue()
            elif command == "3":
                Bizness.PrintHistory()
            else:
                print("Nie rozpoznano komendy.")
                Bizness.Menu(True)
    
    def AddValue():
        os.system("cls")
        value = float(input("Podaj kwote: "))
        with open("data/money/value.txt", "r") as fRead:
            fReadValue = fRead.read()
            with open("data/money/value.txt", "w") as fWrite:
                fWrite.write(str(float(fReadValue) + value))
        Bizness.MakeHistory(value, input("Podaj Tytul operacji: "))
        print("Pomyslnie dodano kwote.")
        sleep(3)
        Bizness.Menu(True)
    
    def SubstractValue():
        os.system("cls")
        value = float(input("Podaj kwote: "))
        with open("data/money/value.txt", "r") as fRead:
            fReadValue = fRead.read()
            with open("data/money/value.txt", "w") as fWrite:
                fWrite.write(str(float(fReadValue) - value))
        Bizness.MakeHistory(- value, input("Podaj Tytul operacji: "))
        print("Pomyslnie odjeto kwote.")
        sleep(3)
        Bizness.Menu(True)
    
    def PrintHistory():
        os.system("cls")
        
        with open("data/money/history.txt", "r") as f:
            print(Coder(f.read()).Decode())
        
        input("[Enter]")
        Bizness.Menu(True)
    
    def MakeHistory(value, title):
        with open("data/money/history.txt", "a") as f:
            x = f"Kwota: {value} zl, Data: {datetime.date.today()} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}, Tytul: {title}\n"
            f.write(Coder(x).Encode())

try:
    Main.FirstStart()
except FileExistsError:
    Bizness.Menu(Main.LogIn())