# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Tue 18 Aug 2020 11:57:58


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1, L.VVV11, L.VVV3, L.VVV4, L.VVV7, L.VVV8, L.VVV9 ],
             couplings = {(0,2):C.GC_379,(0,0):C.GC_402,(0,1):C.GC_232,(0,6):C.GC_231,(0,4):C.GC_3,(0,3):C.GC_404,(0,5):C.GC_408})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV7 ],
             couplings = {(0,0):C.GC_251})

V_3 = Vertex(name = 'V_3',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV11, L.VVV2, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
             couplings = {(0,2):C.GC_403,(0,1):C.GC_378,(0,0):C.GC_64,(0,6):C.GC_63,(0,5):C.GC_145,(0,3):C.GC_413,(0,4):C.GC_380})

V_4 = Vertex(name = 'V_4',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV7 ],
             couplings = {(0,0):C.GC_247})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV10, L.VVV3, L.VVV7, L.VVV9 ],
             couplings = {(0,1):C.GC_381,(0,0):C.GC_19,(0,3):C.GC_18,(0,2):C.GC_7})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
             couplings = {(0,7):C.GC_75,(1,6):C.GC_75,(2,5):C.GC_75,(0,4):C.GC_74,(1,3):C.GC_74,(2,2):C.GC_74,(1,8):C.GC_8,(0,0):C.GC_8,(2,1):C.GC_8})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g, P.g, P.g ],
             color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
             lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV2, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV25, L.VVVVV28, L.VVVVV29, L.VVVVV3, L.VVVVV30, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV37, L.VVVVV4, L.VVVVV40, L.VVVVV41, L.VVVVV42, L.VVVVV43, L.VVVVV44, L.VVVVV46, L.VVVVV47, L.VVVVV48, L.VVVVV49, L.VVVVV5, L.VVVVV50, L.VVVVV51, L.VVVVV53, L.VVVVV54, L.VVVVV6, L.VVVVV7, L.VVVVV9 ],
             couplings = {(27,37):C.GC_80,(24,8):C.GC_81,(21,12):C.GC_80,(18,11):C.GC_81,(15,9):C.GC_80,(12,27):C.GC_80,(28,42):C.GC_80,(25,15):C.GC_81,(22,14):C.GC_80,(9,16):C.GC_80,(6,13):C.GC_81,(3,43):C.GC_81,(29,0):C.GC_81,(19,20):C.GC_80,(16,18):C.GC_81,(10,17):C.GC_80,(7,21):C.GC_81,(0,44):C.GC_80,(26,10):C.GC_80,(20,1):C.GC_81,(13,24):C.GC_80,(11,2):C.GC_81,(4,22):C.GC_80,(1,23):C.GC_80,(23,19):C.GC_81,(17,4):C.GC_80,(14,25):C.GC_81,(8,3):C.GC_80,(5,28):C.GC_81,(2,26):C.GC_81,(24,29):C.GC_79,(21,30):C.GC_78,(18,30):C.GC_79,(15,29):C.GC_78,(28,6):C.GC_79,(22,34):C.GC_79,(9,34):C.GC_78,(3,6):C.GC_78,(29,7):C.GC_79,(16,35):C.GC_79,(10,35):C.GC_78,(0,7):C.GC_78,(26,39):C.GC_78,(20,38):C.GC_78,(4,38):C.GC_79,(1,39):C.GC_79,(25,33):C.GC_79,(6,33):C.GC_78,(19,36):C.GC_79,(7,36):C.GC_78,(23,41):C.GC_78,(17,40):C.GC_78,(5,40):C.GC_79,(2,41):C.GC_79,(27,5):C.GC_79,(12,5):C.GC_78,(13,31):C.GC_79,(11,31):C.GC_78,(14,32):C.GC_78,(8,32):C.GC_79})

V_8 = Vertex(name = 'V_8',
             particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
             color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
             lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV19, L.VVVVVV2, L.VVVVVV20, L.VVVVVV21, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV26, L.VVVVVV27, L.VVVVVV28, L.VVVVVV29, L.VVVVVV3, L.VVVVVV30, L.VVVVVV31, L.VVVVVV32, L.VVVVVV33, L.VVVVVV34, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV38, L.VVVVVV39, L.VVVVVV4, L.VVVVVV40, L.VVVVVV41, L.VVVVVV42, L.VVVVVV43, L.VVVVVV44, L.VVVVVV45, L.VVVVVV46, L.VVVVVV47, L.VVVVVV48, L.VVVVVV49, L.VVVVVV5, L.VVVVVV50, L.VVVVVV51, L.VVVVVV52, L.VVVVVV54, L.VVVVVV55, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV59, L.VVVVVV6, L.VVVVVV60, L.VVVVVV61, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
             couplings = {(41,58):C.GC_86,(47,59):C.GC_85,(53,7):C.GC_86,(35,57):C.GC_85,(46,14):C.GC_86,(52,17):C.GC_85,(34,2):C.GC_86,(40,10):C.GC_85,(51,37):C.GC_86,(33,4):C.GC_85,(39,21):C.GC_86,(45,30):C.GC_85,(17,57):C.GC_86,(23,2):C.GC_85,(29,4):C.GC_86,(11,58):C.GC_85,(22,10):C.GC_86,(28,21):C.GC_85,(10,59):C.GC_86,(16,14):C.GC_85,(27,30):C.GC_86,(9,7):C.GC_85,(15,17):C.GC_86,(21,37):C.GC_85,(59,0):C.GC_86,(65,11):C.GC_85,(71,44):C.GC_86,(64,12):C.GC_86,(70,23):C.GC_85,(58,16):C.GC_85,(69,31):C.GC_86,(57,19):C.GC_86,(63,39):C.GC_85,(5,0):C.GC_85,(20,16):C.GC_86,(26,19):C.GC_85,(4,11):C.GC_86,(14,12):C.GC_85,(25,39):C.GC_86,(3,44):C.GC_85,(13,23):C.GC_86,(19,31):C.GC_85,(77,22):C.GC_85,(83,33):C.GC_86,(76,1):C.GC_86,(82,8):C.GC_85,(81,40):C.GC_86,(75,35):C.GC_85,(2,22):C.GC_86,(8,1):C.GC_85,(24,35):C.GC_86,(1,33):C.GC_85,(7,8):C.GC_86,(18,40):C.GC_85,(89,54):C.GC_86,(88,6):C.GC_85,(87,25):C.GC_86,(0,54):C.GC_85,(6,6):C.GC_86,(12,25):C.GC_85,(62,15):C.GC_86,(68,18):C.GC_85,(56,13):C.GC_85,(67,38):C.GC_86,(55,24):C.GC_86,(61,32):C.GC_85,(44,13):C.GC_86,(50,24):C.GC_85,(38,15):C.GC_85,(49,32):C.GC_86,(37,18):C.GC_86,(43,38):C.GC_85,(74,3):C.GC_86,(80,5):C.GC_85,(79,34):C.GC_86,(73,42):C.GC_85,(32,3):C.GC_85,(48,42):C.GC_86,(31,5):C.GC_86,(42,34):C.GC_85,(86,9):C.GC_85,(85,20):C.GC_86,(30,9):C.GC_86,(36,20):C.GC_85,(78,41):C.GC_86,(72,36):C.GC_85,(66,36):C.GC_86,(60,41):C.GC_85,(65,43):C.GC_83,(71,46):C.GC_84,(77,46):C.GC_83,(83,43):C.GC_84,(41,28):C.GC_83,(53,50):C.GC_83,(76,50):C.GC_84,(88,28):C.GC_84,(35,29):C.GC_83,(52,53):C.GC_83,(64,53):C.GC_84,(87,29):C.GC_84,(34,52):C.GC_84,(40,51):C.GC_84,(69,51):C.GC_83,(81,52):C.GC_83,(17,29):C.GC_84,(23,52):C.GC_83,(80,52):C.GC_84,(86,29):C.GC_83,(11,28):C.GC_84,(22,51):C.GC_83,(68,51):C.GC_84,(85,28):C.GC_83,(9,50):C.GC_84,(15,53):C.GC_84,(61,53):C.GC_83,(73,50):C.GC_83,(4,43):C.GC_84,(14,53):C.GC_83,(49,53):C.GC_84,(78,43):C.GC_83,(3,46):C.GC_83,(19,51):C.GC_84,(37,51):C.GC_83,(72,46):C.GC_84,(2,46):C.GC_84,(8,50):C.GC_83,(48,50):C.GC_84,(66,46):C.GC_83,(1,43):C.GC_83,(18,52):C.GC_84,(31,52):C.GC_83,(60,43):C.GC_84,(6,28):C.GC_83,(12,29):C.GC_83,(30,29):C.GC_84,(36,28):C.GC_84,(47,48):C.GC_83,(82,48):C.GC_84,(46,55):C.GC_83,(70,55):C.GC_84,(33,56):C.GC_84,(39,49):C.GC_84,(63,49):C.GC_83,(75,56):C.GC_83,(29,56):C.GC_83,(74,56):C.GC_84,(28,49):C.GC_83,(62,49):C.GC_84,(10,48):C.GC_84,(16,55):C.GC_84,(67,55):C.GC_83,(79,48):C.GC_83,(25,49):C.GC_84,(38,49):C.GC_83,(13,55):C.GC_83,(43,55):C.GC_84,(24,56):C.GC_84,(32,56):C.GC_83,(7,48):C.GC_83,(42,48):C.GC_84,(84,26):C.GC_86,(54,26):C.GC_85,(59,27):C.GC_83,(89,27):C.GC_84,(51,45):C.GC_83,(58,45):C.GC_84,(21,45):C.GC_84,(55,45):C.GC_83,(5,27):C.GC_84,(20,45):C.GC_83,(50,45):C.GC_84,(84,27):C.GC_83,(0,27):C.GC_83,(54,27):C.GC_84,(45,47):C.GC_84,(57,47):C.GC_83,(27,47):C.GC_83,(56,47):C.GC_84,(26,47):C.GC_84,(44,47):C.GC_83})

V_9 = Vertex(name = 'V_9',
             particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
             couplings = {(0,1):C.GC_234,(0,0):C.GC_233,(0,2):C.GC_5})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_254})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_409})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
              couplings = {(0,2):C.GC_70,(0,1):C.GC_69,(0,0):C.GC_158})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_248})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_421})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV16, L.VVVVV8 ],
              couplings = {(0,1):C.GC_236,(0,0):C.GC_235})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_184,(0,0):C.GC_182,(0,2):C.GC_102})

V_17 = Vertex(name = 'V_17',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_106})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV26, L.VVVVV55 ],
              couplings = {(0,0):C.GC_73,(0,1):C.GC_72})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV32, L.VVVVV57 ],
              couplings = {(0,0):C.GC_189,(0,1):C.GC_187})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_191})

V_21 = Vertex(name = 'V_21',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_185,(0,0):C.GC_183,(0,2):C.GC_253})

V_22 = Vertex(name = 'V_22',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_104})

V_23 = Vertex(name = 'V_23',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_410})

V_24 = Vertex(name = 'V_24',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV38, L.VVVVV45 ],
              couplings = {(0,0):C.GC_190,(0,1):C.GC_188})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV27, L.VVVVV52 ],
              couplings = {(0,0):C.GC_114,(0,1):C.GC_112})

V_26 = Vertex(name = 'V_26',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV62 ],
              couplings = {(0,0):C.GC_116})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_100})

V_28 = Vertex(name = 'V_28',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV39, L.VVVVV56 ],
              couplings = {(0,0):C.GC_115,(0,1):C.GC_113})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_55})

V_30 = Vertex(name = 'V_30',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_229,(0,1):C.GC_226})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_245,(0,1):C.GC_244})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_309,(0,1):C.GC_260})

V_33 = Vertex(name = 'V_33',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_369,(0,1):C.GC_308})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_374,(0,1):C.GC_366})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_373})

V_36 = Vertex(name = 'V_36',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_24,(0,1):C.GC_23})

V_37 = Vertex(name = 'V_37',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
              couplings = {(0,0):C.GC_305,(0,1):C.GC_261,(0,3):C.GC_274,(0,2):C.GC_270,(0,4):C.GC_265})

V_38 = Vertex(name = 'V_38',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_304})

V_39 = Vertex(name = 'V_39',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_26,(0,2):C.GC_25,(0,1):C.GC_101})

V_40 = Vertex(name = 'V_40',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_105})

V_41 = Vertex(name = 'V_41',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_107})

V_42 = Vertex(name = 'V_42',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_307,(0,2):C.GC_306,(0,1):C.GC_323})

V_43 = Vertex(name = 'V_43',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_325})

V_44 = Vertex(name = 'V_44',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_327})

V_45 = Vertex(name = 'V_45',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_328})

V_46 = Vertex(name = 'V_46',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_256,(0,1):C.GC_255})

V_47 = Vertex(name = 'V_47',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_224,(0,1):C.GC_223})

V_48 = Vertex(name = 'V_48',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_230,(0,1):C.GC_225})

V_49 = Vertex(name = 'V_49',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_420,(0,1):C.GC_264})

V_50 = Vertex(name = 'V_50',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_364,(0,1):C.GC_419})

V_51 = Vertex(name = 'V_51',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_370,(0,1):C.GC_363})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_365})

V_53 = Vertex(name = 'V_53',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_58,(0,2):C.GC_57,(0,1):C.GC_99})

V_54 = Vertex(name = 'V_54',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_228,(0,2):C.GC_227,(0,1):C.GC_103})

V_55 = Vertex(name = 'V_55',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_243,(0,2):C.GC_242,(0,1):C.GC_108})

V_56 = Vertex(name = 'V_56',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_382})

V_57 = Vertex(name = 'V_57',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_405})

V_58 = Vertex(name = 'V_58',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_311,(0,2):C.GC_310,(0,1):C.GC_418})

V_59 = Vertex(name = 'V_59',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_368,(0,2):C.GC_367,(0,1):C.GC_324})

V_60 = Vertex(name = 'V_60',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_372,(0,2):C.GC_371,(0,1):C.GC_326})

V_61 = Vertex(name = 'V_61',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_329})

V_62 = Vertex(name = 'V_62',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_416})

V_63 = Vertex(name = 'V_63',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_417})

V_64 = Vertex(name = 'V_64',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3, L.VVVSS6 ],
              couplings = {(0,0):C.GC_77,(0,1):C.GC_76})

V_65 = Vertex(name = 'V_65',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS10, L.VVVS3, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
              couplings = {(0,1):C.GC_318,(0,4):C.GC_266,(0,0):C.GC_275,(0,5):C.GC_271,(0,3):C.GC_268,(0,2):C.GC_262})

V_66 = Vertex(name = 'V_66',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS6 ],
              couplings = {(0,0):C.GC_317})

V_67 = Vertex(name = 'V_67',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3, L.VVVSS4, L.VVVSS6 ],
              couplings = {(0,1):C.GC_68,(0,0):C.GC_180,(0,3):C.GC_65,(0,2):C.GC_179})

V_68 = Vertex(name = 'V_68',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
              couplings = {(0,1):C.GC_315,(0,0):C.GC_360,(0,3):C.GC_312,(0,2):C.GC_359})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2, L.VVVSS3, L.VVVSS5, L.VVVSS6 ],
              couplings = {(0,1):C.GC_181,(0,0):C.GC_67,(0,3):C.GC_178,(0,2):C.GC_66})

V_70 = Vertex(name = 'V_70',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
              couplings = {(0,1):C.GC_361,(0,0):C.GC_314,(0,3):C.GC_358,(0,2):C.GC_313})

V_71 = Vertex(name = 'V_71',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_9,(0,2):C.GC_21,(0,1):C.GC_22})

V_72 = Vertex(name = 'V_72',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_10})

V_73 = Vertex(name = 'V_73',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_11})

V_74 = Vertex(name = 'V_74',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_12})

V_75 = Vertex(name = 'V_75',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_375})

V_76 = Vertex(name = 'V_76',
              particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_20})

V_77 = Vertex(name = 'V_77',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_297,(0,2):C.GC_302,(0,1):C.GC_303})

V_78 = Vertex(name = 'V_78',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_298})

V_79 = Vertex(name = 'V_79',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_299})

V_80 = Vertex(name = 'V_80',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_300})

V_81 = Vertex(name = 'V_81',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_415})

V_82 = Vertex(name = 'V_82',
              particles = [ P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_301})

V_83 = Vertex(name = 'V_83',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_82,(0,0):C.GC_82,(2,2):C.GC_82})

V_84 = Vertex(name = 'V_84',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS17, L.VVVVS19, L.VVVVS2, L.VVVVS3, L.VVVVS4, L.VVVVS7, L.VVVVS8 ],
              couplings = {(2,5):C.GC_267,(2,8):C.GC_276,(1,4):C.GC_267,(1,9):C.GC_276,(2,6):C.GC_273,(0,11):C.GC_269,(0,12):C.GC_277,(1,7):C.GC_273,(0,3):C.GC_272,(1,2):C.GC_269,(2,1):C.GC_269,(0,10):C.GC_267,(1,13):C.GC_263,(0,0):C.GC_263,(2,14):C.GC_263})

V_85 = Vertex(name = 'V_85',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS7, L.VVVVS8 ],
              couplings = {(1,1):C.GC_319,(0,0):C.GC_319,(2,2):C.GC_319})

V_86 = Vertex(name = 'V_86',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_71})

V_87 = Vertex(name = 'V_87',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS6 ],
              couplings = {(0,0):C.GC_316})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_109})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS6 ],
              couplings = {(0,0):C.GC_330})

V_90 = Vertex(name = 'V_90',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS5 ],
              couplings = {(0,0):C.GC_186})

V_91 = Vertex(name = 'V_91',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS9 ],
              couplings = {(0,0):C.GC_362})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_110})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_331})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_111})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS6 ],
              couplings = {(0,0):C.GC_332})

V_96 = Vertex(name = 'V_96',
              particles = [ P.H, P.H, P.H, P.H1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_91})

V_97 = Vertex(name = 'V_97',
              particles = [ P.H, P.H, P.H1, P.H1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_96})

V_98 = Vertex(name = 'V_98',
              particles = [ P.H, P.H1, P.H1, P.H1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_97})

V_99 = Vertex(name = 'V_99',
              particles = [ P.H1, P.H1, P.H1, P.H1 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_98})

V_100 = Vertex(name = 'V_100',
               particles = [ P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_320})

V_101 = Vertex(name = 'V_101',
               particles = [ P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_321})

V_102 = Vertex(name = 'V_102',
               particles = [ P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_322})

V_103 = Vertex(name = 'V_103',
               particles = [ P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_88})

V_104 = Vertex(name = 'V_104',
               particles = [ P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_93})

V_105 = Vertex(name = 'V_105',
               particles = [ P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_88})

V_106 = Vertex(name = 'V_106',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_107 = Vertex(name = 'V_107',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_121})

V_108 = Vertex(name = 'V_108',
               particles = [ P.W__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_125})

V_109 = Vertex(name = 'V_109',
               particles = [ P.W__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_333})

V_110 = Vertex(name = 'V_110',
               particles = [ P.W__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_335})

V_111 = Vertex(name = 'V_111',
               particles = [ P.a, P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_89})

V_112 = Vertex(name = 'V_112',
               particles = [ P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_204})

V_113 = Vertex(name = 'V_113',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_210})

V_114 = Vertex(name = 'V_114',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_121})

V_115 = Vertex(name = 'V_115',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_125})

V_116 = Vertex(name = 'V_116',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_129})

V_117 = Vertex(name = 'V_117',
               particles = [ P.W1__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_335})

V_118 = Vertex(name = 'V_118',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_337})

V_119 = Vertex(name = 'V_119',
               particles = [ P.a, P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_94})

