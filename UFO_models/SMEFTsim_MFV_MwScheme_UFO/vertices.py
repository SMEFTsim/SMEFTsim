# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Thu 7 Jan 2021 11:40:42


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV2, L.VVV3, L.VVV4 ],
             couplings = {(0,2):C.GC_178,(0,0):C.GC_3,(0,1):C.GC_365})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_285})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_292})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_303})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1, L.VVV2, L.VVV4 ],
             couplings = {(0,2):C.GC_55,(0,1):C.GC_119,(0,0):C.GC_288})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_361})

V_7 = Vertex(name = 'V_7',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_362})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_366})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV2, L.VVV4 ],
             couplings = {(0,1):C.GC_15,(0,0):C.GC_7})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
              couplings = {(0,1):C.GC_61,(1,5):C.GC_61,(2,4):C.GC_61,(1,2):C.GC_8,(0,0):C.GC_8,(2,3):C.GC_8})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV2, L.VVVVV4, L.VVVVV5, L.VVVVV6, L.VVVVV7, L.VVVVV8 ],
              couplings = {(24,11):C.GC_64,(21,12):C.GC_63,(18,12):C.GC_64,(15,11):C.GC_63,(28,9):C.GC_64,(22,2):C.GC_64,(9,2):C.GC_63,(3,9):C.GC_63,(29,10):C.GC_64,(16,3):C.GC_64,(10,3):C.GC_63,(0,10):C.GC_63,(26,6):C.GC_63,(20,5):C.GC_63,(4,5):C.GC_64,(1,6):C.GC_64,(25,1):C.GC_64,(6,1):C.GC_63,(19,4):C.GC_64,(7,4):C.GC_63,(23,8):C.GC_63,(17,7):C.GC_63,(5,7):C.GC_64,(2,8):C.GC_64,(27,0):C.GC_64,(12,0):C.GC_63,(13,13):C.GC_64,(11,13):C.GC_63,(14,14):C.GC_63,(8,14):C.GC_64})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV2, L.VVVVVV3, L.VVVVVV4, L.VVVVVV5, L.VVVVVV6, L.VVVVVV7, L.VVVVVV9 ],
              couplings = {(65,10):C.GC_66,(71,12):C.GC_67,(77,12):C.GC_66,(83,10):C.GC_67,(41,8):C.GC_66,(53,2):C.GC_66,(76,2):C.GC_67,(88,8):C.GC_67,(35,9):C.GC_66,(52,5):C.GC_66,(64,5):C.GC_67,(87,9):C.GC_67,(34,4):C.GC_67,(40,3):C.GC_67,(69,3):C.GC_66,(81,4):C.GC_66,(17,9):C.GC_67,(23,4):C.GC_66,(80,4):C.GC_67,(86,9):C.GC_66,(11,8):C.GC_67,(22,3):C.GC_66,(68,3):C.GC_67,(85,8):C.GC_66,(9,2):C.GC_67,(15,5):C.GC_67,(61,5):C.GC_66,(73,2):C.GC_66,(4,10):C.GC_67,(14,5):C.GC_66,(49,5):C.GC_67,(78,10):C.GC_66,(3,12):C.GC_66,(19,3):C.GC_67,(37,3):C.GC_66,(72,12):C.GC_67,(2,12):C.GC_67,(8,2):C.GC_66,(48,2):C.GC_67,(66,12):C.GC_66,(1,10):C.GC_66,(18,4):C.GC_67,(31,4):C.GC_66,(60,10):C.GC_67,(6,8):C.GC_66,(12,9):C.GC_66,(30,9):C.GC_67,(36,8):C.GC_67,(47,14):C.GC_66,(82,14):C.GC_67,(46,6):C.GC_66,(70,6):C.GC_67,(33,7):C.GC_67,(39,1):C.GC_67,(63,1):C.GC_66,(75,7):C.GC_66,(29,7):C.GC_66,(74,7):C.GC_67,(28,1):C.GC_66,(62,1):C.GC_67,(10,14):C.GC_67,(16,6):C.GC_67,(67,6):C.GC_66,(79,14):C.GC_66,(25,1):C.GC_67,(38,1):C.GC_66,(13,6):C.GC_66,(43,6):C.GC_67,(24,7):C.GC_67,(32,7):C.GC_66,(7,14):C.GC_66,(42,14):C.GC_67,(59,0):C.GC_66,(89,0):C.GC_67,(51,11):C.GC_66,(58,11):C.GC_67,(21,11):C.GC_67,(55,11):C.GC_66,(5,0):C.GC_67,(20,11):C.GC_66,(50,11):C.GC_67,(84,0):C.GC_66,(0,0):C.GC_66,(54,0):C.GC_67,(45,13):C.GC_67,(57,13):C.GC_66,(27,13):C.GC_66,(56,13):C.GC_67,(26,13):C.GC_67,(44,13):C.GC_66})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_179,(0,1):C.GC_5})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_294})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_295})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_314})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_368})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6, L.VVVV9 ],
              couplings = {(0,1):C.GC_58,(0,0):C.GC_120})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_394})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_395})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_367})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV6 ],
              couplings = {(0,0):C.GC_370})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV3 ],
              couplings = {(0,0):C.GC_180})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_142,(0,1):C.GC_82})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_307})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_309})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV19 ],
              couplings = {(0,0):C.GC_60})

V_28 = Vertex(name = 'V_28',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV21 ],
              couplings = {(0,0):C.GC_145})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV8 ],
              couplings = {(0,0):C.GC_147})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV3 ],
              couplings = {(0,0):C.GC_143,(0,1):C.GC_84})

V_31 = Vertex(name = 'V_31',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_315})

V_32 = Vertex(name = 'V_32',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_316})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_317})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV3 ],
              couplings = {(0,0):C.GC_369})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV9 ],
              couplings = {(0,0):C.GC_146})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV16 ],
              couplings = {(0,0):C.GC_88})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV17 ],
              couplings = {(0,0):C.GC_90})

V_38 = Vertex(name = 'V_38',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV8 ],
              couplings = {(0,0):C.GC_80})

V_39 = Vertex(name = 'V_39',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV20 ],
              couplings = {(0,0):C.GC_89})

V_40 = Vertex(name = 'V_40',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_9,(0,2):C.GC_17,(0,1):C.GC_18})

V_41 = Vertex(name = 'V_41',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_281})

V_42 = Vertex(name = 'V_42',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_296})

V_43 = Vertex(name = 'V_43',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_297})

V_44 = Vertex(name = 'V_44',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_298})

V_45 = Vertex(name = 'V_45',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_299})

V_46 = Vertex(name = 'V_46',
              particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_16})

V_47 = Vertex(name = 'V_47',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_226,(0,2):C.GC_228,(0,1):C.GC_229})

V_48 = Vertex(name = 'V_48',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_380})

V_49 = Vertex(name = 'V_49',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_381})

V_50 = Vertex(name = 'V_50',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_382})

V_51 = Vertex(name = 'V_51',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_383})

V_52 = Vertex(name = 'V_52',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_384})

V_53 = Vertex(name = 'V_53',
              particles = [ P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_227})

V_54 = Vertex(name = 'V_54',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_49})

V_55 = Vertex(name = 'V_55',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_176})

V_56 = Vertex(name = 'V_56',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_187})

V_57 = Vertex(name = 'V_57',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_189})

V_58 = Vertex(name = 'V_58',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_232})

V_59 = Vertex(name = 'V_59',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_277})

V_60 = Vertex(name = 'V_60',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_280})

V_61 = Vertex(name = 'V_61',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_19})

V_62 = Vertex(name = 'V_62',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4, L.VVS5 ],
              couplings = {(0,0):C.GC_190,(0,2):C.GC_203,(0,1):C.GC_199,(0,3):C.GC_194})

V_63 = Vertex(name = 'V_63',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_230})

V_64 = Vertex(name = 'V_64',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_20,(0,0):C.GC_81})

V_65 = Vertex(name = 'V_65',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_304})

V_66 = Vertex(name = 'V_66',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_305})

V_67 = Vertex(name = 'V_67',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_306})

V_68 = Vertex(name = 'V_68',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_308})

V_69 = Vertex(name = 'V_69',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_231,(0,0):C.GC_242})

V_70 = Vertex(name = 'V_70',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_385})

V_71 = Vertex(name = 'V_71',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_386})

V_72 = Vertex(name = 'V_72',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_387})

V_73 = Vertex(name = 'V_73',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_388})

V_74 = Vertex(name = 'V_74',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_188})

V_75 = Vertex(name = 'V_75',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_174})

V_76 = Vertex(name = 'V_76',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_175})

V_77 = Vertex(name = 'V_77',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_193})

V_78 = Vertex(name = 'V_78',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_393})

V_79 = Vertex(name = 'V_79',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_275})

V_80 = Vertex(name = 'V_80',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_276})

V_81 = Vertex(name = 'V_81',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_50,(0,0):C.GC_83})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_177,(0,0):C.GC_310})

V_83 = Vertex(name = 'V_83',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_186,(0,0):C.GC_311})

V_84 = Vertex(name = 'V_84',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_312})

V_85 = Vertex(name = 'V_85',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_313})

V_86 = Vertex(name = 'V_86',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_233,(0,0):C.GC_243})

V_87 = Vertex(name = 'V_87',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_278,(0,0):C.GC_389})

V_88 = Vertex(name = 'V_88',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_279,(0,0):C.GC_390})

V_89 = Vertex(name = 'V_89',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_391})

V_90 = Vertex(name = 'V_90',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_392})

V_91 = Vertex(name = 'V_91',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3 ],
              couplings = {(0,0):C.GC_62})

V_92 = Vertex(name = 'V_92',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3, L.VVVS4, L.VVVS5, L.VVVS6, L.VVVS7 ],
              couplings = {(0,2):C.GC_195,(0,4):C.GC_204,(0,3):C.GC_200,(0,1):C.GC_197,(0,0):C.GC_191})

V_93 = Vertex(name = 'V_93',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3 ],
              couplings = {(0,0):C.GC_237})

V_94 = Vertex(name = 'V_94',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_65,(0,0):C.GC_65,(2,2):C.GC_65})

V_95 = Vertex(name = 'V_95',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS17, L.VVVVS19, L.VVVVS2, L.VVVVS3, L.VVVVS4, L.VVVVS7, L.VVVVS8 ],
              couplings = {(2,5):C.GC_196,(2,8):C.GC_205,(1,4):C.GC_196,(1,9):C.GC_205,(2,6):C.GC_202,(0,11):C.GC_198,(0,12):C.GC_206,(1,7):C.GC_202,(0,3):C.GC_201,(1,2):C.GC_198,(2,1):C.GC_198,(0,10):C.GC_196,(1,13):C.GC_192,(0,0):C.GC_192,(2,14):C.GC_192})

V_96 = Vertex(name = 'V_96',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS7, L.VVVVS8 ],
              couplings = {(1,1):C.GC_238,(0,0):C.GC_238,(2,2):C.GC_238})

V_97 = Vertex(name = 'V_97',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3 ],
              couplings = {(0,1):C.GC_56,(0,0):C.GC_141})

V_98 = Vertex(name = 'V_98',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3 ],
              couplings = {(0,1):C.GC_234,(0,0):C.GC_273})

V_99 = Vertex(name = 'V_99',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_59})

V_100 = Vertex(name = 'V_100',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_236})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS2, L.VVVSS3 ],
               couplings = {(0,1):C.GC_140,(0,0):C.GC_57})

V_102 = Vertex(name = 'V_102',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS3 ],
               couplings = {(0,1):C.GC_272,(0,0):C.GC_235})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_85})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_244})

V_105 = Vertex(name = 'V_105',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_144})

V_106 = Vertex(name = 'V_106',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS9 ],
               couplings = {(0,0):C.GC_274})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_86})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_245})

V_109 = Vertex(name = 'V_109',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_87})

V_110 = Vertex(name = 'V_110',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_246})

V_111 = Vertex(name = 'V_111',
               particles = [ P.H, P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_72})

V_112 = Vertex(name = 'V_112',
               particles = [ P.H, P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_77})

V_113 = Vertex(name = 'V_113',
               particles = [ P.H, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_78})

V_114 = Vertex(name = 'V_114',
               particles = [ P.H1, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_79})

V_115 = Vertex(name = 'V_115',
               particles = [ P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_239})

V_116 = Vertex(name = 'V_116',
               particles = [ P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_240})

V_117 = Vertex(name = 'V_117',
               particles = [ P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_241})

V_118 = Vertex(name = 'V_118',
               particles = [ P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_69})

V_119 = Vertex(name = 'V_119',
               particles = [ P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_74})

V_120 = Vertex(name = 'V_120',
               particles = [ P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_69})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_99})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_247})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_249})

V_126 = Vertex(name = 'V_126',
               particles = [ P.a, P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_70})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_160})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_166})

V_129 = Vertex(name = 'V_129',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_130 = Vertex(name = 'V_130',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_99})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_103})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W1__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_249})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_251})

V_134 = Vertex(name = 'V_134',
               particles = [ P.a, P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_75})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_166})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_169})

V_137 = Vertex(name = 'V_137',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_96})

V_138 = Vertex(name = 'V_138',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_100})

V_139 = Vertex(name = 'V_139',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_104})

V_140 = Vertex(name = 'V_140',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_141 = Vertex(name = 'V_141',
               particles = [ P.W__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_142 = Vertex(name = 'V_142',
               particles = [ P.W__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_247})

V_143 = Vertex(name = 'V_143',
               particles = [ P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_160})

V_144 = Vertex(name = 'V_144',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_91})

V_145 = Vertex(name = 'V_145',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_95})

V_146 = Vertex(name = 'V_146',
               particles = [ P.W1__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_99})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W1__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_247})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W1__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_249})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_70})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_160})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV2 ],
               couplings = {(0,0):C.GC_166})

V_152 = Vertex(name = 'V_152',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_92})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_96})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_100})

V_155 = Vertex(name = 'V_155',
               particles = [ P.W__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_92})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W1__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_96})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_161})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_167})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_161})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Z, P.Z, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Z, P.Z, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_97})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Z, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_248})

V_163 = Vertex(name = 'V_163',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_94})

V_164 = Vertex(name = 'V_164',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_98})

V_165 = Vertex(name = 'V_165',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_94})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_167})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_170})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_161})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_167})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Z, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_93})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Z, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_97})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Z, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_101})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_248})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_250})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_98})

V_176 = Vertex(name = 'V_176',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_102})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_94})

V_178 = Vertex(name = 'V_178',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_98})

V_179 = Vertex(name = 'V_179',
               particles = [ P.Z1, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_97})

V_180 = Vertex(name = 'V_180',
               particles = [ P.Z1, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_101})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Z1, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_105})

V_182 = Vertex(name = 'V_182',
               particles = [ P.Z1, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_250})

V_183 = Vertex(name = 'V_183',
               particles = [ P.Z1, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS1 ],
               couplings = {(0,0):C.GC_252})

V_184 = Vertex(name = 'V_184',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_102})

V_185 = Vertex(name = 'V_185',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_106})

V_186 = Vertex(name = 'V_186',
               particles = [ P.W__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_98})

V_187 = Vertex(name = 'V_187',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_102})

V_188 = Vertex(name = 'V_188',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_567})

V_189 = Vertex(name = 'V_189',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_575})

V_190 = Vertex(name = 'V_190',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_293})

V_191 = Vertex(name = 'V_191',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_302})

V_192 = Vertex(name = 'V_192',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_365})

V_193 = Vertex(name = 'V_193',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_624})

V_194 = Vertex(name = 'V_194',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_632})

V_195 = Vertex(name = 'V_195',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_293})

V_196 = Vertex(name = 'V_196',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_302})

V_197 = Vertex(name = 'V_197',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_365})

V_198 = Vertex(name = 'V_198',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_4,(0,1):C.GC_895})

V_199 = Vertex(name = 'V_199',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_903})

V_200 = Vertex(name = 'V_200',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_293})

V_201 = Vertex(name = 'V_201',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_302})

V_202 = Vertex(name = 'V_202',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_365})

V_203 = Vertex(name = 'V_203',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_118,(0,3):C.GC_350,(0,2):C.GC_351,(0,4):C.GC_568})

V_204 = Vertex(name = 'V_204',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_352,(0,2):C.GC_574})

V_205 = Vertex(name = 'V_205',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_360})

V_206 = Vertex(name = 'V_206',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_376})

V_207 = Vertex(name = 'V_207',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_379})

V_208 = Vertex(name = 'V_208',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_118,(0,3):C.GC_350,(0,2):C.GC_351,(0,4):C.GC_625})

V_209 = Vertex(name = 'V_209',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_352,(0,2):C.GC_631})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_360})

V_211 = Vertex(name = 'V_211',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_376})

V_212 = Vertex(name = 'V_212',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_379})

V_213 = Vertex(name = 'V_213',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_173,(0,1):C.GC_118,(0,3):C.GC_350,(0,2):C.GC_351,(0,4):C.GC_896})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_289,(0,1):C.GC_352,(0,2):C.GC_902})

V_215 = Vertex(name = 'V_215',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_360})

V_216 = Vertex(name = 'V_216',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_376})

V_217 = Vertex(name = 'V_217',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_379})

V_218 = Vertex(name = 'V_218',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_511})

V_219 = Vertex(name = 'V_219',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_520})

V_220 = Vertex(name = 'V_220',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_290,(0,1):C.GC_2702})

V_221 = Vertex(name = 'V_221',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_300,(0,1):C.GC_2715})

V_222 = Vertex(name = 'V_222',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_363})

V_223 = Vertex(name = 'V_223',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_684})

V_224 = Vertex(name = 'V_224',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_693})

V_225 = Vertex(name = 'V_225',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_290,(0,1):C.GC_3450})

V_226 = Vertex(name = 'V_226',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_300,(0,1):C.GC_3482})

V_227 = Vertex(name = 'V_227',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_363})

V_228 = Vertex(name = 'V_228',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_1,(0,1):C.GC_414})

V_229 = Vertex(name = 'V_229',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_423})

V_230 = Vertex(name = 'V_230',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_290,(0,1):C.GC_4166})

V_231 = Vertex(name = 'V_231',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_300,(0,1):C.GC_4198})

V_232 = Vertex(name = 'V_232',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_363})

V_233 = Vertex(name = 'V_233',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_984})

V_234 = Vertex(name = 'V_234',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_996})

V_235 = Vertex(name = 'V_235',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_291,(0,1):C.GC_3998})

V_236 = Vertex(name = 'V_236',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_301,(0,1):C.GC_4020})

V_237 = Vertex(name = 'V_237',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_238 = Vertex(name = 'V_238',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_453})

V_239 = Vertex(name = 'V_239',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_465})

V_240 = Vertex(name = 'V_240',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_291,(0,1):C.GC_2486})

V_241 = Vertex(name = 'V_241',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_301,(0,1):C.GC_2518})

V_242 = Vertex(name = 'V_242',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_243 = Vertex(name = 'V_243',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_2,(0,1):C.GC_762})

V_244 = Vertex(name = 'V_244',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_774})

V_245 = Vertex(name = 'V_245',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_291,(0,1):C.GC_3845})

V_246 = Vertex(name = 'V_246',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_301,(0,1):C.GC_3877})

V_247 = Vertex(name = 'V_247',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_364})

V_248 = Vertex(name = 'V_248',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_508})

V_249 = Vertex(name = 'V_249',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_2703})

V_250 = Vertex(name = 'V_250',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_681})

V_251 = Vertex(name = 'V_251',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_3453})

V_252 = Vertex(name = 'V_252',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_411})

V_253 = Vertex(name = 'V_253',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_4169})

V_254 = Vertex(name = 'V_254',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_985})

V_255 = Vertex(name = 'V_255',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_4000})

V_256 = Vertex(name = 'V_256',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_454})

V_257 = Vertex(name = 'V_257',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_2489})

V_258 = Vertex(name = 'V_258',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,0):C.GC_6,(0,1):C.GC_763})

V_259 = Vertex(name = 'V_259',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV8 ],
               couplings = {(0,0):C.GC_3848})

V_260 = Vertex(name = 'V_260',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,2):C.GC_987,(0,4):C.GC_510,(0,0):C.GC_1134,(0,1):C.GC_108,(0,3):C.GC_1017})

V_261 = Vertex(name = 'V_261',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_4004,(0,2):C.GC_2705,(0,0):C.GC_318})

V_262 = Vertex(name = 'V_262',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_319})

V_263 = Vertex(name = 'V_263',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_337})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1091})

V_265 = Vertex(name = 'V_265',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_2631,(0,3):C.GC_3053,(0,0):C.GC_109,(0,2):C.GC_1048})

V_266 = Vertex(name = 'V_266',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_320})

V_267 = Vertex(name = 'V_267',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_321})

V_268 = Vertex(name = 'V_268',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_338})

V_269 = Vertex(name = 'V_269',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1092})

V_270 = Vertex(name = 'V_270',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_4003,(0,3):C.GC_2978,(0,0):C.GC_110,(0,2):C.GC_1008})

V_271 = Vertex(name = 'V_271',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_322})

V_272 = Vertex(name = 'V_272',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_323})

V_273 = Vertex(name = 'V_273',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_339})

V_274 = Vertex(name = 'V_274',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1093})

V_275 = Vertex(name = 'V_275',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1665,(0,3):C.GC_3401,(0,0):C.GC_111,(0,2):C.GC_534})

V_276 = Vertex(name = 'V_276',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_324})

V_277 = Vertex(name = 'V_277',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_325})

V_278 = Vertex(name = 'V_278',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_340})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_551})

V_280 = Vertex(name = 'V_280',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_456,(0,3):C.GC_683,(0,0):C.GC_112,(0,2):C.GC_707})

V_281 = Vertex(name = 'V_281',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_2495,(0,2):C.GC_3459,(0,0):C.GC_326})

V_282 = Vertex(name = 'V_282',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_327})

V_283 = Vertex(name = 'V_283',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_341})

V_284 = Vertex(name = 'V_284',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_736})

V_285 = Vertex(name = 'V_285',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_3782,(0,3):C.GC_3378,(0,0):C.GC_113,(0,2):C.GC_477})

V_286 = Vertex(name = 'V_286',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_328})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_329})

V_288 = Vertex(name = 'V_288',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_342})

V_289 = Vertex(name = 'V_289',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_492})

V_290 = Vertex(name = 'V_290',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_1698,(0,3):C.GC_4216,(0,0):C.GC_114,(0,2):C.GC_795})

V_291 = Vertex(name = 'V_291',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_330})

V_292 = Vertex(name = 'V_292',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_331})

V_293 = Vertex(name = 'V_293',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_343})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_853})

V_295 = Vertex(name = 'V_295',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_2570,(0,3):C.GC_4247,(0,0):C.GC_115,(0,2):C.GC_826})

V_296 = Vertex(name = 'V_296',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_332})

V_297 = Vertex(name = 'V_297',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_333})

V_298 = Vertex(name = 'V_298',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_344})

V_299 = Vertex(name = 'V_299',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_854})

V_300 = Vertex(name = 'V_300',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_765,(0,3):C.GC_413,(0,0):C.GC_116,(0,2):C.GC_786})

V_301 = Vertex(name = 'V_301',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_3854,(0,2):C.GC_4175,(0,0):C.GC_334})

V_302 = Vertex(name = 'V_302',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_335})

V_303 = Vertex(name = 'V_303',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_345})

V_304 = Vertex(name = 'V_304',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_855})

V_305 = Vertex(name = 'V_305',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1015,(0,0):C.GC_122})

V_306 = Vertex(name = 'V_306',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1085})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1046,(0,0):C.GC_123})

V_308 = Vertex(name = 'V_308',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1086})

V_309 = Vertex(name = 'V_309',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1006,(0,0):C.GC_124})

V_310 = Vertex(name = 'V_310',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1087})

V_311 = Vertex(name = 'V_311',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_532,(0,0):C.GC_125})

V_312 = Vertex(name = 'V_312',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_549})

V_313 = Vertex(name = 'V_313',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_705,(0,0):C.GC_126})

V_314 = Vertex(name = 'V_314',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_734})

V_315 = Vertex(name = 'V_315',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_475,(0,0):C.GC_127})

V_316 = Vertex(name = 'V_316',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_490})

V_317 = Vertex(name = 'V_317',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_793,(0,0):C.GC_128})

V_318 = Vertex(name = 'V_318',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_847})

V_319 = Vertex(name = 'V_319',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_824,(0,0):C.GC_129})

V_320 = Vertex(name = 'V_320',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_848})

V_321 = Vertex(name = 'V_321',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_784,(0,0):C.GC_130})

V_322 = Vertex(name = 'V_322',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_849})

V_323 = Vertex(name = 'V_323',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_973,(0,3):C.GC_496,(0,2):C.GC_1016,(0,0):C.GC_254})

V_324 = Vertex(name = 'V_324',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_3980,(0,2):C.GC_2692,(0,0):C.GC_1088})

V_325 = Vertex(name = 'V_325',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_2620,(0,3):C.GC_3042,(0,2):C.GC_1047,(0,0):C.GC_255})

V_326 = Vertex(name = 'V_326',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1089})

V_327 = Vertex(name = 'V_327',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_3979,(0,3):C.GC_2967,(0,2):C.GC_1007,(0,0):C.GC_256})

V_328 = Vertex(name = 'V_328',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1090})

V_329 = Vertex(name = 'V_329',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_1654,(0,3):C.GC_3390,(0,2):C.GC_533,(0,0):C.GC_257})

V_330 = Vertex(name = 'V_330',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_550})

V_331 = Vertex(name = 'V_331',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_442,(0,3):C.GC_669,(0,2):C.GC_706,(0,0):C.GC_258})

V_332 = Vertex(name = 'V_332',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_2460,(0,2):C.GC_3424,(0,0):C.GC_735})

V_333 = Vertex(name = 'V_333',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_3771,(0,3):C.GC_3367,(0,2):C.GC_476,(0,0):C.GC_259})

V_334 = Vertex(name = 'V_334',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_491})

V_335 = Vertex(name = 'V_335',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_1687,(0,3):C.GC_4205,(0,2):C.GC_794,(0,0):C.GC_260})

V_336 = Vertex(name = 'V_336',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_850})

V_337 = Vertex(name = 'V_337',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_2559,(0,3):C.GC_4236,(0,2):C.GC_825,(0,0):C.GC_261})

V_338 = Vertex(name = 'V_338',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_851})

V_339 = Vertex(name = 'V_339',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_749,(0,3):C.GC_399,(0,2):C.GC_785,(0,0):C.GC_262})

V_340 = Vertex(name = 'V_340',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_3819,(0,2):C.GC_4140,(0,0):C.GC_852})

V_341 = Vertex(name = 'V_341',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_566,(0,0):C.GC_107})

V_342 = Vertex(name = 'V_342',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_343 = Vertex(name = 'V_343',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_623,(0,0):C.GC_107})

V_344 = Vertex(name = 'V_344',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_345 = Vertex(name = 'V_345',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV9 ],
               couplings = {(0,1):C.GC_894,(0,0):C.GC_107})

V_346 = Vertex(name = 'V_346',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_347 = Vertex(name = 'V_347',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_348 = Vertex(name = 'V_348',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_349 = Vertex(name = 'V_349',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_350 = Vertex(name = 'V_350',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_554,(0,0):C.GC_253})

V_351 = Vertex(name = 'V_351',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_611,(0,0):C.GC_253})

V_352 = Vertex(name = 'V_352',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS5 ],
               couplings = {(0,1):C.GC_882,(0,0):C.GC_253})

V_353 = Vertex(name = 'V_353',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_510,(0,3):C.GC_987,(0,0):C.GC_1171,(0,2):C.GC_1231})

V_354 = Vertex(name = 'V_354',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_2706,(0,2):C.GC_4004,(0,0):C.GC_1175})

V_355 = Vertex(name = 'V_355',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1176})

V_356 = Vertex(name = 'V_356',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1177})

V_357 = Vertex(name = 'V_357',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1279})

V_358 = Vertex(name = 'V_358',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_3015,(0,3):C.GC_2494,(0,0):C.GC_1862,(0,2):C.GC_1899})

V_359 = Vertex(name = 'V_359',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1866})

V_360 = Vertex(name = 'V_360',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1867})

V_361 = Vertex(name = 'V_361',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1868})

V_362 = Vertex(name = 'V_362',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1980})

V_363 = Vertex(name = 'V_363',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_3016,(0,3):C.GC_3852,(0,0):C.GC_2748,(0,2):C.GC_2814})

V_364 = Vertex(name = 'V_364',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2753})

