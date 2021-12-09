# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Sat 1 Aug 2020 04:47:56



from .object_library import all_parameters, Parameter


from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
CKMlambda = Parameter(name = 'CKMlambda',
                      nature = 'external',
                      type = 'real',
                      value = 0.2265,
                      texname = '\\text{CKMlambda}',
                      lhablock = 'CKMBLOCK',
                      lhacode = [ 2 ])

CKMA = Parameter(name = 'CKMA',
                 nature = 'external',
                 type = 'real',
                 value = 0.79,
                 texname = '\\text{CKMA}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 3 ])

CKMrho = Parameter(name = 'CKMrho',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\text{CKMrho}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 4 ])

CKMeta = Parameter(name = 'CKMeta',
                   nature = 'external',
                   type = 'real',
                   value = 0.357,
                   texname = '\\text{CKMeta}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 5 ])

cG = Parameter(name = 'cG',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_G',
               lhablock = 'SMEFT',
               lhacode = [ 1 ])

cW = Parameter(name = 'cW',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_W',
               lhablock = 'SMEFT',
               lhacode = [ 2 ])

cH = Parameter(name = 'cH',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_H',
               lhablock = 'SMEFT',
               lhacode = [ 3 ])

cHbox = Parameter(name = 'cHbox',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{H \\square }',
                  lhablock = 'SMEFT',
                  lhacode = [ 4 ])

cHDD = Parameter(name = 'cHDD',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HD}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 5 ])

cHG = Parameter(name = 'cHG',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HG}}',
                lhablock = 'SMEFT',
                lhacode = [ 6 ])

cHW = Parameter(name = 'cHW',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HW}}',
                lhablock = 'SMEFT',
                lhacode = [ 7 ])

cHB = Parameter(name = 'cHB',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HB}}',
                lhablock = 'SMEFT',
                lhacode = [ 8 ])

cHWB = Parameter(name = 'cHWB',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HWB}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 9 ])

ceH = Parameter(name = 'ceH',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{eH}}',
                lhablock = 'SMEFT',
                lhacode = [ 10 ])

cuH0 = Parameter(name = 'cuH0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uH}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 11 ])

cdH0 = Parameter(name = 'cdH0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dH}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 12 ])

ceW = Parameter(name = 'ceW',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{eW}}',
                lhablock = 'SMEFT',
                lhacode = [ 13 ])

ceB = Parameter(name = 'ceB',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{eB}}',
                lhablock = 'SMEFT',
                lhacode = [ 14 ])

cuG0 = Parameter(name = 'cuG0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uG}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 15 ])

cuW0 = Parameter(name = 'cuW0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uW}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 16 ])

cuB0 = Parameter(name = 'cuB0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uB}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 17 ])

cdG0 = Parameter(name = 'cdG0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dG}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 18 ])

cdW0 = Parameter(name = 'cdW0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dW}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 19 ])

cdB0 = Parameter(name = 'cdB0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dB}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 20 ])

cHl1 = Parameter(name = 'cHl1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hl}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 21 ])

cHl3 = Parameter(name = 'cHl3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hl}}^3',
                 lhablock = 'SMEFT',
                 lhacode = [ 22 ])

cHe = Parameter(name = 'cHe',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{He}}',
                lhablock = 'SMEFT',
                lhacode = [ 23 ])

cHq10 = Parameter(name = 'cHq10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Hq}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 24 ])

cHq30 = Parameter(name = 'cHq30',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Hq}}^3',
                  lhablock = 'SMEFT',
                  lhacode = [ 25 ])

cHu0 = Parameter(name = 'cHu0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hu}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 26 ])

cHd0 = Parameter(name = 'cHd0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hd}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 27 ])

cHud0 = Parameter(name = 'cHud0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Hud}}',
                  lhablock = 'SMEFT',
                  lhacode = [ 28 ])

cll = Parameter(name = 'cll',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ll}}',
                lhablock = 'SMEFT',
                lhacode = [ 29 ])

cll1 = Parameter(name = 'cll1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ll}}^{\\text{Prime}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 30 ])

cqq10 = Parameter(name = 'cqq10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qq}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 31 ])

cqq110 = Parameter(name = 'cqq110',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qq}}^{\\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 32 ])

cqq30 = Parameter(name = 'cqq30',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qq}}^3',
                  lhablock = 'SMEFT',
                  lhacode = [ 33 ])

cqq310 = Parameter(name = 'cqq310',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qq}}^{3 \\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 34 ])

clq10 = Parameter(name = 'clq10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{lq}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 35 ])

clq30 = Parameter(name = 'clq30',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{lq}}^3',
                  lhablock = 'SMEFT',
                  lhacode = [ 36 ])

cee = Parameter(name = 'cee',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ee}}',
                lhablock = 'SMEFT',
                lhacode = [ 37 ])

