# lösenordshanterare
import os
import time
dictionary_with_info={}
list_with_websites=[]
# lägga allt i en fil?
def main():
    while True:
        os.system('cls')

        choice=input("""
1. Hitta lösenord från hemsida
2. Lägg till inloggning för ny hemsida
3. Visa lista med info på hemsidor
4. Ta bort lösenord fråm hemsida
""")

        if choice == "1":
            os.system('cls')

            search=input("Sök hemsida: ")
            for every in dictionary_with_info:
                if search.lower() in list_with_websites:
                    print(f"\nHemsida: {search.lower()}\nGmail: {every}\nLösenord: {dictionary_with_info[every]}")
                    break
                else:
                    print("Hemsidan hittades inte!")

        elif choice == "2":
            os.system('cls')

            while True:
                website = input("Hemsida: ")
                if website in list_with_websites:
                
                    print("Hemsidan finns redan!\n")
                    continue
                
                else:
                    list_with_websites.append((website.lower()))
                    break
                
            while True:
                new_gmail = input("Gmail: ")
                new_password = input("Lösenord: ")
                confirm_password = input("Bekräfta lösenord: ")
                
                if new_password == confirm_password:
                    dictionary_with_info[new_gmail] = new_password
                    print("Lösenorden har lagts till!")
                    time.sleep(2)
                    break
                
                else:
                    print("Lösenorden matchar inte!\n")
                    time.sleep(2)
                    continue
            

        elif choice == "3":
            os.system('cls')
            counter=0
            for each in dictionary_with_info:
                while True:
                    print("\nHemsida: "+list_with_websites[counter])
                    print(f"Gmail: {each}\nLösenord: {dictionary_with_info[each]}")
                    counter+=1
                    break
            
            input("\nTryck ENTER knapp för att gå till startsida\n")


        elif choice == "4":
            os.system('cls')

            while True:
                website_to_remove = input("Hemsida som raderas: ")
                confirm_website = input("Bekräfta hemsidan: ")
                if website_to_remove.lower() in list_with_websites:
                    if website_to_remove == confirm_website:
                        print(f"Är du säker på att du vill ta bort all information till {website_to_remove}?")
                        confirm = input("1. bekräfta\n2. avbryt\n")
                        if confirm == "1":
                            counter=0
                            for a in list_with_websites:
                                if website_to_remove.lower() == a:
                                    list_with_websites.remove(website_to_remove)
                                    key_to_remove = list(dictionary_with_info.keys())[counter]
                                    dictionary_with_info.pop(key_to_remove)
                                    print("Lösenorden har tagits bort!")
                                    time.sleep(2)
                                    break
                                
                                else:
                                    counter+=1                           
                            break
                        else:
                            break
                        
                    else:
                        print("Hemsidorna matchar inte")
                        break
                else:
                    print("Hemsidan hittas inte")
                    time.sleep(2)
                    break

if __name__ == "__main__":
    main()