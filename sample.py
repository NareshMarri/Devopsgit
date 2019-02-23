#!/usr/bin/python
class myclass:
    def __init__(self,name,age,company,location):
        self.age=age
        self.name=name
        self.company=company
        self.location=location
        print("Name of the candidate="+name)
        print("Age of the candidate="+age)
        print("Company of the candidate="+company)
        print("LOcation of the candidate="+location)

p1=myclass('Naresh',36,"Wipro","Bangalore")

