# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Fri 8 Jan 2021 10:13:04


from .object_library import all_vertices, Vertex
from . import particles as P
from . import couplings as C
from . import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
             couplings = {(0,1):C.GC_723,(0,0):C.GC_779,(0,5):C.GC_460,(0,4):C.GC_459,(0,2):C.GC_3,(0,3):C.GC_778})

V_2 = Vertex(name = 'V_2',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_806})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_726})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_736})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV7, L.VVV9 ],
             couplings = {(0,1):C.GC_780,(0,0):C.GC_722,(0,5):C.GC_259,(0,4):C.GC_258,(0,3):C.GC_345,(0,2):C.GC_720})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_775})

V_7 = Vertex(name = 'V_7',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_824})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV5 ],
             couplings = {(0,0):C.GC_781})

V_9 = Vertex(name = 'V_9',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV3, L.VVV5, L.VVV7, L.VVV8 ],
             couplings = {(0,0):C.GC_729,(0,3):C.GC_60,(0,2):C.GC_59,(0,1):C.GC_7})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
              couplings = {(0,7):C.GC_287,(1,6):C.GC_287,(2,5):C.GC_287,(0,4):C.GC_286,(1,3):C.GC_286,(2,2):C.GC_286,(1,8):C.GC_8,(0,0):C.GC_8,(2,1):C.GC_8})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV2, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV25, L.VVVVV28, L.VVVVV29, L.VVVVV3, L.VVVVV30, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV37, L.VVVVV4, L.VVVVV40, L.VVVVV41, L.VVVVV42, L.VVVVV43, L.VVVVV44, L.VVVVV46, L.VVVVV47, L.VVVVV48, L.VVVVV49, L.VVVVV5, L.VVVVV50, L.VVVVV51, L.VVVVV53, L.VVVVV54, L.VVVVV6, L.VVVVV7, L.VVVVV9 ],
              couplings = {(27,37):C.GC_294,(24,8):C.GC_295,(21,12):C.GC_294,(18,11):C.GC_295,(15,9):C.GC_294,(12,27):C.GC_294,(28,42):C.GC_294,(25,15):C.GC_295,(22,14):C.GC_294,(9,16):C.GC_294,(6,13):C.GC_295,(3,43):C.GC_295,(29,0):C.GC_295,(19,20):C.GC_294,(16,18):C.GC_295,(10,17):C.GC_294,(7,21):C.GC_295,(0,44):C.GC_294,(26,10):C.GC_294,(20,1):C.GC_295,(13,24):C.GC_294,(11,2):C.GC_295,(4,22):C.GC_294,(1,23):C.GC_294,(23,19):C.GC_295,(17,4):C.GC_294,(14,25):C.GC_295,(8,3):C.GC_294,(5,28):C.GC_295,(2,26):C.GC_295,(24,29):C.GC_293,(21,30):C.GC_292,(18,30):C.GC_293,(15,29):C.GC_292,(28,6):C.GC_293,(22,34):C.GC_293,(9,34):C.GC_292,(3,6):C.GC_292,(29,7):C.GC_293,(16,35):C.GC_293,(10,35):C.GC_292,(0,7):C.GC_292,(26,39):C.GC_292,(20,38):C.GC_292,(4,38):C.GC_293,(1,39):C.GC_293,(25,33):C.GC_293,(6,33):C.GC_292,(19,36):C.GC_293,(7,36):C.GC_292,(23,41):C.GC_292,(17,40):C.GC_292,(5,40):C.GC_293,(2,41):C.GC_293,(27,5):C.GC_293,(12,5):C.GC_292,(13,31):C.GC_293,(11,31):C.GC_292,(14,32):C.GC_292,(8,32):C.GC_293})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV19, L.VVVVVV2, L.VVVVVV20, L.VVVVVV21, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV26, L.VVVVVV27, L.VVVVVV28, L.VVVVVV29, L.VVVVVV3, L.VVVVVV30, L.VVVVVV31, L.VVVVVV32, L.VVVVVV33, L.VVVVVV34, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV38, L.VVVVVV39, L.VVVVVV4, L.VVVVVV40, L.VVVVVV41, L.VVVVVV42, L.VVVVVV43, L.VVVVVV44, L.VVVVVV45, L.VVVVVV46, L.VVVVVV47, L.VVVVVV48, L.VVVVVV49, L.VVVVVV5, L.VVVVVV50, L.VVVVVV51, L.VVVVVV52, L.VVVVVV54, L.VVVVVV55, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV59, L.VVVVVV6, L.VVVVVV60, L.VVVVVV61, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
              couplings = {(41,58):C.GC_300,(47,59):C.GC_299,(53,7):C.GC_300,(35,57):C.GC_299,(46,14):C.GC_300,(52,17):C.GC_299,(34,2):C.GC_300,(40,10):C.GC_299,(51,37):C.GC_300,(33,4):C.GC_299,(39,21):C.GC_300,(45,30):C.GC_299,(17,57):C.GC_300,(23,2):C.GC_299,(29,4):C.GC_300,(11,58):C.GC_299,(22,10):C.GC_300,(28,21):C.GC_299,(10,59):C.GC_300,(16,14):C.GC_299,(27,30):C.GC_300,(9,7):C.GC_299,(15,17):C.GC_300,(21,37):C.GC_299,(59,0):C.GC_300,(65,11):C.GC_299,(71,44):C.GC_300,(64,12):C.GC_300,(70,23):C.GC_299,(58,16):C.GC_299,(69,31):C.GC_300,(57,19):C.GC_300,(63,39):C.GC_299,(5,0):C.GC_299,(20,16):C.GC_300,(26,19):C.GC_299,(4,11):C.GC_300,(14,12):C.GC_299,(25,39):C.GC_300,(3,44):C.GC_299,(13,23):C.GC_300,(19,31):C.GC_299,(77,22):C.GC_299,(83,33):C.GC_300,(76,1):C.GC_300,(82,8):C.GC_299,(81,40):C.GC_300,(75,35):C.GC_299,(2,22):C.GC_300,(8,1):C.GC_299,(24,35):C.GC_300,(1,33):C.GC_299,(7,8):C.GC_300,(18,40):C.GC_299,(89,54):C.GC_300,(88,6):C.GC_299,(87,25):C.GC_300,(0,54):C.GC_299,(6,6):C.GC_300,(12,25):C.GC_299,(62,15):C.GC_300,(68,18):C.GC_299,(56,13):C.GC_299,(67,38):C.GC_300,(55,24):C.GC_300,(61,32):C.GC_299,(44,13):C.GC_300,(50,24):C.GC_299,(38,15):C.GC_299,(49,32):C.GC_300,(37,18):C.GC_300,(43,38):C.GC_299,(74,3):C.GC_300,(80,5):C.GC_299,(79,34):C.GC_300,(73,42):C.GC_299,(32,3):C.GC_299,(48,42):C.GC_300,(31,5):C.GC_300,(42,34):C.GC_299,(86,9):C.GC_299,(85,20):C.GC_300,(30,9):C.GC_300,(36,20):C.GC_299,(78,41):C.GC_300,(72,36):C.GC_299,(66,36):C.GC_300,(60,41):C.GC_299,(65,43):C.GC_297,(71,46):C.GC_298,(77,46):C.GC_297,(83,43):C.GC_298,(41,28):C.GC_297,(53,50):C.GC_297,(76,50):C.GC_298,(88,28):C.GC_298,(35,29):C.GC_297,(52,53):C.GC_297,(64,53):C.GC_298,(87,29):C.GC_298,(34,52):C.GC_298,(40,51):C.GC_298,(69,51):C.GC_297,(81,52):C.GC_297,(17,29):C.GC_298,(23,52):C.GC_297,(80,52):C.GC_298,(86,29):C.GC_297,(11,28):C.GC_298,(22,51):C.GC_297,(68,51):C.GC_298,(85,28):C.GC_297,(9,50):C.GC_298,(15,53):C.GC_298,(61,53):C.GC_297,(73,50):C.GC_297,(4,43):C.GC_298,(14,53):C.GC_297,(49,53):C.GC_298,(78,43):C.GC_297,(3,46):C.GC_297,(19,51):C.GC_298,(37,51):C.GC_297,(72,46):C.GC_298,(2,46):C.GC_298,(8,50):C.GC_297,(48,50):C.GC_298,(66,46):C.GC_297,(1,43):C.GC_297,(18,52):C.GC_298,(31,52):C.GC_297,(60,43):C.GC_298,(6,28):C.GC_297,(12,29):C.GC_297,(30,29):C.GC_298,(36,28):C.GC_298,(47,48):C.GC_297,(82,48):C.GC_298,(46,55):C.GC_297,(70,55):C.GC_298,(33,56):C.GC_298,(39,49):C.GC_298,(63,49):C.GC_297,(75,56):C.GC_297,(29,56):C.GC_297,(74,56):C.GC_298,(28,49):C.GC_297,(62,49):C.GC_298,(10,48):C.GC_298,(16,55):C.GC_298,(67,55):C.GC_297,(79,48):C.GC_297,(25,49):C.GC_298,(38,49):C.GC_297,(13,55):C.GC_297,(43,55):C.GC_298,(24,56):C.GC_298,(32,56):C.GC_297,(7,48):C.GC_297,(42,48):C.GC_298,(84,26):C.GC_300,(54,26):C.GC_299,(59,27):C.GC_297,(89,27):C.GC_298,(51,45):C.GC_297,(58,45):C.GC_298,(21,45):C.GC_298,(55,45):C.GC_297,(5,27):C.GC_298,(20,45):C.GC_297,(50,45):C.GC_298,(84,27):C.GC_297,(0,27):C.GC_297,(54,27):C.GC_298,(45,47):C.GC_298,(57,47):C.GC_297,(27,47):C.GC_297,(56,47):C.GC_298,(26,47):C.GC_298,(44,47):C.GC_297})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_462,(0,0):C.GC_461,(0,2):C.GC_5})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_807})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_728})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_744})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_782})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
              couplings = {(0,2):C.GC_280,(0,1):C.GC_279,(0,0):C.GC_346})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_811})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_825})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_826})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_784})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV16, L.VVVVV8 ],
              couplings = {(0,1):C.GC_464,(0,0):C.GC_463})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_408,(0,0):C.GC_406,(0,2):C.GC_315})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_810})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_740})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV26, L.VVVVV55 ],
              couplings = {(0,0):C.GC_283,(0,1):C.GC_282})

V_28 = Vertex(name = 'V_28',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVV32, L.VVVVV57 ],
              couplings = {(0,0):C.GC_413,(0,1):C.GC_411})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_415})

V_30 = Vertex(name = 'V_30',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_409,(0,0):C.GC_407,(0,2):C.GC_317})

V_31 = Vertex(name = 'V_31',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_745})

V_32 = Vertex(name = 'V_32',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_813})

V_33 = Vertex(name = 'V_33',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_746})

V_34 = Vertex(name = 'V_34',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_783})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV38, L.VVVVV45 ],
              couplings = {(0,0):C.GC_414,(0,1):C.GC_412})

V_36 = Vertex(name = 'V_36',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV27, L.VVVVV52 ],
              couplings = {(0,0):C.GC_323,(0,1):C.GC_321})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV62 ],
              couplings = {(0,0):C.GC_325})

V_38 = Vertex(name = 'V_38',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVVV53 ],
              couplings = {(0,0):C.GC_313})

V_39 = Vertex(name = 'V_39',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVVV39, L.VVVVV56 ],
              couplings = {(0,0):C.GC_324,(0,1):C.GC_322})

V_40 = Vertex(name = 'V_40',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_236,(0,1):C.GC_235})

V_41 = Vertex(name = 'V_41',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_455,(0,1):C.GC_452})

V_42 = Vertex(name = 'V_42',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_473,(0,1):C.GC_472})

V_43 = Vertex(name = 'V_43',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_564,(0,1):C.GC_476})

V_44 = Vertex(name = 'V_44',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_699,(0,1):C.GC_563})

V_45 = Vertex(name = 'V_45',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_706,(0,1):C.GC_696})

V_46 = Vertex(name = 'V_46',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_705})

V_47 = Vertex(name = 'V_47',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_65,(0,1):C.GC_64})

V_48 = Vertex(name = 'V_48',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
              couplings = {(0,0):C.GC_540,(0,1):C.GC_477,(0,3):C.GC_490,(0,2):C.GC_486,(0,4):C.GC_481})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_539})

V_50 = Vertex(name = 'V_50',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_67,(0,2):C.GC_66,(0,1):C.GC_314})

V_51 = Vertex(name = 'V_51',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_737})

V_52 = Vertex(name = 'V_52',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_738})

V_53 = Vertex(name = 'V_53',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_809})

V_54 = Vertex(name = 'V_54',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_739})

V_55 = Vertex(name = 'V_55',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_542,(0,2):C.GC_541,(0,1):C.GC_604})

V_56 = Vertex(name = 'V_56',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_795})

V_57 = Vertex(name = 'V_57',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_796})

V_58 = Vertex(name = 'V_58',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_831})

V_59 = Vertex(name = 'V_59',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_797})

V_60 = Vertex(name = 'V_60',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_475,(0,1):C.GC_474})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_450,(0,1):C.GC_449})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS4 ],
              couplings = {(0,0):C.GC_456,(0,1):C.GC_451})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_802,(0,1):C.GC_480})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_694,(0,1):C.GC_801})

V_65 = Vertex(name = 'V_65',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS4 ],
              couplings = {(0,0):C.GC_700,(0,1):C.GC_693})

V_66 = Vertex(name = 'V_66',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_695})

V_67 = Vertex(name = 'V_67',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_238,(0,2):C.GC_237,(0,1):C.GC_316})

V_68 = Vertex(name = 'V_68',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_454,(0,2):C.GC_453,(0,1):C.GC_741})

V_69 = Vertex(name = 'V_69',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_471,(0,2):C.GC_470,(0,1):C.GC_742})

V_70 = Vertex(name = 'V_70',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_812})

V_71 = Vertex(name = 'V_71',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_743})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_566,(0,2):C.GC_565,(0,1):C.GC_605})

V_73 = Vertex(name = 'V_73',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_698,(0,2):C.GC_697,(0,1):C.GC_798})

V_74 = Vertex(name = 'V_74',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_704,(0,2):C.GC_703,(0,1):C.GC_799})

V_75 = Vertex(name = 'V_75',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_832})

V_76 = Vertex(name = 'V_76',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_800})

V_77 = Vertex(name = 'V_77',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3, L.VVVSS6 ],
              couplings = {(0,0):C.GC_289,(0,1):C.GC_288})

