
cp=int(input("Please enter the cost of the product before the margin "))
sp=int(input("Please enter the cost of the product after the margin "))
if cp<sp:
    print("The profit is ",sp-cp)
else:
    print("The loss is ", sp-cp)