cuu0 = Parameter(name = 'cuu0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uu}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 38 ])

cuu10 = Parameter(name = 'cuu10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{uu}}^{\\text{Prime}}',
                  lhablock = 'SMEFT',
                  lhacode = [ 39 ])

cdd0 = Parameter(name = 'cdd0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dd}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 40 ])

cdd10 = Parameter(name = 'cdd10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{dd}}^{\\text{Prime}}',
                  lhablock = 'SMEFT',
                  lhacode = [ 41 ])

ceu0 = Parameter(name = 'ceu0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{eu}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 42 ])

ced0 = Parameter(name = 'ced0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ed}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 43 ])

cud10 = Parameter(name = 'cud10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ud}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 44 ])

cud80 = Parameter(name = 'cud80',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ud}}^8',
                  lhablock = 'SMEFT',
                  lhacode = [ 45 ])

cle = Parameter(name = 'cle',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{le}}',
                lhablock = 'SMEFT',
                lhacode = [ 46 ])

clu0 = Parameter(name = 'clu0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{lu}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 47 ])

cld0 = Parameter(name = 'cld0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ld}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 48 ])

cqe0 = Parameter(name = 'cqe0',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{qe}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 49 ])

cqu10 = Parameter(name = 'cqu10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qu}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 50 ])

cqu110 = Parameter(name = 'cqu110',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qu}}^{\\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 51 ])

cqu80 = Parameter(name = 'cqu80',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qu}}^8',
                  lhablock = 'SMEFT',
                  lhacode = [ 52 ])

cqu810 = Parameter(name = 'cqu810',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qu}}^{8 \\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 53 ])

cqd10 = Parameter(name = 'cqd10',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qd}}^1',
                  lhablock = 'SMEFT',
                  lhacode = [ 54 ])

cqd110 = Parameter(name = 'cqd110',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qd}}^{\\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 55 ])

cqd80 = Parameter(name = 'cqd80',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{qd}}^8',
                  lhablock = 'SMEFT',
                  lhacode = [ 56 ])

cqd810 = Parameter(name = 'cqd810',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{qd}}^{8 \\text{Prime}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 57 ])

cledq0 = Parameter(name = 'cledq0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{ledq}}',
                   lhablock = 'SMEFT',
                   lhacode = [ 58 ])

cquqd1 = Parameter(name = 'cquqd1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{quqd}}^1',
                   lhablock = 'SMEFT',
                   lhacode = [ 59 ])

cquqd11 = Parameter(name = 'cquqd11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{quqd}}^{\\text{Prime}}',
                    lhablock = 'SMEFT',
                    lhacode = [ 60 ])

cquqd8 = Parameter(name = 'cquqd8',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{quqd}}^8',
                   lhablock = 'SMEFT',
                   lhacode = [ 61 ])

cquqd81 = Parameter(name = 'cquqd81',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{quqd}}^{8 \\text{Prime}}',
                    lhablock = 'SMEFT',
                    lhacode = [ 62 ])

clequ10 = Parameter(name = 'clequ10',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{lequ}}^1',
                    lhablock = 'SMEFT',
                    lhacode = [ 63 ])

clequ30 = Parameter(name = 'clequ30',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{lequ}}^3',
                    lhablock = 'SMEFT',
                    lhacode = [ 64 ])

