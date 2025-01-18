#############################################
version = 2.1                               #
# \/ \/ \/ CHANNGE YOUR PATH                #
path = "C:\\Users\\USERNAME\\FOLDERNAME"    #
# /\ /\ /\                                  #
#############################################

from time import sleep
import datetime
import os
import string
from random import randint

path = path + "\\MoneyCounter"

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
        os.makedirs(path + "\\data/money")
        os.makedirs(path + "\\data/account")
        f = open(path + "\\data/account/user.txt", "w")
        f2 = open(path + "\\data/money/value.txt", "w")
        f3 = open(path + "\\data/money/history.txt", "x")

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
        with open(path + "\\data/account/user.txt", "r") as f:
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
            print("MENU\n")
            with open(path + "\\data/money/value.txt", "r") as f:
                print(f"Kwota: {f.read()} zl")
            print("[1] Dodaj pieniadze.")
            print("[2] Odejmij pieniadze.")
            print("[3] Pokaż historie.")
            print("[4] Ustawienia.")

            command = input("\n[Podaj nr operacji] ")
            if command == "1":
                Bizness.AddValue()
            elif command == "2":
                Bizness.SubstractValue()
            elif command == "3":
                Bizness.PrintHistory()
            elif command == "4":
                Bizness.ShowSettings()
            
            else:
                print("[Nie rozpoznano komendy.]")
                Bizness.Menu(True)
    
    def AddValue():
        os.system("cls")
        value = float(input("[Podaj kwote] "))
        with open(path + "\\data/money/value.txt", "r") as fRead:
            fReadValue = fRead.read()
            with open(path + "\\data/money/value.txt", "w") as fWrite:
                fWrite.write(str(float(fReadValue) + value))
        Bizness.MakeHistory(value, input("[Podaj Tytul operacji] "))
        print("\n[Pomyslnie dodano kwote.]")
        sleep(3)
        Bizness.Menu(True)
    
    def SubstractValue():
        os.system("cls")
        value = float(input("[Podaj kwote] "))
        with open(path + "\\data/money/value.txt", "r") as fRead:
            fReadValue = fRead.read()
            with open(path + "\\data/money/value.txt", "w") as fWrite:
                fWrite.write(str(float(fReadValue) - value))
        Bizness.MakeHistory(- value, input("[Podaj Tytul operacji] "))
        print("\n[Pomyslnie odjeto kwote.]")
        sleep(3)
        Bizness.Menu(True)
    
    def PrintHistory():
        os.system("cls")
        
        with open(path + "\\data/money/history.txt", "r") as f:
            print(Coder(f.read()).Decode())
        
        input("[Enter]")
        Bizness.Menu(True)
    
    def MakeHistory(value, title):
        with open(path + "\\data/money/history.txt", "a") as f:
            x = f"Kwota: {value} zl, Data: {datetime.date.today()} {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}, Tytul: {title}\n"
            f.write(Coder(x).Encode())
            
    def ShowSettings():
        os.system("cls")
        print("USTAWIENIA\n")
        print("[1] Zmien nazwe uzytkownika.")
        print("[2] Zmien haslo.")
        print("[3] Reset programu.")
        print("[Enter] Powrot do menu.\n")
        
        option = input("[Podaj nr operacji] ")
        
        if option == "1":
            Settings.ChangeUsername()
        elif option == "2":
            Settings.ChangePassword()
        elif option == "3":
            Settings.Reset()
        else:
            Bizness.Menu(True)
        
    
class Settings():
    def ChangeUsername():
        os.system("cls")
        new_username = input("[Podaj nowa nazwe uzytkownika] ")
        print("\n[Czy zmienic nazwe uzytkownika?]")
        veryfy = (input("[tak / t / y / yes / 1] ")).upper()
        agree_chars = ["TAK", "T", "Y", "YES", "1"]
        if veryfy in agree_chars:
            with open(path + "\\data/account/user.txt", "r") as f:
                userDataUpdater = f.read().split("\n")
                with open(path + "\\data/account/user.txt", "w") as f2:
                    f2.write(f"{Coder(new_username).Encode()}\n{userDataUpdater[1]}")
                    print("[Zmieniono nazwe.]")
        else:
            print("\n[Nie udalo sie zmienic nazwy uzytkownika.]")
        
        input("\n[Enter]")
        Bizness.Menu(True)
    
    def ChangePassword():
        os.system("cls")
        new_password = input("[Podaj nowe haslo] ")
        print("\n[Czy zmienic haslo?]")
        veryfy = (input("[tak / t / y / yes / 1] ")).upper()
        agree_chars = ["TAK", "T", "Y", "YES", "1"]
        if veryfy in agree_chars:
            with open(path + "\\data/account/user.txt", "r") as f:
                userDataUpdater = f.read().split("\n")
                with open(path + "\\data/account/user.txt", "w") as f2:
                    f2.write(f"{userDataUpdater[0]}\n{Coder(new_password).Encode()}")
                    print("[Zmieniono haslo.]")
        else:
            print("\n[Nie udalo sie zmienic hasla.]")
        
        input("\n[Enter]")
        Bizness.Menu(True)
    
    def Reset():
        os.system("cls")
        print("[Czy zresetować program?]")
        print("[Wszystkie dane zostaną usuniete a program sie wyłączy i bedzie czekał na konfiguracje.]")
        veryfy = (input("\n[tak / t / y / yes / 1] ")).upper()
        agree_chars = ["TAK", "T", "Y", "YES", "1"]
        if veryfy in agree_chars:
            elements = ["\\data/money/history.txt",
                        "\\data/money/value.txt",
                        "\\data/account/user.txt",
                        "\\data/money",
                        "\\data/account",
                        "\\data"
                        ]
            for i in elements:
                if "." in i:
                    os.remove(path + i)
                else:
                    os.rmdir(path + i)
            os.rmdir(path)
        else:
            print("\n[Nie zresetowano danych!]")

            input("\n[Enter]")
            Bizness.Menu(True)

try:
    Main.FirstStart()
except FileExistsError:
    Bizness.Menu(Main.LogIn())