V_365 = Vertex(name = 'V_365',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2754})

V_366 = Vertex(name = 'V_366',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2755})

V_367 = Vertex(name = 'V_367',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2891})

V_368 = Vertex(name = 'V_368',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_3458,(0,3):C.GC_1755,(0,0):C.GC_1320,(0,2):C.GC_1412})

V_369 = Vertex(name = 'V_369',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1324})

V_370 = Vertex(name = 'V_370',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1325})

V_371 = Vertex(name = 'V_371',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1326})

V_372 = Vertex(name = 'V_372',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1452})

V_373 = Vertex(name = 'V_373',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_683,(0,3):C.GC_456,(0,0):C.GC_2036,(0,2):C.GC_2107})

V_374 = Vertex(name = 'V_374',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_3459,(0,2):C.GC_2495,(0,0):C.GC_2040})

V_375 = Vertex(name = 'V_375',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2041})

V_376 = Vertex(name = 'V_376',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2042})

V_377 = Vertex(name = 'V_377',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2174})

V_378 = Vertex(name = 'V_378',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_3460,(0,3):C.GC_3853,(0,0):C.GC_3096,(0,2):C.GC_3194})

V_379 = Vertex(name = 'V_379',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3101})

V_380 = Vertex(name = 'V_380',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3102})

V_381 = Vertex(name = 'V_381',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3103})

V_382 = Vertex(name = 'V_382',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3258})

V_383 = Vertex(name = 'V_383',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_4173,(0,3):C.GC_1756,(0,0):C.GC_1493,(0,2):C.GC_1557})

V_384 = Vertex(name = 'V_384',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1497})

V_385 = Vertex(name = 'V_385',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1498})

V_386 = Vertex(name = 'V_386',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1499})

V_387 = Vertex(name = 'V_387',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1821})

V_388 = Vertex(name = 'V_388',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_4174,(0,3):C.GC_2496,(0,0):C.GC_2233,(0,2):C.GC_2262})

V_389 = Vertex(name = 'V_389',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2237})

V_390 = Vertex(name = 'V_390',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2238})

V_391 = Vertex(name = 'V_391',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2239})

V_392 = Vertex(name = 'V_392',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2372})

V_393 = Vertex(name = 'V_393',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV9 ],
               couplings = {(0,1):C.GC_413,(0,3):C.GC_765,(0,0):C.GC_3526,(0,2):C.GC_3588})

V_394 = Vertex(name = 'V_394',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,1):C.GC_4175,(0,2):C.GC_3854,(0,0):C.GC_3531})

V_395 = Vertex(name = 'V_395',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3532})

V_396 = Vertex(name = 'V_396',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3533})

V_397 = Vertex(name = 'V_397',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3932})

V_398 = Vertex(name = 'V_398',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1229,(0,0):C.GC_1172})

V_399 = Vertex(name = 'V_399',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1277})

V_400 = Vertex(name = 'V_400',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1897,(0,0):C.GC_1863})

V_401 = Vertex(name = 'V_401',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1978})

V_402 = Vertex(name = 'V_402',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2812,(0,0):C.GC_2749})

V_403 = Vertex(name = 'V_403',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2889})

V_404 = Vertex(name = 'V_404',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1410,(0,0):C.GC_1321})

V_405 = Vertex(name = 'V_405',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1450})

V_406 = Vertex(name = 'V_406',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2105,(0,0):C.GC_2037})

V_407 = Vertex(name = 'V_407',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2172})

V_408 = Vertex(name = 'V_408',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3192,(0,0):C.GC_3097})

V_409 = Vertex(name = 'V_409',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3256})

V_410 = Vertex(name = 'V_410',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1555,(0,0):C.GC_1494})

V_411 = Vertex(name = 'V_411',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1819})

V_412 = Vertex(name = 'V_412',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_2260,(0,0):C.GC_2234})

V_413 = Vertex(name = 'V_413',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2370})

V_414 = Vertex(name = 'V_414',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_3586,(0,0):C.GC_3527})

V_415 = Vertex(name = 'V_415',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3930})

V_416 = Vertex(name = 'V_416',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_496,(0,3):C.GC_973,(0,2):C.GC_1230,(0,0):C.GC_1174})

V_417 = Vertex(name = 'V_417',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_2692,(0,2):C.GC_3980,(0,0):C.GC_1278})

V_418 = Vertex(name = 'V_418',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_2993,(0,3):C.GC_2459,(0,2):C.GC_1898,(0,0):C.GC_1865})

V_419 = Vertex(name = 'V_419',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1979})

V_420 = Vertex(name = 'V_420',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_2994,(0,3):C.GC_3817,(0,2):C.GC_2813,(0,0):C.GC_2752})

V_421 = Vertex(name = 'V_421',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2890})

V_422 = Vertex(name = 'V_422',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_3423,(0,3):C.GC_1733,(0,2):C.GC_1411,(0,0):C.GC_1323})

V_423 = Vertex(name = 'V_423',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1451})

V_424 = Vertex(name = 'V_424',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_669,(0,3):C.GC_442,(0,2):C.GC_2106,(0,0):C.GC_2039})

V_425 = Vertex(name = 'V_425',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_3424,(0,2):C.GC_2460,(0,0):C.GC_2173})

V_426 = Vertex(name = 'V_426',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_3425,(0,3):C.GC_3818,(0,2):C.GC_3193,(0,0):C.GC_3100})

V_427 = Vertex(name = 'V_427',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_3257})

V_428 = Vertex(name = 'V_428',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_4138,(0,3):C.GC_1734,(0,2):C.GC_1556,(0,0):C.GC_1496})

V_429 = Vertex(name = 'V_429',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1820})

V_430 = Vertex(name = 'V_430',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_4139,(0,3):C.GC_2461,(0,2):C.GC_2261,(0,0):C.GC_2236})

V_431 = Vertex(name = 'V_431',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_2371})

V_432 = Vertex(name = 'V_432',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS5 ],
               couplings = {(0,1):C.GC_399,(0,3):C.GC_749,(0,2):C.GC_3587,(0,0):C.GC_3530})

V_433 = Vertex(name = 'V_433',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,1):C.GC_4140,(0,2):C.GC_3819,(0,0):C.GC_3931})

V_434 = Vertex(name = 'V_434',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_566,(0,0):C.GC_107})

V_435 = Vertex(name = 'V_435',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_436 = Vertex(name = 'V_436',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_623,(0,0):C.GC_107})

V_437 = Vertex(name = 'V_437',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_438 = Vertex(name = 'V_438',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,1):C.GC_894,(0,0):C.GC_107})

V_439 = Vertex(name = 'V_439',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_336})

V_440 = Vertex(name = 'V_440',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_441 = Vertex(name = 'V_441',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_442 = Vertex(name = 'V_442',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_121})

V_443 = Vertex(name = 'V_443',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_554,(0,0):C.GC_253})

V_444 = Vertex(name = 'V_444',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_611,(0,0):C.GC_253})

V_445 = Vertex(name = 'V_445',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_882,(0,0):C.GC_253})

V_446 = Vertex(name = 'V_446',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_131})

V_447 = Vertex(name = 'V_447',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_541})

V_448 = Vertex(name = 'V_448',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2683})

V_449 = Vertex(name = 'V_449',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2684})

V_450 = Vertex(name = 'V_450',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2952})

V_451 = Vertex(name = 'V_451',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2954})

V_452 = Vertex(name = 'V_452',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2953})

V_453 = Vertex(name = 'V_453',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2955})

V_454 = Vertex(name = 'V_454',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3346})

V_455 = Vertex(name = 'V_455',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3349})

V_456 = Vertex(name = 'V_456',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_131})

V_457 = Vertex(name = 'V_457',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_724})

V_458 = Vertex(name = 'V_458',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3347})

V_459 = Vertex(name = 'V_459',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3350})

V_460 = Vertex(name = 'V_460',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3348})

V_461 = Vertex(name = 'V_461',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3351})

V_462 = Vertex(name = 'V_462',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4111})

V_463 = Vertex(name = 'V_463',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4114})

V_464 = Vertex(name = 'V_464',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4112})

V_465 = Vertex(name = 'V_465',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4115})

V_466 = Vertex(name = 'V_466',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_131})

V_467 = Vertex(name = 'V_467',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_138,(0,1):C.GC_435})

V_468 = Vertex(name = 'V_468',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4113})

V_469 = Vertex(name = 'V_469',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4116})

V_470 = Vertex(name = 'V_470',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_263,(0,2):C.GC_498})

V_471 = Vertex(name = 'V_471',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_270,(0,1):C.GC_542,(0,2):C.GC_506})

V_472 = Vertex(name = 'V_472',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2685,(0,1):C.GC_2693})

V_473 = Vertex(name = 'V_473',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2686,(0,1):C.GC_2700})

V_474 = Vertex(name = 'V_474',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2956,(0,1):C.GC_2995,(0,2):C.GC_3043})

V_475 = Vertex(name = 'V_475',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2958,(0,1):C.GC_3005,(0,2):C.GC_3048})

V_476 = Vertex(name = 'V_476',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2957,(0,1):C.GC_2996,(0,2):C.GC_2968})

V_477 = Vertex(name = 'V_477',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2959,(0,1):C.GC_3006,(0,2):C.GC_2973})

V_478 = Vertex(name = 'V_478',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3352,(0,1):C.GC_3426,(0,2):C.GC_3391})

V_479 = Vertex(name = 'V_479',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3355,(0,1):C.GC_3443,(0,2):C.GC_3396})

V_480 = Vertex(name = 'V_480',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_263,(0,2):C.GC_671})

V_481 = Vertex(name = 'V_481',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_270,(0,1):C.GC_725,(0,2):C.GC_679})

V_482 = Vertex(name = 'V_482',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3353,(0,1):C.GC_3427})

V_483 = Vertex(name = 'V_483',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3356,(0,1):C.GC_3444})

V_484 = Vertex(name = 'V_484',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3354,(0,1):C.GC_3428,(0,2):C.GC_3368})

V_485 = Vertex(name = 'V_485',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3357,(0,1):C.GC_3445,(0,2):C.GC_3373})

V_486 = Vertex(name = 'V_486',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4117,(0,1):C.GC_4141,(0,2):C.GC_4206})

V_487 = Vertex(name = 'V_487',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4120,(0,1):C.GC_4158,(0,2):C.GC_4211})

V_488 = Vertex(name = 'V_488',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4118,(0,1):C.GC_4142,(0,2):C.GC_4237})

V_489 = Vertex(name = 'V_489',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4121,(0,1):C.GC_4159,(0,2):C.GC_4242})

V_490 = Vertex(name = 'V_490',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_263,(0,2):C.GC_401})

V_491 = Vertex(name = 'V_491',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_270,(0,1):C.GC_436,(0,2):C.GC_409})

V_492 = Vertex(name = 'V_492',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_4119,(0,1):C.GC_4143})

V_493 = Vertex(name = 'V_493',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_4122,(0,1):C.GC_4160})

V_494 = Vertex(name = 'V_494',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_118,(0,3):C.GC_347,(0,2):C.GC_346,(0,4):C.GC_512})

V_495 = Vertex(name = 'V_495',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_353,(0,2):C.GC_543,(0,3):C.GC_519})

V_496 = Vertex(name = 'V_496',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_355,(0,2):C.GC_2707})

V_497 = Vertex(name = 'V_497',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_357,(0,2):C.GC_2714})

V_498 = Vertex(name = 'V_498',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_377,(0,1):C.GC_360})

V_499 = Vertex(name = 'V_499',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2687})

V_500 = Vertex(name = 'V_500',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2688})

V_501 = Vertex(name = 'V_501',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2960,(0,1):C.GC_3017,(0,2):C.GC_3054})

V_502 = Vertex(name = 'V_502',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2962,(0,1):C.GC_3027,(0,2):C.GC_3059})

V_503 = Vertex(name = 'V_503',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2961,(0,1):C.GC_3018,(0,2):C.GC_2979})

V_504 = Vertex(name = 'V_504',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2963,(0,1):C.GC_3028,(0,2):C.GC_2984})

V_505 = Vertex(name = 'V_505',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3358,(0,1):C.GC_3461,(0,2):C.GC_3402})

V_506 = Vertex(name = 'V_506',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3361,(0,1):C.GC_3478,(0,2):C.GC_3407})

V_507 = Vertex(name = 'V_507',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_118,(0,3):C.GC_347,(0,2):C.GC_346,(0,4):C.GC_685})

V_508 = Vertex(name = 'V_508',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_353,(0,2):C.GC_726,(0,3):C.GC_692})

V_509 = Vertex(name = 'V_509',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_355,(0,2):C.GC_3462})

V_510 = Vertex(name = 'V_510',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_357,(0,2):C.GC_3479})

V_511 = Vertex(name = 'V_511',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_377,(0,1):C.GC_360})

V_512 = Vertex(name = 'V_512',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3359})

V_513 = Vertex(name = 'V_513',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3362})

V_514 = Vertex(name = 'V_514',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3360,(0,1):C.GC_3463,(0,2):C.GC_3379})

V_515 = Vertex(name = 'V_515',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3363,(0,1):C.GC_3480,(0,2):C.GC_3384})

V_516 = Vertex(name = 'V_516',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4123,(0,1):C.GC_4176,(0,2):C.GC_4217})

V_517 = Vertex(name = 'V_517',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4126,(0,1):C.GC_4193,(0,2):C.GC_4222})

V_518 = Vertex(name = 'V_518',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4124,(0,1):C.GC_4177,(0,2):C.GC_4248})

V_519 = Vertex(name = 'V_519',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4127,(0,1):C.GC_4194,(0,2):C.GC_4253})

V_520 = Vertex(name = 'V_520',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_171,(0,1):C.GC_118,(0,3):C.GC_347,(0,2):C.GC_346,(0,4):C.GC_415})

V_521 = Vertex(name = 'V_521',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_286,(0,1):C.GC_353,(0,2):C.GC_437,(0,3):C.GC_422})

V_522 = Vertex(name = 'V_522',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_355,(0,2):C.GC_4178})

V_523 = Vertex(name = 'V_523',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_374,(0,1):C.GC_357,(0,2):C.GC_4195})

V_524 = Vertex(name = 'V_524',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_377,(0,1):C.GC_360})

V_525 = Vertex(name = 'V_525',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_4125})

V_526 = Vertex(name = 'V_526',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_4128})

V_527 = Vertex(name = 'V_527',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_132})

V_528 = Vertex(name = 'V_528',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_135})

V_529 = Vertex(name = 'V_529',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_132})

V_530 = Vertex(name = 'V_530',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_135})

V_531 = Vertex(name = 'V_531',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_132})

V_532 = Vertex(name = 'V_532',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_135})

V_533 = Vertex(name = 'V_533',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_265,(0,1):C.GC_264,(0,2):C.GC_556})

V_534 = Vertex(name = 'V_534',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_267,(0,1):C.GC_563})

V_535 = Vertex(name = 'V_535',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_265,(0,1):C.GC_264,(0,2):C.GC_613})

V_536 = Vertex(name = 'V_536',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_267,(0,1):C.GC_620})

V_537 = Vertex(name = 'V_537',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_265,(0,1):C.GC_264,(0,2):C.GC_884})

V_538 = Vertex(name = 'V_538',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_267,(0,1):C.GC_891})

V_539 = Vertex(name = 'V_539',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_117,(0,3):C.GC_349,(0,2):C.GC_358,(0,4):C.GC_988})

V_540 = Vertex(name = 'V_540',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_354,(0,2):C.GC_1071,(0,3):C.GC_995})

V_541 = Vertex(name = 'V_541',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_355,(0,2):C.GC_4006})

V_542 = Vertex(name = 'V_542',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_375,(0,1):C.GC_356,(0,2):C.GC_4018})

V_543 = Vertex(name = 'V_543',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_378,(0,1):C.GC_359})

V_544 = Vertex(name = 'V_544',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3763})

V_545 = Vertex(name = 'V_545',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3766})

V_546 = Vertex(name = 'V_546',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2444,(0,1):C.GC_2632,(0,2):C.GC_2497})

V_547 = Vertex(name = 'V_547',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2447,(0,1):C.GC_2637,(0,2):C.GC_2514})

V_548 = Vertex(name = 'V_548',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3760,(0,1):C.GC_4005,(0,2):C.GC_3855})

V_549 = Vertex(name = 'V_549',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3764,(0,1):C.GC_4017,(0,2):C.GC_3872})

V_550 = Vertex(name = 'V_550',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1647,(0,1):C.GC_1666,(0,2):C.GC_1757})

V_551 = Vertex(name = 'V_551',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1649,(0,1):C.GC_1671,(0,2):C.GC_1767})

V_552 = Vertex(name = 'V_552',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_117,(0,3):C.GC_349,(0,2):C.GC_358,(0,4):C.GC_457})

V_553 = Vertex(name = 'V_553',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_354,(0,2):C.GC_486,(0,3):C.GC_464})

V_554 = Vertex(name = 'V_554',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_355,(0,2):C.GC_2498})

V_555 = Vertex(name = 'V_555',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_375,(0,1):C.GC_356,(0,2):C.GC_2515})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_378,(0,1):C.GC_359})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2445})

V_558 = Vertex(name = 'V_558',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2448})

V_559 = Vertex(name = 'V_559',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3761,(0,1):C.GC_3783,(0,2):C.GC_3856})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3765,(0,1):C.GC_3788,(0,2):C.GC_3873})

V_561 = Vertex(name = 'V_561',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1648,(0,1):C.GC_1699,(0,2):C.GC_1758})

V_562 = Vertex(name = 'V_562',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_1650,(0,1):C.GC_1704,(0,2):C.GC_1768})

V_563 = Vertex(name = 'V_563',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2446,(0,1):C.GC_2571,(0,2):C.GC_2499})

V_564 = Vertex(name = 'V_564',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_2449,(0,1):C.GC_2576,(0,2):C.GC_2516})

V_565 = Vertex(name = 'V_565',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_172,(0,1):C.GC_117,(0,3):C.GC_349,(0,2):C.GC_358,(0,4):C.GC_766})

V_566 = Vertex(name = 'V_566',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV8 ],
               couplings = {(0,0):C.GC_287,(0,1):C.GC_354,(0,2):C.GC_835,(0,3):C.GC_773})

V_567 = Vertex(name = 'V_567',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_355,(0,2):C.GC_3857})

V_568 = Vertex(name = 'V_568',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV8 ],
               couplings = {(0,0):C.GC_375,(0,1):C.GC_356,(0,2):C.GC_3874})

V_569 = Vertex(name = 'V_569',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_378,(0,1):C.GC_359})

V_570 = Vertex(name = 'V_570',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3762})

V_571 = Vertex(name = 'V_571',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3767})

V_572 = Vertex(name = 'V_572',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_139})

V_573 = Vertex(name = 'V_573',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_1069})

V_574 = Vertex(name = 'V_574',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3747})

V_575 = Vertex(name = 'V_575',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3750})

V_576 = Vertex(name = 'V_576',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2432})

V_577 = Vertex(name = 'V_577',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2435})

V_578 = Vertex(name = 'V_578',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3744})

V_579 = Vertex(name = 'V_579',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3748})

V_580 = Vertex(name = 'V_580',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1639})

V_581 = Vertex(name = 'V_581',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1641})

V_582 = Vertex(name = 'V_582',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_139})

V_583 = Vertex(name = 'V_583',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_484})

V_584 = Vertex(name = 'V_584',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2433})

V_585 = Vertex(name = 'V_585',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2436})

V_586 = Vertex(name = 'V_586',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3745})

V_587 = Vertex(name = 'V_587',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3749})

V_588 = Vertex(name = 'V_588',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1640})

V_589 = Vertex(name = 'V_589',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1642})

V_590 = Vertex(name = 'V_590',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2434})

V_591 = Vertex(name = 'V_591',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2437})

V_592 = Vertex(name = 'V_592',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_136,(0,1):C.GC_139})

V_593 = Vertex(name = 'V_593',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_137,(0,1):C.GC_833})

V_594 = Vertex(name = 'V_594',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3746})

V_595 = Vertex(name = 'V_595',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_3751})

V_596 = Vertex(name = 'V_596',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_271,(0,2):C.GC_974})

V_597 = Vertex(name = 'V_597',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_269,(0,1):C.GC_1070,(0,2):C.GC_982})

V_598 = Vertex(name = 'V_598',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3755,(0,1):C.GC_3982})

V_599 = Vertex(name = 'V_599',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3758,(0,1):C.GC_3994})

V_600 = Vertex(name = 'V_600',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2438,(0,1):C.GC_2621,(0,2):C.GC_2462})

V_601 = Vertex(name = 'V_601',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2441,(0,1):C.GC_2626,(0,2):C.GC_2479})

V_602 = Vertex(name = 'V_602',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3752,(0,1):C.GC_3981,(0,2):C.GC_3820})

V_603 = Vertex(name = 'V_603',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3756,(0,1):C.GC_3993,(0,2):C.GC_3837})

V_604 = Vertex(name = 'V_604',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1643,(0,1):C.GC_1655,(0,2):C.GC_1735})

V_605 = Vertex(name = 'V_605',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1645,(0,1):C.GC_1660,(0,2):C.GC_1745})

V_606 = Vertex(name = 'V_606',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_271,(0,2):C.GC_443})

V_607 = Vertex(name = 'V_607',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_269,(0,1):C.GC_485,(0,2):C.GC_451})

V_608 = Vertex(name = 'V_608',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2439,(0,1):C.GC_2463})

V_609 = Vertex(name = 'V_609',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_2442,(0,1):C.GC_2480})

V_610 = Vertex(name = 'V_610',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3753,(0,1):C.GC_3772,(0,2):C.GC_3821})

V_611 = Vertex(name = 'V_611',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3757,(0,1):C.GC_3777,(0,2):C.GC_3838})

V_612 = Vertex(name = 'V_612',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1644,(0,1):C.GC_1688,(0,2):C.GC_1736})

V_613 = Vertex(name = 'V_613',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1646,(0,1):C.GC_1693,(0,2):C.GC_1746})

V_614 = Vertex(name = 'V_614',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2440,(0,1):C.GC_2560,(0,2):C.GC_2464})

V_615 = Vertex(name = 'V_615',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2443,(0,1):C.GC_2565,(0,2):C.GC_2481})

V_616 = Vertex(name = 'V_616',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_268,(0,1):C.GC_271,(0,2):C.GC_750})

V_617 = Vertex(name = 'V_617',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_269,(0,1):C.GC_834,(0,2):C.GC_760})

V_618 = Vertex(name = 'V_618',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3754,(0,1):C.GC_3822})

V_619 = Vertex(name = 'V_619',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_3759,(0,1):C.GC_3839})

V_620 = Vertex(name = 'V_620',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_117})

V_621 = Vertex(name = 'V_621',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_348})

V_622 = Vertex(name = 'V_622',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_352})

V_623 = Vertex(name = 'V_623',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_359})

V_624 = Vertex(name = 'V_624',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_117})

V_625 = Vertex(name = 'V_625',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_348})

V_626 = Vertex(name = 'V_626',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_352})

V_627 = Vertex(name = 'V_627',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_359})

V_628 = Vertex(name = 'V_628',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_117})

V_629 = Vertex(name = 'V_629',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_348})

V_630 = Vertex(name = 'V_630',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_352})

V_631 = Vertex(name = 'V_631',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_359})

V_632 = Vertex(name = 'V_632',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_133})

V_633 = Vertex(name = 'V_633',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_134})

V_634 = Vertex(name = 'V_634',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_133})

V_635 = Vertex(name = 'V_635',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_134})

V_636 = Vertex(name = 'V_636',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_133})

V_637 = Vertex(name = 'V_637',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_134})

V_638 = Vertex(name = 'V_638',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_265})

V_639 = Vertex(name = 'V_639',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_266})

V_640 = Vertex(name = 'V_640',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_265})

V_641 = Vertex(name = 'V_641',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_266})

V_642 = Vertex(name = 'V_642',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_265})

V_643 = Vertex(name = 'V_643',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_266})

V_644 = Vertex(name = 'V_644',
               particles = [ P.t__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_68})

V_645 = Vertex(name = 'V_645',
               particles = [ P.t1__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_73})

V_646 = Vertex(name = 'V_646',
               particles = [ P.t1__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_68})

V_647 = Vertex(name = 'V_647',
               particles = [ P.t__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_71})

V_648 = Vertex(name = 'V_648',
               particles = [ P.t1__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_76})

V_649 = Vertex(name = 'V_649',
               particles = [ P.t1__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_71})

V_650 = Vertex(name = 'V_650',
               particles = [ P.d__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_155})

V_651 = Vertex(name = 'V_651',
               particles = [ P.s__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_156})

V_652 = Vertex(name = 'V_652',
               particles = [ P.b__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_157})

V_653 = Vertex(name = 'V_653',
               particles = [ P.d__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_162})

V_654 = Vertex(name = 'V_654',
               particles = [ P.s__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_163})

V_655 = Vertex(name = 'V_655',
               particles = [ P.b__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_164})

V_656 = Vertex(name = 'V_656',
               particles = [ P.d__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_149})

V_657 = Vertex(name = 'V_657',
               particles = [ P.s__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_150})

V_658 = Vertex(name = 'V_658',
               particles = [ P.b__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_151})

V_659 = Vertex(name = 'V_659',
               particles = [ P.d__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_152})

V_660 = Vertex(name = 'V_660',
               particles = [ P.s__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_153})

V_661 = Vertex(name = 'V_661',
               particles = [ P.b__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_154})

V_662 = Vertex(name = 'V_662',
               particles = [ P.d__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_155})

V_663 = Vertex(name = 'V_663',
               particles = [ P.s__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_156})

V_664 = Vertex(name = 'V_664',
               particles = [ P.b__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_157})

V_665 = Vertex(name = 'V_665',
               particles = [ P.e__plus__, P.ve, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_666 = Vertex(name = 'V_666',
               particles = [ P.mu__plus__, P.vm, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_667 = Vertex(name = 'V_667',
               particles = [ P.ta__plus__, P.vt, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_668 = Vertex(name = 'V_668',
               particles = [ P.t1__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2751})

V_669 = Vertex(name = 'V_669',
               particles = [ P.t1__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3099})

V_670 = Vertex(name = 'V_670',
               particles = [ P.t1__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3529})

V_671 = Vertex(name = 'V_671',
               particles = [ P.u__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1173})

V_672 = Vertex(name = 'V_672',
               particles = [ P.c__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1864})

V_673 = Vertex(name = 'V_673',
               particles = [ P.t__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2750})

V_674 = Vertex(name = 'V_674',
               particles = [ P.u__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1322})

V_675 = Vertex(name = 'V_675',
               particles = [ P.c__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2038})

V_676 = Vertex(name = 'V_676',
               particles = [ P.t__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3098})

V_677 = Vertex(name = 'V_677',
               particles = [ P.u__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_1495})

V_678 = Vertex(name = 'V_678',
               particles = [ P.c__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2235})

V_679 = Vertex(name = 'V_679',
               particles = [ P.t__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3528})

V_680 = Vertex(name = 'V_680',
               particles = [ P.ve__tilde__, P.e__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_681 = Vertex(name = 'V_681',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_682 = Vertex(name = 'V_682',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_148})

V_683 = Vertex(name = 'V_683',
               particles = [ P.t1__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_2750})

V_684 = Vertex(name = 'V_684',
               particles = [ P.t1__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3098})

V_685 = Vertex(name = 'V_685',
               particles = [ P.t1__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_3528})

V_686 = Vertex(name = 'V_686',
               particles = [ P.t__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_158})

V_687 = Vertex(name = 'V_687',
               particles = [ P.t1__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_165})

V_688 = Vertex(name = 'V_688',
               particles = [ P.t1__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_158})

V_689 = Vertex(name = 'V_689',
               particles = [ P.d__tilde__, P.d, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_181,(0,1):C.GC_159})

V_690 = Vertex(name = 'V_690',
               particles = [ P.s__tilde__, P.s, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_181,(0,1):C.GC_159})

V_691 = Vertex(name = 'V_691',
               particles = [ P.b__tilde__, P.b, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_181,(0,1):C.GC_159})

V_692 = Vertex(name = 'V_692',
               particles = [ P.e__plus__, P.e__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_183,(0,1):C.GC_159})

V_693 = Vertex(name = 'V_693',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_183,(0,1):C.GC_159})

V_694 = Vertex(name = 'V_694',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_183,(0,1):C.GC_159})

V_695 = Vertex(name = 'V_695',
               particles = [ P.t__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_165})

V_696 = Vertex(name = 'V_696',
               particles = [ P.t1__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_185,(0,1):C.GC_168})

V_697 = Vertex(name = 'V_697',
               particles = [ P.t1__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_165})

V_698 = Vertex(name = 'V_698',
               particles = [ P.u__tilde__, P.u, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_158})

V_699 = Vertex(name = 'V_699',
               particles = [ P.c__tilde__, P.c, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_158})

V_700 = Vertex(name = 'V_700',
               particles = [ P.t__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_158})

V_701 = Vertex(name = 'V_701',
               particles = [ P.ve__tilde__, P.ve, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_158})

V_702 = Vertex(name = 'V_702',
               particles = [ P.vm__tilde__, P.vm, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_158})

V_703 = Vertex(name = 'V_703',
               particles = [ P.vt__tilde__, P.vt, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_158})

V_704 = Vertex(name = 'V_704',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_493})

V_705 = Vertex(name = 'V_705',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_521})

V_706 = Vertex(name = 'V_706',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_522})

V_707 = Vertex(name = 'V_707',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_523})

V_708 = Vertex(name = 'V_708',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_524})

V_709 = Vertex(name = 'V_709',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_525})

