# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Wed 6 Jan 2021 14:20:52


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
             couplings = {(0,1):C.GC_340,(0,0):C.GC_418,(0,5):C.GC_207,(0,4):C.GC_206,(0,2):C.GC_3,(0,3):C.GC_417})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_334})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_343})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_355})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV7, L.VVV9 ],
             couplings = {(0,1):C.GC_419,(0,0):C.GC_339,(0,5):C.GC_61,(0,4):C.GC_60,(0,3):C.GC_137,(0,2):C.GC_337})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_413})

V_7 = Vertex(name = 'V_7',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_414})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_420})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV3, L.VVV5, L.VVV7, L.VVV8 ],
             couplings = {(0,0):C.GC_347,(0,3):C.GC_16,(0,2):C.GC_15,(0,1):C.GC_7})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
              couplings = {(0,7):C.GC_72,(1,6):C.GC_72,(2,5):C.GC_72,(0,4):C.GC_71,(1,3):C.GC_71,(2,2):C.GC_71,(1,8):C.GC_8,(0,0):C.GC_8,(2,1):C.GC_8})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV2, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV25, L.VVVVV28, L.VVVVV29, L.VVVVV3, L.VVVVV30, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV37, L.VVVVV4, L.VVVVV40, L.VVVVV41, L.VVVVV42, L.VVVVV43, L.VVVVV44, L.VVVVV46, L.VVVVV47, L.VVVVV48, L.VVVVV49, L.VVVVV5, L.VVVVV50, L.VVVVV51, L.VVVVV53, L.VVVVV54, L.VVVVV6, L.VVVVV7, L.VVVVV9 ],
              couplings = {(27,37):C.GC_77,(24,8):C.GC_78,(21,12):C.GC_77,(18,11):C.GC_78,(15,9):C.GC_77,(12,27):C.GC_77,(28,42):C.GC_77,(25,15):C.GC_78,(22,14):C.GC_77,(9,16):C.GC_77,(6,13):C.GC_78,(3,43):C.GC_78,(29,0):C.GC_78,(19,20):C.GC_77,(16,18):C.GC_78,(10,17):C.GC_77,(7,21):C.GC_78,(0,44):C.GC_77,(26,10):C.GC_77,(20,1):C.GC_78,(13,24):C.GC_77,(11,2):C.GC_78,(4,22):C.GC_77,(1,23):C.GC_77,(23,19):C.GC_78,(17,4):C.GC_77,(14,25):C.GC_78,(8,3):C.GC_77,(5,28):C.GC_78,(2,26):C.GC_78,(24,29):C.GC_76,(21,30):C.GC_75,(18,30):C.GC_76,(15,29):C.GC_75,(28,6):C.GC_76,(22,34):C.GC_76,(9,34):C.GC_75,(3,6):C.GC_75,(29,7):C.GC_76,(16,35):C.GC_76,(10,35):C.GC_75,(0,7):C.GC_75,(26,39):C.GC_75,(20,38):C.GC_75,(4,38):C.GC_76,(1,39):C.GC_76,(25,33):C.GC_76,(6,33):C.GC_75,(19,36):C.GC_76,(7,36):C.GC_75,(23,41):C.GC_75,(17,40):C.GC_75,(5,40):C.GC_76,(2,41):C.GC_76,(27,5):C.GC_76,(12,5):C.GC_75,(13,31):C.GC_76,(11,31):C.GC_75,(14,32):C.GC_75,(8,32):C.GC_76})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV19, L.VVVVVV2, L.VVVVVV20, L.VVVVVV21, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV26, L.VVVVVV27, L.VVVVVV28, L.VVVVVV29, L.VVVVVV3, L.VVVVVV30, L.VVVVVV31, L.VVVVVV32, L.VVVVVV33, L.VVVVVV34, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV38, L.VVVVVV39, L.VVVVVV4, L.VVVVVV40, L.VVVVVV41, L.VVVVVV42, L.VVVVVV43, L.VVVVVV44, L.VVVVVV45, L.VVVVVV46, L.VVVVVV47, L.VVVVVV48, L.VVVVVV49, L.VVVVVV5, L.VVVVVV50, L.VVVVVV51, L.VVVVVV52, L.VVVVVV54, L.VVVVVV55, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV59, L.VVVVVV6, L.VVVVVV60, L.VVVVVV61, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
              couplings = {(41,58):C.GC_83,(47,59):C.GC_82,(53,7):C.GC_83,(35,57):C.GC_82,(46,14):C.GC_83,(52,17):C.GC_82,(34,2):C.GC_83,(40,10):C.GC_82,(51,37):C.GC_83,(33,4):C.GC_82,(39,21):C.GC_83,(45,30):C.GC_82,(17,57):C.GC_83,(23,2):C.GC_82,(29,4):C.GC_83,(11,58):C.GC_82,(22,10):C.GC_83,(28,21):C.GC_82,(10,59):C.GC_83,(16,14):C.GC_82,(27,30):C.GC_83,(9,7):C.GC_82,(15,17):C.GC_83,(21,37):C.GC_82,(59,0):C.GC_83,(65,11):C.GC_82,(71,44):C.GC_83,(64,12):C.GC_83,(70,23):C.GC_82,(58,16):C.GC_82,(69,31):C.GC_83,(57,19):C.GC_83,(63,39):C.GC_82,(5,0):C.GC_82,(20,16):C.GC_83,(26,19):C.GC_82,(4,11):C.GC_83,(14,12):C.GC_82,(25,39):C.GC_83,(3,44):C.GC_82,(13,23):C.GC_83,(19,31):C.GC_82,(77,22):C.GC_82,(83,33):C.GC_83,(76,1):C.GC_83,(82,8):C.GC_82,(81,40):C.GC_83,(75,35):C.GC_82,(2,22):C.GC_83,(8,1):C.GC_82,(24,35):C.GC_83,(1,33):C.GC_82,(7,8):C.GC_83,(18,40):C.GC_82,(89,54):C.GC_83,(88,6):C.GC_82,(87,25):C.GC_83,(0,54):C.GC_82,(6,6):C.GC_83,(12,25):C.GC_82,(62,15):C.GC_83,(68,18):C.GC_82,(56,13):C.GC_82,(67,38):C.GC_83,(55,24):C.GC_83,(61,32):C.GC_82,(44,13):C.GC_83,(50,24):C.GC_82,(38,15):C.GC_82,(49,32):C.GC_83,(37,18):C.GC_83,(43,38):C.GC_82,(74,3):C.GC_83,(80,5):C.GC_82,(79,34):C.GC_83,(73,42):C.GC_82,(32,3):C.GC_82,(48,42):C.GC_83,(31,5):C.GC_83,(42,34):C.GC_82,(86,9):C.GC_82,(85,20):C.GC_83,(30,9):C.GC_83,(36,20):C.GC_82,(78,41):C.GC_83,(72,36):C.GC_82,(66,36):C.GC_83,(60,41):C.GC_82,(65,43):C.GC_80,(71,46):C.GC_81,(77,46):C.GC_80,(83,43):C.GC_81,(41,28):C.GC_80,(53,50):C.GC_80,(76,50):C.GC_81,(88,28):C.GC_81,(35,29):C.GC_80,(52,53):C.GC_80,(64,53):C.GC_81,(87,29):C.GC_81,(34,52):C.GC_81,(40,51):C.GC_81,(69,51):C.GC_80,(81,52):C.GC_80,(17,29):C.GC_81,(23,52):C.GC_80,(80,52):C.GC_81,(86,29):C.GC_80,(11,28):C.GC_81,(22,51):C.GC_80,(68,51):C.GC_81,(85,28):C.GC_80,(9,50):C.GC_81,(15,53):C.GC_81,(61,53):C.GC_80,(73,50):C.GC_80,(4,43):C.GC_81,(14,53):C.GC_80,(49,53):C.GC_81,(78,43):C.GC_80,(3,46):C.GC_80,(19,51):C.GC_81,(37,51):C.GC_80,(72,46):C.GC_81,(2,46):C.GC_81,(8,50):C.GC_80,(48,50):C.GC_81,(66,46):C.GC_80,(1,43):C.GC_80,(18,52):C.GC_81,(31,52):C.GC_80,(60,43):C.GC_81,(6,28):C.GC_80,(12,29):C.GC_80,(30,29):C.GC_81,(36,28):C.GC_81,(47,48):C.GC_80,(82,48):C.GC_81,(46,55):C.GC_80,(70,55):C.GC_81,(33,56):C.GC_81,(39,49):C.GC_81,(63,49):C.GC_80,(75,56):C.GC_80,(29,56):C.GC_80,(74,56):C.GC_81,(28,49):C.GC_80,(62,49):C.GC_81,(10,48):C.GC_81,(16,55):C.GC_81,(67,55):C.GC_80,(79,48):C.GC_80,(25,49):C.GC_81,(38,49):C.GC_80,(13,55):C.GC_80,(43,55):C.GC_81,(24,56):C.GC_81,(32,56):C.GC_80,(7,48):C.GC_80,(42,48):C.GC_81,(84,26):C.GC_83,(54,26):C.GC_82,(59,27):C.GC_80,(89,27):C.GC_81,(51,45):C.GC_80,(58,45):C.GC_81,(21,45):C.GC_81,(55,45):C.GC_80,(5,27):C.GC_81,(20,45):C.GC_80,(50,45):C.GC_81,(84,27):C.GC_80,(0,27):C.GC_80,(54,27):C.GC_81,(45,47):C.GC_81,(57,47):C.GC_80,(27,47):C.GC_80,(56,47):C.GC_81,(26,47):C.GC_81,(44,47):C.GC_80})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_209,(0,0):C.GC_208,(0,2):C.GC_5})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_345})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_346})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_366})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_422})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
              couplings = {(0,2):C.GC_67,(0,1):C.GC_66,(0,0):C.GC_138})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_449})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_450})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_421})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_424})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV16, L.VVVVV8 ],
              couplings = {(0,1):C.GC_211,(0,0):C.GC_210})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_164,(0,0):C.GC_162,(0,2):C.GC_98})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_359})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_361})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV26, L.VVVVV55 ],
              couplings = {(0,0):C.GC_70,(0,1):C.GC_69})

V_28 = Vertex(name = 'V_28',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV32, L.VVVVV57 ],
              couplings = {(0,0):C.GC_169,(0,1):C.GC_167})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_171})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_165,(0,0):C.GC_163,(0,2):C.GC_100})

V_31 = Vertex(name = 'V_31',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_367})

V_32 = Vertex(name = 'V_32',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_368})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_369})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_423})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV38, L.VVVVV45 ],
              couplings = {(0,0):C.GC_170,(0,1):C.GC_168})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV27, L.VVVVV52 ],
              couplings = {(0,0):C.GC_106,(0,1):C.GC_104})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV62 ],
              couplings = {(0,0):C.GC_108})

V_38 = Vertex(name = 'V_38',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_96})

V_39 = Vertex(name = 'V_39',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV39, L.VVVVV56 ],
              couplings = {(0,0):C.GC_107,(0,1):C.GC_105})

V_40 = Vertex(name = 'V_40',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_53,(0,1):C.GC_52})

V_41 = Vertex(name = 'V_41',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_204,(0,1):C.GC_201})

V_42 = Vertex(name = 'V_42',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_220,(0,1):C.GC_219})

V_43 = Vertex(name = 'V_43',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_269,(0,1):C.GC_223})

V_44 = Vertex(name = 'V_44',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_324,(0,1):C.GC_268})

V_45 = Vertex(name = 'V_45',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_329,(0,1):C.GC_321})

V_46 = Vertex(name = 'V_46',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_328})

V_47 = Vertex(name = 'V_47',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_20})

V_48 = Vertex(name = 'V_48',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
              couplings = {(0,0):C.GC_265,(0,1):C.GC_224,(0,3):C.GC_237,(0,2):C.GC_233,(0,4):C.GC_228})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_264})

V_50 = Vertex(name = 'V_50',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_23,(0,2):C.GC_22,(0,1):C.GC_97})

V_51 = Vertex(name = 'V_51',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_356})

V_52 = Vertex(name = 'V_52',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_357})

V_53 = Vertex(name = 'V_53',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_358})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_360})

V_55 = Vertex(name = 'V_55',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_267,(0,2):C.GC_266,(0,1):C.GC_283})

V_56 = Vertex(name = 'V_56',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_439})

V_57 = Vertex(name = 'V_57',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_440})

V_58 = Vertex(name = 'V_58',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_441})

V_59 = Vertex(name = 'V_59',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_442})

V_60 = Vertex(name = 'V_60',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_222,(0,1):C.GC_221})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_199,(0,1):C.GC_198})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_205,(0,1):C.GC_200})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_448,(0,1):C.GC_227})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_319,(0,1):C.GC_447})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_325,(0,1):C.GC_318})

V_66 = Vertex(name = 'V_66',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_320})

V_67 = Vertex(name = 'V_67',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_55,(0,2):C.GC_54,(0,1):C.GC_99})

V_68 = Vertex(name = 'V_68',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_203,(0,2):C.GC_202,(0,1):C.GC_362})

V_69 = Vertex(name = 'V_69',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_218,(0,2):C.GC_217,(0,1):C.GC_363})

V_70 = Vertex(name = 'V_70',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_364})

V_71 = Vertex(name = 'V_71',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_365})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_271,(0,2):C.GC_270,(0,1):C.GC_284})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_323,(0,2):C.GC_322,(0,1):C.GC_443})

V_74 = Vertex(name = 'V_74',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_327,(0,2):C.GC_326,(0,1):C.GC_444})

V_75 = Vertex(name = 'V_75',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_445})

V_76 = Vertex(name = 'V_76',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_446})

V_77 = Vertex(name = 'V_77',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3, L.VVVSS6 ],
              couplings = {(0,0):C.GC_74,(0,1):C.GC_73})

V_78 = Vertex(name = 'V_78',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS10, L.VVVS3, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
              couplings = {(0,1):C.GC_278,(0,4):C.GC_229,(0,0):C.GC_238,(0,5):C.GC_234,(0,3):C.GC_231,(0,2):C.GC_225})

V_79 = Vertex(name = 'V_79',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS6 ],
              couplings = {(0,0):C.GC_277})

V_80 = Vertex(name = 'V_80',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3, L.VVVSS4, L.VVVSS6 ],
              couplings = {(0,1):C.GC_65,(0,0):C.GC_160,(0,3):C.GC_62,(0,2):C.GC_159})

V_81 = Vertex(name = 'V_81',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
              couplings = {(0,1):C.GC_275,(0,0):C.GC_315,(0,3):C.GC_272,(0,2):C.GC_314})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2, L.VVVSS3, L.VVVSS5, L.VVVSS6 ],
              couplings = {(0,1):C.GC_161,(0,0):C.GC_64,(0,3):C.GC_158,(0,2):C.GC_63})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
              couplings = {(0,1):C.GC_316,(0,0):C.GC_274,(0,3):C.GC_313,(0,2):C.GC_273})

V_84 = Vertex(name = 'V_84',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_9,(0,2):C.GC_18,(0,1):C.GC_19})

V_85 = Vertex(name = 'V_85',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_330})

V_86 = Vertex(name = 'V_86',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_348})

V_87 = Vertex(name = 'V_87',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_349})

V_88 = Vertex(name = 'V_88',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_350})

V_89 = Vertex(name = 'V_89',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_351})

V_90 = Vertex(name = 'V_90',
              particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_17})

V_91 = Vertex(name = 'V_91',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_260,(0,2):C.GC_262,(0,1):C.GC_263})

V_92 = Vertex(name = 'V_92',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_434})

V_93 = Vertex(name = 'V_93',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_435})

V_94 = Vertex(name = 'V_94',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_436})

V_95 = Vertex(name = 'V_95',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_437})

V_96 = Vertex(name = 'V_96',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_438})

V_97 = Vertex(name = 'V_97',
              particles = [ P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_261})

V_98 = Vertex(name = 'V_98',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_79,(0,0):C.GC_79,(2,2):C.GC_79})

V_99 = Vertex(name = 'V_99',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS17, L.VVVVS19, L.VVVVS2, L.VVVVS3, L.VVVVS4, L.VVVVS7, L.VVVVS8 ],
              couplings = {(2,5):C.GC_230,(2,8):C.GC_239,(1,4):C.GC_230,(1,9):C.GC_239,(2,6):C.GC_236,(0,11):C.GC_232,(0,12):C.GC_240,(1,7):C.GC_236,(0,3):C.GC_235,(1,2):C.GC_232,(2,1):C.GC_232,(0,10):C.GC_230,(1,13):C.GC_226,(0,0):C.GC_226,(2,14):C.GC_226})

V_100 = Vertex(name = 'V_100',
               particles = [ P.g, P.g, P.g, P.g, P.H ],
               color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVS1, L.VVVVS7, L.VVVVS8 ],
               couplings = {(1,1):C.GC_279,(0,0):C.GC_279,(2,2):C.GC_279})

V_101 = Vertex(name = 'V_101',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_68})

V_102 = Vertex(name = 'V_102',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_276})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_101})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_285})

V_105 = Vertex(name = 'V_105',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_166})

V_106 = Vertex(name = 'V_106',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS9 ],
               couplings = {(0,0):C.GC_317})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_102})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_286})

V_109 = Vertex(name = 'V_109',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_103})

V_110 = Vertex(name = 'V_110',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_287})

V_111 = Vertex(name = 'V_111',
               particles = [ P.H, P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_88})

V_112 = Vertex(name = 'V_112',
               particles = [ P.H, P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_93})

V_113 = Vertex(name = 'V_113',
               particles = [ P.H, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_94})

V_114 = Vertex(name = 'V_114',
               particles = [ P.H1, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_95})

V_115 = Vertex(name = 'V_115',
               particles = [ P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_280})

V_116 = Vertex(name = 'V_116',
               particles = [ P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_281})

V_117 = Vertex(name = 'V_117',
               particles = [ P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_282})

V_118 = Vertex(name = 'V_118',
               particles = [ P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_85})

V_119 = Vertex(name = 'V_119',
               particles = [ P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_90})

V_120 = Vertex(name = 'V_120',
               particles = [ P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_85})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_109})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_113})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_288})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_290})

V_126 = Vertex(name = 'V_126',
               particles = [ P.a, P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_86})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_184})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_190})

V_129 = Vertex(name = 'V_129',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_113})

V_130 = Vertex(name = 'V_130',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_121})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W1__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_290})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_292})

V_134 = Vertex(name = 'V_134',
               particles = [ P.a, P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_91})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_190})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_193})

V_137 = Vertex(name = 'V_137',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_114})

V_138 = Vertex(name = 'V_138',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_118})

V_139 = Vertex(name = 'V_139',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_122})

V_140 = Vertex(name = 'V_140',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_109})

V_141 = Vertex(name = 'V_141',
               particles = [ P.W__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_113})

V_142 = Vertex(name = 'V_142',
               particles = [ P.W__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_288})

V_143 = Vertex(name = 'V_143',
               particles = [ P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_184})

V_144 = Vertex(name = 'V_144',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_109})

V_145 = Vertex(name = 'V_145',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_113})

V_146 = Vertex(name = 'V_146',
               particles = [ P.W1__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_117})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W1__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_288})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W1__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_290})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_86})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_184})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_190})

V_152 = Vertex(name = 'V_152',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_110})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_114})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_118})