V_120 = Vertex(name = 'V_120',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_210})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_213})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_122})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_126})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_130})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_121})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_333})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_204})

V_129 = Vertex(name = 'V_129',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_130 = Vertex(name = 'V_130',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_121})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W1__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_125})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W1__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_333})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W1__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_335})

V_134 = Vertex(name = 'V_134',
               particles = [ P.a, P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_89})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_204})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV7 ],
               couplings = {(0,0):C.GC_210})

V_137 = Vertex(name = 'V_137',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_118})

V_138 = Vertex(name = 'V_138',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_122})

V_139 = Vertex(name = 'V_139',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_126})

V_140 = Vertex(name = 'V_140',
               particles = [ P.W__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_118})

V_141 = Vertex(name = 'V_141',
               particles = [ P.W1__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_122})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_205})

V_143 = Vertex(name = 'V_143',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_211})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_205})

V_145 = Vertex(name = 'V_145',
               particles = [ P.Z, P.Z, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_119})

V_146 = Vertex(name = 'V_146',
               particles = [ P.Z, P.Z, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_123})

V_147 = Vertex(name = 'V_147',
               particles = [ P.Z, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_334})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_149 = Vertex(name = 'V_149',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_124})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_151 = Vertex(name = 'V_151',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_211})

V_152 = Vertex(name = 'V_152',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_214})

V_153 = Vertex(name = 'V_153',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_205})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_211})

V_155 = Vertex(name = 'V_155',
               particles = [ P.Z, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_119})

V_156 = Vertex(name = 'V_156',
               particles = [ P.Z, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_123})

V_157 = Vertex(name = 'V_157',
               particles = [ P.Z, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_127})

V_158 = Vertex(name = 'V_158',
               particles = [ P.Z, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_334})

V_159 = Vertex(name = 'V_159',
               particles = [ P.Z, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_336})

V_160 = Vertex(name = 'V_160',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_124})

V_161 = Vertex(name = 'V_161',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_128})

V_162 = Vertex(name = 'V_162',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_163 = Vertex(name = 'V_163',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_124})

V_164 = Vertex(name = 'V_164',
               particles = [ P.Z1, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_123})

V_165 = Vertex(name = 'V_165',
               particles = [ P.Z1, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_127})

V_166 = Vertex(name = 'V_166',
               particles = [ P.Z1, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_131})

V_167 = Vertex(name = 'V_167',
               particles = [ P.Z1, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_336})

V_168 = Vertex(name = 'V_168',
               particles = [ P.Z1, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_338})

V_169 = Vertex(name = 'V_169',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_128})

V_170 = Vertex(name = 'V_170',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_132})

V_171 = Vertex(name = 'V_171',
               particles = [ P.W__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_124})

V_172 = Vertex(name = 'V_172',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_128})

V_173 = Vertex(name = 'V_173',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_657,(0,2):C.GC_656})

V_174 = Vertex(name = 'V_174',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_252,(0,1):C.GC_671,(0,2):C.GC_670})

V_175 = Vertex(name = 'V_175',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_408})

V_176 = Vertex(name = 'V_176',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_750,(0,2):C.GC_749})

V_177 = Vertex(name = 'V_177',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_252,(0,1):C.GC_764,(0,2):C.GC_763})

V_178 = Vertex(name = 'V_178',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_408})

V_179 = Vertex(name = 'V_179',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_1101,(0,2):C.GC_1100})

V_180 = Vertex(name = 'V_180',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_252,(0,1):C.GC_1115,(0,2):C.GC_1114})

V_181 = Vertex(name = 'V_181',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_408})

V_182 = Vertex(name = 'V_182',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_217,(0,3):C.GC_144,(0,5):C.GC_220,(0,6):C.GC_222,(0,4):C.GC_394,(0,1):C.GC_659,(0,2):C.GC_658})

V_183 = Vertex(name = 'V_183',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_259,(0,3):C.GC_157,(0,4):C.GC_377,(0,1):C.GC_669,(0,2):C.GC_668})

V_184 = Vertex(name = 'V_184',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_414,(0,1):C.GC_395})

V_185 = Vertex(name = 'V_185',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_397})

V_186 = Vertex(name = 'V_186',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_217,(0,3):C.GC_144,(0,5):C.GC_220,(0,6):C.GC_222,(0,4):C.GC_394,(0,1):C.GC_752,(0,2):C.GC_751})

V_187 = Vertex(name = 'V_187',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_259,(0,3):C.GC_157,(0,4):C.GC_377,(0,1):C.GC_762,(0,2):C.GC_761})

V_188 = Vertex(name = 'V_188',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_414,(0,1):C.GC_395})

V_189 = Vertex(name = 'V_189',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_397})

V_190 = Vertex(name = 'V_190',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_217,(0,3):C.GC_144,(0,5):C.GC_220,(0,6):C.GC_222,(0,4):C.GC_394,(0,1):C.GC_1103,(0,2):C.GC_1102})

V_191 = Vertex(name = 'V_191',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_259,(0,3):C.GC_157,(0,4):C.GC_377,(0,1):C.GC_1113,(0,2):C.GC_1112})

V_192 = Vertex(name = 'V_192',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_414,(0,1):C.GC_395})

V_193 = Vertex(name = 'V_193',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_397})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_589,(0,2):C.GC_588})

V_195 = Vertex(name = 'V_195',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_605,(0,2):C.GC_604})

V_196 = Vertex(name = 'V_196',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_406})

V_197 = Vertex(name = 'V_197',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_849,(0,2):C.GC_848})

V_198 = Vertex(name = 'V_198',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_865,(0,2):C.GC_864})

V_199 = Vertex(name = 'V_199',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_406})

V_200 = Vertex(name = 'V_200',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_459,(0,2):C.GC_458})

V_201 = Vertex(name = 'V_201',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_249,(0,1):C.GC_475,(0,2):C.GC_474})

V_202 = Vertex(name = 'V_202',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_406})

V_203 = Vertex(name = 'V_203',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_1229,(0,2):C.GC_1228})

V_204 = Vertex(name = 'V_204',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_1252,(0,2):C.GC_1251})

V_205 = Vertex(name = 'V_205',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_407})

V_206 = Vertex(name = 'V_206',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_508,(0,2):C.GC_507})

V_207 = Vertex(name = 'V_207',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_531,(0,2):C.GC_530})

V_208 = Vertex(name = 'V_208',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_407})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_936,(0,2):C.GC_935})

V_210 = Vertex(name = 'V_210',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_250,(0,1):C.GC_959,(0,2):C.GC_958})

V_211 = Vertex(name = 'V_211',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_407})

V_212 = Vertex(name = 'V_212',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_582,(0,2):C.GC_581})

V_213 = Vertex(name = 'V_213',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_842,(0,2):C.GC_841})

V_214 = Vertex(name = 'V_214',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_452,(0,2):C.GC_451})

V_215 = Vertex(name = 'V_215',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_1231,(0,2):C.GC_1230})

V_216 = Vertex(name = 'V_216',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_510,(0,2):C.GC_509})

V_217 = Vertex(name = 'V_217',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_938,(0,2):C.GC_937})

V_218 = Vertex(name = 'V_218',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1235,(0,0):C.GC_585,(0,1):C.GC_134,(0,3):C.GC_1289})

V_219 = Vertex(name = 'V_219',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1237,(0,0):C.GC_587,(0,1):C.GC_147,(0,3):C.GC_1290})

V_220 = Vertex(name = 'V_220',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_384})

V_221 = Vertex(name = 'V_221',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_135,(0,1):C.GC_1361})

V_222 = Vertex(name = 'V_222',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_148,(0,1):C.GC_1362})

V_223 = Vertex(name = 'V_223',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_385})

V_224 = Vertex(name = 'V_224',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_1271})

V_225 = Vertex(name = 'V_225',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_149,(0,1):C.GC_1272})

V_226 = Vertex(name = 'V_226',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_386})

V_227 = Vertex(name = 'V_227',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_624})

V_228 = Vertex(name = 'V_228',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_150,(0,1):C.GC_625})

V_229 = Vertex(name = 'V_229',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_387})

V_230 = Vertex(name = 'V_230',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_514,(0,0):C.GC_845,(0,1):C.GC_138,(0,3):C.GC_884})

V_231 = Vertex(name = 'V_231',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_516,(0,0):C.GC_847,(0,1):C.GC_151,(0,3):C.GC_885})

V_232 = Vertex(name = 'V_232',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_388})

V_233 = Vertex(name = 'V_233',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_139,(0,1):C.GC_550})

V_234 = Vertex(name = 'V_234',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_152,(0,1):C.GC_551})

V_235 = Vertex(name = 'V_235',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_389})

V_236 = Vertex(name = 'V_236',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_140,(0,1):C.GC_996})

V_237 = Vertex(name = 'V_237',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_153,(0,1):C.GC_997})

V_238 = Vertex(name = 'V_238',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_390})

V_239 = Vertex(name = 'V_239',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_141,(0,1):C.GC_1068})

V_240 = Vertex(name = 'V_240',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_1069})

V_241 = Vertex(name = 'V_241',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_391})

V_242 = Vertex(name = 'V_242',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_942,(0,0):C.GC_455,(0,1):C.GC_142,(0,3):C.GC_978})

V_243 = Vertex(name = 'V_243',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_944,(0,0):C.GC_457,(0,1):C.GC_155,(0,3):C.GC_979})

V_244 = Vertex(name = 'V_244',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_392})

V_245 = Vertex(name = 'V_245',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1285,(0,0):C.GC_160})

V_246 = Vertex(name = 'V_246',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1286})

V_247 = Vertex(name = 'V_247',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1357,(0,0):C.GC_161})

V_248 = Vertex(name = 'V_248',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1358})

V_249 = Vertex(name = 'V_249',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1267,(0,0):C.GC_162})

V_250 = Vertex(name = 'V_250',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1268})

V_251 = Vertex(name = 'V_251',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_620,(0,0):C.GC_163})

V_252 = Vertex(name = 'V_252',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_621})

V_253 = Vertex(name = 'V_253',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_880,(0,0):C.GC_164})

V_254 = Vertex(name = 'V_254',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_881})

V_255 = Vertex(name = 'V_255',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_546,(0,0):C.GC_165})

V_256 = Vertex(name = 'V_256',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_547})

V_257 = Vertex(name = 'V_257',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_992,(0,0):C.GC_166})

V_258 = Vertex(name = 'V_258',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_993})

V_259 = Vertex(name = 'V_259',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1064,(0,0):C.GC_167})

V_260 = Vertex(name = 'V_260',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1065})

V_261 = Vertex(name = 'V_261',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_974,(0,0):C.GC_168})

V_262 = Vertex(name = 'V_262',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_975})

V_263 = Vertex(name = 'V_263',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_1209,(0,3):C.GC_559,(0,2):C.GC_1287,(0,0):C.GC_340})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1211,(0,2):C.GC_561,(0,1):C.GC_1288})

V_265 = Vertex(name = 'V_265',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1359,(0,0):C.GC_341})

V_266 = Vertex(name = 'V_266',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1360})

V_267 = Vertex(name = 'V_267',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1269,(0,0):C.GC_342})

V_268 = Vertex(name = 'V_268',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1270})

V_269 = Vertex(name = 'V_269',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_622,(0,0):C.GC_343})

V_270 = Vertex(name = 'V_270',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_623})

V_271 = Vertex(name = 'V_271',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_488,(0,3):C.GC_819,(0,2):C.GC_882,(0,0):C.GC_344})

V_272 = Vertex(name = 'V_272',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_490,(0,2):C.GC_821,(0,1):C.GC_883})

V_273 = Vertex(name = 'V_273',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_548,(0,0):C.GC_345})

V_274 = Vertex(name = 'V_274',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_549})

V_275 = Vertex(name = 'V_275',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_994,(0,0):C.GC_346})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_995})

V_277 = Vertex(name = 'V_277',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1066,(0,0):C.GC_347})

V_278 = Vertex(name = 'V_278',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1067})

V_279 = Vertex(name = 'V_279',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_914,(0,3):C.GC_429,(0,2):C.GC_976,(0,0):C.GC_348})

V_280 = Vertex(name = 'V_280',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_916,(0,2):C.GC_431,(0,1):C.GC_977})

V_281 = Vertex(name = 'V_281',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_653,(0,1):C.GC_133})

V_282 = Vertex(name = 'V_282',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_655,(0,1):C.GC_146})

V_283 = Vertex(name = 'V_283',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_284 = Vertex(name = 'V_284',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_746,(0,1):C.GC_133})

V_285 = Vertex(name = 'V_285',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_748,(0,1):C.GC_146})

V_286 = Vertex(name = 'V_286',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_287 = Vertex(name = 'V_287',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_1097,(0,1):C.GC_133})

V_288 = Vertex(name = 'V_288',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,0):C.GC_1099,(0,1):C.GC_146})

V_289 = Vertex(name = 'V_289',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_290 = Vertex(name = 'V_290',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_291 = Vertex(name = 'V_291',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_292 = Vertex(name = 'V_292',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_293 = Vertex(name = 'V_293',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_631,(0,0):C.GC_339})

V_294 = Vertex(name = 'V_294',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_633})

V_295 = Vertex(name = 'V_295',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_724,(0,0):C.GC_339})

V_296 = Vertex(name = 'V_296',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_726})

V_297 = Vertex(name = 'V_297',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_1075,(0,0):C.GC_339})

V_298 = Vertex(name = 'V_298',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_1077})

V_299 = Vertex(name = 'V_299',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_586,(0,0):C.GC_1234,(0,1):C.GC_1418,(0,3):C.GC_1550})

V_300 = Vertex(name = 'V_300',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_587,(0,0):C.GC_1237,(0,1):C.GC_1419,(0,3):C.GC_1551})

V_301 = Vertex(name = 'V_301',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1423})

V_302 = Vertex(name = 'V_302',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2030,(0,1):C.GC_2108})

V_303 = Vertex(name = 'V_303',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2031,(0,1):C.GC_2109})

V_304 = Vertex(name = 'V_304',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2035})

V_305 = Vertex(name = 'V_305',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2642,(0,1):C.GC_2749})

V_306 = Vertex(name = 'V_306',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2643,(0,1):C.GC_2750})

V_307 = Vertex(name = 'V_307',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2648})

V_308 = Vertex(name = 'V_308',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1622,(0,1):C.GC_1790})

V_309 = Vertex(name = 'V_309',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1623,(0,1):C.GC_1791})

V_310 = Vertex(name = 'V_310',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1627})

V_311 = Vertex(name = 'V_311',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_846,(0,0):C.GC_513,(0,1):C.GC_2234,(0,3):C.GC_2348})

V_312 = Vertex(name = 'V_312',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_847,(0,0):C.GC_516,(0,1):C.GC_2235,(0,3):C.GC_2349})

V_313 = Vertex(name = 'V_313',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2239})

V_314 = Vertex(name = 'V_314',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2847,(0,1):C.GC_2990})

V_315 = Vertex(name = 'V_315',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2848,(0,1):C.GC_2991})

V_316 = Vertex(name = 'V_316',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2853})

V_317 = Vertex(name = 'V_317',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1826,(0,1):C.GC_1934})

V_318 = Vertex(name = 'V_318',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1827,(0,1):C.GC_1935})

V_319 = Vertex(name = 'V_319',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1831})

V_320 = Vertex(name = 'V_320',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2438,(0,1):C.GC_2492})

V_321 = Vertex(name = 'V_321',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2439,(0,1):C.GC_2493})

V_322 = Vertex(name = 'V_322',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2443})

V_323 = Vertex(name = 'V_323',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_456,(0,0):C.GC_941,(0,1):C.GC_3052,(0,3):C.GC_3135})

V_324 = Vertex(name = 'V_324',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_457,(0,0):C.GC_944,(0,1):C.GC_3053,(0,3):C.GC_3136})

V_325 = Vertex(name = 'V_325',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3058})

V_326 = Vertex(name = 'V_326',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1546,(0,0):C.GC_1420})

V_327 = Vertex(name = 'V_327',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1547})

V_328 = Vertex(name = 'V_328',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2104,(0,0):C.GC_2032})

V_329 = Vertex(name = 'V_329',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2105})

V_330 = Vertex(name = 'V_330',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2745,(0,0):C.GC_2644})

V_331 = Vertex(name = 'V_331',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2746})

V_332 = Vertex(name = 'V_332',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1786,(0,0):C.GC_1624})

V_333 = Vertex(name = 'V_333',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1787})

V_334 = Vertex(name = 'V_334',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2344,(0,0):C.GC_2236})

V_335 = Vertex(name = 'V_335',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2345})

V_336 = Vertex(name = 'V_336',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2986,(0,0):C.GC_2849})

V_337 = Vertex(name = 'V_337',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2987})

V_338 = Vertex(name = 'V_338',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1930,(0,0):C.GC_1828})

V_339 = Vertex(name = 'V_339',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1931})

V_340 = Vertex(name = 'V_340',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2488,(0,0):C.GC_2440})

V_341 = Vertex(name = 'V_341',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2489})

V_342 = Vertex(name = 'V_342',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3131,(0,0):C.GC_3054})

V_343 = Vertex(name = 'V_343',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_3132})

V_344 = Vertex(name = 'V_344',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_560,(0,3):C.GC_1208,(0,2):C.GC_1548,(0,0):C.GC_1422})

V_345 = Vertex(name = 'V_345',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_561,(0,2):C.GC_1211,(0,1):C.GC_1549})

V_346 = Vertex(name = 'V_346',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2106,(0,0):C.GC_2034})

V_347 = Vertex(name = 'V_347',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2107})

V_348 = Vertex(name = 'V_348',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2747,(0,0):C.GC_2647})

V_349 = Vertex(name = 'V_349',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2748})

V_350 = Vertex(name = 'V_350',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1788,(0,0):C.GC_1626})

V_351 = Vertex(name = 'V_351',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1789})

V_352 = Vertex(name = 'V_352',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_820,(0,3):C.GC_487,(0,2):C.GC_2346,(0,0):C.GC_2238})

V_353 = Vertex(name = 'V_353',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_821,(0,2):C.GC_490,(0,1):C.GC_2347})

V_354 = Vertex(name = 'V_354',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2988,(0,0):C.GC_2852})

V_355 = Vertex(name = 'V_355',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2989})

V_356 = Vertex(name = 'V_356',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1932,(0,0):C.GC_1830})

V_357 = Vertex(name = 'V_357',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1933})

V_358 = Vertex(name = 'V_358',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2490,(0,0):C.GC_2442})

V_359 = Vertex(name = 'V_359',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2491})

V_360 = Vertex(name = 'V_360',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_430,(0,3):C.GC_913,(0,2):C.GC_3133,(0,0):C.GC_3057})

V_361 = Vertex(name = 'V_361',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_431,(0,2):C.GC_916,(0,1):C.GC_3134})

V_362 = Vertex(name = 'V_362',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_654,(0,0):C.GC_133})

V_363 = Vertex(name = 'V_363',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_655,(0,0):C.GC_146})

V_364 = Vertex(name = 'V_364',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_365 = Vertex(name = 'V_365',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_747,(0,0):C.GC_133})

V_366 = Vertex(name = 'V_366',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_748,(0,0):C.GC_146})

V_367 = Vertex(name = 'V_367',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_368 = Vertex(name = 'V_368',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_1098,(0,0):C.GC_133})

V_369 = Vertex(name = 'V_369',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_1099,(0,0):C.GC_146})

V_370 = Vertex(name = 'V_370',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_371 = Vertex(name = 'V_371',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_372 = Vertex(name = 'V_372',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_373 = Vertex(name = 'V_373',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_159})

V_374 = Vertex(name = 'V_374',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_632,(0,0):C.GC_339})

V_375 = Vertex(name = 'V_375',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_633})

