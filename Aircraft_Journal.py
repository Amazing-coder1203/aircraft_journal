import tkinter as tk
from tkinter import *
import random
import sqlite3 


ab = ("A318", "A319", "A320", "A321", "A330", "A350", "A340", "A380", "beluga")
airbus = ab
abi = ("""Airbus is an europe based aircraft manufacturer. \nIt's one of the largest producer in the world with more than 9000 active aircrafts.\n Airbus aircraft list is given bellow
""")
a318 = """Role : Narrow-body jet airliner\nLength :	31.44m\nCruising speed : 	Mach 0.78 (829 km/h; 515 mph)\nRange (typical payload) :	5,740 km\nEngines(x2) : CFM56-5B\nAircraft Model : A318-111,	A318-112,	A318-121,	A318-122"""
a319 = """Role : Narrow-body jet airliner\nLength :	33.84 m (111 ft 0 in)\nCruising speed : 	Mach 0.78 (829 km/h; 515 mph)\nRange (typical payload) :	3,750 nmi (6,940 km)\nEngines(x2) : CFM56-5B\nAircraft Model : A319-111, A319-112,	A319-113,	A319-114,\n	A319-115,	A319-131,	A319-132,	A319-133"""
a320 = """Role : Narrow-body jet airliner\nLength :	37.57 m (123 ft 3 in)\nCruising speed :	    Mach 0.78 (829 km/h; 515 mph)\nRange (typical payload) : 	112 km (3,300 nmi)\nEngines(x2) : CFM56-5A3\nAircraft Model : A320-111, A320-211,	A320-212,	A320-214, \nA320-215, A320-216,	A320-231,	A320-232,	A320-233"""
a321 = """Role : Narrow-body jet airliner\nLength :	44.51 m (146.0 ft)\nCruising speed :	Mach 0.78 (450 kn; 833 km/h)\nRange (typical payload) :	3,200 nmi (5,930 km)\nEngines(x2) : CFM56-5B\nAircraft Model : A321-111, A321-112,	A321-131,	A321-211,\n	A321-212,	A321-214, A321-231,	A321-111,\n A321-131 A321-211, A321-212,	A321-213,\n	A321-231,	A321-232, A321-232"""
a330 = """Role : Wide-body jet airliner\nLength :	58.82 m (192.98 ft)	63.67 m (208.89 ft)\nCruising speed :	Mach 0.82 (470 kn; 871 km/h)\nRange (typical payload) :	13,450 km / 7,250 nmi\nEngines(x2) : GE CF6 (except -200F) / PW4000 / Trent 700\nAircraft Model : A330-201,	A330-203, A330-223, A330-223F,	A330-243, \nA330-243F,	A330-301,	A330-302,	A330-303, A330-321,\n	A330-322,	A330-323,	A330-341, A330-342, A330-343"""
a340 = """Role : Wide-body jet airliner\nLength :	75.36 m / 247.24 ft\nCruising speed :	Mach 0.86 (493 kn; 914 km/h) max\nRange (typical payload) :	14,450 km / 7,800 nmi\nEngines(x4) : CFM International CFM56-5C,	Trent 553,	Trent 556l\nAircraft Variant : A340-200,	A340-300,	A340-500,	A340-600"""
a350 = """Role : Wide-body jet airliner\nLength :	73.79 m / 242.1 ft\nCruising speed : 	Mach 0.85 (488 kn; 903 km/h)\nRange (typical payload) :	16,100 km (8,700 nmi)\nEngines(x2) : Rolls-Royce Trent XWB\nAircraft Variant : A350-900,	A350-1000"""
a380 = """Role : Wide-body jet airliner\nLength :	72.72 m (238 ft 7 in)\nCruising speed :	903 km/h (561 mph, 488 kn) Mach 0.85\nRange (typical payload) :	14,800 km (9,200 mi, 8,000 nmi)\nEngines(x4) : Trent 970-84/970B-84 \nAircraft Variant : A380-841, A380-842,	A380-861"""
belugai = """Role : Wide-body freight airliner\nLength :	 56.15 m (184 ft 3 in)\nCruising speed :	737 km/h (458 mph, 398 kn) , Mach 0.69\nRange (typical payload) :	 4,632 km (2,501 nmi) \nEngines(x2) : Rolls-Royce Trent 700 turbofan\nAircraft Variant : A300-600ST, ABelugaXL"""


