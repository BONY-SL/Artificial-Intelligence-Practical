def return_bill_amount(price,amount_of_product):

    total_price = price*amount_of_product

    discount_price = price - (price * 2.5 / 100.0)

    last_price = discount_price * amount_of_product

    print("The total price is $",total_price)
    print("The discount price is $",discount_price)
    print("The last price is $",last_price)

get_product_price = float(input("Enter the product price: "))
get_amount_of_product = float(input("Enter the amount of product: "))
return_bill_amount(get_product_price,get_amount_of_product)