V_155 = Vertex(name = 'V_155',
               particles = [ P.W__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_110})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W1__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_114})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_185})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_191})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_185})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Z, P.Z, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_111})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Z, P.Z, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_115})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Z, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_289})

V_163 = Vertex(name = 'V_163',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_112})

V_164 = Vertex(name = 'V_164',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_116})

V_165 = Vertex(name = 'V_165',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_112})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_191})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_194})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_185})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_191})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Z, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_111})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Z, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_115})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Z, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_119})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_289})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_291})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_116})

V_176 = Vertex(name = 'V_176',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_112})

V_178 = Vertex(name = 'V_178',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_116})

V_179 = Vertex(name = 'V_179',
               particles = [ P.Z1, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_115})

V_180 = Vertex(name = 'V_180',
               particles = [ P.Z1, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_119})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Z1, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_123})

V_182 = Vertex(name = 'V_182',
               particles = [ P.Z1, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_291})

V_183 = Vertex(name = 'V_183',
               particles = [ P.Z1, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_293})

V_184 = Vertex(name = 'V_184',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_185 = Vertex(name = 'V_185',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_124})

V_186 = Vertex(name = 'V_186',
               particles = [ P.W__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_116})

V_187 = Vertex(name = 'V_187',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_120})

V_188 = Vertex(name = 'V_188',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_690,(0,1):C.GC_689})

V_189 = Vertex(name = 'V_189',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_333,(0,2):C.GC_704,(0,1):C.GC_703})

V_190 = Vertex(name = 'V_190',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_344})

V_191 = Vertex(name = 'V_191',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_354})

V_192 = Vertex(name = 'V_192',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_417})

V_193 = Vertex(name = 'V_193',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_785,(0,1):C.GC_784})

V_194 = Vertex(name = 'V_194',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_333,(0,2):C.GC_799,(0,1):C.GC_798})

V_195 = Vertex(name = 'V_195',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_344})

V_196 = Vertex(name = 'V_196',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_354})

V_197 = Vertex(name = 'V_197',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_417})

V_198 = Vertex(name = 'V_198',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_1142,(0,1):C.GC_1141})

V_199 = Vertex(name = 'V_199',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_333,(0,2):C.GC_1156,(0,1):C.GC_1155})

V_200 = Vertex(name = 'V_200',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_344})

V_201 = Vertex(name = 'V_201',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_354})

V_202 = Vertex(name = 'V_202',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_417})

V_203 = Vertex(name = 'V_203',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_197,(0,2):C.GC_136,(0,4):C.GC_402,(0,3):C.GC_403,(0,5):C.GC_692,(0,1):C.GC_691})

V_204 = Vertex(name = 'V_204',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_338,(0,2):C.GC_404,(0,3):C.GC_702,(0,1):C.GC_701})

V_205 = Vertex(name = 'V_205',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_427,(0,1):C.GC_412})

V_206 = Vertex(name = 'V_206',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_430})

V_207 = Vertex(name = 'V_207',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_433})

V_208 = Vertex(name = 'V_208',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_197,(0,2):C.GC_136,(0,4):C.GC_402,(0,3):C.GC_403,(0,5):C.GC_787,(0,1):C.GC_786})

V_209 = Vertex(name = 'V_209',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_338,(0,2):C.GC_404,(0,3):C.GC_797,(0,1):C.GC_796})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_427,(0,1):C.GC_412})

V_211 = Vertex(name = 'V_211',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_430})

V_212 = Vertex(name = 'V_212',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_433})

V_213 = Vertex(name = 'V_213',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_197,(0,2):C.GC_136,(0,4):C.GC_402,(0,3):C.GC_403,(0,5):C.GC_1144,(0,1):C.GC_1143})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_338,(0,2):C.GC_404,(0,3):C.GC_1154,(0,1):C.GC_1153})

V_215 = Vertex(name = 'V_215',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_427,(0,1):C.GC_412})

V_216 = Vertex(name = 'V_216',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_430})

V_217 = Vertex(name = 'V_217',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_433})

V_218 = Vertex(name = 'V_218',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_620,(0,1):C.GC_619})

V_219 = Vertex(name = 'V_219',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_331,(0,2):C.GC_636,(0,1):C.GC_635})

V_220 = Vertex(name = 'V_220',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_341})

V_221 = Vertex(name = 'V_221',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_352})

V_222 = Vertex(name = 'V_222',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_415})

V_223 = Vertex(name = 'V_223',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_886,(0,1):C.GC_885})

V_224 = Vertex(name = 'V_224',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_331,(0,2):C.GC_902,(0,1):C.GC_901})

V_225 = Vertex(name = 'V_225',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_341})

V_226 = Vertex(name = 'V_226',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_352})

V_227 = Vertex(name = 'V_227',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_415})

V_228 = Vertex(name = 'V_228',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_486,(0,1):C.GC_485})

V_229 = Vertex(name = 'V_229',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_331,(0,2):C.GC_502,(0,1):C.GC_501})

V_230 = Vertex(name = 'V_230',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_341})

V_231 = Vertex(name = 'V_231',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_352})

V_232 = Vertex(name = 'V_232',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_415})

V_233 = Vertex(name = 'V_233',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_1272,(0,1):C.GC_1271})

V_234 = Vertex(name = 'V_234',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_332,(0,2):C.GC_1295,(0,1):C.GC_1294})

V_235 = Vertex(name = 'V_235',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_342})

V_236 = Vertex(name = 'V_236',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_237 = Vertex(name = 'V_237',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_416})

V_238 = Vertex(name = 'V_238',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_537,(0,1):C.GC_536})

V_239 = Vertex(name = 'V_239',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_332,(0,2):C.GC_560,(0,1):C.GC_559})

V_240 = Vertex(name = 'V_240',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_342})

V_241 = Vertex(name = 'V_241',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_242 = Vertex(name = 'V_242',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_416})

V_243 = Vertex(name = 'V_243',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_975,(0,1):C.GC_974})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_332,(0,2):C.GC_998,(0,1):C.GC_997})

V_245 = Vertex(name = 'V_245',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_342})

V_246 = Vertex(name = 'V_246',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_247 = Vertex(name = 'V_247',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_416})

V_248 = Vertex(name = 'V_248',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_613,(0,1):C.GC_612})

V_249 = Vertex(name = 'V_249',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_879,(0,1):C.GC_878})

V_250 = Vertex(name = 'V_250',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_479,(0,1):C.GC_478})

V_251 = Vertex(name = 'V_251',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_1274,(0,1):C.GC_1273})

V_252 = Vertex(name = 'V_252',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_539,(0,1):C.GC_538})

V_253 = Vertex(name = 'V_253',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_977,(0,1):C.GC_976})

V_254 = Vertex(name = 'V_254',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1278,(0,0):C.GC_616,(0,1):C.GC_126,(0,3):C.GC_1336})

V_255 = Vertex(name = 'V_255',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1280,(0,0):C.GC_618,(0,1):C.GC_370,(0,3):C.GC_1337})

V_256 = Vertex(name = 'V_256',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_371})

V_257 = Vertex(name = 'V_257',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_389})

V_258 = Vertex(name = 'V_258',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_127,(0,1):C.GC_1408})

V_259 = Vertex(name = 'V_259',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_1409})

V_260 = Vertex(name = 'V_260',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_373})

V_261 = Vertex(name = 'V_261',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_390})

V_262 = Vertex(name = 'V_262',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_1318})

V_263 = Vertex(name = 'V_263',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_1319})

V_264 = Vertex(name = 'V_264',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_375})

V_265 = Vertex(name = 'V_265',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_391})

V_266 = Vertex(name = 'V_266',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_129,(0,1):C.GC_659})

V_267 = Vertex(name = 'V_267',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_376,(0,1):C.GC_660})

V_268 = Vertex(name = 'V_268',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_377})

V_269 = Vertex(name = 'V_269',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_392})

V_270 = Vertex(name = 'V_270',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_543,(0,0):C.GC_882,(0,1):C.GC_130,(0,3):C.GC_925})

V_271 = Vertex(name = 'V_271',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_545,(0,0):C.GC_884,(0,1):C.GC_378,(0,3):C.GC_926})

V_272 = Vertex(name = 'V_272',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_379})

V_273 = Vertex(name = 'V_273',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_393})

V_274 = Vertex(name = 'V_274',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_131,(0,1):C.GC_583})

V_275 = Vertex(name = 'V_275',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_380,(0,1):C.GC_584})

V_276 = Vertex(name = 'V_276',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_381})

V_277 = Vertex(name = 'V_277',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_394})

V_278 = Vertex(name = 'V_278',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_1039})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_382,(0,1):C.GC_1040})

V_280 = Vertex(name = 'V_280',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_383})

V_281 = Vertex(name = 'V_281',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_395})

V_282 = Vertex(name = 'V_282',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_1111})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_384,(0,1):C.GC_1112})

V_284 = Vertex(name = 'V_284',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_385})

V_285 = Vertex(name = 'V_285',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_396})

V_286 = Vertex(name = 'V_286',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_981,(0,0):C.GC_482,(0,1):C.GC_134,(0,3):C.GC_1021})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_983,(0,0):C.GC_484,(0,1):C.GC_386,(0,3):C.GC_1022})

V_288 = Vertex(name = 'V_288',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_387})

V_289 = Vertex(name = 'V_289',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_397})

V_290 = Vertex(name = 'V_290',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1332,(0,0):C.GC_140})

V_291 = Vertex(name = 'V_291',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1333})

V_292 = Vertex(name = 'V_292',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1404,(0,0):C.GC_141})

V_293 = Vertex(name = 'V_293',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1405})

V_294 = Vertex(name = 'V_294',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1314,(0,0):C.GC_142})

V_295 = Vertex(name = 'V_295',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1315})

V_296 = Vertex(name = 'V_296',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_655,(0,0):C.GC_143})

V_297 = Vertex(name = 'V_297',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_656})

V_298 = Vertex(name = 'V_298',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_921,(0,0):C.GC_144})

V_299 = Vertex(name = 'V_299',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_922})

V_300 = Vertex(name = 'V_300',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_579,(0,0):C.GC_145})

V_301 = Vertex(name = 'V_301',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_580})

V_302 = Vertex(name = 'V_302',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1035,(0,0):C.GC_146})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1036})

V_304 = Vertex(name = 'V_304',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1107,(0,0):C.GC_147})

V_305 = Vertex(name = 'V_305',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1108})

V_306 = Vertex(name = 'V_306',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1017,(0,0):C.GC_148})

V_307 = Vertex(name = 'V_307',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1018})

V_308 = Vertex(name = 'V_308',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_1252,(0,3):C.GC_590,(0,2):C.GC_1334,(0,0):C.GC_295})

V_309 = Vertex(name = 'V_309',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_1254,(0,2):C.GC_592,(0,1):C.GC_1335})

V_310 = Vertex(name = 'V_310',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1406,(0,0):C.GC_296})

V_311 = Vertex(name = 'V_311',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1407})

V_312 = Vertex(name = 'V_312',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1316,(0,0):C.GC_297})

V_313 = Vertex(name = 'V_313',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1317})

V_314 = Vertex(name = 'V_314',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_657,(0,0):C.GC_298})

V_315 = Vertex(name = 'V_315',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_658})

V_316 = Vertex(name = 'V_316',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_517,(0,3):C.GC_856,(0,2):C.GC_923,(0,0):C.GC_299})

V_317 = Vertex(name = 'V_317',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_519,(0,2):C.GC_858,(0,1):C.GC_924})

V_318 = Vertex(name = 'V_318',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_581,(0,0):C.GC_300})

V_319 = Vertex(name = 'V_319',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_582})

V_320 = Vertex(name = 'V_320',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1037,(0,0):C.GC_301})

V_321 = Vertex(name = 'V_321',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1038})

V_322 = Vertex(name = 'V_322',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1109,(0,0):C.GC_302})

V_323 = Vertex(name = 'V_323',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1110})

V_324 = Vertex(name = 'V_324',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_953,(0,3):C.GC_456,(0,2):C.GC_1019,(0,0):C.GC_303})

V_325 = Vertex(name = 'V_325',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_955,(0,2):C.GC_458,(0,1):C.GC_1020})

V_326 = Vertex(name = 'V_326',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_686,(0,1):C.GC_125})

V_327 = Vertex(name = 'V_327',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_688,(0,1):C.GC_388})

V_328 = Vertex(name = 'V_328',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_781,(0,1):C.GC_125})

V_329 = Vertex(name = 'V_329',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_783,(0,1):C.GC_388})

V_330 = Vertex(name = 'V_330',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_1138,(0,1):C.GC_125})

V_331 = Vertex(name = 'V_331',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_1140,(0,1):C.GC_388})

V_332 = Vertex(name = 'V_332',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_333 = Vertex(name = 'V_333',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_334 = Vertex(name = 'V_334',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_335 = Vertex(name = 'V_335',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6, L.FFVS7 ],
               couplings = {(0,2):C.GC_666,(0,1):C.GC_664,(0,0):C.GC_294})

V_336 = Vertex(name = 'V_336',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_759,(0,0):C.GC_294})

V_337 = Vertex(name = 'V_337',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_761})

V_338 = Vertex(name = 'V_338',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_1116,(0,0):C.GC_294})

V_339 = Vertex(name = 'V_339',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS6 ],
               couplings = {(0,0):C.GC_1118})

V_340 = Vertex(name = 'V_340',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_617,(0,0):C.GC_1277,(0,1):C.GC_1465,(0,3):C.GC_1598})

V_341 = Vertex(name = 'V_341',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_618,(0,0):C.GC_1280,(0,1):C.GC_1469,(0,3):C.GC_1599})

V_342 = Vertex(name = 'V_342',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1470})

V_343 = Vertex(name = 'V_343',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1471})

V_344 = Vertex(name = 'V_344',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2080,(0,1):C.GC_2159})

V_345 = Vertex(name = 'V_345',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2084,(0,1):C.GC_2160})

V_346 = Vertex(name = 'V_346',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2085})

V_347 = Vertex(name = 'V_347',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2086})

V_348 = Vertex(name = 'V_348',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2695,(0,1):C.GC_2803})

V_349 = Vertex(name = 'V_349',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2700,(0,1):C.GC_2804})

V_350 = Vertex(name = 'V_350',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2701})

V_351 = Vertex(name = 'V_351',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2702})

V_352 = Vertex(name = 'V_352',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1670,(0,1):C.GC_1839})

V_353 = Vertex(name = 'V_353',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1674,(0,1):C.GC_1840})

V_354 = Vertex(name = 'V_354',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1675})

V_355 = Vertex(name = 'V_355',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1676})

V_356 = Vertex(name = 'V_356',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_883,(0,0):C.GC_542,(0,1):C.GC_2285,(0,3):C.GC_2400})

V_357 = Vertex(name = 'V_357',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_884,(0,0):C.GC_545,(0,1):C.GC_2289,(0,3):C.GC_2401})

V_358 = Vertex(name = 'V_358',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2290})

V_359 = Vertex(name = 'V_359',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2291})

V_360 = Vertex(name = 'V_360',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2901,(0,1):C.GC_3045})

V_361 = Vertex(name = 'V_361',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2906,(0,1):C.GC_3046})

V_362 = Vertex(name = 'V_362',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2907})

V_363 = Vertex(name = 'V_363',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2908})

V_364 = Vertex(name = 'V_364',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1875,(0,1):C.GC_1984})

V_365 = Vertex(name = 'V_365',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_1879,(0,1):C.GC_1985})

V_366 = Vertex(name = 'V_366',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1880})

V_367 = Vertex(name = 'V_367',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1881})

V_368 = Vertex(name = 'V_368',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2490,(0,1):C.GC_2545})

V_369 = Vertex(name = 'V_369',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_2494,(0,1):C.GC_2546})

V_370 = Vertex(name = 'V_370',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2495})

V_371 = Vertex(name = 'V_371',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2496})

V_372 = Vertex(name = 'V_372',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_483,(0,0):C.GC_980,(0,1):C.GC_3107,(0,3):C.GC_3191})

V_373 = Vertex(name = 'V_373',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_484,(0,0):C.GC_983,(0,1):C.GC_3112,(0,3):C.GC_3192})

V_374 = Vertex(name = 'V_374',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3113})

V_375 = Vertex(name = 'V_375',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3114})

V_376 = Vertex(name = 'V_376',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1594,(0,0):C.GC_1466})

V_377 = Vertex(name = 'V_377',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1595})

V_378 = Vertex(name = 'V_378',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2155,(0,0):C.GC_2081})

V_379 = Vertex(name = 'V_379',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2156})

V_380 = Vertex(name = 'V_380',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2799,(0,0):C.GC_2696})

V_381 = Vertex(name = 'V_381',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2800})

V_382 = Vertex(name = 'V_382',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1835,(0,0):C.GC_1671})

V_383 = Vertex(name = 'V_383',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1836})

V_384 = Vertex(name = 'V_384',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2396,(0,0):C.GC_2286})

V_385 = Vertex(name = 'V_385',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2397})

V_386 = Vertex(name = 'V_386',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3041,(0,0):C.GC_2902})

V_387 = Vertex(name = 'V_387',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_3042})

V_388 = Vertex(name = 'V_388',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1980,(0,0):C.GC_1876})

V_389 = Vertex(name = 'V_389',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1981})

V_390 = Vertex(name = 'V_390',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2541,(0,0):C.GC_2491})

V_391 = Vertex(name = 'V_391',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_2542})

V_392 = Vertex(name = 'V_392',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3187,(0,0):C.GC_3108})

V_393 = Vertex(name = 'V_393',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_3188})

V_394 = Vertex(name = 'V_394',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_591,(0,3):C.GC_1251,(0,2):C.GC_1596,(0,0):C.GC_1468})

V_395 = Vertex(name = 'V_395',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_592,(0,2):C.GC_1254,(0,1):C.GC_1597})

V_396 = Vertex(name = 'V_396',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2157,(0,0):C.GC_2083})

V_397 = Vertex(name = 'V_397',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2158})

V_398 = Vertex(name = 'V_398',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2801,(0,0):C.GC_2699})

V_399 = Vertex(name = 'V_399',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2802})

V_400 = Vertex(name = 'V_400',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1837,(0,0):C.GC_1673})

V_401 = Vertex(name = 'V_401',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1838})

V_402 = Vertex(name = 'V_402',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_857,(0,3):C.GC_516,(0,2):C.GC_2398,(0,0):C.GC_2288})

V_403 = Vertex(name = 'V_403',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_858,(0,2):C.GC_519,(0,1):C.GC_2399})

V_404 = Vertex(name = 'V_404',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_3043,(0,0):C.GC_2905})

V_405 = Vertex(name = 'V_405',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3044})

V_406 = Vertex(name = 'V_406',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_1982,(0,0):C.GC_1878})

V_407 = Vertex(name = 'V_407',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_1983})

V_408 = Vertex(name = 'V_408',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,1):C.GC_2543,(0,0):C.GC_2493})

V_409 = Vertex(name = 'V_409',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2544})

V_410 = Vertex(name = 'V_410',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,1):C.GC_457,(0,3):C.GC_952,(0,2):C.GC_3189,(0,0):C.GC_3111})

V_411 = Vertex(name = 'V_411',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6 ],
               couplings = {(0,0):C.GC_458,(0,2):C.GC_955,(0,1):C.GC_3190})

V_412 = Vertex(name = 'V_412',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_687,(0,0):C.GC_125})

