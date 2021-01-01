# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Sat 1 Aug 2020 04:47:56


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1, L.VVV4, L.VVV5, L.VVV6 ],
             couplings = {(0,3):C.GC_213,(0,1):C.GC_3,(0,0):C.GC_360,(0,2):C.GC_364})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV4 ],
             couplings = {(0,0):C.GC_7})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV4 ],
             couplings = {(0,0):C.GC_223})

V_4 = Vertex(name = 'V_4',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV6 ],
             couplings = {(0,3):C.GC_65,(0,2):C.GC_133,(0,0):C.GC_369,(0,1):C.GC_339})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV4 ],
             couplings = {(0,0):C.GC_232})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV4 ],
             couplings = {(0,0):C.GC_205})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV4, L.VVV6 ],
             couplings = {(0,1):C.GC_25,(0,0):C.GC_14})

V_8 = Vertex(name = 'V_8',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
             couplings = {(0,1):C.GC_71,(1,5):C.GC_71,(2,4):C.GC_71,(1,2):C.GC_15,(0,0):C.GC_15,(2,3):C.GC_15})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g, P.g, P.g ],
             color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
             lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV2, L.VVVVV4, L.VVVVV5, L.VVVVV6, L.VVVVV7, L.VVVVV8 ],
             couplings = {(24,11):C.GC_74,(21,12):C.GC_73,(18,12):C.GC_74,(15,11):C.GC_73,(28,9):C.GC_74,(22,2):C.GC_74,(9,2):C.GC_73,(3,9):C.GC_73,(29,10):C.GC_74,(16,3):C.GC_74,(10,3):C.GC_73,(0,10):C.GC_73,(26,6):C.GC_73,(20,5):C.GC_73,(4,5):C.GC_74,(1,6):C.GC_74,(25,1):C.GC_74,(6,1):C.GC_73,(19,4):C.GC_74,(7,4):C.GC_73,(23,8):C.GC_73,(17,7):C.GC_73,(5,7):C.GC_74,(2,8):C.GC_74,(27,0):C.GC_74,(12,0):C.GC_73,(13,13):C.GC_74,(11,13):C.GC_73,(14,14):C.GC_73,(8,14):C.GC_74})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV2, L.VVVVVV3, L.VVVVVV4, L.VVVVVV5, L.VVVVVV6, L.VVVVVV7, L.VVVVVV9 ],
              couplings = {(65,10):C.GC_76,(71,12):C.GC_77,(77,12):C.GC_76,(83,10):C.GC_77,(41,8):C.GC_76,(53,2):C.GC_76,(76,2):C.GC_77,(88,8):C.GC_77,(35,9):C.GC_76,(52,5):C.GC_76,(64,5):C.GC_77,(87,9):C.GC_77,(34,4):C.GC_77,(40,3):C.GC_77,(69,3):C.GC_76,(81,4):C.GC_76,(17,9):C.GC_77,(23,4):C.GC_76,(80,4):C.GC_77,(86,9):C.GC_76,(11,8):C.GC_77,(22,3):C.GC_76,(68,3):C.GC_77,(85,8):C.GC_76,(9,2):C.GC_77,(15,5):C.GC_77,(61,5):C.GC_76,(73,2):C.GC_76,(4,10):C.GC_77,(14,5):C.GC_76,(49,5):C.GC_77,(78,10):C.GC_76,(3,12):C.GC_76,(19,3):C.GC_77,(37,3):C.GC_76,(72,12):C.GC_77,(2,12):C.GC_77,(8,2):C.GC_76,(48,2):C.GC_77,(66,12):C.GC_76,(1,10):C.GC_76,(18,4):C.GC_77,(31,4):C.GC_76,(60,10):C.GC_77,(6,8):C.GC_76,(12,9):C.GC_76,(30,9):C.GC_77,(36,8):C.GC_77,(47,14):C.GC_76,(82,14):C.GC_77,(46,6):C.GC_76,(70,6):C.GC_77,(33,7):C.GC_77,(39,1):C.GC_77,(63,1):C.GC_76,(75,7):C.GC_76,(29,7):C.GC_76,(74,7):C.GC_77,(28,1):C.GC_76,(62,1):C.GC_77,(10,14):C.GC_77,(16,6):C.GC_77,(67,6):C.GC_76,(79,14):C.GC_76,(25,1):C.GC_77,(38,1):C.GC_76,(13,6):C.GC_76,(43,6):C.GC_77,(24,7):C.GC_77,(32,7):C.GC_76,(7,14):C.GC_76,(42,14):C.GC_77,(59,0):C.GC_76,(89,0):C.GC_77,(51,11):C.GC_76,(58,11):C.GC_77,(21,11):C.GC_77,(55,11):C.GC_76,(5,0):C.GC_77,(20,11):C.GC_76,(50,11):C.GC_77,(84,0):C.GC_76,(0,0):C.GC_76,(54,0):C.GC_77,(45,13):C.GC_77,(57,13):C.GC_76,(27,13):C.GC_76,(56,13):C.GC_77,(26,13):C.GC_77,(44,13):C.GC_76})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_214,(0,1):C.GC_9})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_12})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_225})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_365})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6, L.VVVV9 ],
              couplings = {(0,1):C.GC_68,(0,0):C.GC_147})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_233})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_234})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_376})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV3 ],
              couplings = {(0,0):C.GC_215})

V_20 = Vertex(name = 'V_20',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_169,(0,1):C.GC_92})

V_21 = Vertex(name = 'V_21',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_96})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV19 ],
              couplings = {(0,0):C.GC_70})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV21 ],
              couplings = {(0,0):C.GC_172})

V_24 = Vertex(name = 'V_24',
              particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV8 ],
              couplings = {(0,0):C.GC_174})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_170,(0,1):C.GC_11})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_94})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_235})

V_28 = Vertex(name = 'V_28',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_366})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV9 ],
              couplings = {(0,0):C.GC_173})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV16 ],
              couplings = {(0,0):C.GC_102})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV17 ],
              couplings = {(0,0):C.GC_104})

V_32 = Vertex(name = 'V_32',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV8 ],
              couplings = {(0,0):C.GC_90})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV20 ],
              couplings = {(0,0):C.GC_103})

V_34 = Vertex(name = 'V_34',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_16,(0,2):C.GC_27,(0,1):C.GC_28})

V_35 = Vertex(name = 'V_35',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_17})

V_36 = Vertex(name = 'V_36',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_18})

V_37 = Vertex(name = 'V_37',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_19})

V_38 = Vertex(name = 'V_38',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_336})

V_39 = Vertex(name = 'V_39',
              particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_26})

V_40 = Vertex(name = 'V_40',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_274,(0,2):C.GC_279,(0,1):C.GC_280})

V_41 = Vertex(name = 'V_41',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_275})

V_42 = Vertex(name = 'V_42',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_276})

V_43 = Vertex(name = 'V_43',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_277})

V_44 = Vertex(name = 'V_44',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_371})

V_45 = Vertex(name = 'V_45',
              particles = [ P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_278})

V_46 = Vertex(name = 'V_46',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_59})

V_47 = Vertex(name = 'V_47',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_211})

V_48 = Vertex(name = 'V_48',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_227})

V_49 = Vertex(name = 'V_49',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_237})

V_50 = Vertex(name = 'V_50',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_283})

V_51 = Vertex(name = 'V_51',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_332})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_335})

V_53 = Vertex(name = 'V_53',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_29})

V_54 = Vertex(name = 'V_54',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4, L.VVS5 ],
              couplings = {(0,0):C.GC_238,(0,2):C.GC_251,(0,1):C.GC_247,(0,3):C.GC_242})

V_55 = Vertex(name = 'V_55',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_281})

V_56 = Vertex(name = 'V_56',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_30,(0,0):C.GC_91})

V_57 = Vertex(name = 'V_57',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_95})

V_58 = Vertex(name = 'V_58',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_97})

V_59 = Vertex(name = 'V_59',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_282,(0,0):C.GC_293})

V_60 = Vertex(name = 'V_60',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_295})

V_61 = Vertex(name = 'V_61',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_296})

V_62 = Vertex(name = 'V_62',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_297})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_236})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_209})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_210})

V_66 = Vertex(name = 'V_66',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_241})

V_67 = Vertex(name = 'V_67',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_375})

V_68 = Vertex(name = 'V_68',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_330})

V_69 = Vertex(name = 'V_69',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_331})

V_70 = Vertex(name = 'V_70',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_60,(0,0):C.GC_10})

V_71 = Vertex(name = 'V_71',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_212,(0,0):C.GC_93})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_226,(0,0):C.GC_95})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_98})

V_74 = Vertex(name = 'V_74',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_340})

V_75 = Vertex(name = 'V_75',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_361})

V_76 = Vertex(name = 'V_76',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_284,(0,0):C.GC_374})

V_7600 = Vertex(name = 'V_7600',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_37400})

V_77 = Vertex(name = 'V_77',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_333,(0,0):C.GC_294})

V_78 = Vertex(name = 'V_78',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_334,(0,0):C.GC_296})

V_79 = Vertex(name = 'V_79',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_298})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_372})

V_81 = Vertex(name = 'V_81',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_373})

V_82 = Vertex(name = 'V_82',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3 ],
              couplings = {(0,0):C.GC_72})

V_83 = Vertex(name = 'V_83',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3, L.VVVS4, L.VVVS5, L.VVVS6, L.VVVS7 ],
              couplings = {(0,2):C.GC_243,(0,4):C.GC_252,(0,3):C.GC_248,(0,1):C.GC_245,(0,0):C.GC_239})

V_84 = Vertex(name = 'V_84',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3 ],
              couplings = {(0,0):C.GC_288})

V_85 = Vertex(name = 'V_85',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_75,(0,0):C.GC_75,(2,2):C.GC_75})

V_86 = Vertex(name = 'V_86',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS17, L.VVVVS19, L.VVVVS2, L.VVVVS3, L.VVVVS4, L.VVVVS7, L.VVVVS8 ],
              couplings = {(2,5):C.GC_244,(2,8):C.GC_253,(1,4):C.GC_244,(1,9):C.GC_253,(2,6):C.GC_250,(0,11):C.GC_246,(0,12):C.GC_254,(1,7):C.GC_250,(0,3):C.GC_249,(1,2):C.GC_246,(2,1):C.GC_246,(0,10):C.GC_244,(1,13):C.GC_240,(0,0):C.GC_240,(2,14):C.GC_240})

V_87 = Vertex(name = 'V_87',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS7, L.VVVVS8 ],
              couplings = {(1,1):C.GC_289,(0,0):C.GC_289,(2,2):C.GC_289})

V_88 = Vertex(name = 'V_88',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3 ],
              couplings = {(0,1):C.GC_66,(0,0):C.GC_168})

V_89 = Vertex(name = 'V_89',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3 ],
              couplings = {(0,1):C.GC_285,(0,0):C.GC_328})

V_90 = Vertex(name = 'V_90',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_69})

V_91 = Vertex(name = 'V_91',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS6 ],
              couplings = {(0,0):C.GC_287})

V_92 = Vertex(name = 'V_92',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2, L.VVVSS3 ],
              couplings = {(0,1):C.GC_167,(0,0):C.GC_67})

V_93 = Vertex(name = 'V_93',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3 ],
              couplings = {(0,1):C.GC_327,(0,0):C.GC_286})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_99})

V_95 = Vertex(name = 'V_95',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS6 ],
              couplings = {(0,0):C.GC_299})

V_96 = Vertex(name = 'V_96',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS5 ],
              couplings = {(0,0):C.GC_171})

V_97 = Vertex(name = 'V_97',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS9 ],
              couplings = {(0,0):C.GC_329})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_100})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_300})

V_100 = Vertex(name = 'V_100',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_101})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_301})

V_102 = Vertex(name = 'V_102',
               particles = [ P.H, P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_82})

V_103 = Vertex(name = 'V_103',
               particles = [ P.H, P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_87})

V_104 = Vertex(name = 'V_104',
               particles = [ P.H, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_88})

V_105 = Vertex(name = 'V_105',
               particles = [ P.H1, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_89})

V_106 = Vertex(name = 'V_106',
               particles = [ P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_290})

V_107 = Vertex(name = 'V_107',
               particles = [ P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_291})

V_108 = Vertex(name = 'V_108',
               particles = [ P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_292})

V_109 = Vertex(name = 'V_109',
               particles = [ P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_79})

V_110 = Vertex(name = 'V_110',
               particles = [ P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_84})

V_111 = Vertex(name = 'V_111',
               particles = [ P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_79})

V_112 = Vertex(name = 'V_112',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_113 = Vertex(name = 'V_113',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_114 = Vertex(name = 'V_114',
               particles = [ P.W__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_113})

V_115 = Vertex(name = 'V_115',
               particles = [ P.W__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_302})

V_116 = Vertex(name = 'V_116',
               particles = [ P.W__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_304})

V_117 = Vertex(name = 'V_117',
               particles = [ P.a, P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_80})

V_118 = Vertex(name = 'V_118',
               particles = [ P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_187})

V_119 = Vertex(name = 'V_119',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_193})

V_120 = Vertex(name = 'V_120',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_113})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_117})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W1__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_304})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_306})

V_125 = Vertex(name = 'V_125',
               particles = [ P.a, P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_85})

V_126 = Vertex(name = 'V_126',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_193})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_196})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_110})

V_129 = Vertex(name = 'V_129',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_114})

V_130 = Vertex(name = 'V_130',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_118})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_302})

V_134 = Vertex(name = 'V_134',
               particles = [ P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_187})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_109})

V_137 = Vertex(name = 'V_137',
               particles = [ P.W1__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_113})

V_138 = Vertex(name = 'V_138',
               particles = [ P.W1__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_302})

V_139 = Vertex(name = 'V_139',
               particles = [ P.W1__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_304})

V_140 = Vertex(name = 'V_140',
               particles = [ P.a, P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_80})

V_141 = Vertex(name = 'V_141',
               particles = [ P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_187})

V_142 = Vertex(name = 'V_142',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV4 ],
               couplings = {(0,0):C.GC_193})

V_143 = Vertex(name = 'V_143',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_106})

V_144 = Vertex(name = 'V_144',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_110})

V_145 = Vertex(name = 'V_145',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_114})

V_146 = Vertex(name = 'V_146',
               particles = [ P.W__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_106})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W1__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_110})

V_148 = Vertex(name = 'V_148',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_188})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_194})

V_150 = Vertex(name = 'V_150',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_188})

V_151 = Vertex(name = 'V_151',
               particles = [ P.Z, P.Z, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_107})

V_152 = Vertex(name = 'V_152',
               particles = [ P.Z, P.Z, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_153 = Vertex(name = 'V_153',
               particles = [ P.Z, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_303})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_108})

V_155 = Vertex(name = 'V_155',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_112})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_108})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_194})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_197})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_188})

V_160 = Vertex(name = 'V_160',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_194})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Z, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_107})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Z, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_163 = Vertex(name = 'V_163',
               particles = [ P.Z, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_115})

V_164 = Vertex(name = 'V_164',
               particles = [ P.Z, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_303})

V_165 = Vertex(name = 'V_165',
               particles = [ P.Z, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_305})

V_166 = Vertex(name = 'V_166',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_112})

V_167 = Vertex(name = 'V_167',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_116})

V_168 = Vertex(name = 'V_168',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_108})

V_169 = Vertex(name = 'V_169',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_112})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Z1, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_111})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Z1, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_115})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Z1, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_119})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z1, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_305})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z1, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_307})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_116})

V_176 = Vertex(name = 'V_176',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_120})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_112})

V_178 = Vertex(name = 'V_178',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_116})

V_179 = Vertex(name = 'V_179',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_545})

V_180 = Vertex(name = 'V_180',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_8,(0,1):C.GC_553})

V_181 = Vertex(name = 'V_181',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_224})

V_182 = Vertex(name = 'V_182',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_183 = Vertex(name = 'V_183',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_600})

V_184 = Vertex(name = 'V_184',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_8,(0,1):C.GC_608})

V_185 = Vertex(name = 'V_185',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_224})

V_186 = Vertex(name = 'V_186',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_187 = Vertex(name = 'V_187',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_865})

V_188 = Vertex(name = 'V_188',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_8,(0,1):C.GC_873})

V_189 = Vertex(name = 'V_189',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_224})

V_190 = Vertex(name = 'V_190',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_191 = Vertex(name = 'V_191',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_200,(0,2):C.GC_132,(0,4):C.GC_204,(0,5):C.GC_206,(0,3):C.GC_352,(0,1):C.GC_546})

V_192 = Vertex(name = 'V_192',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_230,(0,2):C.GC_144,(0,3):C.GC_338,(0,1):C.GC_552})

V_193 = Vertex(name = 'V_193',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_353})

V_194 = Vertex(name = 'V_194',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_370,(0,1):C.GC_355})

V_195 = Vertex(name = 'V_195',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_200,(0,2):C.GC_132,(0,4):C.GC_204,(0,5):C.GC_206,(0,3):C.GC_352,(0,1):C.GC_601})

V_196 = Vertex(name = 'V_196',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_230,(0,2):C.GC_144,(0,3):C.GC_338,(0,1):C.GC_607})

V_197 = Vertex(name = 'V_197',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_353})

V_198 = Vertex(name = 'V_198',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_370,(0,1):C.GC_355})

V_199 = Vertex(name = 'V_199',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV13, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_200,(0,3):C.GC_132,(0,5):C.GC_204,(0,6):C.GC_206,(0,4):C.GC_352,(0,2):C.GC_866,(0,1):C.GC_872})

V_200 = Vertex(name = 'V_200',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_144,(0,2):C.GC_338})

V_201 = Vertex(name = 'V_201',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_353})

V_202 = Vertex(name = 'V_202',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_370,(0,1):C.GC_355})

V_203 = Vertex(name = 'V_203',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_490})

V_204 = Vertex(name = 'V_204',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_5,(0,1):C.GC_499})

V_205 = Vertex(name = 'V_205',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_2661})

V_206 = Vertex(name = 'V_206',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_362,(0,1):C.GC_2674})

V_207 = Vertex(name = 'V_207',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_658})

V_208 = Vertex(name = 'V_208',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_5,(0,1):C.GC_667})

V_209 = Vertex(name = 'V_209',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_3407})

V_210 = Vertex(name = 'V_210',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_362,(0,1):C.GC_3439})

V_211 = Vertex(name = 'V_211',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_397})

V_212 = Vertex(name = 'V_212',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_5,(0,1):C.GC_406})

V_213 = Vertex(name = 'V_213',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_4122})

V_214 = Vertex(name = 'V_214',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_362,(0,1):C.GC_4154})

V_215 = Vertex(name = 'V_215',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_952})

V_216 = Vertex(name = 'V_216',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_964})

V_217 = Vertex(name = 'V_217',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_3954})

V_218 = Vertex(name = 'V_218',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_3976})

V_219 = Vertex(name = 'V_219',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_434})

V_220 = Vertex(name = 'V_220',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_446})

V_221 = Vertex(name = 'V_221',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_2445})

V_222 = Vertex(name = 'V_222',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_2477})

V_223 = Vertex(name = 'V_223',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_734})

V_224 = Vertex(name = 'V_224',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_746})

V_225 = Vertex(name = 'V_225',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_3801})

V_226 = Vertex(name = 'V_226',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_3833})

V_227 = Vertex(name = 'V_227',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_487})

V_228 = Vertex(name = 'V_228',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_2662})

V_229 = Vertex(name = 'V_229',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_655})

V_230 = Vertex(name = 'V_230',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_3410})

V_231 = Vertex(name = 'V_231',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_394})

V_232 = Vertex(name = 'V_232',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_4125})

V_233 = Vertex(name = 'V_233',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_953})

V_234 = Vertex(name = 'V_234',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_3956})

V_235 = Vertex(name = 'V_235',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_435})

V_236 = Vertex(name = 'V_236',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_2448})

V_237 = Vertex(name = 'V_237',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV10 ],
               couplings = {(0,0):C.GC_13,(0,1):C.GC_735})

V_238 = Vertex(name = 'V_238',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV10 ],
               couplings = {(0,0):C.GC_3804})

V_239 = Vertex(name = 'V_239',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV14, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,3):C.GC_955,(0,0):C.GC_489,(0,1):C.GC_510,(0,2):C.GC_122,(0,4):C.GC_981})

V_240 = Vertex(name = 'V_240',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_3960,(0,0):C.GC_2664,(0,1):C.GC_135})

V_241 = Vertex(name = 'V_241',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_342})

V_242 = Vertex(name = 'V_242',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1056})

V_243 = Vertex(name = 'V_243',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_2590,(0,0):C.GC_3011,(0,1):C.GC_123,(0,3):C.GC_1012})

V_244 = Vertex(name = 'V_244',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_136})

V_245 = Vertex(name = 'V_245',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_343})

V_246 = Vertex(name = 'V_246',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1057})

V_247 = Vertex(name = 'V_247',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_3959,(0,0):C.GC_2936,(0,1):C.GC_124,(0,3):C.GC_972})

V_248 = Vertex(name = 'V_248',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_137})

V_249 = Vertex(name = 'V_249',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_344})

V_250 = Vertex(name = 'V_250',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1058})

V_251 = Vertex(name = 'V_251',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_1626,(0,0):C.GC_3358,(0,1):C.GC_125,(0,3):C.GC_509})

V_252 = Vertex(name = 'V_252',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_138})

V_253 = Vertex(name = 'V_253',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_345})

V_254 = Vertex(name = 'V_254',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_527})

V_255 = Vertex(name = 'V_255',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_437,(0,0):C.GC_657,(0,1):C.GC_126,(0,3):C.GC_677})

V_256 = Vertex(name = 'V_256',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_2454,(0,0):C.GC_3416,(0,1):C.GC_139})

V_257 = Vertex(name = 'V_257',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_346})

V_258 = Vertex(name = 'V_258',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_706})

V_259 = Vertex(name = 'V_259',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_3738,(0,0):C.GC_3335,(0,1):C.GC_127,(0,3):C.GC_454})

V_260 = Vertex(name = 'V_260',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_140})

V_261 = Vertex(name = 'V_261',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_347})

V_262 = Vertex(name = 'V_262',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_469})

V_263 = Vertex(name = 'V_263',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_1659,(0,0):C.GC_4172,(0,1):C.GC_128,(0,3):C.GC_763})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_141})

V_265 = Vertex(name = 'V_265',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_348})

V_266 = Vertex(name = 'V_266',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_821})

V_267 = Vertex(name = 'V_267',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_2529,(0,0):C.GC_4203,(0,1):C.GC_129,(0,3):C.GC_794})

V_268 = Vertex(name = 'V_268',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_142})

V_269 = Vertex(name = 'V_269',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_349})

V_270 = Vertex(name = 'V_270',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_822})

V_271 = Vertex(name = 'V_271',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_737,(0,0):C.GC_396,(0,1):C.GC_130,(0,3):C.GC_754})

V_272 = Vertex(name = 'V_272',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_3810,(0,0):C.GC_4131,(0,1):C.GC_143})

V_273 = Vertex(name = 'V_273',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_350})

V_274 = Vertex(name = 'V_274',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_823})

V_275 = Vertex(name = 'V_275',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_979,(0,0):C.GC_149})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1050})

V_277 = Vertex(name = 'V_277',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1010,(0,0):C.GC_150})

V_278 = Vertex(name = 'V_278',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1051})

V_279 = Vertex(name = 'V_279',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_970,(0,0):C.GC_151})

V_280 = Vertex(name = 'V_280',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1052})

V_281 = Vertex(name = 'V_281',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_507,(0,0):C.GC_152})

V_282 = Vertex(name = 'V_282',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_525})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_675,(0,0):C.GC_153})

V_284 = Vertex(name = 'V_284',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_704})

V_285 = Vertex(name = 'V_285',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_452,(0,0):C.GC_154})

V_286 = Vertex(name = 'V_286',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_467})

V_287 = Vertex(name = 'V_287',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_761,(0,0):C.GC_155})

V_288 = Vertex(name = 'V_288',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_815})

V_289 = Vertex(name = 'V_289',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_792,(0,0):C.GC_156})

V_290 = Vertex(name = 'V_290',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_816})

V_291 = Vertex(name = 'V_291',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_752,(0,0):C.GC_157})

V_292 = Vertex(name = 'V_292',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_817})

V_293 = Vertex(name = 'V_293',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_941,(0,3):C.GC_475,(0,2):C.GC_980,(0,0):C.GC_309})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_3936,(0,2):C.GC_2651,(0,0):C.GC_1053})

V_295 = Vertex(name = 'V_295',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_2579,(0,3):C.GC_3000,(0,2):C.GC_1011,(0,0):C.GC_310})

V_296 = Vertex(name = 'V_296',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1054})

V_297 = Vertex(name = 'V_297',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_3935,(0,3):C.GC_2925,(0,2):C.GC_971,(0,0):C.GC_311})

V_298 = Vertex(name = 'V_298',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1055})

V_299 = Vertex(name = 'V_299',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_1615,(0,3):C.GC_3347,(0,2):C.GC_508,(0,0):C.GC_312})

V_300 = Vertex(name = 'V_300',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_526})

V_301 = Vertex(name = 'V_301',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_423,(0,3):C.GC_643,(0,2):C.GC_676,(0,0):C.GC_313})

V_302 = Vertex(name = 'V_302',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_2419,(0,2):C.GC_3381,(0,0):C.GC_705})

V_303 = Vertex(name = 'V_303',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_3727,(0,3):C.GC_3324,(0,2):C.GC_453,(0,0):C.GC_314})

V_304 = Vertex(name = 'V_304',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_468})

V_305 = Vertex(name = 'V_305',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_1648,(0,3):C.GC_4161,(0,2):C.GC_762,(0,0):C.GC_315})

V_306 = Vertex(name = 'V_306',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_818})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_2518,(0,3):C.GC_4192,(0,2):C.GC_793,(0,0):C.GC_316})

V_308 = Vertex(name = 'V_308',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_819})

V_309 = Vertex(name = 'V_309',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_721,(0,3):C.GC_382,(0,2):C.GC_753,(0,0):C.GC_317})

V_310 = Vertex(name = 'V_310',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_3775,(0,2):C.GC_4096,(0,0):C.GC_820})

V_311 = Vertex(name = 'V_311',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV2 ],
               couplings = {(0,0):C.GC_544,(0,1):C.GC_121})

V_312 = Vertex(name = 'V_312',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_313 = Vertex(name = 'V_313',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_314 = Vertex(name = 'V_314',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV2 ],
               couplings = {(0,0):C.GC_599,(0,1):C.GC_121})

V_315 = Vertex(name = 'V_315',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_316 = Vertex(name = 'V_316',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_317 = Vertex(name = 'V_317',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV12, L.FFV2 ],
               couplings = {(0,0):C.GC_864,(0,1):C.GC_121})

V_318 = Vertex(name = 'V_318',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_319 = Vertex(name = 'V_319',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_320 = Vertex(name = 'V_320',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_321 = Vertex(name = 'V_321',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_322 = Vertex(name = 'V_322',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_323 = Vertex(name = 'V_323',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,1):C.GC_532,(0,0):C.GC_308})

V_324 = Vertex(name = 'V_324',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,1):C.GC_587,(0,0):C.GC_308})

V_325 = Vertex(name = 'V_325',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS6 ],
               couplings = {(0,1):C.GC_852,(0,0):C.GC_308})

V_326 = Vertex(name = 'V_326',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_489,(0,0):C.GC_955,(0,1):C.GC_1135,(0,3):C.GC_1194})

V_327 = Vertex(name = 'V_327',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_2665,(0,0):C.GC_3960,(0,1):C.GC_1136})

V_328 = Vertex(name = 'V_328',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1140})

V_329 = Vertex(name = 'V_329',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1242})

V_330 = Vertex(name = 'V_330',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_2973,(0,0):C.GC_2453,(0,1):C.GC_1823,(0,3):C.GC_1859})

V_331 = Vertex(name = 'V_331',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1824})

V_332 = Vertex(name = 'V_332',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1828})

V_333 = Vertex(name = 'V_333',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1940})

