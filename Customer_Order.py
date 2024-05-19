print("Welcome to our Restaurant! Here's the menu: ")
menu = {
    'pasta': 200,
    'chicken': 150,
    'coffee': 80,
    'fish':100,
    'beef':400,
    'mutton':600
}
for item,price in menu.items():
    print(f'{item} : {price}')

order_total = 0
maximum_order = 8

for _ in range(maximum_order):
      order = input("Enter your order (or type 'exit' to finish): ")
      if order == 'exit':
        break
      elif order in menu:
          order_total+=menu[order]
          print(f'Your order of {order} costs {menu[order]} and total cost {order_total}')
      else:
          print(f"Sorry ! {order} is not available.")
print(f"Your Total order is = {order_total}")
print("Thank you ! Come again.")






