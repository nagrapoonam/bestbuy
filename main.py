import products
import store
import promotions

"""
function takes a 'store_obj' as a parameter and handles user interactions
"""
def start(store_obj):
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ")

        if choice == "1":
            print("------")
            products = store_obj.get_all_products()
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product.show()}")
            print("------")

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            while True:
                print("------")
                products = store_obj.get_all_products()
                for i, product in enumerate(products, start=1):
                    print(f"{i}. {product.show()}")
                print("------")

                product_choice = input("Which product # do you want? (Press Enter to finish order): ")
                if not product_choice:
                    break

                try:
                    product_choice = int(product_choice)
                    if product_choice < 1 or product_choice > len(products):
                        raise ValueError()
                    product = products[product_choice - 1]
                    quantity = int(input("What amount do you want? "))
                    shopping_list.append((product, quantity))
                    print("Product added to list!")
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")

            total_price = store_obj.order(shopping_list)
            print(f"Order placed successfully! Total price: ${total_price}")

        elif choice == "4":
            print("Thank you for using the store. Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

def main():
    # list of products
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity_limit=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    """
       It creates an instance of the Store class called 'best_buy', 
       passing the 'product list' as a parameter
       """
    best_buy = store.Store(product_list)
    start(best_buy)#to begin the store menu system


if __name__ == "__main__":
    main()
