# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Sat 9 Jan 2021 13:22:45



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

ceHRe11 = Parameter(name = 'ceHRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 10 ])

ceHRe22 = Parameter(name = 'ceHRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 11 ])

ceHRe33 = Parameter(name = 'ceHRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 12 ])

ceHRe12 = Parameter(name = 'ceHRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 13 ])

ceHRe13 = Parameter(name = 'ceHRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 14 ])

ceHRe23 = Parameter(name = 'ceHRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 15 ])

ceHRe21 = Parameter(name = 'ceHRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 16 ])

ceHRe31 = Parameter(name = 'ceHRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 17 ])

ceHRe32 = Parameter(name = 'ceHRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 18 ])

cuHRe11 = Parameter(name = 'cuHRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 19 ])

cuHRe22 = Parameter(name = 'cuHRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 20 ])

cuHRe33 = Parameter(name = 'cuHRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 21 ])

cuHRe12 = Parameter(name = 'cuHRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 22 ])

cuHRe13 = Parameter(name = 'cuHRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 23 ])

cuHRe23 = Parameter(name = 'cuHRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 24 ])

cuHRe21 = Parameter(name = 'cuHRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 25 ])

cuHRe31 = Parameter(name = 'cuHRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 26 ])

cuHRe32 = Parameter(name = 'cuHRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 27 ])

cdHRe11 = Parameter(name = 'cdHRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 28 ])

cdHRe22 = Parameter(name = 'cdHRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 29 ])

cdHRe33 = Parameter(name = 'cdHRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 30 ])

cdHRe12 = Parameter(name = 'cdHRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 31 ])

cdHRe13 = Parameter(name = 'cdHRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 32 ])

cdHRe23 = Parameter(name = 'cdHRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 33 ])

cdHRe21 = Parameter(name = 'cdHRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 34 ])

cdHRe31 = Parameter(name = 'cdHRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 35 ])

cdHRe32 = Parameter(name = 'cdHRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 36 ])

ceWRe11 = Parameter(name = 'ceWRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 37 ])

ceWRe22 = Parameter(name = 'ceWRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 38 ])

ceWRe33 = Parameter(name = 'ceWRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 39 ])

ceWRe12 = Parameter(name = 'ceWRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 40 ])

ceWRe13 = Parameter(name = 'ceWRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 41 ])

ceWRe23 = Parameter(name = 'ceWRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 42 ])

ceWRe21 = Parameter(name = 'ceWRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 43 ])

ceWRe31 = Parameter(name = 'ceWRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 44 ])

ceWRe32 = Parameter(name = 'ceWRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 45 ])

ceBRe11 = Parameter(name = 'ceBRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 46 ])

ceBRe22 = Parameter(name = 'ceBRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 47 ])

ceBRe33 = Parameter(name = 'ceBRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 48 ])

ceBRe12 = Parameter(name = 'ceBRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 49 ])

ceBRe13 = Parameter(name = 'ceBRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 50 ])

ceBRe23 = Parameter(name = 'ceBRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 51 ])

ceBRe21 = Parameter(name = 'ceBRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 52 ])

ceBRe31 = Parameter(name = 'ceBRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 53 ])

ceBRe32 = Parameter(name = 'ceBRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 54 ])

cuGRe11 = Parameter(name = 'cuGRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 55 ])

cuGRe22 = Parameter(name = 'cuGRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 56 ])

cuGRe33 = Parameter(name = 'cuGRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 57 ])

cuGRe12 = Parameter(name = 'cuGRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 58 ])

cuGRe13 = Parameter(name = 'cuGRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 59 ])

cuGRe23 = Parameter(name = 'cuGRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 60 ])

cuGRe21 = Parameter(name = 'cuGRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 61 ])

cuGRe31 = Parameter(name = 'cuGRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 62 ])

cuGRe32 = Parameter(name = 'cuGRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 63 ])

cuWRe11 = Parameter(name = 'cuWRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 64 ])

cuWRe22 = Parameter(name = 'cuWRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 65 ])

cuWRe33 = Parameter(name = 'cuWRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 66 ])

cuWRe12 = Parameter(name = 'cuWRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 67 ])

cuWRe13 = Parameter(name = 'cuWRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 68 ])

cuWRe23 = Parameter(name = 'cuWRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 69 ])

cuWRe21 = Parameter(name = 'cuWRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 70 ])

cuWRe31 = Parameter(name = 'cuWRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 71 ])

cuWRe32 = Parameter(name = 'cuWRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 72 ])

cuBRe11 = Parameter(name = 'cuBRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 73 ])

cuBRe22 = Parameter(name = 'cuBRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 74 ])

cuBRe33 = Parameter(name = 'cuBRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 75 ])

cuBRe12 = Parameter(name = 'cuBRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 76 ])

cuBRe13 = Parameter(name = 'cuBRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 77 ])

cuBRe23 = Parameter(name = 'cuBRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 78 ])

cuBRe21 = Parameter(name = 'cuBRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 79 ])

cuBRe31 = Parameter(name = 'cuBRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 80 ])

cuBRe32 = Parameter(name = 'cuBRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 81 ])

cdGRe11 = Parameter(name = 'cdGRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 82 ])

cdGRe22 = Parameter(name = 'cdGRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 83 ])

cdGRe33 = Parameter(name = 'cdGRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 84 ])

cdGRe12 = Parameter(name = 'cdGRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 85 ])

cdGRe13 = Parameter(name = 'cdGRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 86 ])

cdGRe23 = Parameter(name = 'cdGRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 87 ])

cdGRe21 = Parameter(name = 'cdGRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 88 ])

cdGRe31 = Parameter(name = 'cdGRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 89 ])

cdGRe32 = Parameter(name = 'cdGRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 90 ])

cdWRe11 = Parameter(name = 'cdWRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 91 ])

cdWRe22 = Parameter(name = 'cdWRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 92 ])

cdWRe33 = Parameter(name = 'cdWRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 93 ])

cdWRe12 = Parameter(name = 'cdWRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 94 ])

cdWRe13 = Parameter(name = 'cdWRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 95 ])

cdWRe23 = Parameter(name = 'cdWRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 96 ])

cdWRe21 = Parameter(name = 'cdWRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 97 ])

cdWRe31 = Parameter(name = 'cdWRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 98 ])

cdWRe32 = Parameter(name = 'cdWRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 99 ])

cdBRe11 = Parameter(name = 'cdBRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 100 ])

cdBRe22 = Parameter(name = 'cdBRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 101 ])

cdBRe33 = Parameter(name = 'cdBRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 102 ])

cdBRe12 = Parameter(name = 'cdBRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 103 ])

cdBRe13 = Parameter(name = 'cdBRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 104 ])

cdBRe23 = Parameter(name = 'cdBRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 105 ])

cdBRe21 = Parameter(name = 'cdBRe21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe21}',
                    lhablock = 'SMEFT',
                    lhacode = [ 106 ])

cdBRe31 = Parameter(name = 'cdBRe31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe31}',
                    lhablock = 'SMEFT',
                    lhacode = [ 107 ])

cdBRe32 = Parameter(name = 'cdBRe32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBRe32}',
                    lhablock = 'SMEFT',
                    lhacode = [ 108 ])

cHl1Re11 = Parameter(name = 'cHl1Re11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re11}',
                     lhablock = 'SMEFT',
                     lhacode = [ 109 ])

cHl1Re12 = Parameter(name = 'cHl1Re12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re12}',
                     lhablock = 'SMEFT',
                     lhacode = [ 110 ])

cHl1Re13 = Parameter(name = 'cHl1Re13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re13}',
                     lhablock = 'SMEFT',
                     lhacode = [ 111 ])

cHl1Re22 = Parameter(name = 'cHl1Re22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re22}',
                     lhablock = 'SMEFT',
                     lhacode = [ 112 ])

cHl1Re23 = Parameter(name = 'cHl1Re23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re23}',
                     lhablock = 'SMEFT',
                     lhacode = [ 113 ])

cHl1Re33 = Parameter(name = 'cHl1Re33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Re33}',
                     lhablock = 'SMEFT',
                     lhacode = [ 114 ])

cHl3Re11 = Parameter(name = 'cHl3Re11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re11}',
                     lhablock = 'SMEFT',
                     lhacode = [ 115 ])

cHl3Re12 = Parameter(name = 'cHl3Re12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re12}',
                     lhablock = 'SMEFT',
                     lhacode = [ 116 ])

cHl3Re13 = Parameter(name = 'cHl3Re13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re13}',
                     lhablock = 'SMEFT',
                     lhacode = [ 117 ])

cHl3Re22 = Parameter(name = 'cHl3Re22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re22}',
                     lhablock = 'SMEFT',
                     lhacode = [ 118 ])

cHl3Re23 = Parameter(name = 'cHl3Re23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re23}',
                     lhablock = 'SMEFT',
                     lhacode = [ 119 ])

cHl3Re33 = Parameter(name = 'cHl3Re33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Re33}',
                     lhablock = 'SMEFT',
                     lhacode = [ 120 ])

cHq1Re11 = Parameter(name = 'cHq1Re11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re11}',
                     lhablock = 'SMEFT',
                     lhacode = [ 121 ])

cHq1Re12 = Parameter(name = 'cHq1Re12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re12}',
                     lhablock = 'SMEFT',
                     lhacode = [ 122 ])

cHq1Re13 = Parameter(name = 'cHq1Re13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re13}',
                     lhablock = 'SMEFT',
                     lhacode = [ 123 ])

cHq1Re22 = Parameter(name = 'cHq1Re22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re22}',
                     lhablock = 'SMEFT',
                     lhacode = [ 124 ])

cHq1Re23 = Parameter(name = 'cHq1Re23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re23}',
                     lhablock = 'SMEFT',
                     lhacode = [ 125 ])

cHq1Re33 = Parameter(name = 'cHq1Re33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Re33}',
                     lhablock = 'SMEFT',
                     lhacode = [ 126 ])

cHq3Re11 = Parameter(name = 'cHq3Re11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re11}',
                     lhablock = 'SMEFT',
                     lhacode = [ 127 ])

cHq3Re12 = Parameter(name = 'cHq3Re12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re12}',
                     lhablock = 'SMEFT',
                     lhacode = [ 128 ])

cHq3Re13 = Parameter(name = 'cHq3Re13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re13}',
                     lhablock = 'SMEFT',
                     lhacode = [ 129 ])

cHq3Re22 = Parameter(name = 'cHq3Re22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re22}',
                     lhablock = 'SMEFT',
                     lhacode = [ 130 ])

cHq3Re23 = Parameter(name = 'cHq3Re23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re23}',
                     lhablock = 'SMEFT',
                     lhacode = [ 131 ])

cHq3Re33 = Parameter(name = 'cHq3Re33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Re33}',
                     lhablock = 'SMEFT',
                     lhacode = [ 132 ])

cHeRe11 = Parameter(name = 'cHeRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 133 ])

cHeRe12 = Parameter(name = 'cHeRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 134 ])

cHeRe13 = Parameter(name = 'cHeRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 135 ])

cHeRe22 = Parameter(name = 'cHeRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 136 ])

cHeRe23 = Parameter(name = 'cHeRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 137 ])

cHeRe33 = Parameter(name = 'cHeRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 138 ])

cHuRe11 = Parameter(name = 'cHuRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 139 ])

cHuRe12 = Parameter(name = 'cHuRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 140 ])

cHuRe13 = Parameter(name = 'cHuRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 141 ])

cHuRe22 = Parameter(name = 'cHuRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 142 ])

cHuRe23 = Parameter(name = 'cHuRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 143 ])

cHuRe33 = Parameter(name = 'cHuRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 144 ])

cHdRe11 = Parameter(name = 'cHdRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 145 ])

cHdRe12 = Parameter(name = 'cHdRe12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe12}',
                    lhablock = 'SMEFT',
                    lhacode = [ 146 ])

cHdRe13 = Parameter(name = 'cHdRe13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe13}',
                    lhablock = 'SMEFT',
                    lhacode = [ 147 ])

cHdRe22 = Parameter(name = 'cHdRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 148 ])

cHdRe23 = Parameter(name = 'cHdRe23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe23}',
                    lhablock = 'SMEFT',
                    lhacode = [ 149 ])

cHdRe33 = Parameter(name = 'cHdRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 150 ])

cHudRe11 = Parameter(name = 'cHudRe11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe11}',
                     lhablock = 'SMEFT',
                     lhacode = [ 151 ])

cHudRe22 = Parameter(name = 'cHudRe22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe22}',
                     lhablock = 'SMEFT',
                     lhacode = [ 152 ])

cHudRe33 = Parameter(name = 'cHudRe33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe33}',
                     lhablock = 'SMEFT',
                     lhacode = [ 153 ])

cHudRe12 = Parameter(name = 'cHudRe12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe12}',
                     lhablock = 'SMEFT',
                     lhacode = [ 154 ])

cHudRe13 = Parameter(name = 'cHudRe13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe13}',
                     lhablock = 'SMEFT',
                     lhacode = [ 155 ])

cHudRe23 = Parameter(name = 'cHudRe23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe23}',
                     lhablock = 'SMEFT',
                     lhacode = [ 156 ])

cHudRe21 = Parameter(name = 'cHudRe21',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe21}',
                     lhablock = 'SMEFT',
                     lhacode = [ 157 ])

cHudRe31 = Parameter(name = 'cHudRe31',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe31}',
                     lhablock = 'SMEFT',
                     lhacode = [ 158 ])

cHudRe32 = Parameter(name = 'cHudRe32',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudRe32}',
                     lhablock = 'SMEFT',
                     lhacode = [ 159 ])

cllRe1111 = Parameter(name = 'cllRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 160 ])

cllRe1122 = Parameter(name = 'cllRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 161 ])

cllRe1221 = Parameter(name = 'cllRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 162 ])

cllRe1133 = Parameter(name = 'cllRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 163 ])

cllRe1331 = Parameter(name = 'cllRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 164 ])

cllRe2222 = Parameter(name = 'cllRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 165 ])

cllRe2233 = Parameter(name = 'cllRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 166 ])

cllRe2332 = Parameter(name = 'cllRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 167 ])

cllRe3333 = Parameter(name = 'cllRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 168 ])

cllRe1112 = Parameter(name = 'cllRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 169 ])

cllRe1113 = Parameter(name = 'cllRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 170 ])

cllRe1123 = Parameter(name = 'cllRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 171 ])

cllRe1212 = Parameter(name = 'cllRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 172 ])

cllRe1213 = Parameter(name = 'cllRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 173 ])

cllRe1231 = Parameter(name = 'cllRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 174 ])

cllRe1222 = Parameter(name = 'cllRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 175 ])

cllRe1223 = Parameter(name = 'cllRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 176 ])

cllRe1232 = Parameter(name = 'cllRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 177 ])

cllRe1233 = Parameter(name = 'cllRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 178 ])

cllRe1313 = Parameter(name = 'cllRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 179 ])

cllRe1322 = Parameter(name = 'cllRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 180 ])

cllRe1332 = Parameter(name = 'cllRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 181 ])

cllRe1323 = Parameter(name = 'cllRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 182 ])

cllRe1333 = Parameter(name = 'cllRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 183 ])

cllRe2223 = Parameter(name = 'cllRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 184 ])

cllRe2323 = Parameter(name = 'cllRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 185 ])

cllRe3323 = Parameter(name = 'cllRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 186 ])

cqq1Re1111 = Parameter(name = 'cqq1Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 187 ])

cqq1Re1122 = Parameter(name = 'cqq1Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 188 ])

cqq1Re1221 = Parameter(name = 'cqq1Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 189 ])

cqq1Re1133 = Parameter(name = 'cqq1Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 190 ])

cqq1Re1331 = Parameter(name = 'cqq1Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 191 ])

cqq1Re2222 = Parameter(name = 'cqq1Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 192 ])

cqq1Re2233 = Parameter(name = 'cqq1Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 193 ])

cqq1Re2332 = Parameter(name = 'cqq1Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 194 ])

cqq1Re3333 = Parameter(name = 'cqq1Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 195 ])

cqq1Re1112 = Parameter(name = 'cqq1Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 196 ])

cqq1Re1113 = Parameter(name = 'cqq1Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 197 ])

cqq1Re1123 = Parameter(name = 'cqq1Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 198 ])

cqq1Re1212 = Parameter(name = 'cqq1Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 199 ])

cqq1Re1213 = Parameter(name = 'cqq1Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 200 ])

cqq1Re1231 = Parameter(name = 'cqq1Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 201 ])

cqq1Re1222 = Parameter(name = 'cqq1Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 202 ])

cqq1Re1223 = Parameter(name = 'cqq1Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 203 ])

cqq1Re1232 = Parameter(name = 'cqq1Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 204 ])

cqq1Re1233 = Parameter(name = 'cqq1Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 205 ])

cqq1Re1313 = Parameter(name = 'cqq1Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 206 ])

cqq1Re1322 = Parameter(name = 'cqq1Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 207 ])

cqq1Re1332 = Parameter(name = 'cqq1Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 208 ])

cqq1Re1323 = Parameter(name = 'cqq1Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 209 ])

cqq1Re1333 = Parameter(name = 'cqq1Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 210 ])

cqq1Re2223 = Parameter(name = 'cqq1Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 211 ])

cqq1Re2323 = Parameter(name = 'cqq1Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 212 ])

cqq1Re3323 = Parameter(name = 'cqq1Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 213 ])

cqq3Re1111 = Parameter(name = 'cqq3Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 214 ])

cqq3Re1122 = Parameter(name = 'cqq3Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 215 ])

cqq3Re1221 = Parameter(name = 'cqq3Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 216 ])

cqq3Re1133 = Parameter(name = 'cqq3Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 217 ])

cqq3Re1331 = Parameter(name = 'cqq3Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 218 ])

cqq3Re2222 = Parameter(name = 'cqq3Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 219 ])

cqq3Re2233 = Parameter(name = 'cqq3Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 220 ])

cqq3Re2332 = Parameter(name = 'cqq3Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 221 ])

cqq3Re3333 = Parameter(name = 'cqq3Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 222 ])

cqq3Re1112 = Parameter(name = 'cqq3Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 223 ])

cqq3Re1113 = Parameter(name = 'cqq3Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 224 ])

cqq3Re1123 = Parameter(name = 'cqq3Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 225 ])

cqq3Re1212 = Parameter(name = 'cqq3Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 226 ])

cqq3Re1213 = Parameter(name = 'cqq3Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 227 ])

cqq3Re1231 = Parameter(name = 'cqq3Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 228 ])

cqq3Re1222 = Parameter(name = 'cqq3Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 229 ])

cqq3Re1223 = Parameter(name = 'cqq3Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 230 ])

cqq3Re1232 = Parameter(name = 'cqq3Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 231 ])

cqq3Re1233 = Parameter(name = 'cqq3Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 232 ])

cqq3Re1313 = Parameter(name = 'cqq3Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 233 ])

cqq3Re1322 = Parameter(name = 'cqq3Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 234 ])

cqq3Re1332 = Parameter(name = 'cqq3Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 235 ])

cqq3Re1323 = Parameter(name = 'cqq3Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 236 ])

cqq3Re1333 = Parameter(name = 'cqq3Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 237 ])

cqq3Re2223 = Parameter(name = 'cqq3Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 238 ])

cqq3Re2323 = Parameter(name = 'cqq3Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 239 ])

cqq3Re3323 = Parameter(name = 'cqq3Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 240 ])

clq1Re1111 = Parameter(name = 'clq1Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 241 ])

clq1Re1112 = Parameter(name = 'clq1Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 242 ])

clq1Re1113 = Parameter(name = 'clq1Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 243 ])

clq1Re1123 = Parameter(name = 'clq1Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 244 ])

clq1Re1122 = Parameter(name = 'clq1Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 245 ])

clq1Re1133 = Parameter(name = 'clq1Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 246 ])

clq1Re1211 = Parameter(name = 'clq1Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 247 ])

clq1Re1212 = Parameter(name = 'clq1Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 248 ])

clq1Re1221 = Parameter(name = 'clq1Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 249 ])

clq1Re1213 = Parameter(name = 'clq1Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 250 ])

clq1Re1231 = Parameter(name = 'clq1Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 251 ])

clq1Re1222 = Parameter(name = 'clq1Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 252 ])

clq1Re1223 = Parameter(name = 'clq1Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 253 ])

clq1Re1232 = Parameter(name = 'clq1Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 254 ])

clq1Re1233 = Parameter(name = 'clq1Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 255 ])

clq1Re1311 = Parameter(name = 'clq1Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 256 ])

clq1Re1312 = Parameter(name = 'clq1Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 257 ])

clq1Re1313 = Parameter(name = 'clq1Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 258 ])

clq1Re1331 = Parameter(name = 'clq1Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 259 ])

clq1Re1321 = Parameter(name = 'clq1Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 260 ])

clq1Re1322 = Parameter(name = 'clq1Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 261 ])

clq1Re1332 = Parameter(name = 'clq1Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 262 ])

clq1Re1323 = Parameter(name = 'clq1Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 263 ])

clq1Re1333 = Parameter(name = 'clq1Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 264 ])

clq1Re2211 = Parameter(name = 'clq1Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 265 ])

clq1Re2212 = Parameter(name = 'clq1Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 266 ])

clq1Re2213 = Parameter(name = 'clq1Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 267 ])

clq1Re2222 = Parameter(name = 'clq1Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 268 ])

clq1Re2223 = Parameter(name = 'clq1Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 269 ])

clq1Re2233 = Parameter(name = 'clq1Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 270 ])

clq1Re2311 = Parameter(name = 'clq1Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 271 ])

clq1Re2312 = Parameter(name = 'clq1Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 272 ])

clq1Re2313 = Parameter(name = 'clq1Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 273 ])

clq1Re2321 = Parameter(name = 'clq1Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 274 ])

clq1Re2322 = Parameter(name = 'clq1Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 275 ])

clq1Re2323 = Parameter(name = 'clq1Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 276 ])

clq1Re2331 = Parameter(name = 'clq1Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 277 ])

clq1Re2332 = Parameter(name = 'clq1Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 278 ])

clq1Re2333 = Parameter(name = 'clq1Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 279 ])

clq1Re3311 = Parameter(name = 'clq1Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 280 ])

clq1Re3312 = Parameter(name = 'clq1Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 281 ])

clq1Re3313 = Parameter(name = 'clq1Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 282 ])

clq1Re3322 = Parameter(name = 'clq1Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 283 ])

clq1Re3333 = Parameter(name = 'clq1Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 284 ])

clq1Re3323 = Parameter(name = 'clq1Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 285 ])

clq3Re1111 = Parameter(name = 'clq3Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 286 ])

clq3Re1112 = Parameter(name = 'clq3Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 287 ])

clq3Re1113 = Parameter(name = 'clq3Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 288 ])

clq3Re1123 = Parameter(name = 'clq3Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 289 ])

clq3Re1122 = Parameter(name = 'clq3Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 290 ])

clq3Re1133 = Parameter(name = 'clq3Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 291 ])

clq3Re1211 = Parameter(name = 'clq3Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 292 ])

clq3Re1212 = Parameter(name = 'clq3Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 293 ])

clq3Re1221 = Parameter(name = 'clq3Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 294 ])

clq3Re1213 = Parameter(name = 'clq3Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 295 ])

clq3Re1231 = Parameter(name = 'clq3Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 296 ])

clq3Re1222 = Parameter(name = 'clq3Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 297 ])

clq3Re1223 = Parameter(name = 'clq3Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 298 ])

clq3Re1232 = Parameter(name = 'clq3Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 299 ])

clq3Re1233 = Parameter(name = 'clq3Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 300 ])

clq3Re1311 = Parameter(name = 'clq3Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 301 ])

clq3Re1312 = Parameter(name = 'clq3Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 302 ])

clq3Re1313 = Parameter(name = 'clq3Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 303 ])

clq3Re1331 = Parameter(name = 'clq3Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 304 ])

clq3Re1321 = Parameter(name = 'clq3Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 305 ])

clq3Re1322 = Parameter(name = 'clq3Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 306 ])

clq3Re1332 = Parameter(name = 'clq3Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 307 ])

clq3Re1323 = Parameter(name = 'clq3Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 308 ])

clq3Re1333 = Parameter(name = 'clq3Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 309 ])

clq3Re2211 = Parameter(name = 'clq3Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 310 ])

clq3Re2212 = Parameter(name = 'clq3Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 311 ])

clq3Re2213 = Parameter(name = 'clq3Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 312 ])

clq3Re2222 = Parameter(name = 'clq3Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 313 ])

clq3Re2223 = Parameter(name = 'clq3Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 314 ])

clq3Re2233 = Parameter(name = 'clq3Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 315 ])

clq3Re2311 = Parameter(name = 'clq3Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 316 ])

clq3Re2312 = Parameter(name = 'clq3Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 317 ])

clq3Re2313 = Parameter(name = 'clq3Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 318 ])

clq3Re2321 = Parameter(name = 'clq3Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 319 ])

clq3Re2322 = Parameter(name = 'clq3Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 320 ])

clq3Re2323 = Parameter(name = 'clq3Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 321 ])

clq3Re2331 = Parameter(name = 'clq3Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 322 ])

clq3Re2332 = Parameter(name = 'clq3Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 323 ])

clq3Re2333 = Parameter(name = 'clq3Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 324 ])

clq3Re3311 = Parameter(name = 'clq3Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 325 ])

clq3Re3312 = Parameter(name = 'clq3Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 326 ])

clq3Re3313 = Parameter(name = 'clq3Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 327 ])

clq3Re3322 = Parameter(name = 'clq3Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 328 ])

clq3Re3333 = Parameter(name = 'clq3Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 329 ])

clq3Re3323 = Parameter(name = 'clq3Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 330 ])

ceeRe1111 = Parameter(name = 'ceeRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 331 ])

ceeRe1122 = Parameter(name = 'ceeRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 332 ])

ceeRe1133 = Parameter(name = 'ceeRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 333 ])

ceeRe2222 = Parameter(name = 'ceeRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 334 ])

ceeRe2233 = Parameter(name = 'ceeRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 335 ])

ceeRe3333 = Parameter(name = 'ceeRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 336 ])

ceeRe1112 = Parameter(name = 'ceeRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 337 ])

ceeRe1123 = Parameter(name = 'ceeRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 338 ])

ceeRe1113 = Parameter(name = 'ceeRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 339 ])

ceeRe1213 = Parameter(name = 'ceeRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 340 ])

ceeRe1212 = Parameter(name = 'ceeRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 341 ])

ceeRe1232 = Parameter(name = 'ceeRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 342 ])

ceeRe1222 = Parameter(name = 'ceeRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 343 ])

ceeRe1313 = Parameter(name = 'ceeRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 344 ])

ceeRe1233 = Parameter(name = 'ceeRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 345 ])

ceeRe1323 = Parameter(name = 'ceeRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 346 ])

ceeRe1322 = Parameter(name = 'ceeRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 347 ])

ceeRe2223 = Parameter(name = 'ceeRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 348 ])

ceeRe1333 = Parameter(name = 'ceeRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 349 ])

ceeRe3323 = Parameter(name = 'ceeRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 350 ])

ceeRe2323 = Parameter(name = 'ceeRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 351 ])

cuuRe1111 = Parameter(name = 'cuuRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 352 ])

cuuRe1122 = Parameter(name = 'cuuRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 353 ])

cuuRe1221 = Parameter(name = 'cuuRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 354 ])

cuuRe1133 = Parameter(name = 'cuuRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 355 ])

cuuRe1331 = Parameter(name = 'cuuRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 356 ])

cuuRe2222 = Parameter(name = 'cuuRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 357 ])

cuuRe2233 = Parameter(name = 'cuuRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 358 ])

cuuRe2332 = Parameter(name = 'cuuRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 359 ])

cuuRe3333 = Parameter(name = 'cuuRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 360 ])

cuuRe1112 = Parameter(name = 'cuuRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 361 ])

cuuRe1113 = Parameter(name = 'cuuRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 362 ])

cuuRe1123 = Parameter(name = 'cuuRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 363 ])

cuuRe1212 = Parameter(name = 'cuuRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 364 ])

cuuRe1213 = Parameter(name = 'cuuRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 365 ])

cuuRe1231 = Parameter(name = 'cuuRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 366 ])

cuuRe1222 = Parameter(name = 'cuuRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 367 ])

cuuRe1223 = Parameter(name = 'cuuRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 368 ])

cuuRe1232 = Parameter(name = 'cuuRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 369 ])

cuuRe1233 = Parameter(name = 'cuuRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 370 ])

cuuRe1313 = Parameter(name = 'cuuRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 371 ])

cuuRe1322 = Parameter(name = 'cuuRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 372 ])

cuuRe1332 = Parameter(name = 'cuuRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 373 ])

cuuRe1323 = Parameter(name = 'cuuRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 374 ])

cuuRe1333 = Parameter(name = 'cuuRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 375 ])

cuuRe2223 = Parameter(name = 'cuuRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 376 ])

cuuRe2323 = Parameter(name = 'cuuRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 377 ])

cuuRe3323 = Parameter(name = 'cuuRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 378 ])

cddRe1111 = Parameter(name = 'cddRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 379 ])

cddRe1122 = Parameter(name = 'cddRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 380 ])

cddRe1221 = Parameter(name = 'cddRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 381 ])

cddRe1133 = Parameter(name = 'cddRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 382 ])

cddRe1331 = Parameter(name = 'cddRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 383 ])

cddRe2222 = Parameter(name = 'cddRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 384 ])

cddRe2233 = Parameter(name = 'cddRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 385 ])

cddRe2332 = Parameter(name = 'cddRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 386 ])

cddRe3333 = Parameter(name = 'cddRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 387 ])

cddRe1112 = Parameter(name = 'cddRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 388 ])

cddRe1113 = Parameter(name = 'cddRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 389 ])

cddRe1123 = Parameter(name = 'cddRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 390 ])

cddRe1212 = Parameter(name = 'cddRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 391 ])

cddRe1213 = Parameter(name = 'cddRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 392 ])

cddRe1231 = Parameter(name = 'cddRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 393 ])

cddRe1222 = Parameter(name = 'cddRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 394 ])

cddRe1223 = Parameter(name = 'cddRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 395 ])

cddRe1232 = Parameter(name = 'cddRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 396 ])

cddRe1233 = Parameter(name = 'cddRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 397 ])

cddRe1313 = Parameter(name = 'cddRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 398 ])

cddRe1322 = Parameter(name = 'cddRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 399 ])

cddRe1332 = Parameter(name = 'cddRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 400 ])

cddRe1323 = Parameter(name = 'cddRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 401 ])

cddRe1333 = Parameter(name = 'cddRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 402 ])

cddRe2223 = Parameter(name = 'cddRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 403 ])

cddRe2323 = Parameter(name = 'cddRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 404 ])

cddRe3323 = Parameter(name = 'cddRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 405 ])

ceuRe1111 = Parameter(name = 'ceuRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 406 ])

ceuRe1112 = Parameter(name = 'ceuRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 407 ])

ceuRe1113 = Parameter(name = 'ceuRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 408 ])

ceuRe1123 = Parameter(name = 'ceuRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 409 ])

ceuRe1122 = Parameter(name = 'ceuRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 410 ])

ceuRe1133 = Parameter(name = 'ceuRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 411 ])

ceuRe1211 = Parameter(name = 'ceuRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 412 ])

ceuRe1212 = Parameter(name = 'ceuRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 413 ])

ceuRe1221 = Parameter(name = 'ceuRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 414 ])

ceuRe1213 = Parameter(name = 'ceuRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 415 ])

ceuRe1231 = Parameter(name = 'ceuRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 416 ])

ceuRe1222 = Parameter(name = 'ceuRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 417 ])

ceuRe1223 = Parameter(name = 'ceuRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 418 ])

ceuRe1232 = Parameter(name = 'ceuRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 419 ])

ceuRe1233 = Parameter(name = 'ceuRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 420 ])

ceuRe1311 = Parameter(name = 'ceuRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 421 ])

ceuRe1312 = Parameter(name = 'ceuRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 422 ])

ceuRe1313 = Parameter(name = 'ceuRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 423 ])

ceuRe1331 = Parameter(name = 'ceuRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 424 ])

ceuRe1321 = Parameter(name = 'ceuRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 425 ])

ceuRe1322 = Parameter(name = 'ceuRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 426 ])

ceuRe1332 = Parameter(name = 'ceuRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 427 ])

ceuRe1323 = Parameter(name = 'ceuRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 428 ])

ceuRe1333 = Parameter(name = 'ceuRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 429 ])

ceuRe2211 = Parameter(name = 'ceuRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 430 ])

ceuRe2212 = Parameter(name = 'ceuRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 431 ])

ceuRe2213 = Parameter(name = 'ceuRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 432 ])

ceuRe2222 = Parameter(name = 'ceuRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 433 ])

ceuRe2223 = Parameter(name = 'ceuRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 434 ])

ceuRe2233 = Parameter(name = 'ceuRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 435 ])

ceuRe2311 = Parameter(name = 'ceuRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 436 ])

ceuRe2312 = Parameter(name = 'ceuRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 437 ])

ceuRe2313 = Parameter(name = 'ceuRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 438 ])

ceuRe2321 = Parameter(name = 'ceuRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 439 ])

ceuRe2322 = Parameter(name = 'ceuRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 440 ])

ceuRe2323 = Parameter(name = 'ceuRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 441 ])

ceuRe2331 = Parameter(name = 'ceuRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 442 ])

ceuRe2332 = Parameter(name = 'ceuRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 443 ])

ceuRe2333 = Parameter(name = 'ceuRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 444 ])

ceuRe3311 = Parameter(name = 'ceuRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 445 ])

ceuRe3312 = Parameter(name = 'ceuRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 446 ])

ceuRe3313 = Parameter(name = 'ceuRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 447 ])

ceuRe3322 = Parameter(name = 'ceuRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 448 ])

ceuRe3333 = Parameter(name = 'ceuRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 449 ])

ceuRe3323 = Parameter(name = 'ceuRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 450 ])

cedRe1111 = Parameter(name = 'cedRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 451 ])

cedRe1112 = Parameter(name = 'cedRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 452 ])

cedRe1113 = Parameter(name = 'cedRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 453 ])

cedRe1123 = Parameter(name = 'cedRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 454 ])

cedRe1122 = Parameter(name = 'cedRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 455 ])

cedRe1133 = Parameter(name = 'cedRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 456 ])

cedRe1211 = Parameter(name = 'cedRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 457 ])

cedRe1212 = Parameter(name = 'cedRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 458 ])

cedRe1221 = Parameter(name = 'cedRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 459 ])

cedRe1213 = Parameter(name = 'cedRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 460 ])

cedRe1231 = Parameter(name = 'cedRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 461 ])

cedRe1222 = Parameter(name = 'cedRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 462 ])

cedRe1223 = Parameter(name = 'cedRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 463 ])

cedRe1232 = Parameter(name = 'cedRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 464 ])

cedRe1233 = Parameter(name = 'cedRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 465 ])

cedRe1311 = Parameter(name = 'cedRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 466 ])

cedRe1312 = Parameter(name = 'cedRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 467 ])

cedRe1313 = Parameter(name = 'cedRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 468 ])

cedRe1331 = Parameter(name = 'cedRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 469 ])

cedRe1321 = Parameter(name = 'cedRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 470 ])

cedRe1322 = Parameter(name = 'cedRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 471 ])

cedRe1332 = Parameter(name = 'cedRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 472 ])

cedRe1323 = Parameter(name = 'cedRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 473 ])

cedRe1333 = Parameter(name = 'cedRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 474 ])

cedRe2211 = Parameter(name = 'cedRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 475 ])

cedRe2212 = Parameter(name = 'cedRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 476 ])

cedRe2213 = Parameter(name = 'cedRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 477 ])

cedRe2222 = Parameter(name = 'cedRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 478 ])

cedRe2223 = Parameter(name = 'cedRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 479 ])

cedRe2233 = Parameter(name = 'cedRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 480 ])

cedRe2311 = Parameter(name = 'cedRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 481 ])

cedRe2312 = Parameter(name = 'cedRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 482 ])

cedRe2313 = Parameter(name = 'cedRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 483 ])

cedRe2321 = Parameter(name = 'cedRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 484 ])

cedRe2322 = Parameter(name = 'cedRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 485 ])

cedRe2323 = Parameter(name = 'cedRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 486 ])

cedRe2331 = Parameter(name = 'cedRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 487 ])

cedRe2332 = Parameter(name = 'cedRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 488 ])

cedRe2333 = Parameter(name = 'cedRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 489 ])

cedRe3311 = Parameter(name = 'cedRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 490 ])

cedRe3312 = Parameter(name = 'cedRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 491 ])

cedRe3313 = Parameter(name = 'cedRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 492 ])

cedRe3322 = Parameter(name = 'cedRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 493 ])

cedRe3333 = Parameter(name = 'cedRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 494 ])

cedRe3323 = Parameter(name = 'cedRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 495 ])

cud1Re1111 = Parameter(name = 'cud1Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 496 ])

cud1Re1112 = Parameter(name = 'cud1Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 497 ])

cud1Re1113 = Parameter(name = 'cud1Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 498 ])

cud1Re1123 = Parameter(name = 'cud1Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 499 ])

cud1Re1122 = Parameter(name = 'cud1Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 500 ])

cud1Re1133 = Parameter(name = 'cud1Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 501 ])

cud1Re1211 = Parameter(name = 'cud1Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 502 ])

cud1Re1212 = Parameter(name = 'cud1Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 503 ])

cud1Re1221 = Parameter(name = 'cud1Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 504 ])

cud1Re1213 = Parameter(name = 'cud1Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 505 ])

cud1Re1231 = Parameter(name = 'cud1Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 506 ])

cud1Re1222 = Parameter(name = 'cud1Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 507 ])

cud1Re1223 = Parameter(name = 'cud1Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 508 ])

cud1Re1232 = Parameter(name = 'cud1Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 509 ])

cud1Re1233 = Parameter(name = 'cud1Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 510 ])

cud1Re1311 = Parameter(name = 'cud1Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 511 ])

cud1Re1312 = Parameter(name = 'cud1Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 512 ])

cud1Re1313 = Parameter(name = 'cud1Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 513 ])

cud1Re1331 = Parameter(name = 'cud1Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 514 ])

cud1Re1321 = Parameter(name = 'cud1Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 515 ])

cud1Re1322 = Parameter(name = 'cud1Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 516 ])

cud1Re1332 = Parameter(name = 'cud1Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 517 ])

cud1Re1323 = Parameter(name = 'cud1Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 518 ])

cud1Re1333 = Parameter(name = 'cud1Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 519 ])

cud1Re2211 = Parameter(name = 'cud1Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 520 ])

cud1Re2212 = Parameter(name = 'cud1Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 521 ])

cud1Re2213 = Parameter(name = 'cud1Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 522 ])

cud1Re2222 = Parameter(name = 'cud1Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 523 ])

cud1Re2223 = Parameter(name = 'cud1Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 524 ])

cud1Re2233 = Parameter(name = 'cud1Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 525 ])

cud1Re2311 = Parameter(name = 'cud1Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 526 ])

cud1Re2312 = Parameter(name = 'cud1Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 527 ])

cud1Re2313 = Parameter(name = 'cud1Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 528 ])

cud1Re2321 = Parameter(name = 'cud1Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 529 ])

cud1Re2322 = Parameter(name = 'cud1Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 530 ])

cud1Re2323 = Parameter(name = 'cud1Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 531 ])

cud1Re2331 = Parameter(name = 'cud1Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 532 ])

cud1Re2332 = Parameter(name = 'cud1Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 533 ])

cud1Re2333 = Parameter(name = 'cud1Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 534 ])

cud1Re3311 = Parameter(name = 'cud1Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 535 ])

cud1Re3312 = Parameter(name = 'cud1Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 536 ])

cud1Re3313 = Parameter(name = 'cud1Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 537 ])

cud1Re3322 = Parameter(name = 'cud1Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 538 ])

cud1Re3333 = Parameter(name = 'cud1Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 539 ])

cud1Re3323 = Parameter(name = 'cud1Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 540 ])

cud8Re1111 = Parameter(name = 'cud8Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 541 ])

cud8Re1112 = Parameter(name = 'cud8Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 542 ])

cud8Re1113 = Parameter(name = 'cud8Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 543 ])

cud8Re1123 = Parameter(name = 'cud8Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 544 ])

cud8Re1122 = Parameter(name = 'cud8Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 545 ])

cud8Re1133 = Parameter(name = 'cud8Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 546 ])

cud8Re1211 = Parameter(name = 'cud8Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 547 ])

cud8Re1212 = Parameter(name = 'cud8Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 548 ])

cud8Re1221 = Parameter(name = 'cud8Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 549 ])

cud8Re1213 = Parameter(name = 'cud8Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 550 ])

cud8Re1231 = Parameter(name = 'cud8Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 551 ])

cud8Re1222 = Parameter(name = 'cud8Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 552 ])

cud8Re1223 = Parameter(name = 'cud8Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 553 ])

cud8Re1232 = Parameter(name = 'cud8Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 554 ])

cud8Re1233 = Parameter(name = 'cud8Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 555 ])

cud8Re1311 = Parameter(name = 'cud8Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 556 ])

cud8Re1312 = Parameter(name = 'cud8Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 557 ])

cud8Re1313 = Parameter(name = 'cud8Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 558 ])

cud8Re1331 = Parameter(name = 'cud8Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 559 ])

cud8Re1321 = Parameter(name = 'cud8Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 560 ])

cud8Re1322 = Parameter(name = 'cud8Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 561 ])

cud8Re1332 = Parameter(name = 'cud8Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 562 ])

cud8Re1323 = Parameter(name = 'cud8Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 563 ])

cud8Re1333 = Parameter(name = 'cud8Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 564 ])

cud8Re2211 = Parameter(name = 'cud8Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 565 ])

cud8Re2212 = Parameter(name = 'cud8Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 566 ])

cud8Re2213 = Parameter(name = 'cud8Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 567 ])

cud8Re2222 = Parameter(name = 'cud8Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 568 ])

cud8Re2223 = Parameter(name = 'cud8Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 569 ])

cud8Re2233 = Parameter(name = 'cud8Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 570 ])

cud8Re2311 = Parameter(name = 'cud8Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 571 ])

cud8Re2312 = Parameter(name = 'cud8Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 572 ])

cud8Re2313 = Parameter(name = 'cud8Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 573 ])

cud8Re2321 = Parameter(name = 'cud8Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 574 ])

cud8Re2322 = Parameter(name = 'cud8Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 575 ])

cud8Re2323 = Parameter(name = 'cud8Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 576 ])

cud8Re2331 = Parameter(name = 'cud8Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 577 ])

cud8Re2332 = Parameter(name = 'cud8Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 578 ])

cud8Re2333 = Parameter(name = 'cud8Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 579 ])

cud8Re3311 = Parameter(name = 'cud8Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 580 ])

cud8Re3312 = Parameter(name = 'cud8Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 581 ])

cud8Re3313 = Parameter(name = 'cud8Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 582 ])

cud8Re3322 = Parameter(name = 'cud8Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 583 ])

cud8Re3333 = Parameter(name = 'cud8Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 584 ])

cud8Re3323 = Parameter(name = 'cud8Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 585 ])

cleRe1111 = Parameter(name = 'cleRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 586 ])

cleRe1112 = Parameter(name = 'cleRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 587 ])

cleRe1113 = Parameter(name = 'cleRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 588 ])

cleRe1123 = Parameter(name = 'cleRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 589 ])

cleRe1122 = Parameter(name = 'cleRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 590 ])

cleRe1133 = Parameter(name = 'cleRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 591 ])

cleRe1211 = Parameter(name = 'cleRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 592 ])

cleRe1212 = Parameter(name = 'cleRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 593 ])

cleRe1221 = Parameter(name = 'cleRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 594 ])

cleRe1213 = Parameter(name = 'cleRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 595 ])

cleRe1231 = Parameter(name = 'cleRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 596 ])

cleRe1222 = Parameter(name = 'cleRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 597 ])

cleRe1223 = Parameter(name = 'cleRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 598 ])

cleRe1232 = Parameter(name = 'cleRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 599 ])

cleRe1233 = Parameter(name = 'cleRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 600 ])

cleRe1311 = Parameter(name = 'cleRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 601 ])

cleRe1312 = Parameter(name = 'cleRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 602 ])

cleRe1313 = Parameter(name = 'cleRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 603 ])

cleRe1331 = Parameter(name = 'cleRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 604 ])

cleRe1321 = Parameter(name = 'cleRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 605 ])

cleRe1322 = Parameter(name = 'cleRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 606 ])

cleRe1332 = Parameter(name = 'cleRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 607 ])

cleRe1323 = Parameter(name = 'cleRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 608 ])

cleRe1333 = Parameter(name = 'cleRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 609 ])

cleRe2211 = Parameter(name = 'cleRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 610 ])

cleRe2212 = Parameter(name = 'cleRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 611 ])

cleRe2213 = Parameter(name = 'cleRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 612 ])

cleRe2222 = Parameter(name = 'cleRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 613 ])

cleRe2223 = Parameter(name = 'cleRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 614 ])

cleRe2233 = Parameter(name = 'cleRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 615 ])

cleRe2311 = Parameter(name = 'cleRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 616 ])

cleRe2312 = Parameter(name = 'cleRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 617 ])

cleRe2313 = Parameter(name = 'cleRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 618 ])

cleRe2321 = Parameter(name = 'cleRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 619 ])

cleRe2322 = Parameter(name = 'cleRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 620 ])

cleRe2323 = Parameter(name = 'cleRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 621 ])

cleRe2331 = Parameter(name = 'cleRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 622 ])

cleRe2332 = Parameter(name = 'cleRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 623 ])

cleRe2333 = Parameter(name = 'cleRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 624 ])

cleRe3311 = Parameter(name = 'cleRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 625 ])

cleRe3312 = Parameter(name = 'cleRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 626 ])

cleRe3313 = Parameter(name = 'cleRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 627 ])

cleRe3322 = Parameter(name = 'cleRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 628 ])

cleRe3333 = Parameter(name = 'cleRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 629 ])

cleRe3323 = Parameter(name = 'cleRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 630 ])

cluRe1111 = Parameter(name = 'cluRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 631 ])

cluRe1112 = Parameter(name = 'cluRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 632 ])

cluRe1113 = Parameter(name = 'cluRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 633 ])

cluRe1123 = Parameter(name = 'cluRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 634 ])

cluRe1122 = Parameter(name = 'cluRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 635 ])

cluRe1133 = Parameter(name = 'cluRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 636 ])

cluRe1211 = Parameter(name = 'cluRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 637 ])

cluRe1212 = Parameter(name = 'cluRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 638 ])

cluRe1221 = Parameter(name = 'cluRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 639 ])

cluRe1213 = Parameter(name = 'cluRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 640 ])

cluRe1231 = Parameter(name = 'cluRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 641 ])

cluRe1222 = Parameter(name = 'cluRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 642 ])

cluRe1223 = Parameter(name = 'cluRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 643 ])

cluRe1232 = Parameter(name = 'cluRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 644 ])

cluRe1233 = Parameter(name = 'cluRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 645 ])

cluRe1311 = Parameter(name = 'cluRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 646 ])

cluRe1312 = Parameter(name = 'cluRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 647 ])

cluRe1313 = Parameter(name = 'cluRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 648 ])

cluRe1331 = Parameter(name = 'cluRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 649 ])

cluRe1321 = Parameter(name = 'cluRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 650 ])

cluRe1322 = Parameter(name = 'cluRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 651 ])

cluRe1332 = Parameter(name = 'cluRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 652 ])

cluRe1323 = Parameter(name = 'cluRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 653 ])

cluRe1333 = Parameter(name = 'cluRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 654 ])

cluRe2211 = Parameter(name = 'cluRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 655 ])

cluRe2212 = Parameter(name = 'cluRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 656 ])

cluRe2213 = Parameter(name = 'cluRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 657 ])

cluRe2222 = Parameter(name = 'cluRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 658 ])

cluRe2223 = Parameter(name = 'cluRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 659 ])

cluRe2233 = Parameter(name = 'cluRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 660 ])

cluRe2311 = Parameter(name = 'cluRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 661 ])

cluRe2312 = Parameter(name = 'cluRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 662 ])

cluRe2313 = Parameter(name = 'cluRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 663 ])

cluRe2321 = Parameter(name = 'cluRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 664 ])

cluRe2322 = Parameter(name = 'cluRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 665 ])

cluRe2323 = Parameter(name = 'cluRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 666 ])

cluRe2331 = Parameter(name = 'cluRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 667 ])

cluRe2332 = Parameter(name = 'cluRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 668 ])

cluRe2333 = Parameter(name = 'cluRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 669 ])

cluRe3311 = Parameter(name = 'cluRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 670 ])

cluRe3312 = Parameter(name = 'cluRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 671 ])

cluRe3313 = Parameter(name = 'cluRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 672 ])

cluRe3322 = Parameter(name = 'cluRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 673 ])

cluRe3333 = Parameter(name = 'cluRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 674 ])

cluRe3323 = Parameter(name = 'cluRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 675 ])

cldRe1111 = Parameter(name = 'cldRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 676 ])

cldRe1112 = Parameter(name = 'cldRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 677 ])

cldRe1113 = Parameter(name = 'cldRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 678 ])

cldRe1123 = Parameter(name = 'cldRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 679 ])

cldRe1122 = Parameter(name = 'cldRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 680 ])

cldRe1133 = Parameter(name = 'cldRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 681 ])

cldRe1211 = Parameter(name = 'cldRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 682 ])

cldRe1212 = Parameter(name = 'cldRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 683 ])

cldRe1221 = Parameter(name = 'cldRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 684 ])

cldRe1213 = Parameter(name = 'cldRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 685 ])

cldRe1231 = Parameter(name = 'cldRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 686 ])

cldRe1222 = Parameter(name = 'cldRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 687 ])

cldRe1223 = Parameter(name = 'cldRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 688 ])

cldRe1232 = Parameter(name = 'cldRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 689 ])

cldRe1233 = Parameter(name = 'cldRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 690 ])

cldRe1311 = Parameter(name = 'cldRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 691 ])

cldRe1312 = Parameter(name = 'cldRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 692 ])

cldRe1313 = Parameter(name = 'cldRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 693 ])

cldRe1331 = Parameter(name = 'cldRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 694 ])

cldRe1321 = Parameter(name = 'cldRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 695 ])

cldRe1322 = Parameter(name = 'cldRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 696 ])

cldRe1332 = Parameter(name = 'cldRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 697 ])

cldRe1323 = Parameter(name = 'cldRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 698 ])

cldRe1333 = Parameter(name = 'cldRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 699 ])

cldRe2211 = Parameter(name = 'cldRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 700 ])

cldRe2212 = Parameter(name = 'cldRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 701 ])

cldRe2213 = Parameter(name = 'cldRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 702 ])

cldRe2222 = Parameter(name = 'cldRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 703 ])

cldRe2223 = Parameter(name = 'cldRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 704 ])

cldRe2233 = Parameter(name = 'cldRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 705 ])

cldRe2311 = Parameter(name = 'cldRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 706 ])

cldRe2312 = Parameter(name = 'cldRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 707 ])

cldRe2313 = Parameter(name = 'cldRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 708 ])

cldRe2321 = Parameter(name = 'cldRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 709 ])

cldRe2322 = Parameter(name = 'cldRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 710 ])

cldRe2323 = Parameter(name = 'cldRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 711 ])

cldRe2331 = Parameter(name = 'cldRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 712 ])

cldRe2332 = Parameter(name = 'cldRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 713 ])

cldRe2333 = Parameter(name = 'cldRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 714 ])

cldRe3311 = Parameter(name = 'cldRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 715 ])

cldRe3312 = Parameter(name = 'cldRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 716 ])

cldRe3313 = Parameter(name = 'cldRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 717 ])

cldRe3322 = Parameter(name = 'cldRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 718 ])

cldRe3333 = Parameter(name = 'cldRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 719 ])

cldRe3323 = Parameter(name = 'cldRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 720 ])

cqeRe1111 = Parameter(name = 'cqeRe1111',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1111}',
                      lhablock = 'SMEFT',
                      lhacode = [ 721 ])

cqeRe1112 = Parameter(name = 'cqeRe1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1112}',
                      lhablock = 'SMEFT',
                      lhacode = [ 722 ])

cqeRe1113 = Parameter(name = 'cqeRe1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1113}',
                      lhablock = 'SMEFT',
                      lhacode = [ 723 ])

cqeRe1123 = Parameter(name = 'cqeRe1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1123}',
                      lhablock = 'SMEFT',
                      lhacode = [ 724 ])

cqeRe1122 = Parameter(name = 'cqeRe1122',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1122}',
                      lhablock = 'SMEFT',
                      lhacode = [ 725 ])

cqeRe1133 = Parameter(name = 'cqeRe1133',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1133}',
                      lhablock = 'SMEFT',
                      lhacode = [ 726 ])

cqeRe1211 = Parameter(name = 'cqeRe1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 727 ])

cqeRe1212 = Parameter(name = 'cqeRe1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 728 ])

cqeRe1221 = Parameter(name = 'cqeRe1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1221}',
                      lhablock = 'SMEFT',
                      lhacode = [ 729 ])

cqeRe1213 = Parameter(name = 'cqeRe1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 730 ])

cqeRe1231 = Parameter(name = 'cqeRe1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1231}',
                      lhablock = 'SMEFT',
                      lhacode = [ 731 ])

cqeRe1222 = Parameter(name = 'cqeRe1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 732 ])

cqeRe1223 = Parameter(name = 'cqeRe1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 733 ])

cqeRe1232 = Parameter(name = 'cqeRe1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1232}',
                      lhablock = 'SMEFT',
                      lhacode = [ 734 ])

cqeRe1233 = Parameter(name = 'cqeRe1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 735 ])

cqeRe1311 = Parameter(name = 'cqeRe1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 736 ])

cqeRe1312 = Parameter(name = 'cqeRe1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 737 ])

cqeRe1313 = Parameter(name = 'cqeRe1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 738 ])

cqeRe1331 = Parameter(name = 'cqeRe1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 739 ])

cqeRe1321 = Parameter(name = 'cqeRe1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 740 ])

cqeRe1322 = Parameter(name = 'cqeRe1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 741 ])

cqeRe1332 = Parameter(name = 'cqeRe1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 742 ])

cqeRe1323 = Parameter(name = 'cqeRe1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 743 ])

cqeRe1333 = Parameter(name = 'cqeRe1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe1333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 744 ])

cqeRe2211 = Parameter(name = 'cqeRe2211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2211}',
                      lhablock = 'SMEFT',
                      lhacode = [ 745 ])

cqeRe2212 = Parameter(name = 'cqeRe2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2212}',
                      lhablock = 'SMEFT',
                      lhacode = [ 746 ])

cqeRe2213 = Parameter(name = 'cqeRe2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2213}',
                      lhablock = 'SMEFT',
                      lhacode = [ 747 ])

cqeRe2222 = Parameter(name = 'cqeRe2222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2222}',
                      lhablock = 'SMEFT',
                      lhacode = [ 748 ])

cqeRe2223 = Parameter(name = 'cqeRe2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2223}',
                      lhablock = 'SMEFT',
                      lhacode = [ 749 ])

cqeRe2233 = Parameter(name = 'cqeRe2233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2233}',
                      lhablock = 'SMEFT',
                      lhacode = [ 750 ])

cqeRe2311 = Parameter(name = 'cqeRe2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 751 ])

cqeRe2312 = Parameter(name = 'cqeRe2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 752 ])

cqeRe2313 = Parameter(name = 'cqeRe2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 753 ])

cqeRe2321 = Parameter(name = 'cqeRe2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2321}',
                      lhablock = 'SMEFT',
                      lhacode = [ 754 ])

cqeRe2322 = Parameter(name = 'cqeRe2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 755 ])

cqeRe2323 = Parameter(name = 'cqeRe2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 756 ])

cqeRe2331 = Parameter(name = 'cqeRe2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2331}',
                      lhablock = 'SMEFT',
                      lhacode = [ 757 ])

cqeRe2332 = Parameter(name = 'cqeRe2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2332}',
                      lhablock = 'SMEFT',
                      lhacode = [ 758 ])

cqeRe2333 = Parameter(name = 'cqeRe2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe2333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 759 ])

cqeRe3311 = Parameter(name = 'cqeRe3311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3311}',
                      lhablock = 'SMEFT',
                      lhacode = [ 760 ])

cqeRe3312 = Parameter(name = 'cqeRe3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3312}',
                      lhablock = 'SMEFT',
                      lhacode = [ 761 ])

cqeRe3313 = Parameter(name = 'cqeRe3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3313}',
                      lhablock = 'SMEFT',
                      lhacode = [ 762 ])

cqeRe3322 = Parameter(name = 'cqeRe3322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3322}',
                      lhablock = 'SMEFT',
                      lhacode = [ 763 ])

cqeRe3333 = Parameter(name = 'cqeRe3333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3333}',
                      lhablock = 'SMEFT',
                      lhacode = [ 764 ])

cqeRe3323 = Parameter(name = 'cqeRe3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeRe3323}',
                      lhablock = 'SMEFT',
                      lhacode = [ 765 ])

cqu1Re1111 = Parameter(name = 'cqu1Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 766 ])

cqu1Re1112 = Parameter(name = 'cqu1Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 767 ])

cqu1Re1113 = Parameter(name = 'cqu1Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 768 ])

cqu1Re1123 = Parameter(name = 'cqu1Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 769 ])

cqu1Re1122 = Parameter(name = 'cqu1Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 770 ])

cqu1Re1133 = Parameter(name = 'cqu1Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 771 ])

cqu1Re1211 = Parameter(name = 'cqu1Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 772 ])

cqu1Re1212 = Parameter(name = 'cqu1Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 773 ])

cqu1Re1221 = Parameter(name = 'cqu1Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 774 ])

cqu1Re1213 = Parameter(name = 'cqu1Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 775 ])

cqu1Re1231 = Parameter(name = 'cqu1Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 776 ])

cqu1Re1222 = Parameter(name = 'cqu1Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 777 ])

cqu1Re1223 = Parameter(name = 'cqu1Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 778 ])

cqu1Re1232 = Parameter(name = 'cqu1Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 779 ])

cqu1Re1233 = Parameter(name = 'cqu1Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 780 ])

cqu1Re1311 = Parameter(name = 'cqu1Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 781 ])

cqu1Re1312 = Parameter(name = 'cqu1Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 782 ])

cqu1Re1313 = Parameter(name = 'cqu1Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 783 ])

cqu1Re1331 = Parameter(name = 'cqu1Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 784 ])

cqu1Re1321 = Parameter(name = 'cqu1Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 785 ])

cqu1Re1322 = Parameter(name = 'cqu1Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 786 ])

cqu1Re1332 = Parameter(name = 'cqu1Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 787 ])

cqu1Re1323 = Parameter(name = 'cqu1Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 788 ])

cqu1Re1333 = Parameter(name = 'cqu1Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 789 ])

cqu1Re2211 = Parameter(name = 'cqu1Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 790 ])

cqu1Re2212 = Parameter(name = 'cqu1Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 791 ])

cqu1Re2213 = Parameter(name = 'cqu1Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 792 ])

cqu1Re2222 = Parameter(name = 'cqu1Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 793 ])

cqu1Re2223 = Parameter(name = 'cqu1Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 794 ])

cqu1Re2233 = Parameter(name = 'cqu1Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 795 ])

cqu1Re2311 = Parameter(name = 'cqu1Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 796 ])

cqu1Re2312 = Parameter(name = 'cqu1Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 797 ])

cqu1Re2313 = Parameter(name = 'cqu1Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 798 ])

cqu1Re2321 = Parameter(name = 'cqu1Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 799 ])

cqu1Re2322 = Parameter(name = 'cqu1Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 800 ])

cqu1Re2323 = Parameter(name = 'cqu1Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 801 ])

cqu1Re2331 = Parameter(name = 'cqu1Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 802 ])

cqu1Re2332 = Parameter(name = 'cqu1Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 803 ])

cqu1Re2333 = Parameter(name = 'cqu1Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 804 ])

cqu1Re3311 = Parameter(name = 'cqu1Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 805 ])

cqu1Re3312 = Parameter(name = 'cqu1Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 806 ])

cqu1Re3313 = Parameter(name = 'cqu1Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 807 ])

cqu1Re3322 = Parameter(name = 'cqu1Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 808 ])

cqu1Re3333 = Parameter(name = 'cqu1Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 809 ])

cqu1Re3323 = Parameter(name = 'cqu1Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 810 ])

cqu8Re1111 = Parameter(name = 'cqu8Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 811 ])

cqu8Re1112 = Parameter(name = 'cqu8Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 812 ])

cqu8Re1113 = Parameter(name = 'cqu8Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 813 ])

cqu8Re1123 = Parameter(name = 'cqu8Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 814 ])

cqu8Re1122 = Parameter(name = 'cqu8Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 815 ])

cqu8Re1133 = Parameter(name = 'cqu8Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 816 ])

cqu8Re1211 = Parameter(name = 'cqu8Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 817 ])

cqu8Re1212 = Parameter(name = 'cqu8Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 818 ])

cqu8Re1221 = Parameter(name = 'cqu8Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 819 ])

cqu8Re1213 = Parameter(name = 'cqu8Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 820 ])

cqu8Re1231 = Parameter(name = 'cqu8Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 821 ])

cqu8Re1222 = Parameter(name = 'cqu8Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 822 ])

cqu8Re1223 = Parameter(name = 'cqu8Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 823 ])

cqu8Re1232 = Parameter(name = 'cqu8Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 824 ])

cqu8Re1233 = Parameter(name = 'cqu8Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 825 ])

cqu8Re1311 = Parameter(name = 'cqu8Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 826 ])

cqu8Re1312 = Parameter(name = 'cqu8Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 827 ])

cqu8Re1313 = Parameter(name = 'cqu8Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 828 ])

cqu8Re1331 = Parameter(name = 'cqu8Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 829 ])

cqu8Re1321 = Parameter(name = 'cqu8Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 830 ])

cqu8Re1322 = Parameter(name = 'cqu8Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 831 ])

cqu8Re1332 = Parameter(name = 'cqu8Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 832 ])

cqu8Re1323 = Parameter(name = 'cqu8Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 833 ])

cqu8Re1333 = Parameter(name = 'cqu8Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 834 ])

cqu8Re2211 = Parameter(name = 'cqu8Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 835 ])

cqu8Re2212 = Parameter(name = 'cqu8Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 836 ])

cqu8Re2213 = Parameter(name = 'cqu8Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 837 ])

cqu8Re2222 = Parameter(name = 'cqu8Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 838 ])

cqu8Re2223 = Parameter(name = 'cqu8Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 839 ])

cqu8Re2233 = Parameter(name = 'cqu8Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 840 ])

cqu8Re2311 = Parameter(name = 'cqu8Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 841 ])

cqu8Re2312 = Parameter(name = 'cqu8Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 842 ])

cqu8Re2313 = Parameter(name = 'cqu8Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 843 ])

cqu8Re2321 = Parameter(name = 'cqu8Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 844 ])

cqu8Re2322 = Parameter(name = 'cqu8Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 845 ])

cqu8Re2323 = Parameter(name = 'cqu8Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 846 ])

cqu8Re2331 = Parameter(name = 'cqu8Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 847 ])

cqu8Re2332 = Parameter(name = 'cqu8Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 848 ])

cqu8Re2333 = Parameter(name = 'cqu8Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 849 ])

cqu8Re3311 = Parameter(name = 'cqu8Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 850 ])

cqu8Re3312 = Parameter(name = 'cqu8Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 851 ])

cqu8Re3313 = Parameter(name = 'cqu8Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 852 ])

cqu8Re3322 = Parameter(name = 'cqu8Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 853 ])

cqu8Re3333 = Parameter(name = 'cqu8Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 854 ])

cqu8Re3323 = Parameter(name = 'cqu8Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 855 ])

cqd1Re1111 = Parameter(name = 'cqd1Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 856 ])

cqd1Re1112 = Parameter(name = 'cqd1Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 857 ])

cqd1Re1113 = Parameter(name = 'cqd1Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 858 ])

cqd1Re1123 = Parameter(name = 'cqd1Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 859 ])

cqd1Re1122 = Parameter(name = 'cqd1Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 860 ])

cqd1Re1133 = Parameter(name = 'cqd1Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 861 ])

cqd1Re1211 = Parameter(name = 'cqd1Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 862 ])

cqd1Re1212 = Parameter(name = 'cqd1Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 863 ])

cqd1Re1221 = Parameter(name = 'cqd1Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 864 ])

cqd1Re1213 = Parameter(name = 'cqd1Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 865 ])

cqd1Re1231 = Parameter(name = 'cqd1Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 866 ])

cqd1Re1222 = Parameter(name = 'cqd1Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 867 ])

cqd1Re1223 = Parameter(name = 'cqd1Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 868 ])

cqd1Re1232 = Parameter(name = 'cqd1Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 869 ])

cqd1Re1233 = Parameter(name = 'cqd1Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 870 ])

cqd1Re1311 = Parameter(name = 'cqd1Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 871 ])

cqd1Re1312 = Parameter(name = 'cqd1Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 872 ])

cqd1Re1313 = Parameter(name = 'cqd1Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 873 ])

cqd1Re1331 = Parameter(name = 'cqd1Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 874 ])

cqd1Re1321 = Parameter(name = 'cqd1Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 875 ])

cqd1Re1322 = Parameter(name = 'cqd1Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 876 ])

cqd1Re1332 = Parameter(name = 'cqd1Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 877 ])

cqd1Re1323 = Parameter(name = 'cqd1Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 878 ])

cqd1Re1333 = Parameter(name = 'cqd1Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 879 ])

cqd1Re2211 = Parameter(name = 'cqd1Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 880 ])

cqd1Re2212 = Parameter(name = 'cqd1Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 881 ])

cqd1Re2213 = Parameter(name = 'cqd1Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 882 ])

cqd1Re2222 = Parameter(name = 'cqd1Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 883 ])

cqd1Re2223 = Parameter(name = 'cqd1Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 884 ])

cqd1Re2233 = Parameter(name = 'cqd1Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 885 ])

cqd1Re2311 = Parameter(name = 'cqd1Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 886 ])

cqd1Re2312 = Parameter(name = 'cqd1Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 887 ])

cqd1Re2313 = Parameter(name = 'cqd1Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 888 ])

cqd1Re2321 = Parameter(name = 'cqd1Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 889 ])

cqd1Re2322 = Parameter(name = 'cqd1Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 890 ])

cqd1Re2323 = Parameter(name = 'cqd1Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 891 ])

cqd1Re2331 = Parameter(name = 'cqd1Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 892 ])

cqd1Re2332 = Parameter(name = 'cqd1Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 893 ])

cqd1Re2333 = Parameter(name = 'cqd1Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 894 ])

cqd1Re3311 = Parameter(name = 'cqd1Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 895 ])

cqd1Re3312 = Parameter(name = 'cqd1Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 896 ])

cqd1Re3313 = Parameter(name = 'cqd1Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 897 ])

cqd1Re3322 = Parameter(name = 'cqd1Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 898 ])

cqd1Re3333 = Parameter(name = 'cqd1Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 899 ])

cqd1Re3323 = Parameter(name = 'cqd1Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 900 ])

cqd8Re1111 = Parameter(name = 'cqd8Re1111',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1111}',
                       lhablock = 'SMEFT',
                       lhacode = [ 901 ])

cqd8Re1112 = Parameter(name = 'cqd8Re1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1112}',
                       lhablock = 'SMEFT',
                       lhacode = [ 902 ])

cqd8Re1113 = Parameter(name = 'cqd8Re1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1113}',
                       lhablock = 'SMEFT',
                       lhacode = [ 903 ])

cqd8Re1123 = Parameter(name = 'cqd8Re1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1123}',
                       lhablock = 'SMEFT',
                       lhacode = [ 904 ])

cqd8Re1122 = Parameter(name = 'cqd8Re1122',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1122}',
                       lhablock = 'SMEFT',
                       lhacode = [ 905 ])

cqd8Re1133 = Parameter(name = 'cqd8Re1133',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1133}',
                       lhablock = 'SMEFT',
                       lhacode = [ 906 ])

cqd8Re1211 = Parameter(name = 'cqd8Re1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 907 ])

cqd8Re1212 = Parameter(name = 'cqd8Re1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 908 ])

cqd8Re1221 = Parameter(name = 'cqd8Re1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1221}',
                       lhablock = 'SMEFT',
                       lhacode = [ 909 ])

cqd8Re1213 = Parameter(name = 'cqd8Re1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 910 ])

cqd8Re1231 = Parameter(name = 'cqd8Re1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1231}',
                       lhablock = 'SMEFT',
                       lhacode = [ 911 ])

cqd8Re1222 = Parameter(name = 'cqd8Re1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 912 ])

cqd8Re1223 = Parameter(name = 'cqd8Re1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 913 ])

cqd8Re1232 = Parameter(name = 'cqd8Re1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1232}',
                       lhablock = 'SMEFT',
                       lhacode = [ 914 ])

cqd8Re1233 = Parameter(name = 'cqd8Re1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 915 ])

cqd8Re1311 = Parameter(name = 'cqd8Re1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 916 ])

cqd8Re1312 = Parameter(name = 'cqd8Re1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 917 ])

cqd8Re1313 = Parameter(name = 'cqd8Re1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 918 ])

cqd8Re1331 = Parameter(name = 'cqd8Re1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 919 ])

cqd8Re1321 = Parameter(name = 'cqd8Re1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 920 ])

cqd8Re1322 = Parameter(name = 'cqd8Re1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 921 ])

cqd8Re1332 = Parameter(name = 'cqd8Re1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 922 ])

cqd8Re1323 = Parameter(name = 'cqd8Re1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 923 ])

cqd8Re1333 = Parameter(name = 'cqd8Re1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re1333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 924 ])

cqd8Re2211 = Parameter(name = 'cqd8Re2211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2211}',
                       lhablock = 'SMEFT',
                       lhacode = [ 925 ])

cqd8Re2212 = Parameter(name = 'cqd8Re2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2212}',
                       lhablock = 'SMEFT',
                       lhacode = [ 926 ])

cqd8Re2213 = Parameter(name = 'cqd8Re2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2213}',
                       lhablock = 'SMEFT',
                       lhacode = [ 927 ])

cqd8Re2222 = Parameter(name = 'cqd8Re2222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2222}',
                       lhablock = 'SMEFT',
                       lhacode = [ 928 ])

cqd8Re2223 = Parameter(name = 'cqd8Re2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2223}',
                       lhablock = 'SMEFT',
                       lhacode = [ 929 ])

cqd8Re2233 = Parameter(name = 'cqd8Re2233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2233}',
                       lhablock = 'SMEFT',
                       lhacode = [ 930 ])

cqd8Re2311 = Parameter(name = 'cqd8Re2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 931 ])

cqd8Re2312 = Parameter(name = 'cqd8Re2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 932 ])

cqd8Re2313 = Parameter(name = 'cqd8Re2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 933 ])

cqd8Re2321 = Parameter(name = 'cqd8Re2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2321}',
                       lhablock = 'SMEFT',
                       lhacode = [ 934 ])

cqd8Re2322 = Parameter(name = 'cqd8Re2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 935 ])

cqd8Re2323 = Parameter(name = 'cqd8Re2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 936 ])

cqd8Re2331 = Parameter(name = 'cqd8Re2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2331}',
                       lhablock = 'SMEFT',
                       lhacode = [ 937 ])

cqd8Re2332 = Parameter(name = 'cqd8Re2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2332}',
                       lhablock = 'SMEFT',
                       lhacode = [ 938 ])

cqd8Re2333 = Parameter(name = 'cqd8Re2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re2333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 939 ])

cqd8Re3311 = Parameter(name = 'cqd8Re3311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3311}',
                       lhablock = 'SMEFT',
                       lhacode = [ 940 ])

cqd8Re3312 = Parameter(name = 'cqd8Re3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3312}',
                       lhablock = 'SMEFT',
                       lhacode = [ 941 ])

cqd8Re3313 = Parameter(name = 'cqd8Re3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3313}',
                       lhablock = 'SMEFT',
                       lhacode = [ 942 ])

cqd8Re3322 = Parameter(name = 'cqd8Re3322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3322}',
                       lhablock = 'SMEFT',
                       lhacode = [ 943 ])

cqd8Re3333 = Parameter(name = 'cqd8Re3333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3333}',
                       lhablock = 'SMEFT',
                       lhacode = [ 944 ])

cqd8Re3323 = Parameter(name = 'cqd8Re3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Re3323}',
                       lhablock = 'SMEFT',
                       lhacode = [ 945 ])

cledqRe1111 = Parameter(name = 'cledqRe1111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1111}',
                        lhablock = 'SMEFT',
                        lhacode = [ 946 ])

cledqRe1112 = Parameter(name = 'cledqRe1112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1112}',
                        lhablock = 'SMEFT',
                        lhacode = [ 947 ])

cledqRe1113 = Parameter(name = 'cledqRe1113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1113}',
                        lhablock = 'SMEFT',
                        lhacode = [ 948 ])

cledqRe1121 = Parameter(name = 'cledqRe1121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1121}',
                        lhablock = 'SMEFT',
                        lhacode = [ 949 ])

cledqRe1122 = Parameter(name = 'cledqRe1122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1122}',
                        lhablock = 'SMEFT',
                        lhacode = [ 950 ])

cledqRe1123 = Parameter(name = 'cledqRe1123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1123}',
                        lhablock = 'SMEFT',
                        lhacode = [ 951 ])

cledqRe1131 = Parameter(name = 'cledqRe1131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1131}',
                        lhablock = 'SMEFT',
                        lhacode = [ 952 ])

cledqRe1132 = Parameter(name = 'cledqRe1132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1132}',
                        lhablock = 'SMEFT',
                        lhacode = [ 953 ])

cledqRe1133 = Parameter(name = 'cledqRe1133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1133}',
                        lhablock = 'SMEFT',
                        lhacode = [ 954 ])

cledqRe2211 = Parameter(name = 'cledqRe2211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2211}',
                        lhablock = 'SMEFT',
                        lhacode = [ 955 ])

cledqRe2212 = Parameter(name = 'cledqRe2212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2212}',
                        lhablock = 'SMEFT',
                        lhacode = [ 956 ])

cledqRe2213 = Parameter(name = 'cledqRe2213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2213}',
                        lhablock = 'SMEFT',
                        lhacode = [ 957 ])

cledqRe2221 = Parameter(name = 'cledqRe2221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2221}',
                        lhablock = 'SMEFT',
                        lhacode = [ 958 ])

cledqRe2222 = Parameter(name = 'cledqRe2222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2222}',
                        lhablock = 'SMEFT',
                        lhacode = [ 959 ])

cledqRe2223 = Parameter(name = 'cledqRe2223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2223}',
                        lhablock = 'SMEFT',
                        lhacode = [ 960 ])

cledqRe2231 = Parameter(name = 'cledqRe2231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2231}',
                        lhablock = 'SMEFT',
                        lhacode = [ 961 ])

cledqRe2232 = Parameter(name = 'cledqRe2232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2232}',
                        lhablock = 'SMEFT',
                        lhacode = [ 962 ])

cledqRe2233 = Parameter(name = 'cledqRe2233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2233}',
                        lhablock = 'SMEFT',
                        lhacode = [ 963 ])

cledqRe3311 = Parameter(name = 'cledqRe3311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3311}',
                        lhablock = 'SMEFT',
                        lhacode = [ 964 ])

cledqRe3312 = Parameter(name = 'cledqRe3312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3312}',
                        lhablock = 'SMEFT',
                        lhacode = [ 965 ])

cledqRe3313 = Parameter(name = 'cledqRe3313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3313}',
                        lhablock = 'SMEFT',
                        lhacode = [ 966 ])

cledqRe3321 = Parameter(name = 'cledqRe3321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3321}',
                        lhablock = 'SMEFT',
                        lhacode = [ 967 ])

cledqRe3322 = Parameter(name = 'cledqRe3322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3322}',
                        lhablock = 'SMEFT',
                        lhacode = [ 968 ])

cledqRe3323 = Parameter(name = 'cledqRe3323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3323}',
                        lhablock = 'SMEFT',
                        lhacode = [ 969 ])

cledqRe3331 = Parameter(name = 'cledqRe3331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3331}',
                        lhablock = 'SMEFT',
                        lhacode = [ 970 ])

cledqRe3332 = Parameter(name = 'cledqRe3332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3332}',
                        lhablock = 'SMEFT',
                        lhacode = [ 971 ])

cledqRe3333 = Parameter(name = 'cledqRe3333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3333}',
                        lhablock = 'SMEFT',
                        lhacode = [ 972 ])

cledqRe1211 = Parameter(name = 'cledqRe1211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1211}',
                        lhablock = 'SMEFT',
                        lhacode = [ 973 ])

cledqRe1212 = Parameter(name = 'cledqRe1212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1212}',
                        lhablock = 'SMEFT',
                        lhacode = [ 974 ])

cledqRe1213 = Parameter(name = 'cledqRe1213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1213}',
                        lhablock = 'SMEFT',
                        lhacode = [ 975 ])

cledqRe1221 = Parameter(name = 'cledqRe1221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1221}',
                        lhablock = 'SMEFT',
                        lhacode = [ 976 ])

cledqRe1222 = Parameter(name = 'cledqRe1222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1222}',
                        lhablock = 'SMEFT',
                        lhacode = [ 977 ])

cledqRe1223 = Parameter(name = 'cledqRe1223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1223}',
                        lhablock = 'SMEFT',
                        lhacode = [ 978 ])

cledqRe1231 = Parameter(name = 'cledqRe1231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1231}',
                        lhablock = 'SMEFT',
                        lhacode = [ 979 ])

cledqRe1232 = Parameter(name = 'cledqRe1232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1232}',
                        lhablock = 'SMEFT',
                        lhacode = [ 980 ])

cledqRe1233 = Parameter(name = 'cledqRe1233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1233}',
                        lhablock = 'SMEFT',
                        lhacode = [ 981 ])

cledqRe1311 = Parameter(name = 'cledqRe1311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1311}',
                        lhablock = 'SMEFT',
                        lhacode = [ 982 ])

cledqRe1312 = Parameter(name = 'cledqRe1312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1312}',
                        lhablock = 'SMEFT',
                        lhacode = [ 983 ])

cledqRe1313 = Parameter(name = 'cledqRe1313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1313}',
                        lhablock = 'SMEFT',
                        lhacode = [ 984 ])

cledqRe1321 = Parameter(name = 'cledqRe1321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1321}',
                        lhablock = 'SMEFT',
                        lhacode = [ 985 ])

cledqRe1322 = Parameter(name = 'cledqRe1322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1322}',
                        lhablock = 'SMEFT',
                        lhacode = [ 986 ])

cledqRe1323 = Parameter(name = 'cledqRe1323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1323}',
                        lhablock = 'SMEFT',
                        lhacode = [ 987 ])

cledqRe1331 = Parameter(name = 'cledqRe1331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1331}',
                        lhablock = 'SMEFT',
                        lhacode = [ 988 ])

cledqRe1332 = Parameter(name = 'cledqRe1332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1332}',
                        lhablock = 'SMEFT',
                        lhacode = [ 989 ])

cledqRe1333 = Parameter(name = 'cledqRe1333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe1333}',
                        lhablock = 'SMEFT',
                        lhacode = [ 990 ])

cledqRe2311 = Parameter(name = 'cledqRe2311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2311}',
                        lhablock = 'SMEFT',
                        lhacode = [ 991 ])

cledqRe2312 = Parameter(name = 'cledqRe2312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2312}',
                        lhablock = 'SMEFT',
                        lhacode = [ 992 ])

cledqRe2313 = Parameter(name = 'cledqRe2313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2313}',
                        lhablock = 'SMEFT',
                        lhacode = [ 993 ])

cledqRe2321 = Parameter(name = 'cledqRe2321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2321}',
                        lhablock = 'SMEFT',
                        lhacode = [ 994 ])

cledqRe2322 = Parameter(name = 'cledqRe2322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2322}',
                        lhablock = 'SMEFT',
                        lhacode = [ 995 ])

cledqRe2323 = Parameter(name = 'cledqRe2323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2323}',
                        lhablock = 'SMEFT',
                        lhacode = [ 996 ])

cledqRe2331 = Parameter(name = 'cledqRe2331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2331}',
                        lhablock = 'SMEFT',
                        lhacode = [ 997 ])

cledqRe2332 = Parameter(name = 'cledqRe2332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2332}',
                        lhablock = 'SMEFT',
                        lhacode = [ 998 ])

cledqRe2333 = Parameter(name = 'cledqRe2333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2333}',
                        lhablock = 'SMEFT',
                        lhacode = [ 999 ])

cledqRe2111 = Parameter(name = 'cledqRe2111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2111}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1000 ])

cledqRe2112 = Parameter(name = 'cledqRe2112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2112}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1001 ])

cledqRe2113 = Parameter(name = 'cledqRe2113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2113}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1002 ])

cledqRe2121 = Parameter(name = 'cledqRe2121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2121}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1003 ])

cledqRe2122 = Parameter(name = 'cledqRe2122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2122}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1004 ])

cledqRe2123 = Parameter(name = 'cledqRe2123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2123}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1005 ])

cledqRe2131 = Parameter(name = 'cledqRe2131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2131}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1006 ])

cledqRe2132 = Parameter(name = 'cledqRe2132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2132}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1007 ])

cledqRe2133 = Parameter(name = 'cledqRe2133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe2133}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1008 ])

cledqRe3111 = Parameter(name = 'cledqRe3111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3111}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1009 ])

cledqRe3112 = Parameter(name = 'cledqRe3112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3112}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1010 ])

cledqRe3113 = Parameter(name = 'cledqRe3113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3113}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1011 ])

cledqRe3121 = Parameter(name = 'cledqRe3121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3121}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1012 ])

cledqRe3122 = Parameter(name = 'cledqRe3122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3122}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1013 ])

cledqRe3123 = Parameter(name = 'cledqRe3123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3123}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1014 ])

cledqRe3131 = Parameter(name = 'cledqRe3131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3131}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1015 ])

cledqRe3132 = Parameter(name = 'cledqRe3132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3132}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1016 ])

cledqRe3133 = Parameter(name = 'cledqRe3133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3133}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1017 ])

cledqRe3211 = Parameter(name = 'cledqRe3211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3211}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1018 ])

cledqRe3212 = Parameter(name = 'cledqRe3212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3212}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1019 ])

cledqRe3213 = Parameter(name = 'cledqRe3213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3213}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1020 ])

cledqRe3221 = Parameter(name = 'cledqRe3221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3221}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1021 ])

cledqRe3222 = Parameter(name = 'cledqRe3222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3222}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1022 ])

cledqRe3223 = Parameter(name = 'cledqRe3223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3223}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1023 ])

cledqRe3231 = Parameter(name = 'cledqRe3231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3231}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1024 ])

cledqRe3232 = Parameter(name = 'cledqRe3232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3232}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1025 ])

cledqRe3233 = Parameter(name = 'cledqRe3233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqRe3233}',
                        lhablock = 'SMEFT',
                        lhacode = [ 1026 ])

cquqd1Re1111 = Parameter(name = 'cquqd1Re1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1027 ])

cquqd1Re1112 = Parameter(name = 'cquqd1Re1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1028 ])

cquqd1Re1113 = Parameter(name = 'cquqd1Re1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1029 ])

cquqd1Re1121 = Parameter(name = 'cquqd1Re1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1030 ])

cquqd1Re1122 = Parameter(name = 'cquqd1Re1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1031 ])

cquqd1Re1123 = Parameter(name = 'cquqd1Re1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1032 ])

cquqd1Re1131 = Parameter(name = 'cquqd1Re1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1033 ])

cquqd1Re1132 = Parameter(name = 'cquqd1Re1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1034 ])

cquqd1Re1133 = Parameter(name = 'cquqd1Re1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1035 ])

cquqd1Re2211 = Parameter(name = 'cquqd1Re2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1036 ])

cquqd1Re2212 = Parameter(name = 'cquqd1Re2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1037 ])

cquqd1Re2213 = Parameter(name = 'cquqd1Re2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1038 ])

cquqd1Re2221 = Parameter(name = 'cquqd1Re2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1039 ])

cquqd1Re2222 = Parameter(name = 'cquqd1Re2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1040 ])

cquqd1Re2223 = Parameter(name = 'cquqd1Re2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1041 ])

cquqd1Re2231 = Parameter(name = 'cquqd1Re2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1042 ])

cquqd1Re2232 = Parameter(name = 'cquqd1Re2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1043 ])

cquqd1Re2233 = Parameter(name = 'cquqd1Re2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1044 ])

cquqd1Re3311 = Parameter(name = 'cquqd1Re3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1045 ])

cquqd1Re3312 = Parameter(name = 'cquqd1Re3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1046 ])

cquqd1Re3313 = Parameter(name = 'cquqd1Re3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1047 ])

cquqd1Re3321 = Parameter(name = 'cquqd1Re3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1048 ])

cquqd1Re3322 = Parameter(name = 'cquqd1Re3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1049 ])

cquqd1Re3323 = Parameter(name = 'cquqd1Re3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1050 ])

cquqd1Re3331 = Parameter(name = 'cquqd1Re3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1051 ])

cquqd1Re3332 = Parameter(name = 'cquqd1Re3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1052 ])

cquqd1Re3333 = Parameter(name = 'cquqd1Re3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1053 ])

cquqd1Re1211 = Parameter(name = 'cquqd1Re1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1054 ])

cquqd1Re1212 = Parameter(name = 'cquqd1Re1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1055 ])

cquqd1Re1213 = Parameter(name = 'cquqd1Re1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1056 ])

cquqd1Re1221 = Parameter(name = 'cquqd1Re1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1057 ])

cquqd1Re1222 = Parameter(name = 'cquqd1Re1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1058 ])

cquqd1Re1223 = Parameter(name = 'cquqd1Re1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1059 ])

cquqd1Re1231 = Parameter(name = 'cquqd1Re1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1060 ])

cquqd1Re1232 = Parameter(name = 'cquqd1Re1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1061 ])

cquqd1Re1233 = Parameter(name = 'cquqd1Re1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1062 ])

cquqd1Re1311 = Parameter(name = 'cquqd1Re1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1063 ])

cquqd1Re1312 = Parameter(name = 'cquqd1Re1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1064 ])

cquqd1Re1313 = Parameter(name = 'cquqd1Re1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1065 ])

cquqd1Re1321 = Parameter(name = 'cquqd1Re1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1066 ])

cquqd1Re1322 = Parameter(name = 'cquqd1Re1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1067 ])

cquqd1Re1323 = Parameter(name = 'cquqd1Re1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1068 ])

cquqd1Re1331 = Parameter(name = 'cquqd1Re1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1069 ])

cquqd1Re1332 = Parameter(name = 'cquqd1Re1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1070 ])

cquqd1Re1333 = Parameter(name = 'cquqd1Re1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re1333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1071 ])

cquqd1Re2311 = Parameter(name = 'cquqd1Re2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1072 ])

cquqd1Re2312 = Parameter(name = 'cquqd1Re2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1073 ])

cquqd1Re2313 = Parameter(name = 'cquqd1Re2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1074 ])

cquqd1Re2321 = Parameter(name = 'cquqd1Re2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1075 ])

cquqd1Re2322 = Parameter(name = 'cquqd1Re2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1076 ])

cquqd1Re2323 = Parameter(name = 'cquqd1Re2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1077 ])

cquqd1Re2331 = Parameter(name = 'cquqd1Re2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1078 ])

cquqd1Re2332 = Parameter(name = 'cquqd1Re2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1079 ])

cquqd1Re2333 = Parameter(name = 'cquqd1Re2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1080 ])

cquqd1Re2111 = Parameter(name = 'cquqd1Re2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1081 ])

cquqd1Re2112 = Parameter(name = 'cquqd1Re2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1082 ])

cquqd1Re2113 = Parameter(name = 'cquqd1Re2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1083 ])

cquqd1Re2121 = Parameter(name = 'cquqd1Re2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1084 ])

cquqd1Re2122 = Parameter(name = 'cquqd1Re2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1085 ])

cquqd1Re2123 = Parameter(name = 'cquqd1Re2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1086 ])

cquqd1Re2131 = Parameter(name = 'cquqd1Re2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1087 ])

cquqd1Re2132 = Parameter(name = 'cquqd1Re2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1088 ])

cquqd1Re2133 = Parameter(name = 'cquqd1Re2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re2133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1089 ])

cquqd1Re3111 = Parameter(name = 'cquqd1Re3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1090 ])

cquqd1Re3112 = Parameter(name = 'cquqd1Re3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1091 ])

cquqd1Re3113 = Parameter(name = 'cquqd1Re3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1092 ])

cquqd1Re3121 = Parameter(name = 'cquqd1Re3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1093 ])

cquqd1Re3122 = Parameter(name = 'cquqd1Re3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1094 ])

cquqd1Re3123 = Parameter(name = 'cquqd1Re3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1095 ])

cquqd1Re3131 = Parameter(name = 'cquqd1Re3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1096 ])

cquqd1Re3132 = Parameter(name = 'cquqd1Re3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1097 ])

cquqd1Re3133 = Parameter(name = 'cquqd1Re3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1098 ])

cquqd1Re3211 = Parameter(name = 'cquqd1Re3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1099 ])

cquqd1Re3212 = Parameter(name = 'cquqd1Re3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1100 ])

cquqd1Re3213 = Parameter(name = 'cquqd1Re3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1101 ])

cquqd1Re3221 = Parameter(name = 'cquqd1Re3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1102 ])

cquqd1Re3222 = Parameter(name = 'cquqd1Re3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1103 ])

cquqd1Re3223 = Parameter(name = 'cquqd1Re3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1104 ])

cquqd1Re3231 = Parameter(name = 'cquqd1Re3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1105 ])

cquqd1Re3232 = Parameter(name = 'cquqd1Re3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1106 ])

cquqd1Re3233 = Parameter(name = 'cquqd1Re3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Re3233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1107 ])

cquqd8Re1111 = Parameter(name = 'cquqd8Re1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1108 ])

cquqd8Re1112 = Parameter(name = 'cquqd8Re1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1109 ])

cquqd8Re1113 = Parameter(name = 'cquqd8Re1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1110 ])

cquqd8Re1121 = Parameter(name = 'cquqd8Re1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1111 ])

cquqd8Re1122 = Parameter(name = 'cquqd8Re1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1112 ])

cquqd8Re1123 = Parameter(name = 'cquqd8Re1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1113 ])

cquqd8Re1131 = Parameter(name = 'cquqd8Re1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1114 ])

cquqd8Re1132 = Parameter(name = 'cquqd8Re1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1115 ])

cquqd8Re1133 = Parameter(name = 'cquqd8Re1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1116 ])

cquqd8Re2211 = Parameter(name = 'cquqd8Re2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1117 ])

cquqd8Re2212 = Parameter(name = 'cquqd8Re2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1118 ])

cquqd8Re2213 = Parameter(name = 'cquqd8Re2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1119 ])

cquqd8Re2221 = Parameter(name = 'cquqd8Re2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1120 ])

cquqd8Re2222 = Parameter(name = 'cquqd8Re2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1121 ])

cquqd8Re2223 = Parameter(name = 'cquqd8Re2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1122 ])

cquqd8Re2231 = Parameter(name = 'cquqd8Re2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1123 ])

cquqd8Re2232 = Parameter(name = 'cquqd8Re2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1124 ])

cquqd8Re2233 = Parameter(name = 'cquqd8Re2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1125 ])

cquqd8Re3311 = Parameter(name = 'cquqd8Re3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1126 ])

cquqd8Re3312 = Parameter(name = 'cquqd8Re3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1127 ])

cquqd8Re3313 = Parameter(name = 'cquqd8Re3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1128 ])

cquqd8Re3321 = Parameter(name = 'cquqd8Re3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1129 ])

cquqd8Re3322 = Parameter(name = 'cquqd8Re3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1130 ])

cquqd8Re3323 = Parameter(name = 'cquqd8Re3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1131 ])

cquqd8Re3331 = Parameter(name = 'cquqd8Re3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1132 ])

cquqd8Re3332 = Parameter(name = 'cquqd8Re3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1133 ])

cquqd8Re3333 = Parameter(name = 'cquqd8Re3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1134 ])

cquqd8Re1211 = Parameter(name = 'cquqd8Re1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1135 ])

cquqd8Re1212 = Parameter(name = 'cquqd8Re1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1136 ])

cquqd8Re1213 = Parameter(name = 'cquqd8Re1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1137 ])

cquqd8Re1221 = Parameter(name = 'cquqd8Re1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1138 ])

cquqd8Re1222 = Parameter(name = 'cquqd8Re1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1139 ])

cquqd8Re1223 = Parameter(name = 'cquqd8Re1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1140 ])

cquqd8Re1231 = Parameter(name = 'cquqd8Re1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1141 ])

cquqd8Re1232 = Parameter(name = 'cquqd8Re1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1142 ])

cquqd8Re1233 = Parameter(name = 'cquqd8Re1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1143 ])

cquqd8Re1311 = Parameter(name = 'cquqd8Re1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1144 ])

cquqd8Re1312 = Parameter(name = 'cquqd8Re1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1145 ])

cquqd8Re1313 = Parameter(name = 'cquqd8Re1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1146 ])

cquqd8Re1321 = Parameter(name = 'cquqd8Re1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1147 ])

cquqd8Re1322 = Parameter(name = 'cquqd8Re1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1148 ])

cquqd8Re1323 = Parameter(name = 'cquqd8Re1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1149 ])

cquqd8Re1331 = Parameter(name = 'cquqd8Re1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1150 ])

cquqd8Re1332 = Parameter(name = 'cquqd8Re1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1151 ])

cquqd8Re1333 = Parameter(name = 'cquqd8Re1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re1333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1152 ])

cquqd8Re2311 = Parameter(name = 'cquqd8Re2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1153 ])

cquqd8Re2312 = Parameter(name = 'cquqd8Re2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1154 ])

cquqd8Re2313 = Parameter(name = 'cquqd8Re2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1155 ])

cquqd8Re2321 = Parameter(name = 'cquqd8Re2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1156 ])

cquqd8Re2322 = Parameter(name = 'cquqd8Re2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1157 ])

cquqd8Re2323 = Parameter(name = 'cquqd8Re2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1158 ])

cquqd8Re2331 = Parameter(name = 'cquqd8Re2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1159 ])

cquqd8Re2332 = Parameter(name = 'cquqd8Re2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1160 ])

cquqd8Re2333 = Parameter(name = 'cquqd8Re2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1161 ])

cquqd8Re2111 = Parameter(name = 'cquqd8Re2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1162 ])

cquqd8Re2112 = Parameter(name = 'cquqd8Re2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1163 ])

cquqd8Re2113 = Parameter(name = 'cquqd8Re2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1164 ])

cquqd8Re2121 = Parameter(name = 'cquqd8Re2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1165 ])

cquqd8Re2122 = Parameter(name = 'cquqd8Re2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1166 ])

cquqd8Re2123 = Parameter(name = 'cquqd8Re2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1167 ])

cquqd8Re2131 = Parameter(name = 'cquqd8Re2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1168 ])

cquqd8Re2132 = Parameter(name = 'cquqd8Re2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1169 ])

cquqd8Re2133 = Parameter(name = 'cquqd8Re2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re2133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1170 ])

cquqd8Re3111 = Parameter(name = 'cquqd8Re3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1171 ])

cquqd8Re3112 = Parameter(name = 'cquqd8Re3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1172 ])

cquqd8Re3113 = Parameter(name = 'cquqd8Re3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1173 ])

cquqd8Re3121 = Parameter(name = 'cquqd8Re3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1174 ])

cquqd8Re3122 = Parameter(name = 'cquqd8Re3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1175 ])

cquqd8Re3123 = Parameter(name = 'cquqd8Re3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1176 ])

cquqd8Re3131 = Parameter(name = 'cquqd8Re3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1177 ])

cquqd8Re3132 = Parameter(name = 'cquqd8Re3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1178 ])

cquqd8Re3133 = Parameter(name = 'cquqd8Re3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1179 ])

cquqd8Re3211 = Parameter(name = 'cquqd8Re3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1180 ])

cquqd8Re3212 = Parameter(name = 'cquqd8Re3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1181 ])

cquqd8Re3213 = Parameter(name = 'cquqd8Re3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1182 ])

cquqd8Re3221 = Parameter(name = 'cquqd8Re3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1183 ])

cquqd8Re3222 = Parameter(name = 'cquqd8Re3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1184 ])

cquqd8Re3223 = Parameter(name = 'cquqd8Re3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1185 ])

cquqd8Re3231 = Parameter(name = 'cquqd8Re3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1186 ])

cquqd8Re3232 = Parameter(name = 'cquqd8Re3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1187 ])

cquqd8Re3233 = Parameter(name = 'cquqd8Re3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Re3233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1188 ])

clequ1Re1111 = Parameter(name = 'clequ1Re1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1189 ])

clequ1Re1112 = Parameter(name = 'clequ1Re1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1190 ])

clequ1Re1113 = Parameter(name = 'clequ1Re1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1191 ])

clequ1Re1121 = Parameter(name = 'clequ1Re1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1192 ])

clequ1Re1122 = Parameter(name = 'clequ1Re1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1193 ])

clequ1Re1123 = Parameter(name = 'clequ1Re1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1194 ])

clequ1Re1131 = Parameter(name = 'clequ1Re1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1195 ])

clequ1Re1132 = Parameter(name = 'clequ1Re1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1196 ])

clequ1Re1133 = Parameter(name = 'clequ1Re1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1197 ])

clequ1Re2211 = Parameter(name = 'clequ1Re2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1198 ])

clequ1Re2212 = Parameter(name = 'clequ1Re2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1199 ])

clequ1Re2213 = Parameter(name = 'clequ1Re2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1200 ])

clequ1Re2221 = Parameter(name = 'clequ1Re2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1201 ])

clequ1Re2222 = Parameter(name = 'clequ1Re2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1202 ])

clequ1Re2223 = Parameter(name = 'clequ1Re2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1203 ])

clequ1Re2231 = Parameter(name = 'clequ1Re2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1204 ])

clequ1Re2232 = Parameter(name = 'clequ1Re2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1205 ])

clequ1Re2233 = Parameter(name = 'clequ1Re2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1206 ])

clequ1Re3311 = Parameter(name = 'clequ1Re3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1207 ])

clequ1Re3312 = Parameter(name = 'clequ1Re3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1208 ])

clequ1Re3313 = Parameter(name = 'clequ1Re3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1209 ])

clequ1Re3321 = Parameter(name = 'clequ1Re3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1210 ])

clequ1Re3322 = Parameter(name = 'clequ1Re3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1211 ])

clequ1Re3323 = Parameter(name = 'clequ1Re3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1212 ])

clequ1Re3331 = Parameter(name = 'clequ1Re3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1213 ])

clequ1Re3332 = Parameter(name = 'clequ1Re3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1214 ])

clequ1Re3333 = Parameter(name = 'clequ1Re3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1215 ])

clequ1Re1211 = Parameter(name = 'clequ1Re1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1216 ])

clequ1Re1212 = Parameter(name = 'clequ1Re1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1217 ])

clequ1Re1213 = Parameter(name = 'clequ1Re1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1218 ])

clequ1Re1221 = Parameter(name = 'clequ1Re1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1219 ])

clequ1Re1222 = Parameter(name = 'clequ1Re1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1220 ])

clequ1Re1223 = Parameter(name = 'clequ1Re1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1221 ])

clequ1Re1231 = Parameter(name = 'clequ1Re1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1222 ])

clequ1Re1232 = Parameter(name = 'clequ1Re1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1223 ])

clequ1Re1233 = Parameter(name = 'clequ1Re1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1224 ])

clequ1Re1311 = Parameter(name = 'clequ1Re1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1225 ])

clequ1Re1312 = Parameter(name = 'clequ1Re1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1226 ])

clequ1Re1313 = Parameter(name = 'clequ1Re1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1227 ])

clequ1Re1321 = Parameter(name = 'clequ1Re1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1228 ])

clequ1Re1322 = Parameter(name = 'clequ1Re1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1229 ])

clequ1Re1323 = Parameter(name = 'clequ1Re1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1230 ])

clequ1Re1331 = Parameter(name = 'clequ1Re1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1231 ])

clequ1Re1332 = Parameter(name = 'clequ1Re1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1232 ])

clequ1Re1333 = Parameter(name = 'clequ1Re1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re1333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1233 ])

clequ1Re2311 = Parameter(name = 'clequ1Re2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1234 ])

clequ1Re2312 = Parameter(name = 'clequ1Re2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1235 ])

clequ1Re2313 = Parameter(name = 'clequ1Re2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1236 ])

clequ1Re2321 = Parameter(name = 'clequ1Re2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1237 ])

clequ1Re2322 = Parameter(name = 'clequ1Re2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1238 ])

clequ1Re2323 = Parameter(name = 'clequ1Re2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1239 ])

clequ1Re2331 = Parameter(name = 'clequ1Re2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1240 ])

clequ1Re2332 = Parameter(name = 'clequ1Re2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1241 ])

clequ1Re2333 = Parameter(name = 'clequ1Re2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1242 ])

clequ1Re2111 = Parameter(name = 'clequ1Re2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1243 ])

clequ1Re2112 = Parameter(name = 'clequ1Re2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1244 ])

clequ1Re2113 = Parameter(name = 'clequ1Re2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1245 ])

clequ1Re2121 = Parameter(name = 'clequ1Re2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1246 ])

clequ1Re2122 = Parameter(name = 'clequ1Re2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1247 ])

clequ1Re2123 = Parameter(name = 'clequ1Re2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1248 ])

clequ1Re2131 = Parameter(name = 'clequ1Re2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1249 ])

clequ1Re2132 = Parameter(name = 'clequ1Re2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1250 ])

clequ1Re2133 = Parameter(name = 'clequ1Re2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re2133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1251 ])

clequ1Re3111 = Parameter(name = 'clequ1Re3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1252 ])

clequ1Re3112 = Parameter(name = 'clequ1Re3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1253 ])

clequ1Re3113 = Parameter(name = 'clequ1Re3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1254 ])

clequ1Re3121 = Parameter(name = 'clequ1Re3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1255 ])

clequ1Re3122 = Parameter(name = 'clequ1Re3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1256 ])

clequ1Re3123 = Parameter(name = 'clequ1Re3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1257 ])

clequ1Re3131 = Parameter(name = 'clequ1Re3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1258 ])

clequ1Re3132 = Parameter(name = 'clequ1Re3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1259 ])

clequ1Re3133 = Parameter(name = 'clequ1Re3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1260 ])

clequ1Re3211 = Parameter(name = 'clequ1Re3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1261 ])

clequ1Re3212 = Parameter(name = 'clequ1Re3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1262 ])

clequ1Re3213 = Parameter(name = 'clequ1Re3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1263 ])

clequ1Re3221 = Parameter(name = 'clequ1Re3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1264 ])

clequ1Re3222 = Parameter(name = 'clequ1Re3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1265 ])

clequ1Re3223 = Parameter(name = 'clequ1Re3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1266 ])

clequ1Re3231 = Parameter(name = 'clequ1Re3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1267 ])

clequ1Re3232 = Parameter(name = 'clequ1Re3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1268 ])

clequ1Re3233 = Parameter(name = 'clequ1Re3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Re3233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1269 ])

clequ3Re1111 = Parameter(name = 'clequ3Re1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1270 ])

clequ3Re1112 = Parameter(name = 'clequ3Re1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1271 ])

clequ3Re1113 = Parameter(name = 'clequ3Re1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1272 ])

clequ3Re1121 = Parameter(name = 'clequ3Re1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1273 ])

clequ3Re1122 = Parameter(name = 'clequ3Re1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1274 ])

clequ3Re1123 = Parameter(name = 'clequ3Re1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1275 ])

clequ3Re1131 = Parameter(name = 'clequ3Re1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1276 ])

clequ3Re1132 = Parameter(name = 'clequ3Re1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1277 ])

clequ3Re1133 = Parameter(name = 'clequ3Re1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1278 ])

clequ3Re2211 = Parameter(name = 'clequ3Re2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1279 ])

clequ3Re2212 = Parameter(name = 'clequ3Re2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1280 ])

clequ3Re2213 = Parameter(name = 'clequ3Re2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1281 ])

clequ3Re2221 = Parameter(name = 'clequ3Re2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1282 ])

clequ3Re2222 = Parameter(name = 'clequ3Re2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1283 ])

clequ3Re2223 = Parameter(name = 'clequ3Re2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1284 ])

clequ3Re2231 = Parameter(name = 'clequ3Re2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1285 ])

clequ3Re2232 = Parameter(name = 'clequ3Re2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1286 ])

clequ3Re2233 = Parameter(name = 'clequ3Re2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1287 ])

clequ3Re3311 = Parameter(name = 'clequ3Re3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1288 ])

clequ3Re3312 = Parameter(name = 'clequ3Re3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1289 ])

clequ3Re3313 = Parameter(name = 'clequ3Re3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1290 ])

clequ3Re3321 = Parameter(name = 'clequ3Re3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1291 ])

clequ3Re3322 = Parameter(name = 'clequ3Re3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1292 ])

clequ3Re3323 = Parameter(name = 'clequ3Re3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1293 ])

clequ3Re3331 = Parameter(name = 'clequ3Re3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1294 ])

clequ3Re3332 = Parameter(name = 'clequ3Re3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1295 ])

clequ3Re3333 = Parameter(name = 'clequ3Re3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1296 ])

clequ3Re1211 = Parameter(name = 'clequ3Re1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1297 ])

clequ3Re1212 = Parameter(name = 'clequ3Re1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1298 ])

clequ3Re1213 = Parameter(name = 'clequ3Re1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1299 ])

clequ3Re1221 = Parameter(name = 'clequ3Re1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1300 ])

clequ3Re1222 = Parameter(name = 'clequ3Re1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1301 ])

clequ3Re1223 = Parameter(name = 'clequ3Re1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1302 ])

clequ3Re1231 = Parameter(name = 'clequ3Re1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1303 ])

clequ3Re1232 = Parameter(name = 'clequ3Re1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1304 ])

clequ3Re1233 = Parameter(name = 'clequ3Re1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1305 ])

clequ3Re1311 = Parameter(name = 'clequ3Re1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1306 ])

clequ3Re1312 = Parameter(name = 'clequ3Re1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1307 ])

clequ3Re1313 = Parameter(name = 'clequ3Re1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1308 ])

clequ3Re1321 = Parameter(name = 'clequ3Re1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1309 ])

clequ3Re1322 = Parameter(name = 'clequ3Re1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1310 ])

clequ3Re1323 = Parameter(name = 'clequ3Re1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1311 ])

clequ3Re1331 = Parameter(name = 'clequ3Re1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1312 ])

clequ3Re1332 = Parameter(name = 'clequ3Re1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1313 ])

clequ3Re1333 = Parameter(name = 'clequ3Re1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re1333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1314 ])

clequ3Re2311 = Parameter(name = 'clequ3Re2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2311}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1315 ])

clequ3Re2312 = Parameter(name = 'clequ3Re2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2312}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1316 ])

clequ3Re2313 = Parameter(name = 'clequ3Re2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2313}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1317 ])

clequ3Re2321 = Parameter(name = 'clequ3Re2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2321}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1318 ])

clequ3Re2322 = Parameter(name = 'clequ3Re2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2322}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1319 ])

clequ3Re2323 = Parameter(name = 'clequ3Re2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2323}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1320 ])

clequ3Re2331 = Parameter(name = 'clequ3Re2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2331}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1321 ])

clequ3Re2332 = Parameter(name = 'clequ3Re2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2332}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1322 ])

clequ3Re2333 = Parameter(name = 'clequ3Re2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2333}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1323 ])

clequ3Re2111 = Parameter(name = 'clequ3Re2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1324 ])

clequ3Re2112 = Parameter(name = 'clequ3Re2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1325 ])

clequ3Re2113 = Parameter(name = 'clequ3Re2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1326 ])

clequ3Re2121 = Parameter(name = 'clequ3Re2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1327 ])

clequ3Re2122 = Parameter(name = 'clequ3Re2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1328 ])

clequ3Re2123 = Parameter(name = 'clequ3Re2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1329 ])

clequ3Re2131 = Parameter(name = 'clequ3Re2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1330 ])

clequ3Re2132 = Parameter(name = 'clequ3Re2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1331 ])

clequ3Re2133 = Parameter(name = 'clequ3Re2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re2133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1332 ])

clequ3Re3111 = Parameter(name = 'clequ3Re3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3111}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1333 ])

clequ3Re3112 = Parameter(name = 'clequ3Re3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3112}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1334 ])

clequ3Re3113 = Parameter(name = 'clequ3Re3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3113}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1335 ])

clequ3Re3121 = Parameter(name = 'clequ3Re3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3121}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1336 ])

clequ3Re3122 = Parameter(name = 'clequ3Re3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3122}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1337 ])

clequ3Re3123 = Parameter(name = 'clequ3Re3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3123}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1338 ])

clequ3Re3131 = Parameter(name = 'clequ3Re3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3131}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1339 ])

clequ3Re3132 = Parameter(name = 'clequ3Re3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3132}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1340 ])

clequ3Re3133 = Parameter(name = 'clequ3Re3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3133}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1341 ])

clequ3Re3211 = Parameter(name = 'clequ3Re3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3211}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1342 ])

clequ3Re3212 = Parameter(name = 'clequ3Re3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3212}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1343 ])

clequ3Re3213 = Parameter(name = 'clequ3Re3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3213}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1344 ])

clequ3Re3221 = Parameter(name = 'clequ3Re3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3221}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1345 ])

clequ3Re3222 = Parameter(name = 'clequ3Re3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3222}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1346 ])

clequ3Re3223 = Parameter(name = 'clequ3Re3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3223}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1347 ])

clequ3Re3231 = Parameter(name = 'clequ3Re3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3231}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1348 ])

clequ3Re3232 = Parameter(name = 'clequ3Re3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3232}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1349 ])

clequ3Re3233 = Parameter(name = 'clequ3Re3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Re3233}',
                         lhablock = 'SMEFT',
                         lhacode = [ 1350 ])

cGtil = Parameter(name = 'cGtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{G}}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 1 ])

cWtil = Parameter(name = 'cWtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{W}}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 2 ])

cHGtil = Parameter(name = 'cHGtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{G}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 3 ])

cHWtil = Parameter(name = 'cHWtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{W}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 4 ])

cHBtil = Parameter(name = 'cHBtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{B}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 5 ])

cHWBtil = Parameter(name = 'cHWBtil',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{B H \\tilde{W}}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 6 ])

ceHIm22 = Parameter(name = 'ceHIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 7 ])

ceHIm11 = Parameter(name = 'ceHIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 8 ])

ceHIm33 = Parameter(name = 'ceHIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 9 ])

ceHIm12 = Parameter(name = 'ceHIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 10 ])

ceHIm13 = Parameter(name = 'ceHIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 11 ])

ceHIm23 = Parameter(name = 'ceHIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 12 ])

ceHIm21 = Parameter(name = 'ceHIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 13 ])

ceHIm31 = Parameter(name = 'ceHIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 14 ])

ceHIm32 = Parameter(name = 'ceHIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 15 ])

cuHIm11 = Parameter(name = 'cuHIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 16 ])

cuHIm22 = Parameter(name = 'cuHIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 17 ])

cuHIm33 = Parameter(name = 'cuHIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 18 ])

cuHIm12 = Parameter(name = 'cuHIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 19 ])

cuHIm13 = Parameter(name = 'cuHIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 20 ])

cuHIm23 = Parameter(name = 'cuHIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 21 ])

cuHIm21 = Parameter(name = 'cuHIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 22 ])

cuHIm31 = Parameter(name = 'cuHIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 23 ])

cuHIm32 = Parameter(name = 'cuHIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuHIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 24 ])

cdHIm11 = Parameter(name = 'cdHIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 25 ])

cdHIm22 = Parameter(name = 'cdHIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 26 ])

cdHIm33 = Parameter(name = 'cdHIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 27 ])

cdHIm12 = Parameter(name = 'cdHIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 28 ])

cdHIm13 = Parameter(name = 'cdHIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 29 ])

cdHIm23 = Parameter(name = 'cdHIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 30 ])

cdHIm21 = Parameter(name = 'cdHIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 31 ])

cdHIm31 = Parameter(name = 'cdHIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 32 ])

cdHIm32 = Parameter(name = 'cdHIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdHIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 33 ])

ceWIm11 = Parameter(name = 'ceWIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 34 ])

ceWIm22 = Parameter(name = 'ceWIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 35 ])

ceWIm33 = Parameter(name = 'ceWIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 36 ])

ceWIm12 = Parameter(name = 'ceWIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 37 ])

ceWIm13 = Parameter(name = 'ceWIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 38 ])

ceWIm23 = Parameter(name = 'ceWIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 39 ])

ceWIm21 = Parameter(name = 'ceWIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 40 ])

ceWIm31 = Parameter(name = 'ceWIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 41 ])

ceWIm32 = Parameter(name = 'ceWIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 42 ])

ceBIm11 = Parameter(name = 'ceBIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 43 ])

ceBIm22 = Parameter(name = 'ceBIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 44 ])

ceBIm33 = Parameter(name = 'ceBIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 45 ])

ceBIm12 = Parameter(name = 'ceBIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 46 ])

ceBIm13 = Parameter(name = 'ceBIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 47 ])

ceBIm23 = Parameter(name = 'ceBIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 48 ])

ceBIm21 = Parameter(name = 'ceBIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 49 ])

ceBIm31 = Parameter(name = 'ceBIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 50 ])

ceBIm32 = Parameter(name = 'ceBIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 51 ])

cuGIm11 = Parameter(name = 'cuGIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 52 ])

cuGIm22 = Parameter(name = 'cuGIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 53 ])

cuGIm33 = Parameter(name = 'cuGIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 54 ])

cuGIm12 = Parameter(name = 'cuGIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 55 ])

cuGIm13 = Parameter(name = 'cuGIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 56 ])

cuGIm23 = Parameter(name = 'cuGIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 57 ])

cuGIm21 = Parameter(name = 'cuGIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 58 ])

cuGIm31 = Parameter(name = 'cuGIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 59 ])

cuGIm32 = Parameter(name = 'cuGIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuGIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 60 ])

cuWIm11 = Parameter(name = 'cuWIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 61 ])

cuWIm22 = Parameter(name = 'cuWIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 62 ])

cuWIm33 = Parameter(name = 'cuWIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 63 ])

cuWIm12 = Parameter(name = 'cuWIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 64 ])

cuWIm13 = Parameter(name = 'cuWIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 65 ])

cuWIm23 = Parameter(name = 'cuWIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 66 ])

cuWIm21 = Parameter(name = 'cuWIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 67 ])

cuWIm31 = Parameter(name = 'cuWIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 68 ])

cuWIm32 = Parameter(name = 'cuWIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuWIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 69 ])

cuBIm11 = Parameter(name = 'cuBIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 70 ])

cuBIm22 = Parameter(name = 'cuBIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 71 ])

cuBIm33 = Parameter(name = 'cuBIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 72 ])

cuBIm12 = Parameter(name = 'cuBIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 73 ])

cuBIm13 = Parameter(name = 'cuBIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 74 ])

cuBIm23 = Parameter(name = 'cuBIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 75 ])

cuBIm21 = Parameter(name = 'cuBIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 76 ])

cuBIm31 = Parameter(name = 'cuBIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 77 ])

cuBIm32 = Parameter(name = 'cuBIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cuBIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 78 ])

cdGIm11 = Parameter(name = 'cdGIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 79 ])

cdGIm22 = Parameter(name = 'cdGIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 80 ])

cdGIm33 = Parameter(name = 'cdGIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 81 ])

cdGIm12 = Parameter(name = 'cdGIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 82 ])

cdGIm13 = Parameter(name = 'cdGIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 83 ])

cdGIm23 = Parameter(name = 'cdGIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 84 ])

cdGIm21 = Parameter(name = 'cdGIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 85 ])

cdGIm31 = Parameter(name = 'cdGIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 86 ])

cdGIm32 = Parameter(name = 'cdGIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdGIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 87 ])

cdWIm11 = Parameter(name = 'cdWIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 88 ])

cdWIm22 = Parameter(name = 'cdWIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 89 ])

cdWIm33 = Parameter(name = 'cdWIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 90 ])

cdWIm12 = Parameter(name = 'cdWIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 91 ])

cdWIm13 = Parameter(name = 'cdWIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 92 ])

cdWIm23 = Parameter(name = 'cdWIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 93 ])

cdWIm21 = Parameter(name = 'cdWIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 94 ])

cdWIm31 = Parameter(name = 'cdWIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 95 ])

cdWIm32 = Parameter(name = 'cdWIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdWIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 96 ])

cdBIm11 = Parameter(name = 'cdBIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 97 ])

cdBIm22 = Parameter(name = 'cdBIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 98 ])

cdBIm33 = Parameter(name = 'cdBIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 99 ])

cdBIm12 = Parameter(name = 'cdBIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 100 ])

cdBIm13 = Parameter(name = 'cdBIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 101 ])

cdBIm23 = Parameter(name = 'cdBIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 102 ])

cdBIm21 = Parameter(name = 'cdBIm21',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm21}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 103 ])

cdBIm31 = Parameter(name = 'cdBIm31',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm31}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 104 ])

cdBIm32 = Parameter(name = 'cdBIm32',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cdBIm32}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 105 ])

cHl1Im12 = Parameter(name = 'cHl1Im12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Im12}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 106 ])

cHl1Im13 = Parameter(name = 'cHl1Im13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Im13}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 107 ])

cHl1Im23 = Parameter(name = 'cHl1Im23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl1Im23}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 108 ])

cHl3Im12 = Parameter(name = 'cHl3Im12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Im12}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 109 ])

cHl3Im13 = Parameter(name = 'cHl3Im13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Im13}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 110 ])

cHl3Im23 = Parameter(name = 'cHl3Im23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHl3Im23}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 111 ])

cHeIm12 = Parameter(name = 'cHeIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 112 ])

cHeIm13 = Parameter(name = 'cHeIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 113 ])

cHeIm23 = Parameter(name = 'cHeIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHeIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 114 ])

cHq1Im12 = Parameter(name = 'cHq1Im12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Im12}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 115 ])

cHq1Im13 = Parameter(name = 'cHq1Im13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Im13}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 116 ])

cHq1Im23 = Parameter(name = 'cHq1Im23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq1Im23}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 117 ])

cHq3Im12 = Parameter(name = 'cHq3Im12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Im12}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 118 ])

cHq3Im13 = Parameter(name = 'cHq3Im13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Im13}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 119 ])

cHq3Im23 = Parameter(name = 'cHq3Im23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHq3Im23}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 120 ])

cHuIm12 = Parameter(name = 'cHuIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 121 ])

cHuIm13 = Parameter(name = 'cHuIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 122 ])

cHuIm23 = Parameter(name = 'cHuIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHuIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 123 ])

cHdIm12 = Parameter(name = 'cHdIm12',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdIm12}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 124 ])

cHdIm13 = Parameter(name = 'cHdIm13',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdIm13}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 125 ])

cHdIm23 = Parameter(name = 'cHdIm23',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cHdIm23}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 126 ])

cHudIm11 = Parameter(name = 'cHudIm11',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm11}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 127 ])

cHudIm22 = Parameter(name = 'cHudIm22',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm22}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 128 ])

cHudIm33 = Parameter(name = 'cHudIm33',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm33}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 129 ])

cHudIm12 = Parameter(name = 'cHudIm12',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm12}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 130 ])

cHudIm13 = Parameter(name = 'cHudIm13',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm13}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 131 ])

cHudIm23 = Parameter(name = 'cHudIm23',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm23}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 132 ])

cHudIm21 = Parameter(name = 'cHudIm21',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm21}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 133 ])

cHudIm31 = Parameter(name = 'cHudIm31',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm31}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 134 ])

cHudIm32 = Parameter(name = 'cHudIm32',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cHudIm32}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 135 ])

cllIm1112 = Parameter(name = 'cllIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 136 ])

cllIm1113 = Parameter(name = 'cllIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 137 ])

cllIm1123 = Parameter(name = 'cllIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 138 ])

cllIm1212 = Parameter(name = 'cllIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 139 ])

cllIm1213 = Parameter(name = 'cllIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 140 ])

cllIm1231 = Parameter(name = 'cllIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 141 ])

cllIm1222 = Parameter(name = 'cllIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 142 ])

cllIm1223 = Parameter(name = 'cllIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 143 ])

cllIm1232 = Parameter(name = 'cllIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 144 ])

cllIm1233 = Parameter(name = 'cllIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 145 ])

cllIm1313 = Parameter(name = 'cllIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 146 ])

cllIm1322 = Parameter(name = 'cllIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 147 ])

cllIm1332 = Parameter(name = 'cllIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 148 ])

cllIm1323 = Parameter(name = 'cllIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 149 ])

cllIm1333 = Parameter(name = 'cllIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 150 ])

cllIm2223 = Parameter(name = 'cllIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 151 ])

cllIm2323 = Parameter(name = 'cllIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 152 ])

cllIm3323 = Parameter(name = 'cllIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cllIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 153 ])

cqq1Im1112 = Parameter(name = 'cqq1Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 154 ])

cqq1Im1113 = Parameter(name = 'cqq1Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 155 ])

cqq1Im1123 = Parameter(name = 'cqq1Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 156 ])

cqq1Im1212 = Parameter(name = 'cqq1Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 157 ])

cqq1Im1213 = Parameter(name = 'cqq1Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 158 ])

cqq1Im1231 = Parameter(name = 'cqq1Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 159 ])

cqq1Im1222 = Parameter(name = 'cqq1Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 160 ])

cqq1Im1223 = Parameter(name = 'cqq1Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 161 ])

cqq1Im1232 = Parameter(name = 'cqq1Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 162 ])

cqq1Im1233 = Parameter(name = 'cqq1Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 163 ])

cqq1Im1313 = Parameter(name = 'cqq1Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 164 ])

cqq1Im1322 = Parameter(name = 'cqq1Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 165 ])

cqq1Im1332 = Parameter(name = 'cqq1Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 166 ])

cqq1Im1323 = Parameter(name = 'cqq1Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 167 ])

cqq1Im1333 = Parameter(name = 'cqq1Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 168 ])

cqq1Im2223 = Parameter(name = 'cqq1Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 169 ])

cqq1Im2323 = Parameter(name = 'cqq1Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 170 ])

cqq1Im3323 = Parameter(name = 'cqq1Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq1Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 171 ])

cqq3Im1112 = Parameter(name = 'cqq3Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 172 ])

cqq3Im1113 = Parameter(name = 'cqq3Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 173 ])

cqq3Im1123 = Parameter(name = 'cqq3Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 174 ])

cqq3Im1212 = Parameter(name = 'cqq3Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 175 ])

cqq3Im1213 = Parameter(name = 'cqq3Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 176 ])

cqq3Im1231 = Parameter(name = 'cqq3Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 177 ])

cqq3Im1222 = Parameter(name = 'cqq3Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 178 ])

cqq3Im1223 = Parameter(name = 'cqq3Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 179 ])

cqq3Im1232 = Parameter(name = 'cqq3Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 180 ])

cqq3Im1233 = Parameter(name = 'cqq3Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 181 ])

cqq3Im1313 = Parameter(name = 'cqq3Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 182 ])

cqq3Im1322 = Parameter(name = 'cqq3Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 183 ])

cqq3Im1332 = Parameter(name = 'cqq3Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 184 ])

cqq3Im1323 = Parameter(name = 'cqq3Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 185 ])

cqq3Im1333 = Parameter(name = 'cqq3Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 186 ])

cqq3Im2223 = Parameter(name = 'cqq3Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 187 ])

cqq3Im2323 = Parameter(name = 'cqq3Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 188 ])

cqq3Im3323 = Parameter(name = 'cqq3Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqq3Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 189 ])

cuuIm1112 = Parameter(name = 'cuuIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 190 ])

cuuIm1113 = Parameter(name = 'cuuIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 191 ])

cuuIm1123 = Parameter(name = 'cuuIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 192 ])

cuuIm1212 = Parameter(name = 'cuuIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 193 ])

cuuIm1213 = Parameter(name = 'cuuIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 194 ])

cuuIm1231 = Parameter(name = 'cuuIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 195 ])

cuuIm1222 = Parameter(name = 'cuuIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 196 ])

cuuIm1223 = Parameter(name = 'cuuIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 197 ])

cuuIm1232 = Parameter(name = 'cuuIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 198 ])

cuuIm1233 = Parameter(name = 'cuuIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 199 ])

cuuIm1313 = Parameter(name = 'cuuIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 200 ])

cuuIm1322 = Parameter(name = 'cuuIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 201 ])

cuuIm1332 = Parameter(name = 'cuuIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 202 ])

cuuIm1323 = Parameter(name = 'cuuIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 203 ])

cuuIm1333 = Parameter(name = 'cuuIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 204 ])

cuuIm2223 = Parameter(name = 'cuuIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 205 ])

cuuIm2323 = Parameter(name = 'cuuIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 206 ])

cuuIm3323 = Parameter(name = 'cuuIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cuuIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 207 ])

cddIm1112 = Parameter(name = 'cddIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 208 ])

cddIm1113 = Parameter(name = 'cddIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 209 ])

cddIm1123 = Parameter(name = 'cddIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 210 ])

cddIm1212 = Parameter(name = 'cddIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 211 ])

cddIm1213 = Parameter(name = 'cddIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 212 ])

cddIm1231 = Parameter(name = 'cddIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 213 ])

cddIm1222 = Parameter(name = 'cddIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 214 ])

cddIm1223 = Parameter(name = 'cddIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 215 ])

cddIm1232 = Parameter(name = 'cddIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 216 ])

cddIm1233 = Parameter(name = 'cddIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 217 ])

cddIm1313 = Parameter(name = 'cddIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 218 ])

cddIm1322 = Parameter(name = 'cddIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 219 ])

cddIm1332 = Parameter(name = 'cddIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 220 ])

cddIm1323 = Parameter(name = 'cddIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 221 ])

cddIm1333 = Parameter(name = 'cddIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 222 ])

cddIm2223 = Parameter(name = 'cddIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 223 ])

cddIm2323 = Parameter(name = 'cddIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 224 ])

cddIm3323 = Parameter(name = 'cddIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cddIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 225 ])

ceeIm1112 = Parameter(name = 'ceeIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 226 ])

ceeIm1113 = Parameter(name = 'ceeIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 227 ])

ceeIm1123 = Parameter(name = 'ceeIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 228 ])

ceeIm1212 = Parameter(name = 'ceeIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 229 ])

ceeIm1213 = Parameter(name = 'ceeIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 230 ])

ceeIm1222 = Parameter(name = 'ceeIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 231 ])

ceeIm1232 = Parameter(name = 'ceeIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 232 ])

ceeIm1233 = Parameter(name = 'ceeIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 233 ])

ceeIm1313 = Parameter(name = 'ceeIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 234 ])

ceeIm1322 = Parameter(name = 'ceeIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 235 ])

ceeIm1323 = Parameter(name = 'ceeIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 236 ])

ceeIm1333 = Parameter(name = 'ceeIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 237 ])

ceeIm2223 = Parameter(name = 'ceeIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 238 ])

ceeIm2323 = Parameter(name = 'ceeIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 239 ])

ceeIm3323 = Parameter(name = 'ceeIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceeIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 240 ])

clq1Im1112 = Parameter(name = 'clq1Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 241 ])

clq1Im1113 = Parameter(name = 'clq1Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 242 ])

clq1Im1123 = Parameter(name = 'clq1Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 243 ])

clq1Im1211 = Parameter(name = 'clq1Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 244 ])

clq1Im1212 = Parameter(name = 'clq1Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 245 ])

clq1Im1221 = Parameter(name = 'clq1Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 246 ])

clq1Im1213 = Parameter(name = 'clq1Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 247 ])

clq1Im1231 = Parameter(name = 'clq1Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 248 ])

clq1Im1222 = Parameter(name = 'clq1Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 249 ])

clq1Im1223 = Parameter(name = 'clq1Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 250 ])

clq1Im1232 = Parameter(name = 'clq1Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 251 ])

clq1Im1233 = Parameter(name = 'clq1Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 252 ])

clq1Im1311 = Parameter(name = 'clq1Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 253 ])

clq1Im1312 = Parameter(name = 'clq1Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 254 ])

clq1Im1313 = Parameter(name = 'clq1Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 255 ])

clq1Im1331 = Parameter(name = 'clq1Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 256 ])

clq1Im1321 = Parameter(name = 'clq1Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 257 ])

clq1Im1322 = Parameter(name = 'clq1Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 258 ])

clq1Im1332 = Parameter(name = 'clq1Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 259 ])

clq1Im1323 = Parameter(name = 'clq1Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 260 ])

clq1Im1333 = Parameter(name = 'clq1Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 261 ])

clq1Im2212 = Parameter(name = 'clq1Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 262 ])

clq1Im2213 = Parameter(name = 'clq1Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 263 ])

clq1Im2223 = Parameter(name = 'clq1Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 264 ])

clq1Im2311 = Parameter(name = 'clq1Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 265 ])

clq1Im2312 = Parameter(name = 'clq1Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 266 ])

clq1Im2313 = Parameter(name = 'clq1Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 267 ])

clq1Im2321 = Parameter(name = 'clq1Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 268 ])

clq1Im2322 = Parameter(name = 'clq1Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 269 ])

clq1Im2323 = Parameter(name = 'clq1Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 270 ])

clq1Im2331 = Parameter(name = 'clq1Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 271 ])

clq1Im2332 = Parameter(name = 'clq1Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 272 ])

clq1Im2333 = Parameter(name = 'clq1Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 273 ])

clq1Im3312 = Parameter(name = 'clq1Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 274 ])

clq1Im3313 = Parameter(name = 'clq1Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 275 ])

clq1Im3323 = Parameter(name = 'clq1Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq1Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 276 ])

clq3Im1112 = Parameter(name = 'clq3Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 277 ])

clq3Im1113 = Parameter(name = 'clq3Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 278 ])

clq3Im1123 = Parameter(name = 'clq3Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 279 ])

clq3Im1211 = Parameter(name = 'clq3Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 280 ])

clq3Im1212 = Parameter(name = 'clq3Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 281 ])

clq3Im1221 = Parameter(name = 'clq3Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 282 ])

clq3Im1213 = Parameter(name = 'clq3Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 283 ])

clq3Im1231 = Parameter(name = 'clq3Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 284 ])

clq3Im1222 = Parameter(name = 'clq3Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 285 ])

clq3Im1223 = Parameter(name = 'clq3Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 286 ])

clq3Im1232 = Parameter(name = 'clq3Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 287 ])

clq3Im1233 = Parameter(name = 'clq3Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 288 ])

clq3Im1311 = Parameter(name = 'clq3Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 289 ])

clq3Im1312 = Parameter(name = 'clq3Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 290 ])

clq3Im1313 = Parameter(name = 'clq3Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 291 ])

clq3Im1331 = Parameter(name = 'clq3Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 292 ])

clq3Im1321 = Parameter(name = 'clq3Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 293 ])

clq3Im1322 = Parameter(name = 'clq3Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 294 ])

clq3Im1332 = Parameter(name = 'clq3Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 295 ])

clq3Im1323 = Parameter(name = 'clq3Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 296 ])

clq3Im1333 = Parameter(name = 'clq3Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 297 ])

clq3Im2212 = Parameter(name = 'clq3Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 298 ])

clq3Im2213 = Parameter(name = 'clq3Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 299 ])

clq3Im2223 = Parameter(name = 'clq3Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 300 ])

clq3Im2311 = Parameter(name = 'clq3Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 301 ])

clq3Im2312 = Parameter(name = 'clq3Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 302 ])

clq3Im2313 = Parameter(name = 'clq3Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 303 ])

clq3Im2321 = Parameter(name = 'clq3Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 304 ])

clq3Im2322 = Parameter(name = 'clq3Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 305 ])

clq3Im2323 = Parameter(name = 'clq3Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 306 ])

clq3Im2331 = Parameter(name = 'clq3Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 307 ])

clq3Im2332 = Parameter(name = 'clq3Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 308 ])

clq3Im2333 = Parameter(name = 'clq3Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 309 ])

clq3Im3312 = Parameter(name = 'clq3Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 310 ])

clq3Im3313 = Parameter(name = 'clq3Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 311 ])

clq3Im3323 = Parameter(name = 'clq3Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{clq3Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 312 ])

ceuIm1112 = Parameter(name = 'ceuIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 313 ])

ceuIm1113 = Parameter(name = 'ceuIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 314 ])

ceuIm1123 = Parameter(name = 'ceuIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 315 ])

ceuIm1211 = Parameter(name = 'ceuIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 316 ])

ceuIm1212 = Parameter(name = 'ceuIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 317 ])

ceuIm1221 = Parameter(name = 'ceuIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 318 ])

ceuIm1213 = Parameter(name = 'ceuIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 319 ])

ceuIm1231 = Parameter(name = 'ceuIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 320 ])

ceuIm1222 = Parameter(name = 'ceuIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 321 ])

ceuIm1223 = Parameter(name = 'ceuIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 322 ])

ceuIm1232 = Parameter(name = 'ceuIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 323 ])

ceuIm1233 = Parameter(name = 'ceuIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 324 ])

ceuIm1311 = Parameter(name = 'ceuIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 325 ])

ceuIm1312 = Parameter(name = 'ceuIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 326 ])

ceuIm1313 = Parameter(name = 'ceuIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 327 ])

ceuIm1331 = Parameter(name = 'ceuIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 328 ])

ceuIm1321 = Parameter(name = 'ceuIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 329 ])

ceuIm1322 = Parameter(name = 'ceuIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 330 ])

ceuIm1332 = Parameter(name = 'ceuIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 331 ])

ceuIm1323 = Parameter(name = 'ceuIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 332 ])

ceuIm1333 = Parameter(name = 'ceuIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 333 ])

ceuIm2212 = Parameter(name = 'ceuIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 334 ])

ceuIm2213 = Parameter(name = 'ceuIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 335 ])

ceuIm2223 = Parameter(name = 'ceuIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 336 ])

ceuIm2311 = Parameter(name = 'ceuIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 337 ])

ceuIm2312 = Parameter(name = 'ceuIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 338 ])

ceuIm2313 = Parameter(name = 'ceuIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 339 ])

ceuIm2321 = Parameter(name = 'ceuIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 340 ])

ceuIm2322 = Parameter(name = 'ceuIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 341 ])

ceuIm2323 = Parameter(name = 'ceuIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 342 ])

ceuIm2331 = Parameter(name = 'ceuIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 343 ])

ceuIm2332 = Parameter(name = 'ceuIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 344 ])

ceuIm2333 = Parameter(name = 'ceuIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 345 ])

ceuIm3312 = Parameter(name = 'ceuIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 346 ])

ceuIm3313 = Parameter(name = 'ceuIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 347 ])

ceuIm3323 = Parameter(name = 'ceuIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{ceuIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 348 ])

cedIm1112 = Parameter(name = 'cedIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 349 ])

cedIm1113 = Parameter(name = 'cedIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 350 ])

cedIm1123 = Parameter(name = 'cedIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 351 ])

cedIm1211 = Parameter(name = 'cedIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 352 ])

cedIm1212 = Parameter(name = 'cedIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 353 ])

cedIm1221 = Parameter(name = 'cedIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 354 ])

cedIm1213 = Parameter(name = 'cedIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 355 ])

cedIm1231 = Parameter(name = 'cedIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 356 ])

cedIm1222 = Parameter(name = 'cedIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 357 ])

cedIm1223 = Parameter(name = 'cedIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 358 ])

cedIm1232 = Parameter(name = 'cedIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 359 ])

cedIm1233 = Parameter(name = 'cedIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 360 ])

cedIm1311 = Parameter(name = 'cedIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 361 ])

cedIm1312 = Parameter(name = 'cedIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 362 ])

cedIm1313 = Parameter(name = 'cedIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 363 ])

cedIm1331 = Parameter(name = 'cedIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 364 ])

cedIm1321 = Parameter(name = 'cedIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 365 ])

cedIm1322 = Parameter(name = 'cedIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 366 ])

cedIm1332 = Parameter(name = 'cedIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 367 ])

cedIm1323 = Parameter(name = 'cedIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 368 ])

cedIm1333 = Parameter(name = 'cedIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 369 ])

cedIm2212 = Parameter(name = 'cedIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 370 ])

cedIm2213 = Parameter(name = 'cedIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 371 ])

cedIm2223 = Parameter(name = 'cedIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 372 ])

cedIm2311 = Parameter(name = 'cedIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 373 ])

cedIm2312 = Parameter(name = 'cedIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 374 ])

cedIm2313 = Parameter(name = 'cedIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 375 ])

cedIm2321 = Parameter(name = 'cedIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 376 ])

cedIm2322 = Parameter(name = 'cedIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 377 ])

cedIm2323 = Parameter(name = 'cedIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 378 ])

cedIm2331 = Parameter(name = 'cedIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 379 ])

cedIm2332 = Parameter(name = 'cedIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 380 ])

cedIm2333 = Parameter(name = 'cedIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 381 ])

cedIm3312 = Parameter(name = 'cedIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 382 ])

cedIm3313 = Parameter(name = 'cedIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 383 ])

cedIm3323 = Parameter(name = 'cedIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cedIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 384 ])

cud1Im1112 = Parameter(name = 'cud1Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 385 ])

cud1Im1113 = Parameter(name = 'cud1Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 386 ])

cud1Im1123 = Parameter(name = 'cud1Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 387 ])

cud1Im1211 = Parameter(name = 'cud1Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 388 ])

cud1Im1212 = Parameter(name = 'cud1Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 389 ])

cud1Im1221 = Parameter(name = 'cud1Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 390 ])

cud1Im1213 = Parameter(name = 'cud1Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 391 ])

cud1Im1231 = Parameter(name = 'cud1Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 392 ])

cud1Im1222 = Parameter(name = 'cud1Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 393 ])

cud1Im1223 = Parameter(name = 'cud1Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 394 ])

cud1Im1232 = Parameter(name = 'cud1Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 395 ])

cud1Im1233 = Parameter(name = 'cud1Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 396 ])

cud1Im1311 = Parameter(name = 'cud1Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 397 ])

cud1Im1312 = Parameter(name = 'cud1Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 398 ])

cud1Im1313 = Parameter(name = 'cud1Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 399 ])

cud1Im1331 = Parameter(name = 'cud1Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 400 ])

cud1Im1321 = Parameter(name = 'cud1Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 401 ])

cud1Im1322 = Parameter(name = 'cud1Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 402 ])

cud1Im1332 = Parameter(name = 'cud1Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 403 ])

cud1Im1323 = Parameter(name = 'cud1Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 404 ])

cud1Im1333 = Parameter(name = 'cud1Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 405 ])

cud1Im2212 = Parameter(name = 'cud1Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 406 ])

cud1Im2213 = Parameter(name = 'cud1Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 407 ])

cud1Im2223 = Parameter(name = 'cud1Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 408 ])

cud1Im2311 = Parameter(name = 'cud1Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 409 ])

cud1Im2312 = Parameter(name = 'cud1Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 410 ])

cud1Im2313 = Parameter(name = 'cud1Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 411 ])

cud1Im2321 = Parameter(name = 'cud1Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 412 ])

cud1Im2322 = Parameter(name = 'cud1Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 413 ])

cud1Im2323 = Parameter(name = 'cud1Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 414 ])

cud1Im2331 = Parameter(name = 'cud1Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 415 ])

cud1Im2332 = Parameter(name = 'cud1Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 416 ])

cud1Im2333 = Parameter(name = 'cud1Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 417 ])

cud1Im3312 = Parameter(name = 'cud1Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 418 ])

cud1Im3313 = Parameter(name = 'cud1Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 419 ])

cud1Im3323 = Parameter(name = 'cud1Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud1Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 420 ])

cud8Im1112 = Parameter(name = 'cud8Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 421 ])

cud8Im1113 = Parameter(name = 'cud8Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 422 ])

cud8Im1123 = Parameter(name = 'cud8Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 423 ])

cud8Im1211 = Parameter(name = 'cud8Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 424 ])

cud8Im1212 = Parameter(name = 'cud8Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 425 ])

cud8Im1221 = Parameter(name = 'cud8Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 426 ])

cud8Im1213 = Parameter(name = 'cud8Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 427 ])

cud8Im1231 = Parameter(name = 'cud8Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 428 ])

cud8Im1222 = Parameter(name = 'cud8Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 429 ])

cud8Im1223 = Parameter(name = 'cud8Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 430 ])

cud8Im1232 = Parameter(name = 'cud8Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 431 ])

cud8Im1233 = Parameter(name = 'cud8Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 432 ])

cud8Im1311 = Parameter(name = 'cud8Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 433 ])

cud8Im1312 = Parameter(name = 'cud8Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 434 ])

cud8Im1313 = Parameter(name = 'cud8Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 435 ])

cud8Im1331 = Parameter(name = 'cud8Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 436 ])

cud8Im1321 = Parameter(name = 'cud8Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 437 ])

cud8Im1322 = Parameter(name = 'cud8Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 438 ])

cud8Im1332 = Parameter(name = 'cud8Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 439 ])

cud8Im1323 = Parameter(name = 'cud8Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 440 ])

cud8Im1333 = Parameter(name = 'cud8Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 441 ])

cud8Im2212 = Parameter(name = 'cud8Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 442 ])

cud8Im2213 = Parameter(name = 'cud8Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 443 ])

cud8Im2223 = Parameter(name = 'cud8Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 444 ])

cud8Im2311 = Parameter(name = 'cud8Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 445 ])

cud8Im2312 = Parameter(name = 'cud8Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 446 ])

cud8Im2313 = Parameter(name = 'cud8Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 447 ])

cud8Im2321 = Parameter(name = 'cud8Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 448 ])

cud8Im2322 = Parameter(name = 'cud8Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 449 ])

cud8Im2323 = Parameter(name = 'cud8Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 450 ])

cud8Im2331 = Parameter(name = 'cud8Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 451 ])

cud8Im2332 = Parameter(name = 'cud8Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 452 ])

cud8Im2333 = Parameter(name = 'cud8Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 453 ])

cud8Im3312 = Parameter(name = 'cud8Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 454 ])

cud8Im3313 = Parameter(name = 'cud8Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 455 ])

cud8Im3323 = Parameter(name = 'cud8Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cud8Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 456 ])

cleIm1112 = Parameter(name = 'cleIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 457 ])

cleIm1113 = Parameter(name = 'cleIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 458 ])

cleIm1123 = Parameter(name = 'cleIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 459 ])

cleIm1211 = Parameter(name = 'cleIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 460 ])

cleIm1212 = Parameter(name = 'cleIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 461 ])

cleIm1221 = Parameter(name = 'cleIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 462 ])

cleIm1213 = Parameter(name = 'cleIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 463 ])

cleIm1231 = Parameter(name = 'cleIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 464 ])

cleIm1222 = Parameter(name = 'cleIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 465 ])

cleIm1223 = Parameter(name = 'cleIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 466 ])

cleIm1232 = Parameter(name = 'cleIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 467 ])

cleIm1233 = Parameter(name = 'cleIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 468 ])

cleIm1311 = Parameter(name = 'cleIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 469 ])

cleIm1312 = Parameter(name = 'cleIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 470 ])

cleIm1313 = Parameter(name = 'cleIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 471 ])

cleIm1331 = Parameter(name = 'cleIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 472 ])

cleIm1321 = Parameter(name = 'cleIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 473 ])

cleIm1322 = Parameter(name = 'cleIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 474 ])

cleIm1332 = Parameter(name = 'cleIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 475 ])

cleIm1323 = Parameter(name = 'cleIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 476 ])

cleIm1333 = Parameter(name = 'cleIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 477 ])

cleIm2212 = Parameter(name = 'cleIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 478 ])

cleIm2213 = Parameter(name = 'cleIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 479 ])

cleIm2223 = Parameter(name = 'cleIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 480 ])

cleIm2311 = Parameter(name = 'cleIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 481 ])

cleIm2312 = Parameter(name = 'cleIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 482 ])

cleIm2313 = Parameter(name = 'cleIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 483 ])

cleIm2321 = Parameter(name = 'cleIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 484 ])

cleIm2322 = Parameter(name = 'cleIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 485 ])

cleIm2323 = Parameter(name = 'cleIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 486 ])

cleIm2331 = Parameter(name = 'cleIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 487 ])

cleIm2332 = Parameter(name = 'cleIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 488 ])

cleIm2333 = Parameter(name = 'cleIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 489 ])

cleIm3312 = Parameter(name = 'cleIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 490 ])

cleIm3313 = Parameter(name = 'cleIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 491 ])

cleIm3323 = Parameter(name = 'cleIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cleIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 492 ])

cluIm1112 = Parameter(name = 'cluIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 493 ])

cluIm1113 = Parameter(name = 'cluIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 494 ])

cluIm1123 = Parameter(name = 'cluIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 495 ])

cluIm1211 = Parameter(name = 'cluIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 496 ])

cluIm1212 = Parameter(name = 'cluIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 497 ])

cluIm1221 = Parameter(name = 'cluIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 498 ])

cluIm1213 = Parameter(name = 'cluIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 499 ])

cluIm1231 = Parameter(name = 'cluIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 500 ])

cluIm1222 = Parameter(name = 'cluIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 501 ])

cluIm1223 = Parameter(name = 'cluIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 502 ])

cluIm1232 = Parameter(name = 'cluIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 503 ])

cluIm1233 = Parameter(name = 'cluIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 504 ])

cluIm1311 = Parameter(name = 'cluIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 505 ])

cluIm1312 = Parameter(name = 'cluIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 506 ])

cluIm1313 = Parameter(name = 'cluIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 507 ])

cluIm1331 = Parameter(name = 'cluIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 508 ])

cluIm1321 = Parameter(name = 'cluIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 509 ])

cluIm1322 = Parameter(name = 'cluIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 510 ])

cluIm1332 = Parameter(name = 'cluIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 511 ])

cluIm1323 = Parameter(name = 'cluIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 512 ])

cluIm1333 = Parameter(name = 'cluIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 513 ])

cluIm2212 = Parameter(name = 'cluIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 514 ])

cluIm2213 = Parameter(name = 'cluIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 515 ])

cluIm2223 = Parameter(name = 'cluIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 516 ])

cluIm2311 = Parameter(name = 'cluIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 517 ])

cluIm2312 = Parameter(name = 'cluIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 518 ])

cluIm2313 = Parameter(name = 'cluIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 519 ])

cluIm2321 = Parameter(name = 'cluIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 520 ])

cluIm2322 = Parameter(name = 'cluIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 521 ])

cluIm2323 = Parameter(name = 'cluIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 522 ])

cluIm2331 = Parameter(name = 'cluIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 523 ])

cluIm2332 = Parameter(name = 'cluIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 524 ])

cluIm2333 = Parameter(name = 'cluIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 525 ])

cluIm3312 = Parameter(name = 'cluIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 526 ])

cluIm3313 = Parameter(name = 'cluIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 527 ])

cluIm3323 = Parameter(name = 'cluIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cluIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 528 ])

cldIm1112 = Parameter(name = 'cldIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 529 ])

cldIm1113 = Parameter(name = 'cldIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 530 ])

cldIm1123 = Parameter(name = 'cldIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 531 ])

cldIm1211 = Parameter(name = 'cldIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 532 ])

cldIm1212 = Parameter(name = 'cldIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 533 ])

cldIm1221 = Parameter(name = 'cldIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 534 ])

cldIm1213 = Parameter(name = 'cldIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 535 ])

cldIm1231 = Parameter(name = 'cldIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 536 ])

cldIm1222 = Parameter(name = 'cldIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 537 ])

cldIm1223 = Parameter(name = 'cldIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 538 ])

cldIm1232 = Parameter(name = 'cldIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 539 ])

cldIm1233 = Parameter(name = 'cldIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 540 ])

cldIm1311 = Parameter(name = 'cldIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 541 ])

cldIm1312 = Parameter(name = 'cldIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 542 ])

cldIm1313 = Parameter(name = 'cldIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 543 ])

cldIm1331 = Parameter(name = 'cldIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 544 ])

cldIm1321 = Parameter(name = 'cldIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 545 ])

cldIm1322 = Parameter(name = 'cldIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 546 ])

cldIm1332 = Parameter(name = 'cldIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 547 ])

cldIm1323 = Parameter(name = 'cldIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 548 ])

cldIm1333 = Parameter(name = 'cldIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 549 ])

cldIm2212 = Parameter(name = 'cldIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 550 ])

cldIm2213 = Parameter(name = 'cldIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 551 ])

cldIm2223 = Parameter(name = 'cldIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 552 ])

cldIm2311 = Parameter(name = 'cldIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 553 ])

cldIm2312 = Parameter(name = 'cldIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 554 ])

cldIm2313 = Parameter(name = 'cldIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 555 ])

cldIm2321 = Parameter(name = 'cldIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 556 ])

cldIm2322 = Parameter(name = 'cldIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 557 ])

cldIm2323 = Parameter(name = 'cldIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 558 ])

cldIm2331 = Parameter(name = 'cldIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 559 ])

cldIm2332 = Parameter(name = 'cldIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 560 ])

cldIm2333 = Parameter(name = 'cldIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 561 ])

cldIm3312 = Parameter(name = 'cldIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 562 ])

cldIm3313 = Parameter(name = 'cldIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 563 ])

cldIm3323 = Parameter(name = 'cldIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cldIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 564 ])

cqeIm1112 = Parameter(name = 'cqeIm1112',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1112}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 565 ])

cqeIm1113 = Parameter(name = 'cqeIm1113',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1113}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 566 ])

cqeIm1123 = Parameter(name = 'cqeIm1123',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1123}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 567 ])

cqeIm1211 = Parameter(name = 'cqeIm1211',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1211}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 568 ])

cqeIm1212 = Parameter(name = 'cqeIm1212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 569 ])

cqeIm1221 = Parameter(name = 'cqeIm1221',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1221}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 570 ])

cqeIm1213 = Parameter(name = 'cqeIm1213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 571 ])

cqeIm1231 = Parameter(name = 'cqeIm1231',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1231}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 572 ])

cqeIm1222 = Parameter(name = 'cqeIm1222',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1222}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 573 ])

cqeIm1223 = Parameter(name = 'cqeIm1223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 574 ])

cqeIm1232 = Parameter(name = 'cqeIm1232',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1232}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 575 ])

cqeIm1233 = Parameter(name = 'cqeIm1233',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1233}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 576 ])

cqeIm1311 = Parameter(name = 'cqeIm1311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 577 ])

cqeIm1312 = Parameter(name = 'cqeIm1312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 578 ])

cqeIm1313 = Parameter(name = 'cqeIm1313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 579 ])

cqeIm1331 = Parameter(name = 'cqeIm1331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 580 ])

cqeIm1321 = Parameter(name = 'cqeIm1321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 581 ])

cqeIm1322 = Parameter(name = 'cqeIm1322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 582 ])

cqeIm1332 = Parameter(name = 'cqeIm1332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 583 ])

cqeIm1323 = Parameter(name = 'cqeIm1323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 584 ])

cqeIm1333 = Parameter(name = 'cqeIm1333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm1333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 585 ])

cqeIm2212 = Parameter(name = 'cqeIm2212',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2212}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 586 ])

cqeIm2213 = Parameter(name = 'cqeIm2213',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2213}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 587 ])

cqeIm2223 = Parameter(name = 'cqeIm2223',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2223}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 588 ])

cqeIm2311 = Parameter(name = 'cqeIm2311',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2311}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 589 ])

cqeIm2312 = Parameter(name = 'cqeIm2312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 590 ])

cqeIm2313 = Parameter(name = 'cqeIm2313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 591 ])

cqeIm2321 = Parameter(name = 'cqeIm2321',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2321}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 592 ])

cqeIm2322 = Parameter(name = 'cqeIm2322',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2322}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 593 ])

cqeIm2323 = Parameter(name = 'cqeIm2323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 594 ])

cqeIm2331 = Parameter(name = 'cqeIm2331',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2331}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 595 ])

cqeIm2332 = Parameter(name = 'cqeIm2332',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2332}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 596 ])

cqeIm2333 = Parameter(name = 'cqeIm2333',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm2333}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 597 ])

cqeIm3312 = Parameter(name = 'cqeIm3312',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm3312}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 598 ])

cqeIm3313 = Parameter(name = 'cqeIm3313',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm3313}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 599 ])

cqeIm3323 = Parameter(name = 'cqeIm3323',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cqeIm3323}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 600 ])

cqu1Im1112 = Parameter(name = 'cqu1Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 601 ])

cqu1Im1113 = Parameter(name = 'cqu1Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 602 ])

cqu1Im1123 = Parameter(name = 'cqu1Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 603 ])

cqu1Im1211 = Parameter(name = 'cqu1Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 604 ])

cqu1Im1212 = Parameter(name = 'cqu1Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 605 ])

cqu1Im1221 = Parameter(name = 'cqu1Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 606 ])

cqu1Im1213 = Parameter(name = 'cqu1Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 607 ])

cqu1Im1231 = Parameter(name = 'cqu1Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 608 ])

cqu1Im1222 = Parameter(name = 'cqu1Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 609 ])

cqu1Im1223 = Parameter(name = 'cqu1Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 610 ])

cqu1Im1232 = Parameter(name = 'cqu1Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 611 ])

cqu1Im1233 = Parameter(name = 'cqu1Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 612 ])

cqu1Im1311 = Parameter(name = 'cqu1Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 613 ])

cqu1Im1312 = Parameter(name = 'cqu1Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 614 ])

cqu1Im1313 = Parameter(name = 'cqu1Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 615 ])

cqu1Im1331 = Parameter(name = 'cqu1Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 616 ])

cqu1Im1321 = Parameter(name = 'cqu1Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 617 ])

cqu1Im1322 = Parameter(name = 'cqu1Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 618 ])

cqu1Im1332 = Parameter(name = 'cqu1Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 619 ])

cqu1Im1323 = Parameter(name = 'cqu1Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 620 ])

cqu1Im1333 = Parameter(name = 'cqu1Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 621 ])

cqu1Im2212 = Parameter(name = 'cqu1Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 622 ])

cqu1Im2213 = Parameter(name = 'cqu1Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 623 ])

cqu1Im2223 = Parameter(name = 'cqu1Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 624 ])

cqu1Im2311 = Parameter(name = 'cqu1Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 625 ])

cqu1Im2312 = Parameter(name = 'cqu1Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 626 ])

cqu1Im2313 = Parameter(name = 'cqu1Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 627 ])

cqu1Im2321 = Parameter(name = 'cqu1Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 628 ])

cqu1Im2322 = Parameter(name = 'cqu1Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 629 ])

cqu1Im2323 = Parameter(name = 'cqu1Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 630 ])

cqu1Im2331 = Parameter(name = 'cqu1Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 631 ])

cqu1Im2332 = Parameter(name = 'cqu1Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 632 ])

cqu1Im2333 = Parameter(name = 'cqu1Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 633 ])

cqu1Im3312 = Parameter(name = 'cqu1Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 634 ])

cqu1Im3313 = Parameter(name = 'cqu1Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 635 ])

cqu1Im3323 = Parameter(name = 'cqu1Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu1Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 636 ])

cqd1Im1112 = Parameter(name = 'cqd1Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 637 ])

cqd1Im1113 = Parameter(name = 'cqd1Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 638 ])

cqd1Im1123 = Parameter(name = 'cqd1Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 639 ])

cqd1Im1211 = Parameter(name = 'cqd1Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 640 ])

cqd1Im1212 = Parameter(name = 'cqd1Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 641 ])

cqd1Im1221 = Parameter(name = 'cqd1Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 642 ])

cqd1Im1213 = Parameter(name = 'cqd1Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 643 ])

cqd1Im1231 = Parameter(name = 'cqd1Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 644 ])

cqd1Im1222 = Parameter(name = 'cqd1Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 645 ])

cqd1Im1223 = Parameter(name = 'cqd1Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 646 ])

cqd1Im1232 = Parameter(name = 'cqd1Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 647 ])

cqd1Im1233 = Parameter(name = 'cqd1Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 648 ])

cqd1Im1311 = Parameter(name = 'cqd1Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 649 ])

cqd1Im1312 = Parameter(name = 'cqd1Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 650 ])

cqd1Im1313 = Parameter(name = 'cqd1Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 651 ])

cqd1Im1331 = Parameter(name = 'cqd1Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 652 ])

cqd1Im1321 = Parameter(name = 'cqd1Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 653 ])

cqd1Im1322 = Parameter(name = 'cqd1Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 654 ])

cqd1Im1332 = Parameter(name = 'cqd1Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 655 ])

cqd1Im1323 = Parameter(name = 'cqd1Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 656 ])

cqd1Im1333 = Parameter(name = 'cqd1Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 657 ])

cqd1Im2212 = Parameter(name = 'cqd1Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 658 ])

cqd1Im2213 = Parameter(name = 'cqd1Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 659 ])

cqd1Im2223 = Parameter(name = 'cqd1Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 660 ])

cqd1Im2311 = Parameter(name = 'cqd1Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 661 ])

cqd1Im2312 = Parameter(name = 'cqd1Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 662 ])

cqd1Im2313 = Parameter(name = 'cqd1Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 663 ])

cqd1Im2321 = Parameter(name = 'cqd1Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 664 ])

cqd1Im2322 = Parameter(name = 'cqd1Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 665 ])

cqd1Im2323 = Parameter(name = 'cqd1Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 666 ])

cqd1Im2331 = Parameter(name = 'cqd1Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 667 ])

cqd1Im2332 = Parameter(name = 'cqd1Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 668 ])

cqd1Im2333 = Parameter(name = 'cqd1Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 669 ])

cqd1Im3312 = Parameter(name = 'cqd1Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 670 ])

cqd1Im3313 = Parameter(name = 'cqd1Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 671 ])

cqd1Im3323 = Parameter(name = 'cqd1Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd1Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 672 ])

cqu8Im1112 = Parameter(name = 'cqu8Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 673 ])

cqu8Im1113 = Parameter(name = 'cqu8Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 674 ])

cqu8Im1123 = Parameter(name = 'cqu8Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 675 ])

cqu8Im1211 = Parameter(name = 'cqu8Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 676 ])

cqu8Im1212 = Parameter(name = 'cqu8Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 677 ])

cqu8Im1221 = Parameter(name = 'cqu8Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 678 ])

cqu8Im1213 = Parameter(name = 'cqu8Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 679 ])

cqu8Im1231 = Parameter(name = 'cqu8Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 680 ])

cqu8Im1222 = Parameter(name = 'cqu8Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 681 ])

cqu8Im1223 = Parameter(name = 'cqu8Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 682 ])

cqu8Im1232 = Parameter(name = 'cqu8Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 683 ])

cqu8Im1233 = Parameter(name = 'cqu8Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 684 ])

cqu8Im1311 = Parameter(name = 'cqu8Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 685 ])

cqu8Im1312 = Parameter(name = 'cqu8Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 686 ])

cqu8Im1313 = Parameter(name = 'cqu8Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 687 ])

cqu8Im1331 = Parameter(name = 'cqu8Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 688 ])

cqu8Im1321 = Parameter(name = 'cqu8Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 689 ])

cqu8Im1322 = Parameter(name = 'cqu8Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 690 ])

cqu8Im1332 = Parameter(name = 'cqu8Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 691 ])

cqu8Im1323 = Parameter(name = 'cqu8Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 692 ])

cqu8Im1333 = Parameter(name = 'cqu8Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 693 ])

cqu8Im2212 = Parameter(name = 'cqu8Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 694 ])

cqu8Im2213 = Parameter(name = 'cqu8Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 695 ])

cqu8Im2223 = Parameter(name = 'cqu8Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 696 ])

cqu8Im2311 = Parameter(name = 'cqu8Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 697 ])

cqu8Im2312 = Parameter(name = 'cqu8Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 698 ])

cqu8Im2313 = Parameter(name = 'cqu8Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 699 ])

cqu8Im2321 = Parameter(name = 'cqu8Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 700 ])

cqu8Im2322 = Parameter(name = 'cqu8Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 701 ])

cqu8Im2323 = Parameter(name = 'cqu8Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 702 ])

cqu8Im2331 = Parameter(name = 'cqu8Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 703 ])

cqu8Im2332 = Parameter(name = 'cqu8Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 704 ])

cqu8Im2333 = Parameter(name = 'cqu8Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 705 ])

cqu8Im3312 = Parameter(name = 'cqu8Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 706 ])

cqu8Im3313 = Parameter(name = 'cqu8Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 707 ])

cqu8Im3323 = Parameter(name = 'cqu8Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqu8Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 708 ])

cqd8Im1112 = Parameter(name = 'cqd8Im1112',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1112}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 709 ])

cqd8Im1113 = Parameter(name = 'cqd8Im1113',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1113}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 710 ])

cqd8Im1123 = Parameter(name = 'cqd8Im1123',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1123}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 711 ])

cqd8Im1211 = Parameter(name = 'cqd8Im1211',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1211}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 712 ])

cqd8Im1212 = Parameter(name = 'cqd8Im1212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 713 ])

cqd8Im1221 = Parameter(name = 'cqd8Im1221',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1221}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 714 ])

cqd8Im1213 = Parameter(name = 'cqd8Im1213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 715 ])

cqd8Im1231 = Parameter(name = 'cqd8Im1231',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1231}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 716 ])

cqd8Im1222 = Parameter(name = 'cqd8Im1222',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1222}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 717 ])

cqd8Im1223 = Parameter(name = 'cqd8Im1223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 718 ])

cqd8Im1232 = Parameter(name = 'cqd8Im1232',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1232}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 719 ])

cqd8Im1233 = Parameter(name = 'cqd8Im1233',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1233}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 720 ])

cqd8Im1311 = Parameter(name = 'cqd8Im1311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 721 ])

cqd8Im1312 = Parameter(name = 'cqd8Im1312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 722 ])

cqd8Im1313 = Parameter(name = 'cqd8Im1313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 723 ])

cqd8Im1331 = Parameter(name = 'cqd8Im1331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 724 ])

cqd8Im1321 = Parameter(name = 'cqd8Im1321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 725 ])

cqd8Im1322 = Parameter(name = 'cqd8Im1322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 726 ])

cqd8Im1332 = Parameter(name = 'cqd8Im1332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 727 ])

cqd8Im1323 = Parameter(name = 'cqd8Im1323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 728 ])

cqd8Im1333 = Parameter(name = 'cqd8Im1333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im1333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 729 ])

cqd8Im2212 = Parameter(name = 'cqd8Im2212',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2212}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 730 ])

cqd8Im2213 = Parameter(name = 'cqd8Im2213',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2213}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 731 ])

cqd8Im2223 = Parameter(name = 'cqd8Im2223',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2223}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 732 ])

cqd8Im2311 = Parameter(name = 'cqd8Im2311',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2311}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 733 ])

cqd8Im2312 = Parameter(name = 'cqd8Im2312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 734 ])

cqd8Im2313 = Parameter(name = 'cqd8Im2313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 735 ])

cqd8Im2321 = Parameter(name = 'cqd8Im2321',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2321}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 736 ])

cqd8Im2322 = Parameter(name = 'cqd8Im2322',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2322}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 737 ])

cqd8Im2323 = Parameter(name = 'cqd8Im2323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 738 ])

cqd8Im2331 = Parameter(name = 'cqd8Im2331',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2331}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 739 ])

cqd8Im2332 = Parameter(name = 'cqd8Im2332',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2332}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 740 ])

cqd8Im2333 = Parameter(name = 'cqd8Im2333',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im2333}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 741 ])

cqd8Im3312 = Parameter(name = 'cqd8Im3312',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im3312}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 742 ])

cqd8Im3313 = Parameter(name = 'cqd8Im3313',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im3313}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 743 ])

cqd8Im3323 = Parameter(name = 'cqd8Im3323',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cqd8Im3323}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 744 ])

cledqIm1111 = Parameter(name = 'cledqIm1111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1111}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 745 ])

cledqIm1211 = Parameter(name = 'cledqIm1211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1211}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 746 ])

cledqIm1311 = Parameter(name = 'cledqIm1311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1311}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 747 ])

cledqIm1112 = Parameter(name = 'cledqIm1112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1112}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 748 ])

cledqIm1212 = Parameter(name = 'cledqIm1212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1212}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 749 ])

cledqIm1312 = Parameter(name = 'cledqIm1312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1312}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 750 ])

cledqIm1113 = Parameter(name = 'cledqIm1113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1113}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 751 ])

cledqIm1213 = Parameter(name = 'cledqIm1213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1213}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 752 ])

cledqIm1313 = Parameter(name = 'cledqIm1313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1313}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 753 ])

cledqIm1121 = Parameter(name = 'cledqIm1121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1121}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 754 ])

cledqIm1221 = Parameter(name = 'cledqIm1221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1221}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 755 ])

cledqIm1321 = Parameter(name = 'cledqIm1321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1321}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 756 ])

cledqIm1122 = Parameter(name = 'cledqIm1122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1122}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 757 ])

cledqIm1222 = Parameter(name = 'cledqIm1222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1222}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 758 ])

cledqIm1322 = Parameter(name = 'cledqIm1322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1322}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 759 ])

cledqIm1123 = Parameter(name = 'cledqIm1123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1123}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 760 ])

cledqIm1223 = Parameter(name = 'cledqIm1223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1223}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 761 ])

cledqIm1323 = Parameter(name = 'cledqIm1323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1323}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 762 ])

cledqIm1131 = Parameter(name = 'cledqIm1131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1131}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 763 ])

cledqIm1231 = Parameter(name = 'cledqIm1231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1231}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 764 ])

cledqIm1331 = Parameter(name = 'cledqIm1331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1331}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 765 ])

cledqIm1132 = Parameter(name = 'cledqIm1132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1132}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 766 ])

cledqIm1232 = Parameter(name = 'cledqIm1232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1232}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 767 ])

cledqIm1332 = Parameter(name = 'cledqIm1332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1332}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 768 ])

cledqIm1133 = Parameter(name = 'cledqIm1133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1133}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 769 ])

cledqIm1233 = Parameter(name = 'cledqIm1233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1233}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 770 ])

cledqIm1333 = Parameter(name = 'cledqIm1333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm1333}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 771 ])

cledqIm2211 = Parameter(name = 'cledqIm2211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2211}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 772 ])

cledqIm2111 = Parameter(name = 'cledqIm2111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2111}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 773 ])

cledqIm2311 = Parameter(name = 'cledqIm2311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2311}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 774 ])

cledqIm2212 = Parameter(name = 'cledqIm2212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2212}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 775 ])

cledqIm2112 = Parameter(name = 'cledqIm2112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2112}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 776 ])

cledqIm2312 = Parameter(name = 'cledqIm2312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2312}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 777 ])

cledqIm2213 = Parameter(name = 'cledqIm2213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2213}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 778 ])

cledqIm2113 = Parameter(name = 'cledqIm2113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2113}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 779 ])

cledqIm2313 = Parameter(name = 'cledqIm2313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2313}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 780 ])

cledqIm2221 = Parameter(name = 'cledqIm2221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2221}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 781 ])

cledqIm2121 = Parameter(name = 'cledqIm2121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2121}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 782 ])

cledqIm2321 = Parameter(name = 'cledqIm2321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2321}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 783 ])

cledqIm2222 = Parameter(name = 'cledqIm2222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2222}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 784 ])

cledqIm2122 = Parameter(name = 'cledqIm2122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2122}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 785 ])

cledqIm2322 = Parameter(name = 'cledqIm2322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2322}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 786 ])

cledqIm2223 = Parameter(name = 'cledqIm2223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2223}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 787 ])

cledqIm2123 = Parameter(name = 'cledqIm2123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2123}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 788 ])

cledqIm2323 = Parameter(name = 'cledqIm2323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2323}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 789 ])

cledqIm2231 = Parameter(name = 'cledqIm2231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2231}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 790 ])

cledqIm2131 = Parameter(name = 'cledqIm2131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2131}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 791 ])

cledqIm2331 = Parameter(name = 'cledqIm2331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2331}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 792 ])

cledqIm2232 = Parameter(name = 'cledqIm2232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2232}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 793 ])

cledqIm2132 = Parameter(name = 'cledqIm2132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2132}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 794 ])

cledqIm2332 = Parameter(name = 'cledqIm2332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2332}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 795 ])

cledqIm2233 = Parameter(name = 'cledqIm2233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2233}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 796 ])

cledqIm2133 = Parameter(name = 'cledqIm2133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2133}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 797 ])

cledqIm2333 = Parameter(name = 'cledqIm2333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm2333}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 798 ])

cledqIm3311 = Parameter(name = 'cledqIm3311',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3311}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 799 ])

cledqIm3111 = Parameter(name = 'cledqIm3111',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3111}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 800 ])

cledqIm3211 = Parameter(name = 'cledqIm3211',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3211}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 801 ])

cledqIm3312 = Parameter(name = 'cledqIm3312',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3312}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 802 ])

cledqIm3112 = Parameter(name = 'cledqIm3112',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3112}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 803 ])

cledqIm3212 = Parameter(name = 'cledqIm3212',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3212}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 804 ])

cledqIm3313 = Parameter(name = 'cledqIm3313',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3313}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 805 ])

cledqIm3113 = Parameter(name = 'cledqIm3113',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3113}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 806 ])

cledqIm3213 = Parameter(name = 'cledqIm3213',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3213}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 807 ])

cledqIm3321 = Parameter(name = 'cledqIm3321',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3321}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 808 ])

cledqIm3121 = Parameter(name = 'cledqIm3121',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3121}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 809 ])

cledqIm3221 = Parameter(name = 'cledqIm3221',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3221}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 810 ])

cledqIm3322 = Parameter(name = 'cledqIm3322',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3322}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 811 ])

cledqIm3122 = Parameter(name = 'cledqIm3122',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3122}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 812 ])

cledqIm3222 = Parameter(name = 'cledqIm3222',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3222}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 813 ])

cledqIm3323 = Parameter(name = 'cledqIm3323',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3323}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 814 ])

cledqIm3123 = Parameter(name = 'cledqIm3123',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3123}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 815 ])

cledqIm3223 = Parameter(name = 'cledqIm3223',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3223}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 816 ])

cledqIm3331 = Parameter(name = 'cledqIm3331',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3331}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 817 ])

cledqIm3131 = Parameter(name = 'cledqIm3131',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3131}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 818 ])

cledqIm3231 = Parameter(name = 'cledqIm3231',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3231}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 819 ])

cledqIm3332 = Parameter(name = 'cledqIm3332',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3332}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 820 ])

cledqIm3132 = Parameter(name = 'cledqIm3132',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3132}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 821 ])

cledqIm3232 = Parameter(name = 'cledqIm3232',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3232}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 822 ])

cledqIm3333 = Parameter(name = 'cledqIm3333',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3333}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 823 ])

cledqIm3133 = Parameter(name = 'cledqIm3133',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3133}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 824 ])

cledqIm3233 = Parameter(name = 'cledqIm3233',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{cledqIm3233}',
                        lhablock = 'SMEFTcpv',
                        lhacode = [ 825 ])

cquqd1Im1111 = Parameter(name = 'cquqd1Im1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 826 ])

cquqd1Im1211 = Parameter(name = 'cquqd1Im1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 827 ])

cquqd1Im1311 = Parameter(name = 'cquqd1Im1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 828 ])

cquqd1Im1112 = Parameter(name = 'cquqd1Im1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 829 ])

cquqd1Im1212 = Parameter(name = 'cquqd1Im1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 830 ])

cquqd1Im1312 = Parameter(name = 'cquqd1Im1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 831 ])

cquqd1Im1113 = Parameter(name = 'cquqd1Im1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 832 ])

cquqd1Im1213 = Parameter(name = 'cquqd1Im1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 833 ])

cquqd1Im1313 = Parameter(name = 'cquqd1Im1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 834 ])

cquqd1Im1121 = Parameter(name = 'cquqd1Im1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 835 ])

cquqd1Im1221 = Parameter(name = 'cquqd1Im1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 836 ])

cquqd1Im1321 = Parameter(name = 'cquqd1Im1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 837 ])

cquqd1Im1122 = Parameter(name = 'cquqd1Im1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 838 ])

cquqd1Im1222 = Parameter(name = 'cquqd1Im1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 839 ])

cquqd1Im1322 = Parameter(name = 'cquqd1Im1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 840 ])

cquqd1Im1123 = Parameter(name = 'cquqd1Im1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 841 ])

cquqd1Im1223 = Parameter(name = 'cquqd1Im1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 842 ])

cquqd1Im1323 = Parameter(name = 'cquqd1Im1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 843 ])

cquqd1Im1131 = Parameter(name = 'cquqd1Im1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 844 ])

cquqd1Im1231 = Parameter(name = 'cquqd1Im1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 845 ])

cquqd1Im1331 = Parameter(name = 'cquqd1Im1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 846 ])

cquqd1Im1132 = Parameter(name = 'cquqd1Im1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 847 ])

cquqd1Im1232 = Parameter(name = 'cquqd1Im1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 848 ])

cquqd1Im1332 = Parameter(name = 'cquqd1Im1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 849 ])

cquqd1Im1133 = Parameter(name = 'cquqd1Im1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 850 ])

cquqd1Im1233 = Parameter(name = 'cquqd1Im1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 851 ])

cquqd1Im1333 = Parameter(name = 'cquqd1Im1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im1333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 852 ])

cquqd1Im2211 = Parameter(name = 'cquqd1Im2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 853 ])

cquqd1Im2111 = Parameter(name = 'cquqd1Im2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 854 ])

cquqd1Im2311 = Parameter(name = 'cquqd1Im2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 855 ])

cquqd1Im2212 = Parameter(name = 'cquqd1Im2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 856 ])

cquqd1Im2112 = Parameter(name = 'cquqd1Im2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 857 ])

cquqd1Im2312 = Parameter(name = 'cquqd1Im2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 858 ])

cquqd1Im2213 = Parameter(name = 'cquqd1Im2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 859 ])

cquqd1Im2113 = Parameter(name = 'cquqd1Im2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 860 ])

cquqd1Im2313 = Parameter(name = 'cquqd1Im2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 861 ])

cquqd1Im2221 = Parameter(name = 'cquqd1Im2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 862 ])

cquqd1Im2121 = Parameter(name = 'cquqd1Im2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 863 ])

cquqd1Im2321 = Parameter(name = 'cquqd1Im2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 864 ])

cquqd1Im2222 = Parameter(name = 'cquqd1Im2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 865 ])

cquqd1Im2122 = Parameter(name = 'cquqd1Im2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 866 ])

cquqd1Im2322 = Parameter(name = 'cquqd1Im2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 867 ])

cquqd1Im2223 = Parameter(name = 'cquqd1Im2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 868 ])

cquqd1Im2123 = Parameter(name = 'cquqd1Im2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 869 ])

cquqd1Im2323 = Parameter(name = 'cquqd1Im2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 870 ])

cquqd1Im2231 = Parameter(name = 'cquqd1Im2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 871 ])

cquqd1Im2131 = Parameter(name = 'cquqd1Im2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 872 ])

cquqd1Im2331 = Parameter(name = 'cquqd1Im2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 873 ])

cquqd1Im2232 = Parameter(name = 'cquqd1Im2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 874 ])

cquqd1Im2132 = Parameter(name = 'cquqd1Im2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 875 ])

cquqd1Im2332 = Parameter(name = 'cquqd1Im2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 876 ])

cquqd1Im2233 = Parameter(name = 'cquqd1Im2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 877 ])

cquqd1Im2133 = Parameter(name = 'cquqd1Im2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 878 ])

cquqd1Im2333 = Parameter(name = 'cquqd1Im2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im2333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 879 ])

cquqd1Im3311 = Parameter(name = 'cquqd1Im3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 880 ])

cquqd1Im3111 = Parameter(name = 'cquqd1Im3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 881 ])

cquqd1Im3211 = Parameter(name = 'cquqd1Im3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 882 ])

cquqd1Im3312 = Parameter(name = 'cquqd1Im3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 883 ])

cquqd1Im3112 = Parameter(name = 'cquqd1Im3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 884 ])

cquqd1Im3212 = Parameter(name = 'cquqd1Im3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 885 ])

cquqd1Im3313 = Parameter(name = 'cquqd1Im3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 886 ])

cquqd1Im3113 = Parameter(name = 'cquqd1Im3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 887 ])

cquqd1Im3213 = Parameter(name = 'cquqd1Im3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 888 ])

cquqd1Im3321 = Parameter(name = 'cquqd1Im3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 889 ])

cquqd1Im3121 = Parameter(name = 'cquqd1Im3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 890 ])

cquqd1Im3221 = Parameter(name = 'cquqd1Im3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 891 ])

cquqd1Im3322 = Parameter(name = 'cquqd1Im3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 892 ])

cquqd1Im3122 = Parameter(name = 'cquqd1Im3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 893 ])

cquqd1Im3222 = Parameter(name = 'cquqd1Im3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 894 ])

cquqd1Im3323 = Parameter(name = 'cquqd1Im3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 895 ])

cquqd1Im3123 = Parameter(name = 'cquqd1Im3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 896 ])

cquqd1Im3223 = Parameter(name = 'cquqd1Im3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 897 ])

cquqd1Im3331 = Parameter(name = 'cquqd1Im3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 898 ])

cquqd1Im3131 = Parameter(name = 'cquqd1Im3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 899 ])

cquqd1Im3231 = Parameter(name = 'cquqd1Im3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 900 ])

cquqd1Im3332 = Parameter(name = 'cquqd1Im3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 901 ])

cquqd1Im3132 = Parameter(name = 'cquqd1Im3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 902 ])

cquqd1Im3232 = Parameter(name = 'cquqd1Im3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 903 ])

cquqd1Im3333 = Parameter(name = 'cquqd1Im3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 904 ])

cquqd1Im3133 = Parameter(name = 'cquqd1Im3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 905 ])

cquqd1Im3233 = Parameter(name = 'cquqd1Im3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd1Im3233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 906 ])

cquqd8Im1111 = Parameter(name = 'cquqd8Im1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 907 ])

cquqd8Im1211 = Parameter(name = 'cquqd8Im1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 908 ])

cquqd8Im1311 = Parameter(name = 'cquqd8Im1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 909 ])

cquqd8Im1112 = Parameter(name = 'cquqd8Im1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 910 ])

cquqd8Im1212 = Parameter(name = 'cquqd8Im1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 911 ])

cquqd8Im1312 = Parameter(name = 'cquqd8Im1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 912 ])

cquqd8Im1113 = Parameter(name = 'cquqd8Im1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 913 ])

cquqd8Im1213 = Parameter(name = 'cquqd8Im1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 914 ])

cquqd8Im1313 = Parameter(name = 'cquqd8Im1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 915 ])

cquqd8Im1121 = Parameter(name = 'cquqd8Im1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 916 ])

cquqd8Im1221 = Parameter(name = 'cquqd8Im1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 917 ])

cquqd8Im1321 = Parameter(name = 'cquqd8Im1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 918 ])

cquqd8Im1122 = Parameter(name = 'cquqd8Im1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 919 ])

cquqd8Im1222 = Parameter(name = 'cquqd8Im1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 920 ])

cquqd8Im1322 = Parameter(name = 'cquqd8Im1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 921 ])

cquqd8Im1123 = Parameter(name = 'cquqd8Im1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 922 ])

cquqd8Im1223 = Parameter(name = 'cquqd8Im1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 923 ])

cquqd8Im1323 = Parameter(name = 'cquqd8Im1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 924 ])

cquqd8Im1131 = Parameter(name = 'cquqd8Im1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 925 ])

cquqd8Im1231 = Parameter(name = 'cquqd8Im1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 926 ])

cquqd8Im1331 = Parameter(name = 'cquqd8Im1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 927 ])

cquqd8Im1132 = Parameter(name = 'cquqd8Im1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 928 ])

cquqd8Im1232 = Parameter(name = 'cquqd8Im1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 929 ])

cquqd8Im1332 = Parameter(name = 'cquqd8Im1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 930 ])

cquqd8Im1133 = Parameter(name = 'cquqd8Im1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 931 ])

cquqd8Im1233 = Parameter(name = 'cquqd8Im1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 932 ])

cquqd8Im1333 = Parameter(name = 'cquqd8Im1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im1333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 933 ])

cquqd8Im2211 = Parameter(name = 'cquqd8Im2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 934 ])

cquqd8Im2111 = Parameter(name = 'cquqd8Im2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 935 ])

cquqd8Im2311 = Parameter(name = 'cquqd8Im2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 936 ])

cquqd8Im2212 = Parameter(name = 'cquqd8Im2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 937 ])

cquqd8Im2112 = Parameter(name = 'cquqd8Im2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 938 ])

cquqd8Im2312 = Parameter(name = 'cquqd8Im2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 939 ])

cquqd8Im2213 = Parameter(name = 'cquqd8Im2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 940 ])

cquqd8Im2113 = Parameter(name = 'cquqd8Im2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 941 ])

cquqd8Im2313 = Parameter(name = 'cquqd8Im2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 942 ])

cquqd8Im2221 = Parameter(name = 'cquqd8Im2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 943 ])

cquqd8Im2121 = Parameter(name = 'cquqd8Im2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 944 ])

cquqd8Im2321 = Parameter(name = 'cquqd8Im2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 945 ])

cquqd8Im2222 = Parameter(name = 'cquqd8Im2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 946 ])

cquqd8Im2122 = Parameter(name = 'cquqd8Im2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 947 ])

cquqd8Im2322 = Parameter(name = 'cquqd8Im2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 948 ])

cquqd8Im2223 = Parameter(name = 'cquqd8Im2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 949 ])

cquqd8Im2123 = Parameter(name = 'cquqd8Im2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 950 ])

cquqd8Im2323 = Parameter(name = 'cquqd8Im2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 951 ])

cquqd8Im2231 = Parameter(name = 'cquqd8Im2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 952 ])

cquqd8Im2131 = Parameter(name = 'cquqd8Im2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 953 ])

cquqd8Im2331 = Parameter(name = 'cquqd8Im2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 954 ])

cquqd8Im2232 = Parameter(name = 'cquqd8Im2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 955 ])

cquqd8Im2132 = Parameter(name = 'cquqd8Im2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 956 ])

cquqd8Im2332 = Parameter(name = 'cquqd8Im2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 957 ])

cquqd8Im2233 = Parameter(name = 'cquqd8Im2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 958 ])

cquqd8Im2133 = Parameter(name = 'cquqd8Im2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 959 ])

cquqd8Im2333 = Parameter(name = 'cquqd8Im2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im2333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 960 ])

cquqd8Im3311 = Parameter(name = 'cquqd8Im3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 961 ])

cquqd8Im3111 = Parameter(name = 'cquqd8Im3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 962 ])

cquqd8Im3211 = Parameter(name = 'cquqd8Im3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 963 ])

cquqd8Im3312 = Parameter(name = 'cquqd8Im3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 964 ])

cquqd8Im3112 = Parameter(name = 'cquqd8Im3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 965 ])

cquqd8Im3212 = Parameter(name = 'cquqd8Im3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 966 ])

cquqd8Im3313 = Parameter(name = 'cquqd8Im3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 967 ])

cquqd8Im3113 = Parameter(name = 'cquqd8Im3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 968 ])

cquqd8Im3213 = Parameter(name = 'cquqd8Im3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 969 ])

cquqd8Im3321 = Parameter(name = 'cquqd8Im3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 970 ])

cquqd8Im3121 = Parameter(name = 'cquqd8Im3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 971 ])

cquqd8Im3221 = Parameter(name = 'cquqd8Im3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 972 ])

cquqd8Im3322 = Parameter(name = 'cquqd8Im3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 973 ])

cquqd8Im3122 = Parameter(name = 'cquqd8Im3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 974 ])

cquqd8Im3222 = Parameter(name = 'cquqd8Im3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 975 ])

cquqd8Im3323 = Parameter(name = 'cquqd8Im3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 976 ])

cquqd8Im3123 = Parameter(name = 'cquqd8Im3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 977 ])

cquqd8Im3223 = Parameter(name = 'cquqd8Im3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 978 ])

cquqd8Im3331 = Parameter(name = 'cquqd8Im3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 979 ])

cquqd8Im3131 = Parameter(name = 'cquqd8Im3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 980 ])

cquqd8Im3231 = Parameter(name = 'cquqd8Im3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 981 ])

cquqd8Im3332 = Parameter(name = 'cquqd8Im3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 982 ])

cquqd8Im3132 = Parameter(name = 'cquqd8Im3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 983 ])

cquqd8Im3232 = Parameter(name = 'cquqd8Im3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 984 ])

cquqd8Im3333 = Parameter(name = 'cquqd8Im3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 985 ])

cquqd8Im3133 = Parameter(name = 'cquqd8Im3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 986 ])

cquqd8Im3233 = Parameter(name = 'cquqd8Im3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{cquqd8Im3233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 987 ])

clequ1Im1111 = Parameter(name = 'clequ1Im1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 988 ])

clequ1Im1211 = Parameter(name = 'clequ1Im1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 989 ])

clequ1Im1311 = Parameter(name = 'clequ1Im1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 990 ])

clequ1Im1112 = Parameter(name = 'clequ1Im1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 991 ])

clequ1Im1212 = Parameter(name = 'clequ1Im1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 992 ])

clequ1Im1312 = Parameter(name = 'clequ1Im1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 993 ])

clequ1Im1113 = Parameter(name = 'clequ1Im1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 994 ])

clequ1Im1213 = Parameter(name = 'clequ1Im1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 995 ])

clequ1Im1313 = Parameter(name = 'clequ1Im1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 996 ])

clequ1Im1121 = Parameter(name = 'clequ1Im1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 997 ])

clequ1Im1221 = Parameter(name = 'clequ1Im1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 998 ])

clequ1Im1321 = Parameter(name = 'clequ1Im1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 999 ])

clequ1Im1122 = Parameter(name = 'clequ1Im1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1000 ])

clequ1Im1222 = Parameter(name = 'clequ1Im1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1001 ])

clequ1Im1322 = Parameter(name = 'clequ1Im1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1002 ])

clequ1Im1123 = Parameter(name = 'clequ1Im1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1003 ])

clequ1Im1223 = Parameter(name = 'clequ1Im1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1004 ])

clequ1Im1323 = Parameter(name = 'clequ1Im1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1005 ])

clequ1Im1131 = Parameter(name = 'clequ1Im1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1006 ])

clequ1Im1231 = Parameter(name = 'clequ1Im1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1007 ])

clequ1Im1331 = Parameter(name = 'clequ1Im1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1008 ])

clequ1Im1132 = Parameter(name = 'clequ1Im1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1009 ])

clequ1Im1232 = Parameter(name = 'clequ1Im1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1010 ])

clequ1Im1332 = Parameter(name = 'clequ1Im1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1011 ])

clequ1Im1133 = Parameter(name = 'clequ1Im1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1012 ])

clequ1Im1233 = Parameter(name = 'clequ1Im1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1013 ])

clequ1Im1333 = Parameter(name = 'clequ1Im1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im1333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1014 ])

clequ1Im2211 = Parameter(name = 'clequ1Im2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1015 ])

clequ1Im2111 = Parameter(name = 'clequ1Im2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1016 ])

clequ1Im2311 = Parameter(name = 'clequ1Im2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1017 ])

clequ1Im2212 = Parameter(name = 'clequ1Im2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1018 ])

clequ1Im2112 = Parameter(name = 'clequ1Im2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1019 ])

clequ1Im2312 = Parameter(name = 'clequ1Im2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1020 ])

clequ1Im2213 = Parameter(name = 'clequ1Im2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1021 ])

clequ1Im2113 = Parameter(name = 'clequ1Im2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1022 ])

clequ1Im2313 = Parameter(name = 'clequ1Im2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1023 ])

clequ1Im2221 = Parameter(name = 'clequ1Im2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1024 ])

clequ1Im2121 = Parameter(name = 'clequ1Im2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1025 ])

clequ1Im2321 = Parameter(name = 'clequ1Im2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1026 ])

clequ1Im2222 = Parameter(name = 'clequ1Im2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1027 ])

clequ1Im2122 = Parameter(name = 'clequ1Im2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1028 ])

clequ1Im2322 = Parameter(name = 'clequ1Im2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1029 ])

clequ1Im2223 = Parameter(name = 'clequ1Im2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1030 ])

clequ1Im2123 = Parameter(name = 'clequ1Im2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1031 ])

clequ1Im2323 = Parameter(name = 'clequ1Im2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1032 ])

clequ1Im2231 = Parameter(name = 'clequ1Im2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1033 ])

clequ1Im2131 = Parameter(name = 'clequ1Im2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1034 ])

clequ1Im2331 = Parameter(name = 'clequ1Im2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1035 ])

clequ1Im2232 = Parameter(name = 'clequ1Im2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1036 ])

clequ1Im2132 = Parameter(name = 'clequ1Im2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1037 ])

clequ1Im2332 = Parameter(name = 'clequ1Im2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1038 ])

clequ1Im2233 = Parameter(name = 'clequ1Im2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1039 ])

clequ1Im2133 = Parameter(name = 'clequ1Im2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1040 ])

clequ1Im2333 = Parameter(name = 'clequ1Im2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im2333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1041 ])

clequ1Im3311 = Parameter(name = 'clequ1Im3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1042 ])

clequ1Im3111 = Parameter(name = 'clequ1Im3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1043 ])

clequ1Im3211 = Parameter(name = 'clequ1Im3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1044 ])

clequ1Im3312 = Parameter(name = 'clequ1Im3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1045 ])

clequ1Im3112 = Parameter(name = 'clequ1Im3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1046 ])

clequ1Im3212 = Parameter(name = 'clequ1Im3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1047 ])

clequ1Im3313 = Parameter(name = 'clequ1Im3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1048 ])

clequ1Im3113 = Parameter(name = 'clequ1Im3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1049 ])

clequ1Im3213 = Parameter(name = 'clequ1Im3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1050 ])

clequ1Im3321 = Parameter(name = 'clequ1Im3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1051 ])

clequ1Im3121 = Parameter(name = 'clequ1Im3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1052 ])

clequ1Im3221 = Parameter(name = 'clequ1Im3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1053 ])

clequ1Im3322 = Parameter(name = 'clequ1Im3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1054 ])

clequ1Im3122 = Parameter(name = 'clequ1Im3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1055 ])

clequ1Im3222 = Parameter(name = 'clequ1Im3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1056 ])

clequ1Im3323 = Parameter(name = 'clequ1Im3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1057 ])

clequ1Im3123 = Parameter(name = 'clequ1Im3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1058 ])

clequ1Im3223 = Parameter(name = 'clequ1Im3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1059 ])

clequ1Im3331 = Parameter(name = 'clequ1Im3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1060 ])

clequ1Im3131 = Parameter(name = 'clequ1Im3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1061 ])

clequ1Im3231 = Parameter(name = 'clequ1Im3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1062 ])

clequ1Im3332 = Parameter(name = 'clequ1Im3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1063 ])

clequ1Im3132 = Parameter(name = 'clequ1Im3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1064 ])

clequ1Im3232 = Parameter(name = 'clequ1Im3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1065 ])

clequ1Im3333 = Parameter(name = 'clequ1Im3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1066 ])

clequ1Im3133 = Parameter(name = 'clequ1Im3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1067 ])

clequ1Im3233 = Parameter(name = 'clequ1Im3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ1Im3233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1068 ])

clequ3Im1111 = Parameter(name = 'clequ3Im1111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1069 ])

clequ3Im1211 = Parameter(name = 'clequ3Im1211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1070 ])

clequ3Im1311 = Parameter(name = 'clequ3Im1311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1071 ])

clequ3Im1112 = Parameter(name = 'clequ3Im1112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1072 ])

clequ3Im1212 = Parameter(name = 'clequ3Im1212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1073 ])

clequ3Im1312 = Parameter(name = 'clequ3Im1312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1074 ])

clequ3Im1113 = Parameter(name = 'clequ3Im1113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1075 ])

clequ3Im1213 = Parameter(name = 'clequ3Im1213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1076 ])

clequ3Im1313 = Parameter(name = 'clequ3Im1313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1077 ])

clequ3Im1121 = Parameter(name = 'clequ3Im1121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1078 ])

clequ3Im1221 = Parameter(name = 'clequ3Im1221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1079 ])

clequ3Im1321 = Parameter(name = 'clequ3Im1321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1080 ])

clequ3Im1122 = Parameter(name = 'clequ3Im1122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1081 ])

clequ3Im1222 = Parameter(name = 'clequ3Im1222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1082 ])

clequ3Im1322 = Parameter(name = 'clequ3Im1322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1083 ])

clequ3Im1123 = Parameter(name = 'clequ3Im1123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1084 ])

clequ3Im1223 = Parameter(name = 'clequ3Im1223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1085 ])

clequ3Im1323 = Parameter(name = 'clequ3Im1323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1086 ])

clequ3Im1131 = Parameter(name = 'clequ3Im1131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1087 ])

clequ3Im1231 = Parameter(name = 'clequ3Im1231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1088 ])

clequ3Im1331 = Parameter(name = 'clequ3Im1331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1089 ])

clequ3Im1132 = Parameter(name = 'clequ3Im1132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1090 ])

clequ3Im1232 = Parameter(name = 'clequ3Im1232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1091 ])

clequ3Im1332 = Parameter(name = 'clequ3Im1332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1092 ])

clequ3Im1133 = Parameter(name = 'clequ3Im1133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1093 ])

clequ3Im1233 = Parameter(name = 'clequ3Im1233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1094 ])

clequ3Im1333 = Parameter(name = 'clequ3Im1333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im1333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1095 ])

clequ3Im2211 = Parameter(name = 'clequ3Im2211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1096 ])

clequ3Im2111 = Parameter(name = 'clequ3Im2111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1097 ])

clequ3Im2311 = Parameter(name = 'clequ3Im2311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1098 ])

clequ3Im2212 = Parameter(name = 'clequ3Im2212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1099 ])

clequ3Im2112 = Parameter(name = 'clequ3Im2112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1100 ])

clequ3Im2312 = Parameter(name = 'clequ3Im2312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1101 ])

clequ3Im2213 = Parameter(name = 'clequ3Im2213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1102 ])

clequ3Im2113 = Parameter(name = 'clequ3Im2113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1103 ])

clequ3Im2313 = Parameter(name = 'clequ3Im2313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1104 ])

clequ3Im2221 = Parameter(name = 'clequ3Im2221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1105 ])

clequ3Im2121 = Parameter(name = 'clequ3Im2121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1106 ])

clequ3Im2321 = Parameter(name = 'clequ3Im2321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1107 ])

clequ3Im2222 = Parameter(name = 'clequ3Im2222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1108 ])

clequ3Im2122 = Parameter(name = 'clequ3Im2122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1109 ])

clequ3Im2322 = Parameter(name = 'clequ3Im2322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1110 ])

clequ3Im2223 = Parameter(name = 'clequ3Im2223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1111 ])

clequ3Im2123 = Parameter(name = 'clequ3Im2123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1112 ])

clequ3Im2323 = Parameter(name = 'clequ3Im2323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1113 ])

clequ3Im2231 = Parameter(name = 'clequ3Im2231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1114 ])

clequ3Im2131 = Parameter(name = 'clequ3Im2131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1115 ])

clequ3Im2331 = Parameter(name = 'clequ3Im2331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1116 ])

clequ3Im2232 = Parameter(name = 'clequ3Im2232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1117 ])

clequ3Im2132 = Parameter(name = 'clequ3Im2132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1118 ])

clequ3Im2332 = Parameter(name = 'clequ3Im2332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1119 ])

clequ3Im2233 = Parameter(name = 'clequ3Im2233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1120 ])

clequ3Im2133 = Parameter(name = 'clequ3Im2133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1121 ])

clequ3Im2333 = Parameter(name = 'clequ3Im2333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im2333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1122 ])

clequ3Im3311 = Parameter(name = 'clequ3Im3311',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3311}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1123 ])

clequ3Im3111 = Parameter(name = 'clequ3Im3111',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3111}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1124 ])

clequ3Im3211 = Parameter(name = 'clequ3Im3211',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3211}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1125 ])

clequ3Im3312 = Parameter(name = 'clequ3Im3312',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3312}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1126 ])

clequ3Im3112 = Parameter(name = 'clequ3Im3112',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3112}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1127 ])

clequ3Im3212 = Parameter(name = 'clequ3Im3212',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3212}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1128 ])

clequ3Im3313 = Parameter(name = 'clequ3Im3313',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3313}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1129 ])

clequ3Im3113 = Parameter(name = 'clequ3Im3113',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3113}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1130 ])

clequ3Im3213 = Parameter(name = 'clequ3Im3213',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3213}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1131 ])

clequ3Im3321 = Parameter(name = 'clequ3Im3321',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3321}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1132 ])

clequ3Im3121 = Parameter(name = 'clequ3Im3121',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3121}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1133 ])

clequ3Im3221 = Parameter(name = 'clequ3Im3221',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3221}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1134 ])

clequ3Im3322 = Parameter(name = 'clequ3Im3322',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3322}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1135 ])

clequ3Im3122 = Parameter(name = 'clequ3Im3122',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3122}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1136 ])

clequ3Im3222 = Parameter(name = 'clequ3Im3222',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3222}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1137 ])

clequ3Im3323 = Parameter(name = 'clequ3Im3323',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3323}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1138 ])

clequ3Im3123 = Parameter(name = 'clequ3Im3123',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3123}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1139 ])

clequ3Im3223 = Parameter(name = 'clequ3Im3223',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3223}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1140 ])

clequ3Im3331 = Parameter(name = 'clequ3Im3331',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3331}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1141 ])

clequ3Im3131 = Parameter(name = 'clequ3Im3131',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3131}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1142 ])

clequ3Im3231 = Parameter(name = 'clequ3Im3231',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3231}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1143 ])

clequ3Im3332 = Parameter(name = 'clequ3Im3332',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3332}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1144 ])

clequ3Im3132 = Parameter(name = 'clequ3Im3132',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3132}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1145 ])

clequ3Im3232 = Parameter(name = 'clequ3Im3232',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3232}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1146 ])

clequ3Im3333 = Parameter(name = 'clequ3Im3333',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3333}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1147 ])

clequ3Im3133 = Parameter(name = 'clequ3Im3133',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3133}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1148 ])

clequ3Im3233 = Parameter(name = 'clequ3Im3233',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{clequ3Im3233}',
                         lhablock = 'SMEFTcpv',
                         lhacode = [ 1149 ])

LambdaSMEFT = Parameter(name = 'LambdaSMEFT',
                        nature = 'external',
                        type = 'real',
                        value = 1000,
                        texname = '\\Lambda',
                        lhablock = 'SMEFTcutoff',
                        lhacode = [ 1 ])

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
                value = '((cHl3Re11 + cHl3Re22 - cllRe1221)*vevhat**2)/LambdaSMEFT**2',
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

dgw = Parameter(name = 'dgw',
                nature = 'internal',
                type = 'real',
                value = '-dGf/2.',
                texname = '\\text{dgw}')

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

barlam = Parameter(name = 'barlam',
                   nature = 'internal',
                   type = 'real',
                   value = '(1 - dGf - dMH2)*lam',
                   texname = '\\text{barlam}')

dWT = Parameter(name = 'dWT',
                nature = 'internal',
                type = 'real',
                value = '(6*cHudRe33*MB*MT*MWsm**2*vevhat**2*WT)/(LambdaSMEFT**2*(MB**4 + MT**4 + MT**2*MWsm**2 - 2*MWsm**4 + MB**2*(-2*MT**2 + MWsm**2))) + 2*WT*(dgw + (vevhat*(cHq3Re33*vevhat + (6*MWsm**2*(cuWRe33*MT*(MB**2 - MT**2 + MWsm**2) + cdWRe33*MB*(-MB**2 + MT**2 + MWsm**2))*sth*cmath.sqrt(2))/(ee*((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4))))/LambdaSMEFT**2)',
                texname = '\\text{dWT}')

dWW = Parameter(name = 'dWW',
                nature = 'internal',
                type = 'real',
                value = '(2*dgw + (2*(cHl3Re11 + cHl3Re22 + cHl3Re33 + 3*cHq3Re11 + 3*cHq3Re22)*vevhat**2)/(9.*LambdaSMEFT**2))*WW',
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
                 value = 'yc/(yc + 10**-40)*(-0.02884*(dGf - 2.*dkH + (2.*cuHRe22*vevhat**2)/(LambdaSMEFT**2*(yc+10**-40))))',
                 texname='\\text{dWHc}')

dWHb = Parameter(name = 'dWHb',
                 nature = 'internal',
                 type = 'real',
                 value = 'yb/(yb + 10**-40)*(-0.5809*(dGf - 2.*dkH + (2.*cdHRe33*vevhat**2)/(LambdaSMEFT**2*(yb+10**-40))))',
                 texname='\\text{dWHb}')

dWHta = Parameter(name = 'dWHta',
                 nature = 'internal',
                 type = 'real',
                 value = 'ytau/(ytau + 10**-40)*(-0.06256*(dGf - 2.*dkH + (2.*ceHRe33*vevhat**2)/(LambdaSMEFT**2*(ytau+10**-40))))',
                 texname='\\text{dWHta}')

dWH = Parameter(name = 'dWH',
                nature = 'internal',
                type = 'real',
                value = 'WH*(-0.24161*dGf + 0.96644*dgw + 0.48322*dkH - 0.11186509426655465*dWW + (0.058694359028859104*cHl3Re11*vevhat**2)/LambdaSMEFT**2 + (0.058694359028859104*cHl3Re22*vevhat**2)/LambdaSMEFT**2 + (0.058694359028859104*cHl3Re33*vevhat**2)/LambdaSMEFT**2 + (0.18205189224619084*cHq3Re11*vevhat**2)/LambdaSMEFT**2 + (0.18205189224619084*cHq3Re22*vevhat**2)/LambdaSMEFT**2 + (0.1636*cHG*MT**2*vevhat**2)/(LambdaSMEFT**2*(-0.5*gHgg2*MH**2 + gHgg1*MT**2)) + (cHW*(-0.35937785117066967*gHaa*gHza + 0.006164*cth*gHaa*sth + 0.00454*gHza*sth**2)*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHWB*(-0.00454*cth*gHza*sth + gHaa*(-0.0030819999999999997 + 0.006163999999999999*sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHB*(-0.006163999999999999*cth*gHaa*sth - 0.00454*gHza*(-1. + sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + dWHc + dWHb + dWHta)',
                texname = '\\text{dWH}')

dWZ = Parameter(name = 'dWZ',
                nature = 'internal',
                type = 'real',
                value = 'WZ*(-1 + (36*cth*MB*MZ**2*sth*(cdWRe33*cth + cdBRe33*sth)*(-3 + 4*sth**2)*vevhat*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) + ee*LambdaSMEFT**2*(2*MZ**3*(27 + 54*dgw - 54*(1 + dg1 + dgw)*sth**2 + 76*(1 + 4*dg1 - 2*dgw)*sth**4 + 152*(-dg1 + dgw)*sth**6) + MZ**2*(9 + 18*dgw - 6*(2 + dg1 + 3*dgw)*sth**2 + 8*(1 + 4*dg1 - 2*dgw)*sth**4 + 16*(-dg1 + dgw)*sth**6)*cmath.sqrt(-4*MB**2 + MZ**2) + MB**2*(-9 - 18*dgw - 6*(4 + 11*dg1 - 3*dgw)*sth**2 + 16*(1 + 4*dg1 - 2*dgw)*sth**4 + 32*(-dg1 + dgw)*sth**6)*cmath.sqrt(-4*MB**2 + MZ**2)) + 2*ee*vevhat**2*(6*cHl3Re11*MZ**3 + 6*cHl3Re22*MZ**3 + 6*cHl3Re33*MZ**3 + 18*cHq3Re11*MZ**3 + 18*cHq3Re22*MZ**3 + 9*(3*cHdRe33 - cHq1Re33 - cHq3Re33)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + 9*cHq1Re33*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 9*cHq3Re33*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 3*cHWB*cth*(-7*MB**2 + MZ**2)*sth*cmath.sqrt(-4*MB**2 + MZ**2) + 8*cHWB*cth*sth**3*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) - 8*cHWB*cth*sth**5*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) + 6*sth**2*(-2*(cHdRe33 + cHq1Re33 + cHq3Re33)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(-((cHdRe11 + cHdRe22 + cHeRe11 + cHeRe22 + cHeRe33 + cHl1Re11 + cHl1Re22 + cHl1Re33 + cHl3Re11 + cHl3Re22 + cHl3Re33 - cHq1Re11 - cHq1Re22 + 3*cHq3Re11 + 3*cHq3Re22 - 2*(cHuRe11 + cHuRe22))*MZ) - (cHdRe33 + cHq1Re33 + cHq3Re33)*cmath.sqrt(-4*MB**2 + MZ**2)))))/(ee*LambdaSMEFT**2*(2*MZ**3*(27 - 54*sth**2 + 76*sth**4) + MZ**2*(9 - 12*sth**2 + 8*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2) + MB**2*(-9 - 24*sth**2 + 16*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2))))',
                texname = '\\text{dWZ}')

g1sh = Parameter(name = 'g1sh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dg1 - (cHB*vevhat**2)/LambdaSMEFT**2))/cth',
                 texname = 'g_1')

