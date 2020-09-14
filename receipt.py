# create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

# declare ending message
message = "Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("*" + "\t\t{}".format(company_name.title()) + "\t\t *")
print("*" + "\t\t{}".format(company_address) + "\t\t *")
print("*" + "\t\t{}".format(company_city) + "\t\t\t *")

# print a line between sections
print("*" + "=" * 48 + "*")

# print out header for section of items
print("*" + "\tProduct Name \tProduct Price" + "\t\t *")

# create a print statement for each product
print("*" + "\t{}\t\t${}".format(p1_name.title(), p1_price) + "\t\t\t *")
print("*" + "\t{}\t${}".format(p2_name.title(), p2_price) + "\t\t\t *")
print("*" + "\t{}\t\t${}".format(p3_name.title(), p3_price) + "\t\t\t *")

# print a line between sections
print("*" + "=" * 48 + "*")

# print out header for section of total
print("*" + "\t\t\tTotal" + "\t\t\t *")

# calculate total price and print out
total = p1_price + p2_price + p3_price
print("*" + "\t\t\t${}".format(total) + "\t\t\t *")

# print a line between sections
print("*" + "=" * 48 + "*")

# output thank you message
print("*" + "\t\t\t\t\t\t *\n*\t{}\t *\n".format(message) + "*\t\t\t\t\t\t *")

# create a bottom border
print("*" * 50)