V_710 = Vertex(name = 'V_710',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2716})

V_711 = Vertex(name = 'V_711',
               particles = [ P.s__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3031,(0,1):C.GC_3061})

V_712 = Vertex(name = 'V_712',
               particles = [ P.b__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3032,(0,1):C.GC_2986})

V_713 = Vertex(name = 'V_713',
               particles = [ P.d__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3484,(0,1):C.GC_3409})

V_714 = Vertex(name = 'V_714',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_666})

V_715 = Vertex(name = 'V_715',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_694})

V_716 = Vertex(name = 'V_716',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_695})

V_717 = Vertex(name = 'V_717',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_696})

V_718 = Vertex(name = 'V_718',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_697})

V_719 = Vertex(name = 'V_719',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_698})

V_720 = Vertex(name = 'V_720',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_3485})

V_721 = Vertex(name = 'V_721',
               particles = [ P.b__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3486,(0,1):C.GC_3386})

V_722 = Vertex(name = 'V_722',
               particles = [ P.d__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_4199,(0,1):C.GC_4224})

V_723 = Vertex(name = 'V_723',
               particles = [ P.s__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_4200,(0,1):C.GC_4255})

V_724 = Vertex(name = 'V_724',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_396})

V_725 = Vertex(name = 'V_725',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_424})

V_726 = Vertex(name = 'V_726',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_425})

V_727 = Vertex(name = 'V_727',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_426})

V_728 = Vertex(name = 'V_728',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_427})

V_729 = Vertex(name = 'V_729',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_428})

V_730 = Vertex(name = 'V_730',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_4201})

V_731 = Vertex(name = 'V_731',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_495})

V_732 = Vertex(name = 'V_732',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_2691})

V_733 = Vertex(name = 'V_733',
               particles = [ P.s__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2991,(0,1):C.GC_3041})

V_734 = Vertex(name = 'V_734',
               particles = [ P.b__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2992,(0,1):C.GC_2966})

V_735 = Vertex(name = 'V_735',
               particles = [ P.d__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3420,(0,1):C.GC_3389})

V_736 = Vertex(name = 'V_736',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_668})

V_737 = Vertex(name = 'V_737',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3421})

V_738 = Vertex(name = 'V_738',
               particles = [ P.b__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3422,(0,1):C.GC_3366})

V_739 = Vertex(name = 'V_739',
               particles = [ P.d__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_4135,(0,1):C.GC_4204})

V_740 = Vertex(name = 'V_740',
               particles = [ P.s__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_4136,(0,1):C.GC_4235})

V_741 = Vertex(name = 'V_741',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_398})

V_742 = Vertex(name = 'V_742',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_4137})

V_743 = Vertex(name = 'V_743',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_509})

V_744 = Vertex(name = 'V_744',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_2704})

V_745 = Vertex(name = 'V_745',
               particles = [ P.s__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3013,(0,1):C.GC_3052})

V_746 = Vertex(name = 'V_746',
               particles = [ P.b__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3014,(0,1):C.GC_2977})

V_747 = Vertex(name = 'V_747',
               particles = [ P.d__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3455,(0,1):C.GC_3400})

V_748 = Vertex(name = 'V_748',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_682})

V_749 = Vertex(name = 'V_749',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_3456})

V_750 = Vertex(name = 'V_750',
               particles = [ P.b__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3457,(0,1):C.GC_3377})

V_751 = Vertex(name = 'V_751',
               particles = [ P.d__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_4170,(0,1):C.GC_4215})

V_752 = Vertex(name = 'V_752',
               particles = [ P.s__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_4171,(0,1):C.GC_4246})

V_753 = Vertex(name = 'V_753',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_412})

V_754 = Vertex(name = 'V_754',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_4172})

V_755 = Vertex(name = 'V_755',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_552})

V_756 = Vertex(name = 'V_756',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_576})

V_757 = Vertex(name = 'V_757',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_577})

V_758 = Vertex(name = 'V_758',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_578})

V_759 = Vertex(name = 'V_759',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_579})

V_760 = Vertex(name = 'V_760',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_580})

V_761 = Vertex(name = 'V_761',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_609})

V_762 = Vertex(name = 'V_762',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_633})

V_763 = Vertex(name = 'V_763',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_634})

V_764 = Vertex(name = 'V_764',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_635})

V_765 = Vertex(name = 'V_765',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_636})

V_766 = Vertex(name = 'V_766',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_637})

V_767 = Vertex(name = 'V_767',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_880})

V_768 = Vertex(name = 'V_768',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_904})

V_769 = Vertex(name = 'V_769',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_905})

V_770 = Vertex(name = 'V_770',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_906})

V_771 = Vertex(name = 'V_771',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_907})

V_772 = Vertex(name = 'V_772',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_908})

V_773 = Vertex(name = 'V_773',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_553})

V_774 = Vertex(name = 'V_774',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_610})

V_775 = Vertex(name = 'V_775',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_881})

V_776 = Vertex(name = 'V_776',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_565})

V_777 = Vertex(name = 'V_777',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_622})

V_778 = Vertex(name = 'V_778',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_893})

V_779 = Vertex(name = 'V_779',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_969})

V_780 = Vertex(name = 'V_780',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_997})

V_781 = Vertex(name = 'V_781',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_998})

V_782 = Vertex(name = 'V_782',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_999})

V_783 = Vertex(name = 'V_783',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1000})

V_784 = Vertex(name = 'V_784',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_1001})

V_785 = Vertex(name = 'V_785',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_4022})

V_786 = Vertex(name = 'V_786',
               particles = [ P.c__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2639,(0,1):C.GC_2520})

V_787 = Vertex(name = 'V_787',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_4021,(0,1):C.GC_3878})

V_788 = Vertex(name = 'V_788',
               particles = [ P.u__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_1673,(0,1):C.GC_1771})

V_789 = Vertex(name = 'V_789',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_438})

V_790 = Vertex(name = 'V_790',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_466})

V_791 = Vertex(name = 'V_791',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_467})

V_792 = Vertex(name = 'V_792',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_468})

V_793 = Vertex(name = 'V_793',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_469})

V_794 = Vertex(name = 'V_794',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_470})

V_795 = Vertex(name = 'V_795',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_2521})

V_796 = Vertex(name = 'V_796',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_3790,(0,1):C.GC_3879})

V_797 = Vertex(name = 'V_797',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_1706,(0,1):C.GC_1772})

V_798 = Vertex(name = 'V_798',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2, L.FFS3 ],
               couplings = {(0,0):C.GC_2578,(0,1):C.GC_2522})

V_799 = Vertex(name = 'V_799',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_745})

V_800 = Vertex(name = 'V_800',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_775})

V_801 = Vertex(name = 'V_801',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_776})

V_802 = Vertex(name = 'V_802',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_777})

V_803 = Vertex(name = 'V_803',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_778})

V_804 = Vertex(name = 'V_804',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_779})

V_805 = Vertex(name = 'V_805',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_3880})

V_806 = Vertex(name = 'V_806',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_972})

V_807 = Vertex(name = 'V_807',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3978})

V_808 = Vertex(name = 'V_808',
               particles = [ P.c__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2619,(0,1):C.GC_2456})

V_809 = Vertex(name = 'V_809',
               particles = [ P.t__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3977,(0,1):C.GC_3814})

V_810 = Vertex(name = 'V_810',
               particles = [ P.u__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_1653,(0,1):C.GC_1731})

V_811 = Vertex(name = 'V_811',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_441})

V_812 = Vertex(name = 'V_812',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_2457})

V_813 = Vertex(name = 'V_813',
               particles = [ P.t__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_3770,(0,1):C.GC_3815})

V_814 = Vertex(name = 'V_814',
               particles = [ P.u__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_1686,(0,1):C.GC_1732})

V_815 = Vertex(name = 'V_815',
               particles = [ P.c__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS2, L.FFSSS3 ],
               couplings = {(0,0):C.GC_2558,(0,1):C.GC_2458})

V_816 = Vertex(name = 'V_816',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_748})

V_817 = Vertex(name = 'V_817',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1 ],
               couplings = {(0,0):C.GC_3816})

V_818 = Vertex(name = 'V_818',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_986})

V_819 = Vertex(name = 'V_819',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_4002})

V_820 = Vertex(name = 'V_820',
               particles = [ P.c__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2630,(0,1):C.GC_2491})

V_821 = Vertex(name = 'V_821',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_4001,(0,1):C.GC_3849})

V_822 = Vertex(name = 'V_822',
               particles = [ P.u__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_1664,(0,1):C.GC_1753})

V_823 = Vertex(name = 'V_823',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_455})

V_824 = Vertex(name = 'V_824',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_2492})

V_825 = Vertex(name = 'V_825',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_3781,(0,1):C.GC_3850})

V_826 = Vertex(name = 'V_826',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_1697,(0,1):C.GC_1754})

V_827 = Vertex(name = 'V_827',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_2569,(0,1):C.GC_2493})

V_828 = Vertex(name = 'V_828',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_764})

V_829 = Vertex(name = 'V_829',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_3851})

V_830 = Vertex(name = 'V_830',
               particles = [ P.d__tilde__, P.d, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_502})

V_831 = Vertex(name = 'V_831',
               particles = [ P.s__tilde__, P.s, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_675})

V_832 = Vertex(name = 'V_832',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_405})

V_833 = Vertex(name = 'V_833',
               particles = [ P.e__plus__, P.e__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_559})

V_834 = Vertex(name = 'V_834',
               particles = [ P.mu__plus__, P.mu__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_616})

V_835 = Vertex(name = 'V_835',
               particles = [ P.ta__plus__, P.ta__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_887})

V_836 = Vertex(name = 'V_836',
               particles = [ P.t__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_754})

V_837 = Vertex(name = 'V_837',
               particles = [ P.t__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_755})

V_838 = Vertex(name = 'V_838',
               particles = [ P.t1__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_755})

V_839 = Vertex(name = 'V_839',
               particles = [ P.t1__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_756})

V_840 = Vertex(name = 'V_840',
               particles = [ P.t1__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_754})

V_841 = Vertex(name = 'V_841',
               particles = [ P.t1__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_755})

V_842 = Vertex(name = 'V_842',
               particles = [ P.u__tilde__, P.u, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_978})

V_843 = Vertex(name = 'V_843',
               particles = [ P.c__tilde__, P.c, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_447})

V_844 = Vertex(name = 'V_844',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               couplings = {(0,0):C.GC_754})

V_845 = Vertex(name = 'V_845',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_497})

V_846 = Vertex(name = 'V_846',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_507})

V_847 = Vertex(name = 'V_847',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2689})

V_848 = Vertex(name = 'V_848',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2701})

V_849 = Vertex(name = 'V_849',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2987,(0,1):C.GC_3039})

V_850 = Vertex(name = 'V_850',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3007,(0,1):C.GC_3049})

V_851 = Vertex(name = 'V_851',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2988,(0,1):C.GC_2964})

V_852 = Vertex(name = 'V_852',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3008,(0,1):C.GC_2974})

V_853 = Vertex(name = 'V_853',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3414,(0,1):C.GC_3387})

V_854 = Vertex(name = 'V_854',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3446,(0,1):C.GC_3397})

V_855 = Vertex(name = 'V_855',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_670})

V_856 = Vertex(name = 'V_856',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_680})

V_857 = Vertex(name = 'V_857',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3415})

V_858 = Vertex(name = 'V_858',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3447})

V_859 = Vertex(name = 'V_859',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3416,(0,1):C.GC_3364})

V_860 = Vertex(name = 'V_860',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3448,(0,1):C.GC_3374})

V_861 = Vertex(name = 'V_861',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4129,(0,1):C.GC_4202})

V_862 = Vertex(name = 'V_862',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4161,(0,1):C.GC_4212})

V_863 = Vertex(name = 'V_863',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4130,(0,1):C.GC_4233})

V_864 = Vertex(name = 'V_864',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4162,(0,1):C.GC_4243})

V_865 = Vertex(name = 'V_865',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_400})

V_866 = Vertex(name = 'V_866',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_410})

V_867 = Vertex(name = 'V_867',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4131})

V_868 = Vertex(name = 'V_868',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4163})

V_869 = Vertex(name = 'V_869',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3009,(0,1):C.GC_3050})

V_870 = Vertex(name = 'V_870',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3029,(0,1):C.GC_3060})

V_871 = Vertex(name = 'V_871',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3010,(0,1):C.GC_2975})

V_872 = Vertex(name = 'V_872',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3030,(0,1):C.GC_2985})

V_873 = Vertex(name = 'V_873',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3449,(0,1):C.GC_3398})

V_874 = Vertex(name = 'V_874',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3481,(0,1):C.GC_3408})

V_875 = Vertex(name = 'V_875',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3451,(0,1):C.GC_3375})

V_876 = Vertex(name = 'V_876',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3483,(0,1):C.GC_3385})

V_877 = Vertex(name = 'V_877',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4164,(0,1):C.GC_4213})

V_878 = Vertex(name = 'V_878',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4196,(0,1):C.GC_4223})

V_879 = Vertex(name = 'V_879',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4165,(0,1):C.GC_4244})

V_880 = Vertex(name = 'V_880',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4197,(0,1):C.GC_4254})

V_881 = Vertex(name = 'V_881',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_494})

V_882 = Vertex(name = 'V_882',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_2690})

V_883 = Vertex(name = 'V_883',
               particles = [ P.s__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2989,(0,1):C.GC_3040})

V_884 = Vertex(name = 'V_884',
               particles = [ P.b__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2990,(0,1):C.GC_2965})

V_885 = Vertex(name = 'V_885',
               particles = [ P.d__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3417,(0,1):C.GC_3388})

V_886 = Vertex(name = 'V_886',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_667})

V_887 = Vertex(name = 'V_887',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3418})

V_888 = Vertex(name = 'V_888',
               particles = [ P.b__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3419,(0,1):C.GC_3365})

V_889 = Vertex(name = 'V_889',
               particles = [ P.d__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4132,(0,1):C.GC_4203})

V_890 = Vertex(name = 'V_890',
               particles = [ P.s__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_4133,(0,1):C.GC_4234})

V_891 = Vertex(name = 'V_891',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_397})

V_892 = Vertex(name = 'V_892',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_4134})

V_893 = Vertex(name = 'V_893',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3011,(0,1):C.GC_3051})

V_894 = Vertex(name = 'V_894',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3012,(0,1):C.GC_2976})

V_895 = Vertex(name = 'V_895',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3452,(0,1):C.GC_3399})

V_896 = Vertex(name = 'V_896',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_3454,(0,1):C.GC_3376})

V_897 = Vertex(name = 'V_897',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4167,(0,1):C.GC_4214})

V_898 = Vertex(name = 'V_898',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_4168,(0,1):C.GC_4245})

V_899 = Vertex(name = 'V_899',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_501})

V_900 = Vertex(name = 'V_900',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_2696})

V_901 = Vertex(name = 'V_901',
               particles = [ P.s__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2999,(0,1):C.GC_3045})

V_902 = Vertex(name = 'V_902',
               particles = [ P.b__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3000,(0,1):C.GC_2970})

V_903 = Vertex(name = 'V_903',
               particles = [ P.d__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3433,(0,1):C.GC_3393})

V_904 = Vertex(name = 'V_904',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_674})

V_905 = Vertex(name = 'V_905',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_3434})

V_906 = Vertex(name = 'V_906',
               particles = [ P.b__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3435,(0,1):C.GC_3370})

V_907 = Vertex(name = 'V_907',
               particles = [ P.d__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4148,(0,1):C.GC_4208})

V_908 = Vertex(name = 'V_908',
               particles = [ P.s__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4149,(0,1):C.GC_4239})

V_909 = Vertex(name = 'V_909',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_404})

V_910 = Vertex(name = 'V_910',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_4150})

V_911 = Vertex(name = 'V_911',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_515})

V_912 = Vertex(name = 'V_912',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_2710})

V_913 = Vertex(name = 'V_913',
               particles = [ P.s__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3021,(0,1):C.GC_3056})

V_914 = Vertex(name = 'V_914',
               particles = [ P.b__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3022,(0,1):C.GC_2981})

V_915 = Vertex(name = 'V_915',
               particles = [ P.d__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3468,(0,1):C.GC_3404})

V_916 = Vertex(name = 'V_916',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_688})

V_917 = Vertex(name = 'V_917',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_3469})

V_918 = Vertex(name = 'V_918',
               particles = [ P.b__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3470,(0,1):C.GC_3381})

V_919 = Vertex(name = 'V_919',
               particles = [ P.d__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4183,(0,1):C.GC_4219})

V_920 = Vertex(name = 'V_920',
               particles = [ P.s__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4184,(0,1):C.GC_4250})

V_921 = Vertex(name = 'V_921',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_418})

V_922 = Vertex(name = 'V_922',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_4185})

V_923 = Vertex(name = 'V_923',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_500,(0,1):C.GC_976})

V_924 = Vertex(name = 'V_924',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2695,(0,1):C.GC_3985})

V_925 = Vertex(name = 'V_925',
               particles = [ P.c__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2997,(0,1):C.GC_2465})

V_926 = Vertex(name = 'V_926',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_2998,(0,1):C.GC_3823})

V_927 = Vertex(name = 'V_927',
               particles = [ P.u__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3429,(0,1):C.GC_1737})

V_928 = Vertex(name = 'V_928',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_673,(0,1):C.GC_445})

V_929 = Vertex(name = 'V_929',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3430,(0,1):C.GC_2466})

V_930 = Vertex(name = 'V_930',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3432,(0,1):C.GC_3824})

V_931 = Vertex(name = 'V_931',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4144,(0,1):C.GC_1738})

V_932 = Vertex(name = 'V_932',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4145,(0,1):C.GC_2468})

V_933 = Vertex(name = 'V_933',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_403,(0,1):C.GC_752})

V_934 = Vertex(name = 'V_934',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4146,(0,1):C.GC_3825})

V_935 = Vertex(name = 'V_935',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_990})

V_936 = Vertex(name = 'V_936',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_2709,(0,1):C.GC_4009})

V_937 = Vertex(name = 'V_937',
               particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3019,(0,1):C.GC_2500})

V_938 = Vertex(name = 'V_938',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3020,(0,1):C.GC_3858})

V_939 = Vertex(name = 'V_939',
               particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3464,(0,1):C.GC_1759})

V_940 = Vertex(name = 'V_940',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_687,(0,1):C.GC_459})

V_941 = Vertex(name = 'V_941',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3465,(0,1):C.GC_2501})

V_942 = Vertex(name = 'V_942',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3467,(0,1):C.GC_3859})

V_943 = Vertex(name = 'V_943',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4179,(0,1):C.GC_1760})

V_944 = Vertex(name = 'V_944',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4180,(0,1):C.GC_2503})

V_945 = Vertex(name = 'V_945',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_417,(0,1):C.GC_768})

V_946 = Vertex(name = 'V_946',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4181,(0,1):C.GC_3860})

V_947 = Vertex(name = 'V_947',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_503})

V_948 = Vertex(name = 'V_948',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_2697})

V_949 = Vertex(name = 'V_949',
               particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3001,(0,1):C.GC_3046})

V_950 = Vertex(name = 'V_950',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3002,(0,1):C.GC_2971})

V_951 = Vertex(name = 'V_951',
               particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3436,(0,1):C.GC_3394})

V_952 = Vertex(name = 'V_952',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_676})

V_953 = Vertex(name = 'V_953',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_3437})

V_954 = Vertex(name = 'V_954',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_3438,(0,1):C.GC_3371})

V_955 = Vertex(name = 'V_955',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4151,(0,1):C.GC_4209})

V_956 = Vertex(name = 'V_956',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,0):C.GC_4152,(0,1):C.GC_4240})

V_957 = Vertex(name = 'V_957',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_406})

V_958 = Vertex(name = 'V_958',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_4153})

V_959 = Vertex(name = 'V_959',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_516})

V_960 = Vertex(name = 'V_960',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_2711})

V_961 = Vertex(name = 'V_961',
               particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3, L.FFVV5 ],
               couplings = {(0,0):C.GC_3023,(0,1):C.GC_3057,(0,2):C.GC_1926})

V_962 = Vertex(name = 'V_962',
               particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3024,(0,1):C.GC_2982})

V_963 = Vertex(name = 'V_963',
               particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3471,(0,1):C.GC_3405})

V_964 = Vertex(name = 'V_964',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_689})

V_965 = Vertex(name = 'V_965',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_3472})

V_966 = Vertex(name = 'V_966',
               particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_3473,(0,1):C.GC_3382})

V_967 = Vertex(name = 'V_967',
               particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4186,(0,1):C.GC_4220})

V_968 = Vertex(name = 'V_968',
               particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV4 ],
               couplings = {(0,0):C.GC_4187,(0,1):C.GC_4251})

V_969 = Vertex(name = 'V_969',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_419})

V_970 = Vertex(name = 'V_970',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_4188})

V_971 = Vertex(name = 'V_971',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_555})

V_972 = Vertex(name = 'V_972',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_564})

V_973 = Vertex(name = 'V_973',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_612})

V_974 = Vertex(name = 'V_974',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_621})

V_975 = Vertex(name = 'V_975',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_883})

V_976 = Vertex(name = 'V_976',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_892})

V_977 = Vertex(name = 'V_977',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_558})

V_978 = Vertex(name = 'V_978',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_615})

V_979 = Vertex(name = 'V_979',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_886})

V_980 = Vertex(name = 'V_980',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_570})

V_981 = Vertex(name = 'V_981',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_627})

V_982 = Vertex(name = 'V_982',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_898})

V_983 = Vertex(name = 'V_983',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_560})

V_984 = Vertex(name = 'V_984',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_617})

V_985 = Vertex(name = 'V_985',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_888})

V_986 = Vertex(name = 'V_986',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_571})

V_987 = Vertex(name = 'V_987',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_628})

V_988 = Vertex(name = 'V_988',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_899})

V_989 = Vertex(name = 'V_989',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_970})

V_990 = Vertex(name = 'V_990',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_983})

V_991 = Vertex(name = 'V_991',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3974})

V_992 = Vertex(name = 'V_992',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_3996})

V_993 = Vertex(name = 'V_993',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2617,(0,1):C.GC_2450})

V_994 = Vertex(name = 'V_994',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_2627,(0,1):C.GC_2482})

V_995 = Vertex(name = 'V_995',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3973,(0,1):C.GC_3808})

V_996 = Vertex(name = 'V_996',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_3995,(0,1):C.GC_3840})

V_997 = Vertex(name = 'V_997',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1651,(0,1):C.GC_1727})

V_998 = Vertex(name = 'V_998',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS5 ],
               couplings = {(0,0):C.GC_1661,(0,1):C.GC_1747})