bg = ("B707", "B727", "B737", "B767", "B777", "B787", "B747", "dreamlifter" )
op = [ab, bg]
boeing = bg
bgi = """The Boeing Company is an American multinational corporation that\n designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites. \nTher are more than 10000 active boeing plane in the sky."""
b707 = """Role : Narrow-body jet airliner\nLength : 152 ft 11 in (46.61 m) \nCruising speed :	478-525 kn / 885-974 km/h \nRange (typical payload) : 3,750 nmi (6,940 km) \nEngines(x4) : P&W JT3C-6,	P&W JT3D-1	JT4A-11/12,	Conway-12	Pratt & Whitney JT3D-3/7 \nAircraft Variant : 707-120,	707-120B,	707-320, 707-420,	707-320B,	707-320C\nAircraft Delivered : 1010"""
b727 = """Role : Narrow-body jet airliner\nLength :	153 ft 2 in  (46.68m) \nCruising speed  :	865–953 km/h / 467-515kt \nRange (typical payload) :	1,900 nmi (3,500 km) Adv. 2,550 nmi (4,720 km) \nEngines(x3) : Pratt & Whitney JT8D-1/7/9 \nAircraft Variant : 727-100,	727-200 \nAircraft Delivered : 1831"""
b737 = """Role : Narrow-body jet airliner\nLength :	116.7–143.7 ft (35.56–43.8 m)\nCruising speed :	Mach 0.785 (453 kn; 838 km/h)\nRange (typical payload) :	3,300–3,850 nmi 6,110–7,130 km \nEngines(x2) : CFM56-7 series,	CFM LEAP-1B\nAircraft Variant : 737-100,	737-200,	737-300/-400/-500,	737-600/-700/-800/-900, 737MAX\nAircraft Delivered : 10,586"""
b767 = """Role : Wide-body jet airliner\n Length :	201 ft 4 in / 61.37 m\nCruising speed :	459–486 kn (850–900 km/h)\nRange (typical payload) :	5,625 nmi 10,415 km\nEngines(x2) : CF6 / PW4000, PW4000 / CF6 / RB211\nAircraft Variant : 767-200,	767-200ER,	767-300,	767-300ER/F,	767-400ER\nAircraft Delivered : 1,200"""
b777 = """Role : Wide-body jet airliner\nLength :	209 ft 1 in  (63.73 m)\nCruising speed :	Max. Mach 0.87–Mach 0.89 (499–511 kn; 924–945 km/h\nRange (typical payload) :	8,555 nmi / 15,843 km\nEngines(x2) : 2× GE90-110B/-115B\nAircraft Variant : 777-200/200ER,	777-300,	777-300ER,	777-200LR/777F\nAircraft Delivered : 1,649"""
b787 = """Role : Wide-body jet airliner\nLength :	186 ft 1 in (56.72 m)\nCruising speed :	Max.: Mach 0.90 (516 kn; 956 km/h), Cruise: Mach 0.85 (488 kn; 903 km/h)\nRange (typical payload) :	6,430 nmi (11,910 km)\nEngines(x2) : General Electric GEnx-1B or Rolls-Royce Trent 1000\nAircraft Variant : 787-8,	787-9, 787-10\nAircraft Delivered : 	992"""
b747 = """Role : Wide-body jet airliner\nLength :	231 ft 10 in (70.66 m) 250 ft 2 in (76.25 m)\nCruising speed :	Mach 0.855 (504 kn; 933 km/h)\nRange (typical payload) :	7,670 nmi 14,200 km\nEngines(x4) : Pratt & Whitney JT9D-7 or Rolls-Royce RB211-524 or GE CF6, PW4000 / CF6 / RB211, GEnx-2B67\nAircraft Variant : 747SP,747-100,747-200B,747-300,747-400,747-8\nAircraft Delivered : 1,559"""
dreamlifteri = """Role : Wide-body freight airliner\nLength :	235 ft 2 in (71.68 m)	231 ft 10 in (70.6 m)\nCruising speed :	Mach 0.82 (474 kn, 878 km/h), Mach 0.85 (491 kn, 910 km/h)\nRange (typical payload) :	4200 nmi (4,800 mi; 7,800 km), 7,260 nmi (8,350 mi; 13,450 km)\nEngines(x4) : PW 4062, PW 4062, GE CF6-80C2B5F, RR RB211-524G/H\nAircraft Variant : 747 Dreamlifter, 	747-400\nAircraft Delivered : 4"""



emb = ("EMB 110 Bandeirante", "EMB 202 Ipanema", "EMB 121 Xingu", "EMB 314", "EMB-120 Brasilia", "AMX", "Legacy 600", "EMB-500 Phenom 100", "Phenom 300", "EMB-550 Legacy 500", "C-390 Millennium")
embraer = emb
embi = """Embraer is a Brazilian aerospace conglomerate that produces commercial, military,\n executive and agricultural aircraft and provides aeronautical services.\n It was founded in 1969 in São José dos Campos, São Paulo,\n where its headquarters are located.\n The company is the third largest producer of civil aircraft, \nafter Boeing and Airbus."""
EMB110Bandeirante = """Role : Turboprop Regional airliner\n Length : 15.1 m (49 ft 6 in)\n Cruise speed : 411 km/h (255 mph, 222 kn) maximum at 2,440 m (8,005 ft)\n Range : 1,964 km (1,220 mi, 1,060 nmi)\n Engine x2 : Pratt & Whitney Canada PT6A-34 turboprop engines\n Aircraft Variant : EMB 100, EMB 110A, EC-95B, EMB 110B, EMB 110C, EMB 110C(N), EMB 110E, EMB 110E(J), + \n Aircraft Delivered : 1400"""
EMB202Ipanema = """Role : Agricultural aircraft\n Length : 7.43 m (24 ft 5 in) (tail up)\n Cruise speed : 213 km/h (132 mph, 115 kn)\n Range : 938 km (583 mi, 506 nmi)\n Engine x1 : Textron Lycoming IO-540-K1J5D air-cooled flat-six\n Aircraft Variant : EMB-200, EMB-200A, EMB-201, EMB-201A, EMB-201R, EMB-202, EMB-202A, EMB-202R\n Aircraft Delivered : 1400"""
EMB121Xingu = """Role : Utility aircraft\n Length : 12.25 m (40 ft 2 in)\n Cruise speed : 380 km/h (236 mph, 205 kn) at 3,050 m (10,010 ft)\n Range : 1,230 km (760 mi, 660 nmi) at 6,100 m\n Engine x2 : Pratt & Whitney Canada PT6A-135 turboprop engines,\n Aircraft Variant : EMB 121A Xingu I, EMB 121A1 Xingu II, EMB 121B Xingu III, EMB 123 Tapajós, VU-9\n Aircraft Delivered : 106"""
EMB314 = """Role : Attack and counter-insurgency aircraft\n Length : 11.38 m (37 ft 4 in)\n Cruise speed : 520 km/h (320 mph, 280 kn)\n Range : 1,330 km (830 mi, 720 nmi)\n Engine x1 :  Pratt & Whitney Canada PT6A-68C turboprop engine,\n Aircraft Variant : A-29 Super Tucano, EMB 314\n Aircraft Delivered : 200+"""
EMB120Brasilia = """Role : Turboprop Regional airliner\n Length : 20 m (65 ft 7 in)\n Cruise speed : 552 km/h (343 mph, 298 kn)\n Range : 1,750 km (1,090 mi, 940 nmi)\n Engine x2 : Pratt & Whitney Canada PW118 / Pratt & Whitney Canada PW118A /\n Pratt & Whitney Canada PW118B turboprop engines\n Aircraft Variant : EMB 120, EMB 120ER, EMB 120FC, EMB 120QC, EMB 120RT, VC-97\n Aircraft Delivered : 210"""
AMX = """ Role : 	Ground-attack aircraft\n Length : 13.23 m (43 ft 5 in)\n Cruise speed : 1,053 km/h (654 mph, 569 kn) at 10,975 m (36,007 ft)\n Range : 3,336 km (2,073 mi, 1,801 nmi)\n Engine x1 : Rolls-Royce Spey 807 turbofan engine\n Aircraft Variant : AMX-T, AMX-ATA, AMX-R (RA-1), A-1M, A-11M, TA-11A, A-11B, TA-11B\n Aircraft active : 86"""
Legacy600 = """ Role : Business jet\n Length : 26.33 m / 86 ft 5 in\n Cruise speed : Mach 0.78 (829 km/h; 515 mph)\n Range : 3,400 nmi / 6,297 km\n Engine x2 : Honeywell Primus Elite\n Aircraft Variant : Legacy 600, Legacy 650\n Aircraft Delivered : 283"""
EMB500Phenom100 = """ Role : Very light jet\n Length : 212.82 m (42 ft 1 in)\n Cruise speed : 750 km/h (470 mph, 400 kn)\n Range : 2,182 km (1,356 mi, 1,178 nmi) \n Engine x2 : Pratt & Whitney Canada PW617F1-E turbofan engines\n Aircraft Delivered : 369"""
Phenom300 = """ Role : Light business jet\n Length : 15.9 m (52 ft 2 in)\n Cruise speed : 834 km/h (518 mph, 450 kn)\n Range : 3,723 km (2,313 mi, 2,010 nmi) with IFR reserves, 5 occupants\n Engine x2 :  PW535E1[8] turbofans, 15.471 kN (3,478 lbf) thrust each\n Aircraft Variant : 2020 Phenom 300E, Phenom 300E, Phenom 300 \n Aircraft Delivered : 500+"""
EMB550Legacy500 = """ Role : Business jet\n Length : 20.74 m / 68 ft 1 in\n Cruise speed : 863 km/h / 466 kt\n Range : 5,788 km / 3,125 nmi\n Engine x2 : Honeywell HTF7500E\n Aircraft Variant : EMB-550 Legacy 500, Praetor 600 EMB-545 Legacy 450\n Aircraft Delivered : 68"""
C390Millennium = """ Role :	Medium-sized transport aircraft\n Length : 33.5 m (110.0 ft)\n Cruise speed : 870 km/h (540 mph, 470 kn) Mach 0.8\n Range : 5,820 km (3,610 mi, 3,140 nmi) 14,000 kg (30,865 lb) payload\n Engine x2 : IAE V2500-E5 turbofan\n Aircraft Delivered : 7"""