V_334 = Vertex(name = 'V_334',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_2974,(0,0):C.GC_3808,(0,1):C.GC_2707,(0,3):C.GC_2772})

V_335 = Vertex(name = 'V_335',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2708})

V_336 = Vertex(name = 'V_336',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2713})

V_337 = Vertex(name = 'V_337',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2849})

V_338 = Vertex(name = 'V_338',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_3415,(0,0):C.GC_1716,(0,1):C.GC_1283,(0,3):C.GC_1374})

V_339 = Vertex(name = 'V_339',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1284})

V_340 = Vertex(name = 'V_340',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1288})

V_341 = Vertex(name = 'V_341',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1414})

V_342 = Vertex(name = 'V_342',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_657,(0,0):C.GC_437,(0,1):C.GC_1996,(0,3):C.GC_2066})

V_343 = Vertex(name = 'V_343',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_3416,(0,0):C.GC_2454,(0,1):C.GC_1997})

V_344 = Vertex(name = 'V_344',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2001})

V_345 = Vertex(name = 'V_345',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2133})

V_346 = Vertex(name = 'V_346',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_3417,(0,0):C.GC_3809,(0,1):C.GC_3054,(0,3):C.GC_3151})

V_347 = Vertex(name = 'V_347',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3055})

V_348 = Vertex(name = 'V_348',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3060})

V_349 = Vertex(name = 'V_349',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3215})

V_350 = Vertex(name = 'V_350',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_4129,(0,0):C.GC_1717,(0,1):C.GC_1455,(0,3):C.GC_1518})

V_351 = Vertex(name = 'V_351',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1456})

V_352 = Vertex(name = 'V_352',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1460})

V_353 = Vertex(name = 'V_353',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1782})

V_354 = Vertex(name = 'V_354',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_4130,(0,0):C.GC_2455,(0,1):C.GC_2192,(0,3):C.GC_2220})

V_355 = Vertex(name = 'V_355',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2193})

V_356 = Vertex(name = 'V_356',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2197})

V_357 = Vertex(name = 'V_357',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2331})

V_358 = Vertex(name = 'V_358',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3, L.FFV4 ],
               couplings = {(0,2):C.GC_396,(0,0):C.GC_737,(0,1):C.GC_3483,(0,3):C.GC_3544})

V_359 = Vertex(name = 'V_359',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_4131,(0,0):C.GC_3810,(0,1):C.GC_3484})

V_360 = Vertex(name = 'V_360',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3489})

V_361 = Vertex(name = 'V_361',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3888})

V_362 = Vertex(name = 'V_362',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1192,(0,0):C.GC_1137})

V_363 = Vertex(name = 'V_363',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1240})

V_364 = Vertex(name = 'V_364',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1857,(0,0):C.GC_1825})

V_365 = Vertex(name = 'V_365',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1938})

V_366 = Vertex(name = 'V_366',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2770,(0,0):C.GC_2709})

V_367 = Vertex(name = 'V_367',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2847})

V_368 = Vertex(name = 'V_368',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1372,(0,0):C.GC_1285})

V_369 = Vertex(name = 'V_369',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1412})

V_370 = Vertex(name = 'V_370',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2064,(0,0):C.GC_1998})

V_371 = Vertex(name = 'V_371',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2131})

V_372 = Vertex(name = 'V_372',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3149,(0,0):C.GC_3056})

V_373 = Vertex(name = 'V_373',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3213})

V_374 = Vertex(name = 'V_374',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1516,(0,0):C.GC_1457})

V_375 = Vertex(name = 'V_375',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1780})

V_376 = Vertex(name = 'V_376',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2218,(0,0):C.GC_2194})

V_377 = Vertex(name = 'V_377',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2329})

V_378 = Vertex(name = 'V_378',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3542,(0,0):C.GC_3485})

V_379 = Vertex(name = 'V_379',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3886})

V_380 = Vertex(name = 'V_380',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_475,(0,3):C.GC_941,(0,2):C.GC_1193,(0,0):C.GC_1139})

V_381 = Vertex(name = 'V_381',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_2651,(0,2):C.GC_3936,(0,0):C.GC_1241})

V_382 = Vertex(name = 'V_382',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_2951,(0,3):C.GC_2418,(0,2):C.GC_1858,(0,0):C.GC_1827})

V_383 = Vertex(name = 'V_383',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1939})

V_384 = Vertex(name = 'V_384',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_2952,(0,3):C.GC_3773,(0,2):C.GC_2771,(0,0):C.GC_2712})

V_385 = Vertex(name = 'V_385',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2848})

V_386 = Vertex(name = 'V_386',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_3380,(0,3):C.GC_1694,(0,2):C.GC_1373,(0,0):C.GC_1287})

V_387 = Vertex(name = 'V_387',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1413})

V_388 = Vertex(name = 'V_388',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_643,(0,3):C.GC_423,(0,2):C.GC_2065,(0,0):C.GC_2000})

V_389 = Vertex(name = 'V_389',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_3381,(0,2):C.GC_2419,(0,0):C.GC_2132})

V_390 = Vertex(name = 'V_390',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_3382,(0,3):C.GC_3774,(0,2):C.GC_3150,(0,0):C.GC_3059})

V_391 = Vertex(name = 'V_391',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_3214})

V_392 = Vertex(name = 'V_392',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_4094,(0,3):C.GC_1695,(0,2):C.GC_1517,(0,0):C.GC_1459})

V_393 = Vertex(name = 'V_393',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1781})

V_394 = Vertex(name = 'V_394',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_4095,(0,3):C.GC_2420,(0,2):C.GC_2219,(0,0):C.GC_2196})

V_395 = Vertex(name = 'V_395',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2330})

V_396 = Vertex(name = 'V_396',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6 ],
               couplings = {(0,1):C.GC_382,(0,3):C.GC_721,(0,2):C.GC_3543,(0,0):C.GC_3488})

V_397 = Vertex(name = 'V_397',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,1):C.GC_4096,(0,2):C.GC_3775,(0,0):C.GC_3887})

V_398 = Vertex(name = 'V_398',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_544,(0,0):C.GC_121})

V_399 = Vertex(name = 'V_399',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_400 = Vertex(name = 'V_400',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_401 = Vertex(name = 'V_401',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_599,(0,0):C.GC_121})

V_402 = Vertex(name = 'V_402',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_403 = Vertex(name = 'V_403',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_404 = Vertex(name = 'V_404',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_864,(0,0):C.GC_121})

V_405 = Vertex(name = 'V_405',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_134})

V_406 = Vertex(name = 'V_406',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_407 = Vertex(name = 'V_407',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_408 = Vertex(name = 'V_408',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_409 = Vertex(name = 'V_409',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_148})

V_410 = Vertex(name = 'V_410',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_532,(0,0):C.GC_308})

V_411 = Vertex(name = 'V_411',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_587,(0,0):C.GC_308})

V_412 = Vertex(name = 'V_412',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_852,(0,0):C.GC_308})

V_413 = Vertex(name = 'V_413',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_158})

V_414 = Vertex(name = 'V_414',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_517})

V_415 = Vertex(name = 'V_415',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2642})

V_416 = Vertex(name = 'V_416',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2643})

V_417 = Vertex(name = 'V_417',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2910})

V_418 = Vertex(name = 'V_418',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2912})

V_419 = Vertex(name = 'V_419',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2911})

V_420 = Vertex(name = 'V_420',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2913})

V_421 = Vertex(name = 'V_421',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3303})

V_422 = Vertex(name = 'V_422',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3306})

V_423 = Vertex(name = 'V_423',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_158})

V_424 = Vertex(name = 'V_424',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_694})

V_425 = Vertex(name = 'V_425',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3304})

V_426 = Vertex(name = 'V_426',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3307})

V_427 = Vertex(name = 'V_427',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3305})

V_428 = Vertex(name = 'V_428',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3308})

V_429 = Vertex(name = 'V_429',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4067})

V_430 = Vertex(name = 'V_430',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4070})

V_431 = Vertex(name = 'V_431',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4068})

V_432 = Vertex(name = 'V_432',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4071})

V_433 = Vertex(name = 'V_433',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_158})

V_434 = Vertex(name = 'V_434',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_165,(0,1):C.GC_414})

V_435 = Vertex(name = 'V_435',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4069})

V_436 = Vertex(name = 'V_436',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4072})

V_437 = Vertex(name = 'V_437',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_318,(0,2):C.GC_477})

V_438 = Vertex(name = 'V_438',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_325,(0,1):C.GC_518,(0,2):C.GC_485})

V_439 = Vertex(name = 'V_439',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2644,(0,1):C.GC_2652})

V_440 = Vertex(name = 'V_440',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2645,(0,1):C.GC_2659})

V_441 = Vertex(name = 'V_441',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2914,(0,1):C.GC_2953,(0,2):C.GC_3001})

V_442 = Vertex(name = 'V_442',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2916,(0,1):C.GC_2963,(0,2):C.GC_3006})

V_443 = Vertex(name = 'V_443',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2915,(0,1):C.GC_2954,(0,2):C.GC_2926})

V_444 = Vertex(name = 'V_444',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2917,(0,1):C.GC_2964,(0,2):C.GC_2931})

V_445 = Vertex(name = 'V_445',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3309,(0,1):C.GC_3383,(0,2):C.GC_3348})

V_446 = Vertex(name = 'V_446',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3312,(0,1):C.GC_3400,(0,2):C.GC_3353})

V_447 = Vertex(name = 'V_447',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_318,(0,2):C.GC_645})

V_448 = Vertex(name = 'V_448',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_325,(0,1):C.GC_695,(0,2):C.GC_653})

V_449 = Vertex(name = 'V_449',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3310,(0,1):C.GC_3384})

V_450 = Vertex(name = 'V_450',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3313,(0,1):C.GC_3401})

V_451 = Vertex(name = 'V_451',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3311,(0,1):C.GC_3385,(0,2):C.GC_3325})

V_452 = Vertex(name = 'V_452',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3314,(0,1):C.GC_3402,(0,2):C.GC_3330})

V_453 = Vertex(name = 'V_453',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4073,(0,1):C.GC_4097,(0,2):C.GC_4162})

V_454 = Vertex(name = 'V_454',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4076,(0,1):C.GC_4114,(0,2):C.GC_4167})

V_455 = Vertex(name = 'V_455',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4074,(0,1):C.GC_4098,(0,2):C.GC_4193})

V_456 = Vertex(name = 'V_456',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4077,(0,1):C.GC_4115,(0,2):C.GC_4198})

V_457 = Vertex(name = 'V_457',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_318,(0,2):C.GC_384})

V_458 = Vertex(name = 'V_458',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_325,(0,1):C.GC_415,(0,2):C.GC_392})

V_459 = Vertex(name = 'V_459',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_4075,(0,1):C.GC_4099})

V_460 = Vertex(name = 'V_460',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_4078,(0,1):C.GC_4116})

V_461 = Vertex(name = 'V_461',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,0):C.GC_198,(0,2):C.GC_132,(0,5):C.GC_201,(0,4):C.GC_337,(0,3):C.GC_351,(0,1):C.GC_491})

V_462 = Vertex(name = 'V_462',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_207,(0,2):C.GC_146,(0,3):C.GC_519,(0,1):C.GC_498})

V_463 = Vertex(name = 'V_463',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_228,(0,2):C.GC_356,(0,1):C.GC_2666})

V_464 = Vertex(name = 'V_464',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_367,(0,2):C.GC_358,(0,1):C.GC_2673})

V_465 = Vertex(name = 'V_465',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2646})

V_466 = Vertex(name = 'V_466',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2647})

V_467 = Vertex(name = 'V_467',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2918,(0,2):C.GC_2975,(0,0):C.GC_3012})

V_468 = Vertex(name = 'V_468',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2920,(0,2):C.GC_2985,(0,0):C.GC_3017})

V_469 = Vertex(name = 'V_469',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2919,(0,2):C.GC_2976,(0,0):C.GC_2937})

V_470 = Vertex(name = 'V_470',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2921,(0,2):C.GC_2986,(0,0):C.GC_2942})

V_471 = Vertex(name = 'V_471',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3315,(0,2):C.GC_3418,(0,0):C.GC_3359})

V_472 = Vertex(name = 'V_472',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3318,(0,2):C.GC_3435,(0,0):C.GC_3364})

V_473 = Vertex(name = 'V_473',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,0):C.GC_198,(0,2):C.GC_132,(0,5):C.GC_201,(0,4):C.GC_337,(0,3):C.GC_351,(0,1):C.GC_659})

V_474 = Vertex(name = 'V_474',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_207,(0,2):C.GC_146,(0,3):C.GC_696,(0,1):C.GC_666})

V_475 = Vertex(name = 'V_475',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_228,(0,2):C.GC_356,(0,1):C.GC_3419})

V_476 = Vertex(name = 'V_476',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_367,(0,2):C.GC_358,(0,1):C.GC_3436})

V_477 = Vertex(name = 'V_477',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3316})

V_478 = Vertex(name = 'V_478',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3319})

V_479 = Vertex(name = 'V_479',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3317,(0,2):C.GC_3420,(0,0):C.GC_3336})

V_480 = Vertex(name = 'V_480',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3320,(0,2):C.GC_3437,(0,0):C.GC_3341})

V_481 = Vertex(name = 'V_481',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_4079,(0,2):C.GC_4132,(0,0):C.GC_4173})

V_482 = Vertex(name = 'V_482',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_4082,(0,2):C.GC_4149,(0,0):C.GC_4178})

V_483 = Vertex(name = 'V_483',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_4080,(0,2):C.GC_4133,(0,0):C.GC_4204})

V_484 = Vertex(name = 'V_484',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_4083,(0,2):C.GC_4150,(0,0):C.GC_4209})

V_485 = Vertex(name = 'V_485',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,0):C.GC_198,(0,2):C.GC_132,(0,5):C.GC_201,(0,4):C.GC_337,(0,3):C.GC_351,(0,1):C.GC_398})

V_486 = Vertex(name = 'V_486',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_207,(0,2):C.GC_146,(0,3):C.GC_416,(0,1):C.GC_405})

V_487 = Vertex(name = 'V_487',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_228,(0,2):C.GC_356,(0,1):C.GC_4134})

V_488 = Vertex(name = 'V_488',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_367,(0,2):C.GC_358,(0,1):C.GC_4151})

V_489 = Vertex(name = 'V_489',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_4081})

V_490 = Vertex(name = 'V_490',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_4084})

V_491 = Vertex(name = 'V_491',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_159})

V_492 = Vertex(name = 'V_492',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_162})

V_493 = Vertex(name = 'V_493',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_159})

V_494 = Vertex(name = 'V_494',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_162})

V_495 = Vertex(name = 'V_495',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_159})

V_496 = Vertex(name = 'V_496',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_162})

V_497 = Vertex(name = 'V_497',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_319,(0,2):C.GC_534})

V_498 = Vertex(name = 'V_498',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_541})

V_499 = Vertex(name = 'V_499',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_319,(0,2):C.GC_589})

V_500 = Vertex(name = 'V_500',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_596})

V_501 = Vertex(name = 'V_501',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_319,(0,2):C.GC_854})

V_502 = Vertex(name = 'V_502',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_861})

V_503 = Vertex(name = 'V_503',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_199,(0,3):C.GC_131,(0,5):C.GC_203,(0,6):C.GC_337,(0,4):C.GC_359,(0,1):C.GC_956,(0,2):C.GC_1036})

V_504 = Vertex(name = 'V_504',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_208,(0,2):C.GC_145,(0,3):C.GC_1035,(0,1):C.GC_963})

V_505 = Vertex(name = 'V_505',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_229,(0,2):C.GC_356,(0,1):C.GC_3962})

V_506 = Vertex(name = 'V_506',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_368,(0,2):C.GC_357,(0,1):C.GC_3974})

V_507 = Vertex(name = 'V_507',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3719})

V_508 = Vertex(name = 'V_508',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3722})

V_509 = Vertex(name = 'V_509',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2403,(0,2):C.GC_2591,(0,0):C.GC_2456})

V_510 = Vertex(name = 'V_510',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2406,(0,2):C.GC_2596,(0,0):C.GC_2473})

V_511 = Vertex(name = 'V_511',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3716,(0,2):C.GC_3961,(0,0):C.GC_3811})

V_512 = Vertex(name = 'V_512',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3720,(0,2):C.GC_3973,(0,0):C.GC_3828})

V_513 = Vertex(name = 'V_513',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1608,(0,2):C.GC_1627,(0,0):C.GC_1718})

V_514 = Vertex(name = 'V_514',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1610,(0,2):C.GC_1632,(0,0):C.GC_1728})

V_515 = Vertex(name = 'V_515',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_199,(0,2):C.GC_131,(0,4):C.GC_203,(0,5):C.GC_337,(0,3):C.GC_359,(0,1):C.GC_438})

V_516 = Vertex(name = 'V_516',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_208,(0,2):C.GC_145,(0,3):C.GC_463,(0,1):C.GC_445})

V_517 = Vertex(name = 'V_517',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_229,(0,2):C.GC_356,(0,1):C.GC_2457})

V_518 = Vertex(name = 'V_518',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_368,(0,2):C.GC_357,(0,1):C.GC_2474})

V_519 = Vertex(name = 'V_519',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2404})

V_520 = Vertex(name = 'V_520',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2407})

V_521 = Vertex(name = 'V_521',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3717,(0,2):C.GC_3739,(0,0):C.GC_3812})

V_522 = Vertex(name = 'V_522',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_3721,(0,2):C.GC_3744,(0,0):C.GC_3829})

V_523 = Vertex(name = 'V_523',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1609,(0,2):C.GC_1660,(0,0):C.GC_1719})

V_524 = Vertex(name = 'V_524',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_1611,(0,2):C.GC_1665,(0,0):C.GC_1729})

V_525 = Vertex(name = 'V_525',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2405,(0,2):C.GC_2530,(0,0):C.GC_2458})

V_526 = Vertex(name = 'V_526',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_2408,(0,2):C.GC_2535,(0,0):C.GC_2475})

V_527 = Vertex(name = 'V_527',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_199,(0,2):C.GC_131,(0,4):C.GC_203,(0,5):C.GC_337,(0,3):C.GC_359,(0,1):C.GC_738})

V_528 = Vertex(name = 'V_528',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_208,(0,2):C.GC_145,(0,3):C.GC_803,(0,1):C.GC_745})

V_529 = Vertex(name = 'V_529',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_229,(0,2):C.GC_356,(0,1):C.GC_3813})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV2 ],
               couplings = {(0,0):C.GC_368,(0,2):C.GC_357,(0,1):C.GC_3830})

V_531 = Vertex(name = 'V_531',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3718})

V_532 = Vertex(name = 'V_532',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3723})

V_533 = Vertex(name = 'V_533',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_166})

V_534 = Vertex(name = 'V_534',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_164,(0,1):C.GC_1033})

V_535 = Vertex(name = 'V_535',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3703})

V_536 = Vertex(name = 'V_536',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3706})

V_537 = Vertex(name = 'V_537',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2391})

V_538 = Vertex(name = 'V_538',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2394})

V_539 = Vertex(name = 'V_539',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3700})

V_540 = Vertex(name = 'V_540',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3704})

V_541 = Vertex(name = 'V_541',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1600})

V_542 = Vertex(name = 'V_542',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1602})

V_543 = Vertex(name = 'V_543',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_166})

V_544 = Vertex(name = 'V_544',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_164,(0,1):C.GC_461})

V_545 = Vertex(name = 'V_545',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2392})

V_546 = Vertex(name = 'V_546',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2395})

V_547 = Vertex(name = 'V_547',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3701})

V_548 = Vertex(name = 'V_548',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3705})

V_549 = Vertex(name = 'V_549',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1601})

V_550 = Vertex(name = 'V_550',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1603})

V_551 = Vertex(name = 'V_551',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2393})

V_552 = Vertex(name = 'V_552',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2396})

V_553 = Vertex(name = 'V_553',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_166})

V_554 = Vertex(name = 'V_554',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_164,(0,1):C.GC_801})

V_555 = Vertex(name = 'V_555',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3702})

V_556 = Vertex(name = 'V_556',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3707})

V_557 = Vertex(name = 'V_557',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4, L.FFVS5 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_326,(0,2):C.GC_942,(0,3):C.GC_2318})

V_558 = Vertex(name = 'V_558',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_324,(0,1):C.GC_1034,(0,2):C.GC_950})

V_559 = Vertex(name = 'V_559',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3711,(0,1):C.GC_3938})

V_560 = Vertex(name = 'V_560',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3714,(0,1):C.GC_3950})

V_561 = Vertex(name = 'V_561',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2397,(0,1):C.GC_2580,(0,2):C.GC_2421})

V_562 = Vertex(name = 'V_562',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2400,(0,1):C.GC_2585,(0,2):C.GC_2438})

V_563 = Vertex(name = 'V_563',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3708,(0,1):C.GC_3937,(0,2):C.GC_3776})

V_564 = Vertex(name = 'V_564',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3712,(0,1):C.GC_3949,(0,2):C.GC_3793})

V_565 = Vertex(name = 'V_565',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1604,(0,1):C.GC_1616,(0,2):C.GC_1696})

V_566 = Vertex(name = 'V_566',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1606,(0,1):C.GC_1621,(0,2):C.GC_1706})

V_567 = Vertex(name = 'V_567',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_326,(0,2):C.GC_424})

V_568 = Vertex(name = 'V_568',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_324,(0,1):C.GC_462,(0,2):C.GC_432})

V_569 = Vertex(name = 'V_569',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2398,(0,1):C.GC_2422})

V_570 = Vertex(name = 'V_570',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2401,(0,1):C.GC_2439})

V_571 = Vertex(name = 'V_571',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3709,(0,1):C.GC_3728,(0,2):C.GC_3777})

V_572 = Vertex(name = 'V_572',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3713,(0,1):C.GC_3733,(0,2):C.GC_3794})

V_573 = Vertex(name = 'V_573',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1605,(0,1):C.GC_1649,(0,2):C.GC_1697})

V_574 = Vertex(name = 'V_574',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1607,(0,1):C.GC_1654,(0,2):C.GC_1707})

V_575 = Vertex(name = 'V_575',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2399,(0,1):C.GC_2519,(0,2):C.GC_2423})

V_576 = Vertex(name = 'V_576',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2402,(0,1):C.GC_2524,(0,2):C.GC_2440})

V_577 = Vertex(name = 'V_577',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_323,(0,1):C.GC_326,(0,2):C.GC_722})

V_578 = Vertex(name = 'V_578',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_324,(0,1):C.GC_802,(0,2):C.GC_732})

V_579 = Vertex(name = 'V_579',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3710,(0,1):C.GC_3778})

V_580 = Vertex(name = 'V_580',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3715,(0,1):C.GC_3795})

V_581 = Vertex(name = 'V_581',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_131})

V_582 = Vertex(name = 'V_582',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_145})

V_583 = Vertex(name = 'V_583',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_202})

V_584 = Vertex(name = 'V_584',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_338})

V_585 = Vertex(name = 'V_585',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_353})

V_586 = Vertex(name = 'V_586',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_354})

V_587 = Vertex(name = 'V_587',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_131})

V_588 = Vertex(name = 'V_588',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_145})

V_589 = Vertex(name = 'V_589',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_202})

V_590 = Vertex(name = 'V_590',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_338})

V_591 = Vertex(name = 'V_591',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_353})

V_592 = Vertex(name = 'V_592',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_354})

V_593 = Vertex(name = 'V_593',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_131})

V_594 = Vertex(name = 'V_594',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_145})

V_595 = Vertex(name = 'V_595',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_202})

V_596 = Vertex(name = 'V_596',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_338})

V_597 = Vertex(name = 'V_597',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_353})

V_598 = Vertex(name = 'V_598',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_354})

V_599 = Vertex(name = 'V_599',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_160})

V_600 = Vertex(name = 'V_600',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_161})

V_601 = Vertex(name = 'V_601',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_160})

V_602 = Vertex(name = 'V_602',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_161})

V_603 = Vertex(name = 'V_603',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_160})

V_604 = Vertex(name = 'V_604',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_161})

V_605 = Vertex(name = 'V_605',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_320})

V_606 = Vertex(name = 'V_606',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_321})

V_607 = Vertex(name = 'V_607',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_320})

V_608 = Vertex(name = 'V_608',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_321})

V_609 = Vertex(name = 'V_609',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_320})

V_610 = Vertex(name = 'V_610',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_321})

V_611 = Vertex(name = 'V_611',
               particles = [ P.t__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_78})

V_612 = Vertex(name = 'V_612',
               particles = [ P.t1__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_83})

V_613 = Vertex(name = 'V_613',
               particles = [ P.t1__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_78})

V_614 = Vertex(name = 'V_614',
               particles = [ P.t__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_81})

V_615 = Vertex(name = 'V_615',
               particles = [ P.t1__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_86})

V_616 = Vertex(name = 'V_616',
               particles = [ P.t1__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_81})

V_617 = Vertex(name = 'V_617',
               particles = [ P.d__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_182})

V_618 = Vertex(name = 'V_618',
               particles = [ P.s__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_183})

V_619 = Vertex(name = 'V_619',
               particles = [ P.b__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_184})

V_620 = Vertex(name = 'V_620',
               particles = [ P.d__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_189})

V_621 = Vertex(name = 'V_621',
               particles = [ P.s__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_190})

V_622 = Vertex(name = 'V_622',
               particles = [ P.b__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_191})

V_623 = Vertex(name = 'V_623',
               particles = [ P.d__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_176})

V_624 = Vertex(name = 'V_624',
               particles = [ P.s__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_177})

V_625 = Vertex(name = 'V_625',
               particles = [ P.b__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_178})

V_626 = Vertex(name = 'V_626',
               particles = [ P.d__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_179})

V_627 = Vertex(name = 'V_627',
               particles = [ P.s__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_180})

V_628 = Vertex(name = 'V_628',
               particles = [ P.b__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_181})

V_629 = Vertex(name = 'V_629',
               particles = [ P.d__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_182})

V_630 = Vertex(name = 'V_630',
               particles = [ P.s__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_183})

V_631 = Vertex(name = 'V_631',
               particles = [ P.b__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_184})

