high_school = input("Have you completed high school? (True/False): ").strip().lower() == 'true' 
bachelors= input("Have you completed a bachelor's degree? (True/False): ").strip().lower() == 'true'
if high_school  and bachelors:
    print("You are eligible for the job.")  
else:
    print("You are not eligible for the job.")      