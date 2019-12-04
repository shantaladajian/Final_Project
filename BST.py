import json
import os

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,name):
        tmp= self.head
        if tmp == None:
            self.head=User(name)
        else:
            while tmp.next!=None:
                tmp=tmp.next
            tmp.next=User(name)

    def find(self,name):
        tmp= self.head
        while tmp != None:
            if tmp.isEqual(name):
                return tmp
            tmp=tmp.next
        return None

class BST:
    def __init__(self):
        self.root = None

    def changetoAscii(self,name):
        ascii = 0
        for letter in name:
            ascii = ord(letter) + ascii
        return int(ascii)

    def add(self,name):
        if self.root == None:
            self.root = User(name)
            self.root.ID=self.changetoAscii(name)
        else:
            self._add(name, self.root)

    def _add(self,name, node):
        ID=self.changetoAscii(name)
        if ID < node.ID:
            if node.left == None:
                node.left = User(name)
            else:
                self._add(name, node.left)
        elif ID > node.ID:
            if node.right == None:
                node.right = User(name)
            else:
                self._add(name,node.right)

    def printNodes(self,node):
        if node != None:
            self.printNodes(node.left)
            print(str(node.name))
            self.printNodes(node.right)

    def printBST(self):
        tmp=self.root
        self.printNodes(tmp)

class UserManager:
    def __init__(self):
        self.users=LinkedList()
        self.BSTusers=BST()

    def loadAllUsers(self):
        availableFiles = os.listdir()
        if "users.json" in availableFiles:
            with open("users.json") as file:
                users = json.load(file)
                for key in users:
                    self.users.add(key)
                    self.BSTusers.add(key)
                    user= self.users.find(key)
                    user.setData(users[key])

    def CreatUsername(self):
        username=input("\nPlease type a username you'd like to have :)")
        while True:
            if self.users.find(username)!=None:
                print("Please input another username as this one already exists :)\n")
            else:
                return username

    def saveAllUsers(self):
        file = open('users.json', 'w')
        usersJSON = {}
        tmp = self.users.head
        while tmp != None:
            usersJSON[tmp.name] = tmp.toJSON()
            tmp = tmp.next
        file.write(json.dumps(usersJSON))
        file.close()

    def addUser(self, user):
        self.users.add(user)
        self.BSTusers.add(user)

    def checkifNameexists(self, name):
        if self.users.find(name)!=None:
            return True
        else:
            return False

    def displayAllUsers(self):
        tmp = self.users.head
        while tmp != None:
            tmp.displayName()
            tmp = tmp.next
    def findUser(self,name):
        if self.users.find(name) != None:
            return self.users.find(name)
