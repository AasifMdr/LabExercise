'''
Input the weight of a person in either kg or lbs.
If the person provides his/her
weight in kg then convert it into lbs
else convert it to kg.
'''

weight = int(input("Enter your weight: "))
kg_lbs = input("Is the weight in kg or lbs? (kg/lbs)?: ").upper()
if kg_lbs == "KG":
    convert_weight = float(2.205 * weight)
    print(f'The weight is in {convert_weight} lbs.')
elif kg_lbs == "LBS":
    convert_weight = float(weight / 2.205)
    print(f'The weight is in {convert_weight} kgs.')
else:
    print('The input is invalid.')