V_376 = Vertex(name = 'V_376',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_725,(0,0):C.GC_339})

V_377 = Vertex(name = 'V_377',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_726})

V_378 = Vertex(name = 'V_378',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_1076,(0,0):C.GC_339})

V_379 = Vertex(name = 'V_379',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_1077})

V_380 = Vertex(name = 'V_380',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_169})

V_381 = Vertex(name = 'V_381',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_176})

V_382 = Vertex(name = 'V_382',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_169})

V_383 = Vertex(name = 'V_383',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_176})

V_384 = Vertex(name = 'V_384',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_169})

V_385 = Vertex(name = 'V_385',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_176})

V_386 = Vertex(name = 'V_386',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_349,(0,3):C.GC_565,(0,0):C.GC_564})

V_387 = Vertex(name = 'V_387',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_356,(0,2):C.GC_578,(0,0):C.GC_577})

V_388 = Vertex(name = 'V_388',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_349,(0,3):C.GC_825,(0,0):C.GC_824})

V_389 = Vertex(name = 'V_389',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_356,(0,2):C.GC_838,(0,0):C.GC_837})

V_390 = Vertex(name = 'V_390',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_349,(0,3):C.GC_435,(0,0):C.GC_434})

V_391 = Vertex(name = 'V_391',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_356,(0,2):C.GC_448,(0,0):C.GC_447})

V_392 = Vertex(name = 'V_392',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_215,(0,4):C.GC_144,(0,1):C.GC_218,(0,6):C.GC_221,(0,5):C.GC_393,(0,2):C.GC_591,(0,3):C.GC_590})

V_393 = Vertex(name = 'V_393',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_257,(0,3):C.GC_157,(0,4):C.GC_376,(0,1):C.GC_603,(0,2):C.GC_602})

V_394 = Vertex(name = 'V_394',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_411,(0,1):C.GC_398})

V_395 = Vertex(name = 'V_395',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_396 = Vertex(name = 'V_396',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_215,(0,4):C.GC_144,(0,1):C.GC_218,(0,6):C.GC_221,(0,5):C.GC_393,(0,2):C.GC_851,(0,3):C.GC_850})

V_397 = Vertex(name = 'V_397',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_257,(0,3):C.GC_157,(0,4):C.GC_376,(0,1):C.GC_863,(0,2):C.GC_862})

V_398 = Vertex(name = 'V_398',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_411,(0,1):C.GC_398})

V_399 = Vertex(name = 'V_399',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_400 = Vertex(name = 'V_400',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV6 ],
               couplings = {(0,0):C.GC_215,(0,4):C.GC_144,(0,1):C.GC_218,(0,6):C.GC_221,(0,5):C.GC_393,(0,2):C.GC_461,(0,3):C.GC_460})

V_401 = Vertex(name = 'V_401',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV11, L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_257,(0,3):C.GC_157,(0,4):C.GC_376,(0,1):C.GC_473,(0,2):C.GC_472})

V_402 = Vertex(name = 'V_402',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_411,(0,1):C.GC_398})

V_403 = Vertex(name = 'V_403',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_404 = Vertex(name = 'V_404',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_170})

V_405 = Vertex(name = 'V_405',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_173})

V_406 = Vertex(name = 'V_406',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_170})

V_407 = Vertex(name = 'V_407',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_173})

V_408 = Vertex(name = 'V_408',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_170})

V_409 = Vertex(name = 'V_409',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_173})

V_410 = Vertex(name = 'V_410',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_351,(0,2):C.GC_350,(0,3):C.GC_637,(0,0):C.GC_636})

V_411 = Vertex(name = 'V_411',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_353,(0,2):C.GC_648,(0,0):C.GC_647})

V_412 = Vertex(name = 'V_412',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_351,(0,2):C.GC_350,(0,3):C.GC_730,(0,0):C.GC_729})

V_413 = Vertex(name = 'V_413',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_353,(0,2):C.GC_741,(0,0):C.GC_740})

V_414 = Vertex(name = 'V_414',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_351,(0,2):C.GC_350,(0,3):C.GC_1081,(0,0):C.GC_1080})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_353,(0,2):C.GC_1092,(0,0):C.GC_1091})

V_416 = Vertex(name = 'V_416',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_216,(0,4):C.GC_143,(0,6):C.GC_219,(0,1):C.GC_221,(0,5):C.GC_401,(0,2):C.GC_1238,(0,3):C.GC_1236})

V_417 = Vertex(name = 'V_417',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_258,(0,4):C.GC_156,(0,1):C.GC_376,(0,2):C.GC_1250,(0,3):C.GC_1249})

V_418 = Vertex(name = 'V_418',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_412,(0,1):C.GC_398})

V_419 = Vertex(name = 'V_419',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_399})

V_420 = Vertex(name = 'V_420',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_216,(0,4):C.GC_143,(0,6):C.GC_219,(0,1):C.GC_221,(0,5):C.GC_401,(0,2):C.GC_517,(0,3):C.GC_515})

V_421 = Vertex(name = 'V_421',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_258,(0,4):C.GC_156,(0,1):C.GC_376,(0,2):C.GC_529,(0,3):C.GC_528})

V_422 = Vertex(name = 'V_422',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_412,(0,1):C.GC_398})

V_423 = Vertex(name = 'V_423',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_399})

V_424 = Vertex(name = 'V_424',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_216,(0,4):C.GC_143,(0,6):C.GC_219,(0,1):C.GC_221,(0,5):C.GC_401,(0,2):C.GC_945,(0,3):C.GC_943})

V_425 = Vertex(name = 'V_425',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_258,(0,4):C.GC_156,(0,1):C.GC_376,(0,2):C.GC_957,(0,3):C.GC_956})

V_426 = Vertex(name = 'V_426',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_412,(0,1):C.GC_398})

V_427 = Vertex(name = 'V_427',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_399})

V_428 = Vertex(name = 'V_428',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_177})

V_429 = Vertex(name = 'V_429',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_175})

V_430 = Vertex(name = 'V_430',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_177})

V_431 = Vertex(name = 'V_431',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_175})

V_432 = Vertex(name = 'V_432',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_174,(0,1):C.GC_177})

V_433 = Vertex(name = 'V_433',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_175})

V_434 = Vertex(name = 'V_434',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_357,(0,3):C.GC_1212,(0,0):C.GC_1210})

V_435 = Vertex(name = 'V_435',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_355,(0,2):C.GC_1225,(0,0):C.GC_1224})

V_436 = Vertex(name = 'V_436',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_357,(0,3):C.GC_491,(0,0):C.GC_489})

V_437 = Vertex(name = 'V_437',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_355,(0,2):C.GC_504,(0,0):C.GC_503})

V_438 = Vertex(name = 'V_438',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_354,(0,2):C.GC_357,(0,3):C.GC_917,(0,0):C.GC_915})

V_439 = Vertex(name = 'V_439',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_355,(0,2):C.GC_932,(0,0):C.GC_931})

V_440 = Vertex(name = 'V_440',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_143})

V_441 = Vertex(name = 'V_441',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_246})

V_442 = Vertex(name = 'V_442',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_377})

V_443 = Vertex(name = 'V_443',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_395})

V_444 = Vertex(name = 'V_444',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_396})

V_445 = Vertex(name = 'V_445',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_143})

V_446 = Vertex(name = 'V_446',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_246})

V_447 = Vertex(name = 'V_447',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_377})

V_448 = Vertex(name = 'V_448',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_395})

V_449 = Vertex(name = 'V_449',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_396})

V_450 = Vertex(name = 'V_450',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_143})

V_451 = Vertex(name = 'V_451',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_246})

V_452 = Vertex(name = 'V_452',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_377})

V_453 = Vertex(name = 'V_453',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_395})

V_454 = Vertex(name = 'V_454',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_396})

V_455 = Vertex(name = 'V_455',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_171})

V_456 = Vertex(name = 'V_456',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_172})

V_457 = Vertex(name = 'V_457',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_171})

V_458 = Vertex(name = 'V_458',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_172})

V_459 = Vertex(name = 'V_459',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_171})

V_460 = Vertex(name = 'V_460',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_172})

V_461 = Vertex(name = 'V_461',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_351})

V_462 = Vertex(name = 'V_462',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_352})

V_463 = Vertex(name = 'V_463',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_351})

V_464 = Vertex(name = 'V_464',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_352})

V_465 = Vertex(name = 'V_465',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_351})

V_466 = Vertex(name = 'V_466',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_352})

V_467 = Vertex(name = 'V_467',
               particles = [ P.t__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_87})

V_468 = Vertex(name = 'V_468',
               particles = [ P.t1__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_92})

V_469 = Vertex(name = 'V_469',
               particles = [ P.t1__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_87})

V_470 = Vertex(name = 'V_470',
               particles = [ P.t__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_90})

V_471 = Vertex(name = 'V_471',
               particles = [ P.t1__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_95})

V_472 = Vertex(name = 'V_472',
               particles = [ P.t1__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_90})

V_473 = Vertex(name = 'V_473',
               particles = [ P.d__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_199})

V_474 = Vertex(name = 'V_474',
               particles = [ P.s__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_200})

V_475 = Vertex(name = 'V_475',
               particles = [ P.b__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_201})

V_476 = Vertex(name = 'V_476',
               particles = [ P.d__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_206})

V_477 = Vertex(name = 'V_477',
               particles = [ P.s__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_207})

V_478 = Vertex(name = 'V_478',
               particles = [ P.b__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_208})

V_479 = Vertex(name = 'V_479',
               particles = [ P.d__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_193})

V_480 = Vertex(name = 'V_480',
               particles = [ P.s__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_194})

V_481 = Vertex(name = 'V_481',
               particles = [ P.b__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_195})

V_482 = Vertex(name = 'V_482',
               particles = [ P.d__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_196})

V_483 = Vertex(name = 'V_483',
               particles = [ P.s__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_197})

V_484 = Vertex(name = 'V_484',
               particles = [ P.b__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_198})

V_485 = Vertex(name = 'V_485',
               particles = [ P.d__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_199})

V_486 = Vertex(name = 'V_486',
               particles = [ P.s__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_200})

V_487 = Vertex(name = 'V_487',
               particles = [ P.b__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_201})

V_488 = Vertex(name = 'V_488',
               particles = [ P.e__plus__, P.ve, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_489 = Vertex(name = 'V_489',
               particles = [ P.mu__plus__, P.vm, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_490 = Vertex(name = 'V_490',
               particles = [ P.ta__plus__, P.vt, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_491 = Vertex(name = 'V_491',
               particles = [ P.t1__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2646})

V_492 = Vertex(name = 'V_492',
               particles = [ P.t1__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2851})

V_493 = Vertex(name = 'V_493',
               particles = [ P.t1__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3056})

V_494 = Vertex(name = 'V_494',
               particles = [ P.u__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1421})

V_495 = Vertex(name = 'V_495',
               particles = [ P.c__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2033})

V_496 = Vertex(name = 'V_496',
               particles = [ P.t__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2645})

V_497 = Vertex(name = 'V_497',
               particles = [ P.u__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1625})

V_498 = Vertex(name = 'V_498',
               particles = [ P.c__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2237})

V_499 = Vertex(name = 'V_499',
               particles = [ P.t__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2850})

V_500 = Vertex(name = 'V_500',
               particles = [ P.u__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1829})

V_501 = Vertex(name = 'V_501',
               particles = [ P.c__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2441})

V_502 = Vertex(name = 'V_502',
               particles = [ P.t__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3055})

V_503 = Vertex(name = 'V_503',
               particles = [ P.ve__tilde__, P.e__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_504 = Vertex(name = 'V_504',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_505 = Vertex(name = 'V_505',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_192})

V_506 = Vertex(name = 'V_506',
               particles = [ P.t1__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2645})

V_507 = Vertex(name = 'V_507',
               particles = [ P.t1__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2850})

V_508 = Vertex(name = 'V_508',
               particles = [ P.t1__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3055})

V_509 = Vertex(name = 'V_509',
               particles = [ P.t__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_202})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t1__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_209})

V_511 = Vertex(name = 'V_511',
               particles = [ P.t1__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_202})

V_512 = Vertex(name = 'V_512',
               particles = [ P.d__tilde__, P.d, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_237,(0,1):C.GC_203})

V_513 = Vertex(name = 'V_513',
               particles = [ P.s__tilde__, P.s, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_237,(0,1):C.GC_203})

V_514 = Vertex(name = 'V_514',
               particles = [ P.b__tilde__, P.b, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_237,(0,1):C.GC_203})

V_515 = Vertex(name = 'V_515',
               particles = [ P.e__plus__, P.e__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_239,(0,1):C.GC_203})

V_516 = Vertex(name = 'V_516',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_239,(0,1):C.GC_203})

V_517 = Vertex(name = 'V_517',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_239,(0,1):C.GC_203})

V_518 = Vertex(name = 'V_518',
               particles = [ P.t__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_209})

V_519 = Vertex(name = 'V_519',
               particles = [ P.t1__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_241,(0,1):C.GC_212})

V_520 = Vertex(name = 'V_520',
               particles = [ P.t1__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_209})

V_521 = Vertex(name = 'V_521',
               particles = [ P.u__tilde__, P.u, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_202})

V_522 = Vertex(name = 'V_522',
               particles = [ P.c__tilde__, P.c, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_202})

V_523 = Vertex(name = 'V_523',
               particles = [ P.t__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_238,(0,1):C.GC_202})

V_524 = Vertex(name = 'V_524',
               particles = [ P.ve__tilde__, P.ve, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_202})

V_525 = Vertex(name = 'V_525',
               particles = [ P.vm__tilde__, P.vm, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_202})

V_526 = Vertex(name = 'V_526',
               particles = [ P.vt__tilde__, P.vt, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_202})

V_527 = Vertex(name = 'V_527',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_606,(0,1):C.GC_552})

V_528 = Vertex(name = 'V_528',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_553})

V_529 = Vertex(name = 'V_529',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_554})

V_530 = Vertex(name = 'V_530',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_607})

V_531 = Vertex(name = 'V_531',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_866,(0,1):C.GC_812})

V_532 = Vertex(name = 'V_532',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_813})

V_533 = Vertex(name = 'V_533',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_814})

V_534 = Vertex(name = 'V_534',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_867})

V_535 = Vertex(name = 'V_535',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_476,(0,1):C.GC_422})

V_536 = Vertex(name = 'V_536',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_423})

V_537 = Vertex(name = 'V_537',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_424})

V_538 = Vertex(name = 'V_538',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_477})

V_539 = Vertex(name = 'V_539',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_672,(0,1):C.GC_626})

V_540 = Vertex(name = 'V_540',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_627})

V_541 = Vertex(name = 'V_541',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_628})

V_542 = Vertex(name = 'V_542',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_673})

V_543 = Vertex(name = 'V_543',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_765,(0,1):C.GC_719})

V_544 = Vertex(name = 'V_544',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_720})

V_545 = Vertex(name = 'V_545',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_721})

V_546 = Vertex(name = 'V_546',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_766})

V_547 = Vertex(name = 'V_547',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1116,(0,1):C.GC_1070})

V_548 = Vertex(name = 'V_548',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1071})

V_549 = Vertex(name = 'V_549',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1072})

V_550 = Vertex(name = 'V_550',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1117})

V_551 = Vertex(name = 'V_551',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1253,(0,1):C.GC_1199})

V_552 = Vertex(name = 'V_552',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1200})

V_553 = Vertex(name = 'V_553',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1201})

V_554 = Vertex(name = 'V_554',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1254})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_532,(0,1):C.GC_478})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_479})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_480})

V_558 = Vertex(name = 'V_558',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_533})

V_559 = Vertex(name = 'V_559',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_960,(0,1):C.GC_904})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_905})

V_561 = Vertex(name = 'V_561',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_906})

V_562 = Vertex(name = 'V_562',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_961})

V_563 = Vertex(name = 'V_563',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_557,(0,1):C.GC_558})

V_564 = Vertex(name = 'V_564',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_817,(0,1):C.GC_818})

V_565 = Vertex(name = 'V_565',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_427,(0,1):C.GC_428})

V_566 = Vertex(name = 'V_566',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_583,(0,1):C.GC_584})

V_567 = Vertex(name = 'V_567',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_843,(0,1):C.GC_844})

V_568 = Vertex(name = 'V_568',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_453,(0,1):C.GC_454})

V_569 = Vertex(name = 'V_569',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_629,(0,1):C.GC_630})

V_570 = Vertex(name = 'V_570',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_722,(0,1):C.GC_723})

V_571 = Vertex(name = 'V_571',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1073,(0,1):C.GC_1074})

V_572 = Vertex(name = 'V_572',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_651,(0,1):C.GC_652})

V_573 = Vertex(name = 'V_573',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_744,(0,1):C.GC_745})

V_574 = Vertex(name = 'V_574',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1095,(0,1):C.GC_1096})

V_575 = Vertex(name = 'V_575',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1206,(0,1):C.GC_1207})

V_576 = Vertex(name = 'V_576',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_485,(0,1):C.GC_486})

V_577 = Vertex(name = 'V_577',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_911,(0,1):C.GC_912})

V_578 = Vertex(name = 'V_578',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1232,(0,1):C.GC_1233})

V_579 = Vertex(name = 'V_579',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_511,(0,1):C.GC_512})

V_580 = Vertex(name = 'V_580',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_939,(0,1):C.GC_940})

V_581 = Vertex(name = 'V_581',
               particles = [ P.d__tilde__, P.d, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_571})

V_582 = Vertex(name = 'V_582',
               particles = [ P.s__tilde__, P.s, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_831})

V_583 = Vertex(name = 'V_583',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_441})

V_584 = Vertex(name = 'V_584',
               particles = [ P.e__plus__, P.e__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_641})

V_585 = Vertex(name = 'V_585',
               particles = [ P.mu__plus__, P.mu__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_734})

V_586 = Vertex(name = 'V_586',
               particles = [ P.ta__plus__, P.ta__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1085})

V_587 = Vertex(name = 'V_587',
               particles = [ P.t__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_923})

V_588 = Vertex(name = 'V_588',
               particles = [ P.t__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_924})

V_589 = Vertex(name = 'V_589',
               particles = [ P.t1__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_924})

V_590 = Vertex(name = 'V_590',
               particles = [ P.t1__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_925})

V_591 = Vertex(name = 'V_591',
               particles = [ P.t1__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_923})

V_592 = Vertex(name = 'V_592',
               particles = [ P.t1__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_924})

V_593 = Vertex(name = 'V_593',
               particles = [ P.u__tilde__, P.u, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1218})

V_594 = Vertex(name = 'V_594',
               particles = [ P.c__tilde__, P.c, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_497})

V_595 = Vertex(name = 'V_595',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_923})

V_596 = Vertex(name = 'V_596',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_563,(0,0):C.GC_562})

V_597 = Vertex(name = 'V_597',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_580,(0,0):C.GC_579})

V_598 = Vertex(name = 'V_598',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_823,(0,0):C.GC_822})

V_599 = Vertex(name = 'V_599',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_840,(0,0):C.GC_839})

V_600 = Vertex(name = 'V_600',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_433,(0,0):C.GC_432})

V_601 = Vertex(name = 'V_601',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_450,(0,0):C.GC_449})

V_602 = Vertex(name = 'V_602',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_556,(0,0):C.GC_555})

V_603 = Vertex(name = 'V_603',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_816,(0,0):C.GC_815})

V_604 = Vertex(name = 'V_604',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_426,(0,0):C.GC_425})

V_605 = Vertex(name = 'V_605',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_570,(0,0):C.GC_569})

