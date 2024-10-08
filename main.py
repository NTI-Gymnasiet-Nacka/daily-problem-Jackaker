# lösenordshanterare

dictionary_with_info={}
list_with_websites=[]

while True:
    choice=input("""
1. Hitta lösenord
2. Lägg till nytt lösenord
3. Visa lista på lösenord
4. Ta bort lösenord
""")

    if choice == "1":
        search=input("Sök hemsida: ")
        for int in dictionary_with_info:
            if search.lower() in list_with_websites:
                print(f"\nHemsida: {search.lower()}\nGmail: {int}\nLösenord: {dictionary_with_info[int]}")
                
            else:
                print("Hemsidan hittades inte!")

    elif choice == "2":
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
                break
            
            else:
                print("Lösenorden matchar inte!\n")
                continue
        

    elif choice == "3":
        for each in dictionary_with_info:
            for f in list_with_websites:
                print("\nHemsida: "+f)
                print(f"Gmail: {each}\nLösenord: {dictionary_with_info[each]}")
    

    elif choice == "4":
        while True:
            website_to_remove = input("Hemsida som raderas: ")
            confirm_website = input("Bekräfta hemsidan: ")
            if website_to_remove == confirm_website:
                print(f"Är du säker på att du vill ta bort all information till {website_to_remove}?")
                confirm = input("1. bekräfta\n2. avbryt\n")
                if confirm == "1":
                    counter=0
                    for a in list_with_websites:
                        if website_to_remove.lower() == a:
                            list_with_websites.pop(website_to_remove)
                            del dictionary_with_info[list(dictionary_with_info)(a)]
                        else:
                            counter+=1
                            
                
                else:
                    break
                
            else:
                print("Hemsidorna matchar inte")
                continue





# class dictionary_with_info_With_Two_Keys:
#     def __init__(self, epost, password):
#         self.e=epost
#         self.p=password
    
#     def __str__(self):
#         string="\n"
#         string+="\nE-post: "
#         string+=self.e
#         string+="\nLösenord: "
#         string+=self.p
#         string+="\n"
#         return string
    
# # print(dictionary_with_info_With_Two_Keys("ja@gmail.com", "password"))

# a=input("a")
# b=input("s")
# c=input("e")
# print(a)
# a = dictionary_with_info_With_Two_Keys(b,c)
# print(a)