V_413 = Vertex(name = 'V_413',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_688,(0,0):C.GC_388})

V_414 = Vertex(name = 'V_414',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_782,(0,0):C.GC_125})

V_415 = Vertex(name = 'V_415',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_783,(0,0):C.GC_388})

V_416 = Vertex(name = 'V_416',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_1139,(0,0):C.GC_125})

V_417 = Vertex(name = 'V_417',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_1140,(0,0):C.GC_388})

V_418 = Vertex(name = 'V_418',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_419 = Vertex(name = 'V_419',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_420 = Vertex(name = 'V_420',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_139})

V_421 = Vertex(name = 'V_421',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_665,(0,0):C.GC_294})

V_422 = Vertex(name = 'V_422',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_666})

V_423 = Vertex(name = 'V_423',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_760,(0,0):C.GC_294})

V_424 = Vertex(name = 'V_424',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_761})

V_425 = Vertex(name = 'V_425',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS3 ],
               couplings = {(0,1):C.GC_1117,(0,0):C.GC_294})

V_426 = Vertex(name = 'V_426',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_1118})

V_427 = Vertex(name = 'V_427',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_149})

V_428 = Vertex(name = 'V_428',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_156})

V_429 = Vertex(name = 'V_429',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_149})

V_430 = Vertex(name = 'V_430',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_156})

V_431 = Vertex(name = 'V_431',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_149})

V_432 = Vertex(name = 'V_432',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_156})

V_433 = Vertex(name = 'V_433',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_304,(0,3):C.GC_596,(0,0):C.GC_595})

V_434 = Vertex(name = 'V_434',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_311,(0,2):C.GC_609,(0,0):C.GC_608})

V_435 = Vertex(name = 'V_435',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_304,(0,3):C.GC_862,(0,0):C.GC_861})

V_436 = Vertex(name = 'V_436',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_311,(0,2):C.GC_875,(0,0):C.GC_874})

V_437 = Vertex(name = 'V_437',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_304,(0,3):C.GC_462,(0,0):C.GC_461})

V_438 = Vertex(name = 'V_438',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_311,(0,2):C.GC_475,(0,0):C.GC_474})

V_439 = Vertex(name = 'V_439',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_195,(0,2):C.GC_136,(0,4):C.GC_399,(0,3):C.GC_398,(0,5):C.GC_622,(0,1):C.GC_621})

V_440 = Vertex(name = 'V_440',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_335,(0,2):C.GC_405,(0,3):C.GC_634,(0,1):C.GC_633})

V_441 = Vertex(name = 'V_441',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_425,(0,1):C.GC_407})

V_442 = Vertex(name = 'V_442',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_428,(0,1):C.GC_409})

V_443 = Vertex(name = 'V_443',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_412})

V_444 = Vertex(name = 'V_444',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_195,(0,2):C.GC_136,(0,4):C.GC_399,(0,3):C.GC_398,(0,5):C.GC_888,(0,1):C.GC_887})

V_445 = Vertex(name = 'V_445',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_335,(0,2):C.GC_405,(0,3):C.GC_900,(0,1):C.GC_899})

V_446 = Vertex(name = 'V_446',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_425,(0,1):C.GC_407})

V_447 = Vertex(name = 'V_447',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_428,(0,1):C.GC_409})

V_448 = Vertex(name = 'V_448',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_412})

V_449 = Vertex(name = 'V_449',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_195,(0,2):C.GC_136,(0,4):C.GC_399,(0,3):C.GC_398,(0,5):C.GC_488,(0,1):C.GC_487})

V_450 = Vertex(name = 'V_450',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_335,(0,2):C.GC_405,(0,3):C.GC_500,(0,1):C.GC_499})

V_451 = Vertex(name = 'V_451',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_425,(0,1):C.GC_407})

V_452 = Vertex(name = 'V_452',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_428,(0,1):C.GC_409})

V_453 = Vertex(name = 'V_453',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_431,(0,1):C.GC_412})

V_454 = Vertex(name = 'V_454',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_150})

V_455 = Vertex(name = 'V_455',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_153})

V_456 = Vertex(name = 'V_456',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_150})

V_457 = Vertex(name = 'V_457',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_153})

V_458 = Vertex(name = 'V_458',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_151,(0,1):C.GC_150})

V_459 = Vertex(name = 'V_459',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_153})

V_460 = Vertex(name = 'V_460',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_306,(0,2):C.GC_305,(0,3):C.GC_670,(0,0):C.GC_669})

V_461 = Vertex(name = 'V_461',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_308,(0,2):C.GC_681,(0,0):C.GC_680})

V_462 = Vertex(name = 'V_462',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_306,(0,2):C.GC_305,(0,3):C.GC_765,(0,0):C.GC_764})

V_463 = Vertex(name = 'V_463',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_308,(0,2):C.GC_776,(0,0):C.GC_775})

V_464 = Vertex(name = 'V_464',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_306,(0,2):C.GC_305,(0,3):C.GC_1122,(0,0):C.GC_1121})

V_465 = Vertex(name = 'V_465',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_308,(0,2):C.GC_1133,(0,0):C.GC_1132})

V_466 = Vertex(name = 'V_466',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_196,(0,2):C.GC_135,(0,4):C.GC_401,(0,3):C.GC_410,(0,5):C.GC_1281,(0,1):C.GC_1279})

V_467 = Vertex(name = 'V_467',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_336,(0,2):C.GC_406,(0,3):C.GC_1293,(0,1):C.GC_1292})

V_468 = Vertex(name = 'V_468',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_426,(0,1):C.GC_407})

V_469 = Vertex(name = 'V_469',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_429,(0,1):C.GC_408})

V_470 = Vertex(name = 'V_470',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_432,(0,1):C.GC_411})

V_471 = Vertex(name = 'V_471',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_196,(0,2):C.GC_135,(0,4):C.GC_401,(0,3):C.GC_410,(0,5):C.GC_546,(0,1):C.GC_544})

V_472 = Vertex(name = 'V_472',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_336,(0,2):C.GC_406,(0,3):C.GC_558,(0,1):C.GC_557})

V_473 = Vertex(name = 'V_473',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_426,(0,1):C.GC_407})

V_474 = Vertex(name = 'V_474',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_429,(0,1):C.GC_408})

V_475 = Vertex(name = 'V_475',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_432,(0,1):C.GC_411})

V_476 = Vertex(name = 'V_476',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_196,(0,2):C.GC_135,(0,4):C.GC_401,(0,3):C.GC_410,(0,5):C.GC_984,(0,1):C.GC_982})

V_477 = Vertex(name = 'V_477',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_336,(0,2):C.GC_406,(0,3):C.GC_996,(0,1):C.GC_995})

V_478 = Vertex(name = 'V_478',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_426,(0,1):C.GC_407})

V_479 = Vertex(name = 'V_479',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_429,(0,1):C.GC_408})

V_480 = Vertex(name = 'V_480',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_432,(0,1):C.GC_411})

V_481 = Vertex(name = 'V_481',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_157})

V_482 = Vertex(name = 'V_482',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_155})

V_483 = Vertex(name = 'V_483',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_157})

V_484 = Vertex(name = 'V_484',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_155})

V_485 = Vertex(name = 'V_485',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_157})

V_486 = Vertex(name = 'V_486',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_155})

V_487 = Vertex(name = 'V_487',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_312,(0,3):C.GC_1255,(0,0):C.GC_1253})

V_488 = Vertex(name = 'V_488',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_310,(0,2):C.GC_1268,(0,0):C.GC_1267})

V_489 = Vertex(name = 'V_489',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_312,(0,3):C.GC_520,(0,0):C.GC_518})

V_490 = Vertex(name = 'V_490',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_310,(0,2):C.GC_533,(0,0):C.GC_532})

V_491 = Vertex(name = 'V_491',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_309,(0,2):C.GC_312,(0,3):C.GC_956,(0,0):C.GC_954})

V_492 = Vertex(name = 'V_492',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_310,(0,2):C.GC_971,(0,0):C.GC_970})

V_493 = Vertex(name = 'V_493',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_135})

V_494 = Vertex(name = 'V_494',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_495 = Vertex(name = 'V_495',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_404})

V_496 = Vertex(name = 'V_496',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_411})

V_497 = Vertex(name = 'V_497',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_135})

V_498 = Vertex(name = 'V_498',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_499 = Vertex(name = 'V_499',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_404})

V_500 = Vertex(name = 'V_500',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_411})

V_501 = Vertex(name = 'V_501',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_135})

V_502 = Vertex(name = 'V_502',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_400})

V_503 = Vertex(name = 'V_503',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_404})

V_504 = Vertex(name = 'V_504',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_411})

V_505 = Vertex(name = 'V_505',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_151})

V_506 = Vertex(name = 'V_506',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_152})

V_507 = Vertex(name = 'V_507',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_151})

V_508 = Vertex(name = 'V_508',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_152})

V_509 = Vertex(name = 'V_509',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_151})

V_510 = Vertex(name = 'V_510',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_152})

V_511 = Vertex(name = 'V_511',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_306})

V_512 = Vertex(name = 'V_512',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_307})

V_513 = Vertex(name = 'V_513',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_306})

V_514 = Vertex(name = 'V_514',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_307})

V_515 = Vertex(name = 'V_515',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_306})

V_516 = Vertex(name = 'V_516',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2 ],
               couplings = {(0,0):C.GC_307})

V_517 = Vertex(name = 'V_517',
               particles = [ P.t__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_84})

V_518 = Vertex(name = 'V_518',
               particles = [ P.t1__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_89})

V_519 = Vertex(name = 'V_519',
               particles = [ P.t1__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_84})

V_520 = Vertex(name = 'V_520',
               particles = [ P.t__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_87})

V_521 = Vertex(name = 'V_521',
               particles = [ P.t1__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_92})

V_522 = Vertex(name = 'V_522',
               particles = [ P.t1__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_87})

V_523 = Vertex(name = 'V_523',
               particles = [ P.d__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_179})

V_524 = Vertex(name = 'V_524',
               particles = [ P.s__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_180})

V_525 = Vertex(name = 'V_525',
               particles = [ P.b__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_181})

V_526 = Vertex(name = 'V_526',
               particles = [ P.d__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_186})

V_527 = Vertex(name = 'V_527',
               particles = [ P.s__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_187})

V_528 = Vertex(name = 'V_528',
               particles = [ P.b__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_188})

V_529 = Vertex(name = 'V_529',
               particles = [ P.d__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_173})

V_530 = Vertex(name = 'V_530',
               particles = [ P.s__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_174})

V_531 = Vertex(name = 'V_531',
               particles = [ P.b__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_175})

V_532 = Vertex(name = 'V_532',
               particles = [ P.d__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_176})

V_533 = Vertex(name = 'V_533',
               particles = [ P.s__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_177})

V_534 = Vertex(name = 'V_534',
               particles = [ P.b__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_178})

V_535 = Vertex(name = 'V_535',
               particles = [ P.d__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_179})

V_536 = Vertex(name = 'V_536',
               particles = [ P.s__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_180})

V_537 = Vertex(name = 'V_537',
               particles = [ P.b__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_181})

V_538 = Vertex(name = 'V_538',
               particles = [ P.e__plus__, P.ve, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_539 = Vertex(name = 'V_539',
               particles = [ P.mu__plus__, P.vm, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_540 = Vertex(name = 'V_540',
               particles = [ P.ta__plus__, P.vt, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_541 = Vertex(name = 'V_541',
               particles = [ P.t1__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2698})

V_542 = Vertex(name = 'V_542',
               particles = [ P.t1__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2904})

V_543 = Vertex(name = 'V_543',
               particles = [ P.t1__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3110})

V_544 = Vertex(name = 'V_544',
               particles = [ P.u__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1467})

V_545 = Vertex(name = 'V_545',
               particles = [ P.c__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2082})

V_546 = Vertex(name = 'V_546',
               particles = [ P.t__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2697})

V_547 = Vertex(name = 'V_547',
               particles = [ P.u__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1672})

V_548 = Vertex(name = 'V_548',
               particles = [ P.c__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2287})

V_549 = Vertex(name = 'V_549',
               particles = [ P.t__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2903})

V_550 = Vertex(name = 'V_550',
               particles = [ P.u__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_1877})

V_551 = Vertex(name = 'V_551',
               particles = [ P.c__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2492})

V_552 = Vertex(name = 'V_552',
               particles = [ P.t__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3109})

V_553 = Vertex(name = 'V_553',
               particles = [ P.ve__tilde__, P.e__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_554 = Vertex(name = 'V_554',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_555 = Vertex(name = 'V_555',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_172})

V_556 = Vertex(name = 'V_556',
               particles = [ P.t1__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2697})

V_557 = Vertex(name = 'V_557',
               particles = [ P.t1__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_2903})

V_558 = Vertex(name = 'V_558',
               particles = [ P.t1__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_3109})

V_559 = Vertex(name = 'V_559',
               particles = [ P.t__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_182})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t1__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_189})

V_561 = Vertex(name = 'V_561',
               particles = [ P.t1__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_182})

V_562 = Vertex(name = 'V_562',
               particles = [ P.d__tilde__, P.d, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_212,(0,1):C.GC_183})

V_563 = Vertex(name = 'V_563',
               particles = [ P.s__tilde__, P.s, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_212,(0,1):C.GC_183})

V_564 = Vertex(name = 'V_564',
               particles = [ P.b__tilde__, P.b, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_212,(0,1):C.GC_183})

V_565 = Vertex(name = 'V_565',
               particles = [ P.e__plus__, P.e__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_183})

V_566 = Vertex(name = 'V_566',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_183})

V_567 = Vertex(name = 'V_567',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_214,(0,1):C.GC_183})

V_568 = Vertex(name = 'V_568',
               particles = [ P.t__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_189})

V_569 = Vertex(name = 'V_569',
               particles = [ P.t1__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_192})

V_570 = Vertex(name = 'V_570',
               particles = [ P.t1__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_215,(0,1):C.GC_189})

V_571 = Vertex(name = 'V_571',
               particles = [ P.u__tilde__, P.u, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_182})

V_572 = Vertex(name = 'V_572',
               particles = [ P.c__tilde__, P.c, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_182})

V_573 = Vertex(name = 'V_573',
               particles = [ P.t__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_213,(0,1):C.GC_182})

V_574 = Vertex(name = 'V_574',
               particles = [ P.ve__tilde__, P.ve, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_182})

V_575 = Vertex(name = 'V_575',
               particles = [ P.vm__tilde__, P.vm, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_182})

V_576 = Vertex(name = 'V_576',
               particles = [ P.vt__tilde__, P.vt, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_182})

V_577 = Vertex(name = 'V_577',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_637,(0,1):C.GC_585})

V_578 = Vertex(name = 'V_578',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_638})

V_579 = Vertex(name = 'V_579',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_639})

V_580 = Vertex(name = 'V_580',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_640})

V_581 = Vertex(name = 'V_581',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_641})

V_582 = Vertex(name = 'V_582',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_642})

V_583 = Vertex(name = 'V_583',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_903,(0,1):C.GC_851})

V_584 = Vertex(name = 'V_584',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_904})

V_585 = Vertex(name = 'V_585',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_905})

V_586 = Vertex(name = 'V_586',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_906})

V_587 = Vertex(name = 'V_587',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_907})

V_588 = Vertex(name = 'V_588',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_908})

V_589 = Vertex(name = 'V_589',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_503,(0,1):C.GC_451})

V_590 = Vertex(name = 'V_590',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_504})

V_591 = Vertex(name = 'V_591',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_505})

V_592 = Vertex(name = 'V_592',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_506})

V_593 = Vertex(name = 'V_593',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_507})

V_594 = Vertex(name = 'V_594',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_508})

V_595 = Vertex(name = 'V_595',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_705,(0,1):C.GC_661})

V_596 = Vertex(name = 'V_596',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_706})

V_597 = Vertex(name = 'V_597',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_707})

V_598 = Vertex(name = 'V_598',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_708})

V_599 = Vertex(name = 'V_599',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_709})

V_600 = Vertex(name = 'V_600',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_710})

V_601 = Vertex(name = 'V_601',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_800,(0,1):C.GC_756})

V_602 = Vertex(name = 'V_602',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_801})

V_603 = Vertex(name = 'V_603',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_802})

V_604 = Vertex(name = 'V_604',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_803})

V_605 = Vertex(name = 'V_605',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_804})

V_606 = Vertex(name = 'V_606',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_805})

V_607 = Vertex(name = 'V_607',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1157,(0,1):C.GC_1113})

V_608 = Vertex(name = 'V_608',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1158})

V_609 = Vertex(name = 'V_609',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1159})

V_610 = Vertex(name = 'V_610',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1160})

V_611 = Vertex(name = 'V_611',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1161})

V_612 = Vertex(name = 'V_612',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1162})

V_613 = Vertex(name = 'V_613',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1300,(0,1):C.GC_1244})

V_614 = Vertex(name = 'V_614',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1296})

V_615 = Vertex(name = 'V_615',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1297})

V_616 = Vertex(name = 'V_616',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1298})

V_617 = Vertex(name = 'V_617',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1299})

V_618 = Vertex(name = 'V_618',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1301})

V_619 = Vertex(name = 'V_619',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_565,(0,1):C.GC_509})

V_620 = Vertex(name = 'V_620',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_561})

V_621 = Vertex(name = 'V_621',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_562})

V_622 = Vertex(name = 'V_622',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_563})

V_623 = Vertex(name = 'V_623',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_564})

V_624 = Vertex(name = 'V_624',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_566})

V_625 = Vertex(name = 'V_625',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1003,(0,1):C.GC_945})

V_626 = Vertex(name = 'V_626',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_999})

V_627 = Vertex(name = 'V_627',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1000})

V_628 = Vertex(name = 'V_628',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1001})

V_629 = Vertex(name = 'V_629',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1002})

V_630 = Vertex(name = 'V_630',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1004})

V_631 = Vertex(name = 'V_631',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_588,(0,1):C.GC_589})

V_632 = Vertex(name = 'V_632',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_854,(0,1):C.GC_855})

V_633 = Vertex(name = 'V_633',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_454,(0,1):C.GC_455})

V_634 = Vertex(name = 'V_634',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_614,(0,1):C.GC_615})

V_635 = Vertex(name = 'V_635',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_880,(0,1):C.GC_881})

V_636 = Vertex(name = 'V_636',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_480,(0,1):C.GC_481})

V_637 = Vertex(name = 'V_637',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_662,(0,1):C.GC_663})

V_638 = Vertex(name = 'V_638',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_757,(0,1):C.GC_758})

V_639 = Vertex(name = 'V_639',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1114,(0,1):C.GC_1115})

V_640 = Vertex(name = 'V_640',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_684,(0,1):C.GC_685})

V_641 = Vertex(name = 'V_641',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_779,(0,1):C.GC_780})

V_642 = Vertex(name = 'V_642',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1136,(0,1):C.GC_1137})

V_643 = Vertex(name = 'V_643',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1249,(0,1):C.GC_1250})

V_644 = Vertex(name = 'V_644',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_515})

V_645 = Vertex(name = 'V_645',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_950,(0,1):C.GC_951})

V_646 = Vertex(name = 'V_646',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1275,(0,1):C.GC_1276})

V_647 = Vertex(name = 'V_647',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_540,(0,1):C.GC_541})

V_648 = Vertex(name = 'V_648',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_978,(0,1):C.GC_979})