LambdaSMEFT = Parameter(name = 'LambdaSMEFT',
                        nature = 'external',
                        type = 'real',
                        value = 1000,
                        texname = '\\Lambda',
                        lhablock = 'SMEFTcutoff',
                        lhacode = [ 1 ])

DeltaucuH = Parameter(name = 'DeltaucuH',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{uH}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 1 ])

DeltadcuH = Parameter(name = 'DeltadcuH',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{uH}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 2 ])

DeltaucdH = Parameter(name = 'DeltaucdH',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{dH}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 3 ])

DeltadcdH = Parameter(name = 'DeltadcdH',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{dH}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 4 ])

DeltaucuG = Parameter(name = 'DeltaucuG',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{uG}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 5 ])

DeltadcuG = Parameter(name = 'DeltadcuG',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{uG}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 6 ])

DeltaucuW = Parameter(name = 'DeltaucuW',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{uW}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 7 ])

DeltadcuW = Parameter(name = 'DeltadcuW',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{uW}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 8 ])

DeltaucuB = Parameter(name = 'DeltaucuB',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{uB}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 9 ])

DeltadcuB = Parameter(name = 'DeltadcuB',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{uB}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 10 ])

DeltaucdG = Parameter(name = 'DeltaucdG',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{dG}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 11 ])

DeltadcdG = Parameter(name = 'DeltadcdG',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{dG}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 12 ])

DeltaucdW = Parameter(name = 'DeltaucdW',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{dW}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 13 ])

DeltadcdW = Parameter(name = 'DeltadcdW',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{dW}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 14 ])

DeltaucdB = Parameter(name = 'DeltaucdB',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{dB}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 15 ])

DeltadcdB = Parameter(name = 'DeltadcdB',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{dB}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 16 ])