V_999 = Vertex(name = 'V_999',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_439})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_452})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_2451})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.c__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_2483})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.t__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_3768,(0,1):C.GC_3809})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.t__tilde__, P.c, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_3778,(0,1):C.GC_3841})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.u__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1684,(0,1):C.GC_1728})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.u__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1694,(0,1):C.GC_1748})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.c__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5, L.FFVS6 ],
                couplings = {(0,0):C.GC_2556,(0,1):C.GC_2452,(0,2):C.GC_2263})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.c__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2566,(0,1):C.GC_2484})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_746})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_761})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_3810})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.t__tilde__, P.t, P.a, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_3842})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.c__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2628,(0,1):C.GC_2485})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.c__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2638,(0,1):C.GC_2517})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.t__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_3997,(0,1):C.GC_3843})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.t__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_4019,(0,1):C.GC_3875})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.u__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1662,(0,1):C.GC_1749})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.u__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1672,(0,1):C.GC_1769})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.t__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_3779,(0,1):C.GC_3844})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.t__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_3789,(0,1):C.GC_3876})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.u__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1695,(0,1):C.GC_1750})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.u__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1705,(0,1):C.GC_1770})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.c__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2567,(0,1):C.GC_2487})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.c__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2577,(0,1):C.GC_2519})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.u__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_971})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.u__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_3976})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.c__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2618,(0,1):C.GC_2453})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.t__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_3975,(0,1):C.GC_3811})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.u__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1652,(0,1):C.GC_1729})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.c__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_440})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.c__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_2454})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.t__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_3769,(0,1):C.GC_3812})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.u__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_1685,(0,1):C.GC_1730})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.c__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS2, L.FFVS5 ],
                couplings = {(0,0):C.GC_2557,(0,1):C.GC_2455})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.t__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_747})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.t__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4 ],
                couplings = {(0,0):C.GC_3813})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.c__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2629,(0,1):C.GC_2488})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.t__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_3999,(0,1):C.GC_3846})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.u__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1663,(0,1):C.GC_1751})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.t__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_3780,(0,1):C.GC_3847})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.u__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_1696,(0,1):C.GC_1752})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.c__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV3, L.FFV9 ],
                couplings = {(0,0):C.GC_2568,(0,1):C.GC_2490})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_977})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3987})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.c__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2623,(0,1):C.GC_2469})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.t__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3986,(0,1):C.GC_3827})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.u__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1657,(0,1):C.GC_1739})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_446})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_2470})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.t__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3774,(0,1):C.GC_3828})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.u__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1690,(0,1):C.GC_1740})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.c__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2562,(0,1):C.GC_2471})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_753})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3829})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_991})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4011})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.c__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2634,(0,1):C.GC_2504})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.t__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4010,(0,1):C.GC_3862})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.u__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1668,(0,1):C.GC_1761})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_460})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2505})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.t__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3785,(0,1):C.GC_3863})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.u__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1701,(0,1):C.GC_1762})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.c__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2573,(0,1):C.GC_2506})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_769})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3864})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_975,(0,1):C.GC_499})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3984,(0,1):C.GC_2694})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2622,(0,1):C.GC_3044})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3983,(0,1):C.GC_2969})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1656,(0,1):C.GC_3392})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_444,(0,1):C.GC_672})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2467,(0,1):C.GC_3431})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3773,(0,1):C.GC_3369})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1689,(0,1):C.GC_4207})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2561,(0,1):C.GC_4238})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_751,(0,1):C.GC_402})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3826,(0,1):C.GC_4147})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_989,(0,1):C.GC_513})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4008,(0,1):C.GC_2708})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2633,(0,1):C.GC_3055})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4007,(0,1):C.GC_2980})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1667,(0,1):C.GC_3403})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_458,(0,1):C.GC_686})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2502,(0,1):C.GC_3466})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3784,(0,1):C.GC_3380})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1700,(0,1):C.GC_4218})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2572,(0,1):C.GC_4249})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_767,(0,1):C.GC_416})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3861,(0,1):C.GC_4182})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_979})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3989})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2624,(0,1):C.GC_2472})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3988,(0,1):C.GC_3830})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1658,(0,1):C.GC_1741})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_448})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_2473})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3775,(0,1):C.GC_3831})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1691,(0,1):C.GC_1742})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2563,(0,1):C.GC_2474})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_757})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS2 ],
                couplings = {(0,0):C.GC_3832})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_992})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4013})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2635,(0,1):C.GC_2507})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4012,(0,1):C.GC_3865})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1669,(0,1):C.GC_1763})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_461})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_2508})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3786,(0,1):C.GC_3866})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1702,(0,1):C.GC_1764})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2574,(0,1):C.GC_2509})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_770})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_3867})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_504,(0,1):C.GC_980})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2698,(0,1):C.GC_3991})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3003,(0,1):C.GC_2475})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3004,(0,1):C.GC_3833})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3439,(0,1):C.GC_1743})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_677,(0,1):C.GC_449})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3441,(0,1):C.GC_2477})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3442,(0,1):C.GC_3834})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4154,(0,1):C.GC_1744})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4155,(0,1):C.GC_2478})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_407,(0,1):C.GC_758})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4157,(0,1):C.GC_3836})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_517,(0,1):C.GC_993})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2712,(0,1):C.GC_4015})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3025,(0,1):C.GC_2510})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3026,(0,1):C.GC_3868})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3474,(0,1):C.GC_1765})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_690,(0,1):C.GC_462})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3476,(0,1):C.GC_2512})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3477,(0,1):C.GC_3869})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4189,(0,1):C.GC_1766})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4190,(0,1):C.GC_2513})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_420,(0,1):C.GC_771})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4192,(0,1):C.GC_3871})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_561})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_618})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_889})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_572})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_629})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_900})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_981,(0,1):C.GC_505})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3992,(0,1):C.GC_2699})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2625,(0,1):C.GC_3047})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3990,(0,1):C.GC_2972})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1659,(0,1):C.GC_3395})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_450,(0,1):C.GC_678})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2476,(0,1):C.GC_3440})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3776,(0,1):C.GC_3372})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_1692,(0,1):C.GC_4210})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_2564,(0,1):C.GC_4241})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_759,(0,1):C.GC_408})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3835,(0,1):C.GC_4156})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_994,(0,1):C.GC_518})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4016,(0,1):C.GC_2713})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2636,(0,1):C.GC_3058})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_4014,(0,1):C.GC_2983})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1670,(0,1):C.GC_3406})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_463,(0,1):C.GC_691})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2511,(0,1):C.GC_3475})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3787,(0,1):C.GC_3383})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_1703,(0,1):C.GC_4221})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_2575,(0,1):C.GC_4252})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_772,(0,1):C.GC_421})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV4 ],
                couplings = {(0,0):C.GC_3870,(0,1):C.GC_4191})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_557})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_614})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_885})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_569})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_626})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_897})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_562})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_619})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_890})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_573})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_630})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV4 ],
                couplings = {(0,0):C.GC_901})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(0,0):C.GC_38,(2,0):C.GC_39,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_38,(2,4):C.GC_39,(0,5):C.GC_10})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(0,0):C.GC_2649,(2,0):C.GC_2650,(1,3):C.GC_2649,(3,3):C.GC_2650,(1,1):C.GC_2649,(3,1):C.GC_2650,(1,2):C.GC_11,(0,4):C.GC_2649,(2,4):C.GC_2650,(0,5):C.GC_11})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_1135,(2,0):C.GC_1136,(1,3):C.GC_1135,(3,3):C.GC_1136,(1,1):C.GC_1135,(3,1):C.GC_1136,(1,2):C.GC_537,(0,4):C.GC_1135,(2,4):C.GC_1136,(0,5):C.GC_537})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_538,(0,1):C.GC_538})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2663,(0,1):C.GC_2663})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2669,(0,1):C.GC_2669})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2675,(0,1):C.GC_2675})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2681,(0,1):C.GC_2681})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2936,(0,5):C.GC_2936,(0,0):C.GC_1927,(2,0):C.GC_1930,(1,2):C.GC_1192,(3,2):C.GC_1194,(1,1):C.GC_1927,(3,1):C.GC_1930,(0,3):C.GC_1192,(2,3):C.GC_1194})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2940,(0,3):C.GC_2940,(1,0):C.GC_2920,(3,0):C.GC_2922,(0,1):C.GC_2920,(2,1):C.GC_2922})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2944,(0,1):C.GC_2944})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2950,(0,1):C.GC_2950})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2937,(0,5):C.GC_2937,(0,0):C.GC_2762,(2,0):C.GC_2765,(1,2):C.GC_1193,(3,2):C.GC_1195,(1,1):C.GC_2762,(3,1):C.GC_2765,(0,3):C.GC_1193,(2,3):C.GC_1195})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2941,(0,3):C.GC_2941,(1,0):C.GC_2921,(3,0):C.GC_2923,(0,1):C.GC_2921,(2,1):C.GC_2923})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2946,(0,1):C.GC_2946})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2951,(0,1):C.GC_2951})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3317,(0,5):C.GC_3317,(0,0):C.GC_1333,(2,0):C.GC_1336,(1,2):C.GC_1333,(3,2):C.GC_1336,(1,1):C.GC_1198,(3,1):C.GC_1201,(0,3):C.GC_1198,(2,3):C.GC_1201})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3325,(0,3):C.GC_3325,(0,0):C.GC_3287,(2,0):C.GC_3291,(1,1):C.GC_3287,(3,1):C.GC_3291})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3332,(0,1):C.GC_3332})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3341,(0,1):C.GC_3341})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_2108,(2,0):C.GC_2111,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_1199,(2,4):C.GC_1202,(0,5):C.GC_11})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_3229,(2,2):C.GC_3230,(1,0):C.GC_2864,(2,0):C.GC_2866,(1,1):C.GC_728,(0,3):C.GC_730})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4080,(0,3):C.GC_4088,(1,1):C.GC_1334,(2,1):C.GC_1337,(1,0):C.GC_1933,(2,0):C.GC_1936})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4098,(0,1):C.GC_4106})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3321,(0,5):C.GC_3328,(0,0):C.GC_3110,(2,0):C.GC_3113,(1,2):C.GC_1335,(3,2):C.GC_1338,(1,1):C.GC_2778,(3,1):C.GC_2781,(0,3):C.GC_1200,(2,3):C.GC_1203})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3336,(0,2):C.GC_3345,(1,0):C.GC_3290,(2,0):C.GC_3294})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4075,(0,5):C.GC_4075,(0,0):C.GC_1518,(2,0):C.GC_1521,(1,2):C.GC_1518,(3,2):C.GC_1521,(1,1):C.GC_1178,(3,1):C.GC_1181,(0,3):C.GC_1178,(2,3):C.GC_1181})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4086,(0,3):C.GC_4086,(0,0):C.GC_4045,(2,0):C.GC_4049,(1,1):C.GC_4045,(3,1):C.GC_4049})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4094,(0,1):C.GC_4094})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4104,(0,1):C.GC_4104})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4076,(0,5):C.GC_4087,(0,0):C.GC_2308,(2,0):C.GC_2311,(1,2):C.GC_1519,(3,2):C.GC_1522,(1,1):C.GC_1908,(3,1):C.GC_1911,(0,3):C.GC_1179,(2,3):C.GC_1182})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4096,(0,2):C.GC_4105,(1,0):C.GC_4046,(2,0):C.GC_4050})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_3552,(2,0):C.GC_3555,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_1180,(2,4):C.GC_1183,(0,5):C.GC_11})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_3899,(2,2):C.GC_3900,(1,0):C.GC_2863,(2,0):C.GC_2865,(1,1):C.GC_544,(0,3):C.GC_545})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3319,(0,3):C.GC_3326,(1,1):C.GC_1520,(2,1):C.GC_1523,(1,0):C.GC_2756,(2,0):C.GC_2759})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3334,(0,1):C.GC_3342})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2936,(0,5):C.GC_2936,(0,0):C.GC_2109,(2,0):C.GC_2112,(1,2):C.GC_2109,(3,2):C.GC_2112,(1,1):C.GC_2920,(3,1):C.GC_2922,(0,3):C.GC_2920,(2,3):C.GC_2922})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2940,(0,3):C.GC_2940,(1,0):C.GC_1934,(3,0):C.GC_1937,(0,1):C.GC_1934,(2,1):C.GC_1937})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2944,(0,1):C.GC_2944})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2950,(0,1):C.GC_2950})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2941,(0,5):C.GC_2937,(0,0):C.GC_3111,(2,0):C.GC_3114,(1,2):C.GC_2110,(3,2):C.GC_2113,(1,1):C.GC_2779,(3,1):C.GC_2782,(0,3):C.GC_2921,(2,3):C.GC_2923})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2951,(0,2):C.GC_2946,(0,0):C.GC_1935,(2,0):C.GC_1938})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2936,(0,5):C.GC_2940,(0,0):C.GC_3553,(2,0):C.GC_3556,(1,2):C.GC_2310,(3,2):C.GC_2313,(1,1):C.GC_2920,(3,1):C.GC_2922,(0,3):C.GC_1910,(2,3):C.GC_1913})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2944,(0,2):C.GC_2950,(1,0):C.GC_2757,(2,0):C.GC_2760})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_2937,(0,5):C.GC_2937,(0,0):C.GC_3554,(2,0):C.GC_3557,(1,2):C.GC_3554,(3,2):C.GC_3557,(1,1):C.GC_2921,(3,1):C.GC_2923,(0,3):C.GC_2921,(2,3):C.GC_2923})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2941,(0,3):C.GC_2941,(1,0):C.GC_2758,(3,0):C.GC_2761,(0,1):C.GC_2758,(2,1):C.GC_2761})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2946,(0,1):C.GC_2946})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2951,(0,1):C.GC_2951})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3317,(0,5):C.GC_3317,(0,0):C.GC_3287,(2,0):C.GC_3291,(1,2):C.GC_1352,(3,2):C.GC_1355,(1,1):C.GC_3287,(3,1):C.GC_3291,(0,3):C.GC_1352,(2,3):C.GC_1355})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3325,(0,3):C.GC_3325,(0,0):C.GC_2116,(2,0):C.GC_2119,(1,1):C.GC_2116,(3,1):C.GC_2119})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3332,(0,1):C.GC_3332})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3341,(0,1):C.GC_3341})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4086,(0,5):C.GC_4075,(0,0):C.GC_4045,(2,0):C.GC_4049,(1,2):C.GC_1527,(3,2):C.GC_1530,(1,1):C.GC_2079,(3,1):C.GC_2082,(0,3):C.GC_1328,(2,3):C.GC_1331})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4104,(0,2):C.GC_4094,(0,0):C.GC_2314,(2,0):C.GC_2317})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3317,(0,5):C.GC_3325,(0,0):C.GC_3560,(2,0):C.GC_3563,(1,2):C.GC_1528,(3,2):C.GC_1531,(1,1):C.GC_3287,(3,1):C.GC_3291,(0,3):C.GC_1329,(2,3):C.GC_1332})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3332,(0,2):C.GC_3341,(1,0):C.GC_3104,(2,0):C.GC_3107})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(0,0):C.GC_38,(2,0):C.GC_39,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_38,(2,4):C.GC_39,(0,5):C.GC_10})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(0,0):C.GC_3289,(2,0):C.GC_3293,(1,3):C.GC_3289,(3,3):C.GC_3293,(1,1):C.GC_3289,(3,1):C.GC_3293,(1,2):C.GC_11,(0,4):C.GC_3289,(2,4):C.GC_3293,(0,5):C.GC_11})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_2117,(2,0):C.GC_2120,(1,3):C.GC_2117,(3,3):C.GC_2120,(1,1):C.GC_2117,(3,1):C.GC_2120,(1,2):C.GC_720,(0,4):C.GC_2117,(2,4):C.GC_2120,(0,5):C.GC_720})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_721,(0,1):C.GC_721})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3320,(0,1):C.GC_3320})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3327,(0,1):C.GC_3327})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3335,(0,1):C.GC_3335})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3343,(0,1):C.GC_3343})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3321,(0,5):C.GC_3321,(0,0):C.GC_3117,(2,0):C.GC_3120,(1,2):C.GC_3290,(3,2):C.GC_3294,(1,1):C.GC_3117,(3,1):C.GC_3120,(0,3):C.GC_3290,(2,3):C.GC_3294})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3328,(0,3):C.GC_3328,(1,0):C.GC_2118,(3,0):C.GC_2121,(0,1):C.GC_2118,(2,1):C.GC_2121})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3336,(0,1):C.GC_3336})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3345,(0,1):C.GC_3345})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4076,(0,5):C.GC_4076,(0,0):C.GC_4046,(2,0):C.GC_4050,(1,2):C.GC_4046,(3,2):C.GC_4050,(1,1):C.GC_2080,(3,1):C.GC_2083,(0,3):C.GC_2080,(2,3):C.GC_2083})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4087,(0,3):C.GC_4087,(0,0):C.GC_2315,(2,0):C.GC_2318,(1,1):C.GC_2315,(3,1):C.GC_2318})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4096,(0,1):C.GC_4096})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4105,(0,1):C.GC_4105})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_3561,(2,0):C.GC_3564,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_2081,(2,4):C.GC_2084,(0,5):C.GC_11})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_4048,(2,2):C.GC_4052,(1,0):C.GC_3288,(2,0):C.GC_3292,(1,1):C.GC_727,(0,3):C.GC_729})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2661,(0,3):C.GC_2668,(1,1):C.GC_2316,(2,1):C.GC_2319,(1,0):C.GC_3105,(2,0):C.GC_3108})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2674,(0,1):C.GC_2680})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_3321,(0,5):C.GC_3321,(0,0):C.GC_3562,(2,0):C.GC_3565,(1,2):C.GC_3562,(3,2):C.GC_3565,(1,1):C.GC_3290,(3,1):C.GC_3294,(0,3):C.GC_3290,(2,3):C.GC_3294})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3328,(0,3):C.GC_3328,(1,0):C.GC_3106,(3,0):C.GC_3109,(0,1):C.GC_3106,(2,1):C.GC_3109})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3336,(0,1):C.GC_3336})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3345,(0,1):C.GC_3345})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4075,(0,5):C.GC_4075,(0,0):C.GC_4045,(2,0):C.GC_4049,(1,2):C.GC_1514,(3,2):C.GC_1517,(1,1):C.GC_4045,(3,1):C.GC_4049,(0,3):C.GC_1514,(2,3):C.GC_1517})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4086,(0,3):C.GC_4086,(0,0):C.GC_3534,(2,0):C.GC_3537,(1,1):C.GC_3534,(3,1):C.GC_3537})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4094,(0,1):C.GC_4094})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4104,(0,1):C.GC_4104})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_4076,(0,5):C.GC_4076,(0,0):C.GC_4046,(2,0):C.GC_4050,(1,2):C.GC_2292,(3,2):C.GC_2295,(1,1):C.GC_4046,(3,1):C.GC_4050,(0,3):C.GC_2292,(2,3):C.GC_2295})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4087,(0,3):C.GC_4087,(0,0):C.GC_3535,(2,0):C.GC_3538,(1,1):C.GC_3535,(3,1):C.GC_3538})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4096,(0,1):C.GC_4096})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4105,(0,1):C.GC_4105})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(0,0):C.GC_38,(2,0):C.GC_39,(1,3):C.GC_38,(3,3):C.GC_39,(1,1):C.GC_38,(3,1):C.GC_39,(1,2):C.GC_10,(0,4):C.GC_38,(2,4):C.GC_39,(0,5):C.GC_10})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(0,0):C.GC_4047,(2,0):C.GC_4051,(1,3):C.GC_4047,(3,3):C.GC_4051,(1,1):C.GC_4047,(3,1):C.GC_4051,(1,2):C.GC_11,(0,4):C.GC_4047,(2,4):C.GC_4051,(0,5):C.GC_11})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_3536,(2,0):C.GC_3539,(1,3):C.GC_3536,(3,3):C.GC_3539,(1,1):C.GC_3536,(3,1):C.GC_3539,(1,2):C.GC_431,(0,4):C.GC_3536,(2,4):C.GC_3539,(0,5):C.GC_431})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_432,(0,1):C.GC_432})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4081,(0,1):C.GC_4081})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4089,(0,1):C.GC_4089})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4099,(0,1):C.GC_4099})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4107,(0,1):C.GC_4107})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_23,(0,7):C.GC_23,(0,0):C.GC_22,(0,3):C.GC_22,(0,1):C.GC_22,(0,2):C.GC_13,(0,4):C.GC_22,(0,5):C.GC_13})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_23,(0,4):C.GC_24,(0,2):C.GC_22,(0,0):C.GC_22,(0,1):C.GC_13})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_23,(0,4):C.GC_24,(0,2):C.GC_22,(0,0):C.GC_22,(0,1):C.GC_13})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_23,(0,7):C.GC_23,(0,0):C.GC_22,(0,3):C.GC_22,(0,1):C.GC_22,(0,2):C.GC_13,(0,4):C.GC_22,(0,5):C.GC_13})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(0,3):C.GC_23,(0,4):C.GC_24,(0,2):C.GC_22,(0,0):C.GC_22,(0,1):C.GC_13})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(0,6):C.GC_23,(0,7):C.GC_23,(0,0):C.GC_22,(0,3):C.GC_22,(0,1):C.GC_22,(0,2):C.GC_13,(0,4):C.GC_22,(0,5):C.GC_13})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_597,(0,0):C.GC_597})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_2660,(0,2):C.GC_540,(0,3):C.GC_539,(0,5):C.GC_2717,(0,0):C.GC_2717})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2659})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_654,(0,0):C.GC_654})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_2660,(0,2):C.GC_540,(0,3):C.GC_539,(0,5):C.GC_2718,(0,0):C.GC_2718})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2659})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_925,(0,0):C.GC_925})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_2660,(0,2):C.GC_540,(0,3):C.GC_539,(0,5):C.GC_2719,(0,0):C.GC_2719})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2659})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2928,(0,1):C.GC_2934,(0,3):C.GC_3034,(0,0):C.GC_3062})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2930})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2928,(0,1):C.GC_2934,(0,3):C.GC_3037,(0,0):C.GC_3063})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2930})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2928,(0,1):C.GC_2934,(0,3):C.GC_3065,(0,0):C.GC_3067})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2930})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2929,(0,1):C.GC_2935,(0,3):C.GC_3035,(0,0):C.GC_3033})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2932})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2929,(0,1):C.GC_2935,(0,3):C.GC_3038,(0,0):C.GC_3036})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2932})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_2929,(0,1):C.GC_2935,(0,3):C.GC_3066,(0,0):C.GC_3064})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2932})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3305,(0,1):C.GC_3314,(0,3):C.GC_3487,(0,0):C.GC_3411})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3308})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3305,(0,1):C.GC_3314,(0,3):C.GC_3490,(0,0):C.GC_3413})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3308})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3305,(0,1):C.GC_3314,(0,3):C.GC_3495,(0,0):C.GC_3494})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3308})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_710,(0,0):C.GC_710})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_3315,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_3488,(0,0):C.GC_3488})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3310})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_714,(0,0):C.GC_714})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_3315,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_3491,(0,0):C.GC_3491})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3310})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_929,(0,0):C.GC_929})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_3315,(0,2):C.GC_723,(0,3):C.GC_722,(0,5):C.GC_3496,(0,0):C.GC_3496})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3310})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3307,(0,1):C.GC_3316,(0,3):C.GC_3489,(0,0):C.GC_3410})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3312})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3307,(0,1):C.GC_3316,(0,3):C.GC_3492,(0,0):C.GC_3412})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3312})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_3307,(0,1):C.GC_3316,(0,3):C.GC_3497,(0,0):C.GC_3493})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3312})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4063,(0,1):C.GC_4072,(0,3):C.GC_4225,(0,0):C.GC_4228})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4066})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4063,(0,1):C.GC_4072,(0,3):C.GC_4229,(0,0):C.GC_4232})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4066})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4063,(0,1):C.GC_4072,(0,3):C.GC_4258,(0,0):C.GC_4261})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4066})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4064,(0,1):C.GC_4073,(0,3):C.GC_4226,(0,0):C.GC_4256})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4068})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4064,(0,1):C.GC_4073,(0,3):C.GC_4230,(0,0):C.GC_4257})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4068})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF4, L.FFFF8 ],
                couplings = {(0,2):C.GC_4064,(0,1):C.GC_4073,(0,3):C.GC_4259,(0,0):C.GC_4262})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4068})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_581,(0,0):C.GC_581})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_4074,(0,2):C.GC_434,(0,3):C.GC_433,(0,5):C.GC_4227,(0,0):C.GC_4227})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4070})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_638,(0,0):C.GC_638})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_4074,(0,2):C.GC_434,(0,3):C.GC_433,(0,5):C.GC_4231,(0,0):C.GC_4231})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4070})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_25,(0,1):C.GC_40,(0,2):C.GC_21,(0,3):C.GC_12,(0,5):C.GC_909,(0,0):C.GC_909})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF4, L.FFFF8 ],
                couplings = {(0,4):C.GC_27,(0,1):C.GC_4074,(0,2):C.GC_434,(0,3):C.GC_433,(0,5):C.GC_4260,(0,0):C.GC_4260})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4070})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_28,(0,5):C.GC_1025,(0,3):C.GC_1024,(0,4):C.GC_1024,(0,1):C.GC_1019,(0,0):C.GC_598})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1076,(0,5):C.GC_1107,(0,3):C.GC_1106,(0,4):C.GC_1106,(0,1):C.GC_1103,(0,0):C.GC_1095})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_31,(0,5):C.GC_592,(0,3):C.GC_591,(0,4):C.GC_591,(0,1):C.GC_586,(0,0):C.GC_599})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_546,(0,5):C.GC_607,(0,3):C.GC_606,(0,4):C.GC_606,(0,1):C.GC_605,(0,0):C.GC_608})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_34,(0,5):C.GC_803,(0,3):C.GC_802,(0,4):C.GC_802,(0,1):C.GC_797,(0,0):C.GC_600})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_838,(0,5):C.GC_866,(0,3):C.GC_865,(0,4):C.GC_865,(0,1):C.GC_862,(0,0):C.GC_857})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_29,(0,5):C.GC_1027,(0,3):C.GC_1026,(0,4):C.GC_1026,(0,1):C.GC_1020,(0,0):C.GC_711})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1077,(0,5):C.GC_1109,(0,3):C.GC_1108,(0,4):C.GC_1108,(0,1):C.GC_1104,(0,0):C.GC_1098})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_32,(0,5):C.GC_594,(0,3):C.GC_593,(0,4):C.GC_593,(0,1):C.GC_587,(0,0):C.GC_712})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_731,(0,5):C.GC_739,(0,3):C.GC_738,(0,4):C.GC_738,(0,1):C.GC_737,(0,0):C.GC_743})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_35,(0,5):C.GC_805,(0,3):C.GC_804,(0,4):C.GC_804,(0,1):C.GC_798,(0,0):C.GC_713})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_839,(0,5):C.GC_868,(0,3):C.GC_867,(0,4):C.GC_867,(0,1):C.GC_863,(0,0):C.GC_860})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_30,(0,5):C.GC_1029,(0,3):C.GC_1028,(0,4):C.GC_1028,(0,1):C.GC_1021,(0,0):C.GC_582})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1078,(0,5):C.GC_1111,(0,3):C.GC_1110,(0,4):C.GC_1110,(0,1):C.GC_1105,(0,0):C.GC_1094})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_33,(0,5):C.GC_596,(0,3):C.GC_595,(0,4):C.GC_595,(0,1):C.GC_588,(0,0):C.GC_583})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_487,(0,5):C.GC_604,(0,3):C.GC_603,(0,4):C.GC_603,(0,1):C.GC_602,(0,0):C.GC_601})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_36,(0,5):C.GC_807,(0,3):C.GC_806,(0,4):C.GC_806,(0,1):C.GC_799,(0,0):C.GC_584})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_840,(0,5):C.GC_870,(0,3):C.GC_869,(0,4):C.GC_869,(0,1):C.GC_864,(0,0):C.GC_856})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_28,(0,5):C.GC_1037,(0,3):C.GC_1036,(0,4):C.GC_1036,(0,1):C.GC_1031,(0,0):C.GC_655})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1076,(0,5):C.GC_1116,(0,3):C.GC_1115,(0,4):C.GC_1115,(0,1):C.GC_1112,(0,0):C.GC_1097})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_31,(0,5):C.GC_649,(0,3):C.GC_648,(0,4):C.GC_648,(0,1):C.GC_643,(0,0):C.GC_656})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_546,(0,5):C.GC_664,(0,3):C.GC_663,(0,4):C.GC_663,(0,1):C.GC_662,(0,0):C.GC_665})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_34,(0,5):C.GC_815,(0,3):C.GC_814,(0,4):C.GC_814,(0,1):C.GC_809,(0,0):C.GC_657})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_838,(0,5):C.GC_875,(0,3):C.GC_874,(0,4):C.GC_874,(0,1):C.GC_871,(0,0):C.GC_859})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_29,(0,5):C.GC_1039,(0,3):C.GC_1038,(0,4):C.GC_1038,(0,1):C.GC_1032,(0,0):C.GC_715})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1077,(0,5):C.GC_1118,(0,3):C.GC_1117,(0,4):C.GC_1117,(0,1):C.GC_1113,(0,0):C.GC_1099})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_32,(0,5):C.GC_651,(0,3):C.GC_650,(0,4):C.GC_650,(0,1):C.GC_644,(0,0):C.GC_716})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_731,(0,5):C.GC_742,(0,3):C.GC_741,(0,4):C.GC_741,(0,1):C.GC_740,(0,0):C.GC_744})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_35,(0,5):C.GC_817,(0,3):C.GC_816,(0,4):C.GC_816,(0,1):C.GC_810,(0,0):C.GC_717})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_839,(0,5):C.GC_877,(0,3):C.GC_876,(0,4):C.GC_876,(0,1):C.GC_872,(0,0):C.GC_861})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_30,(0,5):C.GC_1041,(0,3):C.GC_1040,(0,4):C.GC_1040,(0,1):C.GC_1033,(0,0):C.GC_639})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1078,(0,5):C.GC_1120,(0,3):C.GC_1119,(0,4):C.GC_1119,(0,1):C.GC_1114,(0,0):C.GC_1096})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_33,(0,5):C.GC_653,(0,3):C.GC_652,(0,4):C.GC_652,(0,1):C.GC_645,(0,0):C.GC_640})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_487,(0,5):C.GC_661,(0,3):C.GC_660,(0,4):C.GC_660,(0,1):C.GC_659,(0,0):C.GC_658})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_36,(0,5):C.GC_819,(0,3):C.GC_818,(0,4):C.GC_818,(0,1):C.GC_811,(0,0):C.GC_641})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_840,(0,5):C.GC_879,(0,3):C.GC_878,(0,4):C.GC_878,(0,1):C.GC_873,(0,0):C.GC_858})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_28,(0,5):C.GC_1058,(0,3):C.GC_1057,(0,4):C.GC_1057,(0,1):C.GC_1052,(0,0):C.GC_926})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1076,(0,5):C.GC_1125,(0,3):C.GC_1124,(0,4):C.GC_1124,(0,1):C.GC_1121,(0,0):C.GC_1101})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_31,(0,5):C.GC_920,(0,3):C.GC_919,(0,4):C.GC_919,(0,1):C.GC_914,(0,0):C.GC_927})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_546,(0,5):C.GC_951,(0,3):C.GC_950,(0,4):C.GC_950,(0,1):C.GC_949,(0,0):C.GC_952})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_34,(0,5):C.GC_940,(0,3):C.GC_939,(0,4):C.GC_939,(0,1):C.GC_934,(0,0):C.GC_928})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_838,(0,5):C.GC_964,(0,3):C.GC_963,(0,4):C.GC_963,(0,1):C.GC_960,(0,0):C.GC_958})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_29,(0,5):C.GC_1060,(0,3):C.GC_1059,(0,4):C.GC_1059,(0,1):C.GC_1053,(0,0):C.GC_930})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1077,(0,5):C.GC_1127,(0,3):C.GC_1126,(0,4):C.GC_1126,(0,1):C.GC_1122,(0,0):C.GC_1102})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_32,(0,5):C.GC_922,(0,3):C.GC_921,(0,4):C.GC_921,(0,1):C.GC_915,(0,0):C.GC_931})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_731,(0,5):C.GC_955,(0,3):C.GC_954,(0,4):C.GC_954,(0,1):C.GC_953,(0,0):C.GC_956})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_35,(0,5):C.GC_942,(0,3):C.GC_941,(0,4):C.GC_941,(0,1):C.GC_935,(0,0):C.GC_932})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_839,(0,5):C.GC_966,(0,3):C.GC_965,(0,4):C.GC_965,(0,1):C.GC_961,(0,0):C.GC_959})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_30,(0,5):C.GC_1062,(0,3):C.GC_1061,(0,4):C.GC_1061,(0,1):C.GC_1054,(0,0):C.GC_910})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_1078,(0,5):C.GC_1129,(0,3):C.GC_1128,(0,4):C.GC_1128,(0,1):C.GC_1123,(0,0):C.GC_1100})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_33,(0,5):C.GC_924,(0,3):C.GC_923,(0,4):C.GC_923,(0,1):C.GC_916,(0,0):C.GC_911})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_487,(0,5):C.GC_948,(0,3):C.GC_947,(0,4):C.GC_947,(0,1):C.GC_946,(0,0):C.GC_945})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_36,(0,5):C.GC_944,(0,3):C.GC_943,(0,4):C.GC_943,(0,1):C.GC_936,(0,0):C.GC_912})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF10, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,2):C.GC_840,(0,5):C.GC_968,(0,3):C.GC_967,(0,4):C.GC_967,(0,1):C.GC_962,(0,0):C.GC_957})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_1011,(3,0):C.GC_1013,(0,5):C.GC_1141,(2,5):C.GC_1142,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_1011,(3,8):C.GC_1013,(0,1):C.GC_1141,(2,1):C.GC_1142})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_3742,(1,0):C.GC_1227,(3,0):C.GC_1228,(0,5):C.GC_1012,(2,5):C.GC_1014,(1,4):C.GC_3671,(3,4):C.GC_3679,(1,2):C.GC_2653,(3,2):C.GC_2656,(1,3):C.GC_1080,(3,3):C.GC_1083,(1,8):C.GC_1227,(3,8):C.GC_1228,(0,1):C.GC_1012,(2,1):C.GC_1014})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3713,(0,3):C.GC_1153,(1,1):C.GC_535,(2,1):C.GC_536,(1,0):C.GC_1255,(2,0):C.GC_1258})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2875,(0,1):C.GC_1267})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1144})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1162})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1262})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1272})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1835,(0,6):C.GC_1844,(1,0):C.GC_2614,(3,0):C.GC_2616,(0,4):C.GC_2613,(2,4):C.GC_2615,(1,3):C.GC_2381,(3,3):C.GC_2386,(1,2):C.GC_1957,(3,2):C.GC_1960,(1,7):C.GC_2375,(3,7):C.GC_2379,(0,1):C.GC_2373,(2,1):C.GC_2377})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1853,(0,1):C.GC_2672})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2666,(0,1):C.GC_2364})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2362})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2679})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2411})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2721,(0,6):C.GC_2730,(1,0):C.GC_3967,(3,0):C.GC_3971,(0,4):C.GC_3965,(2,4):C.GC_3969,(1,3):C.GC_3665,(3,3):C.GC_3673,(1,2):C.GC_2851,(3,2):C.GC_2854,(1,7):C.GC_3802,(3,7):C.GC_3806,(0,1):C.GC_3800,(2,1):C.GC_3804})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2739,(0,1):C.GC_4092})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_4084,(0,1):C.GC_3659})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3655})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4103})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3707})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1147,(0,6):C.GC_1156,(1,0):C.GC_1610,(3,0):C.GC_1612,(0,4):C.GC_1609,(2,4):C.GC_1611,(1,3):C.GC_1613,(3,3):C.GC_1615,(1,2):C.GC_1221,(3,2):C.GC_1224,(1,7):C.GC_1721,(3,7):C.GC_1725,(0,1):C.GC_1719,(2,1):C.GC_1723})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1165,(0,1):C.GC_1804})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1795,(0,1):C.GC_1607})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1605})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1814})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1629})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(0,7):C.GC_46,(1,6):C.GC_41,(1,0):C.GC_528,(3,0):C.GC_530,(0,5):C.GC_1130,(2,5):C.GC_1131,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_528,(3,8):C.GC_530,(0,1):C.GC_1130,(2,1):C.GC_1131})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(0,7):C.GC_2682,(1,6):C.GC_43,(1,0):C.GC_1889,(3,0):C.GC_1894,(0,5):C.GC_529,(2,5):C.GC_531,(1,4):C.GC_2383,(3,4):C.GC_2388,(1,2):C.GC_2651,(3,2):C.GC_2654,(1,3):C.GC_547,(3,3):C.GC_548,(1,8):C.GC_1889,(3,8):C.GC_1894,(0,1):C.GC_529,(2,1):C.GC_531})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(0,2):C.GC_1847,(1,1):C.GC_2662,(1,0):C.GC_1881,(2,0):C.GC_1884})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,1):C.GC_1974,(1,0):C.GC_2876})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1838})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1856})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1972})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1976})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2724,(0,6):C.GC_2733,(1,0):C.GC_3662,(3,0):C.GC_3664,(0,4):C.GC_3661,(2,4):C.GC_3663,(1,3):C.GC_3666,(3,3):C.GC_3674,(1,2):C.GC_2796,(3,2):C.GC_2799,(1,7):C.GC_3803,(3,7):C.GC_3807,(0,1):C.GC_3801,(2,1):C.GC_3805})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2742,(0,1):C.GC_3911})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3904,(0,1):C.GC_3660})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3656})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3924})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3708})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1150,(0,6):C.GC_1159,(1,0):C.GC_1681,(3,0):C.GC_1683,(0,4):C.GC_1680,(2,4):C.GC_1682,(1,3):C.GC_1614,(3,3):C.GC_1616,(1,2):C.GC_1246,(3,2):C.GC_1249,(1,7):C.GC_1722,(3,7):C.GC_1726,(0,1):C.GC_1720,(2,1):C.GC_1724})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1168,(0,1):C.GC_1808})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1799,(0,1):C.GC_1608})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1606})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1818})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1630})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1841,(0,6):C.GC_1850,(1,0):C.GC_2553,(3,0):C.GC_2555,(0,4):C.GC_2552,(2,4):C.GC_2554,(1,3):C.GC_2385,(3,3):C.GC_2390,(1,2):C.GC_1939,(3,2):C.GC_1942,(1,7):C.GC_2376,(3,7):C.GC_2380,(0,1):C.GC_2374,(2,1):C.GC_2378})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1859,(0,1):C.GC_2591})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2587,(0,1):C.GC_2365})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2363})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2596})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2414})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_789,(3,0):C.GC_791,(0,5):C.GC_1137,(2,5):C.GC_1138,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_789,(3,8):C.GC_791,(0,1):C.GC_1137,(2,1):C.GC_1138})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_3739,(1,0):C.GC_2804,(3,0):C.GC_2809,(0,5):C.GC_790,(2,5):C.GC_792,(1,4):C.GC_3668,(3,4):C.GC_3676,(1,2):C.GC_2652,(3,2):C.GC_2655,(1,3):C.GC_842,(3,3):C.GC_845,(1,8):C.GC_2804,(3,8):C.GC_2809,(0,1):C.GC_790,(2,1):C.GC_792})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3710,(0,2):C.GC_2736,(1,0):C.GC_2833,(2,0):C.GC_2836})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3657,(0,1):C.GC_2877})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2727})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2745})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2870})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2884})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1145,(0,5):C.GC_1154,(1,0):C.GC_2910,(3,0):C.GC_2914,(0,3):C.GC_2908,(2,3):C.GC_2912,(1,2):C.GC_1256,(3,2):C.GC_1259,(1,6):C.GC_2917,(3,6):C.GC_2919,(0,1):C.GC_2916,(2,1):C.GC_2918})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1163,(0,2):C.GC_2861,(1,0):C.GC_2924,(2,0):C.GC_2926})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2860,(0,1):C.GC_2886})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2878})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2862})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2936})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1836,(0,5):C.GC_1845,(1,0):C.GC_1965,(3,0):C.GC_1969,(0,3):C.GC_1963,(2,3):C.GC_1967,(1,2):C.GC_1958,(3,2):C.GC_1961,(1,6):C.GC_1917,(3,6):C.GC_1923,(0,1):C.GC_1914,(2,1):C.GC_1920})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1854,(0,1):C.GC_2004})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2002})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2006})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2722,(0,5):C.GC_2731,(1,0):C.GC_2845,(3,0):C.GC_2849,(0,3):C.GC_2843,(2,3):C.GC_2847,(1,2):C.GC_2852,(3,2):C.GC_2855,(1,6):C.GC_2824,(3,6):C.GC_2830,(0,1):C.GC_2821,(2,1):C.GC_2827})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2740,(0,1):C.GC_2942})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2938})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2948})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1148,(0,6):C.GC_1157,(1,0):C.GC_1186,(3,0):C.GC_1190,(0,4):C.GC_1184,(2,4):C.GC_1188,(1,3):C.GC_708,(3,3):C.GC_709,(1,2):C.GC_1222,(3,2):C.GC_1225,(1,7):C.GC_1240,(3,7):C.GC_1244,(0,1):C.GC_1238,(2,1):C.GC_1242})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1166,(0,1):C.GC_1268})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1263})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1273})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1839,(0,5):C.GC_2886,(1,0):C.GC_1890,(3,0):C.GC_1895,(0,3):C.GC_1887,(2,3):C.GC_1892,(1,2):C.GC_1882,(3,2):C.GC_1885,(1,6):C.GC_1918,(3,6):C.GC_1924,(0,1):C.GC_1915,(2,1):C.GC_1921})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1857,(0,2):C.GC_1848,(1,0):C.GC_2924,(2,0):C.GC_2926})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2936,(0,1):C.GC_1990})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1989})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2945})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1991})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2725,(0,5):C.GC_2734,(1,0):C.GC_2770,(3,0):C.GC_2774,(0,3):C.GC_2768,(2,3):C.GC_2772,(1,2):C.GC_2797,(3,2):C.GC_2800,(1,6):C.GC_2825,(3,6):C.GC_2831,(0,1):C.GC_2822,(2,1):C.GC_2828})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2743,(0,1):C.GC_2873})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2868})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2882})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1151,(0,5):C.GC_1160,(1,0):C.GC_1206,(3,0):C.GC_1210,(0,3):C.GC_1204,(2,3):C.GC_1208,(1,2):C.GC_1247,(3,2):C.GC_1250,(1,6):C.GC_1241,(3,6):C.GC_1245,(0,1):C.GC_1239,(2,1):C.GC_1243})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1169,(0,1):C.GC_1270})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1265})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1275})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1842,(0,5):C.GC_1851,(1,0):C.GC_1947,(3,0):C.GC_1951,(0,3):C.GC_1945,(2,3):C.GC_1949,(1,2):C.GC_1940,(3,2):C.GC_1943,(1,6):C.GC_1919,(3,6):C.GC_1925,(0,1):C.GC_1916,(2,1):C.GC_1922})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1860,(0,1):C.GC_1994})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1992})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1996})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2936,(0,5):C.GC_2886,(1,0):C.GC_2805,(3,0):C.GC_2810,(0,3):C.GC_2802,(2,3):C.GC_2807,(1,2):C.GC_2924,(3,2):C.GC_2926,(1,6):C.GC_2826,(3,6):C.GC_2832,(0,1):C.GC_2823,(2,1):C.GC_2829})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2945,(0,2):C.GC_2737,(1,0):C.GC_2834,(2,0):C.GC_2837})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2728,(0,1):C.GC_2879})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2746})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2871})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2885})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1146,(0,5):C.GC_1155,(1,0):C.GC_2911,(3,0):C.GC_2915,(0,3):C.GC_2909,(2,3):C.GC_2913,(1,2):C.GC_1257,(3,2):C.GC_1260,(1,6):C.GC_2905,(3,6):C.GC_2907,(0,1):C.GC_2904,(2,1):C.GC_2906})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1164,(0,2):C.GC_2858,(1,0):C.GC_2925,(2,0):C.GC_2927})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2857,(0,1):C.GC_2888})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2880})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2859})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2937})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1837,(0,5):C.GC_1846,(1,0):C.GC_1966,(3,0):C.GC_1970,(0,3):C.GC_1964,(2,3):C.GC_1968,(1,2):C.GC_1959,(3,2):C.GC_1962,(1,6):C.GC_1872,(3,6):C.GC_1878,(0,1):C.GC_1869,(2,1):C.GC_1875})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1855,(0,1):C.GC_2005})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2003})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2007})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2723,(0,5):C.GC_2732,(1,0):C.GC_2846,(3,0):C.GC_2850,(0,3):C.GC_2844,(2,3):C.GC_2848,(1,2):C.GC_2853,(3,2):C.GC_2856,(1,6):C.GC_2787,(3,6):C.GC_2793,(0,1):C.GC_2784,(2,1):C.GC_2790})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2741,(0,1):C.GC_2943})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2939})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2949})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1149,(0,5):C.GC_1158,(1,0):C.GC_1187,(3,0):C.GC_1191,(0,3):C.GC_1185,(2,3):C.GC_1189,(1,2):C.GC_1223,(3,2):C.GC_1226,(1,6):C.GC_1215,(3,6):C.GC_1219,(0,1):C.GC_1213,(2,1):C.GC_1217})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1167,(0,1):C.GC_1269})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1264})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1274})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1840,(0,5):C.GC_2888,(1,0):C.GC_1891,(3,0):C.GC_1896,(0,3):C.GC_1888,(2,3):C.GC_1893,(1,2):C.GC_1883,(3,2):C.GC_1886,(1,6):C.GC_1873,(3,6):C.GC_1879,(0,1):C.GC_1870,(2,1):C.GC_1876})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1858,(0,2):C.GC_1849,(1,0):C.GC_2925,(2,0):C.GC_2927})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1973,(0,1):C.GC_1975})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1977})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2937})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2947})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2726,(0,5):C.GC_2735,(1,0):C.GC_2771,(3,0):C.GC_2775,(0,3):C.GC_2769,(2,3):C.GC_2773,(1,2):C.GC_2798,(3,2):C.GC_2801,(1,6):C.GC_2788,(3,6):C.GC_2794,(0,1):C.GC_2785,(2,1):C.GC_2791})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2744,(0,1):C.GC_2874})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2869})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2883})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1152,(0,6):C.GC_1161,(1,0):C.GC_1207,(3,0):C.GC_1211,(0,4):C.GC_1205,(2,4):C.GC_1209,(1,3):C.GC_526,(3,3):C.GC_527,(1,2):C.GC_1248,(3,2):C.GC_1251,(1,7):C.GC_1216,(3,7):C.GC_1220,(0,1):C.GC_1214,(2,1):C.GC_1218})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1170,(0,1):C.GC_1271})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1266})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1276})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1843,(0,5):C.GC_1852,(1,0):C.GC_1948,(3,0):C.GC_1952,(0,3):C.GC_1946,(2,3):C.GC_1950,(1,2):C.GC_1941,(3,2):C.GC_1944,(1,6):C.GC_1874,(3,6):C.GC_1880,(0,1):C.GC_1871,(2,1):C.GC_1877})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1861,(0,1):C.GC_1995})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1993})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1997})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2937,(0,5):C.GC_2888,(1,0):C.GC_2806,(3,0):C.GC_2811,(0,3):C.GC_2803,(2,3):C.GC_2808,(1,2):C.GC_2925,(3,2):C.GC_2927,(1,6):C.GC_2789,(3,6):C.GC_2795,(0,1):C.GC_2786,(2,1):C.GC_2792})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2947,(0,2):C.GC_2738,(1,0):C.GC_2835,(2,0):C.GC_2838})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2729,(0,1):C.GC_2881})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2747})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2872})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2887})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1293,(0,5):C.GC_1302,(1,0):C.GC_3281,(3,0):C.GC_3285,(0,3):C.GC_3279,(2,3):C.GC_3283,(1,2):C.GC_1422,(3,2):C.GC_1425,(1,6):C.GC_3276,(3,6):C.GC_3278,(0,1):C.GC_3275,(2,1):C.GC_3277})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1311,(0,2):C.GC_3225,(1,0):C.GC_3295,(2,0):C.GC_3300})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3223,(0,1):C.GC_3252})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3241})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3227})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3317})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2009,(0,6):C.GC_2018,(1,0):C.GC_2153,(3,0):C.GC_2159,(0,4):C.GC_2150,(2,4):C.GC_2156,(1,3):C.GC_708,(3,3):C.GC_709,(1,2):C.GC_2144,(3,2):C.GC_2147,(1,7):C.GC_2064,(3,7):C.GC_2070,(0,1):C.GC_2061,(2,1):C.GC_2067})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2027,(0,1):C.GC_2199})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2196})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2202})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3069,(0,5):C.GC_3078,(1,0):C.GC_3208,(3,0):C.GC_3214,(0,3):C.GC_3205,(2,3):C.GC_3211,(1,2):C.GC_3217,(3,2):C.GC_3220,(1,6):C.GC_3157,(3,6):C.GC_3163,(0,1):C.GC_3154,(2,1):C.GC_3160})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3087,(0,1):C.GC_3329})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3322})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3338})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1296,(0,5):C.GC_1305,(1,0):C.GC_1342,(3,0):C.GC_1348,(0,3):C.GC_1339,(2,3):C.GC_1345,(1,2):C.GC_1380,(3,2):C.GC_1383,(1,6):C.GC_1388,(3,6):C.GC_1392,(0,1):C.GC_1386,(2,1):C.GC_1390})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1314,(0,1):C.GC_1437})