V_78 = Vertex(name = 'V_78',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS10, L.VVVS3, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
              couplings = {(0,1):C.GC_597,(0,4):C.GC_482,(0,0):C.GC_491,(0,5):C.GC_487,(0,3):C.GC_484,(0,2):C.GC_478})

V_79 = Vertex(name = 'V_79',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS6 ],
              couplings = {(0,0):C.GC_596})

V_80 = Vertex(name = 'V_80',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS1, L.VVVSS3, L.VVVSS4, L.VVVSS6 ],
              couplings = {(0,1):C.GC_275,(0,0):C.GC_399,(0,3):C.GC_272,(0,2):C.GC_398})

V_81 = Vertex(name = 'V_81',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
              couplings = {(0,1):C.GC_589,(0,0):C.GC_667,(0,3):C.GC_586,(0,2):C.GC_666})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2, L.VVVSS3, L.VVVSS5, L.VVVSS6 ],
              couplings = {(0,1):C.GC_400,(0,0):C.GC_274,(0,3):C.GC_397,(0,2):C.GC_273})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
              couplings = {(0,1):C.GC_668,(0,0):C.GC_588,(0,3):C.GC_665,(0,2):C.GC_587})

V_84 = Vertex(name = 'V_84',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
              couplings = {(0,0):C.GC_9,(0,2):C.GC_62,(0,1):C.GC_63})

V_85 = Vertex(name = 'V_85',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_715})

V_86 = Vertex(name = 'V_86',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_730})

V_87 = Vertex(name = 'V_87',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_731})

V_88 = Vertex(name = 'V_88',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_808})

V_89 = Vertex(name = 'V_89',
              particles = [ P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_732})

V_90 = Vertex(name = 'V_90',
              particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSSS1 ],
              couplings = {(0,0):C.GC_61})

V_91 = Vertex(name = 'V_91',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
              couplings = {(0,0):C.GC_513,(0,2):C.GC_537,(0,1):C.GC_538})

V_92 = Vertex(name = 'V_92',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_791})

V_93 = Vertex(name = 'V_93',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_792})

V_94 = Vertex(name = 'V_94',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_793})

V_95 = Vertex(name = 'V_95',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_830})

V_96 = Vertex(name = 'V_96',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_794})

V_97 = Vertex(name = 'V_97',
              particles = [ P.H, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSSSS1 ],
              couplings = {(0,0):C.GC_536})

V_98 = Vertex(name = 'V_98',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_296,(0,0):C.GC_296,(2,2):C.GC_296})

V_99 = Vertex(name = 'V_99',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS17, L.VVVVS19, L.VVVVS2, L.VVVVS3, L.VVVVS4, L.VVVVS7, L.VVVVS8 ],
              couplings = {(2,5):C.GC_483,(2,8):C.GC_492,(1,4):C.GC_483,(1,9):C.GC_492,(2,6):C.GC_489,(0,11):C.GC_485,(0,12):C.GC_493,(1,7):C.GC_489,(0,3):C.GC_488,(1,2):C.GC_485,(2,1):C.GC_485,(0,10):C.GC_483,(1,13):C.GC_479,(0,0):C.GC_479,(2,14):C.GC_479})

V_100 = Vertex(name = 'V_100',
               particles = [ P.g, P.g, P.g, P.g, P.H ],
               color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVS1, L.VVVVS7, L.VVVVS8 ],
               couplings = {(1,1):C.GC_600,(0,0):C.GC_600,(2,2):C.GC_600})

V_101 = Vertex(name = 'V_101',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_281})

V_102 = Vertex(name = 'V_102',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_593})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_318})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_606})

V_105 = Vertex(name = 'V_105',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_410})

V_106 = Vertex(name = 'V_106',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS9 ],
               couplings = {(0,0):C.GC_674})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_319})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_607})

V_109 = Vertex(name = 'V_109',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_320})

V_110 = Vertex(name = 'V_110',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6 ],
               couplings = {(0,0):C.GC_608})

V_111 = Vertex(name = 'V_111',
               particles = [ P.H, P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_305})

V_112 = Vertex(name = 'V_112',
               particles = [ P.H, P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_310})

V_113 = Vertex(name = 'V_113',
               particles = [ P.H, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_311})

V_114 = Vertex(name = 'V_114',
               particles = [ P.H1, P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSSS1 ],
               couplings = {(0,0):C.GC_312})

V_115 = Vertex(name = 'V_115',
               particles = [ P.H, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_601})

V_116 = Vertex(name = 'V_116',
               particles = [ P.H, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_602})

V_117 = Vertex(name = 'V_117',
               particles = [ P.H1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.SSS1 ],
               couplings = {(0,0):C.GC_603})

V_118 = Vertex(name = 'V_118',
               particles = [ P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_302})

V_119 = Vertex(name = 'V_119',
               particles = [ P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_307})

V_120 = Vertex(name = 'V_120',
               particles = [ P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_302})

V_121 = Vertex(name = 'V_121',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_326})

V_122 = Vertex(name = 'V_122',
               particles = [ P.W__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_330})

V_123 = Vertex(name = 'V_123',
               particles = [ P.W__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_334})

V_124 = Vertex(name = 'V_124',
               particles = [ P.W__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_609})

V_125 = Vertex(name = 'V_125',
               particles = [ P.W__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_611})

V_126 = Vertex(name = 'V_126',
               particles = [ P.a, P.a, P.W__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_303})

V_127 = Vertex(name = 'V_127',
               particles = [ P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_419})

V_128 = Vertex(name = 'V_128',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_423})

V_129 = Vertex(name = 'V_129',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_330})

V_130 = Vertex(name = 'V_130',
               particles = [ P.W1__minus__, P.W1__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_334})

V_131 = Vertex(name = 'V_131',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_338})

V_132 = Vertex(name = 'V_132',
               particles = [ P.W1__minus__, P.W1__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_611})

V_133 = Vertex(name = 'V_133',
               particles = [ P.W1__minus__, P.W1__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_613})

V_134 = Vertex(name = 'V_134',
               particles = [ P.a, P.a, P.W1__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_308})

V_135 = Vertex(name = 'V_135',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_423})

V_136 = Vertex(name = 'V_136',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_426})

V_137 = Vertex(name = 'V_137',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_331})

V_138 = Vertex(name = 'V_138',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_335})

V_139 = Vertex(name = 'V_139',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_339})

V_140 = Vertex(name = 'V_140',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_326})

V_141 = Vertex(name = 'V_141',
               particles = [ P.W__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_330})

V_142 = Vertex(name = 'V_142',
               particles = [ P.W__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_609})

V_143 = Vertex(name = 'V_143',
               particles = [ P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_419})

V_144 = Vertex(name = 'V_144',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_326})

V_145 = Vertex(name = 'V_145',
               particles = [ P.W1__minus__, P.W__plus__, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_330})

V_146 = Vertex(name = 'V_146',
               particles = [ P.W1__minus__, P.W__plus__, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_334})

V_147 = Vertex(name = 'V_147',
               particles = [ P.W1__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_609})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W1__minus__, P.W__plus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_611})

V_149 = Vertex(name = 'V_149',
               particles = [ P.a, P.a, P.W1__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_303})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_419})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVV5 ],
               couplings = {(0,0):C.GC_423})

V_152 = Vertex(name = 'V_152',
               particles = [ P.W__minus__, P.W__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_327})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_331})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W1__minus__, P.W1__minus__, P.W1__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_335})

V_155 = Vertex(name = 'V_155',
               particles = [ P.W__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_327})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W1__minus__, P.W1__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_331})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_420})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_424})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_420})

V_160 = Vertex(name = 'V_160',
               particles = [ P.Z, P.Z, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_328})

V_161 = Vertex(name = 'V_161',
               particles = [ P.Z, P.Z, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_332})

V_162 = Vertex(name = 'V_162',
               particles = [ P.Z, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_610})

V_163 = Vertex(name = 'V_163',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_329})

V_164 = Vertex(name = 'V_164',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_333})

V_165 = Vertex(name = 'V_165',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_329})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.W__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_424})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.W1__minus__, P.W1__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_427})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_420})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.W1__minus__, P.W__plus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_424})

V_170 = Vertex(name = 'V_170',
               particles = [ P.Z, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_328})

V_171 = Vertex(name = 'V_171',
               particles = [ P.Z, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_332})

V_172 = Vertex(name = 'V_172',
               particles = [ P.Z, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_336})

V_173 = Vertex(name = 'V_173',
               particles = [ P.Z, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_610})

V_174 = Vertex(name = 'V_174',
               particles = [ P.Z, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_612})

V_175 = Vertex(name = 'V_175',
               particles = [ P.W__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_333})

V_176 = Vertex(name = 'V_176',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_337})

V_177 = Vertex(name = 'V_177',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_329})

V_178 = Vertex(name = 'V_178',
               particles = [ P.W1__minus__, P.W__plus__, P.Z, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_333})

V_179 = Vertex(name = 'V_179',
               particles = [ P.Z1, P.Z1, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_332})

V_180 = Vertex(name = 'V_180',
               particles = [ P.Z1, P.Z1, P.H, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_336})

V_181 = Vertex(name = 'V_181',
               particles = [ P.Z1, P.Z1, P.H1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVSS3 ],
               couplings = {(0,0):C.GC_340})

V_182 = Vertex(name = 'V_182',
               particles = [ P.Z1, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_612})

V_183 = Vertex(name = 'V_183',
               particles = [ P.Z1, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS3 ],
               couplings = {(0,0):C.GC_614})

V_184 = Vertex(name = 'V_184',
               particles = [ P.W__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_337})

V_185 = Vertex(name = 'V_185',
               particles = [ P.W1__minus__, P.W1__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_341})

V_186 = Vertex(name = 'V_186',
               particles = [ P.W__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_333})

V_187 = Vertex(name = 'V_187',
               particles = [ P.W1__minus__, P.W__plus__, P.Z1, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_337})

V_188 = Vertex(name = 'V_188',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_546,(0,1):C.GC_545})

V_189 = Vertex(name = 'V_189',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_803,(0,2):C.GC_678,(0,1):C.GC_677})

V_190 = Vertex(name = 'V_190',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_724})

V_191 = Vertex(name = 'V_191',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_733})

V_192 = Vertex(name = 'V_192',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_776})

V_193 = Vertex(name = 'V_193',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_1021,(0,1):C.GC_1020})

V_194 = Vertex(name = 'V_194',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_803,(0,2):C.GC_1037,(0,1):C.GC_1036})

V_195 = Vertex(name = 'V_195',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_724})

V_196 = Vertex(name = 'V_196',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_733})

V_197 = Vertex(name = 'V_197',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_776})

V_198 = Vertex(name = 'V_198',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_1,(0,2):C.GC_1138,(0,1):C.GC_1137})

V_199 = Vertex(name = 'V_199',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_803,(0,2):C.GC_1154,(0,1):C.GC_1153})

V_200 = Vertex(name = 'V_200',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_724})

V_201 = Vertex(name = 'V_201',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_733})

V_202 = Vertex(name = 'V_202',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_776})

V_203 = Vertex(name = 'V_203',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_552,(0,1):C.GC_549})

V_204 = Vertex(name = 'V_204',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_805,(0,2):C.GC_688,(0,1):C.GC_685})

V_205 = Vertex(name = 'V_205',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_727})

V_206 = Vertex(name = 'V_206',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_735})

V_207 = Vertex(name = 'V_207',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_778})

V_208 = Vertex(name = 'V_208',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_553,(0,1):C.GC_550})

V_209 = Vertex(name = 'V_209',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_805,(0,2):C.GC_689,(0,1):C.GC_686})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_727})

V_211 = Vertex(name = 'V_211',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_735})

V_212 = Vertex(name = 'V_212',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_778})

V_213 = Vertex(name = 'V_213',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_4,(0,2):C.GC_554,(0,1):C.GC_551})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_805,(0,2):C.GC_690,(0,1):C.GC_687})

V_215 = Vertex(name = 'V_215',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_727})

V_216 = Vertex(name = 'V_216',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_735})

V_217 = Vertex(name = 'V_217',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_778})

V_218 = Vertex(name = 'V_218',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_562,(0,1):C.GC_561})

V_219 = Vertex(name = 'V_219',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_804,(0,2):C.GC_702,(0,1):C.GC_701})

V_220 = Vertex(name = 'V_220',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_725})

V_221 = Vertex(name = 'V_221',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_734})

V_222 = Vertex(name = 'V_222',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_777})

V_223 = Vertex(name = 'V_223',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_1292,(0,1):C.GC_1291})

V_224 = Vertex(name = 'V_224',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_804,(0,2):C.GC_1315,(0,1):C.GC_1314})

V_225 = Vertex(name = 'V_225',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_725})

V_226 = Vertex(name = 'V_226',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_734})

V_227 = Vertex(name = 'V_227',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_777})

V_228 = Vertex(name = 'V_228',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_2,(0,2):C.GC_925,(0,1):C.GC_924})

V_229 = Vertex(name = 'V_229',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_804,(0,2):C.GC_948,(0,1):C.GC_947})

V_230 = Vertex(name = 'V_230',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_725})

V_231 = Vertex(name = 'V_231',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_734})

V_232 = Vertex(name = 'V_232',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_777})

V_233 = Vertex(name = 'V_233',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_428,(0,2):C.GC_344,(0,4):C.GC_755,(0,3):C.GC_753,(0,5):C.GC_548,(0,1):C.GC_547})

V_234 = Vertex(name = 'V_234',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_718,(0,2):C.GC_818,(0,3):C.GC_676,(0,1):C.GC_675})

V_235 = Vertex(name = 'V_235',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_785,(0,1):C.GC_768})

V_236 = Vertex(name = 'V_236',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_827,(0,1):C.GC_770})

V_237 = Vertex(name = 'V_237',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_788,(0,1):C.GC_774})

V_238 = Vertex(name = 'V_238',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_428,(0,2):C.GC_344,(0,4):C.GC_755,(0,3):C.GC_754,(0,5):C.GC_1023,(0,1):C.GC_1022})

V_239 = Vertex(name = 'V_239',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_718,(0,2):C.GC_762,(0,3):C.GC_1035,(0,1):C.GC_1034})

V_240 = Vertex(name = 'V_240',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_785,(0,1):C.GC_764})

V_241 = Vertex(name = 'V_241',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_827,(0,1):C.GC_818})

V_242 = Vertex(name = 'V_242',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_788,(0,1):C.GC_774})