V_632 = Vertex(name = 'V_632',
               particles = [ P.e__plus__, P.ve, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_633 = Vertex(name = 'V_633',
               particles = [ P.mu__plus__, P.vm, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_634 = Vertex(name = 'V_634',
               particles = [ P.ta__plus__, P.vt, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_635 = Vertex(name = 'V_635',
               particles = [ P.t1__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2711})

V_636 = Vertex(name = 'V_636',
               particles = [ P.t1__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3058})

V_637 = Vertex(name = 'V_637',
               particles = [ P.t1__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3487})

V_638 = Vertex(name = 'V_638',
               particles = [ P.u__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1138})

V_639 = Vertex(name = 'V_639',
               particles = [ P.c__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1826})

V_640 = Vertex(name = 'V_640',
               particles = [ P.t__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2710})

V_641 = Vertex(name = 'V_641',
               particles = [ P.u__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1286})

V_642 = Vertex(name = 'V_642',
               particles = [ P.c__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1999})

V_643 = Vertex(name = 'V_643',
               particles = [ P.t__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3057})

V_644 = Vertex(name = 'V_644',
               particles = [ P.u__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1458})

V_645 = Vertex(name = 'V_645',
               particles = [ P.c__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2195})

V_646 = Vertex(name = 'V_646',
               particles = [ P.t__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3486})

V_647 = Vertex(name = 'V_647',
               particles = [ P.ve__tilde__, P.e__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_648 = Vertex(name = 'V_648',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_649 = Vertex(name = 'V_649',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_175})

V_650 = Vertex(name = 'V_650',
               particles = [ P.t1__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2710})

V_651 = Vertex(name = 'V_651',
               particles = [ P.t1__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3057})

V_652 = Vertex(name = 'V_652',
               particles = [ P.t1__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3486})

V_653 = Vertex(name = 'V_653',
               particles = [ P.t__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_185})

V_654 = Vertex(name = 'V_654',
               particles = [ P.t1__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_192})

V_655 = Vertex(name = 'V_655',
               particles = [ P.t1__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_185})

V_656 = Vertex(name = 'V_656',
               particles = [ P.d__tilde__, P.d, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_186})

V_657 = Vertex(name = 'V_657',
               particles = [ P.s__tilde__, P.s, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_186})

V_658 = Vertex(name = 'V_658',
               particles = [ P.b__tilde__, P.b, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_186})

V_659 = Vertex(name = 'V_659',
               particles = [ P.e__plus__, P.e__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_186})

V_660 = Vertex(name = 'V_660',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_186})

V_661 = Vertex(name = 'V_661',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_218,(0,1):C.GC_186})

V_662 = Vertex(name = 'V_662',
               particles = [ P.t__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_192})

V_663 = Vertex(name = 'V_663',
               particles = [ P.t1__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_220,(0,1):C.GC_195})

V_664 = Vertex(name = 'V_664',
               particles = [ P.t1__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_192})

V_665 = Vertex(name = 'V_665',
               particles = [ P.u__tilde__, P.u, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_185})

V_666 = Vertex(name = 'V_666',
               particles = [ P.c__tilde__, P.c, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_185})

V_667 = Vertex(name = 'V_667',
               particles = [ P.t__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_217,(0,1):C.GC_185})

V_668 = Vertex(name = 'V_668',
               particles = [ P.ve__tilde__, P.ve, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_185})

V_669 = Vertex(name = 'V_669',
               particles = [ P.vm__tilde__, P.vm, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_185})

V_670 = Vertex(name = 'V_670',
               particles = [ P.vt__tilde__, P.vt, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_185})

V_671 = Vertex(name = 'V_671',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_470})

V_672 = Vertex(name = 'V_672',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_471})

V_673 = Vertex(name = 'V_673',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_472})

V_674 = Vertex(name = 'V_674',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_500})

V_675 = Vertex(name = 'V_675',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2675})

V_676 = Vertex(name = 'V_676',
               particles = [ P.s__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2989,(0,1):C.GC_3019})

V_677 = Vertex(name = 'V_677',
               particles = [ P.b__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2990,(0,1):C.GC_2944})

V_678 = Vertex(name = 'V_678',
               particles = [ P.d__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3441,(0,1):C.GC_3366})

V_679 = Vertex(name = 'V_679',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_638})

V_680 = Vertex(name = 'V_680',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_639})

V_681 = Vertex(name = 'V_681',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_640})

V_682 = Vertex(name = 'V_682',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_668})

V_683 = Vertex(name = 'V_683',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_3442})

V_684 = Vertex(name = 'V_684',
               particles = [ P.b__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3443,(0,1):C.GC_3343})

V_685 = Vertex(name = 'V_685',
               particles = [ P.d__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_4155,(0,1):C.GC_4180})

V_686 = Vertex(name = 'V_686',
               particles = [ P.s__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_4156,(0,1):C.GC_4211})

V_687 = Vertex(name = 'V_687',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_377})

V_688 = Vertex(name = 'V_688',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_378})

V_689 = Vertex(name = 'V_689',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_379})

V_690 = Vertex(name = 'V_690',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_407})

V_691 = Vertex(name = 'V_691',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_4157})

V_692 = Vertex(name = 'V_692',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_474})

V_693 = Vertex(name = 'V_693',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_2650})

V_694 = Vertex(name = 'V_694',
               particles = [ P.s__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2949,(0,1):C.GC_2999})

V_695 = Vertex(name = 'V_695',
               particles = [ P.b__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2950,(0,1):C.GC_2924})

V_696 = Vertex(name = 'V_696',
               particles = [ P.d__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3377,(0,1):C.GC_3346})

V_697 = Vertex(name = 'V_697',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_642})

V_698 = Vertex(name = 'V_698',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3378})

V_699 = Vertex(name = 'V_699',
               particles = [ P.b__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3379,(0,1):C.GC_3323})

V_700 = Vertex(name = 'V_700',
               particles = [ P.d__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_4091,(0,1):C.GC_4160})

V_701 = Vertex(name = 'V_701',
               particles = [ P.s__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_4092,(0,1):C.GC_4191})

V_702 = Vertex(name = 'V_702',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_381})

V_703 = Vertex(name = 'V_703',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_4093})

V_704 = Vertex(name = 'V_704',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_488})

V_705 = Vertex(name = 'V_705',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_2663})

V_706 = Vertex(name = 'V_706',
               particles = [ P.s__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2971,(0,1):C.GC_3010})

V_707 = Vertex(name = 'V_707',
               particles = [ P.b__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2972,(0,1):C.GC_2935})

V_708 = Vertex(name = 'V_708',
               particles = [ P.d__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3412,(0,1):C.GC_3357})

V_709 = Vertex(name = 'V_709',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_656})

V_710 = Vertex(name = 'V_710',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_3413})

V_711 = Vertex(name = 'V_711',
               particles = [ P.b__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3414,(0,1):C.GC_3334})

V_712 = Vertex(name = 'V_712',
               particles = [ P.d__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_4126,(0,1):C.GC_4171})

V_713 = Vertex(name = 'V_713',
               particles = [ P.s__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_4127,(0,1):C.GC_4202})

V_714 = Vertex(name = 'V_714',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_395})

V_715 = Vertex(name = 'V_715',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_4128})

V_716 = Vertex(name = 'V_716',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_528})

V_717 = Vertex(name = 'V_717',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_529})

V_718 = Vertex(name = 'V_718',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_530})

V_719 = Vertex(name = 'V_719',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_554})

V_720 = Vertex(name = 'V_720',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_583})

V_721 = Vertex(name = 'V_721',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_584})

V_722 = Vertex(name = 'V_722',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_585})

V_723 = Vertex(name = 'V_723',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_609})

V_724 = Vertex(name = 'V_724',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_848})

V_725 = Vertex(name = 'V_725',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_849})

V_726 = Vertex(name = 'V_726',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_850})

V_727 = Vertex(name = 'V_727',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_874})

V_728 = Vertex(name = 'V_728',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_531})

V_729 = Vertex(name = 'V_729',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_586})

V_730 = Vertex(name = 'V_730',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_851})

V_731 = Vertex(name = 'V_731',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_543})

V_732 = Vertex(name = 'V_732',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_598})

V_733 = Vertex(name = 'V_733',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_863})

V_734 = Vertex(name = 'V_734',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_935})

V_735 = Vertex(name = 'V_735',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_936})

V_736 = Vertex(name = 'V_736',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_937})

V_737 = Vertex(name = 'V_737',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_965})

V_738 = Vertex(name = 'V_738',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_3978})

V_739 = Vertex(name = 'V_739',
               particles = [ P.c__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2598,(0,1):C.GC_2479})

V_740 = Vertex(name = 'V_740',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3977,(0,1):C.GC_3834})

V_741 = Vertex(name = 'V_741',
               particles = [ P.u__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_1634,(0,1):C.GC_1732})

V_742 = Vertex(name = 'V_742',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_417})

V_743 = Vertex(name = 'V_743',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_418})

V_744 = Vertex(name = 'V_744',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_419})

V_745 = Vertex(name = 'V_745',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_447})

V_746 = Vertex(name = 'V_746',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2480})

V_747 = Vertex(name = 'V_747',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3746,(0,1):C.GC_3835})

V_748 = Vertex(name = 'V_748',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_1667,(0,1):C.GC_1733})

V_749 = Vertex(name = 'V_749',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2537,(0,1):C.GC_2481})

V_750 = Vertex(name = 'V_750',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_715})

V_751 = Vertex(name = 'V_751',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_716})

V_752 = Vertex(name = 'V_752',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_717})

V_753 = Vertex(name = 'V_753',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_747})

V_754 = Vertex(name = 'V_754',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_3836})

V_755 = Vertex(name = 'V_755',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_940})

V_756 = Vertex(name = 'V_756',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3934})

V_757 = Vertex(name = 'V_757',
               particles = [ P.c__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2578,(0,1):C.GC_2415})

V_758 = Vertex(name = 'V_758',
               particles = [ P.t__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3933,(0,1):C.GC_3770})

V_759 = Vertex(name = 'V_759',
               particles = [ P.u__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_1614,(0,1):C.GC_1692})

V_760 = Vertex(name = 'V_760',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_422})

V_761 = Vertex(name = 'V_761',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_2416})

V_762 = Vertex(name = 'V_762',
               particles = [ P.t__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3726,(0,1):C.GC_3771})

V_763 = Vertex(name = 'V_763',
               particles = [ P.u__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_1647,(0,1):C.GC_1693})

V_764 = Vertex(name = 'V_764',
               particles = [ P.c__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2517,(0,1):C.GC_2417})

V_765 = Vertex(name = 'V_765',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_720})

V_766 = Vertex(name = 'V_766',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3772})

V_767 = Vertex(name = 'V_767',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_954})

V_768 = Vertex(name = 'V_768',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_3958})

V_769 = Vertex(name = 'V_769',
               particles = [ P.c__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2589,(0,1):C.GC_2450})

V_770 = Vertex(name = 'V_770',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3957,(0,1):C.GC_3805})

V_771 = Vertex(name = 'V_771',
               particles = [ P.u__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_1625,(0,1):C.GC_1714})

V_772 = Vertex(name = 'V_772',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_436})

V_773 = Vertex(name = 'V_773',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_2451})

V_774 = Vertex(name = 'V_774',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3737,(0,1):C.GC_3806})

V_775 = Vertex(name = 'V_775',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_1658,(0,1):C.GC_1715})

V_776 = Vertex(name = 'V_776',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2528,(0,1):C.GC_2452})

V_777 = Vertex(name = 'V_777',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_736})

V_778 = Vertex(name = 'V_778',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_3807})

V_779 = Vertex(name = 'V_779',
               particles = [ P.d__tilde__, P.d, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_481})

V_780 = Vertex(name = 'V_780',
               particles = [ P.s__tilde__, P.s, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_649})

V_781 = Vertex(name = 'V_781',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_388})

V_782 = Vertex(name = 'V_782',
               particles = [ P.e__plus__, P.e__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_537})

V_783 = Vertex(name = 'V_783',
               particles = [ P.mu__plus__, P.mu__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_592})

V_784 = Vertex(name = 'V_784',
               particles = [ P.ta__plus__, P.ta__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_857})

V_785 = Vertex(name = 'V_785',
               particles = [ P.t__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_726})

V_786 = Vertex(name = 'V_786',
               particles = [ P.t__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_727})

V_787 = Vertex(name = 'V_787',
               particles = [ P.t1__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_727})

V_788 = Vertex(name = 'V_788',
               particles = [ P.t1__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_728})

V_789 = Vertex(name = 'V_789',
               particles = [ P.t1__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_726})

V_790 = Vertex(name = 'V_790',
               particles = [ P.t1__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_727})

V_791 = Vertex(name = 'V_791',
               particles = [ P.u__tilde__, P.u, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_946})

V_792 = Vertex(name = 'V_792',
               particles = [ P.c__tilde__, P.c, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_428})

V_793 = Vertex(name = 'V_793',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_726})

V_794 = Vertex(name = 'V_794',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_476})

V_795 = Vertex(name = 'V_795',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_486})

V_796 = Vertex(name = 'V_796',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2648})

V_797 = Vertex(name = 'V_797',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2660})

V_798 = Vertex(name = 'V_798',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2945,(0,1):C.GC_2997})

V_799 = Vertex(name = 'V_799',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2965,(0,1):C.GC_3007})

V_800 = Vertex(name = 'V_800',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2946,(0,1):C.GC_2922})

V_801 = Vertex(name = 'V_801',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2966,(0,1):C.GC_2932})

V_802 = Vertex(name = 'V_802',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3371,(0,1):C.GC_3344})

V_803 = Vertex(name = 'V_803',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3403,(0,1):C.GC_3354})

V_804 = Vertex(name = 'V_804',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_644})

V_805 = Vertex(name = 'V_805',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_654})

V_806 = Vertex(name = 'V_806',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3372})

V_807 = Vertex(name = 'V_807',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3404})

V_808 = Vertex(name = 'V_808',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3373,(0,1):C.GC_3321})

V_809 = Vertex(name = 'V_809',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3405,(0,1):C.GC_3331})

V_810 = Vertex(name = 'V_810',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4085,(0,1):C.GC_4158})

V_811 = Vertex(name = 'V_811',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4117,(0,1):C.GC_4168})

V_812 = Vertex(name = 'V_812',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4086,(0,1):C.GC_4189})

V_813 = Vertex(name = 'V_813',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4118,(0,1):C.GC_4199})

V_814 = Vertex(name = 'V_814',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_383})

V_815 = Vertex(name = 'V_815',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_393})

V_816 = Vertex(name = 'V_816',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4087})

V_817 = Vertex(name = 'V_817',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4119})

V_818 = Vertex(name = 'V_818',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2967,(0,0):C.GC_3008})

V_819 = Vertex(name = 'V_819',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2987,(0,0):C.GC_3018})

V_820 = Vertex(name = 'V_820',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2968,(0,0):C.GC_2933})

V_821 = Vertex(name = 'V_821',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2988,(0,0):C.GC_2943})

V_822 = Vertex(name = 'V_822',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3406,(0,0):C.GC_3355})

V_823 = Vertex(name = 'V_823',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3438,(0,0):C.GC_3365})

V_824 = Vertex(name = 'V_824',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3408,(0,0):C.GC_3332})

V_825 = Vertex(name = 'V_825',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3440,(0,0):C.GC_3342})

V_826 = Vertex(name = 'V_826',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4120,(0,0):C.GC_4169})

V_827 = Vertex(name = 'V_827',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4152,(0,0):C.GC_4179})

V_828 = Vertex(name = 'V_828',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4121,(0,0):C.GC_4200})

V_829 = Vertex(name = 'V_829',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4153,(0,0):C.GC_4210})

V_830 = Vertex(name = 'V_830',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_473})

V_831 = Vertex(name = 'V_831',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2649})

V_832 = Vertex(name = 'V_832',
               particles = [ P.s__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2947,(0,1):C.GC_2998})

V_833 = Vertex(name = 'V_833',
               particles = [ P.b__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2948,(0,1):C.GC_2923})

V_834 = Vertex(name = 'V_834',
               particles = [ P.d__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3374,(0,1):C.GC_3345})

V_835 = Vertex(name = 'V_835',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_641})

V_836 = Vertex(name = 'V_836',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3375})

V_837 = Vertex(name = 'V_837',
               particles = [ P.b__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3376,(0,1):C.GC_3322})

V_838 = Vertex(name = 'V_838',
               particles = [ P.d__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4088,(0,1):C.GC_4159})

V_839 = Vertex(name = 'V_839',
               particles = [ P.s__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_4089,(0,1):C.GC_4190})

V_840 = Vertex(name = 'V_840',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_380})

V_841 = Vertex(name = 'V_841',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4090})

V_842 = Vertex(name = 'V_842',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2969,(0,0):C.GC_3009})

V_843 = Vertex(name = 'V_843',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2970,(0,0):C.GC_2934})

V_844 = Vertex(name = 'V_844',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3409,(0,0):C.GC_3356})

V_845 = Vertex(name = 'V_845',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3411,(0,0):C.GC_3333})

V_846 = Vertex(name = 'V_846',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4123,(0,0):C.GC_4170})

V_847 = Vertex(name = 'V_847',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_4124,(0,0):C.GC_4201})

V_848 = Vertex(name = 'V_848',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_480})

V_849 = Vertex(name = 'V_849',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_2655})

V_850 = Vertex(name = 'V_850',
               particles = [ P.s__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2957,(0,1):C.GC_3003})

V_851 = Vertex(name = 'V_851',
               particles = [ P.b__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2958,(0,1):C.GC_2928})

V_852 = Vertex(name = 'V_852',
               particles = [ P.d__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3390,(0,1):C.GC_3350})

V_853 = Vertex(name = 'V_853',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_648})

V_854 = Vertex(name = 'V_854',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_3391})

V_855 = Vertex(name = 'V_855',
               particles = [ P.b__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3392,(0,1):C.GC_3327})

V_856 = Vertex(name = 'V_856',
               particles = [ P.d__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4104,(0,1):C.GC_4164})

V_857 = Vertex(name = 'V_857',
               particles = [ P.s__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4105,(0,1):C.GC_4195})

V_858 = Vertex(name = 'V_858',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_387})

V_859 = Vertex(name = 'V_859',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_4106})

V_860 = Vertex(name = 'V_860',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_494})

V_861 = Vertex(name = 'V_861',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_2669})

V_862 = Vertex(name = 'V_862',
               particles = [ P.s__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2979,(0,1):C.GC_3014})

V_863 = Vertex(name = 'V_863',
               particles = [ P.b__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2980,(0,1):C.GC_2939})

V_864 = Vertex(name = 'V_864',
               particles = [ P.d__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3425,(0,1):C.GC_3361})

V_865 = Vertex(name = 'V_865',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_662})

V_866 = Vertex(name = 'V_866',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_3426})

V_867 = Vertex(name = 'V_867',
               particles = [ P.b__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3427,(0,1):C.GC_3338})

V_868 = Vertex(name = 'V_868',
               particles = [ P.d__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4139,(0,1):C.GC_4175})

V_869 = Vertex(name = 'V_869',
               particles = [ P.s__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4140,(0,1):C.GC_4206})

V_870 = Vertex(name = 'V_870',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_401})

V_871 = Vertex(name = 'V_871',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_4141})

V_872 = Vertex(name = 'V_872',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_479,(0,1):C.GC_944})

V_873 = Vertex(name = 'V_873',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2654,(0,1):C.GC_3941})

V_874 = Vertex(name = 'V_874',
               particles = [ P.c__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2955,(0,1):C.GC_2424})

V_875 = Vertex(name = 'V_875',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2956,(0,1):C.GC_3779})

V_876 = Vertex(name = 'V_876',
               particles = [ P.u__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3386,(0,1):C.GC_1698})

V_877 = Vertex(name = 'V_877',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_647,(0,1):C.GC_426})

V_878 = Vertex(name = 'V_878',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3387,(0,1):C.GC_2425})

V_879 = Vertex(name = 'V_879',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3389,(0,1):C.GC_3780})

V_880 = Vertex(name = 'V_880',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4100,(0,1):C.GC_1699})

V_881 = Vertex(name = 'V_881',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4101,(0,1):C.GC_2427})

V_882 = Vertex(name = 'V_882',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_386,(0,1):C.GC_724})

V_883 = Vertex(name = 'V_883',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4102,(0,1):C.GC_3781})

V_884 = Vertex(name = 'V_884',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_493,(0,1):C.GC_958})

V_885 = Vertex(name = 'V_885',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2668,(0,1):C.GC_3965})

V_886 = Vertex(name = 'V_886',
               particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2977,(0,1):C.GC_2459})

V_887 = Vertex(name = 'V_887',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2978,(0,1):C.GC_3814})

V_888 = Vertex(name = 'V_888',
               particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3421,(0,1):C.GC_1720})

V_889 = Vertex(name = 'V_889',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_661,(0,1):C.GC_440})

V_890 = Vertex(name = 'V_890',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3422,(0,1):C.GC_2460})

V_891 = Vertex(name = 'V_891',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3424,(0,1):C.GC_3815})

V_892 = Vertex(name = 'V_892',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4135,(0,1):C.GC_1721})

V_893 = Vertex(name = 'V_893',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4136,(0,1):C.GC_2462})

V_894 = Vertex(name = 'V_894',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_400,(0,1):C.GC_740})

V_895 = Vertex(name = 'V_895',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4137,(0,1):C.GC_3816})

V_896 = Vertex(name = 'V_896',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_482})

V_897 = Vertex(name = 'V_897',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_2656})

V_898 = Vertex(name = 'V_898',
               particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2959,(0,1):C.GC_3004})

V_899 = Vertex(name = 'V_899',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2960,(0,1):C.GC_2929})

V_900 = Vertex(name = 'V_900',
               particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3393,(0,1):C.GC_3351})

V_901 = Vertex(name = 'V_901',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_650})

V_902 = Vertex(name = 'V_902',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_3394})

V_903 = Vertex(name = 'V_903',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3395,(0,1):C.GC_3328})

V_904 = Vertex(name = 'V_904',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4107,(0,1):C.GC_4165})

V_905 = Vertex(name = 'V_905',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4108,(0,1):C.GC_4196})

V_906 = Vertex(name = 'V_906',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_389})

V_907 = Vertex(name = 'V_907',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_4109})

V_908 = Vertex(name = 'V_908',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_495})

V_909 = Vertex(name = 'V_909',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_2670})

V_910 = Vertex(name = 'V_910',
               particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3, L.FFVV5 ],
               couplings = {(0,0):C.GC_2981,(0,1):C.GC_3015,(0,2):C.GC_1886})

V_911 = Vertex(name = 'V_911',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2982,(0,1):C.GC_2940})

V_912 = Vertex(name = 'V_912',
               particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3428,(0,1):C.GC_3362})

V_913 = Vertex(name = 'V_913',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_663})

V_914 = Vertex(name = 'V_914',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_3429})

V_915 = Vertex(name = 'V_915',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3430,(0,1):C.GC_3339})

V_916 = Vertex(name = 'V_916',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4142,(0,1):C.GC_4176})

V_917 = Vertex(name = 'V_917',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4143,(0,1):C.GC_4207})

V_918 = Vertex(name = 'V_918',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_402})

V_919 = Vertex(name = 'V_919',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_4144})

V_920 = Vertex(name = 'V_920',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_533})

V_921 = Vertex(name = 'V_921',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_542})

V_922 = Vertex(name = 'V_922',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_588})

V_923 = Vertex(name = 'V_923',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_597})

V_924 = Vertex(name = 'V_924',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_853})

V_925 = Vertex(name = 'V_925',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_862})

V_926 = Vertex(name = 'V_926',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_536})

V_927 = Vertex(name = 'V_927',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_591})

V_928 = Vertex(name = 'V_928',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_856})

V_929 = Vertex(name = 'V_929',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_548})

V_930 = Vertex(name = 'V_930',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_603})

V_931 = Vertex(name = 'V_931',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_868})

V_932 = Vertex(name = 'V_932',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_538})

V_933 = Vertex(name = 'V_933',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_593})

V_934 = Vertex(name = 'V_934',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_858})

V_935 = Vertex(name = 'V_935',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_549})

V_936 = Vertex(name = 'V_936',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_604})

V_937 = Vertex(name = 'V_937',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_869})

V_938 = Vertex(name = 'V_938',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_938})

V_939 = Vertex(name = 'V_939',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_951})

V_940 = Vertex(name = 'V_940',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3930})

V_941 = Vertex(name = 'V_941',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3952})

V_942 = Vertex(name = 'V_942',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2576,(0,1):C.GC_2409})

V_943 = Vertex(name = 'V_943',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2586,(0,1):C.GC_2441})

V_944 = Vertex(name = 'V_944',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3929,(0,1):C.GC_3764})

V_945 = Vertex(name = 'V_945',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3951,(0,1):C.GC_3796})

V_946 = Vertex(name = 'V_946',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1612,(0,1):C.GC_1688})

V_947 = Vertex(name = 'V_947',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1622,(0,1):C.GC_1708})

V_948 = Vertex(name = 'V_948',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_420})

V_949 = Vertex(name = 'V_949',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_433})

V_950 = Vertex(name = 'V_950',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2410})

V_951 = Vertex(name = 'V_951',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2442})

V_952 = Vertex(name = 'V_952',
               particles = [ P.t__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3724,(0,1):C.GC_3765})

V_953 = Vertex(name = 'V_953',
               particles = [ P.t__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3734,(0,1):C.GC_3797})

V_954 = Vertex(name = 'V_954',
               particles = [ P.u__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1645,(0,1):C.GC_1689})

V_955 = Vertex(name = 'V_955',
               particles = [ P.u__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1655,(0,1):C.GC_1709})

V_956 = Vertex(name = 'V_956',
               particles = [ P.c__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6, L.FFVS7 ],
               couplings = {(0,0):C.GC_2515,(0,1):C.GC_2411,(0,2):C.GC_2221})

V_957 = Vertex(name = 'V_957',
               particles = [ P.c__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2525,(0,1):C.GC_2443})

V_958 = Vertex(name = 'V_958',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_718})

V_959 = Vertex(name = 'V_959',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_733})

V_960 = Vertex(name = 'V_960',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3766})

V_961 = Vertex(name = 'V_961',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3798})

V_962 = Vertex(name = 'V_962',
               particles = [ P.c__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2587,(0,0):C.GC_2444})

V_963 = Vertex(name = 'V_963',
               particles = [ P.c__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2597,(0,0):C.GC_2476})

V_964 = Vertex(name = 'V_964',
               particles = [ P.t__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3953,(0,0):C.GC_3799})

V_965 = Vertex(name = 'V_965',
               particles = [ P.t__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3975,(0,0):C.GC_3831})

V_966 = Vertex(name = 'V_966',
               particles = [ P.u__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1623,(0,0):C.GC_1710})

V_967 = Vertex(name = 'V_967',
               particles = [ P.u__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1633,(0,0):C.GC_1730})

V_968 = Vertex(name = 'V_968',
               particles = [ P.t__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3735,(0,0):C.GC_3800})

V_969 = Vertex(name = 'V_969',
               particles = [ P.t__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3745,(0,0):C.GC_3832})

V_970 = Vertex(name = 'V_970',
               particles = [ P.u__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1656,(0,0):C.GC_1711})

V_971 = Vertex(name = 'V_971',
               particles = [ P.u__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1666,(0,0):C.GC_1731})

V_972 = Vertex(name = 'V_972',
               particles = [ P.c__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2526,(0,0):C.GC_2446})

V_973 = Vertex(name = 'V_973',
               particles = [ P.c__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2536,(0,0):C.GC_2478})

V_974 = Vertex(name = 'V_974',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_939})

V_975 = Vertex(name = 'V_975',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3932})

V_976 = Vertex(name = 'V_976',
               particles = [ P.c__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2577,(0,1):C.GC_2412})

V_977 = Vertex(name = 'V_977',
               particles = [ P.t__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3931,(0,1):C.GC_3767})

V_978 = Vertex(name = 'V_978',
               particles = [ P.u__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1613,(0,1):C.GC_1690})

V_979 = Vertex(name = 'V_979',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_421})

V_980 = Vertex(name = 'V_980',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2413})

V_981 = Vertex(name = 'V_981',
               particles = [ P.t__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_3725,(0,1):C.GC_3768})

V_982 = Vertex(name = 'V_982',
               particles = [ P.u__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_1646,(0,1):C.GC_1691})

V_983 = Vertex(name = 'V_983',
               particles = [ P.c__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS6 ],
               couplings = {(0,0):C.GC_2516,(0,1):C.GC_2414})

V_984 = Vertex(name = 'V_984',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_719})

V_985 = Vertex(name = 'V_985',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3769})

V_986 = Vertex(name = 'V_986',
               particles = [ P.c__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2588,(0,0):C.GC_2447})

V_987 = Vertex(name = 'V_987',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3955,(0,0):C.GC_3802})

V_988 = Vertex(name = 'V_988',
               particles = [ P.u__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1624,(0,0):C.GC_1712})

V_989 = Vertex(name = 'V_989',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_3736,(0,0):C.GC_3803})

V_990 = Vertex(name = 'V_990',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_1657,(0,0):C.GC_1713})

V_991 = Vertex(name = 'V_991',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV3 ],
               couplings = {(0,1):C.GC_2527,(0,0):C.GC_2449})

V_992 = Vertex(name = 'V_992',
               particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_945})

V_993 = Vertex(name = 'V_993',
               particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_3943})

V_994 = Vertex(name = 'V_994',
               particles = [ P.c__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2582,(0,1):C.GC_2428})

V_995 = Vertex(name = 'V_995',
               particles = [ P.t__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3942,(0,1):C.GC_3783})

V_996 = Vertex(name = 'V_996',
               particles = [ P.u__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_1618,(0,1):C.GC_1700})

V_997 = Vertex(name = 'V_997',
               particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_427})

V_998 = Vertex(name = 'V_998',
               particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_2429})