V_1572 = Vertex(name = 'V_1572',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1430})

V_1573 = Vertex(name = 'V_1573',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1444})

V_1574 = Vertex(name = 'V_1574',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2012,(0,5):C.GC_3252,(1,0):C.GC_2091,(3,0):C.GC_2101,(0,3):C.GC_2086,(2,3):C.GC_2096,(1,2):C.GC_2055,(3,2):C.GC_2058,(1,6):C.GC_2065,(3,6):C.GC_2071,(0,1):C.GC_2062,(2,1):C.GC_2068})

V_1575 = Vertex(name = 'V_1575',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2030,(0,2):C.GC_2021,(1,0):C.GC_3295,(2,0):C.GC_3300})

V_1576 = Vertex(name = 'V_1576',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3317,(0,1):C.GC_2166})

V_1577 = Vertex(name = 'V_1577',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2163})

V_1578 = Vertex(name = 'V_1578',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3333})

V_1579 = Vertex(name = 'V_1579',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2169})

V_1580 = Vertex(name = 'V_1580',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3072,(0,5):C.GC_3081,(1,0):C.GC_3125,(3,0):C.GC_3131,(0,3):C.GC_3122,(2,3):C.GC_3128,(1,2):C.GC_3148,(3,2):C.GC_3151,(1,6):C.GC_3158,(3,6):C.GC_3164,(0,1):C.GC_3155,(2,1):C.GC_3161})

V_1581 = Vertex(name = 'V_1581',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3090,(0,1):C.GC_3238})

V_1582 = Vertex(name = 'V_1582',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3232})

V_1583 = Vertex(name = 'V_1583',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3248})

V_1584 = Vertex(name = 'V_1584',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1299,(0,5):C.GC_1308,(1,0):C.GC_1362,(3,0):C.GC_1368,(0,3):C.GC_1359,(2,3):C.GC_1365,(1,2):C.GC_1413,(3,2):C.GC_1416,(1,6):C.GC_1389,(3,6):C.GC_1393,(0,1):C.GC_1387,(2,1):C.GC_1391})

V_1585 = Vertex(name = 'V_1585',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1317,(0,1):C.GC_1440})

V_1586 = Vertex(name = 'V_1586',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1433})

V_1587 = Vertex(name = 'V_1587',
                particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1447})

V_1588 = Vertex(name = 'V_1588',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2015,(0,5):C.GC_2024,(1,0):C.GC_2131,(3,0):C.GC_2137,(0,3):C.GC_2128,(2,3):C.GC_2134,(1,2):C.GC_2122,(3,2):C.GC_2125,(1,6):C.GC_2066,(3,6):C.GC_2072,(0,1):C.GC_2063,(2,1):C.GC_2069})

V_1589 = Vertex(name = 'V_1589',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2033,(0,1):C.GC_2186})

V_1590 = Vertex(name = 'V_1590',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2183})

V_1591 = Vertex(name = 'V_1591',
                particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2189})

V_1592 = Vertex(name = 'V_1592',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3317,(0,5):C.GC_3252,(1,0):C.GC_3179,(3,0):C.GC_3189,(0,3):C.GC_3174,(2,3):C.GC_3184,(1,2):C.GC_3295,(3,2):C.GC_3300,(1,6):C.GC_3159,(3,6):C.GC_3165,(0,1):C.GC_3156,(2,1):C.GC_3162})

V_1593 = Vertex(name = 'V_1593',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3333,(0,2):C.GC_3084,(1,0):C.GC_3195,(2,0):C.GC_3198})

V_1594 = Vertex(name = 'V_1594',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3075,(0,1):C.GC_3242})

V_1595 = Vertex(name = 'V_1595',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3093})

V_1596 = Vertex(name = 'V_1596',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3235})

V_1597 = Vertex(name = 'V_1597',
                particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3251})

V_1598 = Vertex(name = 'V_1598',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_1042,(3,0):C.GC_1044,(0,5):C.GC_1132,(2,5):C.GC_1133,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_1042,(3,8):C.GC_1044,(0,1):C.GC_1132,(2,1):C.GC_1133})

V_1599 = Vertex(name = 'V_1599',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_3743,(1,0):C.GC_1402,(3,0):C.GC_1407,(0,5):C.GC_1043,(2,5):C.GC_1045,(1,4):C.GC_3672,(3,4):C.GC_3680,(1,2):C.GC_3298,(3,2):C.GC_3303,(1,3):C.GC_1081,(3,3):C.GC_1084,(1,8):C.GC_1402,(3,8):C.GC_1407,(0,1):C.GC_1043,(2,1):C.GC_1045})

V_1600 = Vertex(name = 'V_1600',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3714,(0,2):C.GC_1303,(1,0):C.GC_1423,(2,0):C.GC_1426})

V_1601 = Vertex(name = 'V_1601',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3243,(0,1):C.GC_1436})

V_1602 = Vertex(name = 'V_1602',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1294})

V_1603 = Vertex(name = 'V_1603',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1312})

V_1604 = Vertex(name = 'V_1604',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1429})

V_1605 = Vertex(name = 'V_1605',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1443})

V_1606 = Vertex(name = 'V_1606',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2010,(0,6):C.GC_2364,(1,0):C.GC_2154,(3,0):C.GC_2160,(0,4):C.GC_2151,(2,4):C.GC_2157,(1,3):C.GC_2381,(3,3):C.GC_2386,(1,2):C.GC_2145,(3,2):C.GC_2148,(1,7):C.GC_2090,(3,7):C.GC_2100,(0,1):C.GC_2085,(2,1):C.GC_2095})

V_1607 = Vertex(name = 'V_1607',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2028,(0,1):C.GC_2019})

V_1608 = Vertex(name = 'V_1608',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2197,(0,1):C.GC_2200})

V_1609 = Vertex(name = 'V_1609',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2203})

V_1610 = Vertex(name = 'V_1610',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2411})

V_1611 = Vertex(name = 'V_1611',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2421})

V_1612 = Vertex(name = 'V_1612',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3070,(0,6):C.GC_3659,(1,0):C.GC_3209,(3,0):C.GC_3215,(0,4):C.GC_3206,(2,4):C.GC_3212,(1,3):C.GC_3665,(3,3):C.GC_3673,(1,2):C.GC_3218,(3,2):C.GC_3221,(1,7):C.GC_3177,(3,7):C.GC_3187,(0,1):C.GC_3172,(2,1):C.GC_3182})

V_1613 = Vertex(name = 'V_1613',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3088,(0,1):C.GC_3079})

V_1614 = Vertex(name = 'V_1614',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3707,(0,1):C.GC_3330})

V_1615 = Vertex(name = 'V_1615',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3725})

V_1616 = Vertex(name = 'V_1616',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3323})

V_1617 = Vertex(name = 'V_1617',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3339})

V_1618 = Vertex(name = 'V_1618',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1297,(0,6):C.GC_1607,(1,0):C.GC_1343,(3,0):C.GC_1349,(0,4):C.GC_1340,(2,4):C.GC_1346,(1,3):C.GC_1613,(3,3):C.GC_1615,(1,2):C.GC_1381,(3,2):C.GC_1384,(1,7):C.GC_1403,(3,7):C.GC_1408,(0,1):C.GC_1400,(2,1):C.GC_1405})

V_1619 = Vertex(name = 'V_1619',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1315,(0,1):C.GC_1306})

V_1620 = Vertex(name = 'V_1620',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1431,(0,1):C.GC_1438})

V_1621 = Vertex(name = 'V_1621',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1445})

V_1622 = Vertex(name = 'V_1622',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1629})

V_1623 = Vertex(name = 'V_1623',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1634})

V_1624 = Vertex(name = 'V_1624',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_701,(3,0):C.GC_703,(0,5):C.GC_702,(2,5):C.GC_704,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_701,(3,8):C.GC_703,(0,1):C.GC_702,(2,1):C.GC_704})

V_1625 = Vertex(name = 'V_1625',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_3344,(1,0):C.GC_2092,(3,0):C.GC_2102,(0,5):C.GC_2087,(2,5):C.GC_2097,(1,4):C.GC_2384,(3,4):C.GC_2389,(1,2):C.GC_3296,(3,2):C.GC_3301,(1,3):C.GC_732,(3,3):C.GC_733,(1,8):C.GC_2092,(3,8):C.GC_2102,(0,1):C.GC_2087,(2,1):C.GC_2097})

V_1626 = Vertex(name = 'V_1626',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3318,(0,3):C.GC_2022,(1,1):C.GC_718,(2,1):C.GC_719,(1,0):C.GC_2056,(2,0):C.GC_2059})

V_1627 = Vertex(name = 'V_1627',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3244,(0,1):C.GC_2167})

V_1628 = Vertex(name = 'V_1628',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2013})

V_1629 = Vertex(name = 'V_1629',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2031})

V_1630 = Vertex(name = 'V_1630',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2164})

V_1631 = Vertex(name = 'V_1631',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2170})

V_1632 = Vertex(name = 'V_1632',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3073,(0,6):C.GC_3660,(1,0):C.GC_3126,(3,0):C.GC_3132,(0,4):C.GC_3123,(2,4):C.GC_3129,(1,3):C.GC_3666,(3,3):C.GC_3674,(1,2):C.GC_3149,(3,2):C.GC_3152,(1,7):C.GC_3178,(3,7):C.GC_3188,(0,1):C.GC_3173,(2,1):C.GC_3183})

V_1633 = Vertex(name = 'V_1633',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3091,(0,1):C.GC_3082})

V_1634 = Vertex(name = 'V_1634',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3233,(0,1):C.GC_3239})

V_1635 = Vertex(name = 'V_1635',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3249})

V_1636 = Vertex(name = 'V_1636',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3708})

V_1637 = Vertex(name = 'V_1637',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3727})

V_1638 = Vertex(name = 'V_1638',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1300,(0,6):C.GC_1608,(1,0):C.GC_1363,(3,0):C.GC_1369,(0,4):C.GC_1360,(2,4):C.GC_1366,(1,3):C.GC_1614,(3,3):C.GC_1616,(1,2):C.GC_1414,(3,2):C.GC_1417,(1,7):C.GC_1404,(3,7):C.GC_1409,(0,1):C.GC_1401,(2,1):C.GC_1406})

V_1639 = Vertex(name = 'V_1639',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1318,(0,1):C.GC_1309})

V_1640 = Vertex(name = 'V_1640',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1630,(0,1):C.GC_1441})

V_1641 = Vertex(name = 'V_1641',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1636})

V_1642 = Vertex(name = 'V_1642',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1434})

V_1643 = Vertex(name = 'V_1643',
                particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1448})

V_1644 = Vertex(name = 'V_1644',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2016,(0,6):C.GC_2365,(1,0):C.GC_2132,(3,0):C.GC_2138,(0,4):C.GC_2129,(2,4):C.GC_2135,(1,3):C.GC_2385,(3,3):C.GC_2390,(1,2):C.GC_2123,(3,2):C.GC_2126,(1,7):C.GC_2094,(3,7):C.GC_2104,(0,1):C.GC_2089,(2,1):C.GC_2099})

V_1645 = Vertex(name = 'V_1645',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2034,(0,1):C.GC_2025})

V_1646 = Vertex(name = 'V_1646',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2184,(0,1):C.GC_2187})

V_1647 = Vertex(name = 'V_1647',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2190})

V_1648 = Vertex(name = 'V_1648',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2414})

V_1649 = Vertex(name = 'V_1649',
                particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2426})

V_1650 = Vertex(name = 'V_1650',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_820,(3,0):C.GC_822,(0,5):C.GC_821,(2,5):C.GC_823,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_820,(3,8):C.GC_822,(0,1):C.GC_821,(2,1):C.GC_823})