V_243 = Vertex(name = 'V_243',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV8, L.FFV9 ],
               couplings = {(0,0):C.GC_428,(0,2):C.GC_344,(0,4):C.GC_755,(0,3):C.GC_754,(0,5):C.GC_1140,(0,1):C.GC_1139})

V_244 = Vertex(name = 'V_244',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_718,(0,2):C.GC_762,(0,3):C.GC_1152,(0,1):C.GC_1151})

V_245 = Vertex(name = 'V_245',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_785,(0,1):C.GC_764})

V_246 = Vertex(name = 'V_246',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_827,(0,1):C.GC_818})

V_247 = Vertex(name = 'V_247',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_788,(0,1):C.GC_774})

V_248 = Vertex(name = 'V_248',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_430,(0,2):C.GC_344,(0,4):C.GC_758,(0,3):C.GC_759,(0,5):C.GC_558,(0,1):C.GC_555})

V_249 = Vertex(name = 'V_249',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_721,(0,2):C.GC_765,(0,3):C.GC_682,(0,1):C.GC_679})

V_250 = Vertex(name = 'V_250',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_787,(0,1):C.GC_819})

V_251 = Vertex(name = 'V_251',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_829,(0,1):C.GC_774})

V_252 = Vertex(name = 'V_252',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_790})

V_253 = Vertex(name = 'V_253',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_430,(0,2):C.GC_344,(0,4):C.GC_758,(0,3):C.GC_760,(0,5):C.GC_559,(0,1):C.GC_556})

V_254 = Vertex(name = 'V_254',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_721,(0,2):C.GC_766,(0,3):C.GC_683,(0,1):C.GC_680})

V_255 = Vertex(name = 'V_255',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_787,(0,1):C.GC_820})

V_256 = Vertex(name = 'V_256',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_829,(0,1):C.GC_774})

V_257 = Vertex(name = 'V_257',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_790})

V_258 = Vertex(name = 'V_258',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_430,(0,2):C.GC_344,(0,4):C.GC_758,(0,3):C.GC_761,(0,5):C.GC_560,(0,1):C.GC_557})

V_259 = Vertex(name = 'V_259',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_721,(0,2):C.GC_767,(0,3):C.GC_684,(0,1):C.GC_681})

V_260 = Vertex(name = 'V_260',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_787,(0,1):C.GC_823})

V_261 = Vertex(name = 'V_261',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_829,(0,1):C.GC_774})

V_262 = Vertex(name = 'V_262',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_790})

V_263 = Vertex(name = 'V_263',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_429,(0,2):C.GC_343,(0,4):C.GC_757,(0,3):C.GC_771,(0,5):C.GC_573,(0,1):C.GC_571})

V_264 = Vertex(name = 'V_264',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_719,(0,2):C.GC_821,(0,3):C.GC_692,(0,1):C.GC_691})

V_265 = Vertex(name = 'V_265',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_786,(0,1):C.GC_768})

V_266 = Vertex(name = 'V_266',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_828,(0,1):C.GC_769})

V_267 = Vertex(name = 'V_267',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_789,(0,1):C.GC_773})

V_268 = Vertex(name = 'V_268',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_429,(0,2):C.GC_343,(0,4):C.GC_757,(0,3):C.GC_772,(0,5):C.GC_1301,(0,1):C.GC_1299})

V_269 = Vertex(name = 'V_269',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_719,(0,2):C.GC_762,(0,3):C.GC_1313,(0,1):C.GC_1312})

V_270 = Vertex(name = 'V_270',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_786,(0,1):C.GC_763})

V_271 = Vertex(name = 'V_271',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_828,(0,1):C.GC_821})

V_272 = Vertex(name = 'V_272',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_789,(0,1):C.GC_773})

V_273 = Vertex(name = 'V_273',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV9 ],
               couplings = {(0,0):C.GC_429,(0,2):C.GC_343,(0,4):C.GC_757,(0,3):C.GC_772,(0,5):C.GC_934,(0,1):C.GC_932})

V_274 = Vertex(name = 'V_274',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV9 ],
               couplings = {(0,0):C.GC_719,(0,2):C.GC_762,(0,3):C.GC_946,(0,1):C.GC_945})

V_275 = Vertex(name = 'V_275',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_786,(0,1):C.GC_763})

V_276 = Vertex(name = 'V_276',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_828,(0,1):C.GC_821})

V_277 = Vertex(name = 'V_277',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_789,(0,1):C.GC_773})

V_278 = Vertex(name = 'V_278',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_515,(0,1):C.GC_514})

V_279 = Vertex(name = 'V_279',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_1014,(0,1):C.GC_1013})

V_280 = Vertex(name = 'V_280',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_1131,(0,1):C.GC_1130})

V_281 = Vertex(name = 'V_281',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_544,(0,1):C.GC_543})

V_282 = Vertex(name = 'V_282',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_1294,(0,1):C.GC_1293})

V_283 = Vertex(name = 'V_283',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV9 ],
               couplings = {(0,0):C.GC_6,(0,2):C.GC_927,(0,1):C.GC_926})

V_284 = Vertex(name = 'V_284',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_570,(0,0):C.GC_518,(0,1):C.GC_342,(0,3):C.GC_749})

V_285 = Vertex(name = 'V_285',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_572,(0,0):C.GC_520,(0,1):C.GC_816,(0,3):C.GC_751})

V_286 = Vertex(name = 'V_286',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_748})

V_287 = Vertex(name = 'V_287',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_288 = Vertex(name = 'V_288',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_360,(0,0):C.GC_359})

V_289 = Vertex(name = 'V_289',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_362})

V_290 = Vertex(name = 'V_290',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_250,(0,3):C.GC_27,(0,2):C.GC_628,(0,0):C.GC_627})

V_291 = Vertex(name = 'V_291',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_252,(0,2):C.GC_29,(0,1):C.GC_630})

V_292 = Vertex(name = 'V_292',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1298,(0,0):C.GC_1017,(0,1):C.GC_342,(0,3):C.GC_1349})

V_293 = Vertex(name = 'V_293',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1300,(0,0):C.GC_1019,(0,1):C.GC_747,(0,3):C.GC_1351})

V_294 = Vertex(name = 'V_294',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_816})

V_295 = Vertex(name = 'V_295',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_296 = Vertex(name = 'V_296',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_931,(0,0):C.GC_1134,(0,1):C.GC_342,(0,3):C.GC_1188})

V_297 = Vertex(name = 'V_297',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_933,(0,0):C.GC_1136,(0,1):C.GC_747,(0,3):C.GC_1190})

V_298 = Vertex(name = 'V_298',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_816})

V_299 = Vertex(name = 'V_299',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_300 = Vertex(name = 'V_300',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1343,(0,0):C.GC_355})

V_301 = Vertex(name = 'V_301',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1345})

V_302 = Vertex(name = 'V_302',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1182,(0,0):C.GC_355})

V_303 = Vertex(name = 'V_303',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1184})

V_304 = Vertex(name = 'V_304',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_1272,(0,3):C.GC_960,(0,2):C.GC_1346,(0,0):C.GC_623})

V_305 = Vertex(name = 'V_305',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_1274,(0,2):C.GC_962,(0,1):C.GC_1348})

V_306 = Vertex(name = 'V_306',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_905,(0,3):C.GC_1077,(0,2):C.GC_1185,(0,0):C.GC_623})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_907,(0,2):C.GC_1079,(0,1):C.GC_1187})

V_308 = Vertex(name = 'V_308',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_356})

V_309 = Vertex(name = 'V_309',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS8 ],
               couplings = {(0,1):C.GC_50,(0,0):C.GC_624})

V_310 = Vertex(name = 'V_310',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS8 ],
               couplings = {(0,0):C.GC_56})

V_311 = Vertex(name = 'V_311',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_527,(0,1):C.GC_342})

V_312 = Vertex(name = 'V_312',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_533,(0,1):C.GC_815})

V_313 = Vertex(name = 'V_313',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_314 = Vertex(name = 'V_314',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_529,(0,1):C.GC_342})

V_315 = Vertex(name = 'V_315',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_534,(0,1):C.GC_814})

V_316 = Vertex(name = 'V_316',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_317 = Vertex(name = 'V_317',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_342})

V_318 = Vertex(name = 'V_318',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV10, L.FFV3 ],
               couplings = {(0,0):C.GC_535,(0,1):C.GC_817})

V_319 = Vertex(name = 'V_319',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_320 = Vertex(name = 'V_320',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_357})

V_321 = Vertex(name = 'V_321',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS8 ],
               couplings = {(0,1):C.GC_52,(0,0):C.GC_625})

V_322 = Vertex(name = 'V_322',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS8 ],
               couplings = {(0,0):C.GC_57})

V_323 = Vertex(name = 'V_323',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_358})

V_324 = Vertex(name = 'V_324',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS8 ],
               couplings = {(0,1):C.GC_54,(0,0):C.GC_626})

V_325 = Vertex(name = 'V_325',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS8 ],
               couplings = {(0,0):C.GC_58})

V_326 = Vertex(name = 'V_326',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_519,(0,0):C.GC_569,(0,1):C.GC_342,(0,3):C.GC_750})

V_327 = Vertex(name = 'V_327',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_520,(0,0):C.GC_572,(0,1):C.GC_816,(0,3):C.GC_751})

V_328 = Vertex(name = 'V_328',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_748})

V_329 = Vertex(name = 'V_329',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_330 = Vertex(name = 'V_330',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_361,(0,0):C.GC_359})

V_331 = Vertex(name = 'V_331',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_362})

V_332 = Vertex(name = 'V_332',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_28,(0,3):C.GC_249,(0,2):C.GC_629,(0,0):C.GC_627})

V_333 = Vertex(name = 'V_333',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_29,(0,2):C.GC_252,(0,1):C.GC_630})

V_334 = Vertex(name = 'V_334',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1018,(0,0):C.GC_1297,(0,1):C.GC_342,(0,3):C.GC_1350})

V_335 = Vertex(name = 'V_335',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1019,(0,0):C.GC_1300,(0,1):C.GC_747,(0,3):C.GC_1351})

V_336 = Vertex(name = 'V_336',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_816})

V_337 = Vertex(name = 'V_337',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_338 = Vertex(name = 'V_338',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1135,(0,0):C.GC_930,(0,1):C.GC_342,(0,3):C.GC_1189})

V_339 = Vertex(name = 'V_339',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV10, L.FFV3, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1136,(0,0):C.GC_933,(0,1):C.GC_747,(0,3):C.GC_1190})

V_340 = Vertex(name = 'V_340',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_816})

V_341 = Vertex(name = 'V_341',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_342 = Vertex(name = 'V_342',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1344,(0,0):C.GC_355})

V_343 = Vertex(name = 'V_343',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1345})

V_344 = Vertex(name = 'V_344',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,1):C.GC_1183,(0,0):C.GC_355})

V_345 = Vertex(name = 'V_345',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS2 ],
               couplings = {(0,0):C.GC_1184})

V_346 = Vertex(name = 'V_346',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_961,(0,3):C.GC_1271,(0,2):C.GC_1347,(0,0):C.GC_623})

V_347 = Vertex(name = 'V_347',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_962,(0,2):C.GC_1274,(0,1):C.GC_1348})

V_348 = Vertex(name = 'V_348',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS4, L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,1):C.GC_1078,(0,3):C.GC_904,(0,2):C.GC_1186,(0,0):C.GC_623})

V_349 = Vertex(name = 'V_349',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS5, L.FFVS6, L.FFVS8 ],
               couplings = {(0,0):C.GC_1079,(0,2):C.GC_907,(0,1):C.GC_1187})

V_350 = Vertex(name = 'V_350',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_356})

V_351 = Vertex(name = 'V_351',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_51,(0,0):C.GC_624})

V_352 = Vertex(name = 'V_352',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS5 ],
               couplings = {(0,0):C.GC_56})

V_353 = Vertex(name = 'V_353',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_528,(0,0):C.GC_342})

V_354 = Vertex(name = 'V_354',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_533,(0,0):C.GC_815})

V_355 = Vertex(name = 'V_355',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_356 = Vertex(name = 'V_356',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_530,(0,0):C.GC_342})

V_357 = Vertex(name = 'V_357',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_534,(0,0):C.GC_814})

V_358 = Vertex(name = 'V_358',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_359 = Vertex(name = 'V_359',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_532,(0,0):C.GC_342})

V_360 = Vertex(name = 'V_360',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV4 ],
               couplings = {(0,1):C.GC_535,(0,0):C.GC_817})

V_361 = Vertex(name = 'V_361',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_752})

V_362 = Vertex(name = 'V_362',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_357})

V_363 = Vertex(name = 'V_363',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_53,(0,0):C.GC_625})

V_364 = Vertex(name = 'V_364',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS5 ],
               couplings = {(0,0):C.GC_57})

V_365 = Vertex(name = 'V_365',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_358})

V_366 = Vertex(name = 'V_366',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS5 ],
               couplings = {(0,1):C.GC_55,(0,0):C.GC_626})

V_367 = Vertex(name = 'V_367',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS5 ],
               couplings = {(0,0):C.GC_58})

V_368 = Vertex(name = 'V_368',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_380,(0,1):C.GC_363})

V_369 = Vertex(name = 'V_369',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_382})

V_370 = Vertex(name = 'V_370',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_648,(0,2):C.GC_631,(0,3):C.GC_220,(0,0):C.GC_219})

V_371 = Vertex(name = 'V_371',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_650,(0,2):C.GC_432,(0,0):C.GC_431})

V_372 = Vertex(name = 'V_372',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_364})

V_373 = Vertex(name = 'V_373',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_370})

V_374 = Vertex(name = 'V_374',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_364})

V_375 = Vertex(name = 'V_375',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_370})

V_376 = Vertex(name = 'V_376',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_636,(0,2):C.GC_632,(0,3):C.GC_997,(0,0):C.GC_996})

V_377 = Vertex(name = 'V_377',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_638,(0,2):C.GC_1010,(0,0):C.GC_1009})

V_378 = Vertex(name = 'V_378',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_636,(0,2):C.GC_632,(0,3):C.GC_1114,(0,0):C.GC_1113})

V_379 = Vertex(name = 'V_379',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_638,(0,2):C.GC_1127,(0,0):C.GC_1126})

V_380 = Vertex(name = 'V_380',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_371,(0,1):C.GC_365})

V_381 = Vertex(name = 'V_381',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_375})

V_382 = Vertex(name = 'V_382',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_639,(0,2):C.GC_633,(0,3):C.GC_230,(0,0):C.GC_227})

V_383 = Vertex(name = 'V_383',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_643,(0,2):C.GC_438,(0,0):C.GC_435})

