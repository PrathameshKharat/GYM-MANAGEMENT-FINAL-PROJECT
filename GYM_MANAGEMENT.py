class EdYoda_Gym:
    def __init__(self):
        print(" !!WelCome To Gym!! ")
        print(' ')

    def Member(self):
        value = True
        while value:
            print("#################################################")
            print("  ")
            print('''Press 1: Register
Press 0: Exit
                     ''')
            print("  ")
            input1 = input("Please Enter Your Response: ")
            print("  ")
            if input1 == '1':
                print("  ")
                print("#################################################")
                self.Register()

            elif input1 == '0':
                print("Visit Again")
                value = False

    ################################################################################

    def SuperUser(self):
        value1 = True
        while value1:
            print("####################################################")
            print("\n")
            print('''Press 1: Create Member
 Press 2: View Members
 Press 3: Delete Member
 Press 4: Update Member
 Press 5: Create Regimen
 Press 6: View Regimens
 Press 7: Delete Regimen
 Press 8: Update Regimen
 Press 0: Exit''')
            print("  ")
            input2 = input("Please Enter Your Response: ")
            print("  ")
            if input2 == '1':
                print("  ")
                print("#################################################")
                self.Register()
            if input2 == '2':
                print("  ")
                print("#################################################")
                self.View()
            if input2 == '3':
                print("  ")
                print("#################################################")
                self.Delete()
            if input2 == '4':
                print("  ")
                print("#################################################")
                self.Update()
            if input2 == '5':
                print("  ")
                print("#################################################")
                self.Create_Regimen()
            if input2 == '6':
                print("  ")
                print("#################################################")
                self.View_Regimen()
            if input2 == '7':
                print("  ")
                print("#################################################")
                self.Delete_Regimen()
            if input2 == '8':
                print("  ")
                print("#################################################")
                self.Update_Regimen()
            if input2 == '0':
                print("  ")
                print("See You Soon")
                value1 = False

    ##################################################################################################

    users = [['Name', 'Age', 'Gender', 'Contact', 'Email', 'BMI registerd', 'Membership Duration'],
             ['Trainer', '30', 'M', '123456', 'traineradmin', '40', '12'],
             ['Pratham', '21', 'M', '1234', 'pratham@gmail.com', '24', '6'],
             ['PK', '22', 'M', '9876', 'pk@gmail.com', '32', '9'],
             ['CSK', '28', 'M', '98765', 'ck@gmail.com', '12', '12']]

    Regimen_Table = {
        'Set1': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Rest', 'Thu': 'Back', 'Fri': 'Triceps', 'Sat': 'Rest',
                 'Sun': 'Rest'},
        'Set2': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio/Abs', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Rest'},
        'Set3': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Abs/Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Legs', 'Sun': 'Cardio'},
        'Set4': {'Mon': 'Chest', 'Tue': 'Biceps', 'Wed': 'Cardio', 'Thu': 'Back', 'Fri': 'Triceps',
                 'Sat': 'Cardio',
                 'Sun': 'Cardio'}}

    def Register(self):
        Name = input("Enter Your name: ")
        Age = input("Enter Your age: ")
        Gender = input("Enter Your Gender: ")
        Contact = input("Enter Your PhoneNumber: ")
        Email = input("Enter Your Email: ")
        BMI = input("Enter Your BMI: ")
        Duration = input("Enter Your Membership Duration: ")
        role = 'Member'

        self.users.append([Name, Age, Gender, Contact, Email, BMI, Duration])

        print("Member name: ", Name + " Age: ", Age + " BMI: ", BMI)

        if BMI < '18.5':
            print('''Your Regimen is:
■	Mon: Chest
■	Tue: Biceps
■	Wed: Rest
■	Thu: Back
■	Fri: Triceps
■	Sat: Rest
■	Sun: Rest
                  ''')

        elif BMI < '25':
            print('''Your Regimen is:
■	Mon: Chest
■	Tue: Biceps
■	Wed: Cardio/Abs
■	Thu: Back
■	Fri: Triceps
■	Sat: Legs
■	Sun: Rest
''')

        elif BMI < '30':
            print('''Your Regime is:
■	Mon: Chest
■	Tue: Biceps
■	Wed: Abs/Cardio
■	Thu: Back
■	Fri: Triceps
■	Sat: Legs
■	Sun: Cardio
''')
        elif BMI > '30':
            print('''Your Regime is:
■	Mon: Chest
■	Tue: Biceps
■	Wed: Cardio
■	Thu: Back
■	Fri: Triceps
■	Sat: Cardio
■	Sun: Cardio

''')
        else:
            print("Enter Correct Information!!")

    #####################################################################################################

    def View(self):
        for i in self.users:
            print(i)

    def Delete(self):
        for i in self.users:
            print(i)
        ch_ph = input("Enter member phone number to delete:  ")
        for i in range(len(self.users)):
            if ch_ph in self.users[i]:
                removed = self.users.pop(i)
                print("Member deleted")
        else:
            print("Member not found")

    def Update(self):
        inp6 = input("Enter contact number of member: ")
        for i in range(len(self.users)):
            if inp6 in self.users[i]:

                print("\n Welcome SuperUSer  ")
                inp7 = input('''Press 1: To Revoke
Press 2: To Extend''')
                if inp7 == '1':
                    self.users[-1][i] = 0
                    print("Membership revoked")
                else:
                    self.users[-1][i] = input("Enter number of months of Extension: ")
                    print(f"Membership has been extended!! Enjoy your services")

    def Create_Regimen(self):
        tempelate = {'Mon': '', 'Tue': '', 'Wed': '', 'Thu': '', 'Fri': '', 'Sat': '', 'Sun': ''}
        print(" ")
        regimen_name = input("Please enter the name of new regimen: ")
        while regimen_name in self.Regimen_Table:
            print("Regimen name already exists!")
            new_regimen = input("Please enter the name of new regimen: ")
        else:
            self.Regimen_Table[regimen_name] = tempelate
            for i in self.Regimen_Table[regimen_name]:
                self.Regimen_Table[regimen_name][i] = input(f"Please enter workout for {i}: ")
            print(" ")
            print("New Workout Regimen Added Successfully!")
            print(" ")
            print("New Regimen seems like:- " + regimen_name)
            for j in self.Regimen_Table[regimen_name]:
                print(f"{j}:{self.Regimen_Table[regimen_name][j]}")

    def View_Regimen(self):

        print(" ")
        for i in self.Regimen_Table:
            print(i)
        print(" ")
        name = input("Please enter name of Regimen: ")
        if name in self.Regimen_Table:
            print(f'Workout for {name} is: ')
            for j in self.Regimen_Table[name]:
                print(f'{j}: {self.Regimen_Table[name][j]}')
        else:
            print("Incorrect Regimen Name entered!")

    def Delete_Regimen(self):
        delete_reg = input("Please enter name of Regimen to delete: ")
        if delete_reg in self.Regimen_Table:
            del self.Regimen_Table[delete_reg]
            print(f"{delete_reg} Deleted Successfully")
        else:
            print("Sorry! Workout Regimen not found!")

    def Update_Regimen(self):
        print("Here are names of all sets as per created and scheduled ! ! !")
        list_num2 = 1
        for names in self.Regimen_Table:
            print(f'{list_num2}: {names}')
            list_num2 += 1
        regimen_name = input("Please enter the name of regimen set to update: ")
        if regimen_name in self.Regimen_Table:
            print(f"Update Workout for {regimen_name}: ")
            for i in self.Regimen_Table[regimen_name]:
                self.Regimen_Table[regimen_name][i] = input(f"Update for {i}: ")
            print('Updated Regimen is:')
            for j in self.Regimen_Table[regimen_name]:
                print(f'{j}: {self.Regimen_Table[regimen_name][j]}')
        else:
            print("||Regimen not found! Please Enter correct name of regimen set ||")


a = EdYoda_Gym()
# #Please create objects as per requirements as if I declare one now it will not store multiple values for giving example I
# am creating 2 variables i.e s for member operations and a for superuser operations
a.SuperUser()