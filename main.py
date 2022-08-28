#Descriptive analysis
import csv
age_list = []
sex_list = []
bmi_list = []
mwc_list = []
smoker_list =[]
charge_list = []
region_list = []
with open("insurance.csv") as insurance:
    data = csv.DictReader(insurance)
    for row in data:
     age_list.append(row['age'])
     sex_list.append(row['sex'])
     bmi_list.append(row['bmi'])
     mwc_list.append(row['children'])
     smoker_list.append(row['smoker'])
     charge_list.append(row['charges'])
     region_list.append((row['region']))

us_medical_data = zip(age_list,sex_list,bmi_list,
                      mwc_list,smoker_list,charge_list,region_list )
def average_age():
    total_age = 0
    for ages in range(0, len(age_list)):
        total_age = total_age + int(age_list[ages])
        avg_age = (total_age/len(age_list)) # The average age of the dataset
    print(f'The average age of the data set is {round(avg_age)}')
average_age()
#___________________________________________________________________
def analayzed_age():
    max_age =0
    min_age = 0
    for ages in age_list:
        if int(ages) > int(max_age):
            max_age = ages
    print(f'The maximum age of the dataset is {max_age}')
analayzed_age()

def average_bmi_weight():
    total_bmi = 0
    for bmis in range( 0, len(bmi_list)):
        total_bmi = total_bmi + float(bmi_list[bmis])
    print(f'The average bmi of the dataset is {round(total_bmi/len(bmi_list))}')
average_bmi_weight()

def analyze_weight():
    serve_obses = 0
    obese = 0
    over_weighted=0
    healthy_weighted=0
    under_weighted=0
    weight_data = zip(sex_list, age_list, bmi_list)
    for sex, age, bmis in weight_data:
       if float(bmis) >=40 :
           serve_obses +=1
       elif float(bmis) >30:
           obese +=1
       elif float(bmis) >=25:
           over_weighted+=1
       elif float(bmis) >= 18.5:
           healthy_weighted+=1
       elif float(bmis) <18.5:
           under_weighted+=1
    print(f"There is {serve_obses} members that are severely obese with an average {round(serve_obses/len(bmi_list)*100)}% of the dataset ")
    print(f'There is {obese} members that are obese with an average {round(obese/len(bmi_list),2)*100}% of the dataset')
    print(f'There is {over_weighted} members that are overweight with an average {round(over_weighted/len(bmi_list)*100)}% of the dataset')
    print(f'There is {healthy_weighted} members that healthy weight with an average {round(healthy_weighted/len(bmi_list)*100)}% of the dataset')
    print(f'There is {under_weighted} members that are underweight with an average {round(under_weighted/len(bmi_list)*100)}% of the dataset')
analyze_weight()

def analyzed_children():
    total_male_with_children = 0
    total_female_with_children = 0
    total_male_without_kids = 0
    total_female_without_kids = 0
    members_with_children = zip(sex_list,mwc_list)
    for sex, kids in members_with_children:
        if int(kids) > 0 and sex =='male':
            total_male_with_children +=1
        elif int(kids) >0 and sex == 'female':
            total_female_with_children +=1
        elif int(kids) ==0 and sex == 'male':
            total_male_without_kids +=1
        else:
            total_female_without_kids +=1
    print(f'The total number of males with children is {total_male_with_children} with an {round(total_male_with_children/len(mwc_list) *100)}% of the dataset, and the total number of females with children is {total_female_with_children} with an average {round(total_female_with_children/len(mwc_list)*100)}%')
    print(f'the total number of males without kids is {total_male_without_kids} with an {round(total_male_without_kids/len(mwc_list)*100)}% average, and the total number of females without kids is {total_female_without_kids} with an average {round(total_female_without_kids/len(mwc_list)*100)}%')
analyzed_children()
def analyzed_smokers():
    total_smokers_charges_list =[]
    total_nonsmokers_charges_list = []
    smokers_total_charges =0
    nonsmoker_total_charges = 0
    smokers_data = zip(smoker_list, charge_list)
    for smokers, charges in smokers_data:
        if smokers == "yes":
            total_smokers_charges_list.append(charges)
        elif smokers == "no":
            total_nonsmokers_charges_list.append(charges)
    for charge in total_smokers_charges_list:
         smokers_total_charges += float(charge)
    for charge in total_nonsmokers_charges_list:
        nonsmoker_total_charges+= float(charge)
    print(f'The average smoker insurance cost is ${round(smokers_total_charges/len(total_smokers_charges_list))}')
    print(f'The average non-smoker insurance cost is ${round(nonsmoker_total_charges/len(total_nonsmokers_charges_list))}')
    print('Smokers on average pay more about $23,616 more than non-smokers')
analyzed_smokers()

def analayzed_region():
    smokers_in_northwest=0
    smokers_in_northeast=0
    smokers_in_southwest=0
    smokers_in_southeast=0
    non_smokers_in_northwest = 0
    non_smokers_in_northeast = 0
    non_smokers_in_southwest = 0
    non_smokers_in_southeast = 0
    region_data = zip(smoker_list, region_list, charge_list)
    for smokers, region, charge in region_data:
        if smokers == "yes" and region =="northwest":
            smokers_in_northwest +=float(charge)
        elif smokers == "yes" and region == "northeast":
            smokers_in_northeast +=float(charge)
        elif smokers == "yes" and region == "southeast":
            smokers_in_southeast += float(charge)
        elif smokers == "yes" and region == "southwest":
            smokers_in_southwest+=float(charge)
        elif smokers == "no" and region == "northwest":
            non_smokers_in_northwest += float(charge)
        elif smokers == "no" and region == "northeast":
            non_smokers_in_northeast += float(charge)
        elif smokers == "no" and region == "southeast":
            non_smokers_in_southeast += float(charge)
        elif smokers == "no" and region == "southwest":
            non_smokers_in_southwest += float(charge)
        else:
            print("NA")
    print(f'The total insurance charges for smokers in the northwest region is ${round(smokers_in_northwest)}\nThe total insurance charges for smokers in the northeast region is ${round(smokers_in_northeast)}\nThe total insurance charges for smokers in the southeast region is ${round(smokers_in_southeast)}\nThe total insurance charges for smokers in the southwest region is ${round(smokers_in_southwest)}')
    print(f'The total insurance charges for non-smoker in the northwest region is ${round(non_smokers_in_northwest)}\nThe total insurance charges for non-smokers in the northeast region is ${round(non_smokers_in_northeast)}\nThe total insurance charges for non-smokers in the southeast region is ${round(non_smokers_in_southeast)}\nThe total insurance charges for non-smokers in the southwest region is ${round(non_smokers_in_southwest)}')
analayzed_region()




