V_384 = Vertex(name = 'V_384',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_372,(0,1):C.GC_366})

V_385 = Vertex(name = 'V_385',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_377})

V_386 = Vertex(name = 'V_386',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_640,(0,2):C.GC_634,(0,3):C.GC_231,(0,0):C.GC_228})

V_387 = Vertex(name = 'V_387',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_645,(0,2):C.GC_439,(0,0):C.GC_436})

V_388 = Vertex(name = 'V_388',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_373,(0,1):C.GC_367})

V_389 = Vertex(name = 'V_389',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_379})

V_390 = Vertex(name = 'V_390',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,2):C.GC_641,(0,3):C.GC_635,(0,0):C.GC_229,(0,1):C.GC_437,(0,4):C.GC_232})

V_391 = Vertex(name = 'V_391',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4, L.FFVS7 ],
               couplings = {(0,0):C.GC_647,(0,1):C.GC_440})

V_392 = Vertex(name = 'V_392',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_380,(0,1):C.GC_383})

V_393 = Vertex(name = 'V_393',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_381})

V_394 = Vertex(name = 'V_394',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_648,(0,2):C.GC_651,(0,3):C.GC_253,(0,0):C.GC_251})

V_395 = Vertex(name = 'V_395',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_649,(0,2):C.GC_448,(0,0):C.GC_447})

V_396 = Vertex(name = 'V_396',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_384})

V_397 = Vertex(name = 'V_397',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_369})

V_398 = Vertex(name = 'V_398',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_368,(0,1):C.GC_384})

V_399 = Vertex(name = 'V_399',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_369})

V_400 = Vertex(name = 'V_400',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_636,(0,2):C.GC_652,(0,3):C.GC_1275,(0,0):C.GC_1273})

V_401 = Vertex(name = 'V_401',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_637,(0,2):C.GC_1288,(0,0):C.GC_1287})

V_402 = Vertex(name = 'V_402',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS6, L.FFVS7 ],
               couplings = {(0,1):C.GC_636,(0,2):C.GC_652,(0,3):C.GC_908,(0,0):C.GC_906})

V_403 = Vertex(name = 'V_403',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS4, L.FFVS7 ],
               couplings = {(0,1):C.GC_637,(0,2):C.GC_921,(0,0):C.GC_920})

V_404 = Vertex(name = 'V_404',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_371})

V_405 = Vertex(name = 'V_405',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_374})

V_406 = Vertex(name = 'V_406',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_639})

V_407 = Vertex(name = 'V_407',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_642})

V_408 = Vertex(name = 'V_408',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_343})

V_409 = Vertex(name = 'V_409',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_756})

V_410 = Vertex(name = 'V_410',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_765})

V_411 = Vertex(name = 'V_411',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_820})

V_412 = Vertex(name = 'V_412',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_773})

V_413 = Vertex(name = 'V_413',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_343})

V_414 = Vertex(name = 'V_414',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_756})

V_415 = Vertex(name = 'V_415',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_766})

V_416 = Vertex(name = 'V_416',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_819})

V_417 = Vertex(name = 'V_417',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_773})

V_418 = Vertex(name = 'V_418',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_343})

V_419 = Vertex(name = 'V_419',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_756})

V_420 = Vertex(name = 'V_420',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_767})

V_421 = Vertex(name = 'V_421',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_822})

V_422 = Vertex(name = 'V_422',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_773})

V_423 = Vertex(name = 'V_423',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_372})

V_424 = Vertex(name = 'V_424',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_376})

V_425 = Vertex(name = 'V_425',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_640})

V_426 = Vertex(name = 'V_426',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_644})

V_427 = Vertex(name = 'V_427',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_373})

V_428 = Vertex(name = 'V_428',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_378})

V_429 = Vertex(name = 'V_429',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_641})

V_430 = Vertex(name = 'V_430',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS4 ],
               couplings = {(0,0):C.GC_646})

V_431 = Vertex(name = 'V_431',
               particles = [ P.t1__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_306})

V_432 = Vertex(name = 'V_432',
               particles = [ P.t__tilde__, P.t1, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_301})

V_433 = Vertex(name = 'V_433',
               particles = [ P.t1__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_301})

V_434 = Vertex(name = 'V_434',
               particles = [ P.t1__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_309})

V_435 = Vertex(name = 'V_435',
               particles = [ P.t__tilde__, P.t1, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_304})

V_436 = Vertex(name = 'V_436',
               particles = [ P.t1__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_304})

V_437 = Vertex(name = 'V_437',
               particles = [ P.b__tilde__, P.t1, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_438 = Vertex(name = 'V_438',
               particles = [ P.b__tilde__, P.t1, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_421})

V_439 = Vertex(name = 'V_439',
               particles = [ P.b__tilde__, P.t, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_440 = Vertex(name = 'V_440',
               particles = [ P.d__tilde__, P.u, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_441 = Vertex(name = 'V_441',
               particles = [ P.s__tilde__, P.c, P.W1__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_442 = Vertex(name = 'V_442',
               particles = [ P.e__plus__, P.ve, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_443 = Vertex(name = 'V_443',
               particles = [ P.mu__plus__, P.vm, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_444 = Vertex(name = 'V_444',
               particles = [ P.ta__plus__, P.vt, P.W1__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_445 = Vertex(name = 'V_445',
               particles = [ P.t1__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_421})

V_446 = Vertex(name = 'V_446',
               particles = [ P.t__tilde__, P.b, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_447 = Vertex(name = 'V_447',
               particles = [ P.u__tilde__, P.d, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_448 = Vertex(name = 'V_448',
               particles = [ P.c__tilde__, P.s, P.W1__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_449 = Vertex(name = 'V_449',
               particles = [ P.ve__tilde__, P.e__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_450 = Vertex(name = 'V_450',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_451 = Vertex(name = 'V_451',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W1__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_452 = Vertex(name = 'V_452',
               particles = [ P.t1__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_416})

V_453 = Vertex(name = 'V_453',
               particles = [ P.t1__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_468,(0,1):C.GC_422})

V_454 = Vertex(name = 'V_454',
               particles = [ P.t__tilde__, P.t1, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_417})

V_455 = Vertex(name = 'V_455',
               particles = [ P.t1__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_417})

V_456 = Vertex(name = 'V_456',
               particles = [ P.b__tilde__, P.b, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_465,(0,1):C.GC_418})

V_457 = Vertex(name = 'V_457',
               particles = [ P.d__tilde__, P.d, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_465,(0,1):C.GC_418})

V_458 = Vertex(name = 'V_458',
               particles = [ P.s__tilde__, P.s, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_465,(0,1):C.GC_418})

V_459 = Vertex(name = 'V_459',
               particles = [ P.e__plus__, P.e__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_467,(0,1):C.GC_418})

V_460 = Vertex(name = 'V_460',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_467,(0,1):C.GC_418})

V_461 = Vertex(name = 'V_461',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_467,(0,1):C.GC_418})

V_462 = Vertex(name = 'V_462',
               particles = [ P.t1__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_469,(0,1):C.GC_425})

V_463 = Vertex(name = 'V_463',
               particles = [ P.t__tilde__, P.t1, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_468,(0,1):C.GC_422})

V_464 = Vertex(name = 'V_464',
               particles = [ P.t1__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_468,(0,1):C.GC_422})

V_465 = Vertex(name = 'V_465',
               particles = [ P.t__tilde__, P.t, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_417})

V_466 = Vertex(name = 'V_466',
               particles = [ P.u__tilde__, P.u, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_417})

V_467 = Vertex(name = 'V_467',
               particles = [ P.c__tilde__, P.c, P.Z1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_466,(0,1):C.GC_417})

V_468 = Vertex(name = 'V_468',
               particles = [ P.ve__tilde__, P.ve, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_417})

V_469 = Vertex(name = 'V_469',
               particles = [ P.vm__tilde__, P.vm, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_417})

V_470 = Vertex(name = 'V_470',
               particles = [ P.vt__tilde__, P.vt, P.Z1 ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_417})

V_471 = Vertex(name = 'V_471',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_18,(0,1):C.GC_19})

V_472 = Vertex(name = 'V_472',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_517})

V_473 = Vertex(name = 'V_473',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_707,(0,1):C.GC_708})

V_474 = Vertex(name = 'V_474',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_833})

V_475 = Vertex(name = 'V_475',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_835})

V_476 = Vertex(name = 'V_476',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_836})

V_477 = Vertex(name = 'V_477',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_838})

V_478 = Vertex(name = 'V_478',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_837})

V_479 = Vertex(name = 'V_479',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_41,(0,1):C.GC_44})

V_480 = Vertex(name = 'V_480',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_521,(0,1):C.GC_524})

V_481 = Vertex(name = 'V_481',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_709,(0,1):C.GC_712})

V_482 = Vertex(name = 'V_482',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1060})

V_483 = Vertex(name = 'V_483',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1062})

V_484 = Vertex(name = 'V_484',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1063})

V_485 = Vertex(name = 'V_485',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1065})

V_486 = Vertex(name = 'V_486',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1064})

V_487 = Vertex(name = 'V_487',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_42,(0,1):C.GC_45})

V_488 = Vertex(name = 'V_488',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_525})

V_489 = Vertex(name = 'V_489',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_710,(0,1):C.GC_713})

V_490 = Vertex(name = 'V_490',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1066})

V_491 = Vertex(name = 'V_491',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1068})

V_492 = Vertex(name = 'V_492',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1069})

V_493 = Vertex(name = 'V_493',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1071})

V_494 = Vertex(name = 'V_494',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1070})

V_495 = Vertex(name = 'V_495',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_43,(0,1):C.GC_46})

V_496 = Vertex(name = 'V_496',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_523,(0,1):C.GC_526})

V_497 = Vertex(name = 'V_497',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_711,(0,1):C.GC_714})

V_498 = Vertex(name = 'V_498',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1200})

V_499 = Vertex(name = 'V_499',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1202})

V_500 = Vertex(name = 'V_500',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1203})

V_501 = Vertex(name = 'V_501',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1205})

V_502 = Vertex(name = 'V_502',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1204})

V_503 = Vertex(name = 'V_503',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_239,(0,1):C.GC_240})

V_504 = Vertex(name = 'V_504',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_567,(0,1):C.GC_568})

V_505 = Vertex(name = 'V_505',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_716,(0,1):C.GC_717})

V_506 = Vertex(name = 'V_506',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1192})

V_507 = Vertex(name = 'V_507',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1196})

V_508 = Vertex(name = 'V_508',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1197})

V_509 = Vertex(name = 'V_509',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1199})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1198})

V_511 = Vertex(name = 'V_511',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1038,(0,1):C.GC_955})

V_512 = Vertex(name = 'V_512',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1039})

V_513 = Vertex(name = 'V_513',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1040})

V_514 = Vertex(name = 'V_514',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1041})

V_515 = Vertex(name = 'V_515',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1059})

V_516 = Vertex(name = 'V_516',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1042})

V_517 = Vertex(name = 'V_517',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1155,(0,1):C.GC_1072})

V_518 = Vertex(name = 'V_518',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1156})

V_519 = Vertex(name = 'V_519',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1157})

V_520 = Vertex(name = 'V_520',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1158})

V_521 = Vertex(name = 'V_521',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1191})

V_522 = Vertex(name = 'V_522',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1159})

V_523 = Vertex(name = 'V_523',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_958,(0,1):C.GC_959})

V_524 = Vertex(name = 'V_524',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1075,(0,1):C.GC_1076})

V_525 = Vertex(name = 'V_525',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1015,(0,1):C.GC_1016})

V_526 = Vertex(name = 'V_526',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1132,(0,1):C.GC_1133})

V_527 = Vertex(name = 'V_527',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_1319,(0,1):C.GC_1206})

V_528 = Vertex(name = 'V_528',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1316})

V_529 = Vertex(name = 'V_529',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1317})

V_530 = Vertex(name = 'V_530',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1368})

V_531 = Vertex(name = 'V_531',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1318})

V_532 = Vertex(name = 'V_532',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1320})

V_533 = Vertex(name = 'V_533',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_952,(0,1):C.GC_839})

V_534 = Vertex(name = 'V_534',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_949})

V_535 = Vertex(name = 'V_535',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_950})

V_536 = Vertex(name = 'V_536',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_954})

V_537 = Vertex(name = 'V_537',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_951})

V_538 = Vertex(name = 'V_538',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_953})

V_539 = Vertex(name = 'V_539',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_1269,(0,1):C.GC_1270})

V_540 = Vertex(name = 'V_540',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_902,(0,1):C.GC_903})

V_541 = Vertex(name = 'V_541',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1295,(0,1):C.GC_1296})

V_542 = Vertex(name = 'V_542',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_928,(0,1):C.GC_929})

V_543 = Vertex(name = 'V_543',
               particles = [ P.b__tilde__, P.b, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_834})

V_544 = Vertex(name = 'V_544',
               particles = [ P.t1__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1194})

V_545 = Vertex(name = 'V_545',
               particles = [ P.t1__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1195})

V_546 = Vertex(name = 'V_546',
               particles = [ P.t__tilde__, P.t1, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1193})

V_547 = Vertex(name = 'V_547',
               particles = [ P.t__tilde__, P.t1, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1194})

V_548 = Vertex(name = 'V_548',
               particles = [ P.t1__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1193})

V_549 = Vertex(name = 'V_549',
               particles = [ P.t1__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1194})

V_550 = Vertex(name = 'V_550',
               particles = [ P.t__tilde__, P.t, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1193})

V_551 = Vertex(name = 'V_551',
               particles = [ P.d__tilde__, P.d, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1003})

V_552 = Vertex(name = 'V_552',
               particles = [ P.s__tilde__, P.s, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1120})

V_553 = Vertex(name = 'V_553',
               particles = [ P.e__plus__, P.e__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1061})

V_554 = Vertex(name = 'V_554',
               particles = [ P.mu__plus__, P.mu__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1067})

V_555 = Vertex(name = 'V_555',
               particles = [ P.ta__plus__, P.ta__minus__, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1201})

V_556 = Vertex(name = 'V_556',
               particles = [ P.u__tilde__, P.u, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_1281})

V_557 = Vertex(name = 'V_557',
               particles = [ P.c__tilde__, P.c, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               couplings = {(0,0):C.GC_914})

V_558 = Vertex(name = 'V_558',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_218,(0,0):C.GC_217})

V_559 = Vertex(name = 'V_559',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_434,(0,0):C.GC_433})

V_560 = Vertex(name = 'V_560',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_224,(0,0):C.GC_221})

V_561 = Vertex(name = 'V_561',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_444,(0,0):C.GC_441})