class User:
    def __init__(self, name="", weight = "", weightGoal ="",height=""):
        self.name = name
        self.weight = weight
        self.weightGoal = weightGoal
        self.height=height
        self.next=None
        self.right = None
        self.left = None
        self.ID=0

    def isEqual(self,name):
        return self.name==name

    def setData(self, data):
        self.weight = data["weight"]
        self.weightGoal = data["weightGoal"]
        self.height=data["height"]

    def toJSON(self):
        tmp = {}
        tmp["weight"] = self.weight
        tmp["weightGoal"] = self.weightGoal
        tmp["height"]=self.height
        return tmp

    def setWeightGoal(self, weightGoal=""):
        if (weightGoal == ""):
            while True:
                weightGoal = input("\nPlease insert the weight Goal as lose/gain or maintain: ")
                if weightGoal=="lose" or weightGoal=="gain" or weightGoal=="maintain":
                    self.weightGoal = weightGoal
                    break
                else:
                    print("Please in non-capital letters write : lose maintain or gain\n")

    def setWeight(self, weight=""):
        if (weight == ""):
            while True:
                weight = (input("\nPlease insert your weight value in kg "))
                dot=weight
                if dot.replace('.','',1).isdigit()==True:
                    weight=float(weight)
                    self.weight = weight
                    break
                else:
                    print("please write in numeric form:)\n")

    def setHeight(self,height=""):
        if (height == ""):
            while True:
                height = input("\nPlease insert your height value in cm integer form")
                if height.isnumeric():
                    height = int(height)
                    self.height = height
                    break
                else:
                    print("please write in numeric form:)\n")

    def findBMI(self):
        BMI = float(float(self.weight) * 10000 / (float(self.height)) * (float(self.height)))
        if BMI < 18.5:
            print("Dear user, your BMI indicated that you're underweight.The normla range is between 18.5-24.9.\n")
            print("We suggest you choose the gaining goal if you haven't chosen that. \n")
        elif BMI > 18.5 and BMI < 25:
            print(
                "Dear user, your BMI indicated that you're in the normal weight range!The normla range is between 18.5-24.9\n ")
            print("We suggest you choose the maintaining goal if you haven't chosen that.\n")
        elif BMI > 25 and BMI < 30:
            print(
            "\nDear user, your BMI indicated that you're in the overweight range.The normla range is between 18.5-24.9")
            print("We suggest you choose the losing goal if you haven't chosen that.\n")

    def findCalories(self,gender="",age="",lose="",gain=""):
        if gender == "":
            while True:
                gender = input("\nPlease insert your gender as male or female non-capital : ")
                if gender=="male"or gender=="female":
                    break
                else:
                    print("please answer in 'male' or 'female'.\n")
        if age== "":
            while True:
                age= input("\nPlease insert your age in an integer form : ")
                if age.isnumeric():
                    age=int(age)
                    break
                else:
                    print("Please answer in an integer form:)\n")
        if self.weightGoal=="lose":
            if lose == "":
                while True:
                    lose = input("\nPlease insert how many kgs you want to lose per week : ")
                    dot=lose
                    if dot.replace('.','',1).isdigit()==True:
                        lose = float(lose)
                        break
                    else:
                        print("please input in numeric form(float or integer)\n")
            if gender == "male":
                CalorieIn = float(10 * float(self.weight) + 6.25 * float(self.height) - 5 * age + 5 - (lose * 3500) / 7)
                CalorieIn = "{:.2f}".format(CalorieIn)
                print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                      " Kgs from your current weight per week:)\nWe suggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
            if gender == "female":
                CalorieIn = float(
                    10 * float(self.weight) + 6.25 * float(self.height) - 5 * age - 161 - (lose * 3500) / 7)
                print("\nYou should eat:", CalorieIn, "Calories Per day, to lose", lose,
                      " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
        if self.weightGoal=="gain":
            if gain == "":
                while True:
                    gain = input("\nPlease insert how many kgs you want to gain per week : ")
                    dot=gain
                    if dot.replace('.','',1).isdigit()==True:
                        gain=float(gain)
                        break
                    else:
                        print("please input in numeric form(float or integer)")
            if gender == "male":
                CalorieIn = float(10 * float(self.weight) + 6.25 * float(self.height) - 5 * age + 5 + ( gain * 3500) / 7)
                print("\nYou should eat:", CalorieIn, "Calorie Per day, to gain", gain,
                      " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the calories.")
            if gender == "female":
                CalorieIn = float(
                    10 * float(self.weight) + 6.25 * float(self.height) - 5 * age - 161 + (gain * 3500) / 7)
                print("\nYou should eat:", CalorieIn, "Calories Per day, to gain", gain,
                      " Kgs from your current weight per week:)\nsuggest you to use the 'FitnessPall' application to track your calories.\nYou simply input your consumed food and it calculates the  the calories.")
        if self.weightGoal=="maintain":
            if gender == "male":
                CalorieIn = float(10 * float(self.weight) + 6.25 * float(self.height) - 5 * age + 5)
                print("\nYou should eat:", CalorieIn, "CaloriesPer day, to maintain your current weight :) \n")
            elif gender == "female":
                CalorieIn = float(10 * float(self.weight) + 6.25 * float(self.height) - 5 * age - 161)
                CalorieIn = "{:.2f}".format(CalorieIn)
                print("\nYou should eat:", CalorieIn, "Calories Per day, to maintain your current weight :) \n")

    def displayName(self):
        print(self.name)

    def display(self):
        print(self.name, self.weight, self.weightGoal,self.height)

    def checkprogress(self,oldweight,currentweight):
        difference=int(currentweight)-int(oldweight)
        if difference > 0 and (self.weightGoal == "maintain" or self.weightGoal == "lose"):
            print("\nDear user, you have gained : ", difference,
                  "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to", self.weightGoal,
                  " weight.\nWork harder you'll reach there\n")
        if difference > 0 and self.weightGoal == "gain":
            print("\nDear user, you have gained : ", difference,
                  "Kgs since we last saw you !\nYou're on the right track as your goal was to ", self.weightGoal,
                  "your weight :) Keep on going :)\n")
        if difference < 0 and (self.weightGoal == "maintain" or self.weightGoal == "gain"):
            print("\nDear user, you have lost: ", abs(difference),
                  "Kgs since we last saw you. You have to work harder to reach your goal\nwhich was to gain weight.\nWork harder you'll reach there")
        if difference < 0 and self.weightGoal == "lose":
            print("\nDear user, you have lost : ", abs(difference),
                  "Kgs since we last saw you !\nYou're on the right track as your goal was to lose"
                  "weight :) Keep on going :)")
        if difference == 0 and (self.weightGoal=="maintain"):
            print("\nDear user, you have stayed the same weight since we last saw you !\nYou're on the right track as your goal was to ", self.weightGoal,
                  "your weight :) Keep on going :)\n")
        if difference==0 and (self.weightGoal=="lose" or self.weightGoal=="gain"):
            print("\nDear user, you have stayed the same weight since we last saw you,\n However your goal was to ",self.weightGoal,
                  " weight.\nWork harder you'll reach there\n")

    def changeinweight(self):
        while True:
            change = input("\nDo you want to change the data? please type yes or no: ")
            if (change == "yes"):
                oldweight = self.weight
                self.setWeight()
                currentweight = self.weight
                self.checkprogress(oldweight, currentweight)
                break
            if change == "no":
                break
            else:
                print("answer in yes or no :)\n")

def main():
    print("\nThis Application helps you reach your weight goal. :)\n")
    userManager = UserManager()
    userManager.loadAllUsers()
    print("\n***These are all registered users")
    userManager.displayAllUsers()
    while True:
        hasUsed = input("\nHave you used our app before? Please answer in yes or no : ")
        if hasUsed == "no":
            userName = userManager.CreatUsername()
            userManager.addUser(userName)
            currentUser=userManager.findUser(userName)
            currentUser.setWeightGoal()
            currentUser.setWeight()
            currentUser.setHeight()
            currentUser.findBMI()
            currentUser.findCalories()
            break
        elif hasUsed == "yes":
            userName = input("\nplease type your previously created username : ")
            currentUser = userManager.checkifNameexists(userName)
            if currentUser==False:
                print("\nDear User this username doesn't exist.\n which means you need to creat an account by this username first:)\n")
                userManager.addUser(userName)
                currentUser = userManager.findUser(userName)
                currentUser.setWeightGoal()
                currentUser.setWeight()
                currentUser.setHeight()
                currentUser.findBMI()
                currentUser.findCalories()
                break
            else:
                currentUser=userManager.findUser(userName)
                break
        else:
            print("\nsorry Try again!Please type yes or no.(not capital)\n")

    print("\n******This is the current user:\n")
    currentUser.display()
    currentUser.changeinweight()
    print("\nThe new updated list of Users is: ")
    userManager.BSTusers.printBST()
    userManager.saveAllUsers()
main()