bom = ("Learjet 70/75", "Challenger 300", "Challenger 600", "Global Express", "Global 7500", "Airbus A220", "CRJ900", "Dash 8 Q-400")
bombardier = bom
bomi = """Bombardier Inc. is a Canadian multinational that founded in 1942 by Joseph-Armand Bombardier. \nIt is a manufacturer of business jets, public transport vehicles, and trains.\n It was also formerly a manufacturer of commercial jets and recreational vehicles,\n with the latter being spun-off as Bombardier Recreational Products."""
Learjet70 = """ Role : Light Business jet\n Length : 58 ft 0 in (17.7 m)\n Cruise speed : 465 kn (535 mph, 861 km/h\n Range :  2,040 nmi (2,350 mi, 3,780 km)\n Engine x2 : Honeywell TFE731-40BR Turbine\n Aircraft Variant : Learjet70, Learjet75\n Aircraft Delivered : 133"""
Challenger300 = """ Role : Business jet\n Length : 68.63 ft / 20.92 m\n Cruise speed : Mach 0.80 / 459 kn / 850 km/h\n Range :  3,100 nmi / 5,741 km\n Engine x2 : Honeywell HTF7000\n Aircraft Variant : Challenger 300, Challenger 350\n Aircraft Delivered : 454"""
Challenger600 = """ Role : Business jet\n Length : 20.9 m (68 ft 5 in)\n Cruise speed : 854 km/h (531 mph, 461 kn)\n Range :   7,408 km (4,603 mi, 4,000 nmi)\n Engine x2 : General Electric CF34-3B turbofans\n Aircraft Variant : Challenger 600, Challenger 601, Challenger 604, Challenger 605, Challenger 650\n Aircraft Delivered : 81"""
GlobalExpress = """ Role : Business jet\n Length : 	96 ft 10 in / 29.5 m)\n Cruise speed : Mach 0.88 (504 kn / 934 km/h) high-speed, Mach 0.85 (487 kn / 902 km/h) typical\n Range : 5,200 nm / 9,630 km)\n Engine x2 : BR710A2-20\n Aircraft Variant : Global 5000, Global 5500,	Global 6000, Global 6500\n Aircraft Delivered : 148"""
Global7500 = """ Role : Business jet\n Length : 	111.17 ft / 33.88 m\n Cruise speed : Mach 0.85 (487 kn / 902 km/h), Mach 0.90 (516 kn / 955 km/h) Max.\n Range : 7,700 nm / 14,260 km\n Engine x2 : General Electric Passport\n Aircraft Variant : Global 7500,	Global 8000\n Aircraft Delivered : 63"""
AirbusA220 =  """Ownership : Developed by Bombardier and now ownde by Airbus, Role : BNarrow-body jet airliner\n Length : 	35.00 m / 114' 9"\n Cruise speed : Mach .82 (470 kn; 871 km/h) max, Mach .78 (447 kn; 829 km/h) typical\n Range : 6,297 km / 3,400 nmi	6,204 km / 3,350 nmi\n Engine x2 : 2× Pratt & Whitney PW1500G\n Aircraft Variant : A220-100 (BD-500-1A10),	A220-300 (BD-500-1A11)\n Aircraft Delivered : 137"""
CRJ900 = """ Role : Regional jet\n Length : 	118 ft 11 in / 36.2 m\n Cruise speed : Mach 0.78 (447 kn, 829 km/h)\n Range : 1,553 NM / 2,876 km (LR)\n Engine x2 : General Electric CF4-8C5\n Aircraft Variant : CRJ700, CRJ900, CRJ1000\n Aircraft Delivered : 822"""
Dash8q400 = """ Role : Turboprop regional airlinert\n Length : 	107 ft 9 in / 32.8 m\n Cruise speed : 300–360 kn / 556–667 km/h\n Range : 1,100 nmi / 2,040 km\n Engine x2 : PW150\n Aircraft Variant : Q200, Q300, Q400\n Aircraft Delivered : 1249"""



    
    

