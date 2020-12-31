data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

def bmi_calculator(json_data):
    count = 0
    cal_data = []
    for data in json_data:
        bmi = round(data["WeightKg"]/(((data["HeightCm"])/100)**2),2) 
        if bmi <= 18.4:
            cal_data.append({"bmi_weight":bmi,"Category":"Underweight","Health risk":"Malnutrition risk"})
        elif 18.5 <= bmi <= 24.9:
            cal_data.append({"bmi_weight":bmi,"Category":"Normal weight","Health risk":"Low risk"})
        elif 25 <= bmi <= 29.9:
            cal_data.append({"bmi_weight":bmi,"Category":"Overweighterweight","Health risk":"Enhanced risk risk"})
            count += 1
        elif  30 <= bmi <= 34.9:
            cal_data.append({"bmi_weight":bmi,"Category":"Moderately obese","Health risk":"Medium risk"})
        elif 35 <= bmi <= 39.9:
            cal_data.append({"bmi_weight":bmi,"Category":"Severely obese","Health risk":"High risk"})
        elif bmi >= 40:
            cal_data.append({"bmi_weight":bmi,"Category":"Very severely obese","Health risk":"Very high risk"})

    return count,cal_data
overweight_count, details = bmi_calculator(data)
print ("Number of overweight people %s" %overweight_count)
print (details)