V_649 = Vertex(name = 'V_649',
               particles = [ P.d__tilde__, P.d, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_602})

V_650 = Vertex(name = 'V_650',
               particles = [ P.s__tilde__, P.s, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_868})

V_651 = Vertex(name = 'V_651',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_468})

V_652 = Vertex(name = 'V_652',
               particles = [ P.e__plus__, P.e__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_674})

V_653 = Vertex(name = 'V_653',
               particles = [ P.mu__plus__, P.mu__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_769})

V_654 = Vertex(name = 'V_654',
               particles = [ P.ta__plus__, P.ta__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1126})

V_655 = Vertex(name = 'V_655',
               particles = [ P.t__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_962})

V_656 = Vertex(name = 'V_656',
               particles = [ P.t__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_963})

V_657 = Vertex(name = 'V_657',
               particles = [ P.t1__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_963})

V_658 = Vertex(name = 'V_658',
               particles = [ P.t1__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_964})

V_659 = Vertex(name = 'V_659',
               particles = [ P.t1__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_962})

V_660 = Vertex(name = 'V_660',
               particles = [ P.t1__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_963})

V_661 = Vertex(name = 'V_661',
               particles = [ P.u__tilde__, P.u, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1261})

V_662 = Vertex(name = 'V_662',
               particles = [ P.c__tilde__, P.c, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_526})

V_663 = Vertex(name = 'V_663',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_962})

V_664 = Vertex(name = 'V_664',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_594,(0,0):C.GC_593})

V_665 = Vertex(name = 'V_665',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_611,(0,0):C.GC_610})

V_666 = Vertex(name = 'V_666',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_860,(0,0):C.GC_859})

V_667 = Vertex(name = 'V_667',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_877,(0,0):C.GC_876})

V_668 = Vertex(name = 'V_668',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_460,(0,0):C.GC_459})

V_669 = Vertex(name = 'V_669',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_477,(0,0):C.GC_476})

V_670 = Vertex(name = 'V_670',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_587,(0,0):C.GC_586})

V_671 = Vertex(name = 'V_671',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_853,(0,0):C.GC_852})

V_672 = Vertex(name = 'V_672',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_453,(0,0):C.GC_452})

V_673 = Vertex(name = 'V_673',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_601,(0,0):C.GC_600})

V_674 = Vertex(name = 'V_674',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_867,(0,0):C.GC_866})

V_675 = Vertex(name = 'V_675',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_467,(0,0):C.GC_466})

V_676 = Vertex(name = 'V_676',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_627,(0,0):C.GC_626})

V_677 = Vertex(name = 'V_677',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_893,(0,0):C.GC_892})

V_678 = Vertex(name = 'V_678',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_493,(0,0):C.GC_492})

V_679 = Vertex(name = 'V_679',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_597,(0,1):C.GC_1256})

V_680 = Vertex(name = 'V_680',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_599,(0,1):C.GC_1258})

V_681 = Vertex(name = 'V_681',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_863,(0,1):C.GC_521})

V_682 = Vertex(name = 'V_682',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_865,(0,1):C.GC_523})

V_683 = Vertex(name = 'V_683',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_463,(0,1):C.GC_957})

V_684 = Vertex(name = 'V_684',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_465,(0,1):C.GC_959})

V_685 = Vertex(name = 'V_685',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_623,(0,1):C.GC_1282})

V_686 = Vertex(name = 'V_686',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_625,(0,1):C.GC_1284})

V_687 = Vertex(name = 'V_687',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_889,(0,1):C.GC_547})

V_688 = Vertex(name = 'V_688',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_891,(0,1):C.GC_549})

V_689 = Vertex(name = 'V_689',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_489,(0,1):C.GC_985})

V_690 = Vertex(name = 'V_690',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_491,(0,1):C.GC_987})

V_691 = Vertex(name = 'V_691',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_604,(0,0):C.GC_603})

V_692 = Vertex(name = 'V_692',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_870,(0,0):C.GC_869})

V_693 = Vertex(name = 'V_693',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_470,(0,0):C.GC_469})

V_694 = Vertex(name = 'V_694',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_629,(0,0):C.GC_628})

V_695 = Vertex(name = 'V_695',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_895,(0,0):C.GC_894})

V_696 = Vertex(name = 'V_696',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_495,(0,0):C.GC_494})

V_697 = Vertex(name = 'V_697',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_668,(0,0):C.GC_667})

V_698 = Vertex(name = 'V_698',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_683,(0,0):C.GC_682})

V_699 = Vertex(name = 'V_699',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_763,(0,0):C.GC_762})

V_700 = Vertex(name = 'V_700',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_778,(0,0):C.GC_777})

V_701 = Vertex(name = 'V_701',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1120,(0,0):C.GC_1119})

V_702 = Vertex(name = 'V_702',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1135,(0,0):C.GC_1134})

V_703 = Vertex(name = 'V_703',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_671})

V_704 = Vertex(name = 'V_704',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_673})

V_705 = Vertex(name = 'V_705',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_766})

V_706 = Vertex(name = 'V_706',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_768})

V_707 = Vertex(name = 'V_707',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1123})

V_708 = Vertex(name = 'V_708',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1125})

V_709 = Vertex(name = 'V_709',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_693})

V_710 = Vertex(name = 'V_710',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_695})

V_711 = Vertex(name = 'V_711',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_788})

V_712 = Vertex(name = 'V_712',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_790})

V_713 = Vertex(name = 'V_713',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1145})

V_714 = Vertex(name = 'V_714',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1147})

V_715 = Vertex(name = 'V_715',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_676,(0,0):C.GC_675})

V_716 = Vertex(name = 'V_716',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_771,(0,0):C.GC_770})

V_717 = Vertex(name = 'V_717',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1128,(0,0):C.GC_1127})

V_718 = Vertex(name = 'V_718',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_697,(0,0):C.GC_696})

V_719 = Vertex(name = 'V_719',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_792,(0,0):C.GC_791})

V_720 = Vertex(name = 'V_720',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1149,(0,0):C.GC_1148})

V_721 = Vertex(name = 'V_721',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1246,(0,0):C.GC_1245})

V_722 = Vertex(name = 'V_722',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1270,(0,0):C.GC_1269})

V_723 = Vertex(name = 'V_723',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_511,(0,0):C.GC_510})

V_724 = Vertex(name = 'V_724',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_535,(0,0):C.GC_534})

V_725 = Vertex(name = 'V_725',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_947,(0,0):C.GC_946})

V_726 = Vertex(name = 'V_726',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_973,(0,0):C.GC_972})

V_727 = Vertex(name = 'V_727',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_1248,(0,0):C.GC_1247})

V_728 = Vertex(name = 'V_728',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_513,(0,0):C.GC_512})

V_729 = Vertex(name = 'V_729',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_949,(0,0):C.GC_948})

V_730 = Vertex(name = 'V_730',
               particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1260,(0,0):C.GC_1259})

V_731 = Vertex(name = 'V_731',
               particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_525,(0,0):C.GC_524})

V_732 = Vertex(name = 'V_732',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_961,(0,0):C.GC_960})

V_733 = Vertex(name = 'V_733',
               particles = [ P.u__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1286,(0,0):C.GC_1285})

V_734 = Vertex(name = 'V_734',
               particles = [ P.c__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_551,(0,0):C.GC_550})

V_735 = Vertex(name = 'V_735',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_989,(0,0):C.GC_988})

V_736 = Vertex(name = 'V_736',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1256,(0,1):C.GC_597})

V_737 = Vertex(name = 'V_737',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1257,(0,1):C.GC_598})

V_738 = Vertex(name = 'V_738',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_521,(0,1):C.GC_863})

V_739 = Vertex(name = 'V_739',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_864})

V_740 = Vertex(name = 'V_740',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_957,(0,1):C.GC_463})

V_741 = Vertex(name = 'V_741',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_958,(0,1):C.GC_464})

V_742 = Vertex(name = 'V_742',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1282,(0,1):C.GC_623})

V_743 = Vertex(name = 'V_743',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1283,(0,1):C.GC_624})

V_744 = Vertex(name = 'V_744',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_547,(0,1):C.GC_889})

V_745 = Vertex(name = 'V_745',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_548,(0,1):C.GC_890})

V_746 = Vertex(name = 'V_746',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_985,(0,1):C.GC_489})

V_747 = Vertex(name = 'V_747',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_986,(0,1):C.GC_490})

V_748 = Vertex(name = 'V_748',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1264,(0,0):C.GC_1262})

V_749 = Vertex(name = 'V_749',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_529,(0,0):C.GC_527})

V_750 = Vertex(name = 'V_750',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_967,(0,0):C.GC_965})

V_751 = Vertex(name = 'V_751',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1289,(0,0):C.GC_1287})

V_752 = Vertex(name = 'V_752',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_554,(0,0):C.GC_552})

V_753 = Vertex(name = 'V_753',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_992,(0,0):C.GC_990})

V_754 = Vertex(name = 'V_754',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_605,(0,1):C.GC_1263})

V_755 = Vertex(name = 'V_755',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_606,(0,1):C.GC_1265})

V_756 = Vertex(name = 'V_756',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_871,(0,1):C.GC_528})

V_757 = Vertex(name = 'V_757',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_872,(0,1):C.GC_530})

V_758 = Vertex(name = 'V_758',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_471,(0,1):C.GC_966})

V_759 = Vertex(name = 'V_759',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_472,(0,1):C.GC_968})

V_760 = Vertex(name = 'V_760',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_630,(0,1):C.GC_1288})

V_761 = Vertex(name = 'V_761',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_631,(0,1):C.GC_1290})

V_762 = Vertex(name = 'V_762',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_896,(0,1):C.GC_553})

V_763 = Vertex(name = 'V_763',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_897,(0,1):C.GC_555})

V_764 = Vertex(name = 'V_764',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_496,(0,1):C.GC_991})

V_765 = Vertex(name = 'V_765',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_497,(0,1):C.GC_993})

V_766 = Vertex(name = 'V_766',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_677})

V_767 = Vertex(name = 'V_767',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_678})

V_768 = Vertex(name = 'V_768',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_772})

V_769 = Vertex(name = 'V_769',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_773})

V_770 = Vertex(name = 'V_770',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1129})

V_771 = Vertex(name = 'V_771',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1130})

V_772 = Vertex(name = 'V_772',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_698})

V_773 = Vertex(name = 'V_773',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_699})

V_774 = Vertex(name = 'V_774',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_793})

V_775 = Vertex(name = 'V_775',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_794})

V_776 = Vertex(name = 'V_776',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1150})

V_777 = Vertex(name = 'V_777',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1151})

V_778 = Vertex(name = 'V_778',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1263,(0,1):C.GC_605})

V_779 = Vertex(name = 'V_779',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1266,(0,1):C.GC_607})

V_780 = Vertex(name = 'V_780',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_528,(0,1):C.GC_871})

V_781 = Vertex(name = 'V_781',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_873})

V_782 = Vertex(name = 'V_782',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_966,(0,1):C.GC_471})

V_783 = Vertex(name = 'V_783',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_969,(0,1):C.GC_473})

V_784 = Vertex(name = 'V_784',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1288,(0,1):C.GC_630})

V_785 = Vertex(name = 'V_785',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1291,(0,1):C.GC_632})

V_786 = Vertex(name = 'V_786',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_553,(0,1):C.GC_896})

V_787 = Vertex(name = 'V_787',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_556,(0,1):C.GC_898})

V_788 = Vertex(name = 'V_788',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_991,(0,1):C.GC_496})

V_789 = Vertex(name = 'V_789',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_994,(0,1):C.GC_498})

V_790 = Vertex(name = 'V_790',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_671})

V_791 = Vertex(name = 'V_791',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_672})

V_792 = Vertex(name = 'V_792',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_766})

V_793 = Vertex(name = 'V_793',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_767})

V_794 = Vertex(name = 'V_794',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1123})

V_795 = Vertex(name = 'V_795',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1124})

V_796 = Vertex(name = 'V_796',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_693})

V_797 = Vertex(name = 'V_797',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_694})

V_798 = Vertex(name = 'V_798',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_788})

V_799 = Vertex(name = 'V_799',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_789})

V_800 = Vertex(name = 'V_800',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1145})

V_801 = Vertex(name = 'V_801',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1146})

V_802 = Vertex(name = 'V_802',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_677})

V_803 = Vertex(name = 'V_803',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_679})

V_804 = Vertex(name = 'V_804',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_772})

V_805 = Vertex(name = 'V_805',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_774})

V_806 = Vertex(name = 'V_806',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1129})

V_807 = Vertex(name = 'V_807',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_1131})

V_808 = Vertex(name = 'V_808',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_698})

V_809 = Vertex(name = 'V_809',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_700})

V_810 = Vertex(name = 'V_810',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_793})

V_811 = Vertex(name = 'V_811',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_795})

V_812 = Vertex(name = 'V_812',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1150})

V_813 = Vertex(name = 'V_813',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_1152})

V_814 = Vertex(name = 'V_814',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_815 = Vertex(name = 'V_815',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_11,(0,1):C.GC_11})

V_816 = Vertex(name = 'V_816',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_817 = Vertex(name = 'V_817',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_818 = Vertex(name = 'V_818',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_10,(0,3):C.GC_11})

V_819 = Vertex(name = 'V_819',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_820 = Vertex(name = 'V_820',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_10,(0,3):C.GC_11})

V_821 = Vertex(name = 'V_821',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_822 = Vertex(name = 'V_822',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_823 = Vertex(name = 'V_823',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_11,(0,1):C.GC_11})

V_824 = Vertex(name = 'V_824',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_825 = Vertex(name = 'V_825',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_826 = Vertex(name = 'V_826',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_10,(0,3):C.GC_11})

V_827 = Vertex(name = 'V_827',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_828 = Vertex(name = 'V_828',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_829 = Vertex(name = 'V_829',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_11,(0,1):C.GC_11})

V_830 = Vertex(name = 'V_830',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_831 = Vertex(name = 'V_831',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_832 = Vertex(name = 'V_832',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_26,(0,7):C.GC_26,(0,0):C.GC_25,(0,3):C.GC_25,(0,1):C.GC_25,(0,2):C.GC_13,(0,4):C.GC_25,(0,5):C.GC_13})

V_833 = Vertex(name = 'V_833',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_834 = Vertex(name = 'V_834',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_26,(0,4):C.GC_27,(0,2):C.GC_25,(0,0):C.GC_25,(0,1):C.GC_13})

V_835 = Vertex(name = 'V_835',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_26,(0,4):C.GC_27,(0,2):C.GC_25,(0,0):C.GC_25,(0,1):C.GC_13})

V_836 = Vertex(name = 'V_836',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_26,(0,7):C.GC_26,(0,0):C.GC_25,(0,3):C.GC_25,(0,1):C.GC_25,(0,2):C.GC_13,(0,4):C.GC_25,(0,5):C.GC_13})

V_837 = Vertex(name = 'V_837',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_838 = Vertex(name = 'V_838',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_26,(0,4):C.GC_27,(0,2):C.GC_25,(0,0):C.GC_25,(0,1):C.GC_13})

V_839 = Vertex(name = 'V_839',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_26,(0,7):C.GC_26,(0,0):C.GC_25,(0,3):C.GC_25,(0,1):C.GC_25,(0,2):C.GC_13,(0,4):C.GC_25,(0,5):C.GC_13})

V_840 = Vertex(name = 'V_840',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_841 = Vertex(name = 'V_841',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_747,(0,0):C.GC_748})

V_842 = Vertex(name = 'V_842',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_752,(0,0):C.GC_752})

V_843 = Vertex(name = 'V_843',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_842,(0,0):C.GC_843})

V_844 = Vertex(name = 'V_844',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_847,(0,0):C.GC_847})

V_845 = Vertex(name = 'V_845',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_1199,(0,0):C.GC_1200})

V_846 = Vertex(name = 'V_846',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_1204,(0,0):C.GC_1204})

V_847 = Vertex(name = 'V_847',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_927,(0,0):C.GC_928})

V_848 = Vertex(name = 'V_848',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_932,(0,0):C.GC_932})

V_849 = Vertex(name = 'V_849',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_936,(0,0):C.GC_937})

V_850 = Vertex(name = 'V_850',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_941,(0,0):C.GC_941})

V_851 = Vertex(name = 'V_851',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_1208,(0,0):C.GC_1209})

V_852 = Vertex(name = 'V_852',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_1213,(0,0):C.GC_1213})

V_853 = Vertex(name = 'V_853',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_711,(0,0):C.GC_712})

V_854 = Vertex(name = 'V_854',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_716,(0,0):C.GC_716})

V_855 = Vertex(name = 'V_855',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_806,(0,0):C.GC_807})

V_856 = Vertex(name = 'V_856',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_811,(0,0):C.GC_811})

V_857 = Vertex(name = 'V_857',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_28,(0,1):C.GC_43,(0,2):C.GC_24,(0,3):C.GC_12,(0,5):C.GC_1163,(0,0):C.GC_1164})

V_858 = Vertex(name = 'V_858',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_30,(0,2):C.GC_1168,(0,0):C.GC_1168})

V_859 = Vertex(name = 'V_859',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_31,(0,5):C.GC_1351,(0,3):C.GC_1352,(0,4):C.GC_1352,(0,1):C.GC_1340,(0,0):C.GC_749})

V_860 = Vertex(name = 'V_860',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1360,(0,2):C.GC_1359,(0,3):C.GC_1359,(0,1):C.GC_1344,(0,0):C.GC_753})

V_861 = Vertex(name = 'V_861',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_733,(0,3):C.GC_734,(0,4):C.GC_734,(0,1):C.GC_722,(0,0):C.GC_750})

V_862 = Vertex(name = 'V_862',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_742,(0,2):C.GC_741,(0,3):C.GC_741,(0,1):C.GC_726,(0,0):C.GC_754})

V_863 = Vertex(name = 'V_863',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_1054,(0,3):C.GC_1055,(0,4):C.GC_1055,(0,1):C.GC_1043,(0,0):C.GC_751})

V_864 = Vertex(name = 'V_864',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1063,(0,2):C.GC_1062,(0,3):C.GC_1062,(0,1):C.GC_1047,(0,0):C.GC_755})

V_865 = Vertex(name = 'V_865',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_32,(0,5):C.GC_1353,(0,3):C.GC_1354,(0,4):C.GC_1354,(0,1):C.GC_1341,(0,0):C.GC_929})

V_866 = Vertex(name = 'V_866',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1362,(0,2):C.GC_1361,(0,3):C.GC_1361,(0,1):C.GC_1345,(0,0):C.GC_933})

V_867 = Vertex(name = 'V_867',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_735,(0,3):C.GC_736,(0,4):C.GC_736,(0,1):C.GC_723,(0,0):C.GC_930})

V_868 = Vertex(name = 'V_868',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_744,(0,2):C.GC_743,(0,3):C.GC_743,(0,1):C.GC_727,(0,0):C.GC_934})

V_869 = Vertex(name = 'V_869',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_1056,(0,3):C.GC_1057,(0,4):C.GC_1057,(0,1):C.GC_1044,(0,0):C.GC_931})

V_870 = Vertex(name = 'V_870',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1065,(0,2):C.GC_1064,(0,3):C.GC_1064,(0,1):C.GC_1048,(0,0):C.GC_935})