DeltaucHq1 = Parameter(name = 'DeltaucHq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{Hq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 17 ])

DeltadcHq1 = Parameter(name = 'DeltadcHq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{Hq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 18 ])

DeltaucHq3 = Parameter(name = 'DeltaucHq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{Hq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 19 ])

DeltadcHq3 = Parameter(name = 'DeltadcHq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{Hq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 20 ])

DeltacHu = Parameter(name = 'DeltacHu',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{Hu}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 21 ])

DeltacHd = Parameter(name = 'DeltacHd',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{Hd}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 22 ])

Deltaucqq1 = Parameter(name = 'Deltaucqq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{qq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 23 ])

Deltadcqq1 = Parameter(name = 'Deltadcqq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{qq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 24 ])

Deltaucqq11 = Parameter(name = 'Deltaucqq11',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^u c_{\\text{qq}}^{1 \\text{Prime}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 25 ])

Deltadcqq11 = Parameter(name = 'Deltadcqq11',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^d c_{\\text{qq}}^{1 \\text{Prime}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 26 ])

Deltaucqq3 = Parameter(name = 'Deltaucqq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{qq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 27 ])

Deltadcqq3 = Parameter(name = 'Deltadcqq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{qq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 28 ])

Deltaucqq31 = Parameter(name = 'Deltaucqq31',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^u c_{\\text{qq}}^{3 \\text{Prime}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 29 ])

Deltadcqq31 = Parameter(name = 'Deltadcqq31',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^d c_{\\text{qq}}^{3 \\text{Prime}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 30 ])

Deltauclq1 = Parameter(name = 'Deltauclq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{lq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 31 ])

Deltadclq1 = Parameter(name = 'Deltadclq1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{lq}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 32 ])

Deltauclq3 = Parameter(name = 'Deltauclq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{lq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 33 ])

Deltadclq3 = Parameter(name = 'Deltadclq3',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{lq}}^3',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 34 ])

Deltacuu = Parameter(name = 'Deltacuu',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{uu}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 35 ])

Deltacuu1 = Parameter(name = 'Deltacuu1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{$\\Delta $c}_{\\text{uu}}^{\\text{Prime}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 36 ])

Deltacdd = Parameter(name = 'Deltacdd',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{dd}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 37 ])

Deltacdd1 = Parameter(name = 'Deltacdd1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{$\\Delta $c}_{\\text{dd}}^{\\text{Prime}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 38 ])

Deltaceu = Parameter(name = 'Deltaceu',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{eu}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 39 ])

Deltaced = Parameter(name = 'Deltaced',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{ed}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 40 ])

Deltaucud1 = Parameter(name = 'Deltaucud1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{ud}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 41 ])

Deltadcud1 = Parameter(name = 'Deltadcud1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{ud}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 42 ])

Deltaucud8 = Parameter(name = 'Deltaucud8',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^u c_{\\text{ud}}^8',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 43 ])

Deltadcud8 = Parameter(name = 'Deltadcud8',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta ^d c_{\\text{ud}}^8',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 44 ])

Deltaclu = Parameter(name = 'Deltaclu',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{lu}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 45 ])

Deltacld = Parameter(name = 'Deltacld',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{$\\Delta $c}_{\\text{ld}}',
                     lhablock = 'SMEFTFV',
                     lhacode = [ 46 ])

Deltaucqe = Parameter(name = 'Deltaucqe',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^u c_{\\text{qe}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 47 ])

Deltadcqe = Parameter(name = 'Deltadcqe',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\Delta ^d c_{\\text{qe}}',
                      lhablock = 'SMEFTFV',
                      lhacode = [ 48 ])

Delta1ucqu1 = Parameter(name = 'Delta1ucqu1',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^u c_{\\text{qu}}^1',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 49 ])

Delta1dcqu1 = Parameter(name = 'Delta1dcqu1',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^d c_{\\text{qu}}^1',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 50 ])

Delta2cqu1 = Parameter(name = 'Delta2cqu1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta _2 c_{\\text{qu}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 51 ])

Delta1ucqu8 = Parameter(name = 'Delta1ucqu8',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^u c_{\\text{qu}}^8',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 52 ])

Delta1dcqu8 = Parameter(name = 'Delta1dcqu8',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^d c_{\\text{qu}}^8',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 53 ])

Delta2cqu8 = Parameter(name = 'Delta2cqu8',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta _2 c_{\\text{qu}}^8',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 54 ])

Delta1ucqd1 = Parameter(name = 'Delta1ucqd1',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^u c_{\\text{qd}}^1',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 55 ])

Delta1dcqd1 = Parameter(name = 'Delta1dcqd1',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^d c_{\\text{qd}}^1',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 56 ])

Delta2cqd1 = Parameter(name = 'Delta2cqd1',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta _2 c_{\\text{qd}}^1',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 57 ])

Delta1ucqd8 = Parameter(name = 'Delta1ucqd8',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^u c_{\\text{qd}}^8',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 58 ])

Delta1dcqd8 = Parameter(name = 'Delta1dcqd8',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta _1^d c_{\\text{qd}}^8',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 59 ])

Delta2cqd8 = Parameter(name = 'Delta2cqd8',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\Delta _2 c_{\\text{qd}}^8',
                       lhablock = 'SMEFTFV',
                       lhacode = [ 60 ])

Deltaucledq = Parameter(name = 'Deltaucledq',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^u c_{\\text{ledq}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 61 ])

Deltadcledq = Parameter(name = 'Deltadcledq',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\Delta ^d c_{\\text{ledq}}',
                        lhablock = 'SMEFTFV',
                        lhacode = [ 62 ])

Deltauclequ1 = Parameter(name = 'Deltauclequ1',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\Delta ^u c_{\\text{lequ}}^1',
                         lhablock = 'SMEFTFV',
                         lhacode = [ 63 ])

Deltadclequ1 = Parameter(name = 'Deltadclequ1',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\Delta ^d c_{\\text{lequ}}^1',
                         lhablock = 'SMEFTFV',
                         lhacode = [ 64 ])

Deltauclequ3 = Parameter(name = 'Deltauclequ3',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\Delta ^u c_{\\text{lequ}}^3',
                         lhablock = 'SMEFTFV',
                         lhacode = [ 65 ])

Deltadclequ3 = Parameter(name = 'Deltadclequ3',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\Delta ^d c_{\\text{lequ}}^3',
                         lhablock = 'SMEFTFV',
                         lhacode = [ 66 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.387,
               texname = '\\text{MW}',
               lhablock = 'SMINPUTS',
               lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1179,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

linearPropCorrections = Parameter(name = 'linearPropCorrections',
                                  nature = 'external',
                                  type = 'real',
                                  value = 0,
                                  texname = '\\text{linearPropCorrections}',
                                  lhablock = 'SWITCHES',
                                  lhacode = [ 1 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00467,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00216,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.093,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00216,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.76,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00467,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.093,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.18,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.33,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

MWsm = Parameter(name = 'MWsm',
                 nature = 'internal',
                 type = 'real',
                 value = 'MW',
                 texname = '\\text{MWsm}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MW**2*(1 - MW**2/MZ**2)*cmath.sqrt(2))/cmath.pi',
                texname = '\\alpha _{\\text{EW}}')

vevhat = Parameter(name = 'vevhat',
                   nature = 'internal',
                   type = 'real',
                   value = '1/(2**0.25*cmath.sqrt(Gf))',
                   texname = '\\hat{v}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MH**2)/cmath.sqrt(2)',
                texname = '\\text{lam}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

sth2 = Parameter(name = 'sth2',
                 nature = 'internal',
                 type = 'real',
                 value = '1 - MW**2/MZ**2',
                 texname = '\\text{sth2}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMlambda',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-CKMlambda',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**2',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(1 - CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMA*CKMlambda**2)',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

propCorr = Parameter(name = 'propCorr',
                     nature = 'internal',
                     type = 'real',
                     value = 'abs(linearPropCorrections)/(abs(linearPropCorrections) + 10**-40)',
                     texname = '\\Delta _{\\text{prop.}}')

MZ1 = Parameter(name = 'MZ1',
                nature = 'internal',
                type = 'real',
                value = 'MZ',
                texname = '\\text{MZ}\'')

MH1 = Parameter(name = 'MH1',
                nature = 'internal',
                type = 'real',
                value = 'MH',
                texname = '\\text{MH}\'')

MT1 = Parameter(name = 'MT1',
                nature = 'internal',
                type = 'real',
                value = 'MT',
                texname = '\\text{MT}\'')

WZ1 = Parameter(name = 'WZ1',
                nature = 'internal',
                type = 'real',
                value = 'WZ',
                texname = '\\text{WZ}\'')

WW1 = Parameter(name = 'WW1',
                nature = 'internal',
                type = 'real',
                value = 'WW',
                texname = '\\text{WW}\'')

WH1 = Parameter(name = 'WH1',
                nature = 'internal',
                type = 'real',
                value = 'WH',
                texname = '\\text{WH}\'')

WT1 = Parameter(name = 'WT1',
                nature = 'internal',
                type = 'real',
                value = 'WT',
                texname = '\\text{WT}\'')

gHgg2 = Parameter(name = 'gHgg2',
                  nature = 'internal',
                  type = 'real',
                  value = '(-7*aS)/(720.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^2')

gHgg4 = Parameter(name = 'gHgg4',
                  nature = 'internal',
                  type = 'real',
                  value = 'aS/(360.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^4')

gHgg5 = Parameter(name = 'gHgg5',
                  nature = 'internal',
                  type = 'real',
                  value = 'aS/(20.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^5')

cth = Parameter(name = 'cth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - sth2)',
                texname = 'c_{\\theta }')

MW1 = Parameter(name = 'MW1',
                nature = 'internal',
                type = 'real',
                value = 'MWsm',
                texname = '\\text{MW}\'')

sth = Parameter(name = 'sth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(sth2)',
                texname = 's_{\\theta }')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vevhat',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vevhat',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vevhat',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vevhat',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vevhat',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vevhat',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vevhat',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vevhat',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vevhat',
                texname = '\\text{yup}')

gHgg1 = Parameter(name = 'gHgg1',
                  nature = 'internal',
                  type = 'real',
                  value = 'G**2/(48.*cmath.pi**2)',
                  texname = 'g_{\\text{HGG}}^1')

gHgg3 = Parameter(name = 'gHgg3',
                  nature = 'internal',
                  type = 'real',
                  value = '(aS*G)/(60.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^3')

dGf = Parameter(name = 'dGf',
                nature = 'internal',
                type = 'real',
                value = '((2*cHl3 - cll1)*vevhat**2)/LambdaSMEFT**2',
                texname = '\\text{dGf}')

dkH = Parameter(name = 'dkH',
                nature = 'internal',
                type = 'real',
                value = '((cHbox - cHDD/4.)*vevhat**2)/LambdaSMEFT**2',
                texname = '\\text{dkH}')

vevT = Parameter(name = 'vevT',
                 nature = 'internal',
                 type = 'real',
                 value = '(1 + dGf/2.)*vevhat',
                 texname = '\\text{vevT}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cth',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sth',
               texname = 'g_w')

gHaa = Parameter(name = 'gHaa',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(-1.75 + (4*(0.3333333333333333 + (7*MH**2)/(360.*MT**2)))/3. - (29*MH**6)/(16800.*MWsm**6) - (19*MH**4)/(1680.*MWsm**4) - (11*MH**2)/(120.*MWsm**2)))/(8.*cmath.pi**2)',
                 texname = 'g_{\\text{H$\\gamma \\gamma $}}')

gHza = Parameter(name = 'gHza',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(((0.4583333333333333 + (29*MH**6)/(100800.*MWsm**6) + (19*MH**4)/(10080.*MWsm**4) + (11*MH**2)/(720.*MWsm**2) + (MH**4*MZ**2)/(2100.*MWsm**6) + (MH**2*MZ**2)/(280.*MWsm**4) + (7*MZ**2)/(180.*MWsm**2) + (67*MH**2*MZ**4)/(100800.*MWsm**6) + (53*MZ**4)/(10080.*MWsm**4) + (43*MZ**6)/(50400.*MWsm**6) - (31*cth**2)/(24.*sth**2) - (29*cth**2*MH**6)/(20160.*MWsm**6*sth**2) - (19*cth**2*MH**4)/(2016.*MWsm**4*sth**2) - (11*cth**2*MH**2)/(144.*MWsm**2*sth**2) - (cth**2*MH**4*MZ**2)/(560.*MWsm**6*sth**2) - (31*cth**2*MH**2*MZ**2)/(2520.*MWsm**4*sth**2) - (cth**2*MZ**2)/(9.*MWsm**2*sth**2) - (43*cth**2*MH**2*MZ**4)/(20160.*MWsm**6*sth**2) - (17*cth**2*MZ**4)/(1120.*MWsm**4*sth**2) - (5*cth**2*MZ**6)/(2016.*MWsm**6*sth**2))*sth)/cth + ((0.3333333333333333 + (7*MH**2)/(360.*MT**2) + (11*MZ**2)/(360.*MT**2))*(0.5 - (4*sth**2)/3.))/(cth*sth)))/(4.*cmath.pi**2)',
                 texname = 'g_{\\text{HZ$\\gamma $}}')

dMZ2 = Parameter(name = 'dMZ2',
                 nature = 'internal',
                 type = 'real',
                 value = '((cHDD/2. + 2*cHWB*cth*sth)*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMZ2}')

dMH2 = Parameter(name = 'dMH2',
                 nature = 'internal',
                 type = 'real',
                 value = '2*dkH - (3*cH*vevhat**2)/(2.*lam*LambdaSMEFT**2)',
                 texname = '\\text{dMH2}')

dgw = Parameter(name = 'dgw',
                nature = 'internal',
                type = 'real',
                value = '-dGf/2.',
                texname = '\\text{dgw}')

barlam = Parameter(name = 'barlam',
                   nature = 'internal',
                   type = 'real',
                   value = '(1 - dGf - dMH2)*lam',
                   texname = '\\text{barlam}')

dWT = Parameter(name = 'dWT',
                nature = 'internal',
                type = 'real',
                value = 'WT*(-1 + 2*dgw + (ee*(((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4)*(LambdaSMEFT**2 + 2*vevhat**2*(cHq30 + DeltadcHq3*yb**2)) + 6*cHud0*MB*MT*MWsm**2*vevhat**2*yb*yt + 2*DeltaucHq3*((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4)*vevhat**2*yt**2) + 12*MWsm**2*sth*vevhat*(-(MB*(MB**2 - MT**2 - MWsm**2)*yb*(cdW0 + DeltadcdW*yb**2)) + MT*(MB**2 - MT**2 + MWsm**2)*(cuW0 + DeltadcuW*yb**2)*yt + DeltaucdW*MB*(-MB**2 + MT**2 + MWsm**2)*yb*yt**2 + DeltaucuW*MT*(MB**2 - MT**2 + MWsm**2)*yt**3)*cmath.sqrt(2))/(ee*LambdaSMEFT**2*((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4)))',
                texname = '\\text{dWT}')

dWW = Parameter(name = 'dWW',
                nature = 'internal',
                type = 'real',
                value = '(2*dgw + (2*(cHl3 + 2*cHq30)*vevhat**2)/(3.*LambdaSMEFT**2))*WW',
                texname = '\\text{dWW}')

gwsh = Parameter(name = 'gwsh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dgw - (cHW*vevhat**2)/LambdaSMEFT**2))/sth',
                 texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(1 - (3*cH*vevhat**2)/(8.*lam*LambdaSMEFT**2))*vevT',
                texname = '\\text{vev}')

dg1 = Parameter(name = 'dg1',
                nature = 'internal',
                type = 'real',
                value = '(-dGf - dMZ2/sth**2)/2.',
                texname = '\\text{dg1}')

dWHc = Parameter(name = 'dWHc',
                 nature = 'internal',
                 type = 'real',
                 value = 'yc/(yc + 10**-40)*(-0.02884*dGf + 0.05768*dkH - (0.05768*vevhat**2*(cuH0 + DeltaucuH*yc**2))/LambdaSMEFT**2)',
                 texname='\\text{dWHc}')

dWHb = Parameter(name = 'dWHb',
                 nature = 'internal',
                 type = 'real',
                 value = 'yb/(yb + 10**-40)*(-0.5809000000000001*dGf + 1.1618*dkH - (1.1618*vevhat**2*(cdH0 + DeltadcdH*yb**2 + DeltaucdH*yt**2))/LambdaSMEFT**2)',
                 texname='\\text{dWHb}')

dWHta = Parameter(name = 'dWHta',
                 nature = 'internal',
                 type = 'real',
                 value = 'ytau/(ytau + 10**-40)*(-0.06256*(dGf - 2.*dkH + (2.*ceH*vevhat**2)/LambdaSMEFT**2))',
                 texname='\\text{dWHta}')

dWH = Parameter(name = 'dWH',
                nature = 'internal',
                type = 'real',
                 value = 'WH*(-0.24161*dGf + 0.96644*dgw + 0.48322*dkH - 0.11186509426655465*dWW + (0.17608307708657758*cHl3*vevhat**2)/LambdaSMEFT**2 + (0.3641037844923821*cHq30*vevhat**2)/LambdaSMEFT**2 + (0.1636*cHG*MT**2*vevhat**2)/(LambdaSMEFT**2*(-0.5*gHgg2*MH**2 + gHgg1*MT**2)) + (cHW*(-0.3593778511706701*gHaa*gHza + 0.006164*cth*gHaa*sth + 0.00454*gHza*sth**2)*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHWB*(-0.00454*cth*gHza*sth + gHaa*(-0.0030819999999999997 + 0.006163999999999999*sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHB*(-0.006163999999999999*cth*gHaa*sth - 0.00454*gHza*(-1. + sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + dWHc + dWHb + dWHta)',
                texname = '\\text{dWH}')

dWZ = Parameter(name = 'dWZ',
                nature = 'internal',
                type = 'real',
                value = 'WZ*(-1 + (54*ee*LambdaSMEFT**2*MZ**3 + 108*dgw*ee*LambdaSMEFT**2*MZ**3 - 9*ee*LambdaSMEFT**2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) - 18*dgw*ee*LambdaSMEFT**2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + 9*ee*LambdaSMEFT**2*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 18*dgw*ee*LambdaSMEFT**2*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 6*cHWB*cth*ee*(-7*MB**2 + MZ**2)*sth*vevhat**2*cmath.sqrt(-4*MB**2 + MZ**2) - 108*cth*MB*MZ**2*sth**2*vevhat*yb*(cdB0 + DeltadcdB*yb**2 + DeltaucdB*yt**2)*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) + 144*cth*MB*MZ**2*sth**4*vevhat*yb*(cdB0 + DeltadcdB*yb**2 + DeltaucdB*yt**2)*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) - 108*MB*MZ**2*sth*vevhat*yb*(cdW0 + DeltadcdW*yb**2 + DeltaucdW*yt**2)*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) + 252*MB*MZ**2*sth**3*vevhat*yb*(cdW0 + DeltadcdW*yb**2 + DeltaucdW*yt**2)*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) - 144*MB*MZ**2*sth**5*vevhat*yb*(cdW0 + DeltadcdW*yb**2 + DeltaucdW*yt**2)*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) - 6*ee*LambdaSMEFT**2*sth**2*(18*(1 + dg1 + dgw)*MZ**3 + (4 + 11*dg1 - 3*dgw)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + (2 + dg1 + 3*dgw)*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2)) - 12*ee*sth**2*vevhat**2*((2*cHd0 + 3*cHe + 3*cHl1 + 3*cHl3 - 2*cHq10 + 6*cHq30 - 4*cHu0)*MZ**3 + 2*cHd0*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*cHq10*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*cHq30*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + cHd0*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + cHq10*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + cHq30*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*DeltacHd*MB**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*DeltadcHq1*MB**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*DeltadcHq3*MB**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + DeltacHd*MZ**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + DeltadcHq1*MZ**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + DeltadcHq3*MZ**2*yb**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*DeltaucHq1*MB**2*yt**2*cmath.sqrt(-4*MB**2 + MZ**2) + 2*DeltaucHq3*MB**2*yt**2*cmath.sqrt(-4*MB**2 + MZ**2) + DeltaucHq1*MZ**2*yt**2*cmath.sqrt(-4*MB**2 + MZ**2) + DeltaucHq3*MZ**2*yt**2*cmath.sqrt(-4*MB**2 + MZ**2)) + 8*(1 + 4*dg1 - 2*dgw)*ee*LambdaSMEFT**2*sth**4*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) - 16*(dg1 - dgw)*ee*LambdaSMEFT**2*sth**6*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) + 16*cHWB*cth*ee*sth**3*vevhat**2*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) - 16*cHWB*cth*ee*sth**5*vevhat**2*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) + 18*ee*vevhat**2*(2*cHl3*MZ**3 + (3*cHd0 - cHq10)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + (cHq10*MZ**2 + 3*DeltacHd*MB**2*yb**2 - (MB - MZ)*(MB + MZ)*((DeltadcHq1 + DeltadcHq3)*yb**2 + (DeltaucHq1 + DeltaucHq3)*yt**2))*cmath.sqrt(-4*MB**2 + MZ**2) + cHq30*(-(MB**2*cmath.sqrt(-4*MB**2 + MZ**2)) + MZ**2*(4*MZ + cmath.sqrt(-4*MB**2 + MZ**2)))))/(ee*LambdaSMEFT**2*(2*MZ**3*(27 - 54*sth**2 + 76*sth**4) + MZ**2*(9 - 12*sth**2 + 8*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2) + MB**2*(-9 - 24*sth**2 + 16*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2))))',
                texname = '\\text{dWZ}')

g1sh = Parameter(name = 'g1sh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dg1 - (cHB*vevhat**2)/LambdaSMEFT**2))/cth',
                 texname = 'g_1')