V_999 = Vertex(name = 'V_999',
               particles = [ P.t__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3730,(0,1):C.GC_3784})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.u__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1651,(0,1):C.GC_1701})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.c__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2521,(0,1):C.GC_2430})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_725})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3785})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_959})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3967})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.c__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2593,(0,1):C.GC_2463})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.t__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3966,(0,1):C.GC_3818})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.u__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1629,(0,1):C.GC_1722})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_441})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2464})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.t__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3741,(0,1):C.GC_3819})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.u__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1662,(0,1):C.GC_1723})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.c__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2532,(0,1):C.GC_2465})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_741})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3820})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_943,(0,1):C.GC_478})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3940,(0,1):C.GC_2653})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2581,(0,1):C.GC_3002})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3939,(0,1):C.GC_2927})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1617,(0,1):C.GC_3349})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_425,(0,1):C.GC_646})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2426,(0,1):C.GC_3388})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3729,(0,1):C.GC_3326})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1650,(0,1):C.GC_4163})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2520,(0,1):C.GC_4194})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_723,(0,1):C.GC_385})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3782,(0,1):C.GC_4103})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_957,(0,1):C.GC_492})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3964,(0,1):C.GC_2667})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2592,(0,1):C.GC_3013})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3963,(0,1):C.GC_2938})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1628,(0,1):C.GC_3360})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_439,(0,1):C.GC_660})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2461,(0,1):C.GC_3423})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3740,(0,1):C.GC_3337})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1661,(0,1):C.GC_4174})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2531,(0,1):C.GC_4205})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_739,(0,1):C.GC_399})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3817,(0,1):C.GC_4138})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_947})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3945})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2583,(0,1):C.GC_2431})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3944,(0,1):C.GC_3786})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1619,(0,1):C.GC_1702})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_429})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_2432})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3731,(0,1):C.GC_3787})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1652,(0,1):C.GC_1703})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2522,(0,1):C.GC_2433})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_729})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3788})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_960})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3969})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2594,(0,1):C.GC_2466})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3968,(0,1):C.GC_3821})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1630,(0,1):C.GC_1724})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_442})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2467})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3742,(0,1):C.GC_3822})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1663,(0,1):C.GC_1725})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2533,(0,1):C.GC_2468})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_742})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3823})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_483,(0,1):C.GC_948})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2657,(0,1):C.GC_3947})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2961,(0,1):C.GC_2434})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2962,(0,1):C.GC_3789})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3396,(0,1):C.GC_1704})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_651,(0,1):C.GC_430})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3398,(0,1):C.GC_2436})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3399,(0,1):C.GC_3790})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4110,(0,1):C.GC_1705})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4111,(0,1):C.GC_2437})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_390,(0,1):C.GC_730})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4113,(0,1):C.GC_3792})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_496,(0,1):C.GC_961})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2671,(0,1):C.GC_3971})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2983,(0,1):C.GC_2469})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2984,(0,1):C.GC_3824})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3431,(0,1):C.GC_1726})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_664,(0,1):C.GC_443})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3433,(0,1):C.GC_2471})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3434,(0,1):C.GC_3825})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4145,(0,1):C.GC_1727})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4146,(0,1):C.GC_2472})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_403,(0,1):C.GC_743})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4148,(0,1):C.GC_3827})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_539})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_594})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_859})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_550})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_605})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_870})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_949,(0,1):C.GC_484})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3948,(0,1):C.GC_2658})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2584,(0,1):C.GC_3005})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3946,(0,1):C.GC_2930})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1620,(0,1):C.GC_3352})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_431,(0,1):C.GC_652})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2435,(0,1):C.GC_3397})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3732,(0,1):C.GC_3329})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1653,(0,1):C.GC_4166})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2523,(0,1):C.GC_4197})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_731,(0,1):C.GC_391})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3791,(0,1):C.GC_4112})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_962,(0,1):C.GC_497})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3972,(0,1):C.GC_2672})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2595,(0,1):C.GC_3016})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3970,(0,1):C.GC_2941})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1631,(0,1):C.GC_3363})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_444,(0,1):C.GC_665})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2470,(0,1):C.GC_3432})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3743,(0,1):C.GC_3340})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1664,(0,1):C.GC_4177})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2534,(0,1):C.GC_4208})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_744,(0,1):C.GC_404})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3826,(0,1):C.GC_4147})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_535})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_590})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_855})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_547})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_602})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_867})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_540})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_595})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_860})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_551})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_606})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_871})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(0,0):C.GC_48,(2,0):C.GC_49,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_48,(2,4):C.GC_49,(0,5):C.GC_20})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(0,0):C.GC_2608,(2,0):C.GC_2609,(1,3):C.GC_2608,(3,3):C.GC_2609,(1,1):C.GC_2608,(3,1):C.GC_2609,(1,2):C.GC_21,(0,4):C.GC_2608,(2,4):C.GC_2609,(0,5):C.GC_21})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(0,0):C.GC_1099,(2,0):C.GC_1100,(1,3):C.GC_1099,(3,3):C.GC_1100,(1,1):C.GC_1099,(3,1):C.GC_1100,(1,2):C.GC_513,(0,4):C.GC_1099,(2,4):C.GC_1100,(0,5):C.GC_513})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_514,(0,1):C.GC_514})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2622,(0,1):C.GC_2622})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2628,(0,1):C.GC_2628})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2634,(0,1):C.GC_2634})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2640,(0,1):C.GC_2640})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2894,(0,5):C.GC_2894,(0,0):C.GC_1887,(2,0):C.GC_1890,(1,2):C.GC_1155,(3,2):C.GC_1157,(1,1):C.GC_1887,(3,1):C.GC_1890,(0,3):C.GC_1155,(2,3):C.GC_1157})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2898,(0,3):C.GC_2898,(1,0):C.GC_2878,(3,0):C.GC_2880,(0,1):C.GC_2878,(2,1):C.GC_2880})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2902,(0,1):C.GC_2902})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2908,(0,1):C.GC_2908})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2895,(0,5):C.GC_2895,(0,0):C.GC_2720,(2,0):C.GC_2723,(1,2):C.GC_1156,(3,2):C.GC_1158,(1,1):C.GC_2720,(3,1):C.GC_2723,(0,3):C.GC_1156,(2,3):C.GC_1158})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2899,(0,3):C.GC_2899,(1,0):C.GC_2879,(3,0):C.GC_2881,(0,1):C.GC_2879,(2,1):C.GC_2881})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2904,(0,1):C.GC_2904})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2909,(0,1):C.GC_2909})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3274,(0,5):C.GC_3274,(0,0):C.GC_1295,(2,0):C.GC_1298,(1,2):C.GC_1295,(3,2):C.GC_1298,(1,1):C.GC_1161,(3,1):C.GC_1164,(0,3):C.GC_1161,(2,3):C.GC_1164})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3282,(0,3):C.GC_3282,(0,0):C.GC_3244,(2,0):C.GC_3248,(1,1):C.GC_3244,(3,1):C.GC_3248})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3289,(0,1):C.GC_3289})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3298,(0,1):C.GC_3298})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_2067,(2,0):C.GC_2070,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_1162,(2,4):C.GC_1165,(0,5):C.GC_21})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_3186,(2,2):C.GC_3187,(1,0):C.GC_2822,(2,0):C.GC_2824,(1,1):C.GC_698,(0,3):C.GC_700})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4036,(0,3):C.GC_4044,(1,1):C.GC_1296,(2,1):C.GC_1299,(1,0):C.GC_1893,(2,0):C.GC_1896})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4054,(0,1):C.GC_4062})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3278,(0,5):C.GC_3285,(0,0):C.GC_3067,(2,0):C.GC_3070,(1,2):C.GC_1297,(3,2):C.GC_1300,(1,1):C.GC_2736,(3,1):C.GC_2739,(0,3):C.GC_1163,(2,3):C.GC_1166})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3293,(0,2):C.GC_3302,(1,0):C.GC_3247,(2,0):C.GC_3251})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4031,(0,5):C.GC_4031,(0,0):C.GC_1479,(2,0):C.GC_1482,(1,2):C.GC_1479,(3,2):C.GC_1482,(1,1):C.GC_1141,(3,1):C.GC_1144,(0,3):C.GC_1141,(2,3):C.GC_1144})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4042,(0,3):C.GC_4042,(0,0):C.GC_4001,(2,0):C.GC_4005,(1,1):C.GC_4001,(3,1):C.GC_4005})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4050,(0,1):C.GC_4050})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4060,(0,1):C.GC_4060})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4032,(0,5):C.GC_4043,(0,0):C.GC_2266,(2,0):C.GC_2269,(1,2):C.GC_1480,(3,2):C.GC_1483,(1,1):C.GC_1868,(3,1):C.GC_1871,(0,3):C.GC_1142,(2,3):C.GC_1145})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4052,(0,2):C.GC_4061,(1,0):C.GC_4002,(2,0):C.GC_4006})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_3508,(2,0):C.GC_3511,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_1143,(2,4):C.GC_1146,(0,5):C.GC_21})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_3855,(2,2):C.GC_3856,(1,0):C.GC_2821,(2,0):C.GC_2823,(1,1):C.GC_520,(0,3):C.GC_521})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3276,(0,3):C.GC_3283,(1,1):C.GC_1481,(2,1):C.GC_1484,(1,0):C.GC_2714,(2,0):C.GC_2717})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3291,(0,1):C.GC_3299})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2894,(0,5):C.GC_2894,(0,0):C.GC_2068,(2,0):C.GC_2071,(1,2):C.GC_2068,(3,2):C.GC_2071,(1,1):C.GC_2878,(3,1):C.GC_2880,(0,3):C.GC_2878,(2,3):C.GC_2880})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2898,(0,3):C.GC_2898,(1,0):C.GC_1894,(3,0):C.GC_1897,(0,1):C.GC_1894,(2,1):C.GC_1897})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2902,(0,1):C.GC_2902})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2908,(0,1):C.GC_2908})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2899,(0,5):C.GC_2895,(0,0):C.GC_3068,(2,0):C.GC_3071,(1,2):C.GC_2069,(3,2):C.GC_2072,(1,1):C.GC_2737,(3,1):C.GC_2740,(0,3):C.GC_2879,(2,3):C.GC_2881})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2909,(0,2):C.GC_2904,(0,0):C.GC_1895,(2,0):C.GC_1898})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2894,(0,5):C.GC_2898,(0,0):C.GC_3509,(2,0):C.GC_3512,(1,2):C.GC_2268,(3,2):C.GC_2271,(1,1):C.GC_2878,(3,1):C.GC_2880,(0,3):C.GC_1870,(2,3):C.GC_1873})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2902,(0,2):C.GC_2908,(1,0):C.GC_2715,(2,0):C.GC_2718})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2895,(0,5):C.GC_2895,(0,0):C.GC_3510,(2,0):C.GC_3513,(1,2):C.GC_3510,(3,2):C.GC_3513,(1,1):C.GC_2879,(3,1):C.GC_2881,(0,3):C.GC_2879,(2,3):C.GC_2881})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2899,(0,3):C.GC_2899,(1,0):C.GC_2716,(3,0):C.GC_2719,(0,1):C.GC_2716,(2,1):C.GC_2719})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2904,(0,1):C.GC_2904})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2909,(0,1):C.GC_2909})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3274,(0,5):C.GC_3274,(0,0):C.GC_3244,(2,0):C.GC_3248,(1,2):C.GC_1314,(3,2):C.GC_1317,(1,1):C.GC_3244,(3,1):C.GC_3248,(0,3):C.GC_1314,(2,3):C.GC_1317})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3282,(0,3):C.GC_3282,(0,0):C.GC_2075,(2,0):C.GC_2078,(1,1):C.GC_2075,(3,1):C.GC_2078})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3289,(0,1):C.GC_3289})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3298,(0,1):C.GC_3298})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4042,(0,5):C.GC_4031,(0,0):C.GC_4001,(2,0):C.GC_4005,(1,2):C.GC_1488,(3,2):C.GC_1491,(1,1):C.GC_2038,(3,1):C.GC_2041,(0,3):C.GC_1290,(2,3):C.GC_1293})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4060,(0,2):C.GC_4050,(0,0):C.GC_2272,(2,0):C.GC_2275})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3274,(0,5):C.GC_3282,(0,0):C.GC_3516,(2,0):C.GC_3519,(1,2):C.GC_1489,(3,2):C.GC_1492,(1,1):C.GC_3244,(3,1):C.GC_3248,(0,3):C.GC_1291,(2,3):C.GC_1294})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3289,(0,2):C.GC_3298,(1,0):C.GC_3061,(2,0):C.GC_3064})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(0,0):C.GC_48,(2,0):C.GC_49,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_48,(2,4):C.GC_49,(0,5):C.GC_20})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(0,0):C.GC_3246,(2,0):C.GC_3250,(1,3):C.GC_3246,(3,3):C.GC_3250,(1,1):C.GC_3246,(3,1):C.GC_3250,(1,2):C.GC_21,(0,4):C.GC_3246,(2,4):C.GC_3250,(0,5):C.GC_21})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(0,0):C.GC_2076,(2,0):C.GC_2079,(1,3):C.GC_2076,(3,3):C.GC_2079,(1,1):C.GC_2076,(3,1):C.GC_2079,(1,2):C.GC_690,(0,4):C.GC_2076,(2,4):C.GC_2079,(0,5):C.GC_690})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_691,(0,1):C.GC_691})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3277,(0,1):C.GC_3277})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3284,(0,1):C.GC_3284})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3292,(0,1):C.GC_3292})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3300,(0,1):C.GC_3300})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3278,(0,5):C.GC_3278,(0,0):C.GC_3074,(2,0):C.GC_3077,(1,2):C.GC_3247,(3,2):C.GC_3251,(1,1):C.GC_3074,(3,1):C.GC_3077,(0,3):C.GC_3247,(2,3):C.GC_3251})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3285,(0,3):C.GC_3285,(1,0):C.GC_2077,(3,0):C.GC_2080,(0,1):C.GC_2077,(2,1):C.GC_2080})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3293,(0,1):C.GC_3293})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3302,(0,1):C.GC_3302})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4032,(0,5):C.GC_4032,(0,0):C.GC_4002,(2,0):C.GC_4006,(1,2):C.GC_4002,(3,2):C.GC_4006,(1,1):C.GC_2039,(3,1):C.GC_2042,(0,3):C.GC_2039,(2,3):C.GC_2042})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4043,(0,3):C.GC_4043,(0,0):C.GC_2273,(2,0):C.GC_2276,(1,1):C.GC_2273,(3,1):C.GC_2276})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4052,(0,1):C.GC_4052})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4061,(0,1):C.GC_4061})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_3517,(2,0):C.GC_3520,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_2040,(2,4):C.GC_2043,(0,5):C.GC_21})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_4004,(2,2):C.GC_4008,(1,0):C.GC_3245,(2,0):C.GC_3249,(1,1):C.GC_697,(0,3):C.GC_699})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2620,(0,3):C.GC_2627,(1,1):C.GC_2274,(2,1):C.GC_2277,(1,0):C.GC_3062,(2,0):C.GC_3065})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2633,(0,1):C.GC_2639})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3278,(0,5):C.GC_3278,(0,0):C.GC_3518,(2,0):C.GC_3521,(1,2):C.GC_3518,(3,2):C.GC_3521,(1,1):C.GC_3247,(3,1):C.GC_3251,(0,3):C.GC_3247,(2,3):C.GC_3251})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3285,(0,3):C.GC_3285,(1,0):C.GC_3063,(3,0):C.GC_3066,(0,1):C.GC_3063,(2,1):C.GC_3066})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3293,(0,1):C.GC_3293})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3302,(0,1):C.GC_3302})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4031,(0,5):C.GC_4031,(0,0):C.GC_4001,(2,0):C.GC_4005,(1,2):C.GC_1475,(3,2):C.GC_1478,(1,1):C.GC_4001,(3,1):C.GC_4005,(0,3):C.GC_1475,(2,3):C.GC_1478})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4042,(0,3):C.GC_4042,(0,0):C.GC_3490,(2,0):C.GC_3493,(1,1):C.GC_3490,(3,1):C.GC_3493})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4050,(0,1):C.GC_4050})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4060,(0,1):C.GC_4060})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4032,(0,5):C.GC_4032,(0,0):C.GC_4002,(2,0):C.GC_4006,(1,2):C.GC_2250,(3,2):C.GC_2253,(1,1):C.GC_4002,(3,1):C.GC_4006,(0,3):C.GC_2250,(2,3):C.GC_2253})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4043,(0,3):C.GC_4043,(0,0):C.GC_3491,(2,0):C.GC_3494,(1,1):C.GC_3491,(3,1):C.GC_3494})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4052,(0,1):C.GC_4052})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4061,(0,1):C.GC_4061})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(0,0):C.GC_48,(2,0):C.GC_49,(1,3):C.GC_48,(3,3):C.GC_49,(1,1):C.GC_48,(3,1):C.GC_49,(1,2):C.GC_20,(0,4):C.GC_48,(2,4):C.GC_49,(0,5):C.GC_20})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(0,0):C.GC_4003,(2,0):C.GC_4007,(1,3):C.GC_4003,(3,3):C.GC_4007,(1,1):C.GC_4003,(3,1):C.GC_4007,(1,2):C.GC_21,(0,4):C.GC_4003,(2,4):C.GC_4007,(0,5):C.GC_21})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(0,0):C.GC_3492,(2,0):C.GC_3495,(1,3):C.GC_3492,(3,3):C.GC_3495,(1,1):C.GC_3492,(3,1):C.GC_3495,(1,2):C.GC_410,(0,4):C.GC_3492,(2,4):C.GC_3495,(0,5):C.GC_410})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_411,(0,1):C.GC_411})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4037,(0,1):C.GC_4037})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4045,(0,1):C.GC_4045})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4055,(0,1):C.GC_4055})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4063,(0,1):C.GC_4063})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_33,(0,7):C.GC_33,(0,0):C.GC_32,(0,3):C.GC_32,(0,1):C.GC_32,(0,2):C.GC_23,(0,4):C.GC_32,(0,5):C.GC_23})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_33,(0,4):C.GC_34,(0,2):C.GC_32,(0,0):C.GC_32,(0,1):C.GC_23})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_33,(0,4):C.GC_34,(0,2):C.GC_32,(0,0):C.GC_32,(0,1):C.GC_23})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_33,(0,7):C.GC_33,(0,0):C.GC_32,(0,3):C.GC_32,(0,1):C.GC_32,(0,2):C.GC_23,(0,4):C.GC_32,(0,5):C.GC_23})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_33,(0,4):C.GC_34,(0,2):C.GC_32,(0,0):C.GC_32,(0,1):C.GC_23})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_33,(0,7):C.GC_33,(0,0):C.GC_32,(0,3):C.GC_32,(0,1):C.GC_32,(0,2):C.GC_23,(0,4):C.GC_32,(0,5):C.GC_23})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_571,(0,0):C.GC_571})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_2619,(0,2):C.GC_516,(0,3):C.GC_515,(0,5):C.GC_2676,(0,0):C.GC_2676})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2618})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_626,(0,0):C.GC_626})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_2619,(0,2):C.GC_516,(0,3):C.GC_515,(0,5):C.GC_2677,(0,0):C.GC_2677})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2618})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_891,(0,0):C.GC_891})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_2619,(0,2):C.GC_516,(0,3):C.GC_515,(0,5):C.GC_2678,(0,0):C.GC_2678})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2618})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2886,(0,1):C.GC_2892,(0,3):C.GC_2992,(0,0):C.GC_3020})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2888})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2886,(0,1):C.GC_2892,(0,3):C.GC_2995,(0,0):C.GC_3021})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2888})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2886,(0,1):C.GC_2892,(0,3):C.GC_3023,(0,0):C.GC_3025})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2888})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2887,(0,1):C.GC_2893,(0,3):C.GC_2993,(0,0):C.GC_2991})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2890})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2887,(0,1):C.GC_2893,(0,3):C.GC_2996,(0,0):C.GC_2994})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2890})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2887,(0,1):C.GC_2893,(0,3):C.GC_3024,(0,0):C.GC_3022})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2890})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3262,(0,1):C.GC_3271,(0,3):C.GC_3444,(0,0):C.GC_3368})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3265})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3262,(0,1):C.GC_3271,(0,3):C.GC_3447,(0,0):C.GC_3370})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3265})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3262,(0,1):C.GC_3271,(0,3):C.GC_3452,(0,0):C.GC_3451})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3265})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_680,(0,0):C.GC_680})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_3272,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_3445,(0,0):C.GC_3445})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3267})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_684,(0,0):C.GC_684})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_3272,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_3448,(0,0):C.GC_3448})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3267})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_895,(0,0):C.GC_895})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_3272,(0,2):C.GC_693,(0,3):C.GC_692,(0,5):C.GC_3453,(0,0):C.GC_3453})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3267})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3264,(0,1):C.GC_3273,(0,3):C.GC_3446,(0,0):C.GC_3367})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3269})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3264,(0,1):C.GC_3273,(0,3):C.GC_3449,(0,0):C.GC_3369})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3269})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3264,(0,1):C.GC_3273,(0,3):C.GC_3454,(0,0):C.GC_3450})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3269})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4019,(0,1):C.GC_4028,(0,3):C.GC_4181,(0,0):C.GC_4184})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4022})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4019,(0,1):C.GC_4028,(0,3):C.GC_4185,(0,0):C.GC_4188})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4022})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4019,(0,1):C.GC_4028,(0,3):C.GC_4214,(0,0):C.GC_4217})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4022})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4020,(0,1):C.GC_4029,(0,3):C.GC_4182,(0,0):C.GC_4212})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4024})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4020,(0,1):C.GC_4029,(0,3):C.GC_4186,(0,0):C.GC_4213})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4024})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4020,(0,1):C.GC_4029,(0,3):C.GC_4215,(0,0):C.GC_4218})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4024})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_555,(0,0):C.GC_555})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_4030,(0,2):C.GC_413,(0,3):C.GC_412,(0,5):C.GC_4183,(0,0):C.GC_4183})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4026})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_610,(0,0):C.GC_610})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_4030,(0,2):C.GC_413,(0,3):C.GC_412,(0,5):C.GC_4187,(0,0):C.GC_4187})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4026})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_35,(0,1):C.GC_50,(0,2):C.GC_31,(0,3):C.GC_22,(0,5):C.GC_875,(0,0):C.GC_875})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_37,(0,1):C.GC_4030,(0,2):C.GC_413,(0,3):C.GC_412,(0,5):C.GC_4216,(0,0):C.GC_4216})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4026})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_38,(0,5):C.GC_989,(0,3):C.GC_988,(0,4):C.GC_988,(0,1):C.GC_983,(0,0):C.GC_572})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1041,(0,5):C.GC_1072,(0,3):C.GC_1071,(0,4):C.GC_1071,(0,1):C.GC_1068,(0,0):C.GC_1060})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_41,(0,5):C.GC_566,(0,3):C.GC_565,(0,4):C.GC_565,(0,1):C.GC_560,(0,0):C.GC_573})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_522,(0,5):C.GC_581,(0,3):C.GC_580,(0,4):C.GC_580,(0,1):C.GC_579,(0,0):C.GC_582})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_44,(0,5):C.GC_771,(0,3):C.GC_770,(0,4):C.GC_770,(0,1):C.GC_765,(0,0):C.GC_574})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_806,(0,5):C.GC_834,(0,3):C.GC_833,(0,4):C.GC_833,(0,1):C.GC_830,(0,0):C.GC_825})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_39,(0,5):C.GC_991,(0,3):C.GC_990,(0,4):C.GC_990,(0,1):C.GC_984,(0,0):C.GC_681})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1042,(0,5):C.GC_1074,(0,3):C.GC_1073,(0,4):C.GC_1073,(0,1):C.GC_1069,(0,0):C.GC_1063})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_42,(0,5):C.GC_568,(0,3):C.GC_567,(0,4):C.GC_567,(0,1):C.GC_561,(0,0):C.GC_682})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_701,(0,5):C.GC_709,(0,3):C.GC_708,(0,4):C.GC_708,(0,1):C.GC_707,(0,0):C.GC_713})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_45,(0,5):C.GC_773,(0,3):C.GC_772,(0,4):C.GC_772,(0,1):C.GC_766,(0,0):C.GC_683})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_807,(0,5):C.GC_836,(0,3):C.GC_835,(0,4):C.GC_835,(0,1):C.GC_831,(0,0):C.GC_828})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_40,(0,5):C.GC_993,(0,3):C.GC_992,(0,4):C.GC_992,(0,1):C.GC_985,(0,0):C.GC_556})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1043,(0,5):C.GC_1076,(0,3):C.GC_1075,(0,4):C.GC_1075,(0,1):C.GC_1070,(0,0):C.GC_1059})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_43,(0,5):C.GC_570,(0,3):C.GC_569,(0,4):C.GC_569,(0,1):C.GC_562,(0,0):C.GC_557})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_464,(0,5):C.GC_578,(0,3):C.GC_577,(0,4):C.GC_577,(0,1):C.GC_576,(0,0):C.GC_575})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_46,(0,5):C.GC_775,(0,3):C.GC_774,(0,4):C.GC_774,(0,1):C.GC_767,(0,0):C.GC_558})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_808,(0,5):C.GC_838,(0,3):C.GC_837,(0,4):C.GC_837,(0,1):C.GC_832,(0,0):C.GC_824})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_38,(0,5):C.GC_1001,(0,3):C.GC_1000,(0,4):C.GC_1000,(0,1):C.GC_995,(0,0):C.GC_627})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1041,(0,5):C.GC_1081,(0,3):C.GC_1080,(0,4):C.GC_1080,(0,1):C.GC_1077,(0,0):C.GC_1062})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_41,(0,5):C.GC_621,(0,3):C.GC_620,(0,4):C.GC_620,(0,1):C.GC_615,(0,0):C.GC_628})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_522,(0,5):C.GC_636,(0,3):C.GC_635,(0,4):C.GC_635,(0,1):C.GC_634,(0,0):C.GC_637})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_44,(0,5):C.GC_783,(0,3):C.GC_782,(0,4):C.GC_782,(0,1):C.GC_777,(0,0):C.GC_629})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_806,(0,5):C.GC_843,(0,3):C.GC_842,(0,4):C.GC_842,(0,1):C.GC_839,(0,0):C.GC_827})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_39,(0,5):C.GC_1003,(0,3):C.GC_1002,(0,4):C.GC_1002,(0,1):C.GC_996,(0,0):C.GC_685})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1042,(0,5):C.GC_1083,(0,3):C.GC_1082,(0,4):C.GC_1082,(0,1):C.GC_1078,(0,0):C.GC_1064})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_42,(0,5):C.GC_623,(0,3):C.GC_622,(0,4):C.GC_622,(0,1):C.GC_616,(0,0):C.GC_686})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_701,(0,5):C.GC_712,(0,3):C.GC_711,(0,4):C.GC_711,(0,1):C.GC_710,(0,0):C.GC_714})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_45,(0,5):C.GC_785,(0,3):C.GC_784,(0,4):C.GC_784,(0,1):C.GC_778,(0,0):C.GC_687})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_807,(0,5):C.GC_845,(0,3):C.GC_844,(0,4):C.GC_844,(0,1):C.GC_840,(0,0):C.GC_829})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_40,(0,5):C.GC_1005,(0,3):C.GC_1004,(0,4):C.GC_1004,(0,1):C.GC_997,(0,0):C.GC_611})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1043,(0,5):C.GC_1085,(0,3):C.GC_1084,(0,4):C.GC_1084,(0,1):C.GC_1079,(0,0):C.GC_1061})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_43,(0,5):C.GC_625,(0,3):C.GC_624,(0,4):C.GC_624,(0,1):C.GC_617,(0,0):C.GC_612})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_464,(0,5):C.GC_633,(0,3):C.GC_632,(0,4):C.GC_632,(0,1):C.GC_631,(0,0):C.GC_630})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_46,(0,5):C.GC_787,(0,3):C.GC_786,(0,4):C.GC_786,(0,1):C.GC_779,(0,0):C.GC_613})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_808,(0,5):C.GC_847,(0,3):C.GC_846,(0,4):C.GC_846,(0,1):C.GC_841,(0,0):C.GC_826})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_38,(0,5):C.GC_1022,(0,3):C.GC_1021,(0,4):C.GC_1021,(0,1):C.GC_1016,(0,0):C.GC_892})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1041,(0,5):C.GC_1090,(0,3):C.GC_1089,(0,4):C.GC_1089,(0,1):C.GC_1086,(0,0):C.GC_1066})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_41,(0,5):C.GC_886,(0,3):C.GC_885,(0,4):C.GC_885,(0,1):C.GC_880,(0,0):C.GC_893})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_522,(0,5):C.GC_917,(0,3):C.GC_916,(0,4):C.GC_916,(0,1):C.GC_915,(0,0):C.GC_918})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_44,(0,5):C.GC_906,(0,3):C.GC_905,(0,4):C.GC_905,(0,1):C.GC_900,(0,0):C.GC_894})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_806,(0,5):C.GC_930,(0,3):C.GC_929,(0,4):C.GC_929,(0,1):C.GC_926,(0,0):C.GC_924})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_39,(0,5):C.GC_1024,(0,3):C.GC_1023,(0,4):C.GC_1023,(0,1):C.GC_1017,(0,0):C.GC_896})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1042,(0,5):C.GC_1092,(0,3):C.GC_1091,(0,4):C.GC_1091,(0,1):C.GC_1087,(0,0):C.GC_1067})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_42,(0,5):C.GC_888,(0,3):C.GC_887,(0,4):C.GC_887,(0,1):C.GC_881,(0,0):C.GC_897})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_701,(0,5):C.GC_921,(0,3):C.GC_920,(0,4):C.GC_920,(0,1):C.GC_919,(0,0):C.GC_922})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_45,(0,5):C.GC_908,(0,3):C.GC_907,(0,4):C.GC_907,(0,1):C.GC_901,(0,0):C.GC_898})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_807,(0,5):C.GC_932,(0,3):C.GC_931,(0,4):C.GC_931,(0,1):C.GC_927,(0,0):C.GC_925})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_40,(0,5):C.GC_1026,(0,3):C.GC_1025,(0,4):C.GC_1025,(0,1):C.GC_1018,(0,0):C.GC_876})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1043,(0,5):C.GC_1094,(0,3):C.GC_1093,(0,4):C.GC_1093,(0,1):C.GC_1088,(0,0):C.GC_1065})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_43,(0,5):C.GC_890,(0,3):C.GC_889,(0,4):C.GC_889,(0,1):C.GC_882,(0,0):C.GC_877})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_464,(0,5):C.GC_914,(0,3):C.GC_913,(0,4):C.GC_913,(0,1):C.GC_912,(0,0):C.GC_911})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_46,(0,5):C.GC_910,(0,3):C.GC_909,(0,4):C.GC_909,(0,1):C.GC_902,(0,0):C.GC_878})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_808,(0,5):C.GC_934,(0,3):C.GC_933,(0,4):C.GC_933,(0,1):C.GC_928,(0,0):C.GC_923})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_975,(3,0):C.GC_977,(0,5):C.GC_1105,(2,5):C.GC_1106,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_975,(3,8):C.GC_977,(0,1):C.GC_1105,(2,1):C.GC_1106})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_3698,(1,0):C.GC_1190,(3,0):C.GC_1191,(0,5):C.GC_976,(2,5):C.GC_978,(1,4):C.GC_3627,(3,4):C.GC_3635,(1,2):C.GC_2612,(3,2):C.GC_2615,(1,3):C.GC_1045,(3,3):C.GC_1048,(1,8):C.GC_1190,(3,8):C.GC_1191,(0,1):C.GC_976,(2,1):C.GC_978})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3669,(0,3):C.GC_1117,(1,1):C.GC_511,(2,1):C.GC_512,(1,0):C.GC_1218,(2,0):C.GC_1221})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2833,(0,1):C.GC_1230})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1108})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1126})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1225})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1235})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1796,(0,6):C.GC_1805,(1,0):C.GC_2573,(3,0):C.GC_2575,(0,4):C.GC_2572,(2,4):C.GC_2574,(1,3):C.GC_2340,(3,3):C.GC_2345,(1,2):C.GC_1917,(3,2):C.GC_1920,(1,7):C.GC_2334,(3,7):C.GC_2338,(0,1):C.GC_2332,(2,1):C.GC_2336})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1814,(0,1):C.GC_2631})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2625,(0,1):C.GC_2323})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2321})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2638})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2370})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2680,(0,6):C.GC_2689,(1,0):C.GC_3923,(3,0):C.GC_3927,(0,4):C.GC_3921,(2,4):C.GC_3925,(1,3):C.GC_3621,(3,3):C.GC_3629,(1,2):C.GC_2809,(3,2):C.GC_2812,(1,7):C.GC_3758,(3,7):C.GC_3762,(0,1):C.GC_3756,(2,1):C.GC_3760})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2698,(0,1):C.GC_4048})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4040,(0,1):C.GC_3615})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3611})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4059})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3663})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1111,(0,6):C.GC_1120,(1,0):C.GC_1571,(3,0):C.GC_1573,(0,4):C.GC_1570,(2,4):C.GC_1572,(1,3):C.GC_1574,(3,3):C.GC_1576,(1,2):C.GC_1184,(3,2):C.GC_1187,(1,7):C.GC_1682,(3,7):C.GC_1686,(0,1):C.GC_1680,(2,1):C.GC_1684})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1129,(0,1):C.GC_1765})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1756,(0,1):C.GC_1568})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1566})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1775})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1590})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(0,7):C.GC_56,(1,6):C.GC_51,(1,0):C.GC_503,(3,0):C.GC_505,(0,5):C.GC_1095,(2,5):C.GC_1096,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_503,(3,8):C.GC_505,(0,1):C.GC_1095,(2,1):C.GC_1096})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(0,7):C.GC_2641,(1,6):C.GC_53,(1,0):C.GC_1849,(3,0):C.GC_1854,(0,5):C.GC_504,(2,5):C.GC_506,(1,4):C.GC_2342,(3,4):C.GC_2347,(1,2):C.GC_2610,(3,2):C.GC_2613,(1,3):C.GC_523,(3,3):C.GC_524,(1,8):C.GC_1849,(3,8):C.GC_1854,(0,1):C.GC_504,(2,1):C.GC_506})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(0,2):C.GC_1808,(1,1):C.GC_2621,(1,0):C.GC_1841,(2,0):C.GC_1844})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,1):C.GC_1934,(1,0):C.GC_2834})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1799})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1817})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1932})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1936})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2683,(0,6):C.GC_2692,(1,0):C.GC_3618,(3,0):C.GC_3620,(0,4):C.GC_3617,(2,4):C.GC_3619,(1,3):C.GC_3622,(3,3):C.GC_3630,(1,2):C.GC_2754,(3,2):C.GC_2757,(1,7):C.GC_3759,(3,7):C.GC_3763,(0,1):C.GC_3757,(2,1):C.GC_3761})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2701,(0,1):C.GC_3867})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3860,(0,1):C.GC_3616})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3612})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3880})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3664})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1114,(0,6):C.GC_1123,(1,0):C.GC_1642,(3,0):C.GC_1644,(0,4):C.GC_1641,(2,4):C.GC_1643,(1,3):C.GC_1575,(3,3):C.GC_1577,(1,2):C.GC_1209,(3,2):C.GC_1212,(1,7):C.GC_1683,(3,7):C.GC_1687,(0,1):C.GC_1681,(2,1):C.GC_1685})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1132,(0,1):C.GC_1769})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1760,(0,1):C.GC_1569})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1567})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1779})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1591})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1802,(0,6):C.GC_1811,(1,0):C.GC_2512,(3,0):C.GC_2514,(0,4):C.GC_2511,(2,4):C.GC_2513,(1,3):C.GC_2344,(3,3):C.GC_2349,(1,2):C.GC_1899,(3,2):C.GC_1902,(1,7):C.GC_2335,(3,7):C.GC_2339,(0,1):C.GC_2333,(2,1):C.GC_2337})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1820,(0,1):C.GC_2550})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2546,(0,1):C.GC_2324})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2322})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2555})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2373})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_757,(3,0):C.GC_759,(0,5):C.GC_1101,(2,5):C.GC_1102,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_757,(3,8):C.GC_759,(0,1):C.GC_1101,(2,1):C.GC_1102})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_3695,(1,0):C.GC_2762,(3,0):C.GC_2767,(0,5):C.GC_758,(2,5):C.GC_760,(1,4):C.GC_3624,(3,4):C.GC_3632,(1,2):C.GC_2611,(3,2):C.GC_2614,(1,3):C.GC_810,(3,3):C.GC_813,(1,8):C.GC_2762,(3,8):C.GC_2767,(0,1):C.GC_758,(2,1):C.GC_760})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3666,(0,2):C.GC_2695,(1,0):C.GC_2791,(2,0):C.GC_2794})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3613,(0,1):C.GC_2835})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2686})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2704})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2828})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2842})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1109,(0,5):C.GC_1118,(1,0):C.GC_2868,(3,0):C.GC_2872,(0,3):C.GC_2866,(2,3):C.GC_2870,(1,2):C.GC_1219,(3,2):C.GC_1222,(1,6):C.GC_2875,(3,6):C.GC_2877,(0,1):C.GC_2874,(2,1):C.GC_2876})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1127,(0,2):C.GC_2819,(1,0):C.GC_2882,(2,0):C.GC_2884})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2818,(0,1):C.GC_2844})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2836})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2820})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2894})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1797,(0,5):C.GC_1806,(1,0):C.GC_1925,(3,0):C.GC_1929,(0,3):C.GC_1923,(2,3):C.GC_1927,(1,2):C.GC_1918,(3,2):C.GC_1921,(1,6):C.GC_1877,(3,6):C.GC_1883,(0,1):C.GC_1874,(2,1):C.GC_1880})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1815,(0,1):C.GC_1964})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1962})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1966})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2681,(0,5):C.GC_2690,(1,0):C.GC_2803,(3,0):C.GC_2807,(0,3):C.GC_2801,(2,3):C.GC_2805,(1,2):C.GC_2810,(3,2):C.GC_2813,(1,6):C.GC_2782,(3,6):C.GC_2788,(0,1):C.GC_2779,(2,1):C.GC_2785})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2699,(0,1):C.GC_2900})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2896})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2906})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1112,(0,6):C.GC_1121,(1,0):C.GC_1149,(3,0):C.GC_1153,(0,4):C.GC_1147,(2,4):C.GC_1151,(1,3):C.GC_678,(3,3):C.GC_679,(1,2):C.GC_1185,(3,2):C.GC_1188,(1,7):C.GC_1203,(3,7):C.GC_1207,(0,1):C.GC_1201,(2,1):C.GC_1205})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1130,(0,1):C.GC_1231})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1226})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1236})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1800,(0,5):C.GC_2844,(1,0):C.GC_1850,(3,0):C.GC_1855,(0,3):C.GC_1847,(2,3):C.GC_1852,(1,2):C.GC_1842,(3,2):C.GC_1845,(1,6):C.GC_1878,(3,6):C.GC_1884,(0,1):C.GC_1875,(2,1):C.GC_1881})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1818,(0,2):C.GC_1809,(1,0):C.GC_2882,(2,0):C.GC_2884})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2894,(0,1):C.GC_1950})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1949})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2903})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1951})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2684,(0,5):C.GC_2693,(1,0):C.GC_2728,(3,0):C.GC_2732,(0,3):C.GC_2726,(2,3):C.GC_2730,(1,2):C.GC_2755,(3,2):C.GC_2758,(1,6):C.GC_2783,(3,6):C.GC_2789,(0,1):C.GC_2780,(2,1):C.GC_2786})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2702,(0,1):C.GC_2831})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2826})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2840})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1115,(0,5):C.GC_1124,(1,0):C.GC_1169,(3,0):C.GC_1173,(0,3):C.GC_1167,(2,3):C.GC_1171,(1,2):C.GC_1210,(3,2):C.GC_1213,(1,6):C.GC_1204,(3,6):C.GC_1208,(0,1):C.GC_1202,(2,1):C.GC_1206})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1133,(0,1):C.GC_1233})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1228})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1238})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1803,(0,5):C.GC_1812,(1,0):C.GC_1907,(3,0):C.GC_1911,(0,3):C.GC_1905,(2,3):C.GC_1909,(1,2):C.GC_1900,(3,2):C.GC_1903,(1,6):C.GC_1879,(3,6):C.GC_1885,(0,1):C.GC_1876,(2,1):C.GC_1882})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1821,(0,1):C.GC_1954})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1952})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1956})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2894,(0,5):C.GC_2844,(1,0):C.GC_2763,(3,0):C.GC_2768,(0,3):C.GC_2760,(2,3):C.GC_2765,(1,2):C.GC_2882,(3,2):C.GC_2884,(1,6):C.GC_2784,(3,6):C.GC_2790,(0,1):C.GC_2781,(2,1):C.GC_2787})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2903,(0,2):C.GC_2696,(1,0):C.GC_2792,(2,0):C.GC_2795})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2687,(0,1):C.GC_2837})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2705})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2829})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2843})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1110,(0,5):C.GC_1119,(1,0):C.GC_2869,(3,0):C.GC_2873,(0,3):C.GC_2867,(2,3):C.GC_2871,(1,2):C.GC_1220,(3,2):C.GC_1223,(1,6):C.GC_2863,(3,6):C.GC_2865,(0,1):C.GC_2862,(2,1):C.GC_2864})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1128,(0,2):C.GC_2816,(1,0):C.GC_2883,(2,0):C.GC_2885})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2815,(0,1):C.GC_2846})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2838})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2817})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2895})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1798,(0,5):C.GC_1807,(1,0):C.GC_1926,(3,0):C.GC_1930,(0,3):C.GC_1924,(2,3):C.GC_1928,(1,2):C.GC_1919,(3,2):C.GC_1922,(1,6):C.GC_1832,(3,6):C.GC_1838,(0,1):C.GC_1829,(2,1):C.GC_1835})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1816,(0,1):C.GC_1965})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1963})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1967})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2682,(0,5):C.GC_2691,(1,0):C.GC_2804,(3,0):C.GC_2808,(0,3):C.GC_2802,(2,3):C.GC_2806,(1,2):C.GC_2811,(3,2):C.GC_2814,(1,6):C.GC_2745,(3,6):C.GC_2751,(0,1):C.GC_2742,(2,1):C.GC_2748})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2700,(0,1):C.GC_2901})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2897})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2907})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1113,(0,5):C.GC_1122,(1,0):C.GC_1150,(3,0):C.GC_1154,(0,3):C.GC_1148,(2,3):C.GC_1152,(1,2):C.GC_1186,(3,2):C.GC_1189,(1,6):C.GC_1178,(3,6):C.GC_1182,(0,1):C.GC_1176,(2,1):C.GC_1180})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1131,(0,1):C.GC_1232})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1227})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1237})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1801,(0,5):C.GC_2846,(1,0):C.GC_1851,(3,0):C.GC_1856,(0,3):C.GC_1848,(2,3):C.GC_1853,(1,2):C.GC_1843,(3,2):C.GC_1846,(1,6):C.GC_1833,(3,6):C.GC_1839,(0,1):C.GC_1830,(2,1):C.GC_1836})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1819,(0,2):C.GC_1810,(1,0):C.GC_2883,(2,0):C.GC_2885})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1933,(0,1):C.GC_1935})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1937})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2895})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2905})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2685,(0,5):C.GC_2694,(1,0):C.GC_2729,(3,0):C.GC_2733,(0,3):C.GC_2727,(2,3):C.GC_2731,(1,2):C.GC_2756,(3,2):C.GC_2759,(1,6):C.GC_2746,(3,6):C.GC_2752,(0,1):C.GC_2743,(2,1):C.GC_2749})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2703,(0,1):C.GC_2832})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2827})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2841})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1116,(0,6):C.GC_1125,(1,0):C.GC_1170,(3,0):C.GC_1174,(0,4):C.GC_1168,(2,4):C.GC_1172,(1,3):C.GC_501,(3,3):C.GC_502,(1,2):C.GC_1211,(3,2):C.GC_1214,(1,7):C.GC_1179,(3,7):C.GC_1183,(0,1):C.GC_1177,(2,1):C.GC_1181})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1134,(0,1):C.GC_1234})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1229})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1239})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1804,(0,5):C.GC_1813,(1,0):C.GC_1908,(3,0):C.GC_1912,(0,3):C.GC_1906,(2,3):C.GC_1910,(1,2):C.GC_1901,(3,2):C.GC_1904,(1,6):C.GC_1834,(3,6):C.GC_1840,(0,1):C.GC_1831,(2,1):C.GC_1837})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1822,(0,1):C.GC_1955})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1953})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1957})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2895,(0,5):C.GC_2846,(1,0):C.GC_2764,(3,0):C.GC_2769,(0,3):C.GC_2761,(2,3):C.GC_2766,(1,2):C.GC_2883,(3,2):C.GC_2885,(1,6):C.GC_2747,(3,6):C.GC_2753,(0,1):C.GC_2744,(2,1):C.GC_2750})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2905,(0,2):C.GC_2697,(1,0):C.GC_2793,(2,0):C.GC_2796})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2688,(0,1):C.GC_2839})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2706})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2830})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2845})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1256,(0,5):C.GC_1265,(1,0):C.GC_3238,(3,0):C.GC_3242,(0,3):C.GC_3236,(2,3):C.GC_3240,(1,2):C.GC_1384,(3,2):C.GC_1387,(1,6):C.GC_3233,(3,6):C.GC_3235,(0,1):C.GC_3232,(2,1):C.GC_3234})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1274,(0,2):C.GC_3182,(1,0):C.GC_3252,(2,0):C.GC_3257})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3180,(0,1):C.GC_3209})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3198})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3184})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3274})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1969,(0,6):C.GC_1978,(1,0):C.GC_2112,(3,0):C.GC_2118,(0,4):C.GC_2109,(2,4):C.GC_2115,(1,3):C.GC_678,(3,3):C.GC_679,(1,2):C.GC_2103,(3,2):C.GC_2106,(1,7):C.GC_2023,(3,7):C.GC_2029,(0,1):C.GC_2020,(2,1):C.GC_2026})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1987,(0,1):C.GC_2158})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2155})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2161})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3027,(0,5):C.GC_3036,(1,0):C.GC_3165,(3,0):C.GC_3171,(0,3):C.GC_3162,(2,3):C.GC_3168,(1,2):C.GC_3174,(3,2):C.GC_3177,(1,6):C.GC_3114,(3,6):C.GC_3120,(0,1):C.GC_3111,(2,1):C.GC_3117})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3045,(0,1):C.GC_3286})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3279})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3295})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1259,(0,5):C.GC_1268,(1,0):C.GC_1304,(3,0):C.GC_1310,(0,3):C.GC_1301,(2,3):C.GC_1307,(1,2):C.GC_1342,(3,2):C.GC_1345,(1,6):C.GC_1350,(3,6):C.GC_1354,(0,1):C.GC_1348,(2,1):C.GC_1352})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1277,(0,1):C.GC_1399})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1392})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1406})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1972,(0,5):C.GC_3209,(1,0):C.GC_2050,(3,0):C.GC_2060,(0,3):C.GC_2045,(2,3):C.GC_2055,(1,2):C.GC_2014,(3,2):C.GC_2017,(1,6):C.GC_2024,(3,6):C.GC_2030,(0,1):C.GC_2021,(2,1):C.GC_2027})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1990,(0,2):C.GC_1981,(1,0):C.GC_3252,(2,0):C.GC_3257})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3274,(0,1):C.GC_2125})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2122})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3290})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2128})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3030,(0,5):C.GC_3039,(1,0):C.GC_3082,(3,0):C.GC_3088,(0,3):C.GC_3079,(2,3):C.GC_3085,(1,2):C.GC_3105,(3,2):C.GC_3108,(1,6):C.GC_3115,(3,6):C.GC_3121,(0,1):C.GC_3112,(2,1):C.GC_3118})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3048,(0,1):C.GC_3195})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3189})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3205})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1262,(0,5):C.GC_1271,(1,0):C.GC_1324,(3,0):C.GC_1330,(0,3):C.GC_1321,(2,3):C.GC_1327,(1,2):C.GC_1375,(3,2):C.GC_1378,(1,6):C.GC_1351,(3,6):C.GC_1355,(0,1):C.GC_1349,(2,1):C.GC_1353})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1280,(0,1):C.GC_1402})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1395})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1409})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1975,(0,5):C.GC_1984,(1,0):C.GC_2090,(3,0):C.GC_2096,(0,3):C.GC_2087,(2,3):C.GC_2093,(1,2):C.GC_2081,(3,2):C.GC_2084,(1,6):C.GC_2025,(3,6):C.GC_2031,(0,1):C.GC_2022,(2,1):C.GC_2028})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1993,(0,1):C.GC_2145})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2142})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2148})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3274,(0,5):C.GC_3209,(1,0):C.GC_3136,(3,0):C.GC_3146,(0,3):C.GC_3131,(2,3):C.GC_3141,(1,2):C.GC_3252,(3,2):C.GC_3257,(1,6):C.GC_3116,(3,6):C.GC_3122,(0,1):C.GC_3113,(2,1):C.GC_3119})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3290,(0,2):C.GC_3042,(1,0):C.GC_3152,(2,0):C.GC_3155})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3033,(0,1):C.GC_3199})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3051})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3192})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3208})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_1006,(3,0):C.GC_1008,(0,5):C.GC_1097,(2,5):C.GC_1098,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_1006,(3,8):C.GC_1008,(0,1):C.GC_1097,(2,1):C.GC_1098})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_3699,(1,0):C.GC_1364,(3,0):C.GC_1369,(0,5):C.GC_1007,(2,5):C.GC_1009,(1,4):C.GC_3628,(3,4):C.GC_3636,(1,2):C.GC_3255,(3,2):C.GC_3260,(1,3):C.GC_1046,(3,3):C.GC_1049,(1,8):C.GC_1364,(3,8):C.GC_1369,(0,1):C.GC_1007,(2,1):C.GC_1009})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3670,(0,2):C.GC_1266,(1,0):C.GC_1385,(2,0):C.GC_1388})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3200,(0,1):C.GC_1398})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1257})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1275})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1391})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1405})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1970,(0,6):C.GC_2323,(1,0):C.GC_2113,(3,0):C.GC_2119,(0,4):C.GC_2110,(2,4):C.GC_2116,(1,3):C.GC_2340,(3,3):C.GC_2345,(1,2):C.GC_2104,(3,2):C.GC_2107,(1,7):C.GC_2049,(3,7):C.GC_2059,(0,1):C.GC_2044,(2,1):C.GC_2054})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1988,(0,1):C.GC_1979})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2156,(0,1):C.GC_2159})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2162})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2370})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2380})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3028,(0,6):C.GC_3615,(1,0):C.GC_3166,(3,0):C.GC_3172,(0,4):C.GC_3163,(2,4):C.GC_3169,(1,3):C.GC_3621,(3,3):C.GC_3629,(1,2):C.GC_3175,(3,2):C.GC_3178,(1,7):C.GC_3134,(3,7):C.GC_3144,(0,1):C.GC_3129,(2,1):C.GC_3139})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3046,(0,1):C.GC_3037})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3663,(0,1):C.GC_3287})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3681})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3280})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3296})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1260,(0,6):C.GC_1568,(1,0):C.GC_1305,(3,0):C.GC_1311,(0,4):C.GC_1302,(2,4):C.GC_1308,(1,3):C.GC_1574,(3,3):C.GC_1576,(1,2):C.GC_1343,(3,2):C.GC_1346,(1,7):C.GC_1365,(3,7):C.GC_1370,(0,1):C.GC_1362,(2,1):C.GC_1367})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1278,(0,1):C.GC_1269})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1393,(0,1):C.GC_1400})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1407})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1590})

