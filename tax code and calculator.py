'''
Program that determines tax code and income tax on your annual salary
Author: Anirudh Revathi
'''

def main():
    
    def income_total():
        
        income_total = int(input("Total annual income ammounts to: "))
        return income_total    

    def student_loan():

        student_loan = input("Do you have a student loan? Yes/No ")
        return student_loan
    
    def type_income():

        no_income = input("Do you have more than one income? ")
        type_of_income = ""
        if no_income == "Yes":
            question_source = input("Do you receive income tested benefit? ")
            if question_source == "Yes":
                benefit_question = input("Is the tax code for income tested benefit? ")
                if benefit_question == "Yes":
                    type_of_income = "Benefit"
                
                elif benefit_question == "No":
                    type_of_income = "Secondary Income"

            elif question_source == "No":
                code_type = input("Is this tax code for your main or a secondary income? ")
                return code_type
                
            return type_of_income


        elif no_income == "No":
            return "Main Income"
        
    def tax_rate(income_annual):
        if income_annual <= 14000:
            return income_total * 10.5 / 100
        elif 14001 <= income_annual <= 48000:
            return 14000 * 10.5 / 100 + ((income_annual - 14000) * 17.5 / 100)  
        elif 48001 <= income_annual <= 70000:
            return (14000 * 10.5 / 100) + (34000 * 17.5 / 100) + ((income_annual - 48000) * 30/100) 
        elif 70001 <= income_annual <= 180000:
            return (14000 * 10.5 / 100) + (34000 * 17.5 / 100) + (22000 * 30/100) + ((income_annual - 70000) * 33 / 100) 
        elif income_annual > 180000:
            return (14000 * 10.5 / 100) + (34000 * 17.5 / 100) + (22000 * 30/100) + (1100000 * 33 / 100) + ((income_annual - 180000) * 39 / 100)

        
    def tax_type(income_type, education_loan, income_annual, total_tax):



        if education_loan == "No":    
            if income_type == "Benefit":
                print(f"Tax code for benefit received is M, and your total income tax for your annual inomce of  {income_annual} is {total_tax}")

            elif income_type == "Main Income":
                print(f"Tax code for your source of income is M, and your total income tax for your annual inomce of  {income_annual} is {total_tax}")

            elif income_type == "Secondary Income":
                if income_annual <= 14000:
                    print(f"Your tax code is \n 'SB' and and your total income tax for your annual inomce of  {income_annual} is {total_tax}")
                elif 14001 <= income_annual <= 48000:
                    print(f"Your tax code is \n 'S' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")  
                elif 48001 <= income_annual <= 70000:
                    print(f"Your tax code is \n 'SH' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")
                elif 70001 <= income_annual <= 180000:
                    print(f"Your tax code is \n 'ST' and your total income tax for your annual inomce of  {income_annual} is {total_tax}") 
                elif income_annual > 180000:
                    print(f"Your tax code is \n 'SA' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")

        elif education_loan == "Yes":    
            if income_type == "Benefit":
                print(f"Tax code for benefit received is 'M SL', and your total income tax for your annual inomce of  {income_annual} is {total_tax}")

            elif income_type == "Main Income":
                print(f"Tax code for your source of income is 'M SL', and your total income tax for your annual inomce of  {income_annual} is {total_tax}")

            elif income_type == "Secondary Income":
                if income_annual <= 14000:
                    print(f"Your tax code is \n 'SB SL' and and your total income tax for your annual inomce of  {income_annual} is {total_tax}")
                elif 14001 <= income_annual <= 48000:
                    print(f"Your tax code is \n 'S SL' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")  
                elif 48001 <= income_annual <= 70000:
                    print(f"Your tax code is \n 'SH SL' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")
                elif 70001 <= income_annual <= 180000:
                    print(f"Your tax code is \n 'ST SL' and your total income tax for your annual inomce of  {income_annual} is {total_tax}") 
                elif income_annual > 180000:
                    print(f"Your tax code is \n 'SA SL' and your total income tax for your annual inomce of  {income_annual} is {total_tax}")
                
        
                

        
    income_annual = income_total()
    education_loan = student_loan()
    income_type = type_income()
    total_tax = tax_rate(income_annual)
    tax_type(income_type, education_loan, income_annual, total_tax)
main()