V_606 = Vertex(name = 'V_606',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_830,(0,0):C.GC_829})

V_607 = Vertex(name = 'V_607',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_440,(0,0):C.GC_439})

V_608 = Vertex(name = 'V_608',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_596,(0,0):C.GC_595})

V_609 = Vertex(name = 'V_609',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_856,(0,0):C.GC_855})

V_610 = Vertex(name = 'V_610',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_466,(0,0):C.GC_465})

V_611 = Vertex(name = 'V_611',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_566,(0,1):C.GC_1213})

V_612 = Vertex(name = 'V_612',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_568,(0,1):C.GC_1215})

V_613 = Vertex(name = 'V_613',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_826,(0,1):C.GC_492})

V_614 = Vertex(name = 'V_614',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_828,(0,1):C.GC_494})

V_615 = Vertex(name = 'V_615',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_436,(0,1):C.GC_918})

V_616 = Vertex(name = 'V_616',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_438,(0,1):C.GC_920})

V_617 = Vertex(name = 'V_617',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_592,(0,1):C.GC_1239})

V_618 = Vertex(name = 'V_618',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_594,(0,1):C.GC_1241})

V_619 = Vertex(name = 'V_619',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_852,(0,1):C.GC_518})

V_620 = Vertex(name = 'V_620',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_854,(0,1):C.GC_520})

V_621 = Vertex(name = 'V_621',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_462,(0,1):C.GC_946})

V_622 = Vertex(name = 'V_622',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_464,(0,1):C.GC_948})

V_623 = Vertex(name = 'V_623',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_573,(0,0):C.GC_572})

V_624 = Vertex(name = 'V_624',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_833,(0,0):C.GC_832})

V_625 = Vertex(name = 'V_625',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_443,(0,0):C.GC_442})

V_626 = Vertex(name = 'V_626',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_598,(0,0):C.GC_597})

V_627 = Vertex(name = 'V_627',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_858,(0,0):C.GC_857})

V_628 = Vertex(name = 'V_628',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_468,(0,0):C.GC_467})

V_629 = Vertex(name = 'V_629',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_635,(0,0):C.GC_634})

V_630 = Vertex(name = 'V_630',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_650,(0,0):C.GC_649})

V_631 = Vertex(name = 'V_631',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_728,(0,0):C.GC_727})

V_632 = Vertex(name = 'V_632',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_743,(0,0):C.GC_742})

V_633 = Vertex(name = 'V_633',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1079,(0,0):C.GC_1078})

V_634 = Vertex(name = 'V_634',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1094,(0,0):C.GC_1093})

V_635 = Vertex(name = 'V_635',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_638})

V_636 = Vertex(name = 'V_636',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_640})

V_637 = Vertex(name = 'V_637',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_731})

V_638 = Vertex(name = 'V_638',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_733})

V_639 = Vertex(name = 'V_639',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1082})

V_640 = Vertex(name = 'V_640',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1084})

V_641 = Vertex(name = 'V_641',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_660})

V_642 = Vertex(name = 'V_642',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_662})

V_643 = Vertex(name = 'V_643',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_753})

V_644 = Vertex(name = 'V_644',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_755})

V_645 = Vertex(name = 'V_645',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1104})

V_646 = Vertex(name = 'V_646',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1106})

V_647 = Vertex(name = 'V_647',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_643,(0,0):C.GC_642})

V_648 = Vertex(name = 'V_648',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_736,(0,0):C.GC_735})

V_649 = Vertex(name = 'V_649',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1087,(0,0):C.GC_1086})

V_650 = Vertex(name = 'V_650',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_664,(0,0):C.GC_663})

V_651 = Vertex(name = 'V_651',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_757,(0,0):C.GC_756})

V_652 = Vertex(name = 'V_652',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1108,(0,0):C.GC_1107})

V_653 = Vertex(name = 'V_653',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1203,(0,0):C.GC_1202})

V_654 = Vertex(name = 'V_654',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1227,(0,0):C.GC_1226})

V_655 = Vertex(name = 'V_655',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_482,(0,0):C.GC_481})

V_656 = Vertex(name = 'V_656',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_506,(0,0):C.GC_505})

V_657 = Vertex(name = 'V_657',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_908,(0,0):C.GC_907})

V_658 = Vertex(name = 'V_658',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_934,(0,0):C.GC_933})

V_659 = Vertex(name = 'V_659',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1205,(0,0):C.GC_1204})

V_660 = Vertex(name = 'V_660',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_484,(0,0):C.GC_483})

V_661 = Vertex(name = 'V_661',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_910,(0,0):C.GC_909})

V_662 = Vertex(name = 'V_662',
               particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1217,(0,0):C.GC_1216})

V_663 = Vertex(name = 'V_663',
               particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_496,(0,0):C.GC_495})

V_664 = Vertex(name = 'V_664',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_922,(0,0):C.GC_921})

V_665 = Vertex(name = 'V_665',
               particles = [ P.u__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1243,(0,0):C.GC_1242})

V_666 = Vertex(name = 'V_666',
               particles = [ P.c__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_522,(0,0):C.GC_521})

V_667 = Vertex(name = 'V_667',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_950,(0,0):C.GC_949})

V_668 = Vertex(name = 'V_668',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1213,(0,1):C.GC_566})

V_669 = Vertex(name = 'V_669',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1214,(0,1):C.GC_567})

V_670 = Vertex(name = 'V_670',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_492,(0,1):C.GC_826})

V_671 = Vertex(name = 'V_671',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_493,(0,1):C.GC_827})

V_672 = Vertex(name = 'V_672',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_918,(0,1):C.GC_436})

V_673 = Vertex(name = 'V_673',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_919,(0,1):C.GC_437})

V_674 = Vertex(name = 'V_674',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1239,(0,1):C.GC_592})

V_675 = Vertex(name = 'V_675',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1240,(0,1):C.GC_593})

V_676 = Vertex(name = 'V_676',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_518,(0,1):C.GC_852})

V_677 = Vertex(name = 'V_677',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_853})

V_678 = Vertex(name = 'V_678',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_946,(0,1):C.GC_462})

V_679 = Vertex(name = 'V_679',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_947,(0,1):C.GC_463})

V_680 = Vertex(name = 'V_680',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1221,(0,0):C.GC_1219})

V_681 = Vertex(name = 'V_681',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_500,(0,0):C.GC_498})

V_682 = Vertex(name = 'V_682',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_928,(0,0):C.GC_926})

V_683 = Vertex(name = 'V_683',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1246,(0,0):C.GC_1244})

V_684 = Vertex(name = 'V_684',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_525,(0,0):C.GC_523})

V_685 = Vertex(name = 'V_685',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_953,(0,0):C.GC_951})

V_686 = Vertex(name = 'V_686',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_574,(0,1):C.GC_1220})

V_687 = Vertex(name = 'V_687',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_575,(0,1):C.GC_1222})

V_688 = Vertex(name = 'V_688',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_834,(0,1):C.GC_499})

V_689 = Vertex(name = 'V_689',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_835,(0,1):C.GC_501})

V_690 = Vertex(name = 'V_690',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_444,(0,1):C.GC_927})

V_691 = Vertex(name = 'V_691',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_445,(0,1):C.GC_929})

V_692 = Vertex(name = 'V_692',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_599,(0,1):C.GC_1245})

V_693 = Vertex(name = 'V_693',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_600,(0,1):C.GC_1247})

V_694 = Vertex(name = 'V_694',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_859,(0,1):C.GC_524})

V_695 = Vertex(name = 'V_695',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_860,(0,1):C.GC_526})

V_696 = Vertex(name = 'V_696',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_469,(0,1):C.GC_952})

V_697 = Vertex(name = 'V_697',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_470,(0,1):C.GC_954})

V_698 = Vertex(name = 'V_698',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_644})

V_699 = Vertex(name = 'V_699',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_645})

V_700 = Vertex(name = 'V_700',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_737})

V_701 = Vertex(name = 'V_701',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_738})

V_702 = Vertex(name = 'V_702',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1088})

V_703 = Vertex(name = 'V_703',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1089})

V_704 = Vertex(name = 'V_704',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_665})

V_705 = Vertex(name = 'V_705',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_666})

V_706 = Vertex(name = 'V_706',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_758})

V_707 = Vertex(name = 'V_707',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_759})

V_708 = Vertex(name = 'V_708',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1109})

V_709 = Vertex(name = 'V_709',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1110})

V_710 = Vertex(name = 'V_710',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1220,(0,1):C.GC_574})

V_711 = Vertex(name = 'V_711',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1223,(0,1):C.GC_576})

V_712 = Vertex(name = 'V_712',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_499,(0,1):C.GC_834})

V_713 = Vertex(name = 'V_713',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_502,(0,1):C.GC_836})

V_714 = Vertex(name = 'V_714',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_927,(0,1):C.GC_444})

V_715 = Vertex(name = 'V_715',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_930,(0,1):C.GC_446})

V_716 = Vertex(name = 'V_716',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1245,(0,1):C.GC_599})

V_717 = Vertex(name = 'V_717',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1248,(0,1):C.GC_601})

V_718 = Vertex(name = 'V_718',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_524,(0,1):C.GC_859})

V_719 = Vertex(name = 'V_719',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_527,(0,1):C.GC_861})

V_720 = Vertex(name = 'V_720',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_952,(0,1):C.GC_469})

V_721 = Vertex(name = 'V_721',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_955,(0,1):C.GC_471})

V_722 = Vertex(name = 'V_722',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_638})

V_723 = Vertex(name = 'V_723',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_639})

V_724 = Vertex(name = 'V_724',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_731})

V_725 = Vertex(name = 'V_725',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_732})

V_726 = Vertex(name = 'V_726',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1082})

V_727 = Vertex(name = 'V_727',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1083})

V_728 = Vertex(name = 'V_728',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_660})

V_729 = Vertex(name = 'V_729',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_661})

V_730 = Vertex(name = 'V_730',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_753})

V_731 = Vertex(name = 'V_731',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_754})

V_732 = Vertex(name = 'V_732',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1104})

V_733 = Vertex(name = 'V_733',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1105})

V_734 = Vertex(name = 'V_734',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_644})

V_735 = Vertex(name = 'V_735',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_646})

V_736 = Vertex(name = 'V_736',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_737})

V_737 = Vertex(name = 'V_737',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_739})

V_738 = Vertex(name = 'V_738',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1088})

V_739 = Vertex(name = 'V_739',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1090})

V_740 = Vertex(name = 'V_740',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_665})

V_741 = Vertex(name = 'V_741',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_667})

V_742 = Vertex(name = 'V_742',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_758})

V_743 = Vertex(name = 'V_743',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_760})

V_744 = Vertex(name = 'V_744',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1109})

V_745 = Vertex(name = 'V_745',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1111})

V_746 = Vertex(name = 'V_746',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_44,(2,0):C.GC_45,(1,3):C.GC_44,(3,3):C.GC_45,(1,1):C.GC_44,(3,1):C.GC_45,(1,2):C.GC_13,(0,4):C.GC_44,(2,4):C.GC_45,(0,5):C.GC_13})

V_747 = Vertex(name = 'V_747',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_14,(0,1):C.GC_14})

V_748 = Vertex(name = 'V_748',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_749 = Vertex(name = 'V_749',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_750 = Vertex(name = 'V_750',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_44,(2,2):C.GC_45,(1,0):C.GC_44,(2,0):C.GC_45,(1,1):C.GC_13,(0,3):C.GC_14})

V_751 = Vertex(name = 'V_751',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_752 = Vertex(name = 'V_752',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_44,(2,2):C.GC_45,(1,0):C.GC_44,(2,0):C.GC_45,(1,1):C.GC_13,(0,3):C.GC_14})

V_753 = Vertex(name = 'V_753',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_754 = Vertex(name = 'V_754',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_44,(2,0):C.GC_45,(1,3):C.GC_44,(3,3):C.GC_45,(1,1):C.GC_44,(3,1):C.GC_45,(1,2):C.GC_13,(0,4):C.GC_44,(2,4):C.GC_45,(0,5):C.GC_13})

V_755 = Vertex(name = 'V_755',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_14,(0,1):C.GC_14})

V_756 = Vertex(name = 'V_756',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_757 = Vertex(name = 'V_757',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_758 = Vertex(name = 'V_758',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_44,(2,2):C.GC_45,(1,0):C.GC_44,(2,0):C.GC_45,(1,1):C.GC_13,(0,3):C.GC_14})

V_759 = Vertex(name = 'V_759',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_760 = Vertex(name = 'V_760',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_44,(2,0):C.GC_45,(1,3):C.GC_44,(3,3):C.GC_45,(1,1):C.GC_44,(3,1):C.GC_45,(1,2):C.GC_13,(0,4):C.GC_44,(2,4):C.GC_45,(0,5):C.GC_13})

V_761 = Vertex(name = 'V_761',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_14,(0,1):C.GC_14})

V_762 = Vertex(name = 'V_762',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_763 = Vertex(name = 'V_763',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_764 = Vertex(name = 'V_764',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_29,(0,7):C.GC_29,(0,0):C.GC_28,(0,3):C.GC_28,(0,1):C.GC_28,(0,2):C.GC_16,(0,4):C.GC_28,(0,5):C.GC_16})

V_765 = Vertex(name = 'V_765',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_766 = Vertex(name = 'V_766',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_29,(0,4):C.GC_30,(0,2):C.GC_28,(0,0):C.GC_28,(0,1):C.GC_16})

V_767 = Vertex(name = 'V_767',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_29,(0,4):C.GC_30,(0,2):C.GC_28,(0,0):C.GC_28,(0,1):C.GC_16})

V_768 = Vertex(name = 'V_768',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_29,(0,7):C.GC_29,(0,0):C.GC_28,(0,3):C.GC_28,(0,1):C.GC_28,(0,2):C.GC_16,(0,4):C.GC_28,(0,5):C.GC_16})

V_769 = Vertex(name = 'V_769',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_770 = Vertex(name = 'V_770',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_29,(0,4):C.GC_30,(0,2):C.GC_28,(0,0):C.GC_28,(0,1):C.GC_16})

V_771 = Vertex(name = 'V_771',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_29,(0,7):C.GC_29,(0,0):C.GC_28,(0,3):C.GC_28,(0,1):C.GC_28,(0,2):C.GC_16,(0,4):C.GC_28,(0,5):C.GC_16})

V_772 = Vertex(name = 'V_772',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_773 = Vertex(name = 'V_773',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_710,(0,0):C.GC_711})

V_774 = Vertex(name = 'V_774',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_715,(0,0):C.GC_715})

V_775 = Vertex(name = 'V_775',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_803,(0,0):C.GC_804})

V_776 = Vertex(name = 'V_776',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_808,(0,0):C.GC_808})

V_777 = Vertex(name = 'V_777',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_1154,(0,0):C.GC_1155})

V_778 = Vertex(name = 'V_778',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_1159,(0,0):C.GC_1159})

V_779 = Vertex(name = 'V_779',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_886,(0,0):C.GC_887})

V_780 = Vertex(name = 'V_780',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_891,(0,0):C.GC_891})

V_781 = Vertex(name = 'V_781',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_895,(0,0):C.GC_896})

V_782 = Vertex(name = 'V_782',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_900,(0,0):C.GC_900})

V_783 = Vertex(name = 'V_783',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_1163,(0,0):C.GC_1164})

V_784 = Vertex(name = 'V_784',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_1168,(0,0):C.GC_1168})

V_785 = Vertex(name = 'V_785',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_674,(0,0):C.GC_675})

V_786 = Vertex(name = 'V_786',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_679,(0,0):C.GC_679})

V_787 = Vertex(name = 'V_787',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_767,(0,0):C.GC_768})

V_788 = Vertex(name = 'V_788',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_772,(0,0):C.GC_772})

V_789 = Vertex(name = 'V_789',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_31,(0,1):C.GC_46,(0,2):C.GC_27,(0,3):C.GC_15,(0,5):C.GC_1118,(0,0):C.GC_1119})

V_790 = Vertex(name = 'V_790',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_33,(0,2):C.GC_1123,(0,0):C.GC_1123})

V_791 = Vertex(name = 'V_791',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_1304,(0,3):C.GC_1305,(0,4):C.GC_1305,(0,1):C.GC_1293,(0,0):C.GC_712})

V_792 = Vertex(name = 'V_792',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1313,(0,2):C.GC_1312,(0,3):C.GC_1312,(0,1):C.GC_1297,(0,0):C.GC_716})

V_793 = Vertex(name = 'V_793',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_696,(0,3):C.GC_697,(0,4):C.GC_697,(0,1):C.GC_685,(0,0):C.GC_713})

V_794 = Vertex(name = 'V_794',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_705,(0,2):C.GC_704,(0,3):C.GC_704,(0,1):C.GC_689,(0,0):C.GC_717})

V_795 = Vertex(name = 'V_795',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_40,(0,5):C.GC_1011,(0,3):C.GC_1012,(0,4):C.GC_1012,(0,1):C.GC_1000,(0,0):C.GC_714})

V_796 = Vertex(name = 'V_796',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1020,(0,2):C.GC_1019,(0,3):C.GC_1019,(0,1):C.GC_1004,(0,0):C.GC_718})

V_797 = Vertex(name = 'V_797',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_1306,(0,3):C.GC_1307,(0,4):C.GC_1307,(0,1):C.GC_1294,(0,0):C.GC_888})

V_798 = Vertex(name = 'V_798',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1315,(0,2):C.GC_1314,(0,3):C.GC_1314,(0,1):C.GC_1298,(0,0):C.GC_892})

V_799 = Vertex(name = 'V_799',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_698,(0,3):C.GC_699,(0,4):C.GC_699,(0,1):C.GC_686,(0,0):C.GC_889})

V_800 = Vertex(name = 'V_800',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_707,(0,2):C.GC_706,(0,3):C.GC_706,(0,1):C.GC_690,(0,0):C.GC_893})

V_801 = Vertex(name = 'V_801',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_41,(0,5):C.GC_1013,(0,3):C.GC_1014,(0,4):C.GC_1014,(0,1):C.GC_1001,(0,0):C.GC_890})

V_802 = Vertex(name = 'V_802',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1022,(0,2):C.GC_1021,(0,3):C.GC_1021,(0,1):C.GC_1005,(0,0):C.GC_894})

V_803 = Vertex(name = 'V_803',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_1308,(0,3):C.GC_1309,(0,4):C.GC_1309,(0,1):C.GC_1295,(0,0):C.GC_676})

V_804 = Vertex(name = 'V_804',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1317,(0,2):C.GC_1316,(0,3):C.GC_1316,(0,1):C.GC_1299,(0,0):C.GC_680})

V_805 = Vertex(name = 'V_805',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_700,(0,3):C.GC_701,(0,4):C.GC_701,(0,1):C.GC_687,(0,0):C.GC_677})

V_806 = Vertex(name = 'V_806',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_709,(0,2):C.GC_708,(0,3):C.GC_708,(0,1):C.GC_691,(0,0):C.GC_681})

V_807 = Vertex(name = 'V_807',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_42,(0,5):C.GC_1015,(0,3):C.GC_1016,(0,4):C.GC_1016,(0,1):C.GC_1002,(0,0):C.GC_678})

V_808 = Vertex(name = 'V_808',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1024,(0,2):C.GC_1023,(0,3):C.GC_1023,(0,1):C.GC_1006,(0,0):C.GC_682})

V_809 = Vertex(name = 'V_809',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_1331,(0,3):C.GC_1332,(0,4):C.GC_1332,(0,1):C.GC_1320,(0,0):C.GC_805})

V_810 = Vertex(name = 'V_810',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1340,(0,2):C.GC_1339,(0,3):C.GC_1339,(0,1):C.GC_1324,(0,0):C.GC_809})