V_871 = Vertex(name = 'V_871',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_33,(0,5):C.GC_1355,(0,3):C.GC_1356,(0,4):C.GC_1356,(0,1):C.GC_1342,(0,0):C.GC_713})

V_872 = Vertex(name = 'V_872',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1364,(0,2):C.GC_1363,(0,3):C.GC_1363,(0,1):C.GC_1346,(0,0):C.GC_717})

V_873 = Vertex(name = 'V_873',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_737,(0,3):C.GC_738,(0,4):C.GC_738,(0,1):C.GC_724,(0,0):C.GC_714})

V_874 = Vertex(name = 'V_874',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_746,(0,2):C.GC_745,(0,3):C.GC_745,(0,1):C.GC_728,(0,0):C.GC_718})

V_875 = Vertex(name = 'V_875',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_1058,(0,3):C.GC_1059,(0,4):C.GC_1059,(0,1):C.GC_1045,(0,0):C.GC_715})

V_876 = Vertex(name = 'V_876',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1067,(0,2):C.GC_1066,(0,3):C.GC_1066,(0,1):C.GC_1049,(0,0):C.GC_719})

V_877 = Vertex(name = 'V_877',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_31,(0,5):C.GC_1378,(0,3):C.GC_1379,(0,4):C.GC_1379,(0,1):C.GC_1367,(0,0):C.GC_844})

V_878 = Vertex(name = 'V_878',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1387,(0,2):C.GC_1386,(0,3):C.GC_1386,(0,1):C.GC_1371,(0,0):C.GC_848})

V_879 = Vertex(name = 'V_879',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_828,(0,3):C.GC_829,(0,4):C.GC_829,(0,1):C.GC_817,(0,0):C.GC_845})

V_880 = Vertex(name = 'V_880',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_837,(0,2):C.GC_836,(0,3):C.GC_836,(0,1):C.GC_821,(0,0):C.GC_849})

V_881 = Vertex(name = 'V_881',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_1081,(0,3):C.GC_1082,(0,4):C.GC_1082,(0,1):C.GC_1070,(0,0):C.GC_846})

V_882 = Vertex(name = 'V_882',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1090,(0,2):C.GC_1089,(0,3):C.GC_1089,(0,1):C.GC_1074,(0,0):C.GC_850})

V_883 = Vertex(name = 'V_883',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_32,(0,5):C.GC_1380,(0,3):C.GC_1381,(0,4):C.GC_1381,(0,1):C.GC_1368,(0,0):C.GC_938})

V_884 = Vertex(name = 'V_884',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1389,(0,2):C.GC_1388,(0,3):C.GC_1388,(0,1):C.GC_1372,(0,0):C.GC_942})

V_885 = Vertex(name = 'V_885',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_830,(0,3):C.GC_831,(0,4):C.GC_831,(0,1):C.GC_818,(0,0):C.GC_939})

V_886 = Vertex(name = 'V_886',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_839,(0,2):C.GC_838,(0,3):C.GC_838,(0,1):C.GC_822,(0,0):C.GC_943})

V_887 = Vertex(name = 'V_887',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_1083,(0,3):C.GC_1084,(0,4):C.GC_1084,(0,1):C.GC_1071,(0,0):C.GC_940})

V_888 = Vertex(name = 'V_888',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1092,(0,2):C.GC_1091,(0,3):C.GC_1091,(0,1):C.GC_1075,(0,0):C.GC_944})

V_889 = Vertex(name = 'V_889',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_33,(0,5):C.GC_1382,(0,3):C.GC_1383,(0,4):C.GC_1383,(0,1):C.GC_1369,(0,0):C.GC_808})

V_890 = Vertex(name = 'V_890',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1391,(0,2):C.GC_1390,(0,3):C.GC_1390,(0,1):C.GC_1373,(0,0):C.GC_812})

V_891 = Vertex(name = 'V_891',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_832,(0,3):C.GC_833,(0,4):C.GC_833,(0,1):C.GC_819,(0,0):C.GC_809})

V_892 = Vertex(name = 'V_892',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_841,(0,2):C.GC_840,(0,3):C.GC_840,(0,1):C.GC_823,(0,0):C.GC_813})

V_893 = Vertex(name = 'V_893',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_1085,(0,3):C.GC_1086,(0,4):C.GC_1086,(0,1):C.GC_1072,(0,0):C.GC_810})

V_894 = Vertex(name = 'V_894',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1094,(0,2):C.GC_1093,(0,3):C.GC_1093,(0,1):C.GC_1076,(0,0):C.GC_814})

V_895 = Vertex(name = 'V_895',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_31,(0,5):C.GC_1423,(0,3):C.GC_1424,(0,4):C.GC_1424,(0,1):C.GC_1412,(0,0):C.GC_1201})

V_896 = Vertex(name = 'V_896',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1432,(0,2):C.GC_1431,(0,3):C.GC_1431,(0,1):C.GC_1416,(0,0):C.GC_1205})

V_897 = Vertex(name = 'V_897',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_34,(0,5):C.GC_1185,(0,3):C.GC_1186,(0,4):C.GC_1186,(0,1):C.GC_1174,(0,0):C.GC_1202})

V_898 = Vertex(name = 'V_898',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1194,(0,2):C.GC_1193,(0,3):C.GC_1193,(0,1):C.GC_1178,(0,0):C.GC_1206})

V_899 = Vertex(name = 'V_899',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_37,(0,5):C.GC_1230,(0,3):C.GC_1231,(0,4):C.GC_1231,(0,1):C.GC_1219,(0,0):C.GC_1203})

V_900 = Vertex(name = 'V_900',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1239,(0,2):C.GC_1238,(0,3):C.GC_1238,(0,1):C.GC_1223,(0,0):C.GC_1207})

V_901 = Vertex(name = 'V_901',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_32,(0,5):C.GC_1425,(0,3):C.GC_1426,(0,4):C.GC_1426,(0,1):C.GC_1413,(0,0):C.GC_1210})

V_902 = Vertex(name = 'V_902',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1434,(0,2):C.GC_1433,(0,3):C.GC_1433,(0,1):C.GC_1417,(0,0):C.GC_1214})

V_903 = Vertex(name = 'V_903',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_35,(0,5):C.GC_1187,(0,3):C.GC_1188,(0,4):C.GC_1188,(0,1):C.GC_1175,(0,0):C.GC_1211})

V_904 = Vertex(name = 'V_904',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1196,(0,2):C.GC_1195,(0,3):C.GC_1195,(0,1):C.GC_1179,(0,0):C.GC_1215})

V_905 = Vertex(name = 'V_905',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_38,(0,5):C.GC_1232,(0,3):C.GC_1233,(0,4):C.GC_1233,(0,1):C.GC_1220,(0,0):C.GC_1212})

V_906 = Vertex(name = 'V_906',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1241,(0,2):C.GC_1240,(0,3):C.GC_1240,(0,1):C.GC_1224,(0,0):C.GC_1216})

V_907 = Vertex(name = 'V_907',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_33,(0,5):C.GC_1427,(0,3):C.GC_1428,(0,4):C.GC_1428,(0,1):C.GC_1414,(0,0):C.GC_1165})

V_908 = Vertex(name = 'V_908',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1436,(0,2):C.GC_1435,(0,3):C.GC_1435,(0,1):C.GC_1418,(0,0):C.GC_1169})

V_909 = Vertex(name = 'V_909',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_36,(0,5):C.GC_1189,(0,3):C.GC_1190,(0,4):C.GC_1190,(0,1):C.GC_1176,(0,0):C.GC_1166})

V_910 = Vertex(name = 'V_910',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1198,(0,2):C.GC_1197,(0,3):C.GC_1197,(0,1):C.GC_1180,(0,0):C.GC_1170})

V_911 = Vertex(name = 'V_911',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_39,(0,5):C.GC_1234,(0,3):C.GC_1235,(0,4):C.GC_1235,(0,1):C.GC_1221,(0,0):C.GC_1167})

V_912 = Vertex(name = 'V_912',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_1243,(0,2):C.GC_1242,(0,3):C.GC_1242,(0,1):C.GC_1225,(0,0):C.GC_1171})

V_913 = Vertex(name = 'V_913',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1324,(3,0):C.GC_1330,(0,6):C.GC_1320,(2,6):C.GC_1326,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1323,(3,1):C.GC_1329,(0,2):C.GC_1321,(2,2):C.GC_1327})

V_914 = Vertex(name = 'V_914',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_46,(0,5):C.GC_1447,(1,0):C.GC_1325,(3,0):C.GC_1331,(0,3):C.GC_1322,(2,3):C.GC_1328,(1,1):C.GC_1325,(3,1):C.GC_1331,(0,2):C.GC_1322,(2,2):C.GC_1328})

V_915 = Vertex(name = 'V_915',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1438,(1,0):C.GC_1551,(3,0):C.GC_1573,(0,3):C.GC_1561,(2,3):C.GC_1583,(1,1):C.GC_1550,(3,1):C.GC_1572,(0,2):C.GC_1562,(2,2):C.GC_1584})

V_916 = Vertex(name = 'V_916',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1456,(1,0):C.GC_1556,(3,0):C.GC_1578,(0,3):C.GC_1567,(2,3):C.GC_1589,(1,1):C.GC_1556,(3,1):C.GC_1578,(0,2):C.GC_1567,(2,2):C.GC_1589})

V_917 = Vertex(name = 'V_917',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2053,(0,5):C.GC_2062,(1,0):C.GC_2233,(3,0):C.GC_2245,(0,3):C.GC_2239,(2,3):C.GC_2251,(1,1):C.GC_2111,(3,1):C.GC_2133,(0,2):C.GC_2122,(2,2):C.GC_2144})

V_918 = Vertex(name = 'V_918',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2071,(1,0):C.GC_2236,(3,0):C.GC_2248,(0,3):C.GC_2242,(2,3):C.GC_2254,(1,1):C.GC_2117,(3,1):C.GC_2139,(0,2):C.GC_2128,(2,2):C.GC_2150})

V_919 = Vertex(name = 'V_919',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2668,(0,5):C.GC_2677,(1,0):C.GC_2849,(3,0):C.GC_2861,(0,3):C.GC_2855,(2,3):C.GC_2867,(1,1):C.GC_2755,(3,1):C.GC_2777,(0,2):C.GC_2766,(2,2):C.GC_2788})

V_920 = Vertex(name = 'V_920',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2686,(1,0):C.GC_2852,(3,0):C.GC_2864,(0,3):C.GC_2858,(2,3):C.GC_2870,(1,1):C.GC_2761,(3,1):C.GC_2783,(0,2):C.GC_2772,(2,2):C.GC_2794})

V_921 = Vertex(name = 'V_921',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1441,(0,5):C.GC_1450,(1,0):C.GC_1472,(3,0):C.GC_1484,(0,3):C.GC_1478,(2,3):C.GC_1490,(1,1):C.GC_1554,(3,1):C.GC_1576,(0,2):C.GC_1565,(2,2):C.GC_1587})

V_922 = Vertex(name = 'V_922',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1459,(1,0):C.GC_1475,(3,0):C.GC_1487,(0,3):C.GC_1481,(2,3):C.GC_1493,(1,1):C.GC_1559,(3,1):C.GC_1581,(0,2):C.GC_1570,(2,2):C.GC_1592})

V_923 = Vertex(name = 'V_923',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_647,(3,0):C.GC_653,(0,6):C.GC_643,(2,6):C.GC_649,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_646,(3,1):C.GC_652,(0,2):C.GC_644,(2,2):C.GC_650})

V_924 = Vertex(name = 'V_924',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_46,(0,5):C.GC_2065,(1,0):C.GC_648,(3,0):C.GC_654,(0,3):C.GC_645,(2,3):C.GC_651,(1,1):C.GC_648,(3,1):C.GC_654,(0,2):C.GC_645,(2,2):C.GC_651})

V_925 = Vertex(name = 'V_925',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2056,(1,0):C.GC_2113,(3,0):C.GC_2135,(0,3):C.GC_2123,(2,3):C.GC_2145,(1,1):C.GC_2112,(3,1):C.GC_2134,(0,2):C.GC_2124,(2,2):C.GC_2146})

V_926 = Vertex(name = 'V_926',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2074,(1,0):C.GC_2118,(3,0):C.GC_2140,(0,3):C.GC_2129,(2,3):C.GC_2151,(1,1):C.GC_2118,(3,1):C.GC_2140,(0,2):C.GC_2129,(2,2):C.GC_2151})

V_927 = Vertex(name = 'V_927',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2671,(0,5):C.GC_2680,(1,0):C.GC_2703,(3,0):C.GC_2715,(0,3):C.GC_2709,(2,3):C.GC_2721,(1,1):C.GC_2756,(3,1):C.GC_2778,(0,2):C.GC_2767,(2,2):C.GC_2789})

V_928 = Vertex(name = 'V_928',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2689,(1,0):C.GC_2706,(3,0):C.GC_2718,(0,3):C.GC_2712,(2,3):C.GC_2724,(1,1):C.GC_2762,(3,1):C.GC_2784,(0,2):C.GC_2773,(2,2):C.GC_2795})

V_929 = Vertex(name = 'V_929',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1444,(0,5):C.GC_1453,(1,0):C.GC_1500,(3,0):C.GC_1512,(0,3):C.GC_1506,(2,3):C.GC_1518,(1,1):C.GC_1555,(3,1):C.GC_1577,(0,2):C.GC_1566,(2,2):C.GC_1588})

V_930 = Vertex(name = 'V_930',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1462,(1,0):C.GC_1503,(3,0):C.GC_1515,(0,3):C.GC_1509,(2,3):C.GC_1521,(1,1):C.GC_1560,(3,1):C.GC_1582,(0,2):C.GC_1571,(2,2):C.GC_1593})

V_931 = Vertex(name = 'V_931',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2059,(0,5):C.GC_2068,(1,0):C.GC_2201,(3,0):C.GC_2213,(0,3):C.GC_2207,(2,3):C.GC_2219,(1,1):C.GC_2116,(3,1):C.GC_2138,(0,2):C.GC_2127,(2,2):C.GC_2149})

V_932 = Vertex(name = 'V_932',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2077,(1,0):C.GC_2204,(3,0):C.GC_2216,(0,3):C.GC_2210,(2,3):C.GC_2222,(1,1):C.GC_2121,(3,1):C.GC_2143,(0,2):C.GC_2132,(2,2):C.GC_2154})

V_933 = Vertex(name = 'V_933',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1027,(3,0):C.GC_1033,(0,6):C.GC_1023,(2,6):C.GC_1029,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1026,(3,1):C.GC_1032,(0,2):C.GC_1024,(2,2):C.GC_1030})

V_934 = Vertex(name = 'V_934',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_46,(0,5):C.GC_2683,(1,0):C.GC_1028,(3,0):C.GC_1034,(0,3):C.GC_1025,(2,3):C.GC_1031,(1,1):C.GC_1028,(3,1):C.GC_1034,(0,2):C.GC_1025,(2,2):C.GC_1031})

V_935 = Vertex(name = 'V_935',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2674,(1,0):C.GC_2758,(3,0):C.GC_2780,(0,3):C.GC_2768,(2,3):C.GC_2790,(1,1):C.GC_2757,(3,1):C.GC_2779,(0,2):C.GC_2769,(2,2):C.GC_2791})

V_936 = Vertex(name = 'V_936',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2692,(1,0):C.GC_2763,(3,0):C.GC_2785,(0,3):C.GC_2774,(2,3):C.GC_2796,(1,1):C.GC_2763,(3,1):C.GC_2785,(0,2):C.GC_2774,(2,2):C.GC_2796})

V_937 = Vertex(name = 'V_937',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1439,(0,5):C.GC_1448,(1,0):C.GC_1552,(3,0):C.GC_1574,(0,3):C.GC_1563,(2,3):C.GC_1585,(1,1):C.GC_1612,(3,1):C.GC_1624,(0,2):C.GC_1618,(2,2):C.GC_1630})

V_938 = Vertex(name = 'V_938',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1457,(1,0):C.GC_1557,(3,0):C.GC_1579,(0,3):C.GC_1568,(2,3):C.GC_1590,(1,1):C.GC_1615,(3,1):C.GC_1627,(0,2):C.GC_1621,(2,2):C.GC_1633})

V_939 = Vertex(name = 'V_939',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2054,(0,5):C.GC_2063,(1,0):C.GC_2234,(3,0):C.GC_2246,(0,3):C.GC_2240,(2,3):C.GC_2252,(1,1):C.GC_2177,(3,1):C.GC_2189,(0,2):C.GC_2183,(2,2):C.GC_2195})

V_940 = Vertex(name = 'V_940',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2072,(1,0):C.GC_2237,(3,0):C.GC_2249,(0,3):C.GC_2243,(2,3):C.GC_2255,(1,1):C.GC_2180,(3,1):C.GC_2192,(0,2):C.GC_2186,(2,2):C.GC_2198})

V_941 = Vertex(name = 'V_941',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2669,(0,5):C.GC_2678,(1,0):C.GC_2850,(3,0):C.GC_2862,(0,3):C.GC_2856,(2,3):C.GC_2868,(1,1):C.GC_2817,(3,1):C.GC_2829,(0,2):C.GC_2823,(2,2):C.GC_2835})

V_942 = Vertex(name = 'V_942',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2687,(1,0):C.GC_2853,(3,0):C.GC_2865,(0,3):C.GC_2859,(2,3):C.GC_2871,(1,1):C.GC_2820,(3,1):C.GC_2832,(0,2):C.GC_2826,(2,2):C.GC_2838})

V_943 = Vertex(name = 'V_943',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1442,(0,5):C.GC_1451,(1,0):C.GC_1473,(3,0):C.GC_1485,(0,3):C.GC_1479,(2,3):C.GC_1491,(1,1):C.GC_1613,(3,1):C.GC_1625,(0,2):C.GC_1619,(2,2):C.GC_1631})

V_944 = Vertex(name = 'V_944',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1460,(1,0):C.GC_1476,(3,0):C.GC_1488,(0,3):C.GC_1482,(2,3):C.GC_1494,(1,1):C.GC_1616,(3,1):C.GC_1628,(0,2):C.GC_1622,(2,2):C.GC_1634})

V_945 = Vertex(name = 'V_945',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2057,(0,5):C.GC_2066,(1,0):C.GC_2114,(3,0):C.GC_2136,(0,3):C.GC_2125,(2,3):C.GC_2147,(1,1):C.GC_2178,(3,1):C.GC_2190,(0,2):C.GC_2184,(2,2):C.GC_2196})

V_946 = Vertex(name = 'V_946',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2075,(1,0):C.GC_2119,(3,0):C.GC_2141,(0,3):C.GC_2130,(2,3):C.GC_2152,(1,1):C.GC_2181,(3,1):C.GC_2193,(0,2):C.GC_2187,(2,2):C.GC_2199})

V_947 = Vertex(name = 'V_947',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2672,(0,5):C.GC_2681,(1,0):C.GC_2704,(3,0):C.GC_2716,(0,3):C.GC_2710,(2,3):C.GC_2722,(1,1):C.GC_2818,(3,1):C.GC_2830,(0,2):C.GC_2824,(2,2):C.GC_2836})

V_948 = Vertex(name = 'V_948',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2690,(1,0):C.GC_2707,(3,0):C.GC_2719,(0,3):C.GC_2713,(2,3):C.GC_2725,(1,1):C.GC_2821,(3,1):C.GC_2833,(0,2):C.GC_2827,(2,2):C.GC_2839})