def menu2():
    
    
    
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="#101357")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="steel blue1")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  W I T A  AIRCRAFT JOURNAL ',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.0,rely=0.02)
    level = Label(menu_frame,text='know more about these aircrafts',bg="steel blue1",font="calibri 18")
    level.place(relx=0.22,rely=0.03)


    airbus1 = Button(menu_frame,text='AIRBUS',fg="white",bg="#101357",font="Broadway 22",command=airbus)
    airbus1.place(relx=0.1,rely=0.4)
    
    boeing1 = Button(menu_frame,text='BOEING',fg="white",bg="#101357",font="Broadway 22",command=boeing)
    boeing1.place(relx=0.6,rely=0.4)

    embraero1 = Button(menu_frame,text='EMBRAER',fg="white",bg="#101357",font="Broadway 22",command=embraero)
    embraero1.place(relx=0.07,rely=0.6)

    bombardier1 = Button(menu_frame,text='BOMBARDIER',fg="white",bg="#101357",font="Broadway 22",command=bombardier)
    bombardier1.place(relx=0.57,rely=0.6)
    
    
    menu.mainloop()        
     


def Dash8Q400x():
    
    global Dash8Q400t
    Dash8Q400t= Tk()
    Dash8Q400_canvas = Canvas(Dash8Q400t,width=500,height=300,bg="#101357")
    Dash8Q400_canvas.pack()

    Dash8Q400_frame = Frame(Dash8Q400_canvas,bg="white")
    Dash8Q400_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Dash8Q400_canvas,text='DASH8Q400',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Dash8Q400_frame,text=Dash8q400,bg="white",font="calibri 12")
    info07.place(relx=0.1,rely=0.1)

def CRJ900x():
    
    global CRJ900t
    CRJ900t= Tk()
    CRJ900_canvas = Canvas(CRJ900t,width=600,height=300,bg="#101357")
    CRJ900_canvas.pack()

    CRJ900_frame = Frame(CRJ900_canvas,bg="white")
    CRJ900_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(CRJ900_canvas,text='CRJ900',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(CRJ900_frame,text=CRJ900,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)

def AirbusA220x():
    
    global AirbusA220t
    AirbusA220t= Tk()
    AirbusA220_canvas = Canvas(AirbusA220t,width=850,height=300,bg="#101357")
    AirbusA220_canvas.pack()

    AirbusA220_frame = Frame(AirbusA220_canvas,bg="white")
    AirbusA220_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(AirbusA220_canvas,text='AIRBUS A220',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(AirbusA220_frame,text=AirbusA220,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)    

def Global7500x():
    
    global Global7500t
    Global7500t= Tk()
    Global7500_canvas = Canvas(Global7500t,width=850,height=300,bg="#101357")
    Global7500_canvas.pack()

    Global7500_frame = Frame(Global7500_canvas,bg="white")
    Global7500_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Global7500_canvas,text='GLOBAL75000',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Global7500_frame,text=Global7500,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.2) 

def GlobalExpressx():
    
    global GlobalExpresst
    GlobalExpresst= Tk()
    GlobalExpress_canvas = Canvas(GlobalExpresst,width=850,height=300,bg="#101357")
    GlobalExpress_canvas.pack()

    GlobalExpress_frame = Frame(GlobalExpress_canvas,bg="white")
    GlobalExpress_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(GlobalExpress_canvas,text='GlobalExpress',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(GlobalExpress_frame,text=GlobalExpress,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1) 


def Challenger600x():
    
    global Challenger600t
    Challenger600t= Tk()
    Challenger600_canvas = Canvas(Challenger600t,width=850,height=300,bg="#101357")
    Challenger600_canvas.pack()

    Challenger600_frame = Frame(Challenger600_canvas,bg="white")
    Challenger600_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Challenger600_canvas,text='CHALLENGER 600',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Challenger600_frame,text=Challenger600,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1) 
     
    
def Challenger300x():
    
    global Challenger300t
    Challenger300t= Tk()
    Challenger300_canvas = Canvas(Challenger300t,width=650,height=300,bg="#101357")
    Challenger300_canvas.pack()

    Challenger300_frame = Frame(Challenger300_canvas,bg="white")
    Challenger300_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Challenger300_canvas,text='CHALLENGER 300',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Challenger300_frame,text=Challenger300,bg="white",font="calibri 12")
    info07.place(relx=0.2,rely=0.1) 

def Learjet7075x():
    
    global Learjet7075t
    Learjet7075t= Tk()
    Learjet7075_canvas = Canvas(Learjet7075t,width=550,height=300,bg="#101357")
    Learjet7075_canvas.pack()

    Learjet7075_frame = Frame(Learjet7075_canvas,bg="white")
    Learjet7075_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Learjet7075_canvas,text='LEARJET7075',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Learjet7075_frame,text=Learjet70,bg="white",font="calibri 12")
    info07.place(relx=0.2,rely=0.2)    