V_811 = Vertex(name = 'V_811',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_789,(0,3):C.GC_790,(0,4):C.GC_790,(0,1):C.GC_778,(0,0):C.GC_806})

V_812 = Vertex(name = 'V_812',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_798,(0,2):C.GC_797,(0,3):C.GC_797,(0,1):C.GC_782,(0,0):C.GC_810})

V_813 = Vertex(name = 'V_813',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_40,(0,5):C.GC_1038,(0,3):C.GC_1039,(0,4):C.GC_1039,(0,1):C.GC_1027,(0,0):C.GC_807})

V_814 = Vertex(name = 'V_814',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1047,(0,2):C.GC_1046,(0,3):C.GC_1046,(0,1):C.GC_1031,(0,0):C.GC_811})

V_815 = Vertex(name = 'V_815',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_1333,(0,3):C.GC_1334,(0,4):C.GC_1334,(0,1):C.GC_1321,(0,0):C.GC_897})

V_816 = Vertex(name = 'V_816',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1342,(0,2):C.GC_1341,(0,3):C.GC_1341,(0,1):C.GC_1325,(0,0):C.GC_901})

V_817 = Vertex(name = 'V_817',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_791,(0,3):C.GC_792,(0,4):C.GC_792,(0,1):C.GC_779,(0,0):C.GC_898})

V_818 = Vertex(name = 'V_818',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_800,(0,2):C.GC_799,(0,3):C.GC_799,(0,1):C.GC_783,(0,0):C.GC_902})

V_819 = Vertex(name = 'V_819',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_41,(0,5):C.GC_1040,(0,3):C.GC_1041,(0,4):C.GC_1041,(0,1):C.GC_1028,(0,0):C.GC_899})

V_820 = Vertex(name = 'V_820',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1049,(0,2):C.GC_1048,(0,3):C.GC_1048,(0,1):C.GC_1032,(0,0):C.GC_903})

V_821 = Vertex(name = 'V_821',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_1335,(0,3):C.GC_1336,(0,4):C.GC_1336,(0,1):C.GC_1322,(0,0):C.GC_769})

V_822 = Vertex(name = 'V_822',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1344,(0,2):C.GC_1343,(0,3):C.GC_1343,(0,1):C.GC_1326,(0,0):C.GC_773})

V_823 = Vertex(name = 'V_823',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_793,(0,3):C.GC_794,(0,4):C.GC_794,(0,1):C.GC_780,(0,0):C.GC_770})

V_824 = Vertex(name = 'V_824',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_802,(0,2):C.GC_801,(0,3):C.GC_801,(0,1):C.GC_784,(0,0):C.GC_774})

V_825 = Vertex(name = 'V_825',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_42,(0,5):C.GC_1042,(0,3):C.GC_1043,(0,4):C.GC_1043,(0,1):C.GC_1029,(0,0):C.GC_771})

V_826 = Vertex(name = 'V_826',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1051,(0,2):C.GC_1050,(0,3):C.GC_1050,(0,1):C.GC_1033,(0,0):C.GC_775})

V_827 = Vertex(name = 'V_827',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_1376,(0,3):C.GC_1377,(0,4):C.GC_1377,(0,1):C.GC_1365,(0,0):C.GC_1156})

V_828 = Vertex(name = 'V_828',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1385,(0,2):C.GC_1384,(0,3):C.GC_1384,(0,1):C.GC_1369,(0,0):C.GC_1160})

V_829 = Vertex(name = 'V_829',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_1140,(0,3):C.GC_1141,(0,4):C.GC_1141,(0,1):C.GC_1129,(0,0):C.GC_1157})

V_830 = Vertex(name = 'V_830',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1149,(0,2):C.GC_1148,(0,3):C.GC_1148,(0,1):C.GC_1133,(0,0):C.GC_1161})

V_831 = Vertex(name = 'V_831',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_40,(0,5):C.GC_1185,(0,3):C.GC_1186,(0,4):C.GC_1186,(0,1):C.GC_1174,(0,0):C.GC_1158})

V_832 = Vertex(name = 'V_832',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1194,(0,2):C.GC_1193,(0,3):C.GC_1193,(0,1):C.GC_1178,(0,0):C.GC_1162})

V_833 = Vertex(name = 'V_833',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_1378,(0,3):C.GC_1379,(0,4):C.GC_1379,(0,1):C.GC_1366,(0,0):C.GC_1165})

V_834 = Vertex(name = 'V_834',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1387,(0,2):C.GC_1386,(0,3):C.GC_1386,(0,1):C.GC_1370,(0,0):C.GC_1169})

V_835 = Vertex(name = 'V_835',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_1142,(0,3):C.GC_1143,(0,4):C.GC_1143,(0,1):C.GC_1130,(0,0):C.GC_1166})

V_836 = Vertex(name = 'V_836',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1151,(0,2):C.GC_1150,(0,3):C.GC_1150,(0,1):C.GC_1134,(0,0):C.GC_1170})

V_837 = Vertex(name = 'V_837',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_41,(0,5):C.GC_1187,(0,3):C.GC_1188,(0,4):C.GC_1188,(0,1):C.GC_1175,(0,0):C.GC_1167})

V_838 = Vertex(name = 'V_838',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1196,(0,2):C.GC_1195,(0,3):C.GC_1195,(0,1):C.GC_1179,(0,0):C.GC_1171})

V_839 = Vertex(name = 'V_839',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_1380,(0,3):C.GC_1381,(0,4):C.GC_1381,(0,1):C.GC_1367,(0,0):C.GC_1120})

V_840 = Vertex(name = 'V_840',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1389,(0,2):C.GC_1388,(0,3):C.GC_1388,(0,1):C.GC_1371,(0,0):C.GC_1124})

V_841 = Vertex(name = 'V_841',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_1144,(0,3):C.GC_1145,(0,4):C.GC_1145,(0,1):C.GC_1131,(0,0):C.GC_1121})

V_842 = Vertex(name = 'V_842',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1153,(0,2):C.GC_1152,(0,3):C.GC_1152,(0,1):C.GC_1135,(0,0):C.GC_1125})

V_843 = Vertex(name = 'V_843',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_42,(0,5):C.GC_1189,(0,3):C.GC_1190,(0,4):C.GC_1190,(0,1):C.GC_1176,(0,0):C.GC_1122})

V_844 = Vertex(name = 'V_844',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1198,(0,2):C.GC_1197,(0,3):C.GC_1197,(0,1):C.GC_1180,(0,0):C.GC_1126})

V_845 = Vertex(name = 'V_845',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_1277,(3,0):C.GC_1283,(0,6):C.GC_1273,(2,6):C.GC_1279,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_1276,(3,1):C.GC_1282,(0,2):C.GC_1274,(2,2):C.GC_1280})

V_846 = Vertex(name = 'V_846',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_1400,(1,0):C.GC_1278,(3,0):C.GC_1284,(0,3):C.GC_1275,(2,3):C.GC_1281,(1,1):C.GC_1278,(3,1):C.GC_1284,(0,2):C.GC_1275,(2,2):C.GC_1281})

V_847 = Vertex(name = 'V_847',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1391,(1,0):C.GC_1503,(3,0):C.GC_1525,(0,3):C.GC_1513,(2,3):C.GC_1535,(1,1):C.GC_1502,(3,1):C.GC_1524,(0,2):C.GC_1514,(2,2):C.GC_1536})

V_848 = Vertex(name = 'V_848',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1409,(1,0):C.GC_1508,(3,0):C.GC_1530,(0,3):C.GC_1519,(2,3):C.GC_1541,(1,1):C.GC_1508,(3,1):C.GC_1530,(0,2):C.GC_1519,(2,2):C.GC_1541})

V_849 = Vertex(name = 'V_849',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2003,(0,5):C.GC_2012,(1,0):C.GC_2182,(3,0):C.GC_2194,(0,3):C.GC_2188,(2,3):C.GC_2200,(1,1):C.GC_2060,(3,1):C.GC_2082,(0,2):C.GC_2071,(2,2):C.GC_2093})

V_850 = Vertex(name = 'V_850',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2021,(1,0):C.GC_2185,(3,0):C.GC_2197,(0,3):C.GC_2191,(2,3):C.GC_2203,(1,1):C.GC_2066,(3,1):C.GC_2088,(0,2):C.GC_2077,(2,2):C.GC_2099})

V_851 = Vertex(name = 'V_851',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2615,(0,5):C.GC_2624,(1,0):C.GC_2795,(3,0):C.GC_2807,(0,3):C.GC_2801,(2,3):C.GC_2813,(1,1):C.GC_2701,(3,1):C.GC_2723,(0,2):C.GC_2712,(2,2):C.GC_2734})

V_852 = Vertex(name = 'V_852',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2633,(1,0):C.GC_2798,(3,0):C.GC_2810,(0,3):C.GC_2804,(2,3):C.GC_2816,(1,1):C.GC_2707,(3,1):C.GC_2729,(0,2):C.GC_2718,(2,2):C.GC_2740})

V_853 = Vertex(name = 'V_853',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1394,(0,5):C.GC_1403,(1,0):C.GC_1424,(3,0):C.GC_1436,(0,3):C.GC_1430,(2,3):C.GC_1442,(1,1):C.GC_1506,(3,1):C.GC_1528,(0,2):C.GC_1517,(2,2):C.GC_1539})

V_854 = Vertex(name = 'V_854',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1412,(1,0):C.GC_1427,(3,0):C.GC_1439,(0,3):C.GC_1433,(2,3):C.GC_1445,(1,1):C.GC_1511,(3,1):C.GC_1533,(0,2):C.GC_1522,(2,2):C.GC_1544})

V_855 = Vertex(name = 'V_855',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_612,(3,0):C.GC_618,(0,6):C.GC_608,(2,6):C.GC_614,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_611,(3,1):C.GC_617,(0,2):C.GC_609,(2,2):C.GC_615})

V_856 = Vertex(name = 'V_856',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_2015,(1,0):C.GC_613,(3,0):C.GC_619,(0,3):C.GC_610,(2,3):C.GC_616,(1,1):C.GC_613,(3,1):C.GC_619,(0,2):C.GC_610,(2,2):C.GC_616})

V_857 = Vertex(name = 'V_857',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2006,(1,0):C.GC_2062,(3,0):C.GC_2084,(0,3):C.GC_2072,(2,3):C.GC_2094,(1,1):C.GC_2061,(3,1):C.GC_2083,(0,2):C.GC_2073,(2,2):C.GC_2095})

V_858 = Vertex(name = 'V_858',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2024,(1,0):C.GC_2067,(3,0):C.GC_2089,(0,3):C.GC_2078,(2,3):C.GC_2100,(1,1):C.GC_2067,(3,1):C.GC_2089,(0,2):C.GC_2078,(2,2):C.GC_2100})

V_859 = Vertex(name = 'V_859',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2618,(0,5):C.GC_2627,(1,0):C.GC_2649,(3,0):C.GC_2661,(0,3):C.GC_2655,(2,3):C.GC_2667,(1,1):C.GC_2702,(3,1):C.GC_2724,(0,2):C.GC_2713,(2,2):C.GC_2735})

V_860 = Vertex(name = 'V_860',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2636,(1,0):C.GC_2652,(3,0):C.GC_2664,(0,3):C.GC_2658,(2,3):C.GC_2670,(1,1):C.GC_2708,(3,1):C.GC_2730,(0,2):C.GC_2719,(2,2):C.GC_2741})

V_861 = Vertex(name = 'V_861',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1397,(0,5):C.GC_1406,(1,0):C.GC_1452,(3,0):C.GC_1464,(0,3):C.GC_1458,(2,3):C.GC_1470,(1,1):C.GC_1507,(3,1):C.GC_1529,(0,2):C.GC_1518,(2,2):C.GC_1540})

V_862 = Vertex(name = 'V_862',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1415,(1,0):C.GC_1455,(3,0):C.GC_1467,(0,3):C.GC_1461,(2,3):C.GC_1473,(1,1):C.GC_1512,(3,1):C.GC_1534,(0,2):C.GC_1523,(2,2):C.GC_1545})

V_863 = Vertex(name = 'V_863',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2009,(0,5):C.GC_2018,(1,0):C.GC_2150,(3,0):C.GC_2162,(0,3):C.GC_2156,(2,3):C.GC_2168,(1,1):C.GC_2065,(3,1):C.GC_2087,(0,2):C.GC_2076,(2,2):C.GC_2098})

V_864 = Vertex(name = 'V_864',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2027,(1,0):C.GC_2153,(3,0):C.GC_2165,(0,3):C.GC_2159,(2,3):C.GC_2171,(1,1):C.GC_2070,(3,1):C.GC_2092,(0,2):C.GC_2081,(2,2):C.GC_2103})

V_865 = Vertex(name = 'V_865',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_984,(3,0):C.GC_990,(0,6):C.GC_980,(2,6):C.GC_986,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_983,(3,1):C.GC_989,(0,2):C.GC_981,(2,2):C.GC_987})

V_866 = Vertex(name = 'V_866',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_2630,(1,0):C.GC_985,(3,0):C.GC_991,(0,3):C.GC_982,(2,3):C.GC_988,(1,1):C.GC_985,(3,1):C.GC_991,(0,2):C.GC_982,(2,2):C.GC_988})

V_867 = Vertex(name = 'V_867',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2621,(1,0):C.GC_2704,(3,0):C.GC_2726,(0,3):C.GC_2714,(2,3):C.GC_2736,(1,1):C.GC_2703,(3,1):C.GC_2725,(0,2):C.GC_2715,(2,2):C.GC_2737})

V_868 = Vertex(name = 'V_868',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2639,(1,0):C.GC_2709,(3,0):C.GC_2731,(0,3):C.GC_2720,(2,3):C.GC_2742,(1,1):C.GC_2709,(3,1):C.GC_2731,(0,2):C.GC_2720,(2,2):C.GC_2742})

V_869 = Vertex(name = 'V_869',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1392,(0,5):C.GC_1401,(1,0):C.GC_1504,(3,0):C.GC_1526,(0,3):C.GC_1515,(2,3):C.GC_1537,(1,1):C.GC_1564,(3,1):C.GC_1576,(0,2):C.GC_1570,(2,2):C.GC_1582})

V_870 = Vertex(name = 'V_870',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1410,(1,0):C.GC_1509,(3,0):C.GC_1531,(0,3):C.GC_1520,(2,3):C.GC_1542,(1,1):C.GC_1567,(3,1):C.GC_1579,(0,2):C.GC_1573,(2,2):C.GC_1585})

V_871 = Vertex(name = 'V_871',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2004,(0,5):C.GC_2013,(1,0):C.GC_2183,(3,0):C.GC_2195,(0,3):C.GC_2189,(2,3):C.GC_2201,(1,1):C.GC_2126,(3,1):C.GC_2138,(0,2):C.GC_2132,(2,2):C.GC_2144})

V_872 = Vertex(name = 'V_872',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2022,(1,0):C.GC_2186,(3,0):C.GC_2198,(0,3):C.GC_2192,(2,3):C.GC_2204,(1,1):C.GC_2129,(3,1):C.GC_2141,(0,2):C.GC_2135,(2,2):C.GC_2147})

V_873 = Vertex(name = 'V_873',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2616,(0,5):C.GC_2625,(1,0):C.GC_2796,(3,0):C.GC_2808,(0,3):C.GC_2802,(2,3):C.GC_2814,(1,1):C.GC_2763,(3,1):C.GC_2775,(0,2):C.GC_2769,(2,2):C.GC_2781})

V_874 = Vertex(name = 'V_874',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2634,(1,0):C.GC_2799,(3,0):C.GC_2811,(0,3):C.GC_2805,(2,3):C.GC_2817,(1,1):C.GC_2766,(3,1):C.GC_2778,(0,2):C.GC_2772,(2,2):C.GC_2784})

V_875 = Vertex(name = 'V_875',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1395,(0,5):C.GC_1404,(1,0):C.GC_1425,(3,0):C.GC_1437,(0,3):C.GC_1431,(2,3):C.GC_1443,(1,1):C.GC_1565,(3,1):C.GC_1577,(0,2):C.GC_1571,(2,2):C.GC_1583})

V_876 = Vertex(name = 'V_876',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1413,(1,0):C.GC_1428,(3,0):C.GC_1440,(0,3):C.GC_1434,(2,3):C.GC_1446,(1,1):C.GC_1568,(3,1):C.GC_1580,(0,2):C.GC_1574,(2,2):C.GC_1586})

V_877 = Vertex(name = 'V_877',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2007,(0,5):C.GC_2016,(1,0):C.GC_2063,(3,0):C.GC_2085,(0,3):C.GC_2074,(2,3):C.GC_2096,(1,1):C.GC_2127,(3,1):C.GC_2139,(0,2):C.GC_2133,(2,2):C.GC_2145})

V_878 = Vertex(name = 'V_878',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2025,(1,0):C.GC_2068,(3,0):C.GC_2090,(0,3):C.GC_2079,(2,3):C.GC_2101,(1,1):C.GC_2130,(3,1):C.GC_2142,(0,2):C.GC_2136,(2,2):C.GC_2148})

V_879 = Vertex(name = 'V_879',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2619,(0,5):C.GC_2628,(1,0):C.GC_2650,(3,0):C.GC_2662,(0,3):C.GC_2656,(2,3):C.GC_2668,(1,1):C.GC_2764,(3,1):C.GC_2776,(0,2):C.GC_2770,(2,2):C.GC_2782})

V_880 = Vertex(name = 'V_880',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2637,(1,0):C.GC_2653,(3,0):C.GC_2665,(0,3):C.GC_2659,(2,3):C.GC_2671,(1,1):C.GC_2767,(3,1):C.GC_2779,(0,2):C.GC_2773,(2,2):C.GC_2785})

V_881 = Vertex(name = 'V_881',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1398,(0,5):C.GC_1407,(1,0):C.GC_1453,(3,0):C.GC_1465,(0,3):C.GC_1459,(2,3):C.GC_1471,(1,1):C.GC_1566,(3,1):C.GC_1578,(0,2):C.GC_1572,(2,2):C.GC_1584})

V_882 = Vertex(name = 'V_882',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1416,(1,0):C.GC_1456,(3,0):C.GC_1468,(0,3):C.GC_1462,(2,3):C.GC_1474,(1,1):C.GC_1569,(3,1):C.GC_1581,(0,2):C.GC_1575,(2,2):C.GC_1587})

V_883 = Vertex(name = 'V_883',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2010,(0,5):C.GC_2019,(1,0):C.GC_2151,(3,0):C.GC_2163,(0,3):C.GC_2157,(2,3):C.GC_2169,(1,1):C.GC_2128,(3,1):C.GC_2140,(0,2):C.GC_2134,(2,2):C.GC_2146})

V_884 = Vertex(name = 'V_884',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2028,(1,0):C.GC_2154,(3,0):C.GC_2166,(0,3):C.GC_2160,(2,3):C.GC_2172,(1,1):C.GC_2131,(3,1):C.GC_2143,(0,2):C.GC_2137,(2,2):C.GC_2149})

V_885 = Vertex(name = 'V_885',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2622,(0,5):C.GC_2631,(1,0):C.GC_2705,(3,0):C.GC_2727,(0,3):C.GC_2716,(2,3):C.GC_2738,(1,1):C.GC_2765,(3,1):C.GC_2777,(0,2):C.GC_2771,(2,2):C.GC_2783})

V_886 = Vertex(name = 'V_886',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2640,(1,0):C.GC_2710,(3,0):C.GC_2732,(0,3):C.GC_2721,(2,3):C.GC_2743,(1,1):C.GC_2768,(3,1):C.GC_2780,(0,2):C.GC_2774,(2,2):C.GC_2786})