V_1651 = Vertex(name = 'V_1651',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_3740,(1,0):C.GC_3180,(3,0):C.GC_3190,(0,5):C.GC_3175,(2,5):C.GC_3185,(1,4):C.GC_3669,(3,4):C.GC_3677,(1,2):C.GC_3297,(3,2):C.GC_3302,(1,3):C.GC_843,(3,3):C.GC_846,(1,8):C.GC_3180,(3,8):C.GC_3190,(0,1):C.GC_3175,(2,1):C.GC_3185})

V_1652 = Vertex(name = 'V_1652',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3711,(0,2):C.GC_3085,(1,0):C.GC_3196,(2,0):C.GC_3199})

V_1653 = Vertex(name = 'V_1653',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3658,(0,1):C.GC_3245})

V_1654 = Vertex(name = 'V_1654',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3076})

V_1655 = Vertex(name = 'V_1655',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3094})

V_1656 = Vertex(name = 'V_1656',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3236})

V_1657 = Vertex(name = 'V_1657',
                particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3253})

V_1658 = Vertex(name = 'V_1658',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1295,(0,5):C.GC_1304,(1,0):C.GC_3282,(3,0):C.GC_3286,(0,3):C.GC_3280,(2,3):C.GC_3284,(1,2):C.GC_1424,(3,2):C.GC_1427,(1,6):C.GC_3272,(3,6):C.GC_3274,(0,1):C.GC_3271,(2,1):C.GC_3273})

V_1659 = Vertex(name = 'V_1659',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1313,(0,2):C.GC_3226,(1,0):C.GC_3299,(2,0):C.GC_3304})

V_1660 = Vertex(name = 'V_1660',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3224,(0,1):C.GC_3255})

V_1661 = Vertex(name = 'V_1661',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3246})

V_1662 = Vertex(name = 'V_1662',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3228})

V_1663 = Vertex(name = 'V_1663',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3321})

V_1664 = Vertex(name = 'V_1664',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2011,(0,5):C.GC_2020,(1,0):C.GC_2155,(3,0):C.GC_2161,(0,3):C.GC_2152,(2,3):C.GC_2158,(1,2):C.GC_2146,(3,2):C.GC_2149,(1,6):C.GC_2046,(3,6):C.GC_2052,(0,1):C.GC_2043,(2,1):C.GC_2049})

V_1665 = Vertex(name = 'V_1665',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2029,(0,1):C.GC_2201})

V_1666 = Vertex(name = 'V_1666',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2198})

V_1667 = Vertex(name = 'V_1667',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2204})

V_1668 = Vertex(name = 'V_1668',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3071,(0,5):C.GC_3080,(1,0):C.GC_3210,(3,0):C.GC_3216,(0,3):C.GC_3207,(2,3):C.GC_3213,(1,2):C.GC_3219,(3,2):C.GC_3222,(1,6):C.GC_3139,(3,6):C.GC_3145,(0,1):C.GC_3136,(2,1):C.GC_3142})

V_1669 = Vertex(name = 'V_1669',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3089,(0,1):C.GC_3331})

V_1670 = Vertex(name = 'V_1670',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3324})

V_1671 = Vertex(name = 'V_1671',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3340})

V_1672 = Vertex(name = 'V_1672',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1298,(0,5):C.GC_1307,(1,0):C.GC_1344,(3,0):C.GC_1350,(0,3):C.GC_1341,(2,3):C.GC_1347,(1,2):C.GC_1382,(3,2):C.GC_1385,(1,6):C.GC_1374,(3,6):C.GC_1378,(0,1):C.GC_1372,(2,1):C.GC_1376})

V_1673 = Vertex(name = 'V_1673',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1316,(0,1):C.GC_1439})

V_1674 = Vertex(name = 'V_1674',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1432})

V_1675 = Vertex(name = 'V_1675',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1446})

V_1676 = Vertex(name = 'V_1676',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2014,(0,5):C.GC_3255,(1,0):C.GC_2093,(3,0):C.GC_2103,(0,3):C.GC_2088,(2,3):C.GC_2098,(1,2):C.GC_2057,(3,2):C.GC_2060,(1,6):C.GC_2047,(3,6):C.GC_2053,(0,1):C.GC_2044,(2,1):C.GC_2050})

V_1677 = Vertex(name = 'V_1677',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2032,(0,2):C.GC_2023,(1,0):C.GC_3299,(2,0):C.GC_3304})

V_1678 = Vertex(name = 'V_1678',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2165,(0,1):C.GC_2168})

V_1679 = Vertex(name = 'V_1679',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2171})

V_1680 = Vertex(name = 'V_1680',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3321})

V_1681 = Vertex(name = 'V_1681',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3337})

V_1682 = Vertex(name = 'V_1682',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3074,(0,5):C.GC_3083,(1,0):C.GC_3127,(3,0):C.GC_3133,(0,3):C.GC_3124,(2,3):C.GC_3130,(1,2):C.GC_3150,(3,2):C.GC_3153,(1,6):C.GC_3140,(3,6):C.GC_3146,(0,1):C.GC_3137,(2,1):C.GC_3143})

V_1683 = Vertex(name = 'V_1683',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3092,(0,1):C.GC_3240})

V_1684 = Vertex(name = 'V_1684',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3234})

V_1685 = Vertex(name = 'V_1685',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3250})

V_1686 = Vertex(name = 'V_1686',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1301,(0,5):C.GC_1310,(1,0):C.GC_1364,(3,0):C.GC_1370,(0,3):C.GC_1361,(2,3):C.GC_1367,(1,2):C.GC_1415,(3,2):C.GC_1418,(1,6):C.GC_1375,(3,6):C.GC_1379,(0,1):C.GC_1373,(2,1):C.GC_1377})

V_1687 = Vertex(name = 'V_1687',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1319,(0,1):C.GC_1442})

V_1688 = Vertex(name = 'V_1688',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1435})

V_1689 = Vertex(name = 'V_1689',
                particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1449})

V_1690 = Vertex(name = 'V_1690',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2017,(0,6):C.GC_2026,(1,0):C.GC_2133,(3,0):C.GC_2139,(0,4):C.GC_2130,(2,4):C.GC_2136,(1,3):C.GC_699,(3,3):C.GC_700,(1,2):C.GC_2124,(3,2):C.GC_2127,(1,7):C.GC_2048,(3,7):C.GC_2054,(0,1):C.GC_2045,(2,1):C.GC_2051})

V_1691 = Vertex(name = 'V_1691',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2035,(0,1):C.GC_2188})

V_1692 = Vertex(name = 'V_1692',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2185})

V_1693 = Vertex(name = 'V_1693',
                particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2191})

V_1694 = Vertex(name = 'V_1694',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3321,(0,5):C.GC_3255,(1,0):C.GC_3181,(3,0):C.GC_3191,(0,3):C.GC_3176,(2,3):C.GC_3186,(1,2):C.GC_3299,(3,2):C.GC_3304,(1,6):C.GC_3141,(3,6):C.GC_3147,(0,1):C.GC_3138,(2,1):C.GC_3144})

V_1695 = Vertex(name = 'V_1695',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3337,(0,2):C.GC_3086,(1,0):C.GC_3197,(2,0):C.GC_3200})

V_1696 = Vertex(name = 'V_1696',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3077,(0,1):C.GC_3247})

V_1697 = Vertex(name = 'V_1697',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3095})

V_1698 = Vertex(name = 'V_1698',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3237})

V_1699 = Vertex(name = 'V_1699',
                particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3254})

V_1700 = Vertex(name = 'V_1700',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1466,(0,5):C.GC_1475,(1,0):C.GC_3959,(3,0):C.GC_3963,(0,3):C.GC_3957,(2,3):C.GC_3961,(1,2):C.GC_1595,(3,2):C.GC_1598,(1,6):C.GC_3968,(3,6):C.GC_3972,(0,1):C.GC_3966,(2,1):C.GC_3970})

V_1701 = Vertex(name = 'V_1701',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1484,(0,2):C.GC_3728,(1,0):C.GC_4053,(2,0):C.GC_4058})

V_1702 = Vertex(name = 'V_1702',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3719,(0,1):C.GC_3926})

V_1703 = Vertex(name = 'V_1703',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3913})

V_1704 = Vertex(name = 'V_1704',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3735})

V_1705 = Vertex(name = 'V_1705',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4075})

V_1706 = Vertex(name = 'V_1706',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2206,(0,5):C.GC_2215,(1,0):C.GC_2345,(3,0):C.GC_2351,(0,3):C.GC_2342,(2,3):C.GC_2348,(1,2):C.GC_2354,(3,2):C.GC_2357,(1,6):C.GC_2273,(3,6):C.GC_2279,(0,1):C.GC_2270,(2,1):C.GC_2276})

V_1707 = Vertex(name = 'V_1707',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2224,(0,1):C.GC_2670})

V_1708 = Vertex(name = 'V_1708',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2664})

V_1709 = Vertex(name = 'V_1709',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2676})

V_1710 = Vertex(name = 'V_1710',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3499,(0,6):C.GC_3508,(1,0):C.GC_3638,(3,0):C.GC_3644,(0,4):C.GC_3635,(2,4):C.GC_3641,(1,3):C.GC_526,(3,3):C.GC_527,(1,2):C.GC_3647,(3,2):C.GC_3650,(1,7):C.GC_3598,(3,7):C.GC_3604,(0,1):C.GC_3595,(2,1):C.GC_3601})

V_1711 = Vertex(name = 'V_1711',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3517,(0,1):C.GC_4090})

V_1712 = Vertex(name = 'V_1712',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4082})

V_1713 = Vertex(name = 'V_1713',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4100})

V_1714 = Vertex(name = 'V_1714',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1469,(0,5):C.GC_1478,(1,0):C.GC_1503,(3,0):C.GC_1509,(0,3):C.GC_1500,(2,3):C.GC_1506,(1,2):C.GC_1558,(3,2):C.GC_1561,(1,6):C.GC_1566,(3,6):C.GC_1570,(0,1):C.GC_1564,(2,1):C.GC_1568})

V_1715 = Vertex(name = 'V_1715',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1487,(0,1):C.GC_1802})

V_1716 = Vertex(name = 'V_1716',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1793})

V_1717 = Vertex(name = 'V_1717',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1811})

V_1718 = Vertex(name = 'V_1718',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2209,(0,5):C.GC_3926,(1,0):C.GC_2246,(3,0):C.GC_2256,(0,3):C.GC_2241,(2,3):C.GC_2251,(1,2):C.GC_2264,(3,2):C.GC_2267,(1,6):C.GC_2274,(3,6):C.GC_2280,(0,1):C.GC_2271,(2,1):C.GC_2277})

V_1719 = Vertex(name = 'V_1719',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2227,(0,2):C.GC_2218,(1,0):C.GC_4053,(2,0):C.GC_4058})

V_1720 = Vertex(name = 'V_1720',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2416,(0,1):C.GC_2422})

V_1721 = Vertex(name = 'V_1721',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2428})

V_1722 = Vertex(name = 'V_1722',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4075})

V_1723 = Vertex(name = 'V_1723',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4095})

V_1724 = Vertex(name = 'V_1724',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3502,(0,5):C.GC_3511,(1,0):C.GC_3543,(3,0):C.GC_3549,(0,3):C.GC_3540,(2,3):C.GC_3546,(1,2):C.GC_3589,(3,2):C.GC_3592,(1,6):C.GC_3599,(3,6):C.GC_3605,(0,1):C.GC_3596,(2,1):C.GC_3602})

V_1725 = Vertex(name = 'V_1725',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3520,(0,1):C.GC_3909})

V_1726 = Vertex(name = 'V_1726',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3902})

V_1727 = Vertex(name = 'V_1727',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3921})

V_1728 = Vertex(name = 'V_1728',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1472,(0,5):C.GC_1481,(1,0):C.GC_1535,(3,0):C.GC_1541,(0,3):C.GC_1532,(2,3):C.GC_1538,(1,2):C.GC_1586,(3,2):C.GC_1589,(1,6):C.GC_1567,(3,6):C.GC_1571,(0,1):C.GC_1565,(2,1):C.GC_1569})

V_1729 = Vertex(name = 'V_1729',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1490,(0,1):C.GC_1806})

V_1730 = Vertex(name = 'V_1730',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1797})

V_1731 = Vertex(name = 'V_1731',
                particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1815})

V_1732 = Vertex(name = 'V_1732',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2212,(0,5):C.GC_2221,(1,0):C.GC_2323,(3,0):C.GC_2329,(0,3):C.GC_2320,(2,3):C.GC_2326,(1,2):C.GC_2332,(3,2):C.GC_2335,(1,6):C.GC_2275,(3,6):C.GC_2281,(0,1):C.GC_2272,(2,1):C.GC_2278})

V_1733 = Vertex(name = 'V_1733',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2230,(0,1):C.GC_2589})

V_1734 = Vertex(name = 'V_1734',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2585})

V_1735 = Vertex(name = 'V_1735',
                particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2593})

V_1736 = Vertex(name = 'V_1736',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_4075,(0,5):C.GC_3926,(1,0):C.GC_3573,(3,0):C.GC_3583,(0,3):C.GC_3568,(2,3):C.GC_3578,(1,2):C.GC_4053,(3,2):C.GC_4058,(1,6):C.GC_3600,(3,6):C.GC_3606,(0,1):C.GC_3597,(2,1):C.GC_3603})

V_1737 = Vertex(name = 'V_1737',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4095,(0,2):C.GC_3514,(1,0):C.GC_3625,(2,0):C.GC_3628})

V_1738 = Vertex(name = 'V_1738',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3505,(0,1):C.GC_3914})

V_1739 = Vertex(name = 'V_1739',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3523})

V_1740 = Vertex(name = 'V_1740',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3906})

V_1741 = Vertex(name = 'V_1741',
                particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3925})

V_1742 = Vertex(name = 'V_1742',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1467,(0,5):C.GC_1476,(1,0):C.GC_3960,(3,0):C.GC_3964,(0,3):C.GC_3958,(2,3):C.GC_3962,(1,2):C.GC_1596,(3,2):C.GC_1599,(1,6):C.GC_4036,(3,6):C.GC_4038,(0,1):C.GC_4035,(2,1):C.GC_4037})

V_1743 = Vertex(name = 'V_1743',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1485,(0,2):C.GC_3798,(1,0):C.GC_4054,(2,0):C.GC_4059})

V_1744 = Vertex(name = 'V_1744',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3797,(0,1):C.GC_3928})

V_1745 = Vertex(name = 'V_1745',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3915})

V_1746 = Vertex(name = 'V_1746',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3799})

V_1747 = Vertex(name = 'V_1747',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4076})

V_1748 = Vertex(name = 'V_1748',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2207,(0,5):C.GC_2216,(1,0):C.GC_2346,(3,0):C.GC_2352,(0,3):C.GC_2343,(2,3):C.GC_2349,(1,2):C.GC_2355,(3,2):C.GC_2358,(1,6):C.GC_2299,(3,6):C.GC_2305,(0,1):C.GC_2296,(2,1):C.GC_2302})

V_1749 = Vertex(name = 'V_1749',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2225,(0,1):C.GC_2671})

V_1750 = Vertex(name = 'V_1750',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2665})

V_1751 = Vertex(name = 'V_1751',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2677})

V_1752 = Vertex(name = 'V_1752',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_3500,(0,5):C.GC_3509,(1,0):C.GC_3639,(3,0):C.GC_3645,(0,3):C.GC_3636,(2,3):C.GC_3642,(1,2):C.GC_3648,(3,2):C.GC_3651,(1,6):C.GC_3616,(3,6):C.GC_3622,(0,1):C.GC_3613,(2,1):C.GC_3619})

V_1753 = Vertex(name = 'V_1753',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3518,(0,1):C.GC_4091})

V_1754 = Vertex(name = 'V_1754',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4083})

V_1755 = Vertex(name = 'V_1755',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4101})

V_1756 = Vertex(name = 'V_1756',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1470,(0,5):C.GC_1479,(1,0):C.GC_1504,(3,0):C.GC_1510,(0,3):C.GC_1501,(2,3):C.GC_1507,(1,2):C.GC_1559,(3,2):C.GC_1562,(1,6):C.GC_1580,(3,6):C.GC_1584,(0,1):C.GC_1578,(2,1):C.GC_1582})

V_1757 = Vertex(name = 'V_1757',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1488,(0,1):C.GC_1803})

V_1758 = Vertex(name = 'V_1758',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1794})

V_1759 = Vertex(name = 'V_1759',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1812})

V_1760 = Vertex(name = 'V_1760',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2210,(0,5):C.GC_3928,(1,0):C.GC_2247,(3,0):C.GC_2257,(0,3):C.GC_2242,(2,3):C.GC_2252,(1,2):C.GC_2265,(3,2):C.GC_2268,(1,6):C.GC_2300,(3,6):C.GC_2306,(0,1):C.GC_2297,(2,1):C.GC_2303})

V_1761 = Vertex(name = 'V_1761',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2228,(0,2):C.GC_2219,(1,0):C.GC_4054,(2,0):C.GC_4059})

V_1762 = Vertex(name = 'V_1762',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2549,(0,1):C.GC_2550})

V_1763 = Vertex(name = 'V_1763',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2551})

V_1764 = Vertex(name = 'V_1764',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4076})

V_1765 = Vertex(name = 'V_1765',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4097})

V_1766 = Vertex(name = 'V_1766',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3503,(0,6):C.GC_3512,(1,0):C.GC_3544,(3,0):C.GC_3550,(0,4):C.GC_3541,(2,4):C.GC_3547,(1,3):C.GC_699,(3,3):C.GC_700,(1,2):C.GC_3590,(3,2):C.GC_3593,(1,7):C.GC_3617,(3,7):C.GC_3623,(0,1):C.GC_3614,(2,1):C.GC_3620})

V_1767 = Vertex(name = 'V_1767',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3521,(0,1):C.GC_3910})

V_1768 = Vertex(name = 'V_1768',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3903})

V_1769 = Vertex(name = 'V_1769',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3922})

V_1770 = Vertex(name = 'V_1770',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_1473,(0,5):C.GC_1482,(1,0):C.GC_1536,(3,0):C.GC_1542,(0,3):C.GC_1533,(2,3):C.GC_1539,(1,2):C.GC_1587,(3,2):C.GC_1590,(1,6):C.GC_1581,(3,6):C.GC_1585,(0,1):C.GC_1579,(2,1):C.GC_1583})

V_1771 = Vertex(name = 'V_1771',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1491,(0,1):C.GC_1807})

V_1772 = Vertex(name = 'V_1772',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1798})

V_1773 = Vertex(name = 'V_1773',
                particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1816})

V_1774 = Vertex(name = 'V_1774',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_2213,(0,5):C.GC_2222,(1,0):C.GC_2324,(3,0):C.GC_2330,(0,3):C.GC_2321,(2,3):C.GC_2327,(1,2):C.GC_2333,(3,2):C.GC_2336,(1,6):C.GC_2301,(3,6):C.GC_2307,(0,1):C.GC_2298,(2,1):C.GC_2304})

V_1775 = Vertex(name = 'V_1775',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2231,(0,1):C.GC_2590})

V_1776 = Vertex(name = 'V_1776',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2586})

V_1777 = Vertex(name = 'V_1777',
                particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2594})

V_1778 = Vertex(name = 'V_1778',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,4):C.GC_4076,(0,5):C.GC_3928,(1,0):C.GC_3574,(3,0):C.GC_3584,(0,3):C.GC_3569,(2,3):C.GC_3579,(1,2):C.GC_4054,(3,2):C.GC_4059,(1,6):C.GC_3618,(3,6):C.GC_3624,(0,1):C.GC_3615,(2,1):C.GC_3621})

V_1779 = Vertex(name = 'V_1779',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4097,(0,2):C.GC_3515,(1,0):C.GC_3626,(2,0):C.GC_3629})

V_1780 = Vertex(name = 'V_1780',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3506,(0,1):C.GC_3916})

V_1781 = Vertex(name = 'V_1781',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3524})

V_1782 = Vertex(name = 'V_1782',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3907})

V_1783 = Vertex(name = 'V_1783',
                particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3927})

V_1784 = Vertex(name = 'V_1784',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_1002,(3,0):C.GC_1004,(0,5):C.GC_1139,(2,5):C.GC_1140,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_1002,(3,8):C.GC_1004,(0,1):C.GC_1139,(2,1):C.GC_1140})

V_1785 = Vertex(name = 'V_1785',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_4110,(1,0):C.GC_1547,(3,0):C.GC_1552,(0,5):C.GC_1003,(2,5):C.GC_1005,(1,4):C.GC_3670,(3,4):C.GC_3678,(1,2):C.GC_4057,(3,2):C.GC_4062,(1,3):C.GC_1079,(3,3):C.GC_1082,(1,8):C.GC_1547,(3,8):C.GC_1552,(0,1):C.GC_1003,(2,1):C.GC_1005})

V_1786 = Vertex(name = 'V_1786',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4079,(0,2):C.GC_1477,(1,0):C.GC_1597,(2,0):C.GC_1600})

V_1787 = Vertex(name = 'V_1787',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3917,(0,1):C.GC_1801})

V_1788 = Vertex(name = 'V_1788',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1468})

V_1789 = Vertex(name = 'V_1789',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1486})

V_1790 = Vertex(name = 'V_1790',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1792})

V_1791 = Vertex(name = 'V_1791',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1810})

V_1792 = Vertex(name = 'V_1792',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2411,(0,6):C.GC_2364,(1,0):C.GC_2347,(3,0):C.GC_2353,(0,4):C.GC_2344,(2,4):C.GC_2350,(1,3):C.GC_2381,(3,3):C.GC_2386,(1,2):C.GC_2356,(3,2):C.GC_2359,(1,7):C.GC_2245,(3,7):C.GC_2255,(0,1):C.GC_2240,(2,1):C.GC_2250})

V_1793 = Vertex(name = 'V_1793',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2421,(0,1):C.GC_2217})

V_1794 = Vertex(name = 'V_1794',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2208,(0,1):C.GC_2673})

V_1795 = Vertex(name = 'V_1795',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2226})

V_1796 = Vertex(name = 'V_1796',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2667})

V_1797 = Vertex(name = 'V_1797',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2678})

V_1798 = Vertex(name = 'V_1798',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3707,(0,6):C.GC_3659,(1,0):C.GC_3640,(3,0):C.GC_3646,(0,4):C.GC_3637,(2,4):C.GC_3643,(1,3):C.GC_3665,(3,3):C.GC_3673,(1,2):C.GC_3649,(3,2):C.GC_3652,(1,7):C.GC_3571,(3,7):C.GC_3581,(0,1):C.GC_3566,(2,1):C.GC_3576})

V_1799 = Vertex(name = 'V_1799',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3725,(0,1):C.GC_3510})

V_1800 = Vertex(name = 'V_1800',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3501,(0,1):C.GC_4093})

V_1801 = Vertex(name = 'V_1801',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3519})

V_1802 = Vertex(name = 'V_1802',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4085})

V_1803 = Vertex(name = 'V_1803',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_4102})

V_1804 = Vertex(name = 'V_1804',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1629,(0,6):C.GC_1607,(1,0):C.GC_1505,(3,0):C.GC_1511,(0,4):C.GC_1502,(2,4):C.GC_1508,(1,3):C.GC_1613,(3,3):C.GC_1615,(1,2):C.GC_1560,(3,2):C.GC_1563,(1,7):C.GC_1548,(3,7):C.GC_1553,(0,1):C.GC_1545,(2,1):C.GC_1550})

V_1805 = Vertex(name = 'V_1805',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1634,(0,1):C.GC_1480})

V_1806 = Vertex(name = 'V_1806',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1471,(0,1):C.GC_1805})

V_1807 = Vertex(name = 'V_1807',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1489})

V_1808 = Vertex(name = 'V_1808',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1796})

V_1809 = Vertex(name = 'V_1809',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1813})

V_1810 = Vertex(name = 'V_1810',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_471,(3,0):C.GC_473,(0,5):C.GC_472,(2,5):C.GC_474,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_471,(3,8):C.GC_473,(0,1):C.GC_472,(2,1):C.GC_474})

V_1811 = Vertex(name = 'V_1811',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_4108,(1,0):C.GC_2248,(3,0):C.GC_2258,(0,5):C.GC_2243,(2,5):C.GC_2253,(1,4):C.GC_2382,(3,4):C.GC_2387,(1,2):C.GC_4055,(3,2):C.GC_4060,(1,3):C.GC_488,(3,3):C.GC_489,(1,8):C.GC_2248,(3,8):C.GC_2258,(0,1):C.GC_2243,(2,1):C.GC_2253})

V_1812 = Vertex(name = 'V_1812',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_4077,(0,2):C.GC_2220,(1,0):C.GC_2266,(2,0):C.GC_2269})

V_1813 = Vertex(name = 'V_1813',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3918,(0,1):C.GC_2368})

V_1814 = Vertex(name = 'V_1814',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2211})

V_1815 = Vertex(name = 'V_1815',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2229})

V_1816 = Vertex(name = 'V_1816',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2367})

V_1817 = Vertex(name = 'V_1817',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2369})

V_1818 = Vertex(name = 'V_1818',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_3708,(0,6):C.GC_3660,(1,0):C.GC_3545,(3,0):C.GC_3551,(0,4):C.GC_3542,(2,4):C.GC_3548,(1,3):C.GC_3666,(3,3):C.GC_3674,(1,2):C.GC_3591,(3,2):C.GC_3594,(1,7):C.GC_3572,(3,7):C.GC_3582,(0,1):C.GC_3567,(2,1):C.GC_3577})

V_1819 = Vertex(name = 'V_1819',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3727,(0,1):C.GC_3513})

V_1820 = Vertex(name = 'V_1820',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3504,(0,1):C.GC_3912})

V_1821 = Vertex(name = 'V_1821',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3522})

V_1822 = Vertex(name = 'V_1822',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3905})

V_1823 = Vertex(name = 'V_1823',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3923})

V_1824 = Vertex(name = 'V_1824',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_1630,(0,6):C.GC_1608,(1,0):C.GC_1537,(3,0):C.GC_1543,(0,4):C.GC_1534,(2,4):C.GC_1540,(1,3):C.GC_1614,(3,3):C.GC_1616,(1,2):C.GC_1588,(3,2):C.GC_1591,(1,7):C.GC_1549,(3,7):C.GC_1554,(0,1):C.GC_1546,(2,1):C.GC_1551})

V_1825 = Vertex(name = 'V_1825',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1636,(0,1):C.GC_1483})

V_1826 = Vertex(name = 'V_1826',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1474,(0,1):C.GC_1809})

V_1827 = Vertex(name = 'V_1827',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1492})

V_1828 = Vertex(name = 'V_1828',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1800})

V_1829 = Vertex(name = 'V_1829',
                particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_1817})

V_1830 = Vertex(name = 'V_1830',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,5):C.GC_2414,(0,6):C.GC_2365,(1,0):C.GC_2325,(3,0):C.GC_2331,(0,4):C.GC_2322,(2,4):C.GC_2328,(1,3):C.GC_2385,(3,3):C.GC_2390,(1,2):C.GC_2334,(3,2):C.GC_2337,(1,7):C.GC_2249,(3,7):C.GC_2259,(0,1):C.GC_2244,(2,1):C.GC_2254})

V_1831 = Vertex(name = 'V_1831',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2426,(0,1):C.GC_2223})

V_1832 = Vertex(name = 'V_1832',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2214,(0,1):C.GC_2592})

V_1833 = Vertex(name = 'V_1833',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2232})

V_1834 = Vertex(name = 'V_1834',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2588})

V_1835 = Vertex(name = 'V_1835',
                particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_2595})

V_1836 = Vertex(name = 'V_1836',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_46,(1,0):C.GC_780,(3,0):C.GC_782,(0,5):C.GC_781,(2,5):C.GC_783,(1,4):C.GC_38,(3,4):C.GC_39,(1,2):C.GC_47,(3,2):C.GC_48,(1,3):C.GC_51,(3,3):C.GC_52,(1,8):C.GC_780,(3,8):C.GC_782,(0,1):C.GC_781,(2,1):C.GC_783})

V_1837 = Vertex(name = 'V_1837',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF9 ],
                couplings = {(1,6):C.GC_43,(0,7):C.GC_4109,(1,0):C.GC_3575,(3,0):C.GC_3585,(0,5):C.GC_3570,(2,5):C.GC_3580,(1,4):C.GC_429,(3,4):C.GC_430,(1,2):C.GC_4056,(3,2):C.GC_4061,(1,3):C.GC_841,(3,3):C.GC_844,(1,8):C.GC_3575,(3,8):C.GC_3585,(0,1):C.GC_3570,(2,1):C.GC_3580})