V_1572 = Vertex(name = 'V_1572',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1595})

V_1573 = Vertex(name = 'V_1573',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_671,(3,0):C.GC_673,(0,5):C.GC_672,(2,5):C.GC_674,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_671,(3,8):C.GC_673,(0,1):C.GC_672,(2,1):C.GC_674})

V_1574 = Vertex(name = 'V_1574',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_3301,(1,0):C.GC_2051,(3,0):C.GC_2061,(0,5):C.GC_2046,(2,5):C.GC_2056,(1,4):C.GC_2343,(3,4):C.GC_2348,(1,2):C.GC_3253,(3,2):C.GC_3258,(1,3):C.GC_702,(3,3):C.GC_703,(1,8):C.GC_2051,(3,8):C.GC_2061,(0,1):C.GC_2046,(2,1):C.GC_2056})

V_1575 = Vertex(name = 'V_1575',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3275,(0,3):C.GC_1982,(1,1):C.GC_688,(2,1):C.GC_689,(1,0):C.GC_2015,(2,0):C.GC_2018})

V_1576 = Vertex(name = 'V_1576',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3201,(0,1):C.GC_2126})

V_1577 = Vertex(name = 'V_1577',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1973})

V_1578 = Vertex(name = 'V_1578',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1991})

V_1579 = Vertex(name = 'V_1579',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2123})

V_1580 = Vertex(name = 'V_1580',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2129})

V_1581 = Vertex(name = 'V_1581',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3031,(0,6):C.GC_3616,(1,0):C.GC_3083,(3,0):C.GC_3089,(0,4):C.GC_3080,(2,4):C.GC_3086,(1,3):C.GC_3622,(3,3):C.GC_3630,(1,2):C.GC_3106,(3,2):C.GC_3109,(1,7):C.GC_3135,(3,7):C.GC_3145,(0,1):C.GC_3130,(2,1):C.GC_3140})

V_1582 = Vertex(name = 'V_1582',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3049,(0,1):C.GC_3040})

V_1583 = Vertex(name = 'V_1583',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3190,(0,1):C.GC_3196})

V_1584 = Vertex(name = 'V_1584',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3206})

V_1585 = Vertex(name = 'V_1585',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3664})

V_1586 = Vertex(name = 'V_1586',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3683})

V_1587 = Vertex(name = 'V_1587',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1263,(0,6):C.GC_1569,(1,0):C.GC_1325,(3,0):C.GC_1331,(0,4):C.GC_1322,(2,4):C.GC_1328,(1,3):C.GC_1575,(3,3):C.GC_1577,(1,2):C.GC_1376,(3,2):C.GC_1379,(1,7):C.GC_1366,(3,7):C.GC_1371,(0,1):C.GC_1363,(2,1):C.GC_1368})

V_1588 = Vertex(name = 'V_1588',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1281,(0,1):C.GC_1272})

V_1589 = Vertex(name = 'V_1589',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1591,(0,1):C.GC_1403})

V_1590 = Vertex(name = 'V_1590',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1597})

V_1591 = Vertex(name = 'V_1591',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1396})

V_1592 = Vertex(name = 'V_1592',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1410})

V_1593 = Vertex(name = 'V_1593',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1976,(0,6):C.GC_2324,(1,0):C.GC_2091,(3,0):C.GC_2097,(0,4):C.GC_2088,(2,4):C.GC_2094,(1,3):C.GC_2344,(3,3):C.GC_2349,(1,2):C.GC_2082,(3,2):C.GC_2085,(1,7):C.GC_2053,(3,7):C.GC_2063,(0,1):C.GC_2048,(2,1):C.GC_2058})

V_1594 = Vertex(name = 'V_1594',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1994,(0,1):C.GC_1985})

V_1595 = Vertex(name = 'V_1595',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2143,(0,1):C.GC_2146})

V_1596 = Vertex(name = 'V_1596',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2149})

V_1597 = Vertex(name = 'V_1597',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2373})

V_1598 = Vertex(name = 'V_1598',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2385})

V_1599 = Vertex(name = 'V_1599',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_788,(3,0):C.GC_790,(0,5):C.GC_789,(2,5):C.GC_791,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_788,(3,8):C.GC_790,(0,1):C.GC_789,(2,1):C.GC_791})