V_887 = Vertex(name = 'V_887',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1393,(0,5):C.GC_1402,(1,0):C.GC_1505,(3,0):C.GC_1527,(0,3):C.GC_1516,(2,3):C.GC_1538,(1,1):C.GC_1478,(3,1):C.GC_1490,(0,2):C.GC_1484,(2,2):C.GC_1496})

V_888 = Vertex(name = 'V_888',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1411,(1,0):C.GC_1510,(3,0):C.GC_1532,(0,3):C.GC_1521,(2,3):C.GC_1543,(1,1):C.GC_1481,(3,1):C.GC_1493,(0,2):C.GC_1487,(2,2):C.GC_1499})

V_889 = Vertex(name = 'V_889',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2005,(0,5):C.GC_2014,(1,0):C.GC_2184,(3,0):C.GC_2196,(0,3):C.GC_2190,(2,3):C.GC_2202,(1,1):C.GC_2036,(3,1):C.GC_2048,(0,2):C.GC_2042,(2,2):C.GC_2054})

V_890 = Vertex(name = 'V_890',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2023,(1,0):C.GC_2187,(3,0):C.GC_2199,(0,3):C.GC_2193,(2,3):C.GC_2205,(1,1):C.GC_2039,(3,1):C.GC_2051,(0,2):C.GC_2045,(2,2):C.GC_2057})

V_891 = Vertex(name = 'V_891',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2617,(0,5):C.GC_2626,(1,0):C.GC_2797,(3,0):C.GC_2809,(0,3):C.GC_2803,(2,3):C.GC_2815,(1,1):C.GC_2677,(3,1):C.GC_2689,(0,2):C.GC_2683,(2,2):C.GC_2695})

V_892 = Vertex(name = 'V_892',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2635,(1,0):C.GC_2800,(3,0):C.GC_2812,(0,3):C.GC_2806,(2,3):C.GC_2818,(1,1):C.GC_2680,(3,1):C.GC_2692,(0,2):C.GC_2686,(2,2):C.GC_2698})

V_893 = Vertex(name = 'V_893',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1396,(0,5):C.GC_1405,(1,0):C.GC_1426,(3,0):C.GC_1438,(0,3):C.GC_1432,(2,3):C.GC_1444,(1,1):C.GC_1479,(3,1):C.GC_1491,(0,2):C.GC_1485,(2,2):C.GC_1497})

V_894 = Vertex(name = 'V_894',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1414,(1,0):C.GC_1429,(3,0):C.GC_1441,(0,3):C.GC_1435,(2,3):C.GC_1447,(1,1):C.GC_1482,(3,1):C.GC_1494,(0,2):C.GC_1488,(2,2):C.GC_1500})

V_895 = Vertex(name = 'V_895',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2008,(0,5):C.GC_2017,(1,0):C.GC_2064,(3,0):C.GC_2086,(0,3):C.GC_2075,(2,3):C.GC_2097,(1,1):C.GC_2037,(3,1):C.GC_2049,(0,2):C.GC_2043,(2,2):C.GC_2055})

V_896 = Vertex(name = 'V_896',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2026,(1,0):C.GC_2069,(3,0):C.GC_2091,(0,3):C.GC_2080,(2,3):C.GC_2102,(1,1):C.GC_2040,(3,1):C.GC_2052,(0,2):C.GC_2046,(2,2):C.GC_2058})

V_897 = Vertex(name = 'V_897',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2620,(0,5):C.GC_2629,(1,0):C.GC_2651,(3,0):C.GC_2663,(0,3):C.GC_2657,(2,3):C.GC_2669,(1,1):C.GC_2678,(3,1):C.GC_2690,(0,2):C.GC_2684,(2,2):C.GC_2696})

V_898 = Vertex(name = 'V_898',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2638,(1,0):C.GC_2654,(3,0):C.GC_2666,(0,3):C.GC_2660,(2,3):C.GC_2672,(1,1):C.GC_2681,(3,1):C.GC_2693,(0,2):C.GC_2687,(2,2):C.GC_2699})

V_899 = Vertex(name = 'V_899',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1399,(0,5):C.GC_1408,(1,0):C.GC_1454,(3,0):C.GC_1466,(0,3):C.GC_1460,(2,3):C.GC_1472,(1,1):C.GC_1480,(3,1):C.GC_1492,(0,2):C.GC_1486,(2,2):C.GC_1498})

V_900 = Vertex(name = 'V_900',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1417,(1,0):C.GC_1457,(3,0):C.GC_1469,(0,3):C.GC_1463,(2,3):C.GC_1475,(1,1):C.GC_1483,(3,1):C.GC_1495,(0,2):C.GC_1489,(2,2):C.GC_1501})

V_901 = Vertex(name = 'V_901',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2011,(0,5):C.GC_2020,(1,0):C.GC_2152,(3,0):C.GC_2164,(0,3):C.GC_2158,(2,3):C.GC_2170,(1,1):C.GC_2038,(3,1):C.GC_2050,(0,2):C.GC_2044,(2,2):C.GC_2056})

V_902 = Vertex(name = 'V_902',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2029,(1,0):C.GC_2155,(3,0):C.GC_2167,(0,3):C.GC_2161,(2,3):C.GC_2173,(1,1):C.GC_2041,(3,1):C.GC_2053,(0,2):C.GC_2047,(2,2):C.GC_2059})

V_903 = Vertex(name = 'V_903',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2623,(0,5):C.GC_2632,(1,0):C.GC_2706,(3,0):C.GC_2728,(0,3):C.GC_2717,(2,3):C.GC_2739,(1,1):C.GC_2679,(3,1):C.GC_2691,(0,2):C.GC_2685,(2,2):C.GC_2697})

V_904 = Vertex(name = 'V_904',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2641,(1,0):C.GC_2711,(3,0):C.GC_2733,(0,3):C.GC_2722,(2,3):C.GC_2744,(1,1):C.GC_2682,(3,1):C.GC_2694,(0,2):C.GC_2688,(2,2):C.GC_2700})

V_905 = Vertex(name = 'V_905',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1595,(0,5):C.GC_1604,(1,0):C.GC_1742,(3,0):C.GC_1764,(0,3):C.GC_1753,(2,3):C.GC_1775,(1,1):C.GC_1706,(3,1):C.GC_1718,(0,2):C.GC_1712,(2,2):C.GC_1724})

V_906 = Vertex(name = 'V_906',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1613,(1,0):C.GC_1748,(3,0):C.GC_1770,(0,3):C.GC_1759,(2,3):C.GC_1781,(1,1):C.GC_1709,(3,1):C.GC_1721,(0,2):C.GC_1715,(2,2):C.GC_1727})

V_907 = Vertex(name = 'V_907',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2207,(0,5):C.GC_2216,(1,0):C.GC_2386,(3,0):C.GC_2398,(0,3):C.GC_2392,(2,3):C.GC_2404,(1,1):C.GC_2264,(3,1):C.GC_2276,(0,2):C.GC_2270,(2,2):C.GC_2282})

V_908 = Vertex(name = 'V_908',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2225,(1,0):C.GC_2389,(3,0):C.GC_2401,(0,3):C.GC_2395,(2,3):C.GC_2407,(1,1):C.GC_2267,(3,1):C.GC_2279,(0,2):C.GC_2273,(2,2):C.GC_2285})

V_909 = Vertex(name = 'V_909',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2820,(0,5):C.GC_2829,(1,0):C.GC_3000,(3,0):C.GC_3012,(0,3):C.GC_3006,(2,3):C.GC_3018,(1,1):C.GC_2906,(3,1):C.GC_2918,(0,2):C.GC_2912,(2,2):C.GC_2924})

V_910 = Vertex(name = 'V_910',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2838,(1,0):C.GC_3003,(3,0):C.GC_3015,(0,3):C.GC_3009,(2,3):C.GC_3021,(1,1):C.GC_2909,(3,1):C.GC_2921,(0,2):C.GC_2915,(2,2):C.GC_2927})

V_911 = Vertex(name = 'V_911',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1598,(0,5):C.GC_1607,(1,0):C.GC_1628,(3,0):C.GC_1640,(0,3):C.GC_1634,(2,3):C.GC_1646,(1,1):C.GC_1707,(3,1):C.GC_1719,(0,2):C.GC_1713,(2,2):C.GC_1725})

V_912 = Vertex(name = 'V_912',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1616,(1,0):C.GC_1631,(3,0):C.GC_1643,(0,3):C.GC_1637,(2,3):C.GC_1649,(1,1):C.GC_1710,(3,1):C.GC_1722,(0,2):C.GC_1716,(2,2):C.GC_1728})

V_913 = Vertex(name = 'V_913',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2210,(0,5):C.GC_2219,(1,0):C.GC_2301,(3,0):C.GC_2323,(0,3):C.GC_2312,(2,3):C.GC_2334,(1,1):C.GC_2265,(3,1):C.GC_2277,(0,2):C.GC_2271,(2,2):C.GC_2283})

V_914 = Vertex(name = 'V_914',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2228,(1,0):C.GC_2307,(3,0):C.GC_2329,(0,3):C.GC_2318,(2,3):C.GC_2340,(1,1):C.GC_2268,(3,1):C.GC_2280,(0,2):C.GC_2274,(2,2):C.GC_2286})

V_915 = Vertex(name = 'V_915',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2823,(0,5):C.GC_2832,(1,0):C.GC_2854,(3,0):C.GC_2866,(0,3):C.GC_2860,(2,3):C.GC_2872,(1,1):C.GC_2907,(3,1):C.GC_2919,(0,2):C.GC_2913,(2,2):C.GC_2925})

V_916 = Vertex(name = 'V_916',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2841,(1,0):C.GC_2857,(3,0):C.GC_2869,(0,3):C.GC_2863,(2,3):C.GC_2875,(1,1):C.GC_2910,(3,1):C.GC_2922,(0,2):C.GC_2916,(2,2):C.GC_2928})

V_917 = Vertex(name = 'V_917',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1601,(0,5):C.GC_1610,(1,0):C.GC_1656,(3,0):C.GC_1668,(0,3):C.GC_1662,(2,3):C.GC_1674,(1,1):C.GC_1708,(3,1):C.GC_1720,(0,2):C.GC_1714,(2,2):C.GC_1726})

V_918 = Vertex(name = 'V_918',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1619,(1,0):C.GC_1659,(3,0):C.GC_1671,(0,3):C.GC_1665,(2,3):C.GC_1677,(1,1):C.GC_1711,(3,1):C.GC_1723,(0,2):C.GC_1717,(2,2):C.GC_1729})

V_919 = Vertex(name = 'V_919',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2213,(0,5):C.GC_2222,(1,0):C.GC_2354,(3,0):C.GC_2366,(0,3):C.GC_2360,(2,3):C.GC_2372,(1,1):C.GC_2266,(3,1):C.GC_2278,(0,2):C.GC_2272,(2,2):C.GC_2284})

V_920 = Vertex(name = 'V_920',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2231,(1,0):C.GC_2357,(3,0):C.GC_2369,(0,3):C.GC_2363,(2,3):C.GC_2375,(1,1):C.GC_2269,(3,1):C.GC_2281,(0,2):C.GC_2275,(2,2):C.GC_2287})

V_921 = Vertex(name = 'V_921',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2826,(0,5):C.GC_2835,(1,0):C.GC_2944,(3,0):C.GC_2966,(0,3):C.GC_2955,(2,3):C.GC_2977,(1,1):C.GC_2908,(3,1):C.GC_2920,(0,2):C.GC_2914,(2,2):C.GC_2926})

V_922 = Vertex(name = 'V_922',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2844,(1,0):C.GC_2950,(3,0):C.GC_2972,(0,3):C.GC_2961,(2,3):C.GC_2983,(1,1):C.GC_2911,(3,1):C.GC_2923,(0,2):C.GC_2917,(2,2):C.GC_2929})

V_923 = Vertex(name = 'V_923',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_1349,(3,0):C.GC_1355,(0,6):C.GC_1345,(2,6):C.GC_1351,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_1348,(3,1):C.GC_1354,(0,2):C.GC_1346,(2,2):C.GC_1352})

V_924 = Vertex(name = 'V_924',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_1605,(1,0):C.GC_1350,(3,0):C.GC_1356,(0,3):C.GC_1347,(2,3):C.GC_1353,(1,1):C.GC_1350,(3,1):C.GC_1356,(0,2):C.GC_1347,(2,2):C.GC_1353})

V_925 = Vertex(name = 'V_925',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1596,(1,0):C.GC_1744,(3,0):C.GC_1766,(0,3):C.GC_1754,(2,3):C.GC_1776,(1,1):C.GC_1743,(3,1):C.GC_1765,(0,2):C.GC_1755,(2,2):C.GC_1777})

V_926 = Vertex(name = 'V_926',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1614,(1,0):C.GC_1749,(3,0):C.GC_1771,(0,3):C.GC_1760,(2,3):C.GC_1782,(1,1):C.GC_1749,(3,1):C.GC_1771,(0,2):C.GC_1760,(2,2):C.GC_1782})

V_927 = Vertex(name = 'V_927',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2208,(0,5):C.GC_2217,(1,0):C.GC_2387,(3,0):C.GC_2399,(0,3):C.GC_2393,(2,3):C.GC_2405,(1,1):C.GC_2300,(3,1):C.GC_2322,(0,2):C.GC_2311,(2,2):C.GC_2333})

V_928 = Vertex(name = 'V_928',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2226,(1,0):C.GC_2390,(3,0):C.GC_2402,(0,3):C.GC_2396,(2,3):C.GC_2408,(1,1):C.GC_2306,(3,1):C.GC_2328,(0,2):C.GC_2317,(2,2):C.GC_2339})

V_929 = Vertex(name = 'V_929',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2821,(0,5):C.GC_2830,(1,0):C.GC_3001,(3,0):C.GC_3013,(0,3):C.GC_3007,(2,3):C.GC_3019,(1,1):C.GC_2942,(3,1):C.GC_2964,(0,2):C.GC_2953,(2,2):C.GC_2975})

V_930 = Vertex(name = 'V_930',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2839,(1,0):C.GC_3004,(3,0):C.GC_3016,(0,3):C.GC_3010,(2,3):C.GC_3022,(1,1):C.GC_2948,(3,1):C.GC_2970,(0,2):C.GC_2959,(2,2):C.GC_2981})

V_931 = Vertex(name = 'V_931',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1599,(0,5):C.GC_1608,(1,0):C.GC_1629,(3,0):C.GC_1641,(0,3):C.GC_1635,(2,3):C.GC_1647,(1,1):C.GC_1746,(3,1):C.GC_1768,(0,2):C.GC_1757,(2,2):C.GC_1779})

V_932 = Vertex(name = 'V_932',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1617,(1,0):C.GC_1632,(3,0):C.GC_1644,(0,3):C.GC_1638,(2,3):C.GC_1650,(1,1):C.GC_1751,(3,1):C.GC_1773,(0,2):C.GC_1762,(2,2):C.GC_1784})

V_933 = Vertex(name = 'V_933',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_872,(3,0):C.GC_878,(0,6):C.GC_868,(2,6):C.GC_874,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_871,(3,1):C.GC_877,(0,2):C.GC_869,(2,2):C.GC_875})

V_934 = Vertex(name = 'V_934',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_2220,(1,0):C.GC_873,(3,0):C.GC_879,(0,3):C.GC_870,(2,3):C.GC_876,(1,1):C.GC_873,(3,1):C.GC_879,(0,2):C.GC_870,(2,2):C.GC_876})

V_935 = Vertex(name = 'V_935',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2211,(1,0):C.GC_2303,(3,0):C.GC_2325,(0,3):C.GC_2313,(2,3):C.GC_2335,(1,1):C.GC_2302,(3,1):C.GC_2324,(0,2):C.GC_2314,(2,2):C.GC_2336})

V_936 = Vertex(name = 'V_936',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2229,(1,0):C.GC_2308,(3,0):C.GC_2330,(0,3):C.GC_2319,(2,3):C.GC_2341,(1,1):C.GC_2308,(3,1):C.GC_2330,(0,2):C.GC_2319,(2,2):C.GC_2341})

V_937 = Vertex(name = 'V_937',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2824,(0,5):C.GC_2833,(1,0):C.GC_2855,(3,0):C.GC_2867,(0,3):C.GC_2861,(2,3):C.GC_2873,(1,1):C.GC_2943,(3,1):C.GC_2965,(0,2):C.GC_2954,(2,2):C.GC_2976})

V_938 = Vertex(name = 'V_938',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2842,(1,0):C.GC_2858,(3,0):C.GC_2870,(0,3):C.GC_2864,(2,3):C.GC_2876,(1,1):C.GC_2949,(3,1):C.GC_2971,(0,2):C.GC_2960,(2,2):C.GC_2982})

V_939 = Vertex(name = 'V_939',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1602,(0,5):C.GC_1611,(1,0):C.GC_1657,(3,0):C.GC_1669,(0,3):C.GC_1663,(2,3):C.GC_1675,(1,1):C.GC_1747,(3,1):C.GC_1769,(0,2):C.GC_1758,(2,2):C.GC_1780})

V_940 = Vertex(name = 'V_940',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1620,(1,0):C.GC_1660,(3,0):C.GC_1672,(0,3):C.GC_1666,(2,3):C.GC_1678,(1,1):C.GC_1752,(3,1):C.GC_1774,(0,2):C.GC_1763,(2,2):C.GC_1785})

V_941 = Vertex(name = 'V_941',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2214,(0,5):C.GC_2223,(1,0):C.GC_2355,(3,0):C.GC_2367,(0,3):C.GC_2361,(2,3):C.GC_2373,(1,1):C.GC_2305,(3,1):C.GC_2327,(0,2):C.GC_2316,(2,2):C.GC_2338})

V_942 = Vertex(name = 'V_942',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2232,(1,0):C.GC_2358,(3,0):C.GC_2370,(0,3):C.GC_2364,(2,3):C.GC_2376,(1,1):C.GC_2310,(3,1):C.GC_2332,(0,2):C.GC_2321,(2,2):C.GC_2343})

V_943 = Vertex(name = 'V_943',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_1056,(3,0):C.GC_1062,(0,6):C.GC_1052,(2,6):C.GC_1058,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_1055,(3,1):C.GC_1061,(0,2):C.GC_1053,(2,2):C.GC_1059})

V_944 = Vertex(name = 'V_944',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_49,(0,5):C.GC_2836,(1,0):C.GC_1057,(3,0):C.GC_1063,(0,3):C.GC_1054,(2,3):C.GC_1060,(1,1):C.GC_1057,(3,1):C.GC_1063,(0,2):C.GC_1054,(2,2):C.GC_1060})

V_945 = Vertex(name = 'V_945',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2827,(1,0):C.GC_2946,(3,0):C.GC_2968,(0,3):C.GC_2956,(2,3):C.GC_2978,(1,1):C.GC_2945,(3,1):C.GC_2967,(0,2):C.GC_2957,(2,2):C.GC_2979})

V_946 = Vertex(name = 'V_946',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2845,(1,0):C.GC_2951,(3,0):C.GC_2973,(0,3):C.GC_2962,(2,3):C.GC_2984,(1,1):C.GC_2951,(3,1):C.GC_2973,(0,2):C.GC_2962,(2,2):C.GC_2984})

V_947 = Vertex(name = 'V_947',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1597,(0,5):C.GC_1606,(1,0):C.GC_1745,(3,0):C.GC_1767,(0,3):C.GC_1756,(2,3):C.GC_1778,(1,1):C.GC_1682,(3,1):C.GC_1694,(0,2):C.GC_1688,(2,2):C.GC_1700})

