class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Age: "+str(self.citizen_age))
        print("Date of Birth: "+self.citizen_dob)
        print("Citizen Id: "+self.citizen_id)
        print("Citizen Added")
        
        
        citizen1 = Citizen("Peter",8,"19th october 2012","0198")
        citizen1.add_citizen
        
        citizen2 = Citizen("Pete",9,"11th october 2011","0199")
        citizen2.add_citizen
        
        citizen3 = Citizen("Sophia",10,"19th May 2011","2000")
        citizen3.add_citizen
        
        citizen4 = Citizen("Tom",8,"31st December 2011","2001")
        citizen4.add_citizen
        
        citizen5 = Citizen("Mark",12,"11th April 2011","2002")
        citizen5.add_citizen