V_562 = Vertex(name = 'V_562',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_225,(0,0):C.GC_222})

V_563 = Vertex(name = 'V_563',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_445,(0,0):C.GC_442})

V_564 = Vertex(name = 'V_564',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_226,(0,0):C.GC_223})

V_565 = Vertex(name = 'V_565',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_446,(0,0):C.GC_443})

V_566 = Vertex(name = 'V_566',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS3, L.FFVS7 ],
               couplings = {(0,2):C.GC_234,(0,1):C.GC_233,(0,0):C.GC_457})

V_567 = Vertex(name = 'V_567',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS7 ],
               couplings = {(0,0):C.GC_458})

V_568 = Vertex(name = 'V_568',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_16})

V_569 = Vertex(name = 'V_569',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_285,(0,0):C.GC_284})

V_570 = Vertex(name = 'V_570',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_595,(0,0):C.GC_594})

V_571 = Vertex(name = 'V_571',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_216,(0,0):C.GC_215})

V_572 = Vertex(name = 'V_572',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_291,(0,0):C.GC_290})

V_573 = Vertex(name = 'V_573',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_599,(0,0):C.GC_598})

V_574 = Vertex(name = 'V_574',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_995,(0,0):C.GC_994})

V_575 = Vertex(name = 'V_575',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1012,(0,0):C.GC_1011})

V_576 = Vertex(name = 'V_576',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1112,(0,0):C.GC_1111})

V_577 = Vertex(name = 'V_577',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1129,(0,0):C.GC_1128})

V_578 = Vertex(name = 'V_578',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_957,(0,0):C.GC_956})

V_579 = Vertex(name = 'V_579',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1074,(0,0):C.GC_1073})

V_580 = Vertex(name = 'V_580',
               particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1002,(0,0):C.GC_1001})

V_581 = Vertex(name = 'V_581',
               particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1119,(0,0):C.GC_1118})

V_582 = Vertex(name = 'V_582',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1028,(0,0):C.GC_1027})

V_583 = Vertex(name = 'V_583',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1145,(0,0):C.GC_1144})

V_584 = Vertex(name = 'V_584',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1266,(0,0):C.GC_1265})

V_585 = Vertex(name = 'V_585',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1290,(0,0):C.GC_1289})

V_586 = Vertex(name = 'V_586',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_899,(0,0):C.GC_898})

V_587 = Vertex(name = 'V_587',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_923,(0,0):C.GC_922})

V_588 = Vertex(name = 'V_588',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_1268,(0,0):C.GC_1267})

V_589 = Vertex(name = 'V_589',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS3, L.FFVS7 ],
               couplings = {(0,1):C.GC_901,(0,0):C.GC_900})

V_590 = Vertex(name = 'V_590',
               particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1280,(0,0):C.GC_1279})

V_591 = Vertex(name = 'V_591',
               particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_913,(0,0):C.GC_912})

V_592 = Vertex(name = 'V_592',
               particles = [ P.u__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1306,(0,0):C.GC_1305})

V_593 = Vertex(name = 'V_593',
               particles = [ P.c__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_939,(0,0):C.GC_938})

V_594 = Vertex(name = 'V_594',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_260,(0,1):C.GC_276})

V_595 = Vertex(name = 'V_595',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_262,(0,1):C.GC_278})

V_596 = Vertex(name = 'V_596',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_574,(0,1):C.GC_590})

V_597 = Vertex(name = 'V_597',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_576,(0,1):C.GC_592})

V_598 = Vertex(name = 'V_598',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_348,(0,0):C.GC_347})

V_599 = Vertex(name = 'V_599',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_616,(0,0):C.GC_615})

V_600 = Vertex(name = 'V_600',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_385,(0,1):C.GC_402})

V_601 = Vertex(name = 'V_601',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_386,(0,1):C.GC_404})

V_602 = Vertex(name = 'V_602',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_653,(0,1):C.GC_670})

V_603 = Vertex(name = 'V_603',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_654,(0,1):C.GC_672})

V_604 = Vertex(name = 'V_604',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_263})

V_605 = Vertex(name = 'V_605',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_267})

V_606 = Vertex(name = 'V_606',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_577})

V_607 = Vertex(name = 'V_607',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_581})

V_608 = Vertex(name = 'V_608',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_352,(0,0):C.GC_349})

V_609 = Vertex(name = 'V_609',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_620,(0,0):C.GC_617})

V_610 = Vertex(name = 'V_610',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_388})

V_611 = Vertex(name = 'V_611',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_391})

V_612 = Vertex(name = 'V_612',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_656})

V_613 = Vertex(name = 'V_613',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_659})

V_614 = Vertex(name = 'V_614',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_264})

V_615 = Vertex(name = 'V_615',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_269})

V_616 = Vertex(name = 'V_616',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_578})

V_617 = Vertex(name = 'V_617',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_583})

V_618 = Vertex(name = 'V_618',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_353,(0,0):C.GC_350})

V_619 = Vertex(name = 'V_619',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_621,(0,0):C.GC_618})

V_620 = Vertex(name = 'V_620',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_389})

V_621 = Vertex(name = 'V_621',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_393})

V_622 = Vertex(name = 'V_622',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_657})

V_623 = Vertex(name = 'V_623',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_661})

V_624 = Vertex(name = 'V_624',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_265})

V_625 = Vertex(name = 'V_625',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_271})

V_626 = Vertex(name = 'V_626',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_579})

V_627 = Vertex(name = 'V_627',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_585})

V_628 = Vertex(name = 'V_628',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_354,(0,0):C.GC_351})

V_629 = Vertex(name = 'V_629',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_622,(0,0):C.GC_619})

V_630 = Vertex(name = 'V_630',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_390})

V_631 = Vertex(name = 'V_631',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_395})

V_632 = Vertex(name = 'V_632',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_658})

V_633 = Vertex(name = 'V_633',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_663})

V_634 = Vertex(name = 'V_634',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_276,(0,1):C.GC_260})

V_635 = Vertex(name = 'V_635',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_277,(0,1):C.GC_261})

V_636 = Vertex(name = 'V_636',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_590,(0,1):C.GC_574})

V_637 = Vertex(name = 'V_637',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_591,(0,1):C.GC_575})

V_638 = Vertex(name = 'V_638',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_403,(0,0):C.GC_401})

V_639 = Vertex(name = 'V_639',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_671,(0,0):C.GC_669})

V_640 = Vertex(name = 'V_640',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_402,(0,1):C.GC_385})

V_641 = Vertex(name = 'V_641',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_405,(0,1):C.GC_387})

V_642 = Vertex(name = 'V_642',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_670,(0,1):C.GC_653})

V_643 = Vertex(name = 'V_643',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_673,(0,1):C.GC_655})

V_644 = Vertex(name = 'V_644',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_998,(0,1):C.GC_1276})

V_645 = Vertex(name = 'V_645',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1000,(0,1):C.GC_1278})

V_646 = Vertex(name = 'V_646',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1115,(0,1):C.GC_909})

V_647 = Vertex(name = 'V_647',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1117,(0,1):C.GC_911})

V_648 = Vertex(name = 'V_648',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1024,(0,1):C.GC_1302})

V_649 = Vertex(name = 'V_649',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1026,(0,1):C.GC_1304})

V_650 = Vertex(name = 'V_650',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1141,(0,1):C.GC_935})

V_651 = Vertex(name = 'V_651',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1143,(0,1):C.GC_937})

V_652 = Vertex(name = 'V_652',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1005,(0,0):C.GC_1004})

V_653 = Vertex(name = 'V_653',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1122,(0,0):C.GC_1121})

V_654 = Vertex(name = 'V_654',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1030,(0,0):C.GC_1029})

V_655 = Vertex(name = 'V_655',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1147,(0,0):C.GC_1146})

V_656 = Vertex(name = 'V_656',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1006,(0,1):C.GC_1283})

V_657 = Vertex(name = 'V_657',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1007,(0,1):C.GC_1285})

V_658 = Vertex(name = 'V_658',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1123,(0,1):C.GC_916})

V_659 = Vertex(name = 'V_659',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1124,(0,1):C.GC_918})

V_660 = Vertex(name = 'V_660',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1031,(0,1):C.GC_1308})

V_661 = Vertex(name = 'V_661',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1032,(0,1):C.GC_1310})

V_662 = Vertex(name = 'V_662',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1148,(0,1):C.GC_941})

V_663 = Vertex(name = 'V_663',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1149,(0,1):C.GC_943})

V_664 = Vertex(name = 'V_664',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1276,(0,1):C.GC_998})

V_665 = Vertex(name = 'V_665',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1277,(0,1):C.GC_999})

V_666 = Vertex(name = 'V_666',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_909,(0,1):C.GC_1115})

V_667 = Vertex(name = 'V_667',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_910,(0,1):C.GC_1116})

V_668 = Vertex(name = 'V_668',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1302,(0,1):C.GC_1024})

V_669 = Vertex(name = 'V_669',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1303,(0,1):C.GC_1025})

V_670 = Vertex(name = 'V_670',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_935,(0,1):C.GC_1141})

V_671 = Vertex(name = 'V_671',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_936,(0,1):C.GC_1142})

V_672 = Vertex(name = 'V_672',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_1284,(0,0):C.GC_1282})

V_673 = Vertex(name = 'V_673',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS3 ],
               couplings = {(0,1):C.GC_917,(0,0):C.GC_915})

V_674 = Vertex(name = 'V_674',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_1309,(0,0):C.GC_1307})

V_675 = Vertex(name = 'V_675',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV3 ],
               couplings = {(0,1):C.GC_942,(0,0):C.GC_940})

V_676 = Vertex(name = 'V_676',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1283,(0,1):C.GC_1006})

V_677 = Vertex(name = 'V_677',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_1286,(0,1):C.GC_1008})

V_678 = Vertex(name = 'V_678',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_916,(0,1):C.GC_1123})

V_679 = Vertex(name = 'V_679',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2, L.FFVVS4 ],
               couplings = {(0,0):C.GC_919,(0,1):C.GC_1125})

V_680 = Vertex(name = 'V_680',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1308,(0,1):C.GC_1031})

V_681 = Vertex(name = 'V_681',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_1311,(0,1):C.GC_1033})

V_682 = Vertex(name = 'V_682',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_941,(0,1):C.GC_1148})

V_683 = Vertex(name = 'V_683',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2, L.FFVV4 ],
               couplings = {(0,0):C.GC_944,(0,1):C.GC_1150})

V_684 = Vertex(name = 'V_684',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_263})

V_685 = Vertex(name = 'V_685',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_266})

V_686 = Vertex(name = 'V_686',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_577})

V_687 = Vertex(name = 'V_687',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_580})

V_688 = Vertex(name = 'V_688',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4, L.FFVVS5 ],
               couplings = {(0,0):C.GC_264,(0,1):C.GC_268})

V_689 = Vertex(name = 'V_689',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_578})

V_690 = Vertex(name = 'V_690',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_582})

V_691 = Vertex(name = 'V_691',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_265})

V_692 = Vertex(name = 'V_692',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_270})

V_693 = Vertex(name = 'V_693',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_579})

V_694 = Vertex(name = 'V_694',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_584})

V_695 = Vertex(name = 'V_695',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_388})

V_696 = Vertex(name = 'V_696',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_392})

V_697 = Vertex(name = 'V_697',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_656})

V_698 = Vertex(name = 'V_698',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_660})

V_699 = Vertex(name = 'V_699',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_389})

V_700 = Vertex(name = 'V_700',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_394})

V_701 = Vertex(name = 'V_701',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_657})

V_702 = Vertex(name = 'V_702',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_662})

V_703 = Vertex(name = 'V_703',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_390})

V_704 = Vertex(name = 'V_704',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVVS4 ],
               couplings = {(0,0):C.GC_396})

V_705 = Vertex(name = 'V_705',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_658})

V_706 = Vertex(name = 'V_706',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV4 ],
               couplings = {(0,0):C.GC_664})

V_707 = Vertex(name = 'V_707',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_194,(3,6):C.GC_195,(0,7):C.GC_194,(2,7):C.GC_195,(3,1):C.GC_168,(1,2):C.GC_10,(0,4):C.GC_167,(2,4):C.GC_168,(0,5):C.GC_10,(0,0):C.GC_167,(2,0):C.GC_168,(1,3):C.GC_167,(3,3):C.GC_168,(1,1):C.GC_167})

V_708 = Vertex(name = 'V_708',
               particles = [ P.b__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,5):C.GC_174,(2,5):C.GC_175,(0,0):C.GC_20,(2,0):C.GC_21,(1,2):C.GC_963,(3,2):C.GC_966,(1,1):C.GC_964,(3,1):C.GC_967,(0,3):C.GC_169,(2,3):C.GC_170,(0,4):C.GC_11,(2,4):C.GC_12})

V_709 = Vertex(name = 'V_709',
               particles = [ P.b__tilde__, P.b, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF16, L.FFFF4 ],
               couplings = {(0,2):C.GC_177,(2,2):C.GC_180,(1,1):C.GC_965,(3,1):C.GC_968,(1,0):C.GC_965,(3,0):C.GC_968})

V_710 = Vertex(name = 'V_710',
               particles = [ P.b__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,5):C.GC_174,(2,5):C.GC_175,(0,0):C.GC_20,(2,0):C.GC_21,(1,2):C.GC_1080,(3,2):C.GC_1083,(1,1):C.GC_1081,(3,1):C.GC_1084,(0,3):C.GC_169,(2,3):C.GC_170,(0,4):C.GC_11,(2,4):C.GC_12})

V_711 = Vertex(name = 'V_711',
               particles = [ P.b__tilde__, P.b, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF16, L.FFFF4 ],
               couplings = {(0,2):C.GC_177,(2,2):C.GC_180,(1,1):C.GC_1082,(3,1):C.GC_1085,(1,0):C.GC_1082,(3,0):C.GC_1085})

V_712 = Vertex(name = 'V_712',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_73,(3,6):C.GC_74,(0,7):C.GC_73,(2,7):C.GC_74,(0,0):C.GC_68,(2,0):C.GC_69,(1,3):C.GC_68,(3,3):C.GC_69,(1,1):C.GC_68,(3,1):C.GC_69,(1,2):C.GC_30,(3,2):C.GC_31,(0,4):C.GC_68,(2,4):C.GC_69,(0,5):C.GC_30,(2,5):C.GC_31})

V_713 = Vertex(name = 'V_713',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_76,(3,0):C.GC_79,(0,1):C.GC_76,(2,1):C.GC_79})

