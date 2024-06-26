#Q1.
product_data = {
    "name": "Lenevo Laptop",
    "default_code": "LP20032",
    "product_uom_id": 12,
}

# Rename key 'product_uom_id' to 'uom_id'
product_data["uom_id"] = product_data.pop('product_uom_id')

print("product_data =", product_data)


#Q2.

input_list = [40,35,20,87,10,90,25]

result = []

for ele in input_list:
    for i in range(len(result)):
        if ele >= result[i]:
            result.insert(i, ele)
            break
    else:
        result.append(ele)

print("Descending Order:", result)