V_1600 = Vertex(name = 'V_1600',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_3696,(1,0):C.GC_3137,(3,0):C.GC_3147,(0,5):C.GC_3132,(2,5):C.GC_3142,(1,4):C.GC_3625,(3,4):C.GC_3633,(1,2):C.GC_3254,(3,2):C.GC_3259,(1,3):C.GC_811,(3,3):C.GC_814,(1,8):C.GC_3137,(3,8):C.GC_3147,(0,1):C.GC_3132,(2,1):C.GC_3142})

V_1601 = Vertex(name = 'V_1601',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3667,(0,2):C.GC_3043,(1,0):C.GC_3153,(2,0):C.GC_3156})

V_1602 = Vertex(name = 'V_1602',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3614,(0,1):C.GC_3202})

V_1603 = Vertex(name = 'V_1603',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3034})

V_1604 = Vertex(name = 'V_1604',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3052})

V_1605 = Vertex(name = 'V_1605',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3193})

V_1606 = Vertex(name = 'V_1606',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3210})

V_1607 = Vertex(name = 'V_1607',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1258,(0,5):C.GC_1267,(1,0):C.GC_3239,(3,0):C.GC_3243,(0,3):C.GC_3237,(2,3):C.GC_3241,(1,2):C.GC_1386,(3,2):C.GC_1389,(1,6):C.GC_3229,(3,6):C.GC_3231,(0,1):C.GC_3228,(2,1):C.GC_3230})

V_1608 = Vertex(name = 'V_1608',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1276,(0,2):C.GC_3183,(1,0):C.GC_3256,(2,0):C.GC_3261})

V_1609 = Vertex(name = 'V_1609',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3181,(0,1):C.GC_3212})

V_1610 = Vertex(name = 'V_1610',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3203})

V_1611 = Vertex(name = 'V_1611',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3185})

V_1612 = Vertex(name = 'V_1612',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3278})

V_1613 = Vertex(name = 'V_1613',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1971,(0,5):C.GC_1980,(1,0):C.GC_2114,(3,0):C.GC_2120,(0,3):C.GC_2111,(2,3):C.GC_2117,(1,2):C.GC_2105,(3,2):C.GC_2108,(1,6):C.GC_2005,(3,6):C.GC_2011,(0,1):C.GC_2002,(2,1):C.GC_2008})

V_1614 = Vertex(name = 'V_1614',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1989,(0,1):C.GC_2160})

V_1615 = Vertex(name = 'V_1615',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2157})

V_1616 = Vertex(name = 'V_1616',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2163})

V_1617 = Vertex(name = 'V_1617',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3029,(0,5):C.GC_3038,(1,0):C.GC_3167,(3,0):C.GC_3173,(0,3):C.GC_3164,(2,3):C.GC_3170,(1,2):C.GC_3176,(3,2):C.GC_3179,(1,6):C.GC_3096,(3,6):C.GC_3102,(0,1):C.GC_3093,(2,1):C.GC_3099})

V_1618 = Vertex(name = 'V_1618',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3047,(0,1):C.GC_3288})

V_1619 = Vertex(name = 'V_1619',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3281})

V_1620 = Vertex(name = 'V_1620',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3297})

V_1621 = Vertex(name = 'V_1621',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1261,(0,5):C.GC_1270,(1,0):C.GC_1306,(3,0):C.GC_1312,(0,3):C.GC_1303,(2,3):C.GC_1309,(1,2):C.GC_1344,(3,2):C.GC_1347,(1,6):C.GC_1336,(3,6):C.GC_1340,(0,1):C.GC_1334,(2,1):C.GC_1338})

V_1622 = Vertex(name = 'V_1622',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1279,(0,1):C.GC_1401})

V_1623 = Vertex(name = 'V_1623',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1394})

V_1624 = Vertex(name = 'V_1624',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1408})

V_1625 = Vertex(name = 'V_1625',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1974,(0,5):C.GC_3212,(1,0):C.GC_2052,(3,0):C.GC_2062,(0,3):C.GC_2047,(2,3):C.GC_2057,(1,2):C.GC_2016,(3,2):C.GC_2019,(1,6):C.GC_2006,(3,6):C.GC_2012,(0,1):C.GC_2003,(2,1):C.GC_2009})

V_1626 = Vertex(name = 'V_1626',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1992,(0,2):C.GC_1983,(1,0):C.GC_3256,(2,0):C.GC_3261})

V_1627 = Vertex(name = 'V_1627',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2124,(0,1):C.GC_2127})

V_1628 = Vertex(name = 'V_1628',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2130})

V_1629 = Vertex(name = 'V_1629',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3278})

V_1630 = Vertex(name = 'V_1630',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3294})

V_1631 = Vertex(name = 'V_1631',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3032,(0,5):C.GC_3041,(1,0):C.GC_3084,(3,0):C.GC_3090,(0,3):C.GC_3081,(2,3):C.GC_3087,(1,2):C.GC_3107,(3,2):C.GC_3110,(1,6):C.GC_3097,(3,6):C.GC_3103,(0,1):C.GC_3094,(2,1):C.GC_3100})

V_1632 = Vertex(name = 'V_1632',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3050,(0,1):C.GC_3197})

V_1633 = Vertex(name = 'V_1633',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3191})

V_1634 = Vertex(name = 'V_1634',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3207})

V_1635 = Vertex(name = 'V_1635',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1264,(0,5):C.GC_1273,(1,0):C.GC_1326,(3,0):C.GC_1332,(0,3):C.GC_1323,(2,3):C.GC_1329,(1,2):C.GC_1377,(3,2):C.GC_1380,(1,6):C.GC_1337,(3,6):C.GC_1341,(0,1):C.GC_1335,(2,1):C.GC_1339})

V_1636 = Vertex(name = 'V_1636',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1282,(0,1):C.GC_1404})

V_1637 = Vertex(name = 'V_1637',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1397})

V_1638 = Vertex(name = 'V_1638',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1411})

V_1639 = Vertex(name = 'V_1639',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1977,(0,6):C.GC_1986,(1,0):C.GC_2092,(3,0):C.GC_2098,(0,4):C.GC_2089,(2,4):C.GC_2095,(1,3):C.GC_669,(3,3):C.GC_670,(1,2):C.GC_2083,(3,2):C.GC_2086,(1,7):C.GC_2007,(3,7):C.GC_2013,(0,1):C.GC_2004,(2,1):C.GC_2010})

V_1640 = Vertex(name = 'V_1640',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1995,(0,1):C.GC_2147})

V_1641 = Vertex(name = 'V_1641',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2144})

V_1642 = Vertex(name = 'V_1642',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2150})

V_1643 = Vertex(name = 'V_1643',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3278,(0,5):C.GC_3212,(1,0):C.GC_3138,(3,0):C.GC_3148,(0,3):C.GC_3133,(2,3):C.GC_3143,(1,2):C.GC_3256,(3,2):C.GC_3261,(1,6):C.GC_3098,(3,6):C.GC_3104,(0,1):C.GC_3095,(2,1):C.GC_3101})

V_1644 = Vertex(name = 'V_1644',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3294,(0,2):C.GC_3044,(1,0):C.GC_3154,(2,0):C.GC_3157})

V_1645 = Vertex(name = 'V_1645',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3035,(0,1):C.GC_3204})

V_1646 = Vertex(name = 'V_1646',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3053})

V_1647 = Vertex(name = 'V_1647',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3194})

V_1648 = Vertex(name = 'V_1648',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3211})

V_1649 = Vertex(name = 'V_1649',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1428,(0,5):C.GC_1437,(1,0):C.GC_3915,(3,0):C.GC_3919,(0,3):C.GC_3913,(2,3):C.GC_3917,(1,2):C.GC_1556,(3,2):C.GC_1559,(1,6):C.GC_3924,(3,6):C.GC_3928,(0,1):C.GC_3922,(2,1):C.GC_3926})

V_1650 = Vertex(name = 'V_1650',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1446,(0,2):C.GC_3684,(1,0):C.GC_4009,(2,0):C.GC_4014})

V_1651 = Vertex(name = 'V_1651',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3675,(0,1):C.GC_3882})

V_1652 = Vertex(name = 'V_1652',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3869})

V_1653 = Vertex(name = 'V_1653',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3691})

V_1654 = Vertex(name = 'V_1654',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4031})

V_1655 = Vertex(name = 'V_1655',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2165,(0,5):C.GC_2174,(1,0):C.GC_2303,(3,0):C.GC_2309,(0,3):C.GC_2300,(2,3):C.GC_2306,(1,2):C.GC_2312,(3,2):C.GC_2315,(1,6):C.GC_2231,(3,6):C.GC_2237,(0,1):C.GC_2228,(2,1):C.GC_2234})

V_1656 = Vertex(name = 'V_1656',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2183,(0,1):C.GC_2629})

V_1657 = Vertex(name = 'V_1657',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2623})

V_1658 = Vertex(name = 'V_1658',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2635})

V_1659 = Vertex(name = 'V_1659',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3456,(0,6):C.GC_3465,(1,0):C.GC_3594,(3,0):C.GC_3600,(0,4):C.GC_3591,(2,4):C.GC_3597,(1,3):C.GC_501,(3,3):C.GC_502,(1,2):C.GC_3603,(3,2):C.GC_3606,(1,7):C.GC_3554,(3,7):C.GC_3560,(0,1):C.GC_3551,(2,1):C.GC_3557})

V_1660 = Vertex(name = 'V_1660',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3474,(0,1):C.GC_4046})

V_1661 = Vertex(name = 'V_1661',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4038})

V_1662 = Vertex(name = 'V_1662',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4056})

V_1663 = Vertex(name = 'V_1663',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1431,(0,5):C.GC_1440,(1,0):C.GC_1464,(3,0):C.GC_1470,(0,3):C.GC_1461,(2,3):C.GC_1467,(1,2):C.GC_1519,(3,2):C.GC_1522,(1,6):C.GC_1527,(3,6):C.GC_1531,(0,1):C.GC_1525,(2,1):C.GC_1529})

V_1664 = Vertex(name = 'V_1664',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1449,(0,1):C.GC_1763})

V_1665 = Vertex(name = 'V_1665',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1754})

V_1666 = Vertex(name = 'V_1666',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1772})

V_1667 = Vertex(name = 'V_1667',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2168,(0,5):C.GC_3882,(1,0):C.GC_2204,(3,0):C.GC_2214,(0,3):C.GC_2199,(2,3):C.GC_2209,(1,2):C.GC_2222,(3,2):C.GC_2225,(1,6):C.GC_2232,(3,6):C.GC_2238,(0,1):C.GC_2229,(2,1):C.GC_2235})

V_1668 = Vertex(name = 'V_1668',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2186,(0,2):C.GC_2177,(1,0):C.GC_4009,(2,0):C.GC_4014})

V_1669 = Vertex(name = 'V_1669',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2375,(0,1):C.GC_2381})

V_1670 = Vertex(name = 'V_1670',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2387})

V_1671 = Vertex(name = 'V_1671',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4031})

V_1672 = Vertex(name = 'V_1672',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4051})

V_1673 = Vertex(name = 'V_1673',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3459,(0,5):C.GC_3468,(1,0):C.GC_3499,(3,0):C.GC_3505,(0,3):C.GC_3496,(2,3):C.GC_3502,(1,2):C.GC_3545,(3,2):C.GC_3548,(1,6):C.GC_3555,(3,6):C.GC_3561,(0,1):C.GC_3552,(2,1):C.GC_3558})

V_1674 = Vertex(name = 'V_1674',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3477,(0,1):C.GC_3865})

V_1675 = Vertex(name = 'V_1675',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3858})

V_1676 = Vertex(name = 'V_1676',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3877})

V_1677 = Vertex(name = 'V_1677',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1434,(0,5):C.GC_1443,(1,0):C.GC_1496,(3,0):C.GC_1502,(0,3):C.GC_1493,(2,3):C.GC_1499,(1,2):C.GC_1547,(3,2):C.GC_1550,(1,6):C.GC_1528,(3,6):C.GC_1532,(0,1):C.GC_1526,(2,1):C.GC_1530})

V_1678 = Vertex(name = 'V_1678',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1452,(0,1):C.GC_1767})

V_1679 = Vertex(name = 'V_1679',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1758})

V_1680 = Vertex(name = 'V_1680',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1776})

V_1681 = Vertex(name = 'V_1681',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2171,(0,5):C.GC_2180,(1,0):C.GC_2281,(3,0):C.GC_2287,(0,3):C.GC_2278,(2,3):C.GC_2284,(1,2):C.GC_2290,(3,2):C.GC_2293,(1,6):C.GC_2233,(3,6):C.GC_2239,(0,1):C.GC_2230,(2,1):C.GC_2236})

V_1682 = Vertex(name = 'V_1682',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2189,(0,1):C.GC_2548})

V_1683 = Vertex(name = 'V_1683',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2544})

V_1684 = Vertex(name = 'V_1684',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2552})

V_1685 = Vertex(name = 'V_1685',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_4031,(0,5):C.GC_3882,(1,0):C.GC_3529,(3,0):C.GC_3539,(0,3):C.GC_3524,(2,3):C.GC_3534,(1,2):C.GC_4009,(3,2):C.GC_4014,(1,6):C.GC_3556,(3,6):C.GC_3562,(0,1):C.GC_3553,(2,1):C.GC_3559})

V_1686 = Vertex(name = 'V_1686',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4051,(0,2):C.GC_3471,(1,0):C.GC_3581,(2,0):C.GC_3584})

V_1687 = Vertex(name = 'V_1687',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3462,(0,1):C.GC_3870})

V_1688 = Vertex(name = 'V_1688',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3480})

V_1689 = Vertex(name = 'V_1689',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3862})

V_1690 = Vertex(name = 'V_1690',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3881})

V_1691 = Vertex(name = 'V_1691',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1429,(0,5):C.GC_1438,(1,0):C.GC_3916,(3,0):C.GC_3920,(0,3):C.GC_3914,(2,3):C.GC_3918,(1,2):C.GC_1557,(3,2):C.GC_1560,(1,6):C.GC_3992,(3,6):C.GC_3994,(0,1):C.GC_3991,(2,1):C.GC_3993})

V_1692 = Vertex(name = 'V_1692',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1447,(0,2):C.GC_3754,(1,0):C.GC_4010,(2,0):C.GC_4015})

V_1693 = Vertex(name = 'V_1693',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3753,(0,1):C.GC_3884})

V_1694 = Vertex(name = 'V_1694',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3871})

V_1695 = Vertex(name = 'V_1695',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3755})

V_1696 = Vertex(name = 'V_1696',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4032})

V_1697 = Vertex(name = 'V_1697',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2166,(0,5):C.GC_2175,(1,0):C.GC_2304,(3,0):C.GC_2310,(0,3):C.GC_2301,(2,3):C.GC_2307,(1,2):C.GC_2313,(3,2):C.GC_2316,(1,6):C.GC_2257,(3,6):C.GC_2263,(0,1):C.GC_2254,(2,1):C.GC_2260})

V_1698 = Vertex(name = 'V_1698',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2184,(0,1):C.GC_2630})

V_1699 = Vertex(name = 'V_1699',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2624})

V_1700 = Vertex(name = 'V_1700',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2636})

V_1701 = Vertex(name = 'V_1701',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3457,(0,5):C.GC_3466,(1,0):C.GC_3595,(3,0):C.GC_3601,(0,3):C.GC_3592,(2,3):C.GC_3598,(1,2):C.GC_3604,(3,2):C.GC_3607,(1,6):C.GC_3572,(3,6):C.GC_3578,(0,1):C.GC_3569,(2,1):C.GC_3575})

V_1702 = Vertex(name = 'V_1702',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3475,(0,1):C.GC_4047})

V_1703 = Vertex(name = 'V_1703',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4039})

V_1704 = Vertex(name = 'V_1704',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4057})

V_1705 = Vertex(name = 'V_1705',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1432,(0,5):C.GC_1441,(1,0):C.GC_1465,(3,0):C.GC_1471,(0,3):C.GC_1462,(2,3):C.GC_1468,(1,2):C.GC_1520,(3,2):C.GC_1523,(1,6):C.GC_1541,(3,6):C.GC_1545,(0,1):C.GC_1539,(2,1):C.GC_1543})

V_1706 = Vertex(name = 'V_1706',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1450,(0,1):C.GC_1764})

V_1707 = Vertex(name = 'V_1707',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1755})

V_1708 = Vertex(name = 'V_1708',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1773})

V_1709 = Vertex(name = 'V_1709',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2169,(0,5):C.GC_3884,(1,0):C.GC_2205,(3,0):C.GC_2215,(0,3):C.GC_2200,(2,3):C.GC_2210,(1,2):C.GC_2223,(3,2):C.GC_2226,(1,6):C.GC_2258,(3,6):C.GC_2264,(0,1):C.GC_2255,(2,1):C.GC_2261})

V_1710 = Vertex(name = 'V_1710',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2187,(0,2):C.GC_2178,(1,0):C.GC_4010,(2,0):C.GC_4015})

V_1711 = Vertex(name = 'V_1711',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2508,(0,1):C.GC_2509})

V_1712 = Vertex(name = 'V_1712',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2510})

V_1713 = Vertex(name = 'V_1713',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4032})

V_1714 = Vertex(name = 'V_1714',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4053})

V_1715 = Vertex(name = 'V_1715',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3460,(0,6):C.GC_3469,(1,0):C.GC_3500,(3,0):C.GC_3506,(0,4):C.GC_3497,(2,4):C.GC_3503,(1,3):C.GC_669,(3,3):C.GC_670,(1,2):C.GC_3546,(3,2):C.GC_3549,(1,7):C.GC_3573,(3,7):C.GC_3579,(0,1):C.GC_3570,(2,1):C.GC_3576})

V_1716 = Vertex(name = 'V_1716',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3478,(0,1):C.GC_3866})

V_1717 = Vertex(name = 'V_1717',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3859})

V_1718 = Vertex(name = 'V_1718',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3878})

V_1719 = Vertex(name = 'V_1719',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1435,(0,5):C.GC_1444,(1,0):C.GC_1497,(3,0):C.GC_1503,(0,3):C.GC_1494,(2,3):C.GC_1500,(1,2):C.GC_1548,(3,2):C.GC_1551,(1,6):C.GC_1542,(3,6):C.GC_1546,(0,1):C.GC_1540,(2,1):C.GC_1544})

V_1720 = Vertex(name = 'V_1720',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1453,(0,1):C.GC_1768})

V_1721 = Vertex(name = 'V_1721',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1759})

V_1722 = Vertex(name = 'V_1722',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1777})

V_1723 = Vertex(name = 'V_1723',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2172,(0,5):C.GC_2181,(1,0):C.GC_2282,(3,0):C.GC_2288,(0,3):C.GC_2279,(2,3):C.GC_2285,(1,2):C.GC_2291,(3,2):C.GC_2294,(1,6):C.GC_2259,(3,6):C.GC_2265,(0,1):C.GC_2256,(2,1):C.GC_2262})

V_1724 = Vertex(name = 'V_1724',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2190,(0,1):C.GC_2549})

V_1725 = Vertex(name = 'V_1725',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2545})

V_1726 = Vertex(name = 'V_1726',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2553})

V_1727 = Vertex(name = 'V_1727',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_4032,(0,5):C.GC_3884,(1,0):C.GC_3530,(3,0):C.GC_3540,(0,3):C.GC_3525,(2,3):C.GC_3535,(1,2):C.GC_4010,(3,2):C.GC_4015,(1,6):C.GC_3574,(3,6):C.GC_3580,(0,1):C.GC_3571,(2,1):C.GC_3577})

V_1728 = Vertex(name = 'V_1728',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4053,(0,2):C.GC_3472,(1,0):C.GC_3582,(2,0):C.GC_3585})

V_1729 = Vertex(name = 'V_1729',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3463,(0,1):C.GC_3872})

V_1730 = Vertex(name = 'V_1730',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3481})

V_1731 = Vertex(name = 'V_1731',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3863})

V_1732 = Vertex(name = 'V_1732',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3883})

V_1733 = Vertex(name = 'V_1733',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_966,(3,0):C.GC_968,(0,5):C.GC_1103,(2,5):C.GC_1104,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_966,(3,8):C.GC_968,(0,1):C.GC_1103,(2,1):C.GC_1104})

V_1734 = Vertex(name = 'V_1734',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_4066,(1,0):C.GC_1508,(3,0):C.GC_1513,(0,5):C.GC_967,(2,5):C.GC_969,(1,4):C.GC_3626,(3,4):C.GC_3634,(1,2):C.GC_4013,(3,2):C.GC_4018,(1,3):C.GC_1044,(3,3):C.GC_1047,(1,8):C.GC_1508,(3,8):C.GC_1513,(0,1):C.GC_967,(2,1):C.GC_969})

V_1735 = Vertex(name = 'V_1735',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4035,(0,2):C.GC_1439,(1,0):C.GC_1558,(2,0):C.GC_1561})

V_1736 = Vertex(name = 'V_1736',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3873,(0,1):C.GC_1762})

V_1737 = Vertex(name = 'V_1737',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1430})

V_1738 = Vertex(name = 'V_1738',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1448})

V_1739 = Vertex(name = 'V_1739',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1753})

V_1740 = Vertex(name = 'V_1740',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1771})

V_1741 = Vertex(name = 'V_1741',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2370,(0,6):C.GC_2323,(1,0):C.GC_2305,(3,0):C.GC_2311,(0,4):C.GC_2302,(2,4):C.GC_2308,(1,3):C.GC_2340,(3,3):C.GC_2345,(1,2):C.GC_2314,(3,2):C.GC_2317,(1,7):C.GC_2203,(3,7):C.GC_2213,(0,1):C.GC_2198,(2,1):C.GC_2208})

V_1742 = Vertex(name = 'V_1742',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2380,(0,1):C.GC_2176})

V_1743 = Vertex(name = 'V_1743',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2167,(0,1):C.GC_2632})

V_1744 = Vertex(name = 'V_1744',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2185})

V_1745 = Vertex(name = 'V_1745',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2626})

V_1746 = Vertex(name = 'V_1746',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2637})

V_1747 = Vertex(name = 'V_1747',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3663,(0,6):C.GC_3615,(1,0):C.GC_3596,(3,0):C.GC_3602,(0,4):C.GC_3593,(2,4):C.GC_3599,(1,3):C.GC_3621,(3,3):C.GC_3629,(1,2):C.GC_3605,(3,2):C.GC_3608,(1,7):C.GC_3527,(3,7):C.GC_3537,(0,1):C.GC_3522,(2,1):C.GC_3532})

V_1748 = Vertex(name = 'V_1748',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3681,(0,1):C.GC_3467})

V_1749 = Vertex(name = 'V_1749',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3458,(0,1):C.GC_4049})

V_1750 = Vertex(name = 'V_1750',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3476})

V_1751 = Vertex(name = 'V_1751',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4041})

V_1752 = Vertex(name = 'V_1752',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4058})

V_1753 = Vertex(name = 'V_1753',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1590,(0,6):C.GC_1568,(1,0):C.GC_1466,(3,0):C.GC_1472,(0,4):C.GC_1463,(2,4):C.GC_1469,(1,3):C.GC_1574,(3,3):C.GC_1576,(1,2):C.GC_1521,(3,2):C.GC_1524,(1,7):C.GC_1509,(3,7):C.GC_1514,(0,1):C.GC_1506,(2,1):C.GC_1511})

V_1754 = Vertex(name = 'V_1754',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1595,(0,1):C.GC_1442})

V_1755 = Vertex(name = 'V_1755',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1433,(0,1):C.GC_1766})

V_1756 = Vertex(name = 'V_1756',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1451})

V_1757 = Vertex(name = 'V_1757',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1757})

V_1758 = Vertex(name = 'V_1758',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1774})

V_1759 = Vertex(name = 'V_1759',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_448,(3,0):C.GC_450,(0,5):C.GC_449,(2,5):C.GC_451,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_448,(3,8):C.GC_450,(0,1):C.GC_449,(2,1):C.GC_451})

V_1760 = Vertex(name = 'V_1760',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_4064,(1,0):C.GC_2206,(3,0):C.GC_2216,(0,5):C.GC_2201,(2,5):C.GC_2211,(1,4):C.GC_2341,(3,4):C.GC_2346,(1,2):C.GC_4011,(3,2):C.GC_4016,(1,3):C.GC_465,(3,3):C.GC_466,(1,8):C.GC_2206,(3,8):C.GC_2216,(0,1):C.GC_2201,(2,1):C.GC_2211})

V_1761 = Vertex(name = 'V_1761',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4033,(0,2):C.GC_2179,(1,0):C.GC_2224,(2,0):C.GC_2227})

V_1762 = Vertex(name = 'V_1762',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3874,(0,1):C.GC_2327})

V_1763 = Vertex(name = 'V_1763',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2170})

V_1764 = Vertex(name = 'V_1764',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2188})

V_1765 = Vertex(name = 'V_1765',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2326})

V_1766 = Vertex(name = 'V_1766',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2328})

V_1767 = Vertex(name = 'V_1767',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3664,(0,6):C.GC_3616,(1,0):C.GC_3501,(3,0):C.GC_3507,(0,4):C.GC_3498,(2,4):C.GC_3504,(1,3):C.GC_3622,(3,3):C.GC_3630,(1,2):C.GC_3547,(3,2):C.GC_3550,(1,7):C.GC_3528,(3,7):C.GC_3538,(0,1):C.GC_3523,(2,1):C.GC_3533})

V_1768 = Vertex(name = 'V_1768',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3683,(0,1):C.GC_3470})

V_1769 = Vertex(name = 'V_1769',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3461,(0,1):C.GC_3868})

V_1770 = Vertex(name = 'V_1770',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3479})

V_1771 = Vertex(name = 'V_1771',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3861})

V_1772 = Vertex(name = 'V_1772',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3879})

V_1773 = Vertex(name = 'V_1773',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1591,(0,6):C.GC_1569,(1,0):C.GC_1498,(3,0):C.GC_1504,(0,4):C.GC_1495,(2,4):C.GC_1501,(1,3):C.GC_1575,(3,3):C.GC_1577,(1,2):C.GC_1549,(3,2):C.GC_1552,(1,7):C.GC_1510,(3,7):C.GC_1515,(0,1):C.GC_1507,(2,1):C.GC_1512})

V_1774 = Vertex(name = 'V_1774',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1597,(0,1):C.GC_1445})

V_1775 = Vertex(name = 'V_1775',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1436,(0,1):C.GC_1770})

V_1776 = Vertex(name = 'V_1776',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1454})

V_1777 = Vertex(name = 'V_1777',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1761})

V_1778 = Vertex(name = 'V_1778',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1778})

V_1779 = Vertex(name = 'V_1779',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2373,(0,6):C.GC_2324,(1,0):C.GC_2283,(3,0):C.GC_2289,(0,4):C.GC_2280,(2,4):C.GC_2286,(1,3):C.GC_2344,(3,3):C.GC_2349,(1,2):C.GC_2292,(3,2):C.GC_2295,(1,7):C.GC_2207,(3,7):C.GC_2217,(0,1):C.GC_2202,(2,1):C.GC_2212})

V_1780 = Vertex(name = 'V_1780',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2385,(0,1):C.GC_2182})

V_1781 = Vertex(name = 'V_1781',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2173,(0,1):C.GC_2551})

V_1782 = Vertex(name = 'V_1782',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2191})

V_1783 = Vertex(name = 'V_1783',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2547})

V_1784 = Vertex(name = 'V_1784',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2554})

V_1785 = Vertex(name = 'V_1785',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_56,(1,0):C.GC_748,(3,0):C.GC_750,(0,5):C.GC_749,(2,5):C.GC_751,(1,4):C.GC_48,(3,4):C.GC_49,(1,2):C.GC_57,(3,2):C.GC_58,(1,3):C.GC_61,(3,3):C.GC_62,(1,8):C.GC_748,(3,8):C.GC_750,(0,1):C.GC_749,(2,1):C.GC_751})