V_714 = Vertex(name = 'V_714',
               particles = [ P.d__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,3):C.GC_73,(1,3):C.GC_74,(0,0):C.GC_68,(1,0):C.GC_69,(0,1):C.GC_68,(1,1):C.GC_69,(0,2):C.GC_30,(1,2):C.GC_31})

V_715 = Vertex(name = 'V_715',
               particles = [ P.d__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_76,(1,0):C.GC_79})

V_716 = Vertex(name = 'V_716',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_73,(3,6):C.GC_74,(0,7):C.GC_73,(2,7):C.GC_74,(0,0):C.GC_68,(2,0):C.GC_69,(1,3):C.GC_68,(3,3):C.GC_69,(1,1):C.GC_68,(3,1):C.GC_69,(1,2):C.GC_30,(3,2):C.GC_31,(0,4):C.GC_68,(2,4):C.GC_69,(0,5):C.GC_30,(2,5):C.GC_31})

V_717 = Vertex(name = 'V_717',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_76,(3,0):C.GC_79,(0,1):C.GC_76,(2,1):C.GC_79})

V_718 = Vertex(name = 'V_718',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_182,(0,1):C.GC_171,(0,2):C.GC_22,(0,3):C.GC_13,(0,5):C.GC_98,(0,0):C.GC_99})

V_719 = Vertex(name = 'V_719',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_186,(0,2):C.GC_104,(0,0):C.GC_104})

V_720 = Vertex(name = 'V_720',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_143,(0,1):C.GC_70,(0,2):C.GC_83,(0,3):C.GC_32,(0,5):C.GC_977,(0,0):C.GC_978})

V_721 = Vertex(name = 'V_721',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_147,(0,2):C.GC_983,(0,0):C.GC_983})

V_722 = Vertex(name = 'V_722',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_143,(0,1):C.GC_70,(0,2):C.GC_83,(0,3):C.GC_32,(0,5):C.GC_1094,(0,0):C.GC_1095})

V_723 = Vertex(name = 'V_723',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_147,(0,2):C.GC_1100,(0,0):C.GC_1100})

V_724 = Vertex(name = 'V_724',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_155,(0,7):C.GC_155,(0,0):C.GC_86,(0,3):C.GC_86,(0,1):C.GC_86,(0,2):C.GC_35,(0,4):C.GC_86,(0,5):C.GC_35})

V_725 = Vertex(name = 'V_725',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,5):C.GC_156,(0,6):C.GC_158,(0,0):C.GC_89,(0,3):C.GC_91,(0,1):C.GC_87,(0,2):C.GC_36,(0,4):C.GC_89})

V_726 = Vertex(name = 'V_726',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_183,(0,1):C.GC_172,(0,2):C.GC_23,(0,3):C.GC_14,(0,5):C.GC_100,(0,0):C.GC_101})

V_727 = Vertex(name = 'V_727',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_189,(0,2):C.GC_105,(0,0):C.GC_105})

V_728 = Vertex(name = 'V_728',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_144,(0,1):C.GC_71,(0,2):C.GC_84,(0,3):C.GC_33,(0,5):C.GC_979,(0,0):C.GC_980})

V_729 = Vertex(name = 'V_729',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_150,(0,2):C.GC_984,(0,0):C.GC_984})

V_730 = Vertex(name = 'V_730',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_144,(0,1):C.GC_71,(0,2):C.GC_84,(0,3):C.GC_33,(0,5):C.GC_1096,(0,0):C.GC_1097})

V_731 = Vertex(name = 'V_731',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_150,(0,2):C.GC_1101,(0,0):C.GC_1101})

V_732 = Vertex(name = 'V_732',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_160,(0,7):C.GC_160,(0,0):C.GC_92,(0,3):C.GC_92,(0,1):C.GC_92,(0,2):C.GC_38,(0,4):C.GC_92,(0,5):C.GC_38})

V_733 = Vertex(name = 'V_733',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,5):C.GC_157,(0,6):C.GC_159,(0,0):C.GC_90,(0,3):C.GC_95,(0,1):C.GC_88,(0,2):C.GC_37,(0,4):C.GC_90})

V_734 = Vertex(name = 'V_734',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF3, L.FFFF4 ],
               couplings = {(0,5):C.GC_161,(0,6):C.GC_162,(0,0):C.GC_94,(0,3):C.GC_96,(0,1):C.GC_93,(0,2):C.GC_39,(0,4):C.GC_94})

V_735 = Vertex(name = 'V_735',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_184,(0,1):C.GC_173,(0,2):C.GC_24,(0,3):C.GC_15,(0,5):C.GC_102,(0,0):C.GC_103})

V_736 = Vertex(name = 'V_736',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_192,(0,2):C.GC_106,(0,0):C.GC_106})

V_737 = Vertex(name = 'V_737',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_145,(0,1):C.GC_72,(0,2):C.GC_85,(0,3):C.GC_34,(0,5):C.GC_981,(0,0):C.GC_982})

V_738 = Vertex(name = 'V_738',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_153,(0,2):C.GC_985,(0,0):C.GC_985})

V_739 = Vertex(name = 'V_739',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_145,(0,1):C.GC_72,(0,2):C.GC_85,(0,3):C.GC_34,(0,5):C.GC_1098,(0,0):C.GC_1099})

V_740 = Vertex(name = 'V_740',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF4, L.FFFF9 ],
               couplings = {(0,1):C.GC_153,(0,2):C.GC_1102,(0,0):C.GC_1102})

V_741 = Vertex(name = 'V_741',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_163,(0,7):C.GC_163,(0,0):C.GC_97,(0,3):C.GC_97,(0,1):C.GC_97,(0,2):C.GC_40,(0,4):C.GC_97,(0,5):C.GC_40})

V_742 = Vertex(name = 'V_742',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_187,(0,5):C.GC_119,(0,3):C.GC_121,(0,4):C.GC_121,(0,1):C.GC_108,(0,0):C.GC_99})

V_743 = Vertex(name = 'V_743',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_133,(0,2):C.GC_132,(0,3):C.GC_132,(0,1):C.GC_114,(0,0):C.GC_104})

V_744 = Vertex(name = 'V_744',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_190,(0,5):C.GC_123,(0,3):C.GC_125,(0,4):C.GC_125,(0,1):C.GC_110,(0,0):C.GC_101})

V_745 = Vertex(name = 'V_745',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_137,(0,2):C.GC_136,(0,3):C.GC_136,(0,1):C.GC_116,(0,0):C.GC_105})

V_746 = Vertex(name = 'V_746',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_193,(0,5):C.GC_127,(0,3):C.GC_129,(0,4):C.GC_129,(0,1):C.GC_112,(0,0):C.GC_103})

V_747 = Vertex(name = 'V_747',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_141,(0,2):C.GC_140,(0,3):C.GC_140,(0,1):C.GC_118,(0,0):C.GC_106})

V_748 = Vertex(name = 'V_748',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_182,(0,11):C.GC_122,(0,9):C.GC_120,(0,10):C.GC_120,(0,5):C.GC_107,(0,1):C.GC_171,(0,2):C.GC_243,(0,3):C.GC_212,(0,7):C.GC_119,(0,4):C.GC_121,(0,6):C.GC_121,(0,0):C.GC_108})

V_749 = Vertex(name = 'V_749',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_185,(0,8):C.GC_134,(0,6):C.GC_131,(0,7):C.GC_131,(0,2):C.GC_113,(0,4):C.GC_134,(0,1):C.GC_131,(0,3):C.GC_131,(0,0):C.GC_113})

V_750 = Vertex(name = 'V_750',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_183,(0,11):C.GC_126,(0,9):C.GC_124,(0,10):C.GC_124,(0,5):C.GC_109,(0,1):C.GC_172,(0,2):C.GC_244,(0,3):C.GC_213,(0,7):C.GC_123,(0,4):C.GC_125,(0,6):C.GC_125,(0,0):C.GC_110})

V_751 = Vertex(name = 'V_751',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_188,(0,8):C.GC_138,(0,6):C.GC_135,(0,7):C.GC_135,(0,2):C.GC_115,(0,4):C.GC_138,(0,1):C.GC_135,(0,3):C.GC_135,(0,0):C.GC_115})

V_752 = Vertex(name = 'V_752',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_184,(0,11):C.GC_130,(0,9):C.GC_128,(0,10):C.GC_128,(0,5):C.GC_111,(0,1):C.GC_173,(0,2):C.GC_245,(0,3):C.GC_214,(0,7):C.GC_127,(0,4):C.GC_129,(0,6):C.GC_129,(0,0):C.GC_112})

V_753 = Vertex(name = 'V_753',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_191,(0,8):C.GC_142,(0,6):C.GC_139,(0,7):C.GC_139,(0,2):C.GC_117,(0,4):C.GC_142,(0,1):C.GC_139,(0,3):C.GC_139,(0,0):C.GC_117})

V_754 = Vertex(name = 'V_754',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF4 ],
               couplings = {(0,7):C.GC_178,(2,7):C.GC_181,(1,0):C.GC_970,(3,0):C.GC_974,(0,6):C.GC_986,(2,6):C.GC_990,(1,5):C.GC_964,(3,5):C.GC_967,(1,3):C.GC_1207,(3,3):C.GC_1210,(1,4):C.GC_1338,(3,4):C.GC_1341,(1,1):C.GC_1257,(3,1):C.GC_1261,(0,2):C.GC_1214,(2,2):C.GC_1218})

V_755 = Vertex(name = 'V_755',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2 ],
               couplings = {(1,0):C.GC_972,(3,0):C.GC_976,(0,6):C.GC_988,(2,6):C.GC_992,(1,5):C.GC_965,(3,5):C.GC_968,(1,3):C.GC_1209,(3,3):C.GC_1212,(1,4):C.GC_1339,(3,4):C.GC_1342,(1,1):C.GC_1260,(3,1):C.GC_1264,(0,2):C.GC_1215,(2,2):C.GC_1219})

V_756 = Vertex(name = 'V_756',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF4 ],
               couplings = {(0,7):C.GC_178,(2,7):C.GC_181,(1,0):C.GC_1087,(3,0):C.GC_1091,(0,6):C.GC_1103,(2,6):C.GC_1107,(1,5):C.GC_1081,(3,5):C.GC_1084,(1,3):C.GC_840,(3,3):C.GC_843,(1,4):C.GC_1177,(3,4):C.GC_1180,(1,1):C.GC_890,(3,1):C.GC_894,(0,2):C.GC_847,(2,2):C.GC_851})

V_757 = Vertex(name = 'V_757',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2 ],
               couplings = {(1,0):C.GC_1089,(3,0):C.GC_1093,(0,6):C.GC_1105,(2,6):C.GC_1109,(1,5):C.GC_1082,(3,5):C.GC_1085,(1,3):C.GC_842,(3,3):C.GC_845,(1,4):C.GC_1178,(3,4):C.GC_1181,(1,1):C.GC_893,(3,1):C.GC_897,(0,2):C.GC_848,(2,2):C.GC_852})

V_758 = Vertex(name = 'V_758',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_194,(3,7):C.GC_195,(1,0):C.GC_199,(3,0):C.GC_203,(0,6):C.GC_198,(2,6):C.GC_202,(1,5):C.GC_167,(3,5):C.GC_168,(1,3):C.GC_196,(3,3):C.GC_197,(1,4):C.GC_208,(3,4):C.GC_209,(1,1):C.GC_198,(3,1):C.GC_202,(0,2):C.GC_199,(2,2):C.GC_203})

V_759 = Vertex(name = 'V_759',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_201,(3,0):C.GC_205,(0,3):C.GC_200,(2,3):C.GC_204,(1,1):C.GC_201,(3,1):C.GC_205,(0,2):C.GC_200,(2,2):C.GC_204})

V_760 = Vertex(name = 'V_760',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_174,(3,7):C.GC_175,(1,0):C.GC_987,(3,0):C.GC_991,(0,6):C.GC_969,(2,6):C.GC_973,(1,5):C.GC_169,(3,5):C.GC_170,(1,3):C.GC_241,(3,3):C.GC_242,(1,4):C.GC_210,(3,4):C.GC_211,(1,1):C.GC_986,(3,1):C.GC_990,(0,2):C.GC_970,(2,2):C.GC_974})

V_761 = Vertex(name = 'V_761',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_176,(3,4):C.GC_179,(1,0):C.GC_989,(3,0):C.GC_993,(0,3):C.GC_971,(2,3):C.GC_975,(1,1):C.GC_989,(3,1):C.GC_993,(0,2):C.GC_971,(2,2):C.GC_975})

V_762 = Vertex(name = 'V_762',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_174,(3,7):C.GC_175,(1,0):C.GC_1104,(3,0):C.GC_1108,(0,6):C.GC_1086,(2,6):C.GC_1090,(1,5):C.GC_169,(3,5):C.GC_170,(1,3):C.GC_241,(3,3):C.GC_242,(1,4):C.GC_210,(3,4):C.GC_211,(1,1):C.GC_1103,(3,1):C.GC_1107,(0,2):C.GC_1087,(2,2):C.GC_1091})

V_763 = Vertex(name = 'V_763',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_176,(3,4):C.GC_179,(1,0):C.GC_1106,(3,0):C.GC_1110,(0,3):C.GC_1088,(2,3):C.GC_1092,(1,1):C.GC_1106,(3,1):C.GC_1110,(0,2):C.GC_1088,(2,2):C.GC_1092})

V_764 = Vertex(name = 'V_764',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_194,(3,6):C.GC_195,(0,7):C.GC_194,(2,7):C.GC_195,(0,0):C.GC_196,(2,0):C.GC_197,(1,3):C.GC_196,(3,3):C.GC_197,(1,1):C.GC_196,(3,1):C.GC_197,(1,2):C.GC_246,(0,4):C.GC_196,(2,4):C.GC_197,(0,5):C.GC_246})

V_765 = Vertex(name = 'V_765',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_148,(0,5):C.GC_1233,(0,3):C.GC_1235,(0,4):C.GC_1235,(0,1):C.GC_1222,(0,0):C.GC_978})

V_766 = Vertex(name = 'V_766',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_1247,(0,2):C.GC_1246,(0,3):C.GC_1246,(0,1):C.GC_1228,(0,0):C.GC_983})

V_767 = Vertex(name = 'V_767',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_148,(0,5):C.GC_866,(0,3):C.GC_868,(0,4):C.GC_868,(0,1):C.GC_855,(0,0):C.GC_1095})

V_768 = Vertex(name = 'V_768',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_880,(0,2):C.GC_879,(0,3):C.GC_879,(0,1):C.GC_861,(0,0):C.GC_1100})