V_949 = Vertex(name = 'V_949',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1445,(0,5):C.GC_1454,(1,0):C.GC_1501,(3,0):C.GC_1513,(0,3):C.GC_1507,(2,3):C.GC_1519,(1,1):C.GC_1614,(3,1):C.GC_1626,(0,2):C.GC_1620,(2,2):C.GC_1632})

V_950 = Vertex(name = 'V_950',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1463,(1,0):C.GC_1504,(3,0):C.GC_1516,(0,3):C.GC_1510,(2,3):C.GC_1522,(1,1):C.GC_1617,(3,1):C.GC_1629,(0,2):C.GC_1623,(2,2):C.GC_1635})

V_951 = Vertex(name = 'V_951',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2060,(0,5):C.GC_2069,(1,0):C.GC_2202,(3,0):C.GC_2214,(0,3):C.GC_2208,(2,3):C.GC_2220,(1,1):C.GC_2179,(3,1):C.GC_2191,(0,2):C.GC_2185,(2,2):C.GC_2197})

V_952 = Vertex(name = 'V_952',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2078,(1,0):C.GC_2205,(3,0):C.GC_2217,(0,3):C.GC_2211,(2,3):C.GC_2223,(1,1):C.GC_2182,(3,1):C.GC_2194,(0,2):C.GC_2188,(2,2):C.GC_2200})

V_953 = Vertex(name = 'V_953',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2675,(0,5):C.GC_2684,(1,0):C.GC_2759,(3,0):C.GC_2781,(0,3):C.GC_2770,(2,3):C.GC_2792,(1,1):C.GC_2819,(3,1):C.GC_2831,(0,2):C.GC_2825,(2,2):C.GC_2837})

V_954 = Vertex(name = 'V_954',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2693,(1,0):C.GC_2764,(3,0):C.GC_2786,(0,3):C.GC_2775,(2,3):C.GC_2797,(1,1):C.GC_2822,(3,1):C.GC_2834,(0,2):C.GC_2828,(2,2):C.GC_2840})

V_955 = Vertex(name = 'V_955',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1440,(0,5):C.GC_1449,(1,0):C.GC_1553,(3,0):C.GC_1575,(0,3):C.GC_1564,(2,3):C.GC_1586,(1,1):C.GC_1526,(3,1):C.GC_1538,(0,2):C.GC_1532,(2,2):C.GC_1544})

V_956 = Vertex(name = 'V_956',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1458,(1,0):C.GC_1558,(3,0):C.GC_1580,(0,3):C.GC_1569,(2,3):C.GC_1591,(1,1):C.GC_1529,(3,1):C.GC_1541,(0,2):C.GC_1535,(2,2):C.GC_1547})

V_957 = Vertex(name = 'V_957',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2055,(0,5):C.GC_2064,(1,0):C.GC_2235,(3,0):C.GC_2247,(0,3):C.GC_2241,(2,3):C.GC_2253,(1,1):C.GC_2087,(3,1):C.GC_2099,(0,2):C.GC_2093,(2,2):C.GC_2105})

V_958 = Vertex(name = 'V_958',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2073,(1,0):C.GC_2238,(3,0):C.GC_2250,(0,3):C.GC_2244,(2,3):C.GC_2256,(1,1):C.GC_2090,(3,1):C.GC_2102,(0,2):C.GC_2096,(2,2):C.GC_2108})

V_959 = Vertex(name = 'V_959',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2670,(0,5):C.GC_2679,(1,0):C.GC_2851,(3,0):C.GC_2863,(0,3):C.GC_2857,(2,3):C.GC_2869,(1,1):C.GC_2731,(3,1):C.GC_2743,(0,2):C.GC_2737,(2,2):C.GC_2749})

V_960 = Vertex(name = 'V_960',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2688,(1,0):C.GC_2854,(3,0):C.GC_2866,(0,3):C.GC_2860,(2,3):C.GC_2872,(1,1):C.GC_2734,(3,1):C.GC_2746,(0,2):C.GC_2740,(2,2):C.GC_2752})

V_961 = Vertex(name = 'V_961',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1443,(0,5):C.GC_1452,(1,0):C.GC_1474,(3,0):C.GC_1486,(0,3):C.GC_1480,(2,3):C.GC_1492,(1,1):C.GC_1527,(3,1):C.GC_1539,(0,2):C.GC_1533,(2,2):C.GC_1545})

V_962 = Vertex(name = 'V_962',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1461,(1,0):C.GC_1477,(3,0):C.GC_1489,(0,3):C.GC_1483,(2,3):C.GC_1495,(1,1):C.GC_1530,(3,1):C.GC_1542,(0,2):C.GC_1536,(2,2):C.GC_1548})

V_963 = Vertex(name = 'V_963',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2058,(0,5):C.GC_2067,(1,0):C.GC_2115,(3,0):C.GC_2137,(0,3):C.GC_2126,(2,3):C.GC_2148,(1,1):C.GC_2088,(3,1):C.GC_2100,(0,2):C.GC_2094,(2,2):C.GC_2106})

V_964 = Vertex(name = 'V_964',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2076,(1,0):C.GC_2120,(3,0):C.GC_2142,(0,3):C.GC_2131,(2,3):C.GC_2153,(1,1):C.GC_2091,(3,1):C.GC_2103,(0,2):C.GC_2097,(2,2):C.GC_2109})

V_965 = Vertex(name = 'V_965',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2673,(0,5):C.GC_2682,(1,0):C.GC_2705,(3,0):C.GC_2717,(0,3):C.GC_2711,(2,3):C.GC_2723,(1,1):C.GC_2732,(3,1):C.GC_2744,(0,2):C.GC_2738,(2,2):C.GC_2750})

V_966 = Vertex(name = 'V_966',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2691,(1,0):C.GC_2708,(3,0):C.GC_2720,(0,3):C.GC_2714,(2,3):C.GC_2726,(1,1):C.GC_2735,(3,1):C.GC_2747,(0,2):C.GC_2741,(2,2):C.GC_2753})

V_967 = Vertex(name = 'V_967',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1446,(0,5):C.GC_1455,(1,0):C.GC_1502,(3,0):C.GC_1514,(0,3):C.GC_1508,(2,3):C.GC_1520,(1,1):C.GC_1528,(3,1):C.GC_1540,(0,2):C.GC_1534,(2,2):C.GC_1546})

V_968 = Vertex(name = 'V_968',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1464,(1,0):C.GC_1505,(3,0):C.GC_1517,(0,3):C.GC_1511,(2,3):C.GC_1523,(1,1):C.GC_1531,(3,1):C.GC_1543,(0,2):C.GC_1537,(2,2):C.GC_1549})

V_969 = Vertex(name = 'V_969',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2061,(0,5):C.GC_2070,(1,0):C.GC_2203,(3,0):C.GC_2215,(0,3):C.GC_2209,(2,3):C.GC_2221,(1,1):C.GC_2089,(3,1):C.GC_2101,(0,2):C.GC_2095,(2,2):C.GC_2107})

V_970 = Vertex(name = 'V_970',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2079,(1,0):C.GC_2206,(3,0):C.GC_2218,(0,3):C.GC_2212,(2,3):C.GC_2224,(1,1):C.GC_2092,(3,1):C.GC_2104,(0,2):C.GC_2098,(2,2):C.GC_2110})

V_971 = Vertex(name = 'V_971',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2676,(0,5):C.GC_2685,(1,0):C.GC_2760,(3,0):C.GC_2782,(0,3):C.GC_2771,(2,3):C.GC_2793,(1,1):C.GC_2733,(3,1):C.GC_2745,(0,2):C.GC_2739,(2,2):C.GC_2751})

V_972 = Vertex(name = 'V_972',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2694,(1,0):C.GC_2765,(3,0):C.GC_2787,(0,3):C.GC_2776,(2,3):C.GC_2798,(1,1):C.GC_2736,(3,1):C.GC_2748,(0,2):C.GC_2742,(2,2):C.GC_2754})

V_973 = Vertex(name = 'V_973',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1643,(0,5):C.GC_1652,(1,0):C.GC_1791,(3,0):C.GC_1813,(0,3):C.GC_1802,(2,3):C.GC_1824,(1,1):C.GC_1755,(3,1):C.GC_1767,(0,2):C.GC_1761,(2,2):C.GC_1773})

V_974 = Vertex(name = 'V_974',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1661,(1,0):C.GC_1797,(3,0):C.GC_1819,(0,3):C.GC_1808,(2,3):C.GC_1830,(1,1):C.GC_1758,(3,1):C.GC_1770,(0,2):C.GC_1764,(2,2):C.GC_1776})

V_975 = Vertex(name = 'V_975',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2258,(0,5):C.GC_2267,(1,0):C.GC_2438,(3,0):C.GC_2450,(0,3):C.GC_2444,(2,3):C.GC_2456,(1,1):C.GC_2316,(3,1):C.GC_2328,(0,2):C.GC_2322,(2,2):C.GC_2334})

V_976 = Vertex(name = 'V_976',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2276,(1,0):C.GC_2441,(3,0):C.GC_2453,(0,3):C.GC_2447,(2,3):C.GC_2459,(1,1):C.GC_2319,(3,1):C.GC_2331,(0,2):C.GC_2325,(2,2):C.GC_2337})

V_977 = Vertex(name = 'V_977',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2874,(0,5):C.GC_2883,(1,0):C.GC_3055,(3,0):C.GC_3067,(0,3):C.GC_3061,(2,3):C.GC_3073,(1,1):C.GC_2961,(3,1):C.GC_2973,(0,2):C.GC_2967,(2,2):C.GC_2979})

V_978 = Vertex(name = 'V_978',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2892,(1,0):C.GC_3058,(3,0):C.GC_3070,(0,3):C.GC_3064,(2,3):C.GC_3076,(1,1):C.GC_2964,(3,1):C.GC_2976,(0,2):C.GC_2970,(2,2):C.GC_2982})

V_979 = Vertex(name = 'V_979',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1646,(0,5):C.GC_1655,(1,0):C.GC_1677,(3,0):C.GC_1689,(0,3):C.GC_1683,(2,3):C.GC_1695,(1,1):C.GC_1756,(3,1):C.GC_1768,(0,2):C.GC_1762,(2,2):C.GC_1774})

V_980 = Vertex(name = 'V_980',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1664,(1,0):C.GC_1680,(3,0):C.GC_1692,(0,3):C.GC_1686,(2,3):C.GC_1698,(1,1):C.GC_1759,(3,1):C.GC_1771,(0,2):C.GC_1765,(2,2):C.GC_1777})

V_981 = Vertex(name = 'V_981',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2261,(0,5):C.GC_2270,(1,0):C.GC_2353,(3,0):C.GC_2375,(0,3):C.GC_2364,(2,3):C.GC_2386,(1,1):C.GC_2317,(3,1):C.GC_2329,(0,2):C.GC_2323,(2,2):C.GC_2335})

V_982 = Vertex(name = 'V_982',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2279,(1,0):C.GC_2359,(3,0):C.GC_2381,(0,3):C.GC_2370,(2,3):C.GC_2392,(1,1):C.GC_2320,(3,1):C.GC_2332,(0,2):C.GC_2326,(2,2):C.GC_2338})

V_983 = Vertex(name = 'V_983',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2877,(0,5):C.GC_2886,(1,0):C.GC_2909,(3,0):C.GC_2921,(0,3):C.GC_2915,(2,3):C.GC_2927,(1,1):C.GC_2962,(3,1):C.GC_2974,(0,2):C.GC_2968,(2,2):C.GC_2980})

V_984 = Vertex(name = 'V_984',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2895,(1,0):C.GC_2912,(3,0):C.GC_2924,(0,3):C.GC_2918,(2,3):C.GC_2930,(1,1):C.GC_2965,(3,1):C.GC_2977,(0,2):C.GC_2971,(2,2):C.GC_2983})

V_985 = Vertex(name = 'V_985',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1649,(0,5):C.GC_1658,(1,0):C.GC_1705,(3,0):C.GC_1717,(0,3):C.GC_1711,(2,3):C.GC_1723,(1,1):C.GC_1757,(3,1):C.GC_1769,(0,2):C.GC_1763,(2,2):C.GC_1775})

V_986 = Vertex(name = 'V_986',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1667,(1,0):C.GC_1708,(3,0):C.GC_1720,(0,3):C.GC_1714,(2,3):C.GC_1726,(1,1):C.GC_1760,(3,1):C.GC_1772,(0,2):C.GC_1766,(2,2):C.GC_1778})

V_987 = Vertex(name = 'V_987',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2264,(0,5):C.GC_2273,(1,0):C.GC_2406,(3,0):C.GC_2418,(0,3):C.GC_2412,(2,3):C.GC_2424,(1,1):C.GC_2318,(3,1):C.GC_2330,(0,2):C.GC_2324,(2,2):C.GC_2336})

V_988 = Vertex(name = 'V_988',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2282,(1,0):C.GC_2409,(3,0):C.GC_2421,(0,3):C.GC_2415,(2,3):C.GC_2427,(1,1):C.GC_2321,(3,1):C.GC_2333,(0,2):C.GC_2327,(2,2):C.GC_2339})

V_989 = Vertex(name = 'V_989',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2880,(0,5):C.GC_2889,(1,0):C.GC_2999,(3,0):C.GC_3021,(0,3):C.GC_3010,(2,3):C.GC_3032,(1,1):C.GC_2963,(3,1):C.GC_2975,(0,2):C.GC_2969,(2,2):C.GC_2981})

V_990 = Vertex(name = 'V_990',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2898,(1,0):C.GC_3005,(3,0):C.GC_3027,(0,3):C.GC_3016,(2,3):C.GC_3038,(1,1):C.GC_2966,(3,1):C.GC_2978,(0,2):C.GC_2972,(2,2):C.GC_2984})

V_991 = Vertex(name = 'V_991',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1396,(3,0):C.GC_1402,(0,6):C.GC_1392,(2,6):C.GC_1398,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1395,(3,1):C.GC_1401,(0,2):C.GC_1393,(2,2):C.GC_1399})

V_992 = Vertex(name = 'V_992',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_46,(0,5):C.GC_1653,(1,0):C.GC_1397,(3,0):C.GC_1403,(0,3):C.GC_1394,(2,3):C.GC_1400,(1,1):C.GC_1397,(3,1):C.GC_1403,(0,2):C.GC_1394,(2,2):C.GC_1400})

V_993 = Vertex(name = 'V_993',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1644,(1,0):C.GC_1793,(3,0):C.GC_1815,(0,3):C.GC_1803,(2,3):C.GC_1825,(1,1):C.GC_1792,(3,1):C.GC_1814,(0,2):C.GC_1804,(2,2):C.GC_1826})

V_994 = Vertex(name = 'V_994',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_1662,(1,0):C.GC_1798,(3,0):C.GC_1820,(0,3):C.GC_1809,(2,3):C.GC_1831,(1,1):C.GC_1798,(3,1):C.GC_1820,(0,2):C.GC_1809,(2,2):C.GC_1831})

V_995 = Vertex(name = 'V_995',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2259,(0,5):C.GC_2268,(1,0):C.GC_2439,(3,0):C.GC_2451,(0,3):C.GC_2445,(2,3):C.GC_2457,(1,1):C.GC_2352,(3,1):C.GC_2374,(0,2):C.GC_2363,(2,2):C.GC_2385})

V_996 = Vertex(name = 'V_996',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2277,(1,0):C.GC_2442,(3,0):C.GC_2454,(0,3):C.GC_2448,(2,3):C.GC_2460,(1,1):C.GC_2358,(3,1):C.GC_2380,(0,2):C.GC_2369,(2,2):C.GC_2391})

V_997 = Vertex(name = 'V_997',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_2875,(0,5):C.GC_2884,(1,0):C.GC_3056,(3,0):C.GC_3068,(0,3):C.GC_3062,(2,3):C.GC_3074,(1,1):C.GC_2997,(3,1):C.GC_3019,(0,2):C.GC_3008,(2,2):C.GC_3030})

V_998 = Vertex(name = 'V_998',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_2893,(1,0):C.GC_3059,(3,0):C.GC_3071,(0,3):C.GC_3065,(2,3):C.GC_3077,(1,1):C.GC_3003,(3,1):C.GC_3025,(0,2):C.GC_3014,(2,2):C.GC_3036})