V_1786 = Vertex(name = 'V_1786',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_53,(0,7):C.GC_4065,(1,0):C.GC_3531,(3,0):C.GC_3541,(0,5):C.GC_3526,(2,5):C.GC_3536,(1,4):C.GC_408,(3,4):C.GC_409,(1,2):C.GC_4012,(3,2):C.GC_4017,(1,3):C.GC_809,(3,3):C.GC_812,(1,8):C.GC_3531,(3,8):C.GC_3541,(0,1):C.GC_3526,(2,1):C.GC_3536})

V_1787 = Vertex(name = 'V_1787',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4034,(0,3):C.GC_3473,(1,1):C.GC_3623,(2,1):C.GC_3631,(1,0):C.GC_3583,(2,0):C.GC_3586})

V_1788 = Vertex(name = 'V_1788',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3875,(0,1):C.GC_3876})

V_1789 = Vertex(name = 'V_1789',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3464})

V_1790 = Vertex(name = 'V_1790',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3482})

V_1791 = Vertex(name = 'V_1791',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3864})

V_1792 = Vertex(name = 'V_1792',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3885})

V_1793 = Vertex(name = 'V_1793',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_987,(0,9):C.GC_986,(0,10):C.GC_986,(0,6):C.GC_982,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_987,(0,4):C.GC_986,(0,5):C.GC_986,(0,0):C.GC_982})

V_1794 = Vertex(name = 'V_1794',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_3984,(0,9):C.GC_3983,(0,10):C.GC_3983,(0,6):C.GC_3980,(0,1):C.GC_3662,(0,2):C.GC_1030,(0,3):C.GC_1029,(0,7):C.GC_3984,(0,4):C.GC_3983,(0,5):C.GC_3983,(0,0):C.GC_3980})

V_1795 = Vertex(name = 'V_1795',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1796 = Vertex(name = 'V_1796',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3656})

V_1797 = Vertex(name = 'V_1797',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2358,(0,9):C.GC_2601,(0,7):C.GC_2600,(0,8):C.GC_2600,(0,4):C.GC_2599,(0,1):C.GC_2367,(0,5):C.GC_2490,(0,2):C.GC_2489,(0,3):C.GC_2489,(0,0):C.GC_2486})

V_1798 = Vertex(name = 'V_1798',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2362})

V_1799 = Vertex(name = 'V_1799',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3647,(0,9):C.GC_3982,(0,7):C.GC_3981,(0,8):C.GC_3981,(0,4):C.GC_3979,(0,1):C.GC_3659,(0,5):C.GC_3841,(0,2):C.GC_3840,(0,3):C.GC_3840,(0,0):C.GC_3837})

V_1800 = Vertex(name = 'V_1800',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3652})

V_1801 = Vertex(name = 'V_1801',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1582,(0,9):C.GC_1637,(0,7):C.GC_1636,(0,8):C.GC_1636,(0,4):C.GC_1635,(0,1):C.GC_1588,(0,5):C.GC_1737,(0,2):C.GC_1736,(0,3):C.GC_1736,(0,0):C.GC_1734})

V_1802 = Vertex(name = 'V_1802',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1585})

V_1803 = Vertex(name = 'V_1803',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_564,(0,9):C.GC_563,(0,10):C.GC_563,(0,6):C.GC_559,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_564,(0,4):C.GC_563,(0,5):C.GC_563,(0,0):C.GC_559})

V_1804 = Vertex(name = 'V_1804',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_2492,(0,9):C.GC_2491,(0,10):C.GC_2491,(0,6):C.GC_2487,(0,1):C.GC_2368,(0,2):C.GC_458,(0,3):C.GC_457,(0,7):C.GC_2492,(0,4):C.GC_2491,(0,5):C.GC_2491,(0,0):C.GC_2487})

V_1805 = Vertex(name = 'V_1805',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_1806 = Vertex(name = 'V_1806',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2364})

V_1807 = Vertex(name = 'V_1807',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3648,(0,9):C.GC_3749,(0,7):C.GC_3748,(0,8):C.GC_3748,(0,4):C.GC_3747,(0,1):C.GC_3660,(0,5):C.GC_3843,(0,2):C.GC_3842,(0,3):C.GC_3842,(0,0):C.GC_3838})

V_1808 = Vertex(name = 'V_1808',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3654})

V_1809 = Vertex(name = 'V_1809',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1583,(0,9):C.GC_1670,(0,7):C.GC_1669,(0,8):C.GC_1669,(0,4):C.GC_1668,(0,1):C.GC_1589,(0,5):C.GC_1739,(0,2):C.GC_1738,(0,3):C.GC_1738,(0,0):C.GC_1735})

V_1810 = Vertex(name = 'V_1810',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1587})

V_1811 = Vertex(name = 'V_1811',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2360,(0,9):C.GC_2540,(0,7):C.GC_2539,(0,8):C.GC_2539,(0,4):C.GC_2538,(0,1):C.GC_2369,(0,5):C.GC_2494,(0,2):C.GC_2493,(0,3):C.GC_2493,(0,0):C.GC_2488})

V_1812 = Vertex(name = 'V_1812',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2366})

V_1813 = Vertex(name = 'V_1813',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_769,(0,9):C.GC_768,(0,10):C.GC_768,(0,6):C.GC_764,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_769,(0,4):C.GC_768,(0,5):C.GC_768,(0,0):C.GC_764})

V_1814 = Vertex(name = 'V_1814',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_3845,(0,9):C.GC_3844,(0,10):C.GC_3844,(0,6):C.GC_3839,(0,1):C.GC_3661,(0,2):C.GC_798,(0,3):C.GC_797,(0,7):C.GC_3845,(0,4):C.GC_3844,(0,5):C.GC_3844,(0,0):C.GC_3839})

V_1815 = Vertex(name = 'V_1815',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_1816 = Vertex(name = 'V_1816',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3657})

V_1817 = Vertex(name = 'V_1817',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_999,(0,9):C.GC_998,(0,10):C.GC_998,(0,6):C.GC_994,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_999,(0,4):C.GC_998,(0,5):C.GC_998,(0,0):C.GC_994})

V_1818 = Vertex(name = 'V_1818',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_3990,(0,9):C.GC_3989,(0,10):C.GC_3989,(0,6):C.GC_3986,(0,1):C.GC_3662,(0,2):C.GC_1030,(0,3):C.GC_1029,(0,7):C.GC_3990,(0,4):C.GC_3989,(0,5):C.GC_3989,(0,0):C.GC_3986})

V_1819 = Vertex(name = 'V_1819',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1820 = Vertex(name = 'V_1820',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3656})

V_1821 = Vertex(name = 'V_1821',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2358,(0,9):C.GC_2604,(0,7):C.GC_2603,(0,8):C.GC_2603,(0,4):C.GC_2602,(0,1):C.GC_2367,(0,5):C.GC_2503,(0,2):C.GC_2502,(0,3):C.GC_2502,(0,0):C.GC_2499})

V_1822 = Vertex(name = 'V_1822',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2362})

V_1823 = Vertex(name = 'V_1823',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3647,(0,9):C.GC_3988,(0,7):C.GC_3987,(0,8):C.GC_3987,(0,4):C.GC_3985,(0,1):C.GC_3659,(0,5):C.GC_3850,(0,2):C.GC_3849,(0,3):C.GC_3849,(0,0):C.GC_3846})

V_1824 = Vertex(name = 'V_1824',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3652})

V_1825 = Vertex(name = 'V_1825',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1582,(0,9):C.GC_1640,(0,7):C.GC_1639,(0,8):C.GC_1639,(0,4):C.GC_1638,(0,1):C.GC_1588,(0,5):C.GC_1743,(0,2):C.GC_1742,(0,3):C.GC_1742,(0,0):C.GC_1740})

V_1826 = Vertex(name = 'V_1826',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1585})

V_1827 = Vertex(name = 'V_1827',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_619,(0,9):C.GC_618,(0,10):C.GC_618,(0,6):C.GC_614,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_619,(0,4):C.GC_618,(0,5):C.GC_618,(0,0):C.GC_614})

V_1828 = Vertex(name = 'V_1828',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_2505,(0,9):C.GC_2504,(0,10):C.GC_2504,(0,6):C.GC_2500,(0,1):C.GC_2368,(0,2):C.GC_458,(0,3):C.GC_457,(0,7):C.GC_2505,(0,4):C.GC_2504,(0,5):C.GC_2504,(0,0):C.GC_2500})

V_1829 = Vertex(name = 'V_1829',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_1830 = Vertex(name = 'V_1830',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2364})

V_1831 = Vertex(name = 'V_1831',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3648,(0,9):C.GC_3752,(0,7):C.GC_3751,(0,8):C.GC_3751,(0,4):C.GC_3750,(0,1):C.GC_3660,(0,5):C.GC_3852,(0,2):C.GC_3851,(0,3):C.GC_3851,(0,0):C.GC_3847})

V_1832 = Vertex(name = 'V_1832',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3654})

V_1833 = Vertex(name = 'V_1833',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1583,(0,9):C.GC_1673,(0,7):C.GC_1672,(0,8):C.GC_1672,(0,4):C.GC_1671,(0,1):C.GC_1589,(0,5):C.GC_1745,(0,2):C.GC_1744,(0,3):C.GC_1744,(0,0):C.GC_1741})

V_1834 = Vertex(name = 'V_1834',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1587})

V_1835 = Vertex(name = 'V_1835',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2360,(0,9):C.GC_2543,(0,7):C.GC_2542,(0,8):C.GC_2542,(0,4):C.GC_2541,(0,1):C.GC_2369,(0,5):C.GC_2507,(0,2):C.GC_2506,(0,3):C.GC_2506,(0,0):C.GC_2501})

V_1836 = Vertex(name = 'V_1836',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2366})

V_1837 = Vertex(name = 'V_1837',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_781,(0,9):C.GC_780,(0,10):C.GC_780,(0,6):C.GC_776,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_781,(0,4):C.GC_780,(0,5):C.GC_780,(0,0):C.GC_776})

V_1838 = Vertex(name = 'V_1838',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_3854,(0,9):C.GC_3853,(0,10):C.GC_3853,(0,6):C.GC_3848,(0,1):C.GC_3661,(0,2):C.GC_798,(0,3):C.GC_797,(0,7):C.GC_3854,(0,4):C.GC_3853,(0,5):C.GC_3853,(0,0):C.GC_3848})

V_1839 = Vertex(name = 'V_1839',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_1840 = Vertex(name = 'V_1840',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3657})

V_1841 = Vertex(name = 'V_1841',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_1020,(0,9):C.GC_1019,(0,10):C.GC_1019,(0,6):C.GC_1015,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_1020,(0,4):C.GC_1019,(0,5):C.GC_1019,(0,0):C.GC_1015})

V_1842 = Vertex(name = 'V_1842',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_4000,(0,9):C.GC_3999,(0,10):C.GC_3999,(0,6):C.GC_3996,(0,1):C.GC_3662,(0,2):C.GC_1030,(0,3):C.GC_1029,(0,7):C.GC_4000,(0,4):C.GC_3999,(0,5):C.GC_3999,(0,0):C.GC_3996})

V_1843 = Vertex(name = 'V_1843',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1844 = Vertex(name = 'V_1844',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3656})

V_1845 = Vertex(name = 'V_1845',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2358,(0,9):C.GC_2607,(0,7):C.GC_2606,(0,8):C.GC_2606,(0,4):C.GC_2605,(0,1):C.GC_2367,(0,5):C.GC_2564,(0,2):C.GC_2563,(0,3):C.GC_2563,(0,0):C.GC_2560})

V_1846 = Vertex(name = 'V_1846',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2362})

V_1847 = Vertex(name = 'V_1847',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3647,(0,9):C.GC_3998,(0,7):C.GC_3997,(0,8):C.GC_3997,(0,4):C.GC_3995,(0,1):C.GC_3659,(0,5):C.GC_3904,(0,2):C.GC_3903,(0,3):C.GC_3903,(0,0):C.GC_3900})

V_1848 = Vertex(name = 'V_1848',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3652})

V_1849 = Vertex(name = 'V_1849',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1582,(0,9):C.GC_1676,(0,7):C.GC_1675,(0,8):C.GC_1675,(0,4):C.GC_1674,(0,1):C.GC_1588,(0,5):C.GC_1749,(0,2):C.GC_1748,(0,3):C.GC_1748,(0,0):C.GC_1746})

V_1850 = Vertex(name = 'V_1850',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1585})

V_1851 = Vertex(name = 'V_1851',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_884,(0,9):C.GC_883,(0,10):C.GC_883,(0,6):C.GC_879,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_884,(0,4):C.GC_883,(0,5):C.GC_883,(0,0):C.GC_879})

V_1852 = Vertex(name = 'V_1852',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_2566,(0,9):C.GC_2565,(0,10):C.GC_2565,(0,6):C.GC_2561,(0,1):C.GC_2368,(0,2):C.GC_458,(0,3):C.GC_457,(0,7):C.GC_2566,(0,4):C.GC_2565,(0,5):C.GC_2565,(0,0):C.GC_2561})

V_1853 = Vertex(name = 'V_1853',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_1854 = Vertex(name = 'V_1854',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2364})

V_1855 = Vertex(name = 'V_1855',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3648,(0,9):C.GC_3899,(0,7):C.GC_3898,(0,8):C.GC_3898,(0,4):C.GC_3897,(0,1):C.GC_3660,(0,5):C.GC_3906,(0,2):C.GC_3905,(0,3):C.GC_3905,(0,0):C.GC_3901})

V_1856 = Vertex(name = 'V_1856',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3654})

V_1857 = Vertex(name = 'V_1857',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1583,(0,9):C.GC_1679,(0,7):C.GC_1678,(0,8):C.GC_1678,(0,4):C.GC_1677,(0,1):C.GC_1589,(0,5):C.GC_1751,(0,2):C.GC_1750,(0,3):C.GC_1750,(0,0):C.GC_1747})

V_1858 = Vertex(name = 'V_1858',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1587})

V_1859 = Vertex(name = 'V_1859',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2360,(0,9):C.GC_2571,(0,7):C.GC_2570,(0,8):C.GC_2570,(0,4):C.GC_2569,(0,1):C.GC_2369,(0,5):C.GC_2568,(0,2):C.GC_2567,(0,3):C.GC_2567,(0,0):C.GC_2562})

V_1860 = Vertex(name = 'V_1860',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2366})

V_1861 = Vertex(name = 'V_1861',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_35,(0,11):C.GC_904,(0,9):C.GC_903,(0,10):C.GC_903,(0,6):C.GC_899,(0,1):C.GC_50,(0,2):C.GC_47,(0,3):C.GC_24,(0,7):C.GC_904,(0,4):C.GC_903,(0,5):C.GC_903,(0,0):C.GC_899})

V_1862 = Vertex(name = 'V_1862',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_36,(0,11):C.GC_3908,(0,9):C.GC_3907,(0,10):C.GC_3907,(0,6):C.GC_3902,(0,1):C.GC_3661,(0,2):C.GC_798,(0,3):C.GC_797,(0,7):C.GC_3908,(0,4):C.GC_3907,(0,5):C.GC_3907,(0,0):C.GC_3902})

V_1863 = Vertex(name = 'V_1863',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_1864 = Vertex(name = 'V_1864',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3657})

V_1865 = Vertex(name = 'V_1865',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_57,(2,4):C.GC_58,(0,5):C.GC_63,(0,0):C.GC_57,(2,0):C.GC_58,(1,3):C.GC_57})

V_1866 = Vertex(name = 'V_1866',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(3,3):C.GC_3646,(1,1):C.GC_3641,(3,1):C.GC_3646,(1,2):C.GC_64,(0,4):C.GC_3641,(2,4):C.GC_3646,(0,5):C.GC_64,(0,0):C.GC_3641,(2,0):C.GC_3646,(1,3):C.GC_3641})

V_1867 = Vertex(name = 'V_1867',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(3,3):C.GC_1028,(1,1):C.GC_1027,(3,1):C.GC_1028,(1,2):C.GC_1031,(0,4):C.GC_1027,(2,4):C.GC_1028,(0,5):C.GC_1031,(0,0):C.GC_1027,(2,0):C.GC_1028,(1,3):C.GC_1027})

V_1868 = Vertex(name = 'V_1868',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_1032,(0,1):C.GC_1032})

V_1869 = Vertex(name = 'V_1869',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3672,(0,1):C.GC_3672})

V_1870 = Vertex(name = 'V_1870',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3679,(0,1):C.GC_3679})

V_1871 = Vertex(name = 'V_1871',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3688,(0,1):C.GC_3688})

V_1872 = Vertex(name = 'V_1872',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3697,(0,1):C.GC_3697})

V_1873 = Vertex(name = 'V_1873',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2370,(0,3):C.GC_2370,(1,0):C.GC_2350,(3,0):C.GC_2354,(0,1):C.GC_2350,(2,1):C.GC_2354})

V_1874 = Vertex(name = 'V_1874',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2374,(0,1):C.GC_2374})

V_1875 = Vertex(name = 'V_1875',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2379,(0,1):C.GC_2379})

V_1876 = Vertex(name = 'V_1876',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2386,(0,1):C.GC_2386})

V_1877 = Vertex(name = 'V_1877',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3663,(0,3):C.GC_3663,(1,0):C.GC_3637,(3,0):C.GC_3642,(0,1):C.GC_3637,(2,1):C.GC_3642})

V_1878 = Vertex(name = 'V_1878',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3673,(0,1):C.GC_3673})

V_1879 = Vertex(name = 'V_1879',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3680,(0,1):C.GC_3680})

V_1880 = Vertex(name = 'V_1880',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3689,(0,1):C.GC_3689})

V_1881 = Vertex(name = 'V_1881',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1590,(0,3):C.GC_1590,(0,0):C.GC_1578,(2,0):C.GC_1580,(1,1):C.GC_1578,(3,1):C.GC_1580})

V_1882 = Vertex(name = 'V_1882',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1592,(0,1):C.GC_1592})

V_1883 = Vertex(name = 'V_1883',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1594,(0,1):C.GC_1594})

V_1884 = Vertex(name = 'V_1884',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1598,(0,1):C.GC_1598})

V_1885 = Vertex(name = 'V_1885',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_973,(2,0):C.GC_974,(1,3):C.GC_57,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_973,(2,4):C.GC_974,(0,5):C.GC_64})

V_1886 = Vertex(name = 'V_1886',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_2319,(2,2):C.GC_2320,(1,0):C.GC_1562,(2,0):C.GC_1564,(1,1):C.GC_1037,(0,3):C.GC_1039})

V_1887 = Vertex(name = 'V_1887',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3668,(0,1):C.GC_3677})

V_1888 = Vertex(name = 'V_1888',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3686,(0,1):C.GC_3693})

V_1889 = Vertex(name = 'V_1889',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3664,(0,2):C.GC_3674,(1,0):C.GC_3638,(2,0):C.GC_3643})

V_1890 = Vertex(name = 'V_1890',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3682,(0,1):C.GC_3690})

V_1891 = Vertex(name = 'V_1891',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1591,(0,3):C.GC_1591,(0,0):C.GC_1579,(2,0):C.GC_1581,(1,1):C.GC_1579,(3,1):C.GC_1581})

V_1892 = Vertex(name = 'V_1892',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1593,(0,1):C.GC_1593})

V_1893 = Vertex(name = 'V_1893',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1596,(0,1):C.GC_1596})

V_1894 = Vertex(name = 'V_1894',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1599,(0,1):C.GC_1599})

V_1895 = Vertex(name = 'V_1895',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2373,(0,2):C.GC_2378,(1,0):C.GC_2353,(2,0):C.GC_2357})

V_1896 = Vertex(name = 'V_1896',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2384,(0,1):C.GC_2390})

V_1897 = Vertex(name = 'V_1897',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_1013,(2,0):C.GC_1014,(1,3):C.GC_57,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_1013,(2,4):C.GC_1014,(0,5):C.GC_64})

V_1898 = Vertex(name = 'V_1898',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_3609,(2,2):C.GC_3610,(1,0):C.GC_1563,(2,0):C.GC_1565,(1,1):C.GC_1038,(0,3):C.GC_1040})

V_1899 = Vertex(name = 'V_1899',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2371,(0,1):C.GC_2376})

V_1900 = Vertex(name = 'V_1900',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2382,(0,1):C.GC_2388})

V_1901 = Vertex(name = 'V_1901',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2370,(0,3):C.GC_2370,(1,0):C.GC_2350,(3,0):C.GC_2354,(0,1):C.GC_2350,(2,1):C.GC_2354})

V_1902 = Vertex(name = 'V_1902',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2374,(0,1):C.GC_2374})

V_1903 = Vertex(name = 'V_1903',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2379,(0,1):C.GC_2379})

V_1904 = Vertex(name = 'V_1904',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2386,(0,1):C.GC_2386})

V_1905 = Vertex(name = 'V_1905',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3673,(0,2):C.GC_3663,(0,0):C.GC_3637,(2,0):C.GC_3642})

V_1906 = Vertex(name = 'V_1906',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3689,(0,1):C.GC_3680})

V_1907 = Vertex(name = 'V_1907',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2370,(0,2):C.GC_2374,(1,0):C.GC_2350,(2,0):C.GC_2354})

V_1908 = Vertex(name = 'V_1908',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2379,(0,1):C.GC_2386})

V_1909 = Vertex(name = 'V_1909',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3663,(0,3):C.GC_3663,(1,0):C.GC_3637,(3,0):C.GC_3642,(0,1):C.GC_3637,(2,1):C.GC_3642})

V_1910 = Vertex(name = 'V_1910',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3673,(0,1):C.GC_3673})

V_1911 = Vertex(name = 'V_1911',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3680,(0,1):C.GC_3680})

V_1912 = Vertex(name = 'V_1912',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3689,(0,1):C.GC_3689})

V_1913 = Vertex(name = 'V_1913',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1590,(0,3):C.GC_1590,(0,0):C.GC_1578,(2,0):C.GC_1580,(1,1):C.GC_1578,(3,1):C.GC_1580})

V_1914 = Vertex(name = 'V_1914',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1592,(0,1):C.GC_1592})

V_1915 = Vertex(name = 'V_1915',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1594,(0,1):C.GC_1594})

V_1916 = Vertex(name = 'V_1916',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1598,(0,1):C.GC_1598})

V_1917 = Vertex(name = 'V_1917',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1593,(0,2):C.GC_1591,(0,0):C.GC_1579,(2,0):C.GC_1581})

V_1918 = Vertex(name = 'V_1918',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1599,(0,1):C.GC_1596})

V_1919 = Vertex(name = 'V_1919',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1590,(0,2):C.GC_1592,(1,0):C.GC_1578,(2,0):C.GC_1580})

V_1920 = Vertex(name = 'V_1920',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1594,(0,1):C.GC_1598})

V_1921 = Vertex(name = 'V_1921',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(0,0):C.GC_57,(2,0):C.GC_58,(1,3):C.GC_57,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_57,(2,4):C.GC_58,(0,5):C.GC_63})

V_1922 = Vertex(name = 'V_1922',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(0,0):C.GC_455,(2,0):C.GC_456,(1,3):C.GC_455,(3,3):C.GC_456,(1,1):C.GC_455,(3,1):C.GC_456,(1,2):C.GC_64,(0,4):C.GC_455,(2,4):C.GC_456,(0,5):C.GC_64})

V_1923 = Vertex(name = 'V_1923',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(0,0):C.GC_2351,(2,0):C.GC_2355,(1,3):C.GC_2351,(3,3):C.GC_2355,(1,1):C.GC_2351,(3,1):C.GC_2355,(1,2):C.GC_459,(0,4):C.GC_2351,(2,4):C.GC_2355,(0,5):C.GC_459})

V_1924 = Vertex(name = 'V_1924',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_460,(0,1):C.GC_460})

V_1925 = Vertex(name = 'V_1925',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2372,(0,1):C.GC_2372})

V_1926 = Vertex(name = 'V_1926',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2377,(0,1):C.GC_2377})

V_1927 = Vertex(name = 'V_1927',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2383,(0,1):C.GC_2383})

V_1928 = Vertex(name = 'V_1928',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2389,(0,1):C.GC_2389})

V_1929 = Vertex(name = 'V_1929',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3664,(0,3):C.GC_3664,(1,0):C.GC_3638,(3,0):C.GC_3643,(0,1):C.GC_3638,(2,1):C.GC_3643})

V_1930 = Vertex(name = 'V_1930',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3674,(0,1):C.GC_3674})

V_1931 = Vertex(name = 'V_1931',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3682,(0,1):C.GC_3682})

V_1932 = Vertex(name = 'V_1932',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3690,(0,1):C.GC_3690})

V_1933 = Vertex(name = 'V_1933',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2373,(0,3):C.GC_2373,(0,0):C.GC_2353,(2,0):C.GC_2357,(1,1):C.GC_2353,(3,1):C.GC_2357})

V_1934 = Vertex(name = 'V_1934',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2378,(0,1):C.GC_2378})

V_1935 = Vertex(name = 'V_1935',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2384,(0,1):C.GC_2384})

V_1936 = Vertex(name = 'V_1936',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2390,(0,1):C.GC_2390})

V_1937 = Vertex(name = 'V_1937',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_52,(0,0):C.GC_755,(2,0):C.GC_756,(1,3):C.GC_57,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_755,(2,4):C.GC_756,(0,5):C.GC_64})

V_1938 = Vertex(name = 'V_1938',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_54,(0,5):C.GC_55,(1,2):C.GC_3639,(2,2):C.GC_3644,(1,0):C.GC_2352,(2,0):C.GC_2356,(1,1):C.GC_804,(0,3):C.GC_805})

V_1939 = Vertex(name = 'V_1939',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3665,(0,1):C.GC_3676})

V_1940 = Vertex(name = 'V_1940',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3685,(0,1):C.GC_3692})

V_1941 = Vertex(name = 'V_1941',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3664,(0,3):C.GC_3664,(1,0):C.GC_3638,(3,0):C.GC_3643,(0,1):C.GC_3638,(2,1):C.GC_3643})

V_1942 = Vertex(name = 'V_1942',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3674,(0,1):C.GC_3674})

V_1943 = Vertex(name = 'V_1943',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3682,(0,1):C.GC_3682})

V_1944 = Vertex(name = 'V_1944',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3690,(0,1):C.GC_3690})

V_1945 = Vertex(name = 'V_1945',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1591,(0,3):C.GC_1591,(0,0):C.GC_1579,(2,0):C.GC_1581,(1,1):C.GC_1579,(3,1):C.GC_1581})

V_1946 = Vertex(name = 'V_1946',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1593,(0,1):C.GC_1593})

V_1947 = Vertex(name = 'V_1947',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1596,(0,1):C.GC_1596})

V_1948 = Vertex(name = 'V_1948',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1599,(0,1):C.GC_1599})

V_1949 = Vertex(name = 'V_1949',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2373,(0,3):C.GC_2373,(0,0):C.GC_2353,(2,0):C.GC_2357,(1,1):C.GC_2353,(3,1):C.GC_2357})

V_1950 = Vertex(name = 'V_1950',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2378,(0,1):C.GC_2378})

V_1951 = Vertex(name = 'V_1951',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2384,(0,1):C.GC_2384})

V_1952 = Vertex(name = 'V_1952',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2390,(0,1):C.GC_2390})

V_1953 = Vertex(name = 'V_1953',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_51,(0,7):C.GC_51,(0,0):C.GC_57,(2,0):C.GC_58,(1,3):C.GC_57,(3,3):C.GC_58,(1,1):C.GC_57,(3,1):C.GC_58,(1,2):C.GC_63,(0,4):C.GC_57,(2,4):C.GC_58,(0,5):C.GC_63})

V_1954 = Vertex(name = 'V_1954',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_52,(0,7):C.GC_52,(0,0):C.GC_3640,(2,0):C.GC_3645,(1,3):C.GC_3640,(3,3):C.GC_3645,(1,1):C.GC_3640,(3,1):C.GC_3645,(1,2):C.GC_64,(0,4):C.GC_3640,(2,4):C.GC_3645,(0,5):C.GC_64})