V_769 = Vertex(name = 'V_769',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_151,(0,5):C.GC_1237,(0,3):C.GC_1239,(0,4):C.GC_1239,(0,1):C.GC_1224,(0,0):C.GC_980})

V_770 = Vertex(name = 'V_770',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_1251,(0,2):C.GC_1250,(0,3):C.GC_1250,(0,1):C.GC_1230,(0,0):C.GC_984})

V_771 = Vertex(name = 'V_771',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_151,(0,5):C.GC_870,(0,3):C.GC_872,(0,4):C.GC_872,(0,1):C.GC_857,(0,0):C.GC_1097})

V_772 = Vertex(name = 'V_772',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_884,(0,2):C.GC_883,(0,3):C.GC_883,(0,1):C.GC_863,(0,0):C.GC_1101})

V_773 = Vertex(name = 'V_773',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_154,(0,5):C.GC_1241,(0,3):C.GC_1243,(0,4):C.GC_1243,(0,1):C.GC_1226,(0,0):C.GC_982})

V_774 = Vertex(name = 'V_774',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,4):C.GC_1255,(0,2):C.GC_1254,(0,3):C.GC_1254,(0,1):C.GC_1232,(0,0):C.GC_985})

V_775 = Vertex(name = 'V_775',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,4):C.GC_876,(0,2):C.GC_154,(0,6):C.GC_874,(0,3):C.GC_876,(0,5):C.GC_887,(0,1):C.GC_859,(0,0):C.GC_1099})

V_776 = Vertex(name = 'V_776',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF2, L.FFFF6, L.FFFF8 ],
               couplings = {(0,2):C.GC_887,(0,3):C.GC_888,(0,1):C.GC_865,(0,0):C.GC_1102})

V_777 = Vertex(name = 'V_777',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_143,(0,11):C.GC_1236,(0,9):C.GC_1234,(0,10):C.GC_1234,(0,5):C.GC_1221,(0,1):C.GC_70,(0,2):C.GC_164,(0,3):C.GC_47,(0,7):C.GC_1233,(0,4):C.GC_1235,(0,6):C.GC_1235,(0,0):C.GC_1222})

V_778 = Vertex(name = 'V_778',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_146,(0,8):C.GC_1248,(0,6):C.GC_1245,(0,7):C.GC_1245,(0,2):C.GC_1227,(0,4):C.GC_1248,(0,1):C.GC_1245,(0,3):C.GC_1245,(0,0):C.GC_1227})

V_779 = Vertex(name = 'V_779',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_143,(0,11):C.GC_869,(0,9):C.GC_867,(0,10):C.GC_867,(0,5):C.GC_854,(0,1):C.GC_70,(0,2):C.GC_164,(0,3):C.GC_47,(0,7):C.GC_866,(0,4):C.GC_868,(0,6):C.GC_868,(0,0):C.GC_855})

V_780 = Vertex(name = 'V_780',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_146,(0,8):C.GC_881,(0,6):C.GC_878,(0,7):C.GC_878,(0,2):C.GC_860,(0,4):C.GC_881,(0,1):C.GC_878,(0,3):C.GC_878,(0,0):C.GC_860})

V_781 = Vertex(name = 'V_781',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_144,(0,11):C.GC_1240,(0,9):C.GC_1238,(0,10):C.GC_1238,(0,5):C.GC_1223,(0,1):C.GC_71,(0,2):C.GC_165,(0,3):C.GC_48,(0,7):C.GC_1237,(0,4):C.GC_1239,(0,6):C.GC_1239,(0,0):C.GC_1224})

V_782 = Vertex(name = 'V_782',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_149,(0,8):C.GC_1252,(0,6):C.GC_1249,(0,7):C.GC_1249,(0,2):C.GC_1229,(0,4):C.GC_1252,(0,1):C.GC_1249,(0,3):C.GC_1249,(0,0):C.GC_1229})

V_783 = Vertex(name = 'V_783',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_144,(0,11):C.GC_873,(0,9):C.GC_871,(0,10):C.GC_871,(0,5):C.GC_856,(0,1):C.GC_71,(0,2):C.GC_165,(0,3):C.GC_48,(0,7):C.GC_870,(0,4):C.GC_872,(0,6):C.GC_872,(0,0):C.GC_857})

V_784 = Vertex(name = 'V_784',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_149,(0,8):C.GC_885,(0,6):C.GC_882,(0,7):C.GC_882,(0,2):C.GC_862,(0,4):C.GC_885,(0,1):C.GC_882,(0,3):C.GC_882,(0,0):C.GC_862})

V_785 = Vertex(name = 'V_785',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_145,(0,11):C.GC_1244,(0,9):C.GC_1242,(0,10):C.GC_1242,(0,5):C.GC_1225,(0,1):C.GC_72,(0,2):C.GC_166,(0,3):C.GC_49,(0,7):C.GC_1241,(0,4):C.GC_1243,(0,6):C.GC_1243,(0,0):C.GC_1226})

V_786 = Vertex(name = 'V_786',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_152,(0,8):C.GC_1256,(0,6):C.GC_1253,(0,7):C.GC_1253,(0,2):C.GC_1231,(0,4):C.GC_1256,(0,1):C.GC_1253,(0,3):C.GC_1253,(0,0):C.GC_1231})

V_787 = Vertex(name = 'V_787',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,8):C.GC_145,(0,11):C.GC_877,(0,9):C.GC_875,(0,10):C.GC_875,(0,5):C.GC_858,(0,1):C.GC_72,(0,2):C.GC_166,(0,3):C.GC_49,(0,7):C.GC_874,(0,4):C.GC_876,(0,6):C.GC_876,(0,0):C.GC_859})

V_788 = Vertex(name = 'V_788',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF8 ],
               couplings = {(0,5):C.GC_152,(0,8):C.GC_889,(0,6):C.GC_886,(0,7):C.GC_886,(0,2):C.GC_864,(0,4):C.GC_889,(0,1):C.GC_886,(0,3):C.GC_886,(0,0):C.GC_864})

V_789 = Vertex(name = 'V_789',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF4 ],
               couplings = {(0,7):C.GC_178,(2,7):C.GC_181,(1,0):C.GC_1258,(3,0):C.GC_1262,(0,6):C.GC_1213,(2,6):C.GC_1217,(1,5):C.GC_963,(3,5):C.GC_966,(1,3):C.GC_1208,(3,3):C.GC_1211,(1,4):C.GC_1337,(3,4):C.GC_1340,(1,1):C.GC_969,(3,1):C.GC_973,(0,2):C.GC_987,(2,2):C.GC_991})

V_790 = Vertex(name = 'V_790',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2 ],
               couplings = {(1,0):C.GC_1260,(3,0):C.GC_1264,(0,6):C.GC_1215,(2,6):C.GC_1219,(1,5):C.GC_965,(3,5):C.GC_968,(1,3):C.GC_1209,(3,3):C.GC_1212,(1,4):C.GC_1339,(3,4):C.GC_1342,(1,1):C.GC_972,(3,1):C.GC_976,(0,2):C.GC_988,(2,2):C.GC_992})

V_791 = Vertex(name = 'V_791',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF4 ],
               couplings = {(0,7):C.GC_178,(2,7):C.GC_181,(1,0):C.GC_891,(3,0):C.GC_895,(0,6):C.GC_846,(2,6):C.GC_850,(1,5):C.GC_1080,(3,5):C.GC_1083,(1,3):C.GC_841,(3,3):C.GC_844,(1,4):C.GC_1176,(3,4):C.GC_1179,(1,1):C.GC_1086,(3,1):C.GC_1090,(0,2):C.GC_1104,(2,2):C.GC_1108})

V_792 = Vertex(name = 'V_792',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2 ],
               couplings = {(1,0):C.GC_893,(3,0):C.GC_897,(0,6):C.GC_848,(2,6):C.GC_852,(1,5):C.GC_1082,(3,5):C.GC_1085,(1,3):C.GC_842,(3,3):C.GC_845,(1,4):C.GC_1178,(3,4):C.GC_1181,(1,1):C.GC_1089,(3,1):C.GC_1093,(0,2):C.GC_1105,(2,2):C.GC_1109})

V_793 = Vertex(name = 'V_793',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_174,(3,7):C.GC_175,(1,0):C.GC_1214,(3,0):C.GC_1218,(0,6):C.GC_1257,(2,6):C.GC_1261,(1,5):C.GC_20,(3,5):C.GC_21,(1,3):C.GC_206,(3,3):C.GC_207,(1,4):C.GC_25,(3,4):C.GC_26,(1,1):C.GC_1213,(3,1):C.GC_1217,(0,2):C.GC_1258,(2,2):C.GC_1262})

V_794 = Vertex(name = 'V_794',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_176,(3,4):C.GC_179,(1,0):C.GC_1216,(3,0):C.GC_1220,(0,3):C.GC_1259,(2,3):C.GC_1263,(1,1):C.GC_1216,(3,1):C.GC_1220,(0,2):C.GC_1259,(2,2):C.GC_1263})

V_795 = Vertex(name = 'V_795',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_174,(3,7):C.GC_175,(1,0):C.GC_847,(3,0):C.GC_851,(0,6):C.GC_890,(2,6):C.GC_894,(1,5):C.GC_20,(3,5):C.GC_21,(1,3):C.GC_206,(3,3):C.GC_207,(1,4):C.GC_25,(3,4):C.GC_26,(1,1):C.GC_846,(3,1):C.GC_850,(0,2):C.GC_891,(2,2):C.GC_895})

V_796 = Vertex(name = 'V_796',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_176,(3,4):C.GC_179,(1,0):C.GC_849,(3,0):C.GC_853,(0,3):C.GC_892,(2,3):C.GC_896,(1,1):C.GC_849,(3,1):C.GC_853,(0,2):C.GC_892,(2,2):C.GC_896})

V_797 = Vertex(name = 'V_797',
               particles = [ P.t__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,5):C.GC_174,(2,5):C.GC_175,(0,0):C.GC_241,(2,0):C.GC_242,(1,2):C.GC_1207,(3,2):C.GC_1210,(1,1):C.GC_1208,(3,1):C.GC_1211,(0,3):C.GC_206,(2,3):C.GC_207,(0,4):C.GC_247,(2,4):C.GC_248})

V_798 = Vertex(name = 'V_798',
               particles = [ P.t__tilde__, P.t, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF16, L.FFFF4 ],
               couplings = {(0,2):C.GC_177,(2,2):C.GC_180,(1,1):C.GC_1209,(3,1):C.GC_1212,(1,0):C.GC_1209,(3,0):C.GC_1212})

V_799 = Vertex(name = 'V_799',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,5):C.GC_174,(2,5):C.GC_175,(0,0):C.GC_241,(2,0):C.GC_242,(1,2):C.GC_840,(3,2):C.GC_843,(1,1):C.GC_841,(3,1):C.GC_844,(0,3):C.GC_206,(2,3):C.GC_207,(0,4):C.GC_247,(2,4):C.GC_248})

V_800 = Vertex(name = 'V_800',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF16, L.FFFF4 ],
               couplings = {(0,2):C.GC_177,(2,2):C.GC_180,(1,1):C.GC_842,(3,1):C.GC_845,(1,0):C.GC_842,(3,0):C.GC_845})

V_801 = Vertex(name = 'V_801',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_73,(3,7):C.GC_74,(0,8):C.GC_77,(2,8):C.GC_80,(1,0):C.GC_1322,(3,0):C.GC_1330,(0,6):C.GC_1321,(2,6):C.GC_1329,(1,5):C.GC_68,(3,5):C.GC_69,(1,3):C.GC_81,(3,3):C.GC_82,(1,4):C.GC_254,(3,4):C.GC_255,(1,1):C.GC_1321,(3,1):C.GC_1329,(0,2):C.GC_1322,(2,2):C.GC_1330})

V_802 = Vertex(name = 'V_802',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_75,(3,4):C.GC_78,(1,0):C.GC_1324,(3,0):C.GC_1332,(0,3):C.GC_1323,(2,3):C.GC_1331,(1,1):C.GC_1324,(3,1):C.GC_1332,(0,2):C.GC_1323,(2,2):C.GC_1331})

V_803 = Vertex(name = 'V_803',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1326,(3,0):C.GC_1334,(0,3):C.GC_1325,(2,3):C.GC_1333,(1,1):C.GC_1325,(3,1):C.GC_1333,(0,2):C.GC_1326,(2,2):C.GC_1334})

V_804 = Vertex(name = 'V_804',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1328,(3,0):C.GC_1336,(0,3):C.GC_1327,(2,3):C.GC_1335,(1,1):C.GC_1328,(3,1):C.GC_1336,(0,2):C.GC_1327,(2,2):C.GC_1335})

V_805 = Vertex(name = 'V_805',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_73,(3,7):C.GC_74,(1,0):C.GC_1048,(3,0):C.GC_1056,(0,6):C.GC_1043,(2,6):C.GC_1051,(1,5):C.GC_68,(3,5):C.GC_69,(1,3):C.GC_81,(3,3):C.GC_82,(1,4):C.GC_254,(3,4):C.GC_255,(1,1):C.GC_1047,(3,1):C.GC_1055,(0,2):C.GC_1044,(2,2):C.GC_1052})

V_806 = Vertex(name = 'V_806',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_75,(3,4):C.GC_78,(1,0):C.GC_1050,(3,0):C.GC_1058,(0,3):C.GC_1045,(2,3):C.GC_1053,(1,1):C.GC_1050,(3,1):C.GC_1058,(0,2):C.GC_1045,(2,2):C.GC_1053})

V_807 = Vertex(name = 'V_807',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF4 ],
               couplings = {(0,4):C.GC_77,(2,4):C.GC_80,(1,0):C.GC_1044,(3,0):C.GC_1052,(0,3):C.GC_1047,(2,3):C.GC_1055,(1,1):C.GC_1352,(3,1):C.GC_1360,(0,2):C.GC_1357,(2,2):C.GC_1365})

V_808 = Vertex(name = 'V_808',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1046,(3,0):C.GC_1054,(0,3):C.GC_1049,(2,3):C.GC_1057,(1,1):C.GC_1355,(3,1):C.GC_1363,(0,2):C.GC_1358,(2,2):C.GC_1366})

V_809 = Vertex(name = 'V_809',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF4 ],
               couplings = {(0,4):C.GC_77,(2,4):C.GC_80,(1,0):C.GC_1353,(3,0):C.GC_1361,(0,3):C.GC_1356,(2,3):C.GC_1364,(1,1):C.GC_1043,(3,1):C.GC_1051,(0,2):C.GC_1048,(2,2):C.GC_1056})

