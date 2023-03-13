import csv

def menu():
    print("***** PIZZA MEL *****")
    print("1. Classic Pizza - 8.99$")
    print("2. Neapolitan Pizza - 10.99$")
    print("3. Turk Pizza - 19.99$")
    print("4. Chicago Pizza - 12.99$")
    print("5. Greek Pizza - 9.99$")
    print("6. California Pizza - 15.99$")
    print("7. Exit")

def main():
    total_price = 0
    order_list = []
    while True:
        menu()
        choice_pizza = int(input("Pizza seçin (1-6) veya çıkmak için 7'e basın: "))
       
        if choice_pizza == 1:
            pizza_name = "Classic Pizza"
            pizza_price = 8.99
        elif choice_pizza == 2:
            pizza_name = "Neapolitan Pizza"
            pizza_price = 19.99
        elif choice_pizza == 3:
            pizza_name = "Turk Pizza"
            pizza_price = 19.99
        elif choice_pizza == 4:
            pizza_name = "Chicago Pizza"
            pizza_price = 12.99
        elif choice_pizza == 5:
            pizza_name = "Greek Pizza"
            pizza_price = 9.99
        elif choice_pizza == 6:
            pizza_name = "California Pizza"
            pizza_price = 15.99
        else:
            choice_pizza == 7
            break
        
        choice_sauce = input("""
              ***** Sos veya yan ürün seçiniz *****
              A. Yogurt Sauce
              B. GarlicBread
              C. Mexican Sauce
              D. No
              """)
            if choice_sauce == "A" or choice == "a":
            sauce_name = "Yogurt Sauce"
            sauce_price = 2.99
            elif choice_sauce == "B" or choice == "b":
            sauce_name = "Garlic Bread"
            sauce_price = 5.99
            elif choice_sauce == "C" or choice == "c":
            sauce_name = "Mexican Sauce"
            sauce_price = 2.99 
            else:
                choice_sauce == "D" or choice == "d"
                break
            
        
        
        order_description = pizza_name + " - " + choice_sauce + " sos"
        total_price += pizza_price
        
        order = {}
        order["Name"] = input("Adınız: ")
        order["ID"] = input("TC Kimlik Numaranız: ")
        order["Card Number"] = input("Kredi Kartı Numaranız: ")
        order["Card Password"] = input("Kredi Kartı Şifreniz: ")
        order["Order Description"] = order_description
        order["Order Time"] = "placeholder" # bu kısım siparişin tarih/saatini tutacak, ama şimdilik boş bırakıyoruz
        order_list.append(order)
        
        print("Toplam fiyat: " + str(total_price) + " TL")
        
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "ID", "Card Number", "Card Password", "Order Description", "Order Time"])
        writer.writerows(order_list)

if __name__ == "__main__":
    main()

#Kodları düzenlemek için vaktim kalmadı :(

