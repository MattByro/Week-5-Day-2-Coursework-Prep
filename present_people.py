
from person import *
from student_person import *
from staff_person import *

def present_person(p):
    print(p.who_am_i())


pJB = Person("James Bond", "London, UK", "UK")
pRH = Person("Robin Hood", "Nottingham, UK", "UK")
pLM = Student("Lethiwe Mwendwa", "Nottingham, UK", "Keyna", "Bsc in Computer Science")
pTM = Student("Thomas Frewer", "Nottingham, UK", "UK", "Bsc in Computer Science")
pNA = Staff("Nuno Rodrigues Amalio", "Nottingham, UK", "Portugal", "Senior Lecturer in Computer Science")
pJE = Student("Jonathan Alexander East", "Nottingham, UK", "UK", "Bsc in Computer Science and Maths")
pTN = Student("Taboka Ndlovu", "Nottingham, UK", "Zimbabwe", "Bsc in Software Engineering")
pME = Student ("Martin Evans", "Nottingham, UK", "UK", "Bsc in Computer Science")
pTL = Student ("Toby Lowe", "Nottingham, UK", "UK", "Bsc in Data Science")

people = [pJB, pRH, pLM, pTM, pNA, pJE, pTN, pME, pTL]



for p in people:
     present_person(p) 