V_810 = Vertex(name = 'V_810',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1355,(3,0):C.GC_1363,(0,3):C.GC_1358,(2,3):C.GC_1366,(1,1):C.GC_1046,(3,1):C.GC_1054,(0,2):C.GC_1049,(2,2):C.GC_1057})

V_811 = Vertex(name = 'V_811',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3 ],
               couplings = {(1,7):C.GC_73,(3,7):C.GC_74,(1,0):C.GC_1357,(3,0):C.GC_1365,(0,6):C.GC_1352,(2,6):C.GC_1360,(1,5):C.GC_68,(3,5):C.GC_69,(1,3):C.GC_81,(3,3):C.GC_82,(1,4):C.GC_254,(3,4):C.GC_255,(1,1):C.GC_1356,(3,1):C.GC_1364,(0,2):C.GC_1353,(2,2):C.GC_1361})

V_812 = Vertex(name = 'V_812',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_75,(3,4):C.GC_78,(1,0):C.GC_1359,(3,0):C.GC_1367,(0,3):C.GC_1354,(2,3):C.GC_1362,(1,1):C.GC_1359,(3,1):C.GC_1367,(0,2):C.GC_1354,(2,2):C.GC_1362})

V_813 = Vertex(name = 'V_813',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_73,(3,7):C.GC_74,(0,8):C.GC_77,(2,8):C.GC_80,(1,0):C.GC_1161,(3,0):C.GC_1169,(0,6):C.GC_1160,(2,6):C.GC_1168,(1,5):C.GC_68,(3,5):C.GC_69,(1,3):C.GC_81,(3,3):C.GC_82,(1,4):C.GC_254,(3,4):C.GC_255,(1,1):C.GC_1160,(3,1):C.GC_1168,(0,2):C.GC_1161,(2,2):C.GC_1169})

V_814 = Vertex(name = 'V_814',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2, L.FFFF3 ],
               couplings = {(1,4):C.GC_75,(3,4):C.GC_78,(1,0):C.GC_1163,(3,0):C.GC_1171,(0,3):C.GC_1162,(2,3):C.GC_1170,(1,1):C.GC_1163,(3,1):C.GC_1171,(0,2):C.GC_1162,(2,2):C.GC_1170})

V_815 = Vertex(name = 'V_815',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1165,(3,0):C.GC_1173,(0,3):C.GC_1164,(2,3):C.GC_1172,(1,1):C.GC_1164,(3,1):C.GC_1172,(0,2):C.GC_1165,(2,2):C.GC_1173})

V_816 = Vertex(name = 'V_816',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF2 ],
               couplings = {(1,0):C.GC_1167,(3,0):C.GC_1175,(0,3):C.GC_1166,(2,3):C.GC_1174,(1,1):C.GC_1167,(3,1):C.GC_1175,(0,2):C.GC_1166,(2,2):C.GC_1174})

V_817 = Vertex(name = 'V_817',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_73,(3,6):C.GC_74,(0,7):C.GC_73,(2,7):C.GC_74,(0,0):C.GC_81,(2,0):C.GC_82,(1,3):C.GC_81,(3,3):C.GC_82,(1,1):C.GC_81,(3,1):C.GC_82,(1,2):C.GC_256,(3,2):C.GC_257,(0,4):C.GC_81,(2,4):C.GC_82,(0,5):C.GC_256,(2,5):C.GC_257})

V_818 = Vertex(name = 'V_818',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_76,(3,0):C.GC_79,(0,1):C.GC_76,(2,1):C.GC_79})

V_819 = Vertex(name = 'V_819',
               particles = [ P.u__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4 ],
               couplings = {(0,3):C.GC_73,(1,3):C.GC_74,(0,0):C.GC_81,(1,0):C.GC_82,(0,1):C.GC_81,(1,1):C.GC_82,(0,2):C.GC_256,(1,2):C.GC_257})

V_820 = Vertex(name = 'V_820',
               particles = [ P.u__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_76,(1,0):C.GC_79})

V_821 = Vertex(name = 'V_821',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_73,(3,6):C.GC_74,(0,7):C.GC_73,(2,7):C.GC_74,(0,0):C.GC_81,(2,0):C.GC_82,(1,3):C.GC_81,(3,3):C.GC_82,(1,1):C.GC_81,(3,1):C.GC_82,(1,2):C.GC_256,(3,2):C.GC_257,(0,4):C.GC_81,(2,4):C.GC_82,(0,5):C.GC_256,(2,5):C.GC_257})

V_822 = Vertex(name = 'V_822',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(1,0):C.GC_76,(3,0):C.GC_79,(0,1):C.GC_76,(2,1):C.GC_79})

V_823 = Vertex(name = 'V_823',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_187,(0,4):C.GC_122,(0,2):C.GC_120,(0,3):C.GC_120,(0,0):C.GC_98,(0,1):C.GC_107})

V_824 = Vertex(name = 'V_824',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_133,(0,2):C.GC_132,(0,3):C.GC_132,(0,0):C.GC_104,(0,1):C.GC_114})

V_825 = Vertex(name = 'V_825',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_148,(0,4):C.GC_1236,(0,2):C.GC_1234,(0,3):C.GC_1234,(0,0):C.GC_977,(0,1):C.GC_1221})

V_826 = Vertex(name = 'V_826',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_1247,(0,2):C.GC_1246,(0,3):C.GC_1246,(0,0):C.GC_983,(0,1):C.GC_1228})

V_827 = Vertex(name = 'V_827',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_148,(0,4):C.GC_869,(0,2):C.GC_867,(0,3):C.GC_867,(0,0):C.GC_1094,(0,1):C.GC_854})

V_828 = Vertex(name = 'V_828',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_880,(0,2):C.GC_879,(0,3):C.GC_879,(0,0):C.GC_1100,(0,1):C.GC_861})

V_829 = Vertex(name = 'V_829',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_182,(0,0):C.GC_22})

V_830 = Vertex(name = 'V_830',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_185})

V_831 = Vertex(name = 'V_831',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_143,(0,0):C.GC_83})

V_832 = Vertex(name = 'V_832',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_146})

V_833 = Vertex(name = 'V_833',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_143,(0,0):C.GC_83})

V_834 = Vertex(name = 'V_834',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_146})

V_835 = Vertex(name = 'V_835',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_155,(0,0):C.GC_86})

V_836 = Vertex(name = 'V_836',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_156,(0,0):C.GC_87})

V_837 = Vertex(name = 'V_837',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_157,(0,0):C.GC_88})

V_838 = Vertex(name = 'V_838',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_182,(0,0):C.GC_243})

V_839 = Vertex(name = 'V_839',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_186})

V_840 = Vertex(name = 'V_840',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_143,(0,0):C.GC_164})

V_841 = Vertex(name = 'V_841',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_147})

V_842 = Vertex(name = 'V_842',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_143,(0,0):C.GC_164})

V_843 = Vertex(name = 'V_843',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_147})

V_844 = Vertex(name = 'V_844',
               particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_155,(0,1):C.GC_155})

V_845 = Vertex(name = 'V_845',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_158,(0,0):C.GC_89})

V_846 = Vertex(name = 'V_846',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_159,(0,0):C.GC_90})

V_847 = Vertex(name = 'V_847',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_190,(0,4):C.GC_126,(0,2):C.GC_124,(0,3):C.GC_124,(0,0):C.GC_100,(0,1):C.GC_109})

V_848 = Vertex(name = 'V_848',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_137,(0,2):C.GC_136,(0,3):C.GC_136,(0,0):C.GC_105,(0,1):C.GC_116})

V_849 = Vertex(name = 'V_849',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_151,(0,4):C.GC_1240,(0,2):C.GC_1238,(0,3):C.GC_1238,(0,0):C.GC_979,(0,1):C.GC_1223})

V_850 = Vertex(name = 'V_850',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_1251,(0,2):C.GC_1250,(0,3):C.GC_1250,(0,0):C.GC_984,(0,1):C.GC_1230})

V_851 = Vertex(name = 'V_851',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_151,(0,4):C.GC_873,(0,2):C.GC_871,(0,3):C.GC_871,(0,0):C.GC_1096,(0,1):C.GC_856})

V_852 = Vertex(name = 'V_852',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_884,(0,2):C.GC_883,(0,3):C.GC_883,(0,0):C.GC_1101,(0,1):C.GC_863})

V_853 = Vertex(name = 'V_853',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_158,(0,0):C.GC_89})

V_854 = Vertex(name = 'V_854',
               particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_156,(0,1):C.GC_158})

V_855 = Vertex(name = 'V_855',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_183,(0,0):C.GC_23})

V_856 = Vertex(name = 'V_856',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_188})

V_857 = Vertex(name = 'V_857',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_144,(0,0):C.GC_84})

V_858 = Vertex(name = 'V_858',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_149})

V_859 = Vertex(name = 'V_859',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_144,(0,0):C.GC_84})

V_860 = Vertex(name = 'V_860',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_149})

V_861 = Vertex(name = 'V_861',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_156,(0,0):C.GC_91})

V_862 = Vertex(name = 'V_862',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_160,(0,0):C.GC_92})

V_863 = Vertex(name = 'V_863',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_161,(0,0):C.GC_93})

V_864 = Vertex(name = 'V_864',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_183,(0,0):C.GC_244})

V_865 = Vertex(name = 'V_865',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_189})

V_866 = Vertex(name = 'V_866',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_144,(0,0):C.GC_165})

V_867 = Vertex(name = 'V_867',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_150})

V_868 = Vertex(name = 'V_868',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_144,(0,0):C.GC_165})

V_869 = Vertex(name = 'V_869',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_150})

V_870 = Vertex(name = 'V_870',
               particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_160,(0,1):C.GC_160})

V_871 = Vertex(name = 'V_871',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_162,(0,0):C.GC_94})

V_872 = Vertex(name = 'V_872',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_193,(0,4):C.GC_130,(0,2):C.GC_128,(0,3):C.GC_128,(0,0):C.GC_102,(0,1):C.GC_111})

V_873 = Vertex(name = 'V_873',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_141,(0,2):C.GC_140,(0,3):C.GC_140,(0,0):C.GC_106,(0,1):C.GC_118})

V_874 = Vertex(name = 'V_874',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_154,(0,4):C.GC_1244,(0,2):C.GC_1242,(0,3):C.GC_1242,(0,0):C.GC_981,(0,1):C.GC_1225})

V_875 = Vertex(name = 'V_875',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_1255,(0,2):C.GC_1254,(0,3):C.GC_1254,(0,0):C.GC_985,(0,1):C.GC_1232})

V_876 = Vertex(name = 'V_876',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_154,(0,4):C.GC_877,(0,2):C.GC_875,(0,3):C.GC_875,(0,0):C.GC_1098,(0,1):C.GC_858})

V_877 = Vertex(name = 'V_877',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_888,(0,2):C.GC_887,(0,3):C.GC_887,(0,0):C.GC_1102,(0,1):C.GC_865})

V_878 = Vertex(name = 'V_878',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_159,(0,0):C.GC_90})

V_879 = Vertex(name = 'V_879',
               particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_157,(0,1):C.GC_159})

V_880 = Vertex(name = 'V_880',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_162,(0,0):C.GC_94})

V_881 = Vertex(name = 'V_881',
               particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_161,(0,1):C.GC_162})

V_882 = Vertex(name = 'V_882',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_184,(0,0):C.GC_24})

V_883 = Vertex(name = 'V_883',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_191})

V_884 = Vertex(name = 'V_884',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_145,(0,0):C.GC_85})

V_885 = Vertex(name = 'V_885',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_152})

V_886 = Vertex(name = 'V_886',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_145,(0,0):C.GC_85})

V_887 = Vertex(name = 'V_887',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_152})

V_888 = Vertex(name = 'V_888',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_157,(0,0):C.GC_95})

V_889 = Vertex(name = 'V_889',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_161,(0,0):C.GC_96})

V_890 = Vertex(name = 'V_890',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_163,(0,0):C.GC_97})

V_891 = Vertex(name = 'V_891',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_184,(0,0):C.GC_245})

V_892 = Vertex(name = 'V_892',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_192})

V_893 = Vertex(name = 'V_893',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_145,(0,0):C.GC_166})

V_894 = Vertex(name = 'V_894',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_153})

V_895 = Vertex(name = 'V_895',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_145,(0,0):C.GC_166})

V_896 = Vertex(name = 'V_896',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_153})

V_897 = Vertex(name = 'V_897',
               particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_163,(0,1):C.GC_163})

V_898 = Vertex(name = 'V_898',
               particles = [ P.a, P.a, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_494})

V_899 = Vertex(name = 'V_899',
               particles = [ P.g, P.g, P.H1 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS4, L.VVS5, L.VVS6, L.VVS7 ],
               couplings = {(0,0):C.GC_495,(0,2):C.GC_508,(0,1):C.GC_504,(0,3):C.GC_499})

V_900 = Vertex(name = 'V_900',
               particles = [ P.a, P.Z, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_498})

V_901 = Vertex(name = 'V_901',
               particles = [ P.a, P.Z1, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_498})

V_902 = Vertex(name = 'V_902',
               particles = [ P.a, P.Z1, P.H1 ],
               color = [ '1' ],
               lorentz = [ L.VVS4 ],
               couplings = {(0,0):C.GC_512})

V_903 = Vertex(name = 'V_903',
               particles = [ P.g, P.g, P.g, P.H1 ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVS10, L.VVVS6, L.VVVS7, L.VVVS8, L.VVVS9 ],
               couplings = {(0,3):C.GC_500,(0,0):C.GC_509,(0,4):C.GC_505,(0,2):C.GC_502,(0,1):C.GC_496})

V_904 = Vertex(name = 'V_904',
               particles = [ P.g, P.g, P.g, P.g, P.H1 ],
               color = [ 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)' ],
               lorentz = [ L.VVVVS1, L.VVVVS10, L.VVVVS11, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS15, L.VVVVS16, L.VVVVS18, L.VVVVS2, L.VVVVS20, L.VVVVS3, L.VVVVS5, L.VVVVS7, L.VVVVS8 ],
               couplings = {(2,5):C.GC_501,(2,8):C.GC_510,(1,4):C.GC_501,(1,10):C.GC_510,(2,6):C.GC_507,(0,11):C.GC_503,(0,12):C.GC_511,(1,7):C.GC_507,(0,3):C.GC_506,(1,2):C.GC_503,(2,1):C.GC_503,(0,9):C.GC_501,(1,13):C.GC_497,(0,0):C.GC_497,(2,14):C.GC_497})