V_1955 = Vertex(name = 'V_1955',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_54,(0,7):C.GC_54,(0,0):C.GC_795,(2,0):C.GC_796,(1,3):C.GC_795,(3,3):C.GC_796,(1,1):C.GC_795,(3,1):C.GC_796,(1,2):C.GC_799,(0,4):C.GC_795,(2,4):C.GC_796,(0,5):C.GC_799})

V_1956 = Vertex(name = 'V_1956',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_55,(0,3):C.GC_55,(1,0):C.GC_800,(0,1):C.GC_800})

V_1957 = Vertex(name = 'V_1957',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3671,(0,1):C.GC_3671})

V_1958 = Vertex(name = 'V_1958',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3678,(0,1):C.GC_3678})

V_1959 = Vertex(name = 'V_1959',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3687,(0,1):C.GC_3687})

V_1960 = Vertex(name = 'V_1960',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3694,(0,1):C.GC_3694})

V_1961 = Vertex(name = 'V_1961',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1962 = Vertex(name = 'V_1962',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1963 = Vertex(name = 'V_1963',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1964 = Vertex(name = 'V_1964',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1965 = Vertex(name = 'V_1965',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1966 = Vertex(name = 'V_1966',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1967 = Vertex(name = 'V_1967',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1968 = Vertex(name = 'V_1968',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1969 = Vertex(name = 'V_1969',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1970 = Vertex(name = 'V_1970',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1971 = Vertex(name = 'V_1971',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1972 = Vertex(name = 'V_1972',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1973 = Vertex(name = 'V_1973',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1974 = Vertex(name = 'V_1974',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1975 = Vertex(name = 'V_1975',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1976 = Vertex(name = 'V_1976',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1977 = Vertex(name = 'V_1977',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_33,(0,0):C.GC_32})

V_1978 = Vertex(name = 'V_1978',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_34})

V_1979 = Vertex(name = 'V_1979',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_33})

V_1980 = Vertex(name = 'V_1980',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1981 = Vertex(name = 'V_1981',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_34})

V_1982 = Vertex(name = 'V_1982',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_34})

V_1983 = Vertex(name = 'V_1983',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_33})

V_1984 = Vertex(name = 'V_1984',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1985 = Vertex(name = 'V_1985',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_34})

V_1986 = Vertex(name = 'V_1986',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_33,(0,1):C.GC_33})

V_1987 = Vertex(name = 'V_1987',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_1988 = Vertex(name = 'V_1988',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_1989 = Vertex(name = 'V_1989',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_1030})

V_1990 = Vertex(name = 'V_1990',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1991 = Vertex(name = 'V_1991',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3658})

V_1992 = Vertex(name = 'V_1992',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_1993 = Vertex(name = 'V_1993',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_1030})

V_1994 = Vertex(name = 'V_1994',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1995 = Vertex(name = 'V_1995',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3658})

V_1996 = Vertex(name = 'V_1996',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_1997 = Vertex(name = 'V_1997',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_1030})

V_1998 = Vertex(name = 'V_1998',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3650})

V_1999 = Vertex(name = 'V_1999',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3658})

V_2000 = Vertex(name = 'V_2000',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2358})

V_2001 = Vertex(name = 'V_2001',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2361})

V_2002 = Vertex(name = 'V_2002',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2358})

V_2003 = Vertex(name = 'V_2003',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2361})

V_2004 = Vertex(name = 'V_2004',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2358})

V_2005 = Vertex(name = 'V_2005',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2361})

V_2006 = Vertex(name = 'V_2006',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3647})

V_2007 = Vertex(name = 'V_2007',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3651})

V_2008 = Vertex(name = 'V_2008',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3647})

V_2009 = Vertex(name = 'V_2009',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3651})

V_2010 = Vertex(name = 'V_2010',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3647})

V_2011 = Vertex(name = 'V_2011',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3651})

V_2012 = Vertex(name = 'V_2012',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1582})

V_2013 = Vertex(name = 'V_2013',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1584})

V_2014 = Vertex(name = 'V_2014',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1582})

V_2015 = Vertex(name = 'V_2015',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1584})

V_2016 = Vertex(name = 'V_2016',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1582})

V_2017 = Vertex(name = 'V_2017',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1584})

V_2018 = Vertex(name = 'V_2018',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2019 = Vertex(name = 'V_2019',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_458})

V_2020 = Vertex(name = 'V_2020',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_2021 = Vertex(name = 'V_2021',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2363})

V_2022 = Vertex(name = 'V_2022',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2023 = Vertex(name = 'V_2023',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_458})

V_2024 = Vertex(name = 'V_2024',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_2025 = Vertex(name = 'V_2025',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2363})

V_2026 = Vertex(name = 'V_2026',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2027 = Vertex(name = 'V_2027',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_458})

V_2028 = Vertex(name = 'V_2028',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2359})

V_2029 = Vertex(name = 'V_2029',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2363})

V_2030 = Vertex(name = 'V_2030',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3648})

V_2031 = Vertex(name = 'V_2031',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3653})

V_2032 = Vertex(name = 'V_2032',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3648})

V_2033 = Vertex(name = 'V_2033',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3653})

V_2034 = Vertex(name = 'V_2034',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3648})

V_2035 = Vertex(name = 'V_2035',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3653})

V_2036 = Vertex(name = 'V_2036',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1583})

V_2037 = Vertex(name = 'V_2037',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1586})

V_2038 = Vertex(name = 'V_2038',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1583})

V_2039 = Vertex(name = 'V_2039',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1586})

V_2040 = Vertex(name = 'V_2040',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1583})

V_2041 = Vertex(name = 'V_2041',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1586})

V_2042 = Vertex(name = 'V_2042',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2360})

V_2043 = Vertex(name = 'V_2043',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2365})

V_2044 = Vertex(name = 'V_2044',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2360})

V_2045 = Vertex(name = 'V_2045',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2365})

V_2046 = Vertex(name = 'V_2046',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2360})

V_2047 = Vertex(name = 'V_2047',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2365})

V_2048 = Vertex(name = 'V_2048',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2049 = Vertex(name = 'V_2049',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_798})

V_2050 = Vertex(name = 'V_2050',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_2051 = Vertex(name = 'V_2051',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3655})

V_2052 = Vertex(name = 'V_2052',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2053 = Vertex(name = 'V_2053',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_798})

V_2054 = Vertex(name = 'V_2054',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_2055 = Vertex(name = 'V_2055',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3655})

V_2056 = Vertex(name = 'V_2056',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_47})

V_2057 = Vertex(name = 'V_2057',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_37,(0,0):C.GC_798})

V_2058 = Vertex(name = 'V_2058',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3649})

V_2059 = Vertex(name = 'V_2059',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3655})

V_2060 = Vertex(name = 'V_2060',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1107,(0,4):C.GC_1197,(0,2):C.GC_1196,(0,3):C.GC_1196,(0,0):C.GC_1159,(0,1):C.GC_1195})

V_2061 = Vertex(name = 'V_2061',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1224,(0,4):C.GC_1248,(0,2):C.GC_1247,(0,3):C.GC_1247,(0,0):C.GC_1243,(0,1):C.GC_1246})

V_2062 = Vertex(name = 'V_2062',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1795,(0,4):C.GC_1862,(0,2):C.GC_1861,(0,3):C.GC_1861,(0,0):C.GC_1863,(0,1):C.GC_1860})

V_2063 = Vertex(name = 'V_2063',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1931,(0,4):C.GC_1943,(0,2):C.GC_1942,(0,3):C.GC_1942,(0,0):C.GC_1944,(0,1):C.GC_1941})

V_2064 = Vertex(name = 'V_2064',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2679,(0,4):C.GC_2775,(0,2):C.GC_2774,(0,3):C.GC_2774,(0,0):C.GC_2734,(0,1):C.GC_2773})

V_2065 = Vertex(name = 'V_2065',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2825,(0,4):C.GC_2854,(0,2):C.GC_2853,(0,3):C.GC_2853,(0,0):C.GC_2850,(0,1):C.GC_2852})

V_2066 = Vertex(name = 'V_2066',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1107,(0,4):C.GC_1200,(0,2):C.GC_1199,(0,3):C.GC_1199,(0,0):C.GC_1160,(0,1):C.GC_1198})

V_2067 = Vertex(name = 'V_2067',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1224,(0,4):C.GC_1251,(0,2):C.GC_1250,(0,3):C.GC_1250,(0,0):C.GC_1244,(0,1):C.GC_1249})

V_2068 = Vertex(name = 'V_2068',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1795,(0,4):C.GC_1866,(0,2):C.GC_1865,(0,3):C.GC_1865,(0,0):C.GC_1867,(0,1):C.GC_1864})

V_2069 = Vertex(name = 'V_2069',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1931,(0,4):C.GC_1947,(0,2):C.GC_1946,(0,3):C.GC_1946,(0,0):C.GC_1948,(0,1):C.GC_1945})

V_2070 = Vertex(name = 'V_2070',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2679,(0,4):C.GC_2778,(0,2):C.GC_2777,(0,3):C.GC_2777,(0,0):C.GC_2735,(0,1):C.GC_2776})

V_2071 = Vertex(name = 'V_2071',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2825,(0,4):C.GC_2857,(0,2):C.GC_2856,(0,3):C.GC_2856,(0,0):C.GC_2851,(0,1):C.GC_2855})

V_2072 = Vertex(name = 'V_2072',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1107,(0,4):C.GC_1217,(0,2):C.GC_1216,(0,3):C.GC_1216,(0,0):C.GC_1175,(0,1):C.GC_1215})

V_2073 = Vertex(name = 'V_2073',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1224,(0,4):C.GC_1254,(0,2):C.GC_1253,(0,3):C.GC_1253,(0,0):C.GC_1245,(0,1):C.GC_1252})

V_2074 = Vertex(name = 'V_2074',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1795,(0,4):C.GC_1915,(0,2):C.GC_1914,(0,3):C.GC_1914,(0,0):C.GC_1916,(0,1):C.GC_1913})

V_2075 = Vertex(name = 'V_2075',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1931,(0,4):C.GC_1960,(0,2):C.GC_1959,(0,3):C.GC_1959,(0,0):C.GC_1961,(0,1):C.GC_1958})

V_2076 = Vertex(name = 'V_2076',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2679,(0,4):C.GC_2800,(0,2):C.GC_2799,(0,3):C.GC_2799,(0,0):C.GC_2797,(0,1):C.GC_2798})

V_2077 = Vertex(name = 'V_2077',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2825,(0,4):C.GC_2861,(0,2):C.GC_2860,(0,3):C.GC_2860,(0,0):C.GC_2858,(0,1):C.GC_2859})

V_2078 = Vertex(name = 'V_2078',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1255,(0,4):C.GC_1358,(0,2):C.GC_1357,(0,3):C.GC_1357,(0,0):C.GC_1319,(0,1):C.GC_1356})

V_2079 = Vertex(name = 'V_2079',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1420,(0,2):C.GC_1419,(0,3):C.GC_1419,(0,0):C.GC_1415,(0,1):C.GC_1418})

V_2080 = Vertex(name = 'V_2080',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1968,(0,4):C.GC_2034,(0,2):C.GC_2033,(0,3):C.GC_2033,(0,0):C.GC_2073,(0,1):C.GC_2032})

V_2081 = Vertex(name = 'V_2081',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2121,(0,4):C.GC_2136,(0,2):C.GC_2135,(0,3):C.GC_2135,(0,0):C.GC_2140,(0,1):C.GC_2134})

V_2082 = Vertex(name = 'V_2082',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3026,(0,4):C.GC_3125,(0,2):C.GC_3124,(0,3):C.GC_3124,(0,0):C.GC_3091,(0,1):C.GC_3123})

V_2083 = Vertex(name = 'V_2083',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3188,(0,4):C.GC_3220,(0,2):C.GC_3219,(0,3):C.GC_3219,(0,0):C.GC_3216,(0,1):C.GC_3218})

V_2084 = Vertex(name = 'V_2084',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1255,(0,4):C.GC_1361,(0,2):C.GC_1360,(0,3):C.GC_1360,(0,0):C.GC_1320,(0,1):C.GC_1359})

V_2085 = Vertex(name = 'V_2085',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1423,(0,2):C.GC_1422,(0,3):C.GC_1422,(0,0):C.GC_1416,(0,1):C.GC_1421})

V_2086 = Vertex(name = 'V_2086',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1968,(0,4):C.GC_2037,(0,2):C.GC_2036,(0,3):C.GC_2036,(0,0):C.GC_2074,(0,1):C.GC_2035})

V_2087 = Vertex(name = 'V_2087',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2121,(0,4):C.GC_2139,(0,2):C.GC_2138,(0,3):C.GC_2138,(0,0):C.GC_2141,(0,1):C.GC_2137})

V_2088 = Vertex(name = 'V_2088',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3026,(0,4):C.GC_3128,(0,2):C.GC_3127,(0,3):C.GC_3127,(0,0):C.GC_3092,(0,1):C.GC_3126})

V_2089 = Vertex(name = 'V_2089',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3188,(0,4):C.GC_3223,(0,2):C.GC_3222,(0,3):C.GC_3222,(0,0):C.GC_3217,(0,1):C.GC_3221})

V_2090 = Vertex(name = 'V_2090',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1255,(0,4):C.GC_1383,(0,2):C.GC_1382,(0,3):C.GC_1382,(0,0):C.GC_1333,(0,1):C.GC_1381})

V_2091 = Vertex(name = 'V_2091',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1390,(0,4):C.GC_1426,(0,2):C.GC_1425,(0,3):C.GC_1425,(0,0):C.GC_1417,(0,1):C.GC_1424})

V_2092 = Vertex(name = 'V_2092',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1968,(0,4):C.GC_2101,(0,2):C.GC_2100,(0,3):C.GC_2100,(0,0):C.GC_2102,(0,1):C.GC_2099})

V_2093 = Vertex(name = 'V_2093',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2121,(0,4):C.GC_2153,(0,2):C.GC_2152,(0,3):C.GC_2152,(0,0):C.GC_2154,(0,1):C.GC_2151})

V_2094 = Vertex(name = 'V_2094',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3026,(0,4):C.GC_3161,(0,2):C.GC_3160,(0,3):C.GC_3160,(0,0):C.GC_3158,(0,1):C.GC_3159})

V_2095 = Vertex(name = 'V_2095',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3188,(0,4):C.GC_3227,(0,2):C.GC_3226,(0,3):C.GC_3226,(0,0):C.GC_3224,(0,1):C.GC_3225})

V_2096 = Vertex(name = 'V_2096',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1427,(0,4):C.GC_1535,(0,2):C.GC_1534,(0,3):C.GC_1534,(0,0):C.GC_1485,(0,1):C.GC_1533})

V_2097 = Vertex(name = 'V_2097',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1752,(0,4):C.GC_1788,(0,2):C.GC_1787,(0,3):C.GC_1787,(0,0):C.GC_1783,(0,1):C.GC_1786})

V_2098 = Vertex(name = 'V_2098',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2164,(0,4):C.GC_2243,(0,2):C.GC_2242,(0,3):C.GC_2242,(0,0):C.GC_2240,(0,1):C.GC_2241})

V_2099 = Vertex(name = 'V_2099',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2325,(0,4):C.GC_2485,(0,2):C.GC_2484,(0,3):C.GC_2484,(0,0):C.GC_2482,(0,1):C.GC_2483})

V_2100 = Vertex(name = 'V_2100',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3455,(0,4):C.GC_3565,(0,2):C.GC_3564,(0,3):C.GC_3564,(0,0):C.GC_3514,(0,1):C.GC_3563})

V_2101 = Vertex(name = 'V_2101',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3857,(0,4):C.GC_3893,(0,2):C.GC_3892,(0,3):C.GC_3892,(0,0):C.GC_3889,(0,1):C.GC_3891})

V_2102 = Vertex(name = 'V_2102',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1427,(0,4):C.GC_1538,(0,2):C.GC_1537,(0,3):C.GC_1537,(0,0):C.GC_1486,(0,1):C.GC_1536})

V_2103 = Vertex(name = 'V_2103',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1752,(0,4):C.GC_1791,(0,2):C.GC_1790,(0,3):C.GC_1790,(0,0):C.GC_1784,(0,1):C.GC_1789})

V_2104 = Vertex(name = 'V_2104',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2164,(0,4):C.GC_2247,(0,2):C.GC_2246,(0,3):C.GC_2246,(0,0):C.GC_2244,(0,1):C.GC_2245})

V_2105 = Vertex(name = 'V_2105',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2325,(0,4):C.GC_2498,(0,2):C.GC_2497,(0,3):C.GC_2497,(0,0):C.GC_2495,(0,1):C.GC_2496})

V_2106 = Vertex(name = 'V_2106',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3455,(0,4):C.GC_3568,(0,2):C.GC_3567,(0,3):C.GC_3567,(0,0):C.GC_3515,(0,1):C.GC_3566})

V_2107 = Vertex(name = 'V_2107',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3857,(0,4):C.GC_3896,(0,2):C.GC_3895,(0,3):C.GC_3895,(0,0):C.GC_3890,(0,1):C.GC_3894})

V_2108 = Vertex(name = 'V_2108',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1427,(0,4):C.GC_1555,(0,2):C.GC_1554,(0,3):C.GC_1554,(0,0):C.GC_1505,(0,1):C.GC_1553})

V_2109 = Vertex(name = 'V_2109',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1752,(0,4):C.GC_1794,(0,2):C.GC_1793,(0,3):C.GC_1793,(0,0):C.GC_1785,(0,1):C.GC_1792})

V_2110 = Vertex(name = 'V_2110',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2164,(0,4):C.GC_2299,(0,2):C.GC_2298,(0,3):C.GC_2298,(0,0):C.GC_2296,(0,1):C.GC_2297})

V_2111 = Vertex(name = 'V_2111',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2325,(0,4):C.GC_2559,(0,2):C.GC_2558,(0,3):C.GC_2558,(0,0):C.GC_2556,(0,1):C.GC_2557})

V_2112 = Vertex(name = 'V_2112',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3455,(0,4):C.GC_3590,(0,2):C.GC_3589,(0,3):C.GC_3589,(0,0):C.GC_3587,(0,1):C.GC_3588})

V_2113 = Vertex(name = 'V_2113',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3857,(0,4):C.GC_3912,(0,2):C.GC_3911,(0,3):C.GC_3911,(0,0):C.GC_3909,(0,1):C.GC_3910})

V_2114 = Vertex(name = 'V_2114',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2115 = Vertex(name = 'V_2115',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_516})

V_2116 = Vertex(name = 'V_2116',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_2117 = Vertex(name = 'V_2117',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2617})

V_2118 = Vertex(name = 'V_2118',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2119 = Vertex(name = 'V_2119',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_516})

V_2120 = Vertex(name = 'V_2120',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_2121 = Vertex(name = 'V_2121',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2617})

V_2122 = Vertex(name = 'V_2122',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2123 = Vertex(name = 'V_2123',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_516})

V_2124 = Vertex(name = 'V_2124',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2616})

V_2125 = Vertex(name = 'V_2125',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2617})

V_2126 = Vertex(name = 'V_2126',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2886})

V_2127 = Vertex(name = 'V_2127',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2889})

V_2128 = Vertex(name = 'V_2128',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2886})

V_2129 = Vertex(name = 'V_2129',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2889})

V_2130 = Vertex(name = 'V_2130',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2886})

V_2131 = Vertex(name = 'V_2131',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2889})

V_2132 = Vertex(name = 'V_2132',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2887})

V_2133 = Vertex(name = 'V_2133',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2891})

V_2134 = Vertex(name = 'V_2134',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2887})

V_2135 = Vertex(name = 'V_2135',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2891})

V_2136 = Vertex(name = 'V_2136',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2887})

V_2137 = Vertex(name = 'V_2137',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2891})

V_2138 = Vertex(name = 'V_2138',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3262})

V_2139 = Vertex(name = 'V_2139',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3266})

V_2140 = Vertex(name = 'V_2140',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3262})

V_2141 = Vertex(name = 'V_2141',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3266})

V_2142 = Vertex(name = 'V_2142',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3262})

V_2143 = Vertex(name = 'V_2143',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3266})

V_2144 = Vertex(name = 'V_2144',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2145 = Vertex(name = 'V_2145',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_693})

V_2146 = Vertex(name = 'V_2146',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_2147 = Vertex(name = 'V_2147',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3268})

V_2148 = Vertex(name = 'V_2148',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2149 = Vertex(name = 'V_2149',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_693})

V_2150 = Vertex(name = 'V_2150',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_2151 = Vertex(name = 'V_2151',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3268})

V_2152 = Vertex(name = 'V_2152',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2153 = Vertex(name = 'V_2153',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_693})

V_2154 = Vertex(name = 'V_2154',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3263})

V_2155 = Vertex(name = 'V_2155',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3268})

V_2156 = Vertex(name = 'V_2156',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3264})

V_2157 = Vertex(name = 'V_2157',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3270})

V_2158 = Vertex(name = 'V_2158',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3264})

V_2159 = Vertex(name = 'V_2159',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3270})

V_2160 = Vertex(name = 'V_2160',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3264})

V_2161 = Vertex(name = 'V_2161',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3270})

V_2162 = Vertex(name = 'V_2162',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4019})

V_2163 = Vertex(name = 'V_2163',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4023})

V_2164 = Vertex(name = 'V_2164',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4019})

V_2165 = Vertex(name = 'V_2165',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4023})

V_2166 = Vertex(name = 'V_2166',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4019})

V_2167 = Vertex(name = 'V_2167',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4023})

V_2168 = Vertex(name = 'V_2168',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4020})

V_2169 = Vertex(name = 'V_2169',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4025})

V_2170 = Vertex(name = 'V_2170',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4020})

V_2171 = Vertex(name = 'V_2171',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4025})

V_2172 = Vertex(name = 'V_2172',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4020})

V_2173 = Vertex(name = 'V_2173',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4025})

V_2174 = Vertex(name = 'V_2174',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2175 = Vertex(name = 'V_2175',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_413})

V_2176 = Vertex(name = 'V_2176',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_2177 = Vertex(name = 'V_2177',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4027})

V_2178 = Vertex(name = 'V_2178',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2179 = Vertex(name = 'V_2179',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_413})

V_2180 = Vertex(name = 'V_2180',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_2181 = Vertex(name = 'V_2181',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4027})

V_2182 = Vertex(name = 'V_2182',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_35,(0,0):C.GC_31})

V_2183 = Vertex(name = 'V_2183',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_36,(0,0):C.GC_413})

V_2184 = Vertex(name = 'V_2184',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4021})

V_2185 = Vertex(name = 'V_2185',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4027})

V_2186 = Vertex(name = 'V_2186',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1888,(2,0):C.GC_1891,(1,2):C.GC_1888,(3,2):C.GC_1891,(1,1):C.GC_1888,(3,1):C.GC_1891,(0,3):C.GC_1888,(2,3):C.GC_1891})

V_2187 = Vertex(name = 'V_2187',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2721,(2,0):C.GC_2724,(1,2):C.GC_1889,(3,2):C.GC_1892,(1,1):C.GC_2721,(3,1):C.GC_2724,(0,3):C.GC_1889,(2,3):C.GC_1892})

V_2188 = Vertex(name = 'V_2188',
                particles = [ P.s__tilde__, P.b, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1869,(2,0):C.GC_1872,(1,2):C.GC_1869,(3,2):C.GC_1872,(1,1):C.GC_2267,(3,1):C.GC_2270,(0,3):C.GC_2267,(2,3):C.GC_2270})

V_2189 = Vertex(name = 'V_2189',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2722,(2,0):C.GC_2725,(1,2):C.GC_2722,(3,2):C.GC_2725,(1,1):C.GC_2722,(3,1):C.GC_2725,(0,3):C.GC_2722,(2,3):C.GC_2725})

V_2190 = Vertex(name = 'V_2190',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2738,(2,0):C.GC_2741,(1,2):C.GC_2738,(3,2):C.GC_2741,(1,1):C.GC_3069,(3,1):C.GC_3072,(0,3):C.GC_3069,(2,3):C.GC_3072})

V_2191 = Vertex(name = 'V_2191',
                particles = [ P.d__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1313,(2,0):C.GC_1316,(1,2):C.GC_1313,(3,2):C.GC_1316,(1,1):C.GC_1313,(3,1):C.GC_1316,(0,3):C.GC_1313,(2,3):C.GC_1316})

V_2192 = Vertex(name = 'V_2192',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_3073,(2,0):C.GC_3076,(1,2):C.GC_1315,(3,2):C.GC_1318,(1,1):C.GC_3073,(3,1):C.GC_3076,(0,3):C.GC_1315,(2,3):C.GC_1318})

V_2193 = Vertex(name = 'V_2193',
                particles = [ P.d__tilde__, P.b, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1289,(2,0):C.GC_1292,(1,2):C.GC_1289,(3,2):C.GC_1292,(1,1):C.GC_1487,(3,1):C.GC_1490,(0,3):C.GC_1487,(2,3):C.GC_1490})

V_2194 = Vertex(name = 'V_2194',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_3075,(2,0):C.GC_3078,(1,2):C.GC_3075,(3,2):C.GC_3078,(1,1):C.GC_3075,(3,1):C.GC_3078,(0,3):C.GC_3075,(2,3):C.GC_3078})

V_2195 = Vertex(name = 'V_2195',
                particles = [ P.d__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1473,(2,0):C.GC_1476,(1,2):C.GC_1473,(3,2):C.GC_1476,(1,1):C.GC_1473,(3,1):C.GC_1476,(0,3):C.GC_1473,(2,3):C.GC_1476})

V_2196 = Vertex(name = 'V_2196',
                particles = [ P.s__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2248,(2,0):C.GC_2251,(1,2):C.GC_1474,(3,2):C.GC_1477,(1,1):C.GC_2248,(3,1):C.GC_2251,(0,3):C.GC_1474,(2,3):C.GC_1477})

V_2197 = Vertex(name = 'V_2197',
                particles = [ P.s__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2249,(2,0):C.GC_2252,(1,2):C.GC_2249,(3,2):C.GC_2252,(1,1):C.GC_2249,(3,1):C.GC_2252,(0,3):C.GC_2249,(2,3):C.GC_2252})

V_2198 = Vertex(name = 'V_2198',
                particles = [ P.a, P.a, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_255})

V_2199 = Vertex(name = 'V_2199',
                particles = [ P.g, P.g, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2, L.VVS3, L.VVS4, L.VVS5 ],
                couplings = {(0,0):C.GC_256,(0,2):C.GC_269,(0,1):C.GC_265,(0,3):C.GC_260})

V_2200 = Vertex(name = 'V_2200',
                particles = [ P.a, P.Z, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_259})

V_2201 = Vertex(name = 'V_2201',
                particles = [ P.a, P.Z1, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_259})

V_2202 = Vertex(name = 'V_2202',
                particles = [ P.a, P.Z1, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_273})

V_2203 = Vertex(name = 'V_2203',
                particles = [ P.g, P.g, P.g, P.H1 ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVVS3, L.VVVS4, L.VVVS5, L.VVVS6, L.VVVS7 ],
                couplings = {(0,2):C.GC_261,(0,4):C.GC_270,(0,3):C.GC_266,(0,1):C.GC_263,(0,0):C.GC_257})

V_2204 = Vertex(name = 'V_2204',
                particles = [ P.g, P.g, P.g, P.g, P.H1 ],
                color = [ 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)' ],
                lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS18, L.VVVVS2, L.VVVVS20, L.VVVVS3, L.VVVVS5, L.VVVVS7, L.VVVVS8 ],
                couplings = {(2,5):C.GC_262,(2,8):C.GC_271,(1,4):C.GC_262,(1,10):C.GC_271,(2,6):C.GC_268,(0,11):C.GC_264,(0,12):C.GC_272,(1,7):C.GC_268,(0,3):C.GC_267,(1,2):C.GC_264,(2,1):C.GC_264,(0,9):C.GC_262,(1,13):C.GC_258,(0,0):C.GC_258,(2,14):C.GC_258})