V_948 = Vertex(name = 'V_948',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1615,(1,0):C.GC_1750,(3,0):C.GC_1772,(0,3):C.GC_1761,(2,3):C.GC_1783,(1,1):C.GC_1685,(3,1):C.GC_1697,(0,2):C.GC_1691,(2,2):C.GC_1703})

V_949 = Vertex(name = 'V_949',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2209,(0,5):C.GC_2218,(1,0):C.GC_2388,(3,0):C.GC_2400,(0,3):C.GC_2394,(2,3):C.GC_2406,(1,1):C.GC_2240,(3,1):C.GC_2252,(0,2):C.GC_2246,(2,2):C.GC_2258})

V_950 = Vertex(name = 'V_950',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2227,(1,0):C.GC_2391,(3,0):C.GC_2403,(0,3):C.GC_2397,(2,3):C.GC_2409,(1,1):C.GC_2243,(3,1):C.GC_2255,(0,2):C.GC_2249,(2,2):C.GC_2261})

V_951 = Vertex(name = 'V_951',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2822,(0,5):C.GC_2831,(1,0):C.GC_3002,(3,0):C.GC_3014,(0,3):C.GC_3008,(2,3):C.GC_3020,(1,1):C.GC_2882,(3,1):C.GC_2894,(0,2):C.GC_2888,(2,2):C.GC_2900})

V_952 = Vertex(name = 'V_952',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2840,(1,0):C.GC_3005,(3,0):C.GC_3017,(0,3):C.GC_3011,(2,3):C.GC_3023,(1,1):C.GC_2885,(3,1):C.GC_2897,(0,2):C.GC_2891,(2,2):C.GC_2903})

V_953 = Vertex(name = 'V_953',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1600,(0,5):C.GC_1609,(1,0):C.GC_1630,(3,0):C.GC_1642,(0,3):C.GC_1636,(2,3):C.GC_1648,(1,1):C.GC_1683,(3,1):C.GC_1695,(0,2):C.GC_1689,(2,2):C.GC_1701})

V_954 = Vertex(name = 'V_954',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1618,(1,0):C.GC_1633,(3,0):C.GC_1645,(0,3):C.GC_1639,(2,3):C.GC_1651,(1,1):C.GC_1686,(3,1):C.GC_1698,(0,2):C.GC_1692,(2,2):C.GC_1704})

V_955 = Vertex(name = 'V_955',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2212,(0,5):C.GC_2221,(1,0):C.GC_2304,(3,0):C.GC_2326,(0,3):C.GC_2315,(2,3):C.GC_2337,(1,1):C.GC_2241,(3,1):C.GC_2253,(0,2):C.GC_2247,(2,2):C.GC_2259})

V_956 = Vertex(name = 'V_956',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2230,(1,0):C.GC_2309,(3,0):C.GC_2331,(0,3):C.GC_2320,(2,3):C.GC_2342,(1,1):C.GC_2244,(3,1):C.GC_2256,(0,2):C.GC_2250,(2,2):C.GC_2262})

V_957 = Vertex(name = 'V_957',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2825,(0,5):C.GC_2834,(1,0):C.GC_2856,(3,0):C.GC_2868,(0,3):C.GC_2862,(2,3):C.GC_2874,(1,1):C.GC_2883,(3,1):C.GC_2895,(0,2):C.GC_2889,(2,2):C.GC_2901})

V_958 = Vertex(name = 'V_958',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2843,(1,0):C.GC_2859,(3,0):C.GC_2871,(0,3):C.GC_2865,(2,3):C.GC_2877,(1,1):C.GC_2886,(3,1):C.GC_2898,(0,2):C.GC_2892,(2,2):C.GC_2904})

V_959 = Vertex(name = 'V_959',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1603,(0,5):C.GC_1612,(1,0):C.GC_1658,(3,0):C.GC_1670,(0,3):C.GC_1664,(2,3):C.GC_1676,(1,1):C.GC_1684,(3,1):C.GC_1696,(0,2):C.GC_1690,(2,2):C.GC_1702})

V_960 = Vertex(name = 'V_960',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1621,(1,0):C.GC_1661,(3,0):C.GC_1673,(0,3):C.GC_1667,(2,3):C.GC_1679,(1,1):C.GC_1687,(3,1):C.GC_1699,(0,2):C.GC_1693,(2,2):C.GC_1705})

V_961 = Vertex(name = 'V_961',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2215,(0,5):C.GC_2224,(1,0):C.GC_2356,(3,0):C.GC_2368,(0,3):C.GC_2362,(2,3):C.GC_2374,(1,1):C.GC_2242,(3,1):C.GC_2254,(0,2):C.GC_2248,(2,2):C.GC_2260})

V_962 = Vertex(name = 'V_962',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2233,(1,0):C.GC_2359,(3,0):C.GC_2371,(0,3):C.GC_2365,(2,3):C.GC_2377,(1,1):C.GC_2245,(3,1):C.GC_2257,(0,2):C.GC_2251,(2,2):C.GC_2263})

V_963 = Vertex(name = 'V_963',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2828,(0,5):C.GC_2837,(1,0):C.GC_2947,(3,0):C.GC_2969,(0,3):C.GC_2958,(2,3):C.GC_2980,(1,1):C.GC_2884,(3,1):C.GC_2896,(0,2):C.GC_2890,(2,2):C.GC_2902})

V_964 = Vertex(name = 'V_964',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2846,(1,0):C.GC_2952,(3,0):C.GC_2974,(0,3):C.GC_2963,(2,3):C.GC_2985,(1,1):C.GC_2887,(3,1):C.GC_2899,(0,2):C.GC_2893,(2,2):C.GC_2905})

V_965 = Vertex(name = 'V_965',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1799,(0,5):C.GC_1808,(1,0):C.GC_1886,(3,0):C.GC_1908,(0,3):C.GC_1897,(2,3):C.GC_1919,(1,1):C.GC_1936,(3,1):C.GC_1948,(0,2):C.GC_1942,(2,2):C.GC_1954})

V_966 = Vertex(name = 'V_966',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1817,(1,0):C.GC_1892,(3,0):C.GC_1914,(0,3):C.GC_1903,(2,3):C.GC_1925,(1,1):C.GC_1939,(3,1):C.GC_1951,(0,2):C.GC_1945,(2,2):C.GC_1957})

V_967 = Vertex(name = 'V_967',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2411,(0,5):C.GC_2420,(1,0):C.GC_2590,(3,0):C.GC_2602,(0,3):C.GC_2596,(2,3):C.GC_2608,(1,1):C.GC_2494,(3,1):C.GC_2506,(0,2):C.GC_2500,(2,2):C.GC_2512})

V_968 = Vertex(name = 'V_968',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2429,(1,0):C.GC_2593,(3,0):C.GC_2605,(0,3):C.GC_2599,(2,3):C.GC_2611,(1,1):C.GC_2497,(3,1):C.GC_2509,(0,2):C.GC_2503,(2,2):C.GC_2515})

V_969 = Vertex(name = 'V_969',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3025,(0,5):C.GC_3034,(1,0):C.GC_3205,(3,0):C.GC_3217,(0,3):C.GC_3211,(2,3):C.GC_3223,(1,1):C.GC_3137,(3,1):C.GC_3149,(0,2):C.GC_3143,(2,2):C.GC_3155})

V_970 = Vertex(name = 'V_970',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_3043,(1,0):C.GC_3208,(3,0):C.GC_3220,(0,3):C.GC_3214,(2,3):C.GC_3226,(1,1):C.GC_3140,(3,1):C.GC_3152,(0,2):C.GC_3146,(2,2):C.GC_3158})

V_971 = Vertex(name = 'V_971',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1802,(0,5):C.GC_1811,(1,0):C.GC_1832,(3,0):C.GC_1844,(0,3):C.GC_1838,(2,3):C.GC_1850,(1,1):C.GC_1937,(3,1):C.GC_1949,(0,2):C.GC_1943,(2,2):C.GC_1955})

V_972 = Vertex(name = 'V_972',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1820,(1,0):C.GC_1835,(3,0):C.GC_1847,(0,3):C.GC_1841,(2,3):C.GC_1853,(1,1):C.GC_1940,(3,1):C.GC_1952,(0,2):C.GC_1946,(2,2):C.GC_1958})

V_973 = Vertex(name = 'V_973',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2414,(0,5):C.GC_2423,(1,0):C.GC_2445,(3,0):C.GC_2467,(0,3):C.GC_2456,(2,3):C.GC_2478,(1,1):C.GC_2495,(3,1):C.GC_2507,(0,2):C.GC_2501,(2,2):C.GC_2513})

V_974 = Vertex(name = 'V_974',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2432,(1,0):C.GC_2451,(3,0):C.GC_2473,(0,3):C.GC_2462,(2,3):C.GC_2484,(1,1):C.GC_2498,(3,1):C.GC_2510,(0,2):C.GC_2504,(2,2):C.GC_2516})

V_975 = Vertex(name = 'V_975',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3028,(0,5):C.GC_3037,(1,0):C.GC_3059,(3,0):C.GC_3071,(0,3):C.GC_3065,(2,3):C.GC_3077,(1,1):C.GC_3138,(3,1):C.GC_3150,(0,2):C.GC_3144,(2,2):C.GC_3156})

V_976 = Vertex(name = 'V_976',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_3046,(1,0):C.GC_3062,(3,0):C.GC_3074,(0,3):C.GC_3068,(2,3):C.GC_3080,(1,1):C.GC_3141,(3,1):C.GC_3153,(0,2):C.GC_3147,(2,2):C.GC_3159})

V_977 = Vertex(name = 'V_977',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1805,(0,5):C.GC_1814,(1,0):C.GC_1860,(3,0):C.GC_1872,(0,3):C.GC_1866,(2,3):C.GC_1878,(1,1):C.GC_1938,(3,1):C.GC_1950,(0,2):C.GC_1944,(2,2):C.GC_1956})

V_978 = Vertex(name = 'V_978',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1823,(1,0):C.GC_1863,(3,0):C.GC_1875,(0,3):C.GC_1869,(2,3):C.GC_1881,(1,1):C.GC_1941,(3,1):C.GC_1953,(0,2):C.GC_1947,(2,2):C.GC_1959})

V_979 = Vertex(name = 'V_979',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2417,(0,5):C.GC_2426,(1,0):C.GC_2558,(3,0):C.GC_2570,(0,3):C.GC_2564,(2,3):C.GC_2576,(1,1):C.GC_2496,(3,1):C.GC_2508,(0,2):C.GC_2502,(2,2):C.GC_2514})

V_980 = Vertex(name = 'V_980',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2435,(1,0):C.GC_2561,(3,0):C.GC_2573,(0,3):C.GC_2567,(2,3):C.GC_2579,(1,1):C.GC_2499,(3,1):C.GC_2511,(0,2):C.GC_2505,(2,2):C.GC_2517})

V_981 = Vertex(name = 'V_981',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3031,(0,5):C.GC_3040,(1,0):C.GC_3089,(3,0):C.GC_3111,(0,3):C.GC_3100,(2,3):C.GC_3122,(1,1):C.GC_3139,(3,1):C.GC_3151,(0,2):C.GC_3145,(2,2):C.GC_3157})

V_982 = Vertex(name = 'V_982',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_3049,(1,0):C.GC_3095,(3,0):C.GC_3117,(0,3):C.GC_3106,(2,3):C.GC_3128,(1,1):C.GC_3142,(3,1):C.GC_3154,(0,2):C.GC_3148,(2,2):C.GC_3160})

V_983 = Vertex(name = 'V_983',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1800,(0,5):C.GC_1809,(1,0):C.GC_1887,(3,0):C.GC_1909,(0,3):C.GC_1898,(2,3):C.GC_1920,(1,1):C.GC_1972,(3,1):C.GC_1984,(0,2):C.GC_1978,(2,2):C.GC_1990})

V_984 = Vertex(name = 'V_984',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1818,(1,0):C.GC_1893,(3,0):C.GC_1915,(0,3):C.GC_1904,(2,3):C.GC_1926,(1,1):C.GC_1975,(3,1):C.GC_1987,(0,2):C.GC_1981,(2,2):C.GC_1993})

V_985 = Vertex(name = 'V_985',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2412,(0,5):C.GC_2421,(1,0):C.GC_2591,(3,0):C.GC_2603,(0,3):C.GC_2597,(2,3):C.GC_2609,(1,1):C.GC_2534,(3,1):C.GC_2546,(0,2):C.GC_2540,(2,2):C.GC_2552})

V_986 = Vertex(name = 'V_986',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2430,(1,0):C.GC_2594,(3,0):C.GC_2606,(0,3):C.GC_2600,(2,3):C.GC_2612,(1,1):C.GC_2537,(3,1):C.GC_2549,(0,2):C.GC_2543,(2,2):C.GC_2555})

V_987 = Vertex(name = 'V_987',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3026,(0,5):C.GC_3035,(1,0):C.GC_3206,(3,0):C.GC_3218,(0,3):C.GC_3212,(2,3):C.GC_3224,(1,1):C.GC_3173,(3,1):C.GC_3185,(0,2):C.GC_3179,(2,2):C.GC_3191})

V_988 = Vertex(name = 'V_988',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_3044,(1,0):C.GC_3209,(3,0):C.GC_3221,(0,3):C.GC_3215,(2,3):C.GC_3227,(1,1):C.GC_3176,(3,1):C.GC_3188,(0,2):C.GC_3182,(2,2):C.GC_3194})

V_989 = Vertex(name = 'V_989',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1803,(0,5):C.GC_1812,(1,0):C.GC_1833,(3,0):C.GC_1845,(0,3):C.GC_1839,(2,3):C.GC_1851,(1,1):C.GC_1973,(3,1):C.GC_1985,(0,2):C.GC_1979,(2,2):C.GC_1991})

V_990 = Vertex(name = 'V_990',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1821,(1,0):C.GC_1836,(3,0):C.GC_1848,(0,3):C.GC_1842,(2,3):C.GC_1854,(1,1):C.GC_1976,(3,1):C.GC_1988,(0,2):C.GC_1982,(2,2):C.GC_1994})

V_991 = Vertex(name = 'V_991',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2415,(0,5):C.GC_2424,(1,0):C.GC_2446,(3,0):C.GC_2468,(0,3):C.GC_2457,(2,3):C.GC_2479,(1,1):C.GC_2535,(3,1):C.GC_2547,(0,2):C.GC_2541,(2,2):C.GC_2553})

V_992 = Vertex(name = 'V_992',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2433,(1,0):C.GC_2452,(3,0):C.GC_2474,(0,3):C.GC_2463,(2,3):C.GC_2485,(1,1):C.GC_2538,(3,1):C.GC_2550,(0,2):C.GC_2544,(2,2):C.GC_2556})

V_993 = Vertex(name = 'V_993',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3029,(0,5):C.GC_3038,(1,0):C.GC_3060,(3,0):C.GC_3072,(0,3):C.GC_3066,(2,3):C.GC_3078,(1,1):C.GC_3174,(3,1):C.GC_3186,(0,2):C.GC_3180,(2,2):C.GC_3192})

V_994 = Vertex(name = 'V_994',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_3047,(1,0):C.GC_3063,(3,0):C.GC_3075,(0,3):C.GC_3069,(2,3):C.GC_3081,(1,1):C.GC_3177,(3,1):C.GC_3189,(0,2):C.GC_3183,(2,2):C.GC_3195})

V_995 = Vertex(name = 'V_995',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1806,(0,5):C.GC_1815,(1,0):C.GC_1861,(3,0):C.GC_1873,(0,3):C.GC_1867,(2,3):C.GC_1879,(1,1):C.GC_1974,(3,1):C.GC_1986,(0,2):C.GC_1980,(2,2):C.GC_1992})

V_996 = Vertex(name = 'V_996',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1824,(1,0):C.GC_1864,(3,0):C.GC_1876,(0,3):C.GC_1870,(2,3):C.GC_1882,(1,1):C.GC_1977,(3,1):C.GC_1989,(0,2):C.GC_1983,(2,2):C.GC_1995})

V_997 = Vertex(name = 'V_997',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2418,(0,5):C.GC_2427,(1,0):C.GC_2559,(3,0):C.GC_2571,(0,3):C.GC_2565,(2,3):C.GC_2577,(1,1):C.GC_2536,(3,1):C.GC_2548,(0,2):C.GC_2542,(2,2):C.GC_2554})

V_998 = Vertex(name = 'V_998',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2436,(1,0):C.GC_2562,(3,0):C.GC_2574,(0,3):C.GC_2568,(2,3):C.GC_2580,(1,1):C.GC_2539,(3,1):C.GC_2551,(0,2):C.GC_2545,(2,2):C.GC_2557})