V_1838 = Vertex(name = 'V_1838',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_4078,(0,3):C.GC_3516,(1,1):C.GC_3667,(2,1):C.GC_3675,(1,0):C.GC_3627,(2,0):C.GC_3630})

V_1839 = Vertex(name = 'V_1839',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3919,(0,1):C.GC_3920})

V_1840 = Vertex(name = 'V_1840',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3507})

V_1841 = Vertex(name = 'V_1841',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3525})

V_1842 = Vertex(name = 'V_1842',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3908})

V_1843 = Vertex(name = 'V_1843',
                particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
                color = [ 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3 ],
                couplings = {(0,0):C.GC_3929})

V_1844 = Vertex(name = 'V_1844',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_1023,(0,9):C.GC_1022,(0,10):C.GC_1022,(0,6):C.GC_1018,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_1023,(0,4):C.GC_1022,(0,5):C.GC_1022,(0,0):C.GC_1018})

V_1845 = Vertex(name = 'V_1845',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_4028,(0,9):C.GC_4027,(0,10):C.GC_4027,(0,6):C.GC_4024,(0,1):C.GC_3706,(0,2):C.GC_1066,(0,3):C.GC_1065,(0,7):C.GC_4028,(0,4):C.GC_4027,(0,5):C.GC_4027,(0,0):C.GC_4024})

V_1846 = Vertex(name = 'V_1846',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_1847 = Vertex(name = 'V_1847',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3700})

V_1848 = Vertex(name = 'V_1848',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2399,(0,9):C.GC_2642,(0,7):C.GC_2641,(0,8):C.GC_2641,(0,4):C.GC_2640,(0,1):C.GC_2408,(0,5):C.GC_2531,(0,2):C.GC_2530,(0,3):C.GC_2530,(0,0):C.GC_2527})

V_1849 = Vertex(name = 'V_1849',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2403})

V_1850 = Vertex(name = 'V_1850',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3691,(0,9):C.GC_4026,(0,7):C.GC_4025,(0,8):C.GC_4025,(0,4):C.GC_4023,(0,1):C.GC_3703,(0,5):C.GC_3885,(0,2):C.GC_3884,(0,3):C.GC_3884,(0,0):C.GC_3881})

V_1851 = Vertex(name = 'V_1851',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3696})

V_1852 = Vertex(name = 'V_1852',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1621,(0,9):C.GC_1676,(0,7):C.GC_1675,(0,8):C.GC_1675,(0,4):C.GC_1674,(0,1):C.GC_1627,(0,5):C.GC_1776,(0,2):C.GC_1775,(0,3):C.GC_1775,(0,0):C.GC_1773})

V_1853 = Vertex(name = 'V_1853',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1624})

V_1854 = Vertex(name = 'V_1854',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_590,(0,9):C.GC_589,(0,10):C.GC_589,(0,6):C.GC_585,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_590,(0,4):C.GC_589,(0,5):C.GC_589,(0,0):C.GC_585})

V_1855 = Vertex(name = 'V_1855',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_2533,(0,9):C.GC_2532,(0,10):C.GC_2532,(0,6):C.GC_2528,(0,1):C.GC_2409,(0,2):C.GC_481,(0,3):C.GC_480,(0,7):C.GC_2533,(0,4):C.GC_2532,(0,5):C.GC_2532,(0,0):C.GC_2528})

V_1856 = Vertex(name = 'V_1856',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_1857 = Vertex(name = 'V_1857',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2405})

V_1858 = Vertex(name = 'V_1858',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3692,(0,9):C.GC_3793,(0,7):C.GC_3792,(0,8):C.GC_3792,(0,4):C.GC_3791,(0,1):C.GC_3704,(0,5):C.GC_3887,(0,2):C.GC_3886,(0,3):C.GC_3886,(0,0):C.GC_3882})

V_1859 = Vertex(name = 'V_1859',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3698})

V_1860 = Vertex(name = 'V_1860',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1622,(0,9):C.GC_1709,(0,7):C.GC_1708,(0,8):C.GC_1708,(0,4):C.GC_1707,(0,1):C.GC_1628,(0,5):C.GC_1778,(0,2):C.GC_1777,(0,3):C.GC_1777,(0,0):C.GC_1774})

V_1861 = Vertex(name = 'V_1861',
                particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1626})

V_1862 = Vertex(name = 'V_1862',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2401,(0,9):C.GC_2581,(0,7):C.GC_2580,(0,8):C.GC_2580,(0,4):C.GC_2579,(0,1):C.GC_2410,(0,5):C.GC_2535,(0,2):C.GC_2534,(0,3):C.GC_2534,(0,0):C.GC_2529})

V_1863 = Vertex(name = 'V_1863',
                particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2407})

V_1864 = Vertex(name = 'V_1864',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_801,(0,9):C.GC_800,(0,10):C.GC_800,(0,6):C.GC_796,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_801,(0,4):C.GC_800,(0,5):C.GC_800,(0,0):C.GC_796})

V_1865 = Vertex(name = 'V_1865',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_3889,(0,9):C.GC_3888,(0,10):C.GC_3888,(0,6):C.GC_3883,(0,1):C.GC_3705,(0,2):C.GC_830,(0,3):C.GC_829,(0,7):C.GC_3889,(0,4):C.GC_3888,(0,5):C.GC_3888,(0,0):C.GC_3883})

V_1866 = Vertex(name = 'V_1866',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_1867 = Vertex(name = 'V_1867',
                particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3701})

V_1868 = Vertex(name = 'V_1868',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_1035,(0,9):C.GC_1034,(0,10):C.GC_1034,(0,6):C.GC_1030,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_1035,(0,4):C.GC_1034,(0,5):C.GC_1034,(0,0):C.GC_1030})

V_1869 = Vertex(name = 'V_1869',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_4034,(0,9):C.GC_4033,(0,10):C.GC_4033,(0,6):C.GC_4030,(0,1):C.GC_3706,(0,2):C.GC_1066,(0,3):C.GC_1065,(0,7):C.GC_4034,(0,4):C.GC_4033,(0,5):C.GC_4033,(0,0):C.GC_4030})

V_1870 = Vertex(name = 'V_1870',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_1871 = Vertex(name = 'V_1871',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3700})

V_1872 = Vertex(name = 'V_1872',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2399,(0,9):C.GC_2645,(0,7):C.GC_2644,(0,8):C.GC_2644,(0,4):C.GC_2643,(0,1):C.GC_2408,(0,5):C.GC_2544,(0,2):C.GC_2543,(0,3):C.GC_2543,(0,0):C.GC_2540})

V_1873 = Vertex(name = 'V_1873',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2403})

V_1874 = Vertex(name = 'V_1874',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3691,(0,9):C.GC_4032,(0,7):C.GC_4031,(0,8):C.GC_4031,(0,4):C.GC_4029,(0,1):C.GC_3703,(0,5):C.GC_3894,(0,2):C.GC_3893,(0,3):C.GC_3893,(0,0):C.GC_3890})

V_1875 = Vertex(name = 'V_1875',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3696})

V_1876 = Vertex(name = 'V_1876',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1621,(0,9):C.GC_1679,(0,7):C.GC_1678,(0,8):C.GC_1678,(0,4):C.GC_1677,(0,1):C.GC_1627,(0,5):C.GC_1782,(0,2):C.GC_1781,(0,3):C.GC_1781,(0,0):C.GC_1779})

V_1877 = Vertex(name = 'V_1877',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1624})

V_1878 = Vertex(name = 'V_1878',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_647,(0,9):C.GC_646,(0,10):C.GC_646,(0,6):C.GC_642,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_647,(0,4):C.GC_646,(0,5):C.GC_646,(0,0):C.GC_642})

V_1879 = Vertex(name = 'V_1879',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_2546,(0,9):C.GC_2545,(0,10):C.GC_2545,(0,6):C.GC_2541,(0,1):C.GC_2409,(0,2):C.GC_481,(0,3):C.GC_480,(0,7):C.GC_2546,(0,4):C.GC_2545,(0,5):C.GC_2545,(0,0):C.GC_2541})

V_1880 = Vertex(name = 'V_1880',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_1881 = Vertex(name = 'V_1881',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2405})

V_1882 = Vertex(name = 'V_1882',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3692,(0,9):C.GC_3796,(0,7):C.GC_3795,(0,8):C.GC_3795,(0,4):C.GC_3794,(0,1):C.GC_3704,(0,5):C.GC_3896,(0,2):C.GC_3895,(0,3):C.GC_3895,(0,0):C.GC_3891})

V_1883 = Vertex(name = 'V_1883',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3698})

V_1884 = Vertex(name = 'V_1884',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1622,(0,9):C.GC_1712,(0,7):C.GC_1711,(0,8):C.GC_1711,(0,4):C.GC_1710,(0,1):C.GC_1628,(0,5):C.GC_1784,(0,2):C.GC_1783,(0,3):C.GC_1783,(0,0):C.GC_1780})

V_1885 = Vertex(name = 'V_1885',
                particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1626})

V_1886 = Vertex(name = 'V_1886',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2401,(0,9):C.GC_2584,(0,7):C.GC_2583,(0,8):C.GC_2583,(0,4):C.GC_2582,(0,1):C.GC_2410,(0,5):C.GC_2548,(0,2):C.GC_2547,(0,3):C.GC_2547,(0,0):C.GC_2542})

V_1887 = Vertex(name = 'V_1887',
                particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2407})

V_1888 = Vertex(name = 'V_1888',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_813,(0,9):C.GC_812,(0,10):C.GC_812,(0,6):C.GC_808,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_813,(0,4):C.GC_812,(0,5):C.GC_812,(0,0):C.GC_808})

V_1889 = Vertex(name = 'V_1889',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_3898,(0,9):C.GC_3897,(0,10):C.GC_3897,(0,6):C.GC_3892,(0,1):C.GC_3705,(0,2):C.GC_830,(0,3):C.GC_829,(0,7):C.GC_3898,(0,4):C.GC_3897,(0,5):C.GC_3897,(0,0):C.GC_3892})

V_1890 = Vertex(name = 'V_1890',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_1891 = Vertex(name = 'V_1891',
                particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3701})

V_1892 = Vertex(name = 'V_1892',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_1056,(0,9):C.GC_1055,(0,10):C.GC_1055,(0,6):C.GC_1051,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_1056,(0,4):C.GC_1055,(0,5):C.GC_1055,(0,0):C.GC_1051})

V_1893 = Vertex(name = 'V_1893',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_4044,(0,9):C.GC_4043,(0,10):C.GC_4043,(0,6):C.GC_4040,(0,1):C.GC_3706,(0,2):C.GC_1066,(0,3):C.GC_1065,(0,7):C.GC_4044,(0,4):C.GC_4043,(0,5):C.GC_4043,(0,0):C.GC_4040})

V_1894 = Vertex(name = 'V_1894',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_1895 = Vertex(name = 'V_1895',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3700})

V_1896 = Vertex(name = 'V_1896',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2399,(0,9):C.GC_2648,(0,7):C.GC_2647,(0,8):C.GC_2647,(0,4):C.GC_2646,(0,1):C.GC_2408,(0,5):C.GC_2605,(0,2):C.GC_2604,(0,3):C.GC_2604,(0,0):C.GC_2601})

V_1897 = Vertex(name = 'V_1897',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2403})

V_1898 = Vertex(name = 'V_1898',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3691,(0,9):C.GC_4042,(0,7):C.GC_4041,(0,8):C.GC_4041,(0,4):C.GC_4039,(0,1):C.GC_3703,(0,5):C.GC_3948,(0,2):C.GC_3947,(0,3):C.GC_3947,(0,0):C.GC_3944})

V_1899 = Vertex(name = 'V_1899',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3696})

V_1900 = Vertex(name = 'V_1900',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1621,(0,9):C.GC_1715,(0,7):C.GC_1714,(0,8):C.GC_1714,(0,4):C.GC_1713,(0,1):C.GC_1627,(0,5):C.GC_1788,(0,2):C.GC_1787,(0,3):C.GC_1787,(0,0):C.GC_1785})

V_1901 = Vertex(name = 'V_1901',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1624})

V_1902 = Vertex(name = 'V_1902',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_918,(0,9):C.GC_917,(0,10):C.GC_917,(0,6):C.GC_913,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_918,(0,4):C.GC_917,(0,5):C.GC_917,(0,0):C.GC_913})

V_1903 = Vertex(name = 'V_1903',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_2607,(0,9):C.GC_2606,(0,10):C.GC_2606,(0,6):C.GC_2602,(0,1):C.GC_2409,(0,2):C.GC_481,(0,3):C.GC_480,(0,7):C.GC_2607,(0,4):C.GC_2606,(0,5):C.GC_2606,(0,0):C.GC_2602})

V_1904 = Vertex(name = 'V_1904',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_1905 = Vertex(name = 'V_1905',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2405})

V_1906 = Vertex(name = 'V_1906',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_3692,(0,9):C.GC_3943,(0,7):C.GC_3942,(0,8):C.GC_3942,(0,4):C.GC_3941,(0,1):C.GC_3704,(0,5):C.GC_3950,(0,2):C.GC_3949,(0,3):C.GC_3949,(0,0):C.GC_3945})

V_1907 = Vertex(name = 'V_1907',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3698})

V_1908 = Vertex(name = 'V_1908',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_1622,(0,9):C.GC_1718,(0,7):C.GC_1717,(0,8):C.GC_1717,(0,4):C.GC_1716,(0,1):C.GC_1628,(0,5):C.GC_1790,(0,2):C.GC_1789,(0,3):C.GC_1789,(0,0):C.GC_1786})

V_1909 = Vertex(name = 'V_1909',
                particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1626})

V_1910 = Vertex(name = 'V_1910',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,6):C.GC_2401,(0,9):C.GC_2612,(0,7):C.GC_2611,(0,8):C.GC_2611,(0,4):C.GC_2610,(0,1):C.GC_2410,(0,5):C.GC_2609,(0,2):C.GC_2608,(0,3):C.GC_2608,(0,0):C.GC_2603})

V_1911 = Vertex(name = 'V_1911',
                particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2407})

V_1912 = Vertex(name = 'V_1912',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_25,(0,11):C.GC_938,(0,9):C.GC_937,(0,10):C.GC_937,(0,6):C.GC_933,(0,1):C.GC_40,(0,2):C.GC_37,(0,3):C.GC_14,(0,7):C.GC_938,(0,4):C.GC_937,(0,5):C.GC_937,(0,0):C.GC_933})

V_1913 = Vertex(name = 'V_1913',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF11, L.FFFF12, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
                couplings = {(0,8):C.GC_26,(0,11):C.GC_3952,(0,9):C.GC_3951,(0,10):C.GC_3951,(0,6):C.GC_3946,(0,1):C.GC_3705,(0,2):C.GC_830,(0,3):C.GC_829,(0,7):C.GC_3952,(0,4):C.GC_3951,(0,5):C.GC_3951,(0,0):C.GC_3946})

V_1914 = Vertex(name = 'V_1914',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_1915 = Vertex(name = 'V_1915',
                particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3701})

V_1916 = Vertex(name = 'V_1916',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_47,(2,4):C.GC_48,(0,5):C.GC_53,(0,0):C.GC_47,(2,0):C.GC_48,(1,3):C.GC_47})

V_1917 = Vertex(name = 'V_1917',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(3,3):C.GC_3690,(1,1):C.GC_3685,(3,1):C.GC_3690,(1,2):C.GC_54,(0,4):C.GC_3685,(2,4):C.GC_3690,(0,5):C.GC_54,(0,0):C.GC_3685,(2,0):C.GC_3690,(1,3):C.GC_3685})

V_1918 = Vertex(name = 'V_1918',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(3,3):C.GC_1064,(1,1):C.GC_1063,(3,1):C.GC_1064,(1,2):C.GC_1067,(0,4):C.GC_1063,(2,4):C.GC_1064,(0,5):C.GC_1067,(0,0):C.GC_1063,(2,0):C.GC_1064,(1,3):C.GC_1063})

V_1919 = Vertex(name = 'V_1919',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_1068,(0,1):C.GC_1068})

V_1920 = Vertex(name = 'V_1920',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3716,(0,1):C.GC_3716})

V_1921 = Vertex(name = 'V_1921',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3723,(0,1):C.GC_3723})

V_1922 = Vertex(name = 'V_1922',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3732,(0,1):C.GC_3732})

V_1923 = Vertex(name = 'V_1923',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3741,(0,1):C.GC_3741})

V_1924 = Vertex(name = 'V_1924',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2411,(0,3):C.GC_2411,(1,0):C.GC_2391,(3,0):C.GC_2395,(0,1):C.GC_2391,(2,1):C.GC_2395})

V_1925 = Vertex(name = 'V_1925',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2415,(0,1):C.GC_2415})

V_1926 = Vertex(name = 'V_1926',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2420,(0,1):C.GC_2420})

V_1927 = Vertex(name = 'V_1927',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2427,(0,1):C.GC_2427})

V_1928 = Vertex(name = 'V_1928',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3707,(0,3):C.GC_3707,(1,0):C.GC_3681,(3,0):C.GC_3686,(0,1):C.GC_3681,(2,1):C.GC_3686})

V_1929 = Vertex(name = 'V_1929',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3717,(0,1):C.GC_3717})

V_1930 = Vertex(name = 'V_1930',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3724,(0,1):C.GC_3724})

V_1931 = Vertex(name = 'V_1931',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3733,(0,1):C.GC_3733})

V_1932 = Vertex(name = 'V_1932',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1629,(0,3):C.GC_1629,(0,0):C.GC_1617,(2,0):C.GC_1619,(1,1):C.GC_1617,(3,1):C.GC_1619})

V_1933 = Vertex(name = 'V_1933',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1631,(0,1):C.GC_1631})

V_1934 = Vertex(name = 'V_1934',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1633,(0,1):C.GC_1633})

V_1935 = Vertex(name = 'V_1935',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1637,(0,1):C.GC_1637})

V_1936 = Vertex(name = 'V_1936',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_1009,(2,0):C.GC_1010,(1,3):C.GC_47,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_1009,(2,4):C.GC_1010,(0,5):C.GC_54})

V_1937 = Vertex(name = 'V_1937',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_2360,(2,2):C.GC_2361,(1,0):C.GC_1601,(2,0):C.GC_1603,(1,1):C.GC_1072,(0,3):C.GC_1074})

V_1938 = Vertex(name = 'V_1938',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3712,(0,1):C.GC_3721})

V_1939 = Vertex(name = 'V_1939',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3730,(0,1):C.GC_3737})

V_1940 = Vertex(name = 'V_1940',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3708,(0,2):C.GC_3718,(1,0):C.GC_3682,(2,0):C.GC_3687})

V_1941 = Vertex(name = 'V_1941',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3726,(0,1):C.GC_3734})

V_1942 = Vertex(name = 'V_1942',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1630,(0,3):C.GC_1630,(0,0):C.GC_1618,(2,0):C.GC_1620,(1,1):C.GC_1618,(3,1):C.GC_1620})

V_1943 = Vertex(name = 'V_1943',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1632,(0,1):C.GC_1632})

V_1944 = Vertex(name = 'V_1944',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1635,(0,1):C.GC_1635})

V_1945 = Vertex(name = 'V_1945',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1638,(0,1):C.GC_1638})

V_1946 = Vertex(name = 'V_1946',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2414,(0,2):C.GC_2419,(1,0):C.GC_2394,(2,0):C.GC_2398})

V_1947 = Vertex(name = 'V_1947',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2425,(0,1):C.GC_2431})

V_1948 = Vertex(name = 'V_1948',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_1049,(2,0):C.GC_1050,(1,3):C.GC_47,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_1049,(2,4):C.GC_1050,(0,5):C.GC_54})

V_1949 = Vertex(name = 'V_1949',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_3653,(2,2):C.GC_3654,(1,0):C.GC_1602,(2,0):C.GC_1604,(1,1):C.GC_1073,(0,3):C.GC_1075})

V_1950 = Vertex(name = 'V_1950',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2412,(0,1):C.GC_2417})

V_1951 = Vertex(name = 'V_1951',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2423,(0,1):C.GC_2429})

V_1952 = Vertex(name = 'V_1952',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2411,(0,3):C.GC_2411,(1,0):C.GC_2391,(3,0):C.GC_2395,(0,1):C.GC_2391,(2,1):C.GC_2395})

V_1953 = Vertex(name = 'V_1953',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2415,(0,1):C.GC_2415})

V_1954 = Vertex(name = 'V_1954',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2420,(0,1):C.GC_2420})

V_1955 = Vertex(name = 'V_1955',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2427,(0,1):C.GC_2427})

V_1956 = Vertex(name = 'V_1956',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_3717,(0,2):C.GC_3707,(0,0):C.GC_3681,(2,0):C.GC_3686})

V_1957 = Vertex(name = 'V_1957',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3733,(0,1):C.GC_3724})

V_1958 = Vertex(name = 'V_1958',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_2411,(0,2):C.GC_2415,(1,0):C.GC_2391,(2,0):C.GC_2395})

V_1959 = Vertex(name = 'V_1959',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2420,(0,1):C.GC_2427})

V_1960 = Vertex(name = 'V_1960',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3707,(0,3):C.GC_3707,(1,0):C.GC_3681,(3,0):C.GC_3686,(0,1):C.GC_3681,(2,1):C.GC_3686})

V_1961 = Vertex(name = 'V_1961',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3717,(0,1):C.GC_3717})

V_1962 = Vertex(name = 'V_1962',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3724,(0,1):C.GC_3724})

V_1963 = Vertex(name = 'V_1963',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3733,(0,1):C.GC_3733})

V_1964 = Vertex(name = 'V_1964',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1629,(0,3):C.GC_1629,(0,0):C.GC_1617,(2,0):C.GC_1619,(1,1):C.GC_1617,(3,1):C.GC_1619})

V_1965 = Vertex(name = 'V_1965',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1631,(0,1):C.GC_1631})

V_1966 = Vertex(name = 'V_1966',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1633,(0,1):C.GC_1633})

V_1967 = Vertex(name = 'V_1967',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1637,(0,1):C.GC_1637})

V_1968 = Vertex(name = 'V_1968',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
                lorentz = [ L.FFFF12, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1632,(0,2):C.GC_1630,(0,0):C.GC_1618,(2,0):C.GC_1620})

V_1969 = Vertex(name = 'V_1969',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1638,(0,1):C.GC_1635})

V_1970 = Vertex(name = 'V_1970',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,1):C.GC_1629,(0,2):C.GC_1631,(1,0):C.GC_1617,(2,0):C.GC_1619})

V_1971 = Vertex(name = 'V_1971',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1633,(0,1):C.GC_1637})

V_1972 = Vertex(name = 'V_1972',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(0,0):C.GC_47,(2,0):C.GC_48,(1,3):C.GC_47,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_47,(2,4):C.GC_48,(0,5):C.GC_53})

V_1973 = Vertex(name = 'V_1973',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(0,0):C.GC_478,(2,0):C.GC_479,(1,3):C.GC_478,(3,3):C.GC_479,(1,1):C.GC_478,(3,1):C.GC_479,(1,2):C.GC_54,(0,4):C.GC_478,(2,4):C.GC_479,(0,5):C.GC_54})

V_1974 = Vertex(name = 'V_1974',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_2392,(2,0):C.GC_2396,(1,3):C.GC_2392,(3,3):C.GC_2396,(1,1):C.GC_2392,(3,1):C.GC_2396,(1,2):C.GC_482,(0,4):C.GC_2392,(2,4):C.GC_2396,(0,5):C.GC_482})

V_1975 = Vertex(name = 'V_1975',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_483,(0,1):C.GC_483})

V_1976 = Vertex(name = 'V_1976',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2413,(0,1):C.GC_2413})

V_1977 = Vertex(name = 'V_1977',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2418,(0,1):C.GC_2418})

V_1978 = Vertex(name = 'V_1978',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2424,(0,1):C.GC_2424})

V_1979 = Vertex(name = 'V_1979',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2430,(0,1):C.GC_2430})

V_1980 = Vertex(name = 'V_1980',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3708,(0,3):C.GC_3708,(1,0):C.GC_3682,(3,0):C.GC_3687,(0,1):C.GC_3682,(2,1):C.GC_3687})

V_1981 = Vertex(name = 'V_1981',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3718,(0,1):C.GC_3718})

V_1982 = Vertex(name = 'V_1982',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3726,(0,1):C.GC_3726})

V_1983 = Vertex(name = 'V_1983',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3734,(0,1):C.GC_3734})

V_1984 = Vertex(name = 'V_1984',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF15, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2414,(0,3):C.GC_2414,(0,0):C.GC_2394,(2,0):C.GC_2398,(1,1):C.GC_2394,(3,1):C.GC_2398})

V_1985 = Vertex(name = 'V_1985',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2419,(0,1):C.GC_2419})

V_1986 = Vertex(name = 'V_1986',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2425,(0,1):C.GC_2425})

V_1987 = Vertex(name = 'V_1987',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2431,(0,1):C.GC_2431})

V_1988 = Vertex(name = 'V_1988',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_42,(0,0):C.GC_787,(2,0):C.GC_788,(1,3):C.GC_47,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_787,(2,4):C.GC_788,(0,5):C.GC_54})

V_1989 = Vertex(name = 'V_1989',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,4):C.GC_44,(0,5):C.GC_45,(1,2):C.GC_3683,(2,2):C.GC_3688,(1,0):C.GC_2393,(2,0):C.GC_2397,(1,1):C.GC_836,(0,3):C.GC_837})

V_1990 = Vertex(name = 'V_1990',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3709,(0,1):C.GC_3720})

V_1991 = Vertex(name = 'V_1991',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3729,(0,1):C.GC_3736})

V_1992 = Vertex(name = 'V_1992',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF13, L.FFFF16, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_3708,(0,3):C.GC_3708,(1,0):C.GC_3682,(3,0):C.GC_3687,(0,1):C.GC_3682,(2,1):C.GC_3687})

V_1993 = Vertex(name = 'V_1993',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3718,(0,1):C.GC_3718})

V_1994 = Vertex(name = 'V_1994',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3726,(0,1):C.GC_3726})

V_1995 = Vertex(name = 'V_1995',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3734,(0,1):C.GC_3734})

V_1996 = Vertex(name = 'V_1996',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_1630,(0,3):C.GC_1630,(0,0):C.GC_1618,(2,0):C.GC_1620,(1,1):C.GC_1618,(3,1):C.GC_1620})

V_1997 = Vertex(name = 'V_1997',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1632,(0,1):C.GC_1632})

V_1998 = Vertex(name = 'V_1998',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1635,(0,1):C.GC_1635})

V_1999 = Vertex(name = 'V_1999',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_1638,(0,1):C.GC_1638})

V_2000 = Vertex(name = 'V_2000',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_2414,(0,3):C.GC_2414,(0,0):C.GC_2394,(2,0):C.GC_2398,(1,1):C.GC_2394,(3,1):C.GC_2398})

V_2001 = Vertex(name = 'V_2001',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2419,(0,1):C.GC_2419})

V_2002 = Vertex(name = 'V_2002',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2425,(0,1):C.GC_2425})

V_2003 = Vertex(name = 'V_2003',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_2431,(0,1):C.GC_2431})

V_2004 = Vertex(name = 'V_2004',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_41,(0,7):C.GC_41,(0,0):C.GC_47,(2,0):C.GC_48,(1,3):C.GC_47,(3,3):C.GC_48,(1,1):C.GC_47,(3,1):C.GC_48,(1,2):C.GC_53,(0,4):C.GC_47,(2,4):C.GC_48,(0,5):C.GC_53})

V_2005 = Vertex(name = 'V_2005',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_42,(0,7):C.GC_42,(0,0):C.GC_3684,(2,0):C.GC_3689,(1,3):C.GC_3684,(3,3):C.GC_3689,(1,1):C.GC_3684,(3,1):C.GC_3689,(1,2):C.GC_54,(0,4):C.GC_3684,(2,4):C.GC_3689,(0,5):C.GC_54})

V_2006 = Vertex(name = 'V_2006',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,6):C.GC_44,(0,7):C.GC_44,(0,0):C.GC_827,(2,0):C.GC_828,(1,3):C.GC_827,(3,3):C.GC_828,(1,1):C.GC_827,(3,1):C.GC_828,(1,2):C.GC_831,(0,4):C.GC_827,(2,4):C.GC_828,(0,5):C.GC_831})

V_2007 = Vertex(name = 'V_2007',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF14, L.FFFF17, L.FFFF3, L.FFFF4 ],
                couplings = {(1,2):C.GC_45,(0,3):C.GC_45,(1,0):C.GC_832,(0,1):C.GC_832})