def bombardier():
    menu.destroy()
    
    global bomb 
    bomb = Tk()
    
    
    bombardier_canvas = Canvas(bomb,width=720,height=500,bg="#101357")
    bombardier_canvas.pack()

    bombardier_frame = Frame(bombardier_canvas,bg="steel blue1")
    bombardier_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(bombardier_canvas,text='BOMBARDIER',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    infob = Label(bombardier_frame,text=bomi,bg="steel blue1",font="calibri 10")
    infob.place(relx=0.05,rely=0.03)


    Learjet7075 = Button(bombardier_frame,text='Learjet 70/75',bg="white",font="calibri 12",command=Learjet7075x)
    Learjet7075.place(relx=0.2,rely=0.4)
    
    Challenger300 = Button(bombardier_frame,text='Challenger300',bg="white",font="calibri 12",command=Challenger300x)
    Challenger300.place(relx=0.2,rely=0.5)
    
    Challenger600 = Button(bombardier_frame,text='Challenger600',bg="white",font="calibri 12", command=Challenger600x)
    Challenger600.place(relx=0.2,rely=0.6)

    GlobalExpress = Button(bombardier_frame,text='GlobalExpress',bg="white",font="calibri 12",command=GlobalExpressx)  
    GlobalExpress.place(relx=0.2,rely=0.7)

    Global7500 = Button(bombardier_frame,text='Global7500',bg="white",font="calibri 12",command=Global7500x)  
    Global7500.place(relx=0.8,rely=0.4)

    AirbusA220 = Button(bombardier_frame,text='AirbusA220',bg="white",font="calibri 12",command=AirbusA220x)  
    AirbusA220.place(relx=0.8,rely=0.5)
    
    CRJ900 = Button(bombardier_frame,text='CRJ900',bg="white",font="calibri 12",command=CRJ900x)  
    CRJ900.place(relx=0.8,rely=0.6)

    Dash8Q400 = Button(bombardier_frame,text='Dash8Q400',bg="white",font="calibri 12",command=Dash8Q400x)  
    Dash8Q400.place(relx=0.8,rely=0.7)

    
    def delete_bombardier():
        bomb.destroy()
        menu2()

    back = Button(bombardier_frame,text='BACK',bg="#101357",fg='white',font="calibri 12",command=delete_bombardier)
    back.place(relx=0.5,rely=0.5)

def EMB110Bandeirantex():
    
    global EMB110Bandeirant
    EMB110Bandeirant= Tk()
    EMB110Bandeirante_canvas = Canvas(EMB110Bandeirant,width=850,height=300,bg="#101357")
    EMB110Bandeirante_canvas.pack()

    EMB110Bandeirante_frame = Frame(EMB110Bandeirante_canvas,bg="white")
    EMB110Bandeirante_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB110Bandeirante_canvas,text='EMB110BANDEIRANTE',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB110Bandeirante_frame,text=EMB110Bandeirante,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)

def EMB202Ipanemax():
    
    global EMB202Ipanemat
    EMB202Ipanemat= Tk()
    EMB202Ipanema_canvas = Canvas(EMB202Ipanemat,width=850,height=300,bg="#101357")
    EMB202Ipanema_canvas.pack()

    EMB202Ipanema_frame = Frame(EMB202Ipanema_canvas,bg="white")
    EMB202Ipanema_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB202Ipanema_canvas,text='EMB202IPANEMA',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB202Ipanema_frame,text=EMB202Ipanema,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)

def EMB121Xingux():
    
    global EMB121Xingut
    EMB121Xingut= Tk()
    EMB121Xingu_canvas = Canvas(EMB121Xingut,width=850,height=300,bg="#101357")
    EMB121Xingu_canvas.pack()

    EMB121Xingu_frame = Frame(EMB121Xingu_canvas,bg="white")
    EMB121Xingu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB121Xingu_canvas,text='EMB121XINGU',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB121Xingu_frame,text=EMB121Xingu,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)    

def EMB314x():
    
    global EMB314t
    EMB314t= Tk()
    EMB314_canvas = Canvas(EMB314t,width=850,height=300,bg="#101357")
    EMB314_canvas.pack()

    EMB314_frame = Frame(EMB314_canvas,bg="white")
    EMB314_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB314_canvas,text='EMB314',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB314_frame,text=EMB314,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)

def EMB120Brasiliax():
    
    global EMB120Brasiliat
    EMB120Brasiliat= Tk()
    EMB120Brasilia_canvas = Canvas(EMB120Brasiliat,width=850,height=300,bg="#101357")
    EMB120Brasilia_canvas.pack()

    EMB120Brasilia_frame = Frame(EMB120Brasilia_canvas,bg="white")
    EMB120Brasilia_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB120Brasilia_canvas,text='EMB120BRASILIA',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB120Brasilia_frame,text=EMB120Brasilia,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)

def AMXx():
    
    global AMXt
    AMXt= Tk()
    AMX_canvas = Canvas(AMXt,width=850,height=300,bg="#101357")
    AMX_canvas.pack()

    AMX_frame = Frame(AMX_canvas,bg="white")
    AMX_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(AMX_canvas,text='AMX',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(AMX_frame,text=AMX,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1)    

def Legacy600x():
    
    global Legacy600t
    Legacy600t= Tk()
    Legacy600_canvas = Canvas(Legacy600t,width=850,height=300,bg="#101357")
    Legacy600_canvas.pack()

    Legacy600_frame = Frame(Legacy600_canvas,bg="white")
    Legacy600_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Legacy600_canvas,text='LEGACY 600',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Legacy600_frame,text=Legacy600,bg="white",font="calibri 14")
    info07.place(relx=0.2,rely=0.2) 

def EMB500Phenom100x():
    
    global EMB500Phenom100t
    EMB500Phenom100t= Tk()
    EMB500Phenom100_canvas = Canvas(EMB500Phenom100t,width=700,height=300,bg="#101357")
    EMB500Phenom100_canvas.pack()

    EMB500Phenom100_frame = Frame(EMB500Phenom100_canvas,bg="white")
    EMB500Phenom100_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB500Phenom100_canvas,text='EMB500 PHENOM100',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB500Phenom100_frame,text=EMB500Phenom100,bg="white",font="calibri 11")
    info07.place(relx=0.1,rely=0.1) 


