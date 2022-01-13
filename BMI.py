def function(weight, Height):

    calculator = float(weight / Height / Height * 10000) # [weight (kg) / height (cm) / height (cm)] x 10,000

    if calculator <= 18 :
        print(f'your BMI result {calculator} (Underweight)')
    elif calculator >= 18 :
        print(f'Your BMI result {calculator} (Healthy weight)')    
    else:
        print(f"Your BMI result {calculator} (Overweight)")

function(55, 180)