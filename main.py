'''We would like to keep a record of medical patients and their insurance costs.
First, create an empty dictionary called'''
medical_costs = {}

'''Let’s populate our medical_costs dictionary by adding the following key-value pairs:'''
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0

'''Using one line of code, add the following three patients to the medical_costs dictionary'''
medical_costs.update({"Connie": 8886.0, "Issac": 16444.0, "Valentina":6420.0})

'''You notice that Vinay’s insurance cost was incorrectly inputted. Update the value associated with Vinay to 3325.0.'''
medical_costs.update({"Vinay": 3325})
'''
Let’s calculate the average medical cost of each patient. Create a variable called total_cost and set it equal to 0.'''
total_cost = 0
for cost in medical_costs.values():
    total_cost += cost
    '''After the loop, create a variable called average_cost that stores the total_cost divided by the length of the medical_costs dictionary.'''
average_cost = total_cost/len(medical_costs)
# print(f'Average Insurance Cost: {average_cost}')

'''You have been asked to create a second dictionary that maps patient names to their ages.'''
names = ['Marina', 'Vinay', 'Connie','Isaac', 'Valentina']
ages = [27, 24, 43,35,52]
'''Next, create a variable called zipped_ages that is a zipped list of pairs between the names list and the ages list.'''
zipped_ages = zip(names,ages)

'''Create a dictionary called names_to_ages by using a list comprehension that iterates through zipped_ages and turns each pair into a key : value item.'''
names_to_ages = {key:value for key, value in zipped_ages}
# print(names_to_ages)

'''Use .get() to get the value of Marina’s age and store it in a variable called marina_age. Use None as a default value if the key doesn’t exist.'''
marina_age =names_to_ages.get("Marina", None)
# print(f"Marina's age is {marina_age}")

'''Let’s create a third dictionary to represent a database of medical records that contains information such as a patient’s name, age, sex, gender, BMI, number of children, smoker status, and insurance cost.'''
medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Issac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420}
# print(medical_records)
# print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")
# medical_records.pop("Vinay")
# print(medical_records)
for key, value in medical_records.items():

 print(f"{key} is a {medical_records[key]['Age']} year old {medical_records[key]['Sex']} {medical_records[key]['Smoker']} with a BMI of {medical_records[key]['BMI']} and insurance cost of {medical_records[key]['Insurance_cost']}")