# Algorithm to identify best-selling product
 
sales = [100, 200, 150, 300, 250]

best_sale = 0
 
for sale in sales:        # loop modified

    if sale > best_sale:  # if condition

        best_sale = sale

    else:

        best_sale = best_sale
 
print("Best selling value:", best_sale)

 