V_999 = Vertex(name = 'V_999',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_3032,(0,5):C.GC_3041,(1,0):C.GC_3090,(3,0):C.GC_3112,(0,3):C.GC_3101,(2,3):C.GC_3123,(1,1):C.GC_3175,(3,1):C.GC_3187,(0,2):C.GC_3181,(2,2):C.GC_3193})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3050,(1,0):C.GC_3096,(3,0):C.GC_3118,(0,3):C.GC_3107,(2,3):C.GC_3129,(1,1):C.GC_3178,(3,1):C.GC_3190,(0,2):C.GC_3184,(2,2):C.GC_3196})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_1259,(3,0):C.GC_1265,(0,6):C.GC_1255,(2,6):C.GC_1261,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_1258,(3,1):C.GC_1264,(0,2):C.GC_1256,(2,2):C.GC_1262})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_49,(0,5):C.GC_1810,(1,0):C.GC_1260,(3,0):C.GC_1266,(0,3):C.GC_1257,(2,3):C.GC_1263,(1,1):C.GC_1260,(3,1):C.GC_1266,(0,2):C.GC_1257,(2,2):C.GC_1263})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1801,(1,0):C.GC_1889,(3,0):C.GC_1911,(0,3):C.GC_1899,(2,3):C.GC_1921,(1,1):C.GC_1888,(3,1):C.GC_1910,(0,2):C.GC_1900,(2,2):C.GC_1922})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1819,(1,0):C.GC_1894,(3,0):C.GC_1916,(0,3):C.GC_1905,(2,3):C.GC_1927,(1,1):C.GC_1894,(3,1):C.GC_1916,(0,2):C.GC_1905,(2,2):C.GC_1927})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2413,(0,5):C.GC_2422,(1,0):C.GC_2592,(3,0):C.GC_2604,(0,3):C.GC_2598,(2,3):C.GC_2610,(1,1):C.GC_2444,(3,1):C.GC_2466,(0,2):C.GC_2455,(2,2):C.GC_2477})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2431,(1,0):C.GC_2595,(3,0):C.GC_2607,(0,3):C.GC_2601,(2,3):C.GC_2613,(1,1):C.GC_2450,(3,1):C.GC_2472,(0,2):C.GC_2461,(2,2):C.GC_2483})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3027,(0,5):C.GC_3036,(1,0):C.GC_3207,(3,0):C.GC_3219,(0,3):C.GC_3213,(2,3):C.GC_3225,(1,1):C.GC_3087,(3,1):C.GC_3109,(0,2):C.GC_3098,(2,2):C.GC_3120})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3045,(1,0):C.GC_3210,(3,0):C.GC_3222,(0,3):C.GC_3216,(2,3):C.GC_3228,(1,1):C.GC_3093,(3,1):C.GC_3115,(0,2):C.GC_3104,(2,2):C.GC_3126})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1804,(0,5):C.GC_1813,(1,0):C.GC_1834,(3,0):C.GC_1846,(0,3):C.GC_1840,(2,3):C.GC_1852,(1,1):C.GC_1890,(3,1):C.GC_1912,(0,2):C.GC_1901,(2,2):C.GC_1923})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1822,(1,0):C.GC_1837,(3,0):C.GC_1849,(0,3):C.GC_1843,(2,3):C.GC_1855,(1,1):C.GC_1895,(3,1):C.GC_1917,(0,2):C.GC_1906,(2,2):C.GC_1928})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_538,(3,0):C.GC_544,(0,6):C.GC_534,(2,6):C.GC_540,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_537,(3,1):C.GC_543,(0,2):C.GC_535,(2,2):C.GC_541})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_49,(0,5):C.GC_2425,(1,0):C.GC_539,(3,0):C.GC_545,(0,3):C.GC_536,(2,3):C.GC_542,(1,1):C.GC_539,(3,1):C.GC_545,(0,2):C.GC_536,(2,2):C.GC_542})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2416,(1,0):C.GC_2448,(3,0):C.GC_2470,(0,3):C.GC_2458,(2,3):C.GC_2480,(1,1):C.GC_2447,(3,1):C.GC_2469,(0,2):C.GC_2459,(2,2):C.GC_2481})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2434,(1,0):C.GC_2453,(3,0):C.GC_2475,(0,3):C.GC_2464,(2,3):C.GC_2486,(1,1):C.GC_2453,(3,1):C.GC_2475,(0,2):C.GC_2464,(2,2):C.GC_2486})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3030,(0,5):C.GC_3039,(1,0):C.GC_3061,(3,0):C.GC_3073,(0,3):C.GC_3067,(2,3):C.GC_3079,(1,1):C.GC_3088,(3,1):C.GC_3110,(0,2):C.GC_3099,(2,2):C.GC_3121})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3048,(1,0):C.GC_3064,(3,0):C.GC_3076,(0,3):C.GC_3070,(2,3):C.GC_3082,(1,1):C.GC_3094,(3,1):C.GC_3116,(0,2):C.GC_3105,(2,2):C.GC_3127})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1807,(0,5):C.GC_1816,(1,0):C.GC_1862,(3,0):C.GC_1874,(0,3):C.GC_1868,(2,3):C.GC_1880,(1,1):C.GC_1891,(3,1):C.GC_1913,(0,2):C.GC_1902,(2,2):C.GC_1924})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1825,(1,0):C.GC_1865,(3,0):C.GC_1877,(0,3):C.GC_1871,(2,3):C.GC_1883,(1,1):C.GC_1896,(3,1):C.GC_1918,(0,2):C.GC_1907,(2,2):C.GC_1929})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2419,(0,5):C.GC_2428,(1,0):C.GC_2560,(3,0):C.GC_2572,(0,3):C.GC_2566,(2,3):C.GC_2578,(1,1):C.GC_2449,(3,1):C.GC_2471,(0,2):C.GC_2460,(2,2):C.GC_2482})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2437,(1,0):C.GC_2563,(3,0):C.GC_2575,(0,3):C.GC_2569,(2,3):C.GC_2581,(1,1):C.GC_2454,(3,1):C.GC_2476,(0,2):C.GC_2465,(2,2):C.GC_2487})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_47,(0,8):C.GC_52,(1,0):C.GC_966,(3,0):C.GC_972,(0,6):C.GC_962,(2,6):C.GC_968,(1,5):C.GC_44,(3,5):C.GC_45,(1,3):C.GC_53,(3,3):C.GC_54,(1,4):C.GC_59,(3,4):C.GC_60,(1,1):C.GC_965,(3,1):C.GC_971,(0,2):C.GC_963,(2,2):C.GC_969})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_49,(0,5):C.GC_3042,(1,0):C.GC_967,(3,0):C.GC_973,(0,3):C.GC_964,(2,3):C.GC_970,(1,1):C.GC_967,(3,1):C.GC_973,(0,2):C.GC_964,(2,2):C.GC_970})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3033,(1,0):C.GC_3092,(3,0):C.GC_3114,(0,3):C.GC_3102,(2,3):C.GC_3124,(1,1):C.GC_3091,(3,1):C.GC_3113,(0,2):C.GC_3103,(2,2):C.GC_3125})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3051,(1,0):C.GC_3097,(3,0):C.GC_3119,(0,3):C.GC_3108,(2,3):C.GC_3130,(1,1):C.GC_3097,(3,1):C.GC_3119,(0,2):C.GC_3108,(2,2):C.GC_3130})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1303,(0,9):C.GC_1301,(0,10):C.GC_1301,(0,5):C.GC_1291,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1300,(0,4):C.GC_1302,(0,6):C.GC_1302,(0,0):C.GC_1292})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1311,(0,6):C.GC_1310,(0,7):C.GC_1310,(0,2):C.GC_1296,(0,4):C.GC_1311,(0,1):C.GC_1310,(0,3):C.GC_1310,(0,0):C.GC_1296})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_695,(0,9):C.GC_693,(0,10):C.GC_693,(0,5):C.GC_683,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_692,(0,4):C.GC_694,(0,6):C.GC_694,(0,0):C.GC_684})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_703,(0,6):C.GC_702,(0,7):C.GC_702,(0,2):C.GC_688,(0,4):C.GC_703,(0,1):C.GC_702,(0,3):C.GC_702,(0,0):C.GC_688})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1010,(0,9):C.GC_1008,(0,10):C.GC_1008,(0,5):C.GC_998,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1007,(0,4):C.GC_1009,(0,6):C.GC_1009,(0,0):C.GC_999})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1018,(0,6):C.GC_1017,(0,7):C.GC_1017,(0,2):C.GC_1003,(0,4):C.GC_1018,(0,1):C.GC_1017,(0,3):C.GC_1017,(0,0):C.GC_1003})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1330,(0,9):C.GC_1328,(0,10):C.GC_1328,(0,5):C.GC_1318,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1327,(0,4):C.GC_1329,(0,6):C.GC_1329,(0,0):C.GC_1319})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1338,(0,6):C.GC_1337,(0,7):C.GC_1337,(0,2):C.GC_1323,(0,4):C.GC_1338,(0,1):C.GC_1337,(0,3):C.GC_1337,(0,0):C.GC_1323})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_788,(0,9):C.GC_786,(0,10):C.GC_786,(0,5):C.GC_776,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_785,(0,4):C.GC_787,(0,6):C.GC_787,(0,0):C.GC_777})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_796,(0,6):C.GC_795,(0,7):C.GC_795,(0,2):C.GC_781,(0,4):C.GC_796,(0,1):C.GC_795,(0,3):C.GC_795,(0,0):C.GC_781})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1037,(0,9):C.GC_1035,(0,10):C.GC_1035,(0,5):C.GC_1025,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1034,(0,4):C.GC_1036,(0,6):C.GC_1036,(0,0):C.GC_1026})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1045,(0,6):C.GC_1044,(0,7):C.GC_1044,(0,2):C.GC_1030,(0,4):C.GC_1045,(0,1):C.GC_1044,(0,3):C.GC_1044,(0,0):C.GC_1030})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
                couplings = {(0,11):C.GC_1382,(0,8):C.GC_31,(0,12):C.GC_1375,(0,9):C.GC_1373,(0,10):C.GC_1373,(0,5):C.GC_1363,(0,4):C.GC_1374,(0,6):C.GC_1374,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1372,(0,0):C.GC_1364})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,7):C.GC_1383,(0,6):C.GC_1382,(0,2):C.GC_1368,(0,1):C.GC_1382,(0,3):C.GC_1382,(0,4):C.GC_1383,(0,0):C.GC_1368})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1139,(0,9):C.GC_1137,(0,10):C.GC_1137,(0,5):C.GC_1127,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1136,(0,4):C.GC_1138,(0,6):C.GC_1138,(0,0):C.GC_1128})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1147,(0,6):C.GC_1146,(0,7):C.GC_1146,(0,2):C.GC_1132,(0,4):C.GC_1147,(0,1):C.GC_1146,(0,3):C.GC_1146,(0,0):C.GC_1132})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_31,(0,11):C.GC_1184,(0,9):C.GC_1182,(0,10):C.GC_1182,(0,5):C.GC_1172,(0,1):C.GC_46,(0,2):C.GC_43,(0,3):C.GC_17,(0,7):C.GC_1181,(0,4):C.GC_1183,(0,6):C.GC_1183,(0,0):C.GC_1173})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_32,(0,8):C.GC_1192,(0,6):C.GC_1191,(0,7):C.GC_1191,(0,2):C.GC_1177,(0,4):C.GC_1192,(0,1):C.GC_1191,(0,3):C.GC_1191,(0,0):C.GC_1177})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_53,(2,0):C.GC_54,(1,3):C.GC_53,(3,3):C.GC_54,(1,1):C.GC_53,(3,1):C.GC_54,(1,2):C.GC_61,(0,4):C.GC_53,(2,4):C.GC_54,(0,5):C.GC_61})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_62,(0,1):C.GC_62})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_53,(2,2):C.GC_54,(1,0):C.GC_53,(2,0):C.GC_54,(1,1):C.GC_61,(0,3):C.GC_62})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_53,(2,2):C.GC_54,(1,0):C.GC_53,(2,0):C.GC_54,(1,1):C.GC_61,(0,3):C.GC_62})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_53,(2,0):C.GC_54,(1,3):C.GC_53,(3,3):C.GC_54,(1,1):C.GC_53,(3,1):C.GC_54,(1,2):C.GC_61,(0,4):C.GC_53,(2,4):C.GC_54,(0,5):C.GC_61})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_62,(0,1):C.GC_62})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_47,(0,5):C.GC_48,(1,2):C.GC_53,(2,2):C.GC_54,(1,0):C.GC_53,(2,0):C.GC_54,(1,1):C.GC_61,(0,3):C.GC_62})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_51})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_47,(0,7):C.GC_47,(0,0):C.GC_53,(2,0):C.GC_54,(1,3):C.GC_53,(3,3):C.GC_54,(1,1):C.GC_53,(3,1):C.GC_54,(1,2):C.GC_61,(0,4):C.GC_53,(2,4):C.GC_54,(0,5):C.GC_61})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_48,(0,3):C.GC_48,(1,0):C.GC_62,(0,1):C.GC_62})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_50,(0,1):C.GC_50})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_51,(0,1):C.GC_51})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_29,(0,0):C.GC_28})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_29})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_30})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_30})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_29})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_30})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_29,(0,1):C.GC_29})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_30,(0,1):C.GC_30})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_43})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_33})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1555,(0,2):C.GC_1554,(0,3):C.GC_1554,(0,0):C.GC_1448,(0,1):C.GC_1552})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1557,(0,2):C.GC_1556,(0,3):C.GC_1556,(0,0):C.GC_1449,(0,1):C.GC_1553})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2002,(0,4):C.GC_2113,(0,2):C.GC_2112,(0,3):C.GC_2112,(0,0):C.GC_2116,(0,1):C.GC_2110})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2115,(0,2):C.GC_2114,(0,3):C.GC_2114,(0,0):C.GC_2117,(0,1):C.GC_2111})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2614,(0,4):C.GC_2754,(0,2):C.GC_2753,(0,3):C.GC_2753,(0,0):C.GC_2673,(0,1):C.GC_2751})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2756,(0,2):C.GC_2755,(0,3):C.GC_2755,(0,0):C.GC_2674,(0,1):C.GC_2752})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1561,(0,2):C.GC_1560,(0,3):C.GC_1560,(0,0):C.GC_1450,(0,1):C.GC_1558})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1563,(0,2):C.GC_1562,(0,3):C.GC_1562,(0,0):C.GC_1451,(0,1):C.GC_1559})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2002,(0,4):C.GC_2121,(0,2):C.GC_2120,(0,3):C.GC_2120,(0,0):C.GC_2124,(0,1):C.GC_2118})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2123,(0,2):C.GC_2122,(0,3):C.GC_2122,(0,0):C.GC_2125,(0,1):C.GC_2119})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2614,(0,4):C.GC_2760,(0,2):C.GC_2759,(0,3):C.GC_2759,(0,0):C.GC_2675,(0,1):C.GC_2757})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2762,(0,2):C.GC_2761,(0,3):C.GC_2761,(0,0):C.GC_2676,(0,1):C.GC_2758})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1591,(0,2):C.GC_1590,(0,3):C.GC_1590,(0,0):C.GC_1476,(0,1):C.GC_1588})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1593,(0,2):C.GC_1592,(0,3):C.GC_1592,(0,0):C.GC_1477,(0,1):C.GC_1589})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2002,(0,4):C.GC_2177,(0,2):C.GC_2176,(0,3):C.GC_2176,(0,0):C.GC_2180,(0,1):C.GC_2174})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2179,(0,2):C.GC_2178,(0,3):C.GC_2178,(0,0):C.GC_2181,(0,1):C.GC_2175})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2614,(0,4):C.GC_2792,(0,2):C.GC_2791,(0,3):C.GC_2791,(0,0):C.GC_2787,(0,1):C.GC_2789})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2794,(0,2):C.GC_2793,(0,3):C.GC_2793,(0,0):C.GC_2788,(0,1):C.GC_2790})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1594,(0,4):C.GC_1733,(0,2):C.GC_1732,(0,3):C.GC_1732,(0,0):C.GC_1652,(0,1):C.GC_1730})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1735,(0,2):C.GC_1734,(0,3):C.GC_1734,(0,0):C.GC_1653,(0,1):C.GC_1731})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2206,(0,4):C.GC_2291,(0,2):C.GC_2290,(0,3):C.GC_2290,(0,0):C.GC_2350,(0,1):C.GC_2288})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2293,(0,2):C.GC_2292,(0,3):C.GC_2292,(0,0):C.GC_2351,(0,1):C.GC_2289})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2819,(0,4):C.GC_2933,(0,2):C.GC_2932,(0,3):C.GC_2932,(0,0):C.GC_2878,(0,1):C.GC_2930})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2935,(0,2):C.GC_2934,(0,3):C.GC_2934,(0,0):C.GC_2879,(0,1):C.GC_2931})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1594,(0,4):C.GC_1739,(0,2):C.GC_1738,(0,3):C.GC_1738,(0,0):C.GC_1654,(0,1):C.GC_1736})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1741,(0,2):C.GC_1740,(0,3):C.GC_1740,(0,0):C.GC_1655,(0,1):C.GC_1737})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2206,(0,4):C.GC_2297,(0,2):C.GC_2296,(0,3):C.GC_2296,(0,0):C.GC_2352,(0,1):C.GC_2294})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2299,(0,2):C.GC_2298,(0,3):C.GC_2298,(0,0):C.GC_2353,(0,1):C.GC_2295})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2819,(0,4):C.GC_2939,(0,2):C.GC_2938,(0,3):C.GC_2938,(0,0):C.GC_2880,(0,1):C.GC_2936})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2941,(0,2):C.GC_2940,(0,3):C.GC_2940,(0,0):C.GC_2881,(0,1):C.GC_2937})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1594,(0,4):C.GC_1795,(0,2):C.GC_1794,(0,3):C.GC_1794,(0,0):C.GC_1680,(0,1):C.GC_1792})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1797,(0,2):C.GC_1796,(0,3):C.GC_1796,(0,0):C.GC_1681,(0,1):C.GC_1793})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2206,(0,4):C.GC_2381,(0,2):C.GC_2380,(0,3):C.GC_2380,(0,0):C.GC_2384,(0,1):C.GC_2378})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2383,(0,2):C.GC_2382,(0,3):C.GC_2382,(0,0):C.GC_2385,(0,1):C.GC_2379})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2819,(0,4):C.GC_2997,(0,2):C.GC_2996,(0,3):C.GC_2996,(0,0):C.GC_2992,(0,1):C.GC_2994})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2999,(0,2):C.GC_2998,(0,3):C.GC_2998,(0,0):C.GC_2993,(0,1):C.GC_2995})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1798,(0,4):C.GC_1963,(0,2):C.GC_1962,(0,3):C.GC_1962,(0,0):C.GC_1856,(0,1):C.GC_1960})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1965,(0,2):C.GC_1964,(0,3):C.GC_1964,(0,0):C.GC_1857,(0,1):C.GC_1961})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2410,(0,4):C.GC_2523,(0,2):C.GC_2522,(0,3):C.GC_2522,(0,0):C.GC_2518,(0,1):C.GC_2520})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2525,(0,2):C.GC_2524,(0,3):C.GC_2524,(0,0):C.GC_2519,(0,1):C.GC_2521})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3024,(0,4):C.GC_3164,(0,2):C.GC_3163,(0,3):C.GC_3163,(0,0):C.GC_3083,(0,1):C.GC_3161})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3166,(0,2):C.GC_3165,(0,3):C.GC_3165,(0,0):C.GC_3084,(0,1):C.GC_3162})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1798,(0,4):C.GC_1969,(0,2):C.GC_1968,(0,3):C.GC_1968,(0,0):C.GC_1858,(0,1):C.GC_1966})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1971,(0,2):C.GC_1970,(0,3):C.GC_1970,(0,0):C.GC_1859,(0,1):C.GC_1967})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2410,(0,4):C.GC_2531,(0,2):C.GC_2530,(0,3):C.GC_2530,(0,0):C.GC_2526,(0,1):C.GC_2528})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2533,(0,2):C.GC_2532,(0,3):C.GC_2532,(0,0):C.GC_2527,(0,1):C.GC_2529})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3024,(0,4):C.GC_3170,(0,2):C.GC_3169,(0,3):C.GC_3169,(0,0):C.GC_3085,(0,1):C.GC_3167})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3172,(0,2):C.GC_3171,(0,3):C.GC_3171,(0,0):C.GC_3086,(0,1):C.GC_3168})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1798,(0,4):C.GC_1999,(0,2):C.GC_1998,(0,3):C.GC_1998,(0,0):C.GC_1884,(0,1):C.GC_1996})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2001,(0,2):C.GC_2000,(0,3):C.GC_2000,(0,0):C.GC_1885,(0,1):C.GC_1997})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2410,(0,4):C.GC_2587,(0,2):C.GC_2586,(0,3):C.GC_2586,(0,0):C.GC_2582,(0,1):C.GC_2584})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2589,(0,2):C.GC_2588,(0,3):C.GC_2588,(0,0):C.GC_2583,(0,1):C.GC_2585})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3024,(0,4):C.GC_3202,(0,2):C.GC_3201,(0,3):C.GC_3201,(0,0):C.GC_3197,(0,1):C.GC_3199})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3204,(0,2):C.GC_3203,(0,3):C.GC_3203,(0,0):C.GC_3198,(0,1):C.GC_3200})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_31,(0,0):C.GC_27})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_32})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.a, P.a, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_278})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.g, P.g, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
                couplings = {(0,0):C.GC_279,(0,2):C.GC_292,(0,1):C.GC_288,(0,3):C.GC_283})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.a, P.Z, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_282})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.a, P.Z1, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_282})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.a, P.Z1, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_296})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.g, P.g, P.g, P.H1 ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVVS10, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
                couplings = {(0,3):C.GC_284,(0,0):C.GC_293,(0,4):C.GC_289,(0,2):C.GC_286,(0,1):C.GC_280})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.g, P.g, P.g, P.g, P.H1 ],
                color = [ 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)' ],
                lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS18, L.VVVVS2, L.VVVVS20, L.VVVVS3, L.VVVVS5, L.VVVVS7, L.VVVVS8 ],
                couplings = {(2,5):C.GC_285,(2,8):C.GC_294,(1,4):C.GC_285,(1,10):C.GC_294,(2,6):C.GC_291,(0,11):C.GC_287,(0,12):C.GC_295,(1,7):C.GC_291,(0,3):C.GC_290,(1,2):C.GC_287,(2,1):C.GC_287,(0,9):C.GC_285,(1,13):C.GC_281,(0,0):C.GC_281,(2,14):C.GC_281})