def EMB550Legacy500x():
    
    global EMB550Legacy500t
    EMB550Legacy500t= Tk()
    EMB550Legacy500_canvas = Canvas(EMB550Legacy500t,width=720,height=300,bg="#101357")
    EMB550Legacy500_canvas.pack()

    EMB550Legacy500_frame = Frame(EMB550Legacy500_canvas,bg="white")
    EMB550Legacy500_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(EMB550Legacy500_canvas,text='EMB550 LEGACY500',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(EMB550Legacy500_frame,text=EMB550Legacy500,bg="white",font="calibri 11")
    info07.place(relx=0.1,rely=0.1) 
     
    
def Phenom300x():
    
    global Phenom300t
    Phenom300t= Tk()
    Phenom300_canvas = Canvas(Phenom300t,width=720,height=300,bg="#101357")
    Phenom300_canvas.pack()

    Phenom300_frame = Frame(Phenom300_canvas,bg="white")
    Phenom300_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(Phenom300_canvas,text='PHENOM 300',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(Phenom300_frame,text=Phenom300,bg="white",font="calibri 10")
    info07.place(relx=0.1,rely=0.1) 

def C390Millenniumx():
    
    global C390Millenniumt
    C390Millenniumt= Tk()
    C390Millennium_canvas = Canvas(C390Millenniumt,width=700,height=300,bg="#101357")
    C390Millennium_canvas.pack()

    C390Millennium_frame = Frame(C390Millennium_canvas,bg="white")
    C390Millennium_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(C390Millennium_canvas,text='C390 MILLENNIUM',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(C390Millennium_frame,text=C390Millennium,bg="white",font="calibri 11")
    info07.place(relx=0.1,rely=0.1)    

def embraero():
    menu.destroy()
    
    global ebr 
    ebr = Tk()
    
    
    embraero_canvas = Canvas(ebr,width=820,height=600,bg="#101357")
    embraero_canvas.pack()

    embraero_frame = Frame(embraero_canvas,bg="steel blue1")
    embraero_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(embraero_canvas,text='EMBRAER',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    infob = Label(embraero_frame,text=embi,bg="steel blue1",font="calibri 13")
    infob.place(relx=0.0,rely=0.03)

    EMB110Bandeirante = Button(embraero_frame,text='EMB110Bandeirante',bg="white",font="calibri 12",command=EMB110Bandeirantex)
    EMB110Bandeirante.place(relx=0.2,rely=0.4)
    
    EMB202Ipanema = Button(embraero_frame,text='EMB202Ipanema',bg="white",font="calibri 12",command=EMB202Ipanemax)
    EMB202Ipanema.place(relx=0.2,rely=0.48)
    
    EMB121Xingu = Button(embraero_frame,text='EMB121Xingu',bg="white",font="calibri 12", command=EMB121Xingux)
    EMB121Xingu.place(relx=0.2,rely=0.56)

    EMB314 = Button(embraero_frame,text='EMB314',bg="white",font="calibri 12",command=EMB314x)  
    EMB314.place(relx=0.2,rely=0.64)

    EMB120Brasilia = Button(embraero_frame,text='EMB120Brasilia',bg="white",font="calibri 12",command=EMB120Brasiliax)  
    EMB120Brasilia.place(relx=0.8,rely=0.4)

    AMX = Button(embraero_frame,text='AMX',bg="white",font="calibri 12",command=AMXx)  
    AMX.place(relx=0.8,rely=0.48)
    
    Legacy600 = Button(embraero_frame,text='Legacy600',bg="white",font="calibri 12",command=Legacy600x)  
    Legacy600.place(relx=0.8,rely=0.56)

    EMB500Phenom100 = Button(embraero_frame,text='EMB500Phenom100',bg="white",font="calibri 12",command=EMB500Phenom100x)  
    EMB500Phenom100.place(relx=0.8,rely=0.64)

    Phenom300 = Button(embraero_frame,text='Phenom300',bg="white",font="calibri 12",command=Phenom300x)  
    Phenom300.place(relx=0.8,rely=0.72)

    EMB550Legacy500 = Button(embraero_frame,text='EMB550Legacy500',bg="white",font="calibri 12",command=EMB550Legacy500x)  
    EMB550Legacy500.place(relx=0.2,rely=0.72)

    C390Millennium = Button(embraero_frame,text='C390Millennium',bg="white",font="calibri 12",command=C390Millenniumx)  
    C390Millennium.place(relx=0.8,rely=0.8)
    
    def delete_embraero():
        ebr.destroy()
        menu2()

    back = Button(embraero_frame,text='BACK',bg="#101357",fg='white',font="calibri 12",command=delete_embraero)
    back.place(relx=0.5,rely=0.5)
        
    
    

def boeb707():
    
    global b07
    b07= Tk()
    boeb707_canvas = Canvas(b07,width=850,height=300,bg="#101357")
    boeb707_canvas.pack()

    boeb707_frame = Frame(boeb707_canvas,bg="white")
    boeb707_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb707_canvas,text='BOEING B707',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info07 = Label(boeb707_frame,text=b707,bg="white",font="calibri 10")
    info07.place(relx=0.0,rely=0.03)
    
     

def boeb727():
    
    global b27
    b27= Tk()
    boeb727_canvas = Canvas(b27,width=700,height=300,bg="#101357")
    boeb727_canvas.pack()

    boeb727_frame = Frame(boeb727_canvas,bg="white")
    boeb727_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb727_canvas,text='BOEING B727',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info27 = Label(boeb727_frame,text=b727,bg="white",font="calibri 10")
    info27.place(relx=0.1,rely=0.1)
    


def boeb767():
    
    global b67
    b67= Tk()
    boeb767_canvas = Canvas(b67,width=850,height=300,bg="#101357")
    boeb767_canvas.pack()

    boeb767_frame = Frame(boeb767_canvas,bg="white")
    boeb767_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb767_canvas,text='BOEING B767',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info67 = Label(boeb767_frame,text=b767,bg="white",font="calibri 10")
    info67.place(relx=0.1,rely=0.1)



def boeb737():
    
    global b37
    b37= Tk()
    boeb737_canvas = Canvas(b37,width=850,height=300,bg="#101357")
    boeb737_canvas.pack()

    boeb737_frame = Frame(boeb737_canvas,bg="white")
    boeb737_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb737_canvas,text='BOEING B737',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info37 = Label(boeb737_frame,text=b737,bg="white",font="calibri 10")
    info37.place(relx=0.1,rely=0.1)
    

def boeb747():
    
    global b47
    b47= Tk()
    boeb747_canvas = Canvas(b47,width=850,height=300,bg="#101357")
    boeb747_canvas.pack()

    boeb747_frame = Frame(boeb747_canvas,bg="white")
    boeb747_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb747_canvas,text='BOEING B747',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info47 = Label(boeb747_frame,text=b747,bg="white",font="calibri 10")
    info47.place(relx=0.1,rely=0.1)
    

def boeb777():
    
    global b77
    b77= Tk()
    boeb777_canvas = Canvas(b77,width=850,height=300,bg="#101357")
    boeb777_canvas.pack()

    boeb777_frame = Frame(boeb777_canvas,bg="white")
    boeb777_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb777_canvas,text='BOEING B777',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info77 = Label(boeb777_frame,text=b777,bg="white",font="calibri 10")
    info77.place(relx=0.1,rely=0.1)
    
def boeb787():
    
    global b87
    b87= Tk()
    boeb787_canvas = Canvas(b87,width=850,height=300,bg="#101357")
    boeb787_canvas.pack()

    boeb787_frame = Frame(boeb787_canvas,bg="white")
    boeb787_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boeb787_canvas,text='BOEING B787',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info87 = Label(boeb787_frame,text=b787,bg="white",font="calibri 10")
    info87.place(relx=0.1,rely=0.1)
    
def dreamlifter():
    
    
    global bd
    bd= Tk()
    boedream_canvas = Canvas(bd,width=850,height=300,bg="#101357")
    boedream_canvas.pack()

    boedream_frame = Frame(boedream_canvas,bg="white")
    boedream_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(boedream_canvas,text='BOEING DREAMLIFTER',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    infod = Label(boedream_frame,text=dreamlifteri,bg="white",font="calibri 12")
    infod.place(relx=0.1,rely=0.1)
    

def boeing():
    menu.destroy()
    
    global boe 
    boe = Tk()
    
    
    boeing_canvas = Canvas(boe,width=720,height=440,bg="#101357")
    boeing_canvas.pack()

    boeing_frame = Frame(boeing_canvas,bg="steel blue1")
    boeing_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(boeing_canvas,text='BOEING',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    infob = Label(boeing_frame,text=bgi,bg="steel blue1",font="calibri 14")
    infob.place(relx=0.0,rely=0.03)


    b707 = Button(boeing_frame,text='B707',bg="white",font="calibri 12",command=boeb707)
    b707.place(relx=0.25,rely=0.4)
    
    b727 = Button(boeing_frame,text='B727',bg="white",font="calibri 12",command=boeb727)
    b727.place(relx=0.25,rely=0.5)
    
    b737 = Button(boeing_frame,text='B737',bg="white",font="calibri 12", command=boeb737)
    b737.place(relx=0.25,rely=0.6)

    b747 = Button(boeing_frame,text='B747',bg="white",font="calibri 12",command=boeb747)  
    b747.place(relx=0.25,rely=0.7)

    b767 = Button(boeing_frame,text='B767',bg="white",font="calibri 12",command=boeb767)  
    b767.place(relx=0.8,rely=0.4)

    b777 = Button(boeing_frame,text='B777',bg="white",font="calibri 12",command=boeb777)  
    b777.place(relx=0.8,rely=0.5)

    b787 = Button(boeing_frame,text='B787',bg="white",font="calibri 12",command=boeb787)  
    b787.place(relx=0.8,rely=0.6)

    dream = Button(boeing_frame,text='DREAMLIFTER',bg="white",font="calibri 12",command=dreamlifter)  
    dream.place(relx=0.8,rely=0.7)
    def delete_boeing():
        boe.destroy()
        menu2()

    back = Button(boeing_frame,text='BACK',bg="#101357",fg='white',font="calibri 12",command=delete_boeing)
    back.place(relx=0.5,rely=0.5)
    
    

def aira318():
    
    
    global a18
    a18= Tk()
    air318_canvas = Canvas(a18,width=850,height=300,bg="#101357")
    air318_canvas.pack()

    air318_frame = Frame(air318_canvas,bg="white")
    air318_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air318_canvas,text='AIRBUS A318',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info18 = Label(air318_frame,text=a318,bg="white",font="calibri 11")
    info18.place(relx=0.1,rely=0.1)
    

    

def aira319():
    
    global a19
    a19= Tk()
    air319_canvas = Canvas(a19,width=850,height=300,bg="#101357")
    air319_canvas.pack()

    air319_frame = Frame(air319_canvas,bg="white")
    air319_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air319_canvas,text='AIRBUS A319',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info19 = Label(air319_frame,text=a319,bg="white",font="calibri 12")
    info19.place(relx=0.1,rely=0.1)
    def delete_airbus():
        
        a19.destroy()
        airbus2()
    

def aira320():
    
    global a20
    a20= Tk()
    air320_canvas = Canvas(a20,width=850,height=300,bg="#101357")
    air320_canvas.pack()

    air320_frame = Frame(air320_canvas,bg="white")
    air320_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air320_canvas,text='AIRBUS A320',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info20 = Label(air320_frame,text=a320,bg="white",font="calibri 12")
    info20.place(relx=0.1,rely=0.1)
    def delete_airbus():
        
        a20.destroy()
        airbus2()
    
    

def aira321():
    
    global a21
    a21= Tk()
    air321_canvas = Canvas(a21,width=850,height=300,bg="#101357")
    air321_canvas.pack()

    air321_frame = Frame(air321_canvas,bg="white")
    air321_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air321_canvas,text='AIRBUS A321',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info21 = Label(air321_frame,text=a321,bg="white",font="calibri 11")
    info21.place(relx=0.2,rely=0.1)
    def delete_airbus():
        
        a21.destroy()
        airbus2()
    
          
def aira330():
    
    global a30
    a30= Tk()
    air330_canvas = Canvas(a30,width=850,height=300,bg="#101357")
    air330_canvas.pack()

    air330_frame = Frame(air330_canvas,bg="white")
    air330_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air330_canvas,text='AIRBUS A3130',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info30 = Label(air330_frame,text=a330,bg="white",font="calibri 11")
    info30.place(relx=0.1,rely=0.2)
    def delete_airbus():
        
        a30.destroy()
        airbus2()
    

def aira340():
    
    global a40
    a40= Tk()
    air340_canvas = Canvas(a40,width=850,height=300,bg="#101357")
    air340_canvas.pack()

    air340_frame = Frame(air340_canvas,bg="white")
    air340_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air340_canvas,text='AIRBUS A340',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info40 = Label(air340_frame,text=a340,bg="white",font="calibri 12")
    info40.place(relx=0.1,rely=0.1)
    def delete_airbus():
        
        a40.destroy()
        airbus2()
    

def aira350():
    
    global a50
    a50= Tk()
    air350_canvas = Canvas(a50,width=850,height=300,bg="#101357")
    air350_canvas.pack()

    air350_frame = Frame(air350_canvas,bg="white")
    air350_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air350_canvas,text='AIRBUS A350',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info50 = Label(air350_frame,text=a350,bg="white",font="calibri 12")
    info50.place(relx=0.2,rely=0.2)
    def delete_airbus():
        
        a50.destroy()
        airbus2()
   
def aira380():
    
    global a80
    a80= Tk()
    air380_canvas = Canvas(a80,width=850,height=300,bg="#101357")
    air380_canvas.pack()

    air380_frame = Frame(air380_canvas,bg="white")
    air380_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(air380_canvas,text='AIRBUS A380',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info80 = Label(air380_frame,text=a380,bg="white",font="calibri 12")
    info80.place(relx=0.2,rely=0.2)
    def delete_airbus():
        
        a80.destroy()
        airbus2()
    

def beluga():
    
    global bel
    bel= Tk()
    airbel_canvas = Canvas(bel,width=850,height=300,bg="#101357")
    airbel_canvas.pack()

    airbel_frame = Frame(airbel_canvas,bg="white")
    airbel_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    wel = Label(airbel_canvas,text='AIRBUS BELUGA',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    info80 = Label(airbel_frame,text=belugai,bg="white",font="calibri 13")
    info80.place(relx=0.1,rely=0.1)
    def delete_airbus():
        
        bel.destroy()
        airbus2()
    


def airbus():
    menu.destroy()
    
    global air 
    air = Tk()
    
    
    airbus_canvas = Canvas(air,width=720,height=440,bg="#101357")
    airbus_canvas.pack()

    airbus_frame = Frame(airbus_canvas,bg="steel blue1")
    airbus_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(airbus_canvas,text='AIRBUS',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    level = Label(airbus_frame,text=abi,bg="steel blue1",font="calibri 12")
    level.place(relx=0.05,rely=0.03)


    a318 = Button(airbus_frame,text='A318',bg="white",font="calibri 12",command=aira318)
    a318.place(relx=0.25,rely=0.4)
    
    a319 = Button(airbus_frame,text='A319',bg="white",font="calibri 12",command=aira319)
    a319.place(relx=0.25,rely=0.5)
    
    a320 = Button(airbus_frame,text='A320',bg="white",font="calibri 12", command=aira320)
    a320.place(relx=0.25,rely=0.6)

    a321 = Button(airbus_frame,text='A321',bg="white",font="calibri 12",command=aira321)  
    a321.place(relx=0.25,rely=0.7)

    a330 = Button(airbus_frame,text='A330',bg="white",font="calibri 12",command=aira330)  
    a330.place(relx=0.8,rely=0.4)

    a340 = Button(airbus_frame,text='A340',bg="white",font="calibri 12",command=aira340)  
    a340.place(relx=0.8,rely=0.5)

    a350 = Button(airbus_frame,text='A350',bg="white",font="calibri 12",command=aira350)  
    a350.place(relx=0.8,rely=0.6)

    a380 = Button(airbus_frame,text='A380',bg="white",font="calibri 12",command=aira380)  
    a380.place(relx=0.8,rely=0.7)

    bel = Button(airbus_frame,text='BELUGA',bg="white",font="calibri 12",command=beluga)  
    bel.place(relx=0.25,rely=0.8)
    def airdest():
        air.destroy()
        menu2()

    back = Button(airbus_frame,text='BACK',bg="#101357",fg='white',font="calibri 12",command=airdest)
    back.place(relx=0.5,rely=0.5)
          

def menu():
    
    
    
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=720,height=440,bg="#101357")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="steel blue1")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  W I T A  AIRCRAFT JOURNAL ',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.0,rely=0.02)
    level = Label(menu_frame,text='know more about these aircrafts',bg="steel blue1",font="calibri 18")
    level.place(relx=0.22,rely=0.03)


    airbus1 = Button(menu_frame,text='AIRBUS',fg="white",bg="#101357",font="Broadway 22",command=airbus)
    airbus1.place(relx=0.1,rely=0.4)
    
    boeing1 = Button(menu_frame,text='BOEING',fg="white",bg="#101357",font="Broadway 22",command=boeing)
    boeing1.place(relx=0.6,rely=0.4)

    embraero1 = Button(menu_frame,text='EMBRAER',fg="white",bg="#101357",font="Broadway 22",command=embraero)
    embraero1.place(relx=0.07,rely=0.6)

    bombardier1 = Button(menu_frame,text='BOMBARDIER',fg="white",bg="#101357",font="Broadway 22",command=bombardier)
    bombardier1.place(relx=0.57,rely=0.6)
    
    
    menu.mainloop()     

def start():
    global root 
    root = Tk()
    
    start_canvas = Canvas(root,width = 500,height =350, bg = 'navajo white',)
    start_canvas.pack()
    start_frame= Frame(start_canvas,bg = "navajo white")
    start_frame.place(relwidth=0.8,relheight= 0.8)

    wel = Label(start_canvas,text='PROJECT BY \nSHIVKUMAR DEVANE',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.15,rely=0.2)
    wel2 = Label(start_canvas,text="  What's in the Air",fg="#101357",bg="navajo white") 
    wel2.config(font=('Broadway 24'))
    wel2.place(relx=0.15,rely=0.0)
    def strata():
        root.destroy()
        menu()

    button = Button(root, text='click here for Aircraft Journal',font= 'Broadway 18',command = strata,relief= RAISED) 
    button.place(relx=0.1,rely=0.8)
    


    root.mainloop()


    
    
if __name__=='__main__':
    start()