V_2008 = Vertex(name = 'V_2008',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3715,(0,1):C.GC_3715})

V_2009 = Vertex(name = 'V_2009',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3722,(0,1):C.GC_3722})

V_2010 = Vertex(name = 'V_2010',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3731,(0,1):C.GC_3731})

V_2011 = Vertex(name = 'V_2011',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(1,0):C.GC_3738,(0,1):C.GC_3738})

V_2012 = Vertex(name = 'V_2012',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2013 = Vertex(name = 'V_2013',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2014 = Vertex(name = 'V_2014',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2015 = Vertex(name = 'V_2015',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2016 = Vertex(name = 'V_2016',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2017 = Vertex(name = 'V_2017',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2018 = Vertex(name = 'V_2018',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2019 = Vertex(name = 'V_2019',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2020 = Vertex(name = 'V_2020',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2021 = Vertex(name = 'V_2021',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2022 = Vertex(name = 'V_2022',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2023 = Vertex(name = 'V_2023',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2024 = Vertex(name = 'V_2024',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2025 = Vertex(name = 'V_2025',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2026 = Vertex(name = 'V_2026',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2027 = Vertex(name = 'V_2027',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2028 = Vertex(name = 'V_2028',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_23,(0,0):C.GC_22})

V_2029 = Vertex(name = 'V_2029',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_24})

V_2030 = Vertex(name = 'V_2030',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_23})

V_2031 = Vertex(name = 'V_2031',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_2032 = Vertex(name = 'V_2032',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_2033 = Vertex(name = 'V_2033',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_2034 = Vertex(name = 'V_2034',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_23})

V_2035 = Vertex(name = 'V_2035',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_2036 = Vertex(name = 'V_2036',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_2037 = Vertex(name = 'V_2037',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_23,(0,1):C.GC_23})

V_2038 = Vertex(name = 'V_2038',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF3, L.FFFF4 ],
                couplings = {(0,0):C.GC_24,(0,1):C.GC_24})

V_2039 = Vertex(name = 'V_2039',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2040 = Vertex(name = 'V_2040',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_1066})

V_2041 = Vertex(name = 'V_2041',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_2042 = Vertex(name = 'V_2042',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3702})

V_2043 = Vertex(name = 'V_2043',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2044 = Vertex(name = 'V_2044',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_1066})

V_2045 = Vertex(name = 'V_2045',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_2046 = Vertex(name = 'V_2046',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3702})

V_2047 = Vertex(name = 'V_2047',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2048 = Vertex(name = 'V_2048',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_1066})

V_2049 = Vertex(name = 'V_2049',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3694})

V_2050 = Vertex(name = 'V_2050',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3702})

V_2051 = Vertex(name = 'V_2051',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2399})

V_2052 = Vertex(name = 'V_2052',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2402})

V_2053 = Vertex(name = 'V_2053',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2399})

V_2054 = Vertex(name = 'V_2054',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2402})

V_2055 = Vertex(name = 'V_2055',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2399})

V_2056 = Vertex(name = 'V_2056',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2402})

V_2057 = Vertex(name = 'V_2057',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3691})

V_2058 = Vertex(name = 'V_2058',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3695})

V_2059 = Vertex(name = 'V_2059',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3691})

V_2060 = Vertex(name = 'V_2060',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3695})

V_2061 = Vertex(name = 'V_2061',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3691})

V_2062 = Vertex(name = 'V_2062',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3695})

V_2063 = Vertex(name = 'V_2063',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1621})

V_2064 = Vertex(name = 'V_2064',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1623})

V_2065 = Vertex(name = 'V_2065',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1621})

V_2066 = Vertex(name = 'V_2066',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1623})

V_2067 = Vertex(name = 'V_2067',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1621})

V_2068 = Vertex(name = 'V_2068',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1623})

V_2069 = Vertex(name = 'V_2069',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2070 = Vertex(name = 'V_2070',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_481})

V_2071 = Vertex(name = 'V_2071',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_2072 = Vertex(name = 'V_2072',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2404})

V_2073 = Vertex(name = 'V_2073',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2074 = Vertex(name = 'V_2074',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_481})

V_2075 = Vertex(name = 'V_2075',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_2076 = Vertex(name = 'V_2076',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2404})

V_2077 = Vertex(name = 'V_2077',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2078 = Vertex(name = 'V_2078',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_481})

V_2079 = Vertex(name = 'V_2079',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2400})

V_2080 = Vertex(name = 'V_2080',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2404})

V_2081 = Vertex(name = 'V_2081',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3692})

V_2082 = Vertex(name = 'V_2082',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3697})

V_2083 = Vertex(name = 'V_2083',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3692})

V_2084 = Vertex(name = 'V_2084',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3697})

V_2085 = Vertex(name = 'V_2085',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3692})

V_2086 = Vertex(name = 'V_2086',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3697})

V_2087 = Vertex(name = 'V_2087',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1622})

V_2088 = Vertex(name = 'V_2088',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1625})

V_2089 = Vertex(name = 'V_2089',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1622})

V_2090 = Vertex(name = 'V_2090',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1625})

V_2091 = Vertex(name = 'V_2091',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1622})

V_2092 = Vertex(name = 'V_2092',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_1625})

V_2093 = Vertex(name = 'V_2093',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2401})

V_2094 = Vertex(name = 'V_2094',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2406})

V_2095 = Vertex(name = 'V_2095',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2401})

V_2096 = Vertex(name = 'V_2096',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2406})

V_2097 = Vertex(name = 'V_2097',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2401})

V_2098 = Vertex(name = 'V_2098',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2406})

V_2099 = Vertex(name = 'V_2099',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2100 = Vertex(name = 'V_2100',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_830})

V_2101 = Vertex(name = 'V_2101',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_2102 = Vertex(name = 'V_2102',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3699})

V_2103 = Vertex(name = 'V_2103',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2104 = Vertex(name = 'V_2104',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_830})

V_2105 = Vertex(name = 'V_2105',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_2106 = Vertex(name = 'V_2106',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3699})

V_2107 = Vertex(name = 'V_2107',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_37})

V_2108 = Vertex(name = 'V_2108',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_27,(0,0):C.GC_830})

V_2109 = Vertex(name = 'V_2109',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3693})

V_2110 = Vertex(name = 'V_2110',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3699})

V_2111 = Vertex(name = 'V_2111',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1143,(0,4):C.GC_1234,(0,2):C.GC_1233,(0,3):C.GC_1233,(0,0):C.GC_1196,(0,1):C.GC_1232})

V_2112 = Vertex(name = 'V_2112',
                particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1261,(0,4):C.GC_1285,(0,2):C.GC_1284,(0,3):C.GC_1284,(0,0):C.GC_1280,(0,1):C.GC_1283})

V_2113 = Vertex(name = 'V_2113',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1834,(0,4):C.GC_1902,(0,2):C.GC_1901,(0,3):C.GC_1901,(0,0):C.GC_1903,(0,1):C.GC_1900})

V_2114 = Vertex(name = 'V_2114',
                particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1971,(0,4):C.GC_1983,(0,2):C.GC_1982,(0,3):C.GC_1982,(0,0):C.GC_1984,(0,1):C.GC_1981})

V_2115 = Vertex(name = 'V_2115',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2720,(0,4):C.GC_2817,(0,2):C.GC_2816,(0,3):C.GC_2816,(0,0):C.GC_2776,(0,1):C.GC_2815})

V_2116 = Vertex(name = 'V_2116',
                particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2867,(0,4):C.GC_2896,(0,2):C.GC_2895,(0,3):C.GC_2895,(0,0):C.GC_2892,(0,1):C.GC_2894})

V_2117 = Vertex(name = 'V_2117',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1143,(0,4):C.GC_1237,(0,2):C.GC_1236,(0,3):C.GC_1236,(0,0):C.GC_1197,(0,1):C.GC_1235})

V_2118 = Vertex(name = 'V_2118',
                particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1261,(0,4):C.GC_1288,(0,2):C.GC_1287,(0,3):C.GC_1287,(0,0):C.GC_1281,(0,1):C.GC_1286})

V_2119 = Vertex(name = 'V_2119',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1834,(0,4):C.GC_1906,(0,2):C.GC_1905,(0,3):C.GC_1905,(0,0):C.GC_1907,(0,1):C.GC_1904})

V_2120 = Vertex(name = 'V_2120',
                particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1971,(0,4):C.GC_1987,(0,2):C.GC_1986,(0,3):C.GC_1986,(0,0):C.GC_1988,(0,1):C.GC_1985})

V_2121 = Vertex(name = 'V_2121',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2720,(0,4):C.GC_2820,(0,2):C.GC_2819,(0,3):C.GC_2819,(0,0):C.GC_2777,(0,1):C.GC_2818})

V_2122 = Vertex(name = 'V_2122',
                particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2867,(0,4):C.GC_2899,(0,2):C.GC_2898,(0,3):C.GC_2898,(0,0):C.GC_2893,(0,1):C.GC_2897})

V_2123 = Vertex(name = 'V_2123',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1143,(0,4):C.GC_1254,(0,2):C.GC_1253,(0,3):C.GC_1253,(0,0):C.GC_1212,(0,1):C.GC_1252})

V_2124 = Vertex(name = 'V_2124',
                particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1261,(0,4):C.GC_1291,(0,2):C.GC_1290,(0,3):C.GC_1290,(0,0):C.GC_1282,(0,1):C.GC_1289})

V_2125 = Vertex(name = 'V_2125',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1834,(0,4):C.GC_1955,(0,2):C.GC_1954,(0,3):C.GC_1954,(0,0):C.GC_1956,(0,1):C.GC_1953})

V_2126 = Vertex(name = 'V_2126',
                particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1971,(0,4):C.GC_2000,(0,2):C.GC_1999,(0,3):C.GC_1999,(0,0):C.GC_2001,(0,1):C.GC_1998})

V_2127 = Vertex(name = 'V_2127',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2720,(0,4):C.GC_2842,(0,2):C.GC_2841,(0,3):C.GC_2841,(0,0):C.GC_2839,(0,1):C.GC_2840})

V_2128 = Vertex(name = 'V_2128',
                particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2867,(0,4):C.GC_2903,(0,2):C.GC_2902,(0,3):C.GC_2902,(0,0):C.GC_2900,(0,1):C.GC_2901})

V_2129 = Vertex(name = 'V_2129',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1292,(0,4):C.GC_1396,(0,2):C.GC_1395,(0,3):C.GC_1395,(0,0):C.GC_1357,(0,1):C.GC_1394})

V_2130 = Vertex(name = 'V_2130',
                particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1428,(0,4):C.GC_1458,(0,2):C.GC_1457,(0,3):C.GC_1457,(0,0):C.GC_1453,(0,1):C.GC_1456})

V_2131 = Vertex(name = 'V_2131',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2008,(0,4):C.GC_2075,(0,2):C.GC_2074,(0,3):C.GC_2074,(0,0):C.GC_2114,(0,1):C.GC_2073})

V_2132 = Vertex(name = 'V_2132',
                particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2162,(0,4):C.GC_2177,(0,2):C.GC_2176,(0,3):C.GC_2176,(0,0):C.GC_2181,(0,1):C.GC_2175})

V_2133 = Vertex(name = 'V_2133',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3068,(0,4):C.GC_3168,(0,2):C.GC_3167,(0,3):C.GC_3167,(0,0):C.GC_3134,(0,1):C.GC_3166})

V_2134 = Vertex(name = 'V_2134',
                particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3231,(0,4):C.GC_3263,(0,2):C.GC_3262,(0,3):C.GC_3262,(0,0):C.GC_3259,(0,1):C.GC_3261})

V_2135 = Vertex(name = 'V_2135',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1292,(0,4):C.GC_1399,(0,2):C.GC_1398,(0,3):C.GC_1398,(0,0):C.GC_1358,(0,1):C.GC_1397})

V_2136 = Vertex(name = 'V_2136',
                particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1428,(0,4):C.GC_1461,(0,2):C.GC_1460,(0,3):C.GC_1460,(0,0):C.GC_1454,(0,1):C.GC_1459})

V_2137 = Vertex(name = 'V_2137',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2008,(0,4):C.GC_2078,(0,2):C.GC_2077,(0,3):C.GC_2077,(0,0):C.GC_2115,(0,1):C.GC_2076})

V_2138 = Vertex(name = 'V_2138',
                particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2162,(0,4):C.GC_2180,(0,2):C.GC_2179,(0,3):C.GC_2179,(0,0):C.GC_2182,(0,1):C.GC_2178})

V_2139 = Vertex(name = 'V_2139',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3068,(0,4):C.GC_3171,(0,2):C.GC_3170,(0,3):C.GC_3170,(0,0):C.GC_3135,(0,1):C.GC_3169})

V_2140 = Vertex(name = 'V_2140',
                particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3231,(0,4):C.GC_3266,(0,2):C.GC_3265,(0,3):C.GC_3265,(0,0):C.GC_3260,(0,1):C.GC_3264})

V_2141 = Vertex(name = 'V_2141',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1292,(0,4):C.GC_1421,(0,2):C.GC_1420,(0,3):C.GC_1420,(0,0):C.GC_1371,(0,1):C.GC_1419})

V_2142 = Vertex(name = 'V_2142',
                particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1428,(0,4):C.GC_1464,(0,2):C.GC_1463,(0,3):C.GC_1463,(0,0):C.GC_1455,(0,1):C.GC_1462})

V_2143 = Vertex(name = 'V_2143',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2008,(0,4):C.GC_2142,(0,2):C.GC_2141,(0,3):C.GC_2141,(0,0):C.GC_2143,(0,1):C.GC_2140})

V_2144 = Vertex(name = 'V_2144',
                particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2162,(0,4):C.GC_2194,(0,2):C.GC_2193,(0,3):C.GC_2193,(0,0):C.GC_2195,(0,1):C.GC_2192})

V_2145 = Vertex(name = 'V_2145',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3068,(0,4):C.GC_3204,(0,2):C.GC_3203,(0,3):C.GC_3203,(0,0):C.GC_3201,(0,1):C.GC_3202})

V_2146 = Vertex(name = 'V_2146',
                particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3231,(0,4):C.GC_3270,(0,2):C.GC_3269,(0,3):C.GC_3269,(0,0):C.GC_3267,(0,1):C.GC_3268})

V_2147 = Vertex(name = 'V_2147',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1465,(0,4):C.GC_1574,(0,2):C.GC_1573,(0,3):C.GC_1573,(0,0):C.GC_1524,(0,1):C.GC_1572})

V_2148 = Vertex(name = 'V_2148',
                particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1791,(0,4):C.GC_1827,(0,2):C.GC_1826,(0,3):C.GC_1826,(0,0):C.GC_1822,(0,1):C.GC_1825})

V_2149 = Vertex(name = 'V_2149',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2205,(0,4):C.GC_2285,(0,2):C.GC_2284,(0,3):C.GC_2284,(0,0):C.GC_2282,(0,1):C.GC_2283})

V_2150 = Vertex(name = 'V_2150',
                particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2366,(0,4):C.GC_2526,(0,2):C.GC_2525,(0,3):C.GC_2525,(0,0):C.GC_2523,(0,1):C.GC_2524})

V_2151 = Vertex(name = 'V_2151',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3498,(0,4):C.GC_3609,(0,2):C.GC_3608,(0,3):C.GC_3608,(0,0):C.GC_3558,(0,1):C.GC_3607})

V_2152 = Vertex(name = 'V_2152',
                particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3901,(0,4):C.GC_3937,(0,2):C.GC_3936,(0,3):C.GC_3936,(0,0):C.GC_3933,(0,1):C.GC_3935})

V_2153 = Vertex(name = 'V_2153',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1465,(0,4):C.GC_1577,(0,2):C.GC_1576,(0,3):C.GC_1576,(0,0):C.GC_1525,(0,1):C.GC_1575})

V_2154 = Vertex(name = 'V_2154',
                particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1791,(0,4):C.GC_1830,(0,2):C.GC_1829,(0,3):C.GC_1829,(0,0):C.GC_1823,(0,1):C.GC_1828})

V_2155 = Vertex(name = 'V_2155',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2205,(0,4):C.GC_2289,(0,2):C.GC_2288,(0,3):C.GC_2288,(0,0):C.GC_2286,(0,1):C.GC_2287})

V_2156 = Vertex(name = 'V_2156',
                particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2366,(0,4):C.GC_2539,(0,2):C.GC_2538,(0,3):C.GC_2538,(0,0):C.GC_2536,(0,1):C.GC_2537})

V_2157 = Vertex(name = 'V_2157',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3498,(0,4):C.GC_3612,(0,2):C.GC_3611,(0,3):C.GC_3611,(0,0):C.GC_3559,(0,1):C.GC_3610})

V_2158 = Vertex(name = 'V_2158',
                particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3901,(0,4):C.GC_3940,(0,2):C.GC_3939,(0,3):C.GC_3939,(0,0):C.GC_3934,(0,1):C.GC_3938})

V_2159 = Vertex(name = 'V_2159',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1465,(0,4):C.GC_1594,(0,2):C.GC_1593,(0,3):C.GC_1593,(0,0):C.GC_1544,(0,1):C.GC_1592})

V_2160 = Vertex(name = 'V_2160',
                particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_1791,(0,4):C.GC_1833,(0,2):C.GC_1832,(0,3):C.GC_1832,(0,0):C.GC_1824,(0,1):C.GC_1831})

V_2161 = Vertex(name = 'V_2161',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2205,(0,4):C.GC_2341,(0,2):C.GC_2340,(0,3):C.GC_2340,(0,0):C.GC_2338,(0,1):C.GC_2339})

V_2162 = Vertex(name = 'V_2162',
                particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_2366,(0,4):C.GC_2600,(0,2):C.GC_2599,(0,3):C.GC_2599,(0,0):C.GC_2597,(0,1):C.GC_2598})

V_2163 = Vertex(name = 'V_2163',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3498,(0,4):C.GC_3634,(0,2):C.GC_3633,(0,3):C.GC_3633,(0,0):C.GC_3631,(0,1):C.GC_3632})

V_2164 = Vertex(name = 'V_2164',
                particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF10, L.FFFF11, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4 ],
                couplings = {(0,5):C.GC_3901,(0,4):C.GC_3956,(0,2):C.GC_3955,(0,3):C.GC_3955,(0,0):C.GC_3953,(0,1):C.GC_3954})

V_2165 = Vertex(name = 'V_2165',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2166 = Vertex(name = 'V_2166',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_540})

V_2167 = Vertex(name = 'V_2167',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_2168 = Vertex(name = 'V_2168',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2658})

V_2169 = Vertex(name = 'V_2169',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2170 = Vertex(name = 'V_2170',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_540})

V_2171 = Vertex(name = 'V_2171',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_2172 = Vertex(name = 'V_2172',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2658})

V_2173 = Vertex(name = 'V_2173',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2174 = Vertex(name = 'V_2174',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_540})

V_2175 = Vertex(name = 'V_2175',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2657})

V_2176 = Vertex(name = 'V_2176',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2658})

V_2177 = Vertex(name = 'V_2177',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2928})

V_2178 = Vertex(name = 'V_2178',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2931})

V_2179 = Vertex(name = 'V_2179',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2928})

V_2180 = Vertex(name = 'V_2180',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2931})

V_2181 = Vertex(name = 'V_2181',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2928})

V_2182 = Vertex(name = 'V_2182',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2931})

V_2183 = Vertex(name = 'V_2183',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2929})

V_2184 = Vertex(name = 'V_2184',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2933})

V_2185 = Vertex(name = 'V_2185',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2929})

V_2186 = Vertex(name = 'V_2186',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2933})

V_2187 = Vertex(name = 'V_2187',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2929})

V_2188 = Vertex(name = 'V_2188',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_2933})

V_2189 = Vertex(name = 'V_2189',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3305})

V_2190 = Vertex(name = 'V_2190',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3309})

V_2191 = Vertex(name = 'V_2191',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3305})

V_2192 = Vertex(name = 'V_2192',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3309})

V_2193 = Vertex(name = 'V_2193',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3305})

V_2194 = Vertex(name = 'V_2194',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3309})

V_2195 = Vertex(name = 'V_2195',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2196 = Vertex(name = 'V_2196',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_723})

V_2197 = Vertex(name = 'V_2197',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_2198 = Vertex(name = 'V_2198',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3311})

V_2199 = Vertex(name = 'V_2199',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2200 = Vertex(name = 'V_2200',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_723})

V_2201 = Vertex(name = 'V_2201',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_2202 = Vertex(name = 'V_2202',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3311})

V_2203 = Vertex(name = 'V_2203',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2204 = Vertex(name = 'V_2204',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_723})

V_2205 = Vertex(name = 'V_2205',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3306})

V_2206 = Vertex(name = 'V_2206',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3311})

V_2207 = Vertex(name = 'V_2207',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3307})

V_2208 = Vertex(name = 'V_2208',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3313})

V_2209 = Vertex(name = 'V_2209',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3307})

V_2210 = Vertex(name = 'V_2210',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3313})

V_2211 = Vertex(name = 'V_2211',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3307})

V_2212 = Vertex(name = 'V_2212',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_3313})

V_2213 = Vertex(name = 'V_2213',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4063})

V_2214 = Vertex(name = 'V_2214',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4067})

V_2215 = Vertex(name = 'V_2215',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4063})

V_2216 = Vertex(name = 'V_2216',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4067})

V_2217 = Vertex(name = 'V_2217',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4063})

V_2218 = Vertex(name = 'V_2218',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4067})

V_2219 = Vertex(name = 'V_2219',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4064})

V_2220 = Vertex(name = 'V_2220',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4069})

V_2221 = Vertex(name = 'V_2221',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4064})

V_2222 = Vertex(name = 'V_2222',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4069})

V_2223 = Vertex(name = 'V_2223',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4064})

V_2224 = Vertex(name = 'V_2224',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4069})

V_2225 = Vertex(name = 'V_2225',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2226 = Vertex(name = 'V_2226',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_434})

V_2227 = Vertex(name = 'V_2227',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_2228 = Vertex(name = 'V_2228',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4071})

V_2229 = Vertex(name = 'V_2229',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2230 = Vertex(name = 'V_2230',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_434})

V_2231 = Vertex(name = 'V_2231',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_2232 = Vertex(name = 'V_2232',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4071})

V_2233 = Vertex(name = 'V_2233',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_25,(0,0):C.GC_21})

V_2234 = Vertex(name = 'V_2234',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF12, L.FFFF4 ],
                couplings = {(0,1):C.GC_26,(0,0):C.GC_434})

V_2235 = Vertex(name = 'V_2235',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4065})

V_2236 = Vertex(name = 'V_2236',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF4 ],
                couplings = {(0,0):C.GC_4071})

V_2237 = Vertex(name = 'V_2237',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1928,(2,0):C.GC_1931,(1,2):C.GC_1928,(3,2):C.GC_1931,(1,1):C.GC_1928,(3,1):C.GC_1931,(0,3):C.GC_1928,(2,3):C.GC_1931})

V_2238 = Vertex(name = 'V_2238',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2763,(2,0):C.GC_2766,(1,2):C.GC_1929,(3,2):C.GC_1932,(1,1):C.GC_2763,(3,1):C.GC_2766,(0,3):C.GC_1929,(2,3):C.GC_1932})

V_2239 = Vertex(name = 'V_2239',
                particles = [ P.s__tilde__, P.b, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1909,(2,0):C.GC_1912,(1,2):C.GC_1909,(3,2):C.GC_1912,(1,1):C.GC_2309,(3,1):C.GC_2312,(0,3):C.GC_2309,(2,3):C.GC_2312})

V_2240 = Vertex(name = 'V_2240',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2764,(2,0):C.GC_2767,(1,2):C.GC_2764,(3,2):C.GC_2767,(1,1):C.GC_2764,(3,1):C.GC_2767,(0,3):C.GC_2764,(2,3):C.GC_2767})

V_2241 = Vertex(name = 'V_2241',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2780,(2,0):C.GC_2783,(1,2):C.GC_2780,(3,2):C.GC_2783,(1,1):C.GC_3112,(3,1):C.GC_3115,(0,3):C.GC_3112,(2,3):C.GC_3115})

V_2242 = Vertex(name = 'V_2242',
                particles = [ P.d__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1351,(2,0):C.GC_1354,(1,2):C.GC_1351,(3,2):C.GC_1354,(1,1):C.GC_1351,(3,1):C.GC_1354,(0,3):C.GC_1351,(2,3):C.GC_1354})

V_2243 = Vertex(name = 'V_2243',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_3116,(2,0):C.GC_3119,(1,2):C.GC_1353,(3,2):C.GC_1356,(1,1):C.GC_3116,(3,1):C.GC_3119,(0,3):C.GC_1353,(2,3):C.GC_1356})

V_2244 = Vertex(name = 'V_2244',
                particles = [ P.d__tilde__, P.b, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1327,(2,0):C.GC_1330,(1,2):C.GC_1327,(3,2):C.GC_1330,(1,1):C.GC_1526,(3,1):C.GC_1529,(0,3):C.GC_1526,(2,3):C.GC_1529})

V_2245 = Vertex(name = 'V_2245',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_3118,(2,0):C.GC_3121,(1,2):C.GC_3118,(3,2):C.GC_3121,(1,1):C.GC_3118,(3,1):C.GC_3121,(0,3):C.GC_3118,(2,3):C.GC_3121})

V_2246 = Vertex(name = 'V_2246',
                particles = [ P.d__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_1512,(2,0):C.GC_1515,(1,2):C.GC_1512,(3,2):C.GC_1515,(1,1):C.GC_1512,(3,1):C.GC_1515,(0,3):C.GC_1512,(2,3):C.GC_1515})

V_2247 = Vertex(name = 'V_2247',
                particles = [ P.s__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2290,(2,0):C.GC_2293,(1,2):C.GC_1513,(3,2):C.GC_1516,(1,1):C.GC_2290,(3,1):C.GC_2293,(0,3):C.GC_1513,(2,3):C.GC_1516})

V_2248 = Vertex(name = 'V_2248',
                particles = [ P.s__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF12, L.FFFF13, L.FFFF15, L.FFFF16 ],
                couplings = {(0,0):C.GC_2291,(2,0):C.GC_2294,(1,2):C.GC_2291,(3,2):C.GC_2294,(1,1):C.GC_2291,(3,1):C.GC_2294,(0,3):C.GC_2291,(2,3):C.GC_2294})

V_2249 = Vertex(name = 'V_2249',
                particles = [ P.a, P.a, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_207})

V_2250 = Vertex(name = 'V_2250',
                particles = [ P.g, P.g, P.H1 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS2, L.VVS3, L.VVS4, L.VVS5 ],
                couplings = {(0,0):C.GC_208,(0,2):C.GC_221,(0,1):C.GC_217,(0,3):C.GC_212})

V_2251 = Vertex(name = 'V_2251',
                particles = [ P.a, P.Z, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_211})

V_2252 = Vertex(name = 'V_2252',
                particles = [ P.a, P.Z1, P.H ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_211})

V_2253 = Vertex(name = 'V_2253',
                particles = [ P.a, P.Z1, P.H1 ],
                color = [ '1' ],
                lorentz = [ L.VVS2 ],
                couplings = {(0,0):C.GC_225})

V_2254 = Vertex(name = 'V_2254',
                particles = [ P.g, P.g, P.g, P.H1 ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVVS3, L.VVVS4, L.VVVS5, L.VVVS6, L.VVVS7 ],
                couplings = {(0,2):C.GC_213,(0,4):C.GC_222,(0,3):C.GC_218,(0,1):C.GC_215,(0,0):C.GC_209})

V_2255 = Vertex(name = 'V_2255',
                particles = [ P.g, P.g, P.g, P.g, P.H1 ],
                color = [ 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)' ],
                lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS18, L.VVVVS2, L.VVVVS20, L.VVVVS3, L.VVVVS5, L.VVVVS7, L.VVVVS8 ],
                couplings = {(2,5):C.GC_214,(2,8):C.GC_223,(1,4):C.GC_214,(1,10):C.GC_223,(2,6):C.GC_220,(0,11):C.GC_216,(0,12):C.GC_224,(1,7):C.GC_220,(0,3):C.GC_219,(1,2):C.GC_216,(2,1):C.GC_216,(0,9):C.GC_214,(1,13):C.GC_210,(0,0):C.GC_210,(2,14):C.GC_210})