V_999 = Vertex(name = 'V_999',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_1647,(0,5):C.GC_1656,(1,0):C.GC_1678,(3,0):C.GC_1690,(0,3):C.GC_1684,(2,3):C.GC_1696,(1,1):C.GC_1795,(3,1):C.GC_1817,(0,2):C.GC_1806,(2,2):C.GC_1828})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1665,(1,0):C.GC_1681,(3,0):C.GC_1693,(0,3):C.GC_1687,(2,3):C.GC_1699,(1,1):C.GC_1800,(3,1):C.GC_1822,(0,2):C.GC_1811,(2,2):C.GC_1833})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_913,(3,0):C.GC_919,(0,6):C.GC_909,(2,6):C.GC_915,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_912,(3,1):C.GC_918,(0,2):C.GC_910,(2,2):C.GC_916})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_46,(0,5):C.GC_2271,(1,0):C.GC_914,(3,0):C.GC_920,(0,3):C.GC_911,(2,3):C.GC_917,(1,1):C.GC_914,(3,1):C.GC_920,(0,2):C.GC_911,(2,2):C.GC_917})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2262,(1,0):C.GC_2355,(3,0):C.GC_2377,(0,3):C.GC_2365,(2,3):C.GC_2387,(1,1):C.GC_2354,(3,1):C.GC_2376,(0,2):C.GC_2366,(2,2):C.GC_2388})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2280,(1,0):C.GC_2360,(3,0):C.GC_2382,(0,3):C.GC_2371,(2,3):C.GC_2393,(1,1):C.GC_2360,(3,1):C.GC_2382,(0,2):C.GC_2371,(2,2):C.GC_2393})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2878,(0,5):C.GC_2887,(1,0):C.GC_2910,(3,0):C.GC_2922,(0,3):C.GC_2916,(2,3):C.GC_2928,(1,1):C.GC_2998,(3,1):C.GC_3020,(0,2):C.GC_3009,(2,2):C.GC_3031})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2896,(1,0):C.GC_2913,(3,0):C.GC_2925,(0,3):C.GC_2919,(2,3):C.GC_2931,(1,1):C.GC_3004,(3,1):C.GC_3026,(0,2):C.GC_3015,(2,2):C.GC_3037})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1650,(0,5):C.GC_1659,(1,0):C.GC_1706,(3,0):C.GC_1718,(0,3):C.GC_1712,(2,3):C.GC_1724,(1,1):C.GC_1796,(3,1):C.GC_1818,(0,2):C.GC_1807,(2,2):C.GC_1829})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1668,(1,0):C.GC_1709,(3,0):C.GC_1721,(0,3):C.GC_1715,(2,3):C.GC_1727,(1,1):C.GC_1801,(3,1):C.GC_1823,(0,2):C.GC_1812,(2,2):C.GC_1834})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2265,(0,5):C.GC_2274,(1,0):C.GC_2407,(3,0):C.GC_2419,(0,3):C.GC_2413,(2,3):C.GC_2425,(1,1):C.GC_2357,(3,1):C.GC_2379,(0,2):C.GC_2368,(2,2):C.GC_2390})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2283,(1,0):C.GC_2410,(3,0):C.GC_2422,(0,3):C.GC_2416,(2,3):C.GC_2428,(1,1):C.GC_2362,(3,1):C.GC_2384,(0,2):C.GC_2373,(2,2):C.GC_2395})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1099,(3,0):C.GC_1105,(0,6):C.GC_1095,(2,6):C.GC_1101,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1098,(3,1):C.GC_1104,(0,2):C.GC_1096,(2,2):C.GC_1102})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_46,(0,5):C.GC_2890,(1,0):C.GC_1100,(3,0):C.GC_1106,(0,3):C.GC_1097,(2,3):C.GC_1103,(1,1):C.GC_1100,(3,1):C.GC_1106,(0,2):C.GC_1097,(2,2):C.GC_1103})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2881,(1,0):C.GC_3001,(3,0):C.GC_3023,(0,3):C.GC_3011,(2,3):C.GC_3033,(1,1):C.GC_3000,(3,1):C.GC_3022,(0,2):C.GC_3012,(2,2):C.GC_3034})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2899,(1,0):C.GC_3006,(3,0):C.GC_3028,(0,3):C.GC_3017,(2,3):C.GC_3039,(1,1):C.GC_3006,(3,1):C.GC_3028,(0,2):C.GC_3017,(2,2):C.GC_3039})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1645,(0,5):C.GC_1654,(1,0):C.GC_1794,(3,0):C.GC_1816,(0,3):C.GC_1805,(2,3):C.GC_1827,(1,1):C.GC_1731,(3,1):C.GC_1743,(0,2):C.GC_1737,(2,2):C.GC_1749})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1663,(1,0):C.GC_1799,(3,0):C.GC_1821,(0,3):C.GC_1810,(2,3):C.GC_1832,(1,1):C.GC_1734,(3,1):C.GC_1746,(0,2):C.GC_1740,(2,2):C.GC_1752})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2260,(0,5):C.GC_2269,(1,0):C.GC_2440,(3,0):C.GC_2452,(0,3):C.GC_2446,(2,3):C.GC_2458,(1,1):C.GC_2292,(3,1):C.GC_2304,(0,2):C.GC_2298,(2,2):C.GC_2310})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2278,(1,0):C.GC_2443,(3,0):C.GC_2455,(0,3):C.GC_2449,(2,3):C.GC_2461,(1,1):C.GC_2295,(3,1):C.GC_2307,(0,2):C.GC_2301,(2,2):C.GC_2313})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2876,(0,5):C.GC_2885,(1,0):C.GC_3057,(3,0):C.GC_3069,(0,3):C.GC_3063,(2,3):C.GC_3075,(1,1):C.GC_2937,(3,1):C.GC_2949,(0,2):C.GC_2943,(2,2):C.GC_2955})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2894,(1,0):C.GC_3060,(3,0):C.GC_3072,(0,3):C.GC_3066,(2,3):C.GC_3078,(1,1):C.GC_2940,(3,1):C.GC_2952,(0,2):C.GC_2946,(2,2):C.GC_2958})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1648,(0,5):C.GC_1657,(1,0):C.GC_1679,(3,0):C.GC_1691,(0,3):C.GC_1685,(2,3):C.GC_1697,(1,1):C.GC_1732,(3,1):C.GC_1744,(0,2):C.GC_1738,(2,2):C.GC_1750})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1666,(1,0):C.GC_1682,(3,0):C.GC_1694,(0,3):C.GC_1688,(2,3):C.GC_1700,(1,1):C.GC_1735,(3,1):C.GC_1747,(0,2):C.GC_1741,(2,2):C.GC_1753})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2263,(0,5):C.GC_2272,(1,0):C.GC_2356,(3,0):C.GC_2378,(0,3):C.GC_2367,(2,3):C.GC_2389,(1,1):C.GC_2293,(3,1):C.GC_2305,(0,2):C.GC_2299,(2,2):C.GC_2311})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2281,(1,0):C.GC_2361,(3,0):C.GC_2383,(0,3):C.GC_2372,(2,3):C.GC_2394,(1,1):C.GC_2296,(3,1):C.GC_2308,(0,2):C.GC_2302,(2,2):C.GC_2314})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2879,(0,5):C.GC_2888,(1,0):C.GC_2911,(3,0):C.GC_2923,(0,3):C.GC_2917,(2,3):C.GC_2929,(1,1):C.GC_2938,(3,1):C.GC_2950,(0,2):C.GC_2944,(2,2):C.GC_2956})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2897,(1,0):C.GC_2914,(3,0):C.GC_2926,(0,3):C.GC_2920,(2,3):C.GC_2932,(1,1):C.GC_2941,(3,1):C.GC_2953,(0,2):C.GC_2947,(2,2):C.GC_2959})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1651,(0,5):C.GC_1660,(1,0):C.GC_1707,(3,0):C.GC_1719,(0,3):C.GC_1713,(2,3):C.GC_1725,(1,1):C.GC_1733,(3,1):C.GC_1745,(0,2):C.GC_1739,(2,2):C.GC_1751})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1669,(1,0):C.GC_1710,(3,0):C.GC_1722,(0,3):C.GC_1716,(2,3):C.GC_1728,(1,1):C.GC_1736,(3,1):C.GC_1748,(0,2):C.GC_1742,(2,2):C.GC_1754})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2266,(0,5):C.GC_2275,(1,0):C.GC_2408,(3,0):C.GC_2420,(0,3):C.GC_2414,(2,3):C.GC_2426,(1,1):C.GC_2294,(3,1):C.GC_2306,(0,2):C.GC_2300,(2,2):C.GC_2312})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2284,(1,0):C.GC_2411,(3,0):C.GC_2423,(0,3):C.GC_2417,(2,3):C.GC_2429,(1,1):C.GC_2297,(3,1):C.GC_2309,(0,2):C.GC_2303,(2,2):C.GC_2315})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2882,(0,5):C.GC_2891,(1,0):C.GC_3002,(3,0):C.GC_3024,(0,3):C.GC_3013,(2,3):C.GC_3035,(1,1):C.GC_2939,(3,1):C.GC_2951,(0,2):C.GC_2945,(2,2):C.GC_2957})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2900,(1,0):C.GC_3007,(3,0):C.GC_3029,(0,3):C.GC_3018,(2,3):C.GC_3040,(1,1):C.GC_2942,(3,1):C.GC_2954,(0,2):C.GC_2948,(2,2):C.GC_2960})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1848,(0,5):C.GC_1857,(1,0):C.GC_1936,(3,0):C.GC_1958,(0,3):C.GC_1947,(2,3):C.GC_1969,(1,1):C.GC_1986,(3,1):C.GC_1998,(0,2):C.GC_1992,(2,2):C.GC_2004})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1866,(1,0):C.GC_1942,(3,0):C.GC_1964,(0,3):C.GC_1953,(2,3):C.GC_1975,(1,1):C.GC_1989,(3,1):C.GC_2001,(0,2):C.GC_1995,(2,2):C.GC_2007})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2463,(0,5):C.GC_2472,(1,0):C.GC_2643,(3,0):C.GC_2655,(0,3):C.GC_2649,(2,3):C.GC_2661,(1,1):C.GC_2547,(3,1):C.GC_2559,(0,2):C.GC_2553,(2,2):C.GC_2565})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2481,(1,0):C.GC_2646,(3,0):C.GC_2658,(0,3):C.GC_2652,(2,3):C.GC_2664,(1,1):C.GC_2550,(3,1):C.GC_2562,(0,2):C.GC_2556,(2,2):C.GC_2568})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3080,(0,5):C.GC_3089,(1,0):C.GC_3261,(3,0):C.GC_3273,(0,3):C.GC_3267,(2,3):C.GC_3279,(1,1):C.GC_3193,(3,1):C.GC_3205,(0,2):C.GC_3199,(2,2):C.GC_3211})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3098,(1,0):C.GC_3264,(3,0):C.GC_3276,(0,3):C.GC_3270,(2,3):C.GC_3282,(1,1):C.GC_3196,(3,1):C.GC_3208,(0,2):C.GC_3202,(2,2):C.GC_3214})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1851,(0,5):C.GC_1860,(1,0):C.GC_1882,(3,0):C.GC_1894,(0,3):C.GC_1888,(2,3):C.GC_1900,(1,1):C.GC_1987,(3,1):C.GC_1999,(0,2):C.GC_1993,(2,2):C.GC_2005})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1869,(1,0):C.GC_1885,(3,0):C.GC_1897,(0,3):C.GC_1891,(2,3):C.GC_1903,(1,1):C.GC_1990,(3,1):C.GC_2002,(0,2):C.GC_1996,(2,2):C.GC_2008})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2466,(0,5):C.GC_2475,(1,0):C.GC_2498,(3,0):C.GC_2520,(0,3):C.GC_2509,(2,3):C.GC_2531,(1,1):C.GC_2548,(3,1):C.GC_2560,(0,2):C.GC_2554,(2,2):C.GC_2566})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2484,(1,0):C.GC_2504,(3,0):C.GC_2526,(0,3):C.GC_2515,(2,3):C.GC_2537,(1,1):C.GC_2551,(3,1):C.GC_2563,(0,2):C.GC_2557,(2,2):C.GC_2569})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3083,(0,5):C.GC_3092,(1,0):C.GC_3115,(3,0):C.GC_3127,(0,3):C.GC_3121,(2,3):C.GC_3133,(1,1):C.GC_3194,(3,1):C.GC_3206,(0,2):C.GC_3200,(2,2):C.GC_3212})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3101,(1,0):C.GC_3118,(3,0):C.GC_3130,(0,3):C.GC_3124,(2,3):C.GC_3136,(1,1):C.GC_3197,(3,1):C.GC_3209,(0,2):C.GC_3203,(2,2):C.GC_3215})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1854,(0,5):C.GC_1863,(1,0):C.GC_1910,(3,0):C.GC_1922,(0,3):C.GC_1916,(2,3):C.GC_1928,(1,1):C.GC_1988,(3,1):C.GC_2000,(0,2):C.GC_1994,(2,2):C.GC_2006})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1872,(1,0):C.GC_1913,(3,0):C.GC_1925,(0,3):C.GC_1919,(2,3):C.GC_1931,(1,1):C.GC_1991,(3,1):C.GC_2003,(0,2):C.GC_1997,(2,2):C.GC_2009})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2469,(0,5):C.GC_2478,(1,0):C.GC_2611,(3,0):C.GC_2623,(0,3):C.GC_2617,(2,3):C.GC_2629,(1,1):C.GC_2549,(3,1):C.GC_2561,(0,2):C.GC_2555,(2,2):C.GC_2567})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2487,(1,0):C.GC_2614,(3,0):C.GC_2626,(0,3):C.GC_2620,(2,3):C.GC_2632,(1,1):C.GC_2552,(3,1):C.GC_2564,(0,2):C.GC_2558,(2,2):C.GC_2570})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3086,(0,5):C.GC_3095,(1,0):C.GC_3145,(3,0):C.GC_3167,(0,3):C.GC_3156,(2,3):C.GC_3178,(1,1):C.GC_3195,(3,1):C.GC_3207,(0,2):C.GC_3201,(2,2):C.GC_3213})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3104,(1,0):C.GC_3151,(3,0):C.GC_3173,(0,3):C.GC_3162,(2,3):C.GC_3184,(1,1):C.GC_3198,(3,1):C.GC_3210,(0,2):C.GC_3204,(2,2):C.GC_3216})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1849,(0,5):C.GC_1858,(1,0):C.GC_1937,(3,0):C.GC_1959,(0,3):C.GC_1948,(2,3):C.GC_1970,(1,1):C.GC_2022,(3,1):C.GC_2034,(0,2):C.GC_2028,(2,2):C.GC_2040})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1867,(1,0):C.GC_1943,(3,0):C.GC_1965,(0,3):C.GC_1954,(2,3):C.GC_1976,(1,1):C.GC_2025,(3,1):C.GC_2037,(0,2):C.GC_2031,(2,2):C.GC_2043})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2464,(0,5):C.GC_2473,(1,0):C.GC_2644,(3,0):C.GC_2656,(0,3):C.GC_2650,(2,3):C.GC_2662,(1,1):C.GC_2587,(3,1):C.GC_2599,(0,2):C.GC_2593,(2,2):C.GC_2605})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2482,(1,0):C.GC_2647,(3,0):C.GC_2659,(0,3):C.GC_2653,(2,3):C.GC_2665,(1,1):C.GC_2590,(3,1):C.GC_2602,(0,2):C.GC_2596,(2,2):C.GC_2608})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3081,(0,5):C.GC_3090,(1,0):C.GC_3262,(3,0):C.GC_3274,(0,3):C.GC_3268,(2,3):C.GC_3280,(1,1):C.GC_3229,(3,1):C.GC_3241,(0,2):C.GC_3235,(2,2):C.GC_3247})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3099,(1,0):C.GC_3265,(3,0):C.GC_3277,(0,3):C.GC_3271,(2,3):C.GC_3283,(1,1):C.GC_3232,(3,1):C.GC_3244,(0,2):C.GC_3238,(2,2):C.GC_3250})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1852,(0,5):C.GC_1861,(1,0):C.GC_1883,(3,0):C.GC_1895,(0,3):C.GC_1889,(2,3):C.GC_1901,(1,1):C.GC_2023,(3,1):C.GC_2035,(0,2):C.GC_2029,(2,2):C.GC_2041})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1870,(1,0):C.GC_1886,(3,0):C.GC_1898,(0,3):C.GC_1892,(2,3):C.GC_1904,(1,1):C.GC_2026,(3,1):C.GC_2038,(0,2):C.GC_2032,(2,2):C.GC_2044})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2467,(0,5):C.GC_2476,(1,0):C.GC_2499,(3,0):C.GC_2521,(0,3):C.GC_2510,(2,3):C.GC_2532,(1,1):C.GC_2588,(3,1):C.GC_2600,(0,2):C.GC_2594,(2,2):C.GC_2606})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2485,(1,0):C.GC_2505,(3,0):C.GC_2527,(0,3):C.GC_2516,(2,3):C.GC_2538,(1,1):C.GC_2591,(3,1):C.GC_2603,(0,2):C.GC_2597,(2,2):C.GC_2609})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3084,(0,5):C.GC_3093,(1,0):C.GC_3116,(3,0):C.GC_3128,(0,3):C.GC_3122,(2,3):C.GC_3134,(1,1):C.GC_3230,(3,1):C.GC_3242,(0,2):C.GC_3236,(2,2):C.GC_3248})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3102,(1,0):C.GC_3119,(3,0):C.GC_3131,(0,3):C.GC_3125,(2,3):C.GC_3137,(1,1):C.GC_3233,(3,1):C.GC_3245,(0,2):C.GC_3239,(2,2):C.GC_3251})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1855,(0,5):C.GC_1864,(1,0):C.GC_1911,(3,0):C.GC_1923,(0,3):C.GC_1917,(2,3):C.GC_1929,(1,1):C.GC_2024,(3,1):C.GC_2036,(0,2):C.GC_2030,(2,2):C.GC_2042})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1873,(1,0):C.GC_1914,(3,0):C.GC_1926,(0,3):C.GC_1920,(2,3):C.GC_1932,(1,1):C.GC_2027,(3,1):C.GC_2039,(0,2):C.GC_2033,(2,2):C.GC_2045})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2470,(0,5):C.GC_2479,(1,0):C.GC_2612,(3,0):C.GC_2624,(0,3):C.GC_2618,(2,3):C.GC_2630,(1,1):C.GC_2589,(3,1):C.GC_2601,(0,2):C.GC_2595,(2,2):C.GC_2607})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2488,(1,0):C.GC_2615,(3,0):C.GC_2627,(0,3):C.GC_2621,(2,3):C.GC_2633,(1,1):C.GC_2592,(3,1):C.GC_2604,(0,2):C.GC_2598,(2,2):C.GC_2610})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3087,(0,5):C.GC_3096,(1,0):C.GC_3146,(3,0):C.GC_3168,(0,3):C.GC_3157,(2,3):C.GC_3179,(1,1):C.GC_3231,(3,1):C.GC_3243,(0,2):C.GC_3237,(2,2):C.GC_3249})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3105,(1,0):C.GC_3152,(3,0):C.GC_3174,(0,3):C.GC_3163,(2,3):C.GC_3185,(1,1):C.GC_3234,(3,1):C.GC_3246,(0,2):C.GC_3240,(2,2):C.GC_3252})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1306,(3,0):C.GC_1312,(0,6):C.GC_1302,(2,6):C.GC_1308,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1305,(3,1):C.GC_1311,(0,2):C.GC_1303,(2,2):C.GC_1309})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_46,(0,5):C.GC_1859,(1,0):C.GC_1307,(3,0):C.GC_1313,(0,3):C.GC_1304,(2,3):C.GC_1310,(1,1):C.GC_1307,(3,1):C.GC_1313,(0,2):C.GC_1304,(2,2):C.GC_1310})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1850,(1,0):C.GC_1939,(3,0):C.GC_1961,(0,3):C.GC_1949,(2,3):C.GC_1971,(1,1):C.GC_1938,(3,1):C.GC_1960,(0,2):C.GC_1950,(2,2):C.GC_1972})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1868,(1,0):C.GC_1944,(3,0):C.GC_1966,(0,3):C.GC_1955,(2,3):C.GC_1977,(1,1):C.GC_1944,(3,1):C.GC_1966,(0,2):C.GC_1955,(2,2):C.GC_1977})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2465,(0,5):C.GC_2474,(1,0):C.GC_2645,(3,0):C.GC_2657,(0,3):C.GC_2651,(2,3):C.GC_2663,(1,1):C.GC_2497,(3,1):C.GC_2519,(0,2):C.GC_2508,(2,2):C.GC_2530})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2483,(1,0):C.GC_2648,(3,0):C.GC_2660,(0,3):C.GC_2654,(2,3):C.GC_2666,(1,1):C.GC_2503,(3,1):C.GC_2525,(0,2):C.GC_2514,(2,2):C.GC_2536})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3082,(0,5):C.GC_3091,(1,0):C.GC_3263,(3,0):C.GC_3275,(0,3):C.GC_3269,(2,3):C.GC_3281,(1,1):C.GC_3143,(3,1):C.GC_3165,(0,2):C.GC_3154,(2,2):C.GC_3176})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3100,(1,0):C.GC_3266,(3,0):C.GC_3278,(0,3):C.GC_3272,(2,3):C.GC_3284,(1,1):C.GC_3149,(3,1):C.GC_3171,(0,2):C.GC_3160,(2,2):C.GC_3182})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1853,(0,5):C.GC_1862,(1,0):C.GC_1884,(3,0):C.GC_1896,(0,3):C.GC_1890,(2,3):C.GC_1902,(1,1):C.GC_1940,(3,1):C.GC_1962,(0,2):C.GC_1951,(2,2):C.GC_1973})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1871,(1,0):C.GC_1887,(3,0):C.GC_1899,(0,3):C.GC_1893,(2,3):C.GC_1905,(1,1):C.GC_1945,(3,1):C.GC_1967,(0,2):C.GC_1956,(2,2):C.GC_1978})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_571,(3,0):C.GC_577,(0,6):C.GC_567,(2,6):C.GC_573,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_570,(3,1):C.GC_576,(0,2):C.GC_568,(2,2):C.GC_574})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_46,(0,5):C.GC_2477,(1,0):C.GC_572,(3,0):C.GC_578,(0,3):C.GC_569,(2,3):C.GC_575,(1,1):C.GC_572,(3,1):C.GC_578,(0,2):C.GC_569,(2,2):C.GC_575})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2468,(1,0):C.GC_2501,(3,0):C.GC_2523,(0,3):C.GC_2511,(2,3):C.GC_2533,(1,1):C.GC_2500,(3,1):C.GC_2522,(0,2):C.GC_2512,(2,2):C.GC_2534})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2486,(1,0):C.GC_2506,(3,0):C.GC_2528,(0,3):C.GC_2517,(2,3):C.GC_2539,(1,1):C.GC_2506,(3,1):C.GC_2528,(0,2):C.GC_2517,(2,2):C.GC_2539})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3085,(0,5):C.GC_3094,(1,0):C.GC_3117,(3,0):C.GC_3129,(0,3):C.GC_3123,(2,3):C.GC_3135,(1,1):C.GC_3144,(3,1):C.GC_3166,(0,2):C.GC_3155,(2,2):C.GC_3177})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3103,(1,0):C.GC_3120,(3,0):C.GC_3132,(0,3):C.GC_3126,(2,3):C.GC_3138,(1,1):C.GC_3150,(3,1):C.GC_3172,(0,2):C.GC_3161,(2,2):C.GC_3183})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_1856,(0,5):C.GC_1865,(1,0):C.GC_1912,(3,0):C.GC_1924,(0,3):C.GC_1918,(2,3):C.GC_1930,(1,1):C.GC_1941,(3,1):C.GC_1963,(0,2):C.GC_1952,(2,2):C.GC_1974})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_1874,(1,0):C.GC_1915,(3,0):C.GC_1927,(0,3):C.GC_1921,(2,3):C.GC_1933,(1,1):C.GC_1946,(3,1):C.GC_1968,(0,2):C.GC_1957,(2,2):C.GC_1979})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2471,(0,5):C.GC_2480,(1,0):C.GC_2613,(3,0):C.GC_2625,(0,3):C.GC_2619,(2,3):C.GC_2631,(1,1):C.GC_2502,(3,1):C.GC_2524,(0,2):C.GC_2513,(2,2):C.GC_2535})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_2489,(1,0):C.GC_2616,(3,0):C.GC_2628,(0,3):C.GC_2622,(2,3):C.GC_2634,(1,1):C.GC_2507,(3,1):C.GC_2529,(0,2):C.GC_2518,(2,2):C.GC_2540})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,7):C.GC_44,(0,8):C.GC_49,(1,0):C.GC_1009,(3,0):C.GC_1015,(0,6):C.GC_1005,(2,6):C.GC_1011,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_50,(3,3):C.GC_51,(1,4):C.GC_56,(3,4):C.GC_57,(1,1):C.GC_1008,(3,1):C.GC_1014,(0,2):C.GC_1006,(2,2):C.GC_1012})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_46,(0,5):C.GC_3097,(1,0):C.GC_1010,(3,0):C.GC_1016,(0,3):C.GC_1007,(2,3):C.GC_1013,(1,1):C.GC_1010,(3,1):C.GC_1016,(0,2):C.GC_1007,(2,2):C.GC_1013})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3088,(1,0):C.GC_3148,(3,0):C.GC_3170,(0,3):C.GC_3158,(2,3):C.GC_3180,(1,1):C.GC_3147,(3,1):C.GC_3169,(0,2):C.GC_3159,(2,2):C.GC_3181})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
                couplings = {(1,4):C.GC_3106,(1,0):C.GC_3153,(3,0):C.GC_3175,(0,3):C.GC_3164,(2,3):C.GC_3186,(1,1):C.GC_3153,(3,1):C.GC_3175,(0,2):C.GC_3164,(2,2):C.GC_3186})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1350,(0,9):C.GC_1348,(0,10):C.GC_1348,(0,5):C.GC_1338,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1347,(0,4):C.GC_1349,(0,6):C.GC_1349,(0,0):C.GC_1339})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1358,(0,6):C.GC_1357,(0,7):C.GC_1357,(0,2):C.GC_1343,(0,4):C.GC_1358,(0,1):C.GC_1357,(0,3):C.GC_1357,(0,0):C.GC_1343})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_732,(0,9):C.GC_730,(0,10):C.GC_730,(0,5):C.GC_720,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_729,(0,4):C.GC_731,(0,6):C.GC_731,(0,0):C.GC_721})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_740,(0,6):C.GC_739,(0,7):C.GC_739,(0,2):C.GC_725,(0,4):C.GC_740,(0,1):C.GC_739,(0,3):C.GC_739,(0,0):C.GC_725})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1053,(0,9):C.GC_1051,(0,10):C.GC_1051,(0,5):C.GC_1041,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1050,(0,4):C.GC_1052,(0,6):C.GC_1052,(0,0):C.GC_1042})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1061,(0,6):C.GC_1060,(0,7):C.GC_1060,(0,2):C.GC_1046,(0,4):C.GC_1061,(0,1):C.GC_1060,(0,3):C.GC_1060,(0,0):C.GC_1046})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1377,(0,9):C.GC_1375,(0,10):C.GC_1375,(0,5):C.GC_1365,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1374,(0,4):C.GC_1376,(0,6):C.GC_1376,(0,0):C.GC_1366})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1385,(0,6):C.GC_1384,(0,7):C.GC_1384,(0,2):C.GC_1370,(0,4):C.GC_1385,(0,1):C.GC_1384,(0,3):C.GC_1384,(0,0):C.GC_1370})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_827,(0,9):C.GC_825,(0,10):C.GC_825,(0,5):C.GC_815,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_824,(0,4):C.GC_826,(0,6):C.GC_826,(0,0):C.GC_816})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_835,(0,6):C.GC_834,(0,7):C.GC_834,(0,2):C.GC_820,(0,4):C.GC_835,(0,1):C.GC_834,(0,3):C.GC_834,(0,0):C.GC_820})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1080,(0,9):C.GC_1078,(0,10):C.GC_1078,(0,5):C.GC_1068,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1077,(0,4):C.GC_1079,(0,6):C.GC_1079,(0,0):C.GC_1069})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1088,(0,6):C.GC_1087,(0,7):C.GC_1087,(0,2):C.GC_1073,(0,4):C.GC_1088,(0,1):C.GC_1087,(0,3):C.GC_1087,(0,0):C.GC_1073})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
                couplings = {(0,11):C.GC_1429,(0,8):C.GC_28,(0,12):C.GC_1422,(0,9):C.GC_1420,(0,10):C.GC_1420,(0,5):C.GC_1410,(0,4):C.GC_1421,(0,6):C.GC_1421,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1419,(0,0):C.GC_1411})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,7):C.GC_1430,(0,6):C.GC_1429,(0,2):C.GC_1415,(0,1):C.GC_1429,(0,3):C.GC_1429,(0,4):C.GC_1430,(0,0):C.GC_1415})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1184,(0,9):C.GC_1182,(0,10):C.GC_1182,(0,5):C.GC_1172,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1181,(0,4):C.GC_1183,(0,6):C.GC_1183,(0,0):C.GC_1173})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1192,(0,6):C.GC_1191,(0,7):C.GC_1191,(0,2):C.GC_1177,(0,4):C.GC_1192,(0,1):C.GC_1191,(0,3):C.GC_1191,(0,0):C.GC_1177})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,8):C.GC_28,(0,11):C.GC_1229,(0,9):C.GC_1227,(0,10):C.GC_1227,(0,5):C.GC_1217,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_14,(0,7):C.GC_1226,(0,4):C.GC_1228,(0,6):C.GC_1228,(0,0):C.GC_1218})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
                couplings = {(0,5):C.GC_29,(0,8):C.GC_1237,(0,6):C.GC_1236,(0,7):C.GC_1236,(0,2):C.GC_1222,(0,4):C.GC_1237,(0,1):C.GC_1236,(0,3):C.GC_1236,(0,0):C.GC_1222})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_50,(2,0):C.GC_51,(1,3):C.GC_50,(3,3):C.GC_51,(1,1):C.GC_50,(3,1):C.GC_51,(1,2):C.GC_58,(0,4):C.GC_50,(2,4):C.GC_51,(0,5):C.GC_58})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_59,(0,1):C.GC_59})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_50,(2,2):C.GC_51,(1,0):C.GC_50,(2,0):C.GC_51,(1,1):C.GC_58,(0,3):C.GC_59})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_50,(2,2):C.GC_51,(1,0):C.GC_50,(2,0):C.GC_51,(1,1):C.GC_58,(0,3):C.GC_59})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_50,(2,0):C.GC_51,(1,3):C.GC_50,(3,3):C.GC_51,(1,1):C.GC_50,(3,1):C.GC_51,(1,2):C.GC_58,(0,4):C.GC_50,(2,4):C.GC_51,(0,5):C.GC_58})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_59,(0,1):C.GC_59})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_50,(2,2):C.GC_51,(1,0):C.GC_50,(2,0):C.GC_51,(1,1):C.GC_58,(0,3):C.GC_59})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_48})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_50,(2,0):C.GC_51,(1,3):C.GC_50,(3,3):C.GC_51,(1,1):C.GC_50,(3,1):C.GC_51,(1,2):C.GC_58,(0,4):C.GC_50,(2,4):C.GC_51,(0,5):C.GC_58})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF15, L.FFFF18, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_59,(0,1):C.GC_59})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_47,(0,1):C.GC_47})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_48,(0,1):C.GC_48})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_25})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_27})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_26})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_27})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_27})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_26})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_27})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_26,(0,1):C.GC_26})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_27,(0,1):C.GC_27})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_40})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_30})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1437,(0,4):C.GC_1603,(0,2):C.GC_1602,(0,3):C.GC_1602,(0,0):C.GC_1496,(0,1):C.GC_1600})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1605,(0,2):C.GC_1604,(0,3):C.GC_1604,(0,0):C.GC_1497,(0,1):C.GC_1601})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2052,(0,4):C.GC_2164,(0,2):C.GC_2163,(0,3):C.GC_2163,(0,0):C.GC_2167,(0,1):C.GC_2161})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2166,(0,2):C.GC_2165,(0,3):C.GC_2165,(0,0):C.GC_2168,(0,1):C.GC_2162})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2667,(0,4):C.GC_2808,(0,2):C.GC_2807,(0,3):C.GC_2807,(0,0):C.GC_2727,(0,1):C.GC_2805})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2810,(0,2):C.GC_2809,(0,3):C.GC_2809,(0,0):C.GC_2728,(0,1):C.GC_2806})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1437,(0,4):C.GC_1609,(0,2):C.GC_1608,(0,3):C.GC_1608,(0,0):C.GC_1498,(0,1):C.GC_1606})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1611,(0,2):C.GC_1610,(0,3):C.GC_1610,(0,0):C.GC_1499,(0,1):C.GC_1607})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2052,(0,4):C.GC_2172,(0,2):C.GC_2171,(0,3):C.GC_2171,(0,0):C.GC_2175,(0,1):C.GC_2169})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2174,(0,2):C.GC_2173,(0,3):C.GC_2173,(0,0):C.GC_2176,(0,1):C.GC_2170})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2667,(0,4):C.GC_2814,(0,2):C.GC_2813,(0,3):C.GC_2813,(0,0):C.GC_2729,(0,1):C.GC_2811})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2816,(0,2):C.GC_2815,(0,3):C.GC_2815,(0,0):C.GC_2730,(0,1):C.GC_2812})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1437,(0,4):C.GC_1639,(0,2):C.GC_1638,(0,3):C.GC_1638,(0,0):C.GC_1524,(0,1):C.GC_1636})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1641,(0,2):C.GC_1640,(0,3):C.GC_1640,(0,0):C.GC_1525,(0,1):C.GC_1637})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2052,(0,4):C.GC_2228,(0,2):C.GC_2227,(0,3):C.GC_2227,(0,0):C.GC_2231,(0,1):C.GC_2225})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2230,(0,2):C.GC_2229,(0,3):C.GC_2229,(0,0):C.GC_2232,(0,1):C.GC_2226})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2667,(0,4):C.GC_2846,(0,2):C.GC_2845,(0,3):C.GC_2845,(0,0):C.GC_2841,(0,1):C.GC_2843})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2848,(0,2):C.GC_2847,(0,3):C.GC_2847,(0,0):C.GC_2842,(0,1):C.GC_2844})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1642,(0,4):C.GC_1782,(0,2):C.GC_1781,(0,3):C.GC_1781,(0,0):C.GC_1701,(0,1):C.GC_1779})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1784,(0,2):C.GC_1783,(0,3):C.GC_1783,(0,0):C.GC_1702,(0,1):C.GC_1780})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2257,(0,4):C.GC_2343,(0,2):C.GC_2342,(0,3):C.GC_2342,(0,0):C.GC_2402,(0,1):C.GC_2340})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2345,(0,2):C.GC_2344,(0,3):C.GC_2344,(0,0):C.GC_2403,(0,1):C.GC_2341})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2873,(0,4):C.GC_2988,(0,2):C.GC_2987,(0,3):C.GC_2987,(0,0):C.GC_2933,(0,1):C.GC_2985})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2990,(0,2):C.GC_2989,(0,3):C.GC_2989,(0,0):C.GC_2934,(0,1):C.GC_2986})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1642,(0,4):C.GC_1788,(0,2):C.GC_1787,(0,3):C.GC_1787,(0,0):C.GC_1703,(0,1):C.GC_1785})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1790,(0,2):C.GC_1789,(0,3):C.GC_1789,(0,0):C.GC_1704,(0,1):C.GC_1786})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2257,(0,4):C.GC_2349,(0,2):C.GC_2348,(0,3):C.GC_2348,(0,0):C.GC_2404,(0,1):C.GC_2346})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2351,(0,2):C.GC_2350,(0,3):C.GC_2350,(0,0):C.GC_2405,(0,1):C.GC_2347})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2873,(0,4):C.GC_2994,(0,2):C.GC_2993,(0,3):C.GC_2993,(0,0):C.GC_2935,(0,1):C.GC_2991})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2996,(0,2):C.GC_2995,(0,3):C.GC_2995,(0,0):C.GC_2936,(0,1):C.GC_2992})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1642,(0,4):C.GC_1844,(0,2):C.GC_1843,(0,3):C.GC_1843,(0,0):C.GC_1729,(0,1):C.GC_1841})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_1846,(0,2):C.GC_1845,(0,3):C.GC_1845,(0,0):C.GC_1730,(0,1):C.GC_1842})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2257,(0,4):C.GC_2433,(0,2):C.GC_2432,(0,3):C.GC_2432,(0,0):C.GC_2436,(0,1):C.GC_2430})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2435,(0,2):C.GC_2434,(0,3):C.GC_2434,(0,0):C.GC_2437,(0,1):C.GC_2431})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2873,(0,4):C.GC_3052,(0,2):C.GC_3051,(0,3):C.GC_3051,(0,0):C.GC_3047,(0,1):C.GC_3049})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3054,(0,2):C.GC_3053,(0,3):C.GC_3053,(0,0):C.GC_3048,(0,1):C.GC_3050})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1847,(0,4):C.GC_2013,(0,2):C.GC_2012,(0,3):C.GC_2012,(0,0):C.GC_1906,(0,1):C.GC_2010})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2015,(0,2):C.GC_2014,(0,3):C.GC_2014,(0,0):C.GC_1907,(0,1):C.GC_2011})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2462,(0,4):C.GC_2576,(0,2):C.GC_2575,(0,3):C.GC_2575,(0,0):C.GC_2571,(0,1):C.GC_2573})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2578,(0,2):C.GC_2577,(0,3):C.GC_2577,(0,0):C.GC_2572,(0,1):C.GC_2574})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3079,(0,4):C.GC_3220,(0,2):C.GC_3219,(0,3):C.GC_3219,(0,0):C.GC_3139,(0,1):C.GC_3217})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3222,(0,2):C.GC_3221,(0,3):C.GC_3221,(0,0):C.GC_3140,(0,1):C.GC_3218})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1847,(0,4):C.GC_2019,(0,2):C.GC_2018,(0,3):C.GC_2018,(0,0):C.GC_1908,(0,1):C.GC_2016})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2021,(0,2):C.GC_2020,(0,3):C.GC_2020,(0,0):C.GC_1909,(0,1):C.GC_2017})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2462,(0,4):C.GC_2584,(0,2):C.GC_2583,(0,3):C.GC_2583,(0,0):C.GC_2579,(0,1):C.GC_2581})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2586,(0,2):C.GC_2585,(0,3):C.GC_2585,(0,0):C.GC_2580,(0,1):C.GC_2582})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3079,(0,4):C.GC_3226,(0,2):C.GC_3225,(0,3):C.GC_3225,(0,0):C.GC_3141,(0,1):C.GC_3223})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3228,(0,2):C.GC_3227,(0,3):C.GC_3227,(0,0):C.GC_3142,(0,1):C.GC_3224})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_1847,(0,4):C.GC_2049,(0,2):C.GC_2048,(0,3):C.GC_2048,(0,0):C.GC_1934,(0,1):C.GC_2046})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2051,(0,2):C.GC_2050,(0,3):C.GC_2050,(0,0):C.GC_1935,(0,1):C.GC_2047})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_2462,(0,4):C.GC_2640,(0,2):C.GC_2639,(0,3):C.GC_2639,(0,0):C.GC_2635,(0,1):C.GC_2637})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_2642,(0,2):C.GC_2641,(0,3):C.GC_2641,(0,0):C.GC_2636,(0,1):C.GC_2638})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
                couplings = {(0,5):C.GC_3079,(0,4):C.GC_3258,(0,2):C.GC_3257,(0,3):C.GC_3257,(0,0):C.GC_3253,(0,1):C.GC_3255})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
                couplings = {(0,4):C.GC_3260,(0,2):C.GC_3259,(0,3):C.GC_3259,(0,0):C.GC_3254,(0,1):C.GC_3256})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF13, L.FFFF4 ],
                couplings = {(0,1):C.GC_28,(0,0):C.GC_24})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_29})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.a, P.a, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_241})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.g, P.g, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
                couplings = {(0,0):C.GC_242,(0,2):C.GC_255,(0,1):C.GC_251,(0,3):C.GC_246})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.a, P.Z, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_245})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.a, P.Z1, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_245})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.a, P.Z1, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS4 ],
                couplings = {(0,0):C.GC_259})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.g, P.g, P.g, P.H1 ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVVS10, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
                couplings = {(0,3):C.GC_247,(0,0):C.GC_256,(0,4):C.GC_252,(0,2):C.GC_249,(0,1):C.GC_243})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.g, P.g, P.g, P.g, P.H1 ],
                color = [ 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)' ],
                lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS18, L.VVVVS2, L.VVVVS20, L.VVVVS3, L.VVVVS5, L.VVVVS7, L.VVVVS8 ],
                couplings = {(2,5):C.GC_248,(2,8):C.GC_257,(1,4):C.GC_248,(1,10):C.GC_257,(2,6):C.GC_254,(0,11):C.GC_250,(0,12):C.GC_258,(1,7):C.GC_254,(0,3):C.GC_253,(1,2):C.GC_250,(2,1):C.GC_250,(0,9):C.GC_248,(1,13):C.GC_244,(0,0):C.GC_244,(2,14):C.GC_244})

