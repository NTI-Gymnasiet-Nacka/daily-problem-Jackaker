import os
import time

dict_with_info={}
list_with_websites=[]

def search_info():
    """
    Searching for existing websites to show its information
    
    Args:
        search (str): the searched website
    
    Returns:
        None
    """
    
    while True:
        os.system('cls')
        search = input("Sök hemsida: ")
        
        if search.lower() in list_with_websites:
            
            for every in dict_with_info:
                
                print(f"\nHemsida: {search.lower()}")
                print(f"Gmail: {every}")
                print(f"Lösenord: {dict_with_info[every]}")
                input("\nTryck ENTER knapp för att gå till startsida\n")
                break
            
            break
        
        else:
            print("Hemsidan hittades inte!")
            time.sleep(2)
            break


def add_info():
    """Add information to a new website
    
    Args:
        website (str): the website's name
        new_gmail (str): the gmail to that website
        new_password (str): the passwordto that website
        confirm_password (str): confirm password
          
    Returns:
        None
    """
    os.system('cls')

    while True:
        website = input("Hemsida: ")
        if website == "": 
            print("Ogiltig websida!")
            time.sleep(2)
            os.system('cls')
            continue
        
        elif website.lower() in list_with_websites:
            print("Hemsidan finns redan!")
            time.sleep(2)
            os.system('cls')
            continue
        
        else:
            list_with_websites.append((website.lower()))
            break
        
    while True:
        new_gmail = input("Gmail: ")
        new_password = input("Lösenord: ")
        confirm_password = input("Bekräfta lösenord: ")
        
        if new_password == confirm_password:
            dict_with_info[new_gmail] = new_password
            print("Lösenorden har lagts till!")
            time.sleep(2)
            break
        
        else:
            print("Lösenorden matchar inte!\n")
            time.sleep(2)
            continue


def show_all():
    """Show all website with information
    
    Args:
        None
        
    Returns:
        None
    """
    os.system('cls')
    counter=0
    
    for each in dict_with_info:
        
        while True:
            print("Lista på inloggningar")
            print("\nHemsida: "+list_with_websites[counter])
            print(f"Gmail: {each}\nLösenord: {dict_with_info[each]}")
            counter+=1
            break
    
    input("\nTryck ENTER knapp för att gå till startsida\n")


def remove_website():
    """Remove website with its information
    
    Args:
        website_to_remove (str): website to remove
        confirm_website (str): confirm website
        confirm (str): confirm action
    
    Returns:
        None
    """
    os.system('cls')

    while True:
        website_to_remove = input("Hemsida som raderas: ")
        confirm_website = input("Bekräfta hemsidan: ")
        
        if website_to_remove.lower() in list_with_websites:
            
            if website_to_remove == confirm_website:
                
                print(f"Bekräfta borttagning av {website_to_remove}?")
                confirm = input("1. bekräfta\n2. avbryt\n")
                
                if confirm == "1":
                    counter=0
                    
                    for a in list_with_websites:
                        
                        if website_to_remove.lower() == a:
                            list_with_websites.remove(website_to_remove)
                            remove = list(dict_with_info.keys())[counter]
                            dict_with_info.pop(remove)
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


def main():
    while True:
        os.system('cls')

        choice=input("""
1. Sök efter hemsida
2. Lägg till lösenord för ny hemsida
3. Visa lista med lösenord på hemsidor
4. Ta bort lösenord fråm hemsida
5. Avsluta(alla data försvinner)
""")

        if choice == "1":
            search_info()

        elif choice == "2":
            add_info()

        elif choice == "3":
            show_all()

        elif choice == "4":
            remove_website()
        
        elif choice == "5":
            break
        
        else:
            continue

if __name__ == "__main__":
    main()