# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Fri 8 Jan 2021 11:25:12


from .object_library import all_couplings, Coupling

from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(2*cbb*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbb':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(cbd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbd1':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(cbd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbd8':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(cbe11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbe':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '(cbe22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbe':1,'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(cbe33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbe':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(cbGIm/(LambdaSMEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPcbG':1,'NPcpv':1,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(cbGRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbG':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-3*cbHIm)/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbH':1,'NPcpv':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(3*cbHRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbH':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(cbj1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbj1':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cbj8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbj8':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cbl11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbl':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cbl22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbl':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(cbl33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbl':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cbu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbu1':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(cbu8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbu8':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(cbWIm/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = 'cbWIm/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cbWRe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbW':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(2*cdd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd1':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(2*cdd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd8':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ced11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPced':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ced22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPced':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ced33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPced':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(2*cee1111*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cee1122*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cee1133*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(2*cee2222*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cee2233*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(2*cee3333*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-3*ceHIm11)/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-3*ceHIm22)/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(-3*ceHIm33)/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(3*ceHRe11*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(3*ceHRe22*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(3*ceHRe33*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPceH':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(ceu11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceu':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ceu22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceu':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ceu33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceu':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(ceWIm11/LambdaSMEFT**2)',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = 'ceWIm11/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ceWIm22/LambdaSMEFT**2)',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = 'ceWIm22/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ceWIm33/LambdaSMEFT**2)',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = 'ceWIm33/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ceWRe11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ceWRe22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ceWRe33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceW':1,'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(-6*cG)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = 'cGtil/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(90*cH*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcH':1,'QED':3})

GC_62 = Coupling(name = 'GC_62',
                 value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHbox':1,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcHDD':1,'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHG':1,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(-2*cHGtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHW':1,'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '(4*cHWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cjd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjd1':1,'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cjd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjd8':1,'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cje11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcje':1,'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cje22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcje':1,'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cje33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcje':1,'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(2*cjj11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj11':1,'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(2*cjj18*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj18':1,'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-2*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(2*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(4*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(-2*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(2*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(4*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cju1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcju1':1,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cju8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcju8':1,'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cld11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcld':1,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(cld22*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcld':1,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cld33*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcld':1,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cle1111*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cle1122*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cle1133*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(cle1221*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle1':1,'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(cle1331*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle1':1,'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cle2211*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cle2222*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cle2233*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cle2332*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle1':1,'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '(cle3311*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(cle3322*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '(cle3333*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(clebQIm11/LambdaSMEFT**2)',
                 order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = 'clebQIm11/LambdaSMEFT**2',
                 order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(clebQIm22/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = 'clebQIm22/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(clebQIm33/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = 'clebQIm33/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(clebQRe11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(clebQRe22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(clebQRe33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(cleQt1Im11/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = 'cleQt1Im11/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(cleQt1Im22/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = 'cleQt1Im22/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-(cleQt1Im33/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = 'cleQt1Im33/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((cleQt1Re11*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '(cleQt1Re11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cleQt1Re22*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cleQt1Re22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((cleQt1Re33*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(cleQt1Re33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '-cleQt3Im11/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '-cleQt3Im11/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = 'cleQt3Im11/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = 'cleQt3Im11/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '-cleQt3Im22/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '-cleQt3Im22/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = 'cleQt3Im22/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = 'cleQt3Im22/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '-cleQt3Im33/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-cleQt3Im33/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = 'cleQt3Im33/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = 'cleQt3Im33/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '-(cleQt3Re11*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cleQt3Re11*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(cleQt3Re11*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '(cleQt3Re11*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(cleQt3Re22*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(cleQt3Re22*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(cleQt3Re22*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '(cleQt3Re22*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(cleQt3Re33*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '(cleQt3Re33*complex(0,1))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '-(cleQt3Re33*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cleQt3Re33*complex(0,1))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '(clj111*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj1':1,'QED':2})

GC_144 = Coupling(name = 'GC_144',
                  value = '(clj122*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj1':1,'QED':2})

GC_145 = Coupling(name = 'GC_145',
                  value = '(clj133*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj1':1,'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((clj311*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '(clj311*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_148 = Coupling(name = 'GC_148',
                  value = '(2*clj311*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((clj322*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(clj322*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '(2*clj322*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((clj333*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_153 = Coupling(name = 'GC_153',
                  value = '(clj333*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_154 = Coupling(name = 'GC_154',
                  value = '(2*clj333*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclj3':1,'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(2*cll1111*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(cll1122*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '(cll1133*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '(cll1221*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(cll1331*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(2*cll2222*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(cll2233*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(cll2332*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '(2*cll3333*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll':1,'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '(clu11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclu':1,'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '(clu22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclu':1,'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '(clu33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPclu':1,'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '(cQb1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQb1':1,'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '(cQb8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQb8':1,'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '(cQd1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQd1':1,'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cQd8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQd8':1,'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '(cQe11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQe':1,'QED':2})

GC_172 = Coupling(name = 'GC_172',
                  value = '(cQe22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQe':1,'QED':2})

GC_173 = Coupling(name = 'GC_173',
                  value = '(cQe33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQe':1,'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '(cQj11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj11':1,'QED':2})

GC_175 = Coupling(name = 'GC_175',
                  value = '(cQj18*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj18':1,'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((cQj31*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQj31':1,'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '(cQj31*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj31':1,'QED':2})

GC_178 = Coupling(name = 'GC_178',
                  value = '(2*cQj31*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj31':1,'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((cQj38*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQj38':1,'QED':2})

GC_180 = Coupling(name = 'GC_180',
                  value = '(cQj38*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj38':1,'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '(2*cQj38*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQj38':1,'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '(cQl111*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl1':1,'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(cQl122*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl1':1,'QED':2})

GC_184 = Coupling(name = 'GC_184',
                  value = '(cQl133*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl1':1,'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((cQl311*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(cQl311*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(2*cQl311*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((cQl322*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cQl322*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(2*cQl322*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((cQl333*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '(cQl333*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_193 = Coupling(name = 'GC_193',
                  value = '(2*cQl333*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQl3':1,'QED':2})

GC_194 = Coupling(name = 'GC_194',
                  value = '(2*cQQ1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQQ1':1,'QED':2})

GC_195 = Coupling(name = 'GC_195',
                  value = '(2*cQQ8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQQ8':1,'QED':2})

GC_196 = Coupling(name = 'GC_196',
                  value = '(cQt1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQt1':1,'QED':2})

GC_197 = Coupling(name = 'GC_197',
                  value = '(cQt8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQt8':1,'QED':2})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(cQtQb1Im/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtQb1':1,'QED':2})

GC_199 = Coupling(name = 'GC_199',
                  value = 'cQtQb1Im/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtQb1':1,'QED':2})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((cQtQb1Re*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtQb1':1,'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '(cQtQb1Re*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtQb1':1,'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(cQtQb8Im/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtQb8':1,'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = 'cQtQb8Im/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtQb8':1,'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((cQtQb8Re*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtQb8':1,'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '(cQtQb8Re*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtQb8':1,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(cQu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQu1':1,'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cQu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQu8':1,'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(ctb1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctb1':1,'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '(ctb8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctb8':1,'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ctd1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctd1':1,'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(ctd8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctd8':1,'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '(cte11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcte':1,'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '(cte22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcte':1,'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '(cte33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcte':1,'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(ctGIm/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '(ctGRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QED':2})

GC_217 = Coupling(name = 'GC_217',
                  value = '-((cbBIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(cbBRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'QED':2})

GC_219 = Coupling(name = 'GC_219',
                  value = '(cbWIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_220 = Coupling(name = 'GC_220',
                  value = '-((cbWRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((ceBIm11*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((ceBIm22*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((ceBIm33*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '(ceBRe11*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '(ceBRe22*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_226 = Coupling(name = 'GC_226',
                  value = '(ceBRe33*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_227 = Coupling(name = 'GC_227',
                  value = '(ceWIm11*cth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_228 = Coupling(name = 'GC_228',
                  value = '(ceWIm22*cth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_229 = Coupling(name = 'GC_229',
                  value = '(ceWIm33*cth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((ceWRe11*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((ceWRe22*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((ceWRe33*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((ctBIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':2})

GC_234 = Coupling(name = 'GC_234',
                  value = '(ctBRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctB':1,'QED':2})

GC_235 = Coupling(name = 'GC_235',
                  value = '(4*cHB*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_236 = Coupling(name = 'GC_236',
                  value = '(-2*cHBtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_237 = Coupling(name = 'GC_237',
                  value = '(4*cHW*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_238 = Coupling(name = 'GC_238',
                  value = '(-2*cHWtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_239 = Coupling(name = 'GC_239',
                  value = '(-3*ctHIm)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1,'QED':2})

GC_240 = Coupling(name = 'GC_240',
                  value = '(3*ctHRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1,'QED':2})

GC_241 = Coupling(name = 'GC_241',
                  value = '(ctj1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctj1':1,'QED':2})

GC_242 = Coupling(name = 'GC_242',
                  value = '(ctj8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctj8':1,'QED':2})

GC_243 = Coupling(name = 'GC_243',
                  value = '(ctl11*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctl':1,'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '(ctl22*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctl':1,'QED':2})

GC_245 = Coupling(name = 'GC_245',
                  value = '(ctl33*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctl':1,'QED':2})

GC_246 = Coupling(name = 'GC_246',
                  value = '(2*ctt*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctt':1,'QED':2})

GC_247 = Coupling(name = 'GC_247',
                  value = '(ctu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctu1':1,'QED':2})

GC_248 = Coupling(name = 'GC_248',
                  value = '(ctu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctu8':1,'QED':2})

GC_249 = Coupling(name = 'GC_249',
                  value = '-(ctWIm/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_250 = Coupling(name = 'GC_250',
                  value = 'ctWIm/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '-((cth*ctWIm)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(ctWRe*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(cth*ctWRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_254 = Coupling(name = 'GC_254',
                  value = '(cud1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcud1':1,'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '(cud8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcud8':1,'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(2*cuu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuu1':1,'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(2*cuu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuu8':1,'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(2*cth*cWtil*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(cbWIm*ee)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_261 = Coupling(name = 'GC_261',
                  value = '-((cbWRe*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_262 = Coupling(name = 'GC_262',
                  value = '(cbWRe*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_263 = Coupling(name = 'GC_263',
                  value = '(ceWIm11*ee)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_264 = Coupling(name = 'GC_264',
                  value = '(ceWIm22*ee)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_265 = Coupling(name = 'GC_265',
                  value = '(ceWIm33*ee)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_266 = Coupling(name = 'GC_266',
                  value = '-((ceWRe11*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_267 = Coupling(name = 'GC_267',
                  value = '(ceWRe11*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_268 = Coupling(name = 'GC_268',
                  value = '-((ceWRe22*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_269 = Coupling(name = 'GC_269',
                  value = '(ceWRe22*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((ceWRe33*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_271 = Coupling(name = 'GC_271',
                  value = '(ceWRe33*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_272 = Coupling(name = 'GC_272',
                  value = '(4*cHW*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_273 = Coupling(name = 'GC_273',
                  value = '(2*cHWB*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':3})

GC_274 = Coupling(name = 'GC_274',
                  value = '(-2*cHWBtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':3})

GC_275 = Coupling(name = 'GC_275',
                  value = '(-4*cHWtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':3})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((ctWIm*ee)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((ctWRe*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_278 = Coupling(name = 'GC_278',
                  value = '(ctWRe*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_279 = Coupling(name = 'GC_279',
                  value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_280 = Coupling(name = 'GC_280',
                  value = '(-2*cth*cWtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_281 = Coupling(name = 'GC_281',
                  value = '(-4*cHW*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_282 = Coupling(name = 'GC_282',
                  value = '(-6*cth*cW*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_283 = Coupling(name = 'GC_283',
                  value = '(-4*cth*cWtil*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_284 = Coupling(name = 'GC_284',
                  value = '(cbGIm*complex(0,1)*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(cbGRe*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QCD':1,'QED':2})

GC_286 = Coupling(name = 'GC_286',
                  value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':1,'QED':2})

GC_287 = Coupling(name = 'GC_287',
                  value = '(cGtil*complex(0,1)*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':1,'QED':2})

GC_288 = Coupling(name = 'GC_288',
                  value = '(-4*cHG*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':2})

GC_289 = Coupling(name = 'GC_289',
                  value = '(4*cHGtil*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1,'QED':2})

GC_290 = Coupling(name = 'GC_290',
                  value = '(ctGIm*complex(0,1)*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QCD':1,'QED':2})

GC_291 = Coupling(name = 'GC_291',
                  value = '(ctGRe*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QCD':1,'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '(-3*cG*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(3*cG*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '(-2*cGtil*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':2,'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '(2*cGtil*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':2,'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '(-4*cHG*complex(0,1)*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '-((cG*complex(0,1)*G**3)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '(cG*complex(0,1)*G**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '-((cGtil*complex(0,1)*G**3)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':3,'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(cGtil*complex(0,1)*G**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':3,'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(-2*ee*complex(0,1)*propCorr)/3.',
                  order = {'NPprop':1,'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '-(ee*complex(0,1)*propCorr)',
                  order = {'NPprop':1,'QED':1})

GC_303 = Coupling(name = 'GC_303',
                  value = 'ee**2*complex(0,1)*propCorr',
                  order = {'NPprop':1,'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(complex(0,1)*G*propCorr)',
                  order = {'NPprop':1,'QCD':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '-6*complex(0,1)*lam*propCorr',
                  order = {'NPprop':1,'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(-2*ee*complex(0,1)*propCorr**2)/3.',
                  order = {'NPprop':2,'QED':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '-(ee*complex(0,1)*propCorr**2)',
                  order = {'NPprop':2,'QED':1})

GC_308 = Coupling(name = 'GC_308',
                  value = 'ee**2*complex(0,1)*propCorr**2',
                  order = {'NPprop':2,'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '-(complex(0,1)*G*propCorr**2)',
                  order = {'NPprop':2,'QCD':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-6*complex(0,1)*lam*propCorr**2',
                  order = {'NPprop':2,'QED':2})

GC_311 = Coupling(name = 'GC_311',
                  value = '-6*complex(0,1)*lam*propCorr**3',
                  order = {'NPprop':3,'QED':2})

GC_312 = Coupling(name = 'GC_312',
                  value = '-6*complex(0,1)*lam*propCorr**4',
                  order = {'NPprop':4,'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(-24*cth**2*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**3)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_314 = Coupling(name = 'GC_314',
                  value = '(ee**2*complex(0,1))/(2.*sth**2)',
                  order = {'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '-((ee**2*complex(0,1))/sth**2)',
                  order = {'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(ee**2*complex(0,1))/(2.*cth**2*sth**2)',
                  order = {'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(cth**2*ee**2*complex(0,1))/sth**2',
                  order = {'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(4*cHW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_319 = Coupling(name = 'GC_319',
                  value = '(3*cHDD*ee**2*complex(0,1))/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':4})

GC_320 = Coupling(name = 'GC_320',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_321 = Coupling(name = 'GC_321',
                  value = '(-6*cth*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_322 = Coupling(name = 'GC_322',
                  value = '(-6*cth**3*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_323 = Coupling(name = 'GC_323',
                  value = '(-4*cth*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_324 = Coupling(name = 'GC_324',
                  value = '(-4*cth**3*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_325 = Coupling(name = 'GC_325',
                  value = '(-24*cth*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_326 = Coupling(name = 'GC_326',
                  value = '(ee**2*complex(0,1)*propCorr)/(2.*sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '-((ee**2*complex(0,1)*propCorr)/sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_328 = Coupling(name = 'GC_328',
                  value = '(ee**2*complex(0,1)*propCorr)/(2.*cth**2*sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_329 = Coupling(name = 'GC_329',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr)/sth**2',
                  order = {'NPprop':1,'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(ee**2*complex(0,1)*propCorr**2)/(2.*sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '-((ee**2*complex(0,1)*propCorr**2)/sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_332 = Coupling(name = 'GC_332',
                  value = '(ee**2*complex(0,1)*propCorr**2)/(2.*cth**2*sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_333 = Coupling(name = 'GC_333',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**2)/sth**2',
                  order = {'NPprop':2,'QED':2})

GC_334 = Coupling(name = 'GC_334',
                  value = '(ee**2*complex(0,1)*propCorr**3)/(2.*sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '-((ee**2*complex(0,1)*propCorr**3)/sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(ee**2*complex(0,1)*propCorr**3)/(2.*cth**2*sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**3)/sth**2',
                  order = {'NPprop':3,'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(ee**2*complex(0,1)*propCorr**4)/(2.*sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '-((ee**2*complex(0,1)*propCorr**4)/sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(ee**2*complex(0,1)*propCorr**4)/(2.*cth**2*sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**4)/sth**2',
                  order = {'NPprop':4,'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '-(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-((cth*ee*complex(0,1))/sth)',
                  order = {'QED':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '(-2*cth*ee**2*complex(0,1))/sth',
                  order = {'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '-((cbWIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_348 = Coupling(name = 'GC_348',
                  value = '(cbWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_349 = Coupling(name = 'GC_349',
                  value = '-((ceWIm11*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_350 = Coupling(name = 'GC_350',
                  value = '-((ceWIm22*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_351 = Coupling(name = 'GC_351',
                  value = '-((ceWIm33*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_352 = Coupling(name = 'GC_352',
                  value = '(ceWRe11*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_353 = Coupling(name = 'GC_353',
                  value = '(ceWRe22*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_354 = Coupling(name = 'GC_354',
                  value = '(ceWRe33*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_355 = Coupling(name = 'GC_355',
                  value = '-((cHj3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_356 = Coupling(name = 'GC_356',
                  value = '-((cHl311*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_357 = Coupling(name = 'GC_357',
                  value = '-((cHl322*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_358 = Coupling(name = 'GC_358',
                  value = '-((cHl333*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_359 = Coupling(name = 'GC_359',
                  value = '-((cHQ3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_360 = Coupling(name = 'GC_360',
                  value = '-((cHtbIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':3})

GC_361 = Coupling(name = 'GC_361',
                  value = '(cHtbIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':3})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cHtbRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':3})

GC_363 = Coupling(name = 'GC_363',
                  value = '(cHbq*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':3})

GC_364 = Coupling(name = 'GC_364',
                  value = '(cHd*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':3})

GC_365 = Coupling(name = 'GC_365',
                  value = '(cHe11*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':3})

GC_366 = Coupling(name = 'GC_366',
                  value = '(cHe22*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':3})

GC_367 = Coupling(name = 'GC_367',
                  value = '(cHe33*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':3})

GC_368 = Coupling(name = 'GC_368',
                  value = '(cHj1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':3})

GC_369 = Coupling(name = 'GC_369',
                  value = '-((cHj3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cHj3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_371 = Coupling(name = 'GC_371',
                  value = '(cHl111*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':3})

GC_372 = Coupling(name = 'GC_372',
                  value = '(cHl122*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':3})

GC_373 = Coupling(name = 'GC_373',
                  value = '(cHl133*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':3})

GC_374 = Coupling(name = 'GC_374',
                  value = '-((cHl311*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_375 = Coupling(name = 'GC_375',
                  value = '(cHl311*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_376 = Coupling(name = 'GC_376',
                  value = '-((cHl322*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_377 = Coupling(name = 'GC_377',
                  value = '(cHl322*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_378 = Coupling(name = 'GC_378',
                  value = '-((cHl333*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_379 = Coupling(name = 'GC_379',
                  value = '(cHl333*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_380 = Coupling(name = 'GC_380',
                  value = '(cHQ1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':3})

GC_381 = Coupling(name = 'GC_381',
                  value = '-((cHQ3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_382 = Coupling(name = 'GC_382',
                  value = '(cHQ3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_383 = Coupling(name = 'GC_383',
                  value = '(cHt*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':3})

GC_384 = Coupling(name = 'GC_384',
                  value = '(cHu*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':3})

GC_385 = Coupling(name = 'GC_385',
                  value = '-((cbWIm*cth*ee)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_386 = Coupling(name = 'GC_386',
                  value = '-((cbWRe*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_387 = Coupling(name = 'GC_387',
                  value = '(cbWRe*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_388 = Coupling(name = 'GC_388',
                  value = '-((ceWIm11*cth*ee)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_389 = Coupling(name = 'GC_389',
                  value = '-((ceWIm22*cth*ee)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_390 = Coupling(name = 'GC_390',
                  value = '-((ceWIm33*cth*ee)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_391 = Coupling(name = 'GC_391',
                  value = '-((ceWRe11*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_392 = Coupling(name = 'GC_392',
                  value = '(ceWRe11*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_393 = Coupling(name = 'GC_393',
                  value = '-((ceWRe22*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_394 = Coupling(name = 'GC_394',
                  value = '(ceWRe22*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_395 = Coupling(name = 'GC_395',
                  value = '-((ceWRe33*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_396 = Coupling(name = 'GC_396',
                  value = '(ceWRe33*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_397 = Coupling(name = 'GC_397',
                  value = '(4*cHW*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_398 = Coupling(name = 'GC_398',
                  value = '(-2*cHWB*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':3})

GC_399 = Coupling(name = 'GC_399',
                  value = '(2*cHWBtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':3})

GC_400 = Coupling(name = 'GC_400',
                  value = '(-4*cHWtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':3})

GC_401 = Coupling(name = 'GC_401',
                  value = '(ctWIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_402 = Coupling(name = 'GC_402',
                  value = '(cth*ctWIm*ee)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_403 = Coupling(name = 'GC_403',
                  value = '-((ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_404 = Coupling(name = 'GC_404',
                  value = '-((cth*ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_405 = Coupling(name = 'GC_405',
                  value = '(cth*ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_406 = Coupling(name = 'GC_406',
                  value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_407 = Coupling(name = 'GC_407',
                  value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_408 = Coupling(name = 'GC_408',
                  value = '(-2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_409 = Coupling(name = 'GC_409',
                  value = '(2*cth**2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_410 = Coupling(name = 'GC_410',
                  value = '(8*cHW*cth*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_411 = Coupling(name = 'GC_411',
                  value = '(-6*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_412 = Coupling(name = 'GC_412',
                  value = '(-6*cth**2*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_413 = Coupling(name = 'GC_413',
                  value = '(4*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_414 = Coupling(name = 'GC_414',
                  value = '(-4*cth**2*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_415 = Coupling(name = 'GC_415',
                  value = '(-24*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_416 = Coupling(name = 'GC_416',
                  value = '-((ee*complex(0,1)*propCorr)/(sth*cmath.sqrt(2)))',
                  order = {'NPprop':1,'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '-(ee*complex(0,1)*propCorr)/(2.*cth*sth)',
                  order = {'NPprop':1,'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '(ee*complex(0,1)*propCorr)/(2.*cth*sth)',
                  order = {'NPprop':1,'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '-((cth*ee*complex(0,1)*propCorr)/sth)',
                  order = {'NPprop':1,'QED':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr)/sth',
                  order = {'NPprop':1,'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '-((ee*complex(0,1)*propCorr**2)/(sth*cmath.sqrt(2)))',
                  order = {'NPprop':2,'QED':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '-(ee*complex(0,1)*propCorr**2)/(2.*cth*sth)',
                  order = {'NPprop':2,'QED':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '-((cth*ee*complex(0,1)*propCorr**2)/sth)',
                  order = {'NPprop':2,'QED':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr**2)/sth',
                  order = {'NPprop':2,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '-(ee*complex(0,1)*propCorr**3)/(2.*cth*sth)',
                  order = {'NPprop':3,'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '-((cth*ee*complex(0,1)*propCorr**3)/sth)',
                  order = {'NPprop':3,'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr**3)/sth',
                  order = {'NPprop':3,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '-(ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '(2*ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '-((ee*complex(0,1)*sth)/cth)',
                  order = {'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '(cbBIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '-((cbBRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'QED':2})

GC_433 = Coupling(name = 'GC_433',
                  value = '(cbWIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_434 = Coupling(name = 'GC_434',
                  value = '-((cbWRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_435 = Coupling(name = 'GC_435',
                  value = '(ceBIm11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_436 = Coupling(name = 'GC_436',
                  value = '(ceBIm22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '(ceBIm33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_438 = Coupling(name = 'GC_438',
                  value = '-((ceBRe11*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_439 = Coupling(name = 'GC_439',
                  value = '-((ceBRe22*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_440 = Coupling(name = 'GC_440',
                  value = '-((ceBRe33*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(ceWIm11*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_442 = Coupling(name = 'GC_442',
                  value = '(ceWIm22*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_443 = Coupling(name = 'GC_443',
                  value = '(ceWIm33*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((ceWRe11*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_445 = Coupling(name = 'GC_445',
                  value = '-((ceWRe22*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '-((ceWRe33*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '(ctBIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':2})

GC_448 = Coupling(name = 'GC_448',
                  value = '-((ctBRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctB':1,'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '(-4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(-4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '(4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(4*cHWtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '-((ctWIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(ctWRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(2*cWtil*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_462 = Coupling(name = 'GC_462',
                  value = '(2*cWtil*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_463 = Coupling(name = 'GC_463',
                  value = '(-12*cW*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_464 = Coupling(name = 'GC_464',
                  value = '(-4*cWtil*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_465 = Coupling(name = 'GC_465',
                  value = '-(ee*complex(0,1)*propCorr*sth)/(3.*cth)',
                  order = {'NPprop':1,'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(2*ee*complex(0,1)*propCorr*sth)/(3.*cth)',
                  order = {'NPprop':1,'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((ee*complex(0,1)*propCorr*sth)/cth)',
                  order = {'NPprop':1,'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '(2*ee*complex(0,1)*propCorr**2*sth)/(3.*cth)',
                  order = {'NPprop':2,'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '(2*ee*complex(0,1)*propCorr**3*sth)/(3.*cth)',
                  order = {'NPprop':3,'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '(4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '(-2*cHBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '(4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '(-2*cHWtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(-2*cHWB*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '(-2*cHWBtil*complex(0,1))/LambdaSMEFT**2 + (4*cHWBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '(4*complex(0,1)*gHaa)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(4*complex(0,1)*gHgg1)/vevhat',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '(-4*G*gHgg1)/vevhat',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '(-4*complex(0,1)*G**2*gHgg1)/vevhat',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '(2*complex(0,1)*gHza)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '(-4*complex(0,1)*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '(-4*G*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '(4*complex(0,1)*G**2*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '(-6*gHgg3)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '(-6*complex(0,1)*G*gHgg3)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(-2*complex(0,1)*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '(2*G*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(-2*complex(0,1)*G**2*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '(-8*complex(0,1)*G**2*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(complex(0,1)*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '(-2*G*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(2*complex(0,1)*G**2*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '(6*complex(0,1)*G**2*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(4*complex(0,1)*gHaa*propCorr)/vevhat',
                  order = {'NPprop':1,'QED':3,'SMHLOOP':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '(4*complex(0,1)*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(-4*G*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(-4*complex(0,1)*G**2*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(2*complex(0,1)*gHza*propCorr)/vevhat',
                  order = {'NPprop':1,'QED':3,'SMHLOOP':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(-4*complex(0,1)*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(-4*G*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(4*complex(0,1)*G**2*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(-6*gHgg3*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(-6*complex(0,1)*G*gHgg3*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(-2*complex(0,1)*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '(2*G*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(-2*complex(0,1)*G**2*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(-8*complex(0,1)*G**2*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '(complex(0,1)*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(-2*G*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '(2*complex(0,1)*G**2*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '(6*complex(0,1)*G**2*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '(2*complex(0,1)*gHza*propCorr**2)/vevhat',
                  order = {'NPprop':2,'QED':3,'SMHLOOP':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '-6*complex(0,1)*lam*vevhat',
                  order = {'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((cbGIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '(cbGRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '(-3*cbHIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1,'NPcpv':1,'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(3*cbHRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1,'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((cbWIm*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '(cbWIm*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(cbWRe*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(-3*ceHIm11*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '(-3*ceHIm22*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '(-3*ceHIm33*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '(3*ceHRe11*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '(3*ceHRe22*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '(3*ceHRe33*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '-((ceWIm11*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(ceWIm11*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '-((ceWIm22*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(ceWIm22*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '-((ceWIm33*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '(ceWIm33*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '(ceWRe11*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(ceWRe22*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(ceWRe33*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(90*cH*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':2})

GC_537 = Coupling(name = 'GC_537',
                  value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QED':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '(-2*cHGtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '(4*cHWtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '-((ctGIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QED':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(ctGRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QED':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((cbBIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(cbBRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '(cbWIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '-((cbWRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '-((ceBIm11*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '-((ceBIm22*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '-((ceBIm33*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '(ceBRe11*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '(ceBRe22*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(ceBRe33*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(ceWIm11*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(ceWIm22*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '(ceWIm33*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '-((ceWRe11*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((ceWRe22*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '-((ceWRe33*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((ctBIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(ctBRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctB':1,'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(4*cHB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '(-2*cHBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '(4*cHW*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '(-2*cHWtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '(-3*ctHIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1,'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(3*ctHRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1,'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '-((ctWIm*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '(ctWIm*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '-((cth*ctWIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '(ctWRe*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '(cth*ctWRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '(cbWIm*ee*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_575 = Coupling(name = 'GC_575',
                  value = '-((cbWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_576 = Coupling(name = 'GC_576',
                  value = '(cbWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_577 = Coupling(name = 'GC_577',
                  value = '(ceWIm11*ee*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '(ceWIm22*ee*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '(ceWIm33*ee*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '-((ceWRe11*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '(ceWRe11*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '-((ceWRe22*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '(ceWRe22*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '-((ceWRe33*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '(ceWRe33*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_586 = Coupling(name = 'GC_586',
                  value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_588 = Coupling(name = 'GC_588',
                  value = '(-2*cHWBtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '(-4*cHWtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '-((ctWIm*ee*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '-((ctWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_592 = Coupling(name = 'GC_592',
                  value = '(ctWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_593 = Coupling(name = 'GC_593',
                  value = '(-4*cHW*ee**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_594 = Coupling(name = 'GC_594',
                  value = '(cbGIm*complex(0,1)*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QCD':1,'QED':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '(cbGRe*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QCD':1,'QED':1})

GC_596 = Coupling(name = 'GC_596',
                  value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':1})

GC_597 = Coupling(name = 'GC_597',
                  value = '(4*cHGtil*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1,'QED':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '(ctGIm*complex(0,1)*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QCD':1,'QED':1})

GC_599 = Coupling(name = 'GC_599',
                  value = '(ctGRe*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QCD':1,'QED':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '(-4*cHG*complex(0,1)*G**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':1})

GC_601 = Coupling(name = 'GC_601',
                  value = '-6*complex(0,1)*lam*propCorr*vevhat',
                  order = {'NPprop':1,'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '-6*complex(0,1)*lam*propCorr**2*vevhat',
                  order = {'NPprop':2,'QED':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '-6*complex(0,1)*lam*propCorr**3*vevhat',
                  order = {'NPprop':3,'QED':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'QED':1})

GC_605 = Coupling(name = 'GC_605',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*cth**2*sth**2)',
                  order = {'QED':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '(4*cHW*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_607 = Coupling(name = 'GC_607',
                  value = '(3*cHDD*ee**2*complex(0,1)*vevhat)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':3})

GC_608 = Coupling(name = 'GC_608',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_609 = Coupling(name = 'GC_609',
                  value = '(ee**2*complex(0,1)*propCorr*vevhat)/(2.*sth**2)',
                  order = {'NPprop':1,'QED':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '(ee**2*complex(0,1)*propCorr*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':1,'QED':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '(ee**2*complex(0,1)*propCorr**2*vevhat)/(2.*sth**2)',
                  order = {'NPprop':2,'QED':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '(ee**2*complex(0,1)*propCorr**2*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':2,'QED':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '(ee**2*complex(0,1)*propCorr**3*vevhat)/(2.*sth**2)',
                  order = {'NPprop':3,'QED':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '(ee**2*complex(0,1)*propCorr**3*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':3,'QED':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '-((cbWIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '(cbWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '-((ceWIm11*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '-((ceWIm22*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-((ceWIm33*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '(ceWRe11*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '(ceWRe22*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '(ceWRe33*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_623 = Coupling(name = 'GC_623',
                  value = '-((cHj3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_624 = Coupling(name = 'GC_624',
                  value = '-((cHl311*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_625 = Coupling(name = 'GC_625',
                  value = '-((cHl322*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '-((cHl333*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-((cHtbIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '(cHtbIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(cHtbRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '(cHbq*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':2})

GC_632 = Coupling(name = 'GC_632',
                  value = '(cHd*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '(cHe11*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(cHe22*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '(cHe33*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '(cHj1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':2})

GC_637 = Coupling(name = 'GC_637',
                  value = '-((cHj3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '(cHj3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '(cHl111*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':2})

GC_640 = Coupling(name = 'GC_640',
                  value = '(cHl122*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '(cHl133*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':2})

GC_642 = Coupling(name = 'GC_642',
                  value = '-((cHl311*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cHl311*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_644 = Coupling(name = 'GC_644',
                  value = '-((cHl322*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cHl322*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '-((cHl333*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(cHl333*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(cHQ1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '(cHQ3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_651 = Coupling(name = 'GC_651',
                  value = '(cHt*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':2})

GC_652 = Coupling(name = 'GC_652',
                  value = '(cHu*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '-((cbWIm*cth*ee*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '-((cbWRe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '(cbWRe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_656 = Coupling(name = 'GC_656',
                  value = '-((ceWIm11*cth*ee*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '-((ceWIm22*cth*ee*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_658 = Coupling(name = 'GC_658',
                  value = '-((ceWIm33*cth*ee*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_659 = Coupling(name = 'GC_659',
                  value = '-((ceWRe11*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_660 = Coupling(name = 'GC_660',
                  value = '(ceWRe11*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_661 = Coupling(name = 'GC_661',
                  value = '-((ceWRe22*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_662 = Coupling(name = 'GC_662',
                  value = '(ceWRe22*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_663 = Coupling(name = 'GC_663',
                  value = '-((ceWRe33*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_664 = Coupling(name = 'GC_664',
                  value = '(ceWRe33*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_665 = Coupling(name = 'GC_665',
                  value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_666 = Coupling(name = 'GC_666',
                  value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_667 = Coupling(name = 'GC_667',
                  value = '(2*cHWBtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_668 = Coupling(name = 'GC_668',
                  value = '(-4*cHWtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_669 = Coupling(name = 'GC_669',
                  value = '(ctWIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cth*ctWIm*ee*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '-((ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '-((cth*ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cth*ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_674 = Coupling(name = 'GC_674',
                  value = '(8*cHW*cth*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cbBIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '-((cbBRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'QED':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '(cbWIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '-((cbWRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(ceBIm11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '(ceBIm22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(ceBIm33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '-((ceBRe11*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '-((ceBRe22*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '-((ceBRe33*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '(ceWIm11*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '(ceWIm22*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '(ceWIm33*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '-((ceWRe11*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '-((ceWRe22*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '-((ceWRe33*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(ctBIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '-((ctBRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctB':1,'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '(-4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '(4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '(-4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '(4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_699 = Coupling(name = 'GC_699',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_700 = Coupling(name = 'GC_700',
                  value = '(4*cHWtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_701 = Coupling(name = 'GC_701',
                  value = '-((ctWIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_702 = Coupling(name = 'GC_702',
                  value = '(ctWRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_703 = Coupling(name = 'GC_703',
                  value = '(4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_704 = Coupling(name = 'GC_704',
                  value = '(-2*cHBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_705 = Coupling(name = 'GC_705',
                  value = '(4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_706 = Coupling(name = 'GC_706',
                  value = '(-2*cHWtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_707 = Coupling(name = 'GC_707',
                  value = '-((cbHIm*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbH':1,'NPcpv':1})

GC_708 = Coupling(name = 'GC_708',
                  value = '(cbHRe*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1})

GC_709 = Coupling(name = 'GC_709',
                  value = '-((ceHIm11*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1})

GC_710 = Coupling(name = 'GC_710',
                  value = '-((ceHIm22*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1})

GC_711 = Coupling(name = 'GC_711',
                  value = '-((ceHIm33*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1})

GC_712 = Coupling(name = 'GC_712',
                  value = '(ceHRe11*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1})

GC_713 = Coupling(name = 'GC_713',
                  value = '(ceHRe22*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1})

GC_714 = Coupling(name = 'GC_714',
                  value = '(ceHRe33*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1})

GC_715 = Coupling(name = 'GC_715',
                  value = '(36*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '-((ctHIm*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '(ctHRe*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((cHWBtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '(-2*cHWtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_720 = Coupling(name = 'GC_720',
                  value = '(2*cHGtil*G*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '(-12*cHbox*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_722 = Coupling(name = 'GC_722',
                  value = '(3*cHDD*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(-3*cll1221*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**2)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_726 = Coupling(name = 'GC_726',
                  value = '(cHDD*ee**2*complex(0,1)*vevhat**2)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_727 = Coupling(name = 'GC_727',
                  value = '(cll1221*ee**2*complex(0,1)*vevhat**2)/(4.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_728 = Coupling(name = 'GC_728',
                  value = '-((cHj3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_730 = Coupling(name = 'GC_730',
                  value = '-(cHtbIm*ee*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':1})

GC_731 = Coupling(name = 'GC_731',
                  value = '(cHtbIm*ee*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':1})

GC_732 = Coupling(name = 'GC_732',
                  value = '(cHtbRe*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':1})

GC_733 = Coupling(name = 'GC_733',
                  value = '(cHbq*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':1})

GC_734 = Coupling(name = 'GC_734',
                  value = '(cHd*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':1})

GC_735 = Coupling(name = 'GC_735',
                  value = '(cHDD*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '(cHe11*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '(cHe22*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':1})

GC_738 = Coupling(name = 'GC_738',
                  value = '(cHe33*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':1})

GC_739 = Coupling(name = 'GC_739',
                  value = '(cHj1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':1})

GC_740 = Coupling(name = 'GC_740',
                  value = '-(cHj3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_741 = Coupling(name = 'GC_741',
                  value = '(cHj3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_742 = Coupling(name = 'GC_742',
                  value = '(cHl111*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':1})

GC_743 = Coupling(name = 'GC_743',
                  value = '(cHl122*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':1})

GC_744 = Coupling(name = 'GC_744',
                  value = '(cHl133*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':1})

GC_745 = Coupling(name = 'GC_745',
                  value = '(cHQ1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':1})

GC_746 = Coupling(name = 'GC_746',
                  value = '-(cHQ3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_747 = Coupling(name = 'GC_747',
                  value = '(cHQ3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_748 = Coupling(name = 'GC_748',
                  value = '(cHt*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':1})

GC_749 = Coupling(name = 'GC_749',
                  value = '(cHu*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':1})

GC_750 = Coupling(name = 'GC_750',
                  value = '-(cll1221*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_751 = Coupling(name = 'GC_751',
                  value = '-((cHWB*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '(cHWBtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(-2*cHWtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2*(1 - 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_755 = Coupling(name = 'GC_755',
                  value = '(cll1221*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2*(1 - 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_757 = Coupling(name = 'GC_757',
                  value = '-((cHWB*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-1 + 2*sth**2)))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_758 = Coupling(name = 'GC_758',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_759 = Coupling(name = 'GC_759',
                  value = '-((cHWB*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-1 + 2*sth**2)*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_760 = Coupling(name = 'GC_760',
                  value = '(-2*cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_761 = Coupling(name = 'GC_761',
                  value = '(-2*cHWB*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_762 = Coupling(name = 'GC_762',
                  value = '-(cHDD*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_763 = Coupling(name = 'GC_763',
                  value = '(cHDD*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_764 = Coupling(name = 'GC_764',
                  value = '-(cll1221*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_765 = Coupling(name = 'GC_765',
                  value = '(cll1221*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_766 = Coupling(name = 'GC_766',
                  value = '-(cHDD*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_767 = Coupling(name = 'GC_767',
                  value = '(cHDD*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_768 = Coupling(name = 'GC_768',
                  value = '-(cll1221*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_769 = Coupling(name = 'GC_769',
                  value = '(cll1221*ee*complex(0,1)*vevhat**2)/(8.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_770 = Coupling(name = 'GC_770',
                  value = '-(cHDD*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_771 = Coupling(name = 'GC_771',
                  value = '(cll1221*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_772 = Coupling(name = 'GC_772',
                  value = '-(cHDD*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_773 = Coupling(name = 'GC_773',
                  value = '(-2*cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_774 = Coupling(name = 'GC_774',
                  value = '(2*cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '(cll1221*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '(cHDD*ee*complex(0,1)*sth*vevhat**2)/(12.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '-(cHDD*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '(cHDD*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '(cHl311*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '(cHl311*ee*complex(0,1)*sth*vevhat**2)/(cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '(cHl322*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '(cHl322*ee*complex(0,1)*sth*vevhat**2)/(cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '-(cll1221*ee*complex(0,1)*sth*vevhat**2)/(12.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '(cll1221*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '-(cll1221*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '(cll1221*cth**2*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*(-sth + 2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*(-sth + 2*sth**3))',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_788 = Coupling(name = 'GC_788',
                  value = '(cHDD*cth**2*ee*complex(0,1)*vevhat**2)/((4*LambdaSMEFT**2*sth - 8*LambdaSMEFT**2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '(6*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '(-6*cHbox*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '(3*cHDD*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '(-3*cll1221*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_795 = Coupling(name = 'GC_795',
                  value = '(cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '(cll1221*ee**2*complex(0,1)*vevhat**3)/(8.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-(cll1221*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '(cHWB*cth*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*(-sth + 2*sth**3))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '(-2*cHWB*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_800 = Coupling(name = 'GC_800',
                  value = '(-2*cHWBtil*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_801 = Coupling(name = 'GC_801',
                  value = '(6*cHl311*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + (6*cHl322*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_802 = Coupling(name = 'GC_802',
                  value = '-(cHl311*ee**2*complex(0,1)*vevhat**2)/(2.*cth**2*LambdaSMEFT**2*sth**2) - (cHl322*ee**2*complex(0,1)*vevhat**2)/(2.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_803 = Coupling(name = 'GC_803',
                  value = '(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth) - (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_804 = Coupling(name = 'GC_804',
                  value = '-(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth) + (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth) + (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth) - (cHl333*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_806 = Coupling(name = 'GC_806',
                  value = '(-3*cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*(-1 + 2*sth**2)) + (cHDD*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_807 = Coupling(name = 'GC_807',
                  value = '(cHl311*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2)) + (cHl322*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_808 = Coupling(name = 'GC_808',
                  value = '-((cHl311*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))) - (cHl322*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_809 = Coupling(name = 'GC_809',
                  value = '(cHl311*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2*(-1 + 2*sth**2)) + (cHl322*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_810 = Coupling(name = 'GC_810',
                  value = '-(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) - (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) - (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_812 = Coupling(name = 'GC_812',
                  value = '-(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) + (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) + (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_814 = Coupling(name = 'GC_814',
                  value = '(cHl333*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth) + (cHl311*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) + (cHl322*ee*complex(0,1)*vevhat**2)/(4.*cth*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '-(cHl311*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2)) - (cHl322*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '-((cHl311*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*(-1 + 2*sth**2))) - (cHl322*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_817 = Coupling(name = 'GC_817',
                  value = '(cHl311*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2*(-1 + 2*sth**2)) + (cHl322*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_818 = Coupling(name = 'GC_818',
                  value = '-(cHl311*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2*(-1 + 2*sth**2)) - (cHl322*ee*complex(0,1)*sth*vevhat**2)/(3.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_819 = Coupling(name = 'GC_819',
                  value = '(cHl311*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2*(-1 + 2*sth**2)) + (cHl322*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_820 = Coupling(name = 'GC_820',
                  value = '(cHl322*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2)*cmath.sqrt(2)) - (3*cHl322*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2*(-1 + 2*sth**2)*cmath.sqrt(2)) + (cHl311*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_821 = Coupling(name = 'GC_821',
                  value = '(cHl311*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*(-1 + 2*sth**2)*cmath.sqrt(2)) - (3*cHl311*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2*(-1 + 2*sth**2)*cmath.sqrt(2)) + (cHl322*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_822 = Coupling(name = 'GC_822',
                  value = '(cHl311*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2)) + (cHl322*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_823 = Coupling(name = 'GC_823',
                  value = '-((cHl333*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) + (cHl311*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2)) + (cHl322*cth**2*ee*complex(0,1)*vevhat**2)/((2*LambdaSMEFT**2*sth - 4*LambdaSMEFT**2*sth**3)*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_824 = Coupling(name = 'GC_824',
                  value = '(3*cHl311*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2 + (3*cHl322*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_825 = Coupling(name = 'GC_825',
                  value = '-(cHl311*ee**2*complex(0,1)*vevhat**3)/(4.*cth**2*LambdaSMEFT**2*sth**2) - (cHl322*ee**2*complex(0,1)*vevhat**3)/(4.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_826 = Coupling(name = 'GC_826',
                  value = '-(cHDD*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*(-1 + 2*sth**2)) + (3*cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_827 = Coupling(name = 'GC_827',
                  value = '(cHl311*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2)) + (cHl322*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2*sth**2*(-1 + 2*sth**2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_828 = Coupling(name = 'GC_828',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_829 = Coupling(name = 'GC_829',
                  value = '-((complex(0,1)*propCorr*yb)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_830 = Coupling(name = 'GC_830',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_831 = Coupling(name = 'GC_831',
                  value = '(cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_832 = Coupling(name = 'GC_832',
                  value = '-(cll1221*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_833 = Coupling(name = 'GC_833',
                  value = '(cHl311*complex(0,1)*vevhat**2*yb)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*yb)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_834 = Coupling(name = 'GC_834',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_835 = Coupling(name = 'GC_835',
                  value = '-((cjQtu1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_836 = Coupling(name = 'GC_836',
                  value = '(cjQtu1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_837 = Coupling(name = 'GC_837',
                  value = '(cjQtu1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu1':1,'QED':3})

GC_838 = Coupling(name = 'GC_838',
                  value = '-((cjQtu8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_839 = Coupling(name = 'GC_839',
                  value = '(cjQtu8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_840 = Coupling(name = 'GC_840',
                  value = '(cjQtu8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu8':1,'QED':3})

GC_841 = Coupling(name = 'GC_841',
                  value = '-((cjuQb1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_842 = Coupling(name = 'GC_842',
                  value = '(cjuQb1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_843 = Coupling(name = 'GC_843',
                  value = '-((cjuQb1Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_844 = Coupling(name = 'GC_844',
                  value = '(cjuQb1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_845 = Coupling(name = 'GC_845',
                  value = '-((cjuQb8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_846 = Coupling(name = 'GC_846',
                  value = '(cjuQb8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_847 = Coupling(name = 'GC_847',
                  value = '-((cjuQb8Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_848 = Coupling(name = 'GC_848',
                  value = '(cjuQb8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_849 = Coupling(name = 'GC_849',
                  value = '-((cleju1Im11*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_850 = Coupling(name = 'GC_850',
                  value = '(cleju1Im11*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_851 = Coupling(name = 'GC_851',
                  value = '-((cleju1Im22*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_852 = Coupling(name = 'GC_852',
                  value = '(cleju1Im22*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_853 = Coupling(name = 'GC_853',
                  value = '-((cleju1Im33*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_854 = Coupling(name = 'GC_854',
                  value = '(cleju1Im33*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((cleju1Re11*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_856 = Coupling(name = 'GC_856',
                  value = '(cleju1Re11*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_857 = Coupling(name = 'GC_857',
                  value = '-((cleju1Re22*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_858 = Coupling(name = 'GC_858',
                  value = '(cleju1Re22*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((cleju1Re33*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_860 = Coupling(name = 'GC_860',
                  value = '(cleju1Re33*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'QED':3})

GC_861 = Coupling(name = 'GC_861',
                  value = '-(cleju3Im11*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_862 = Coupling(name = 'GC_862',
                  value = '-(cleju3Im11*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_863 = Coupling(name = 'GC_863',
                  value = '(cleju3Im11*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_864 = Coupling(name = 'GC_864',
                  value = '(cleju3Im11*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_865 = Coupling(name = 'GC_865',
                  value = '-(cleju3Im22*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_866 = Coupling(name = 'GC_866',
                  value = '-(cleju3Im22*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cleju3Im22*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_868 = Coupling(name = 'GC_868',
                  value = '(cleju3Im22*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_869 = Coupling(name = 'GC_869',
                  value = '-(cleju3Im33*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_870 = Coupling(name = 'GC_870',
                  value = '-(cleju3Im33*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_871 = Coupling(name = 'GC_871',
                  value = '(cleju3Im33*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_872 = Coupling(name = 'GC_872',
                  value = '(cleju3Im33*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_873 = Coupling(name = 'GC_873',
                  value = '-(cleju3Re11*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_874 = Coupling(name = 'GC_874',
                  value = '(cleju3Re11*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_875 = Coupling(name = 'GC_875',
                  value = '-(cleju3Re11*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_876 = Coupling(name = 'GC_876',
                  value = '(cleju3Re11*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_877 = Coupling(name = 'GC_877',
                  value = '-(cleju3Re22*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_878 = Coupling(name = 'GC_878',
                  value = '(cleju3Re22*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_879 = Coupling(name = 'GC_879',
                  value = '-(cleju3Re22*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cleju3Re22*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_881 = Coupling(name = 'GC_881',
                  value = '-(cleju3Re33*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cleju3Re33*complex(0,1)*yc)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_883 = Coupling(name = 'GC_883',
                  value = '-(cleju3Re33*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cleju3Re33*complex(0,1)*yc)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':3})

GC_885 = Coupling(name = 'GC_885',
                  value = '-((cQujb1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_886 = Coupling(name = 'GC_886',
                  value = '(cQujb1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((cQujb1Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_888 = Coupling(name = 'GC_888',
                  value = '(cQujb1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_889 = Coupling(name = 'GC_889',
                  value = '-((cQujb8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_890 = Coupling(name = 'GC_890',
                  value = '(cQujb8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_891 = Coupling(name = 'GC_891',
                  value = '-((cQujb8Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_892 = Coupling(name = 'GC_892',
                  value = '(cQujb8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_893 = Coupling(name = 'GC_893',
                  value = '-((cth*cuBIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_894 = Coupling(name = 'GC_894',
                  value = '(cth*cuBRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_895 = Coupling(name = 'GC_895',
                  value = '-((cuGIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':3})

GC_896 = Coupling(name = 'GC_896',
                  value = '(cuGRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':3})

GC_897 = Coupling(name = 'GC_897',
                  value = '(-3*cuHIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':3})

GC_898 = Coupling(name = 'GC_898',
                  value = '(3*cuHRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':3})

GC_899 = Coupling(name = 'GC_899',
                  value = '-((cuWIm*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_900 = Coupling(name = 'GC_900',
                  value = '(cuWIm*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_901 = Coupling(name = 'GC_901',
                  value = '-((cth*cuWIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_902 = Coupling(name = 'GC_902',
                  value = '(cuWRe*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_903 = Coupling(name = 'GC_903',
                  value = '(cth*cuWRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_904 = Coupling(name = 'GC_904',
                  value = '-((cuWIm*ee*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_905 = Coupling(name = 'GC_905',
                  value = '-((cuWRe*ee*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_906 = Coupling(name = 'GC_906',
                  value = '(cuWRe*ee*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_907 = Coupling(name = 'GC_907',
                  value = '(cuGIm*complex(0,1)*G*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':3})

GC_908 = Coupling(name = 'GC_908',
                  value = '(cuGRe*G*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_909 = Coupling(name = 'GC_909',
                  value = '-((complex(0,1)*propCorr*yc)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_910 = Coupling(name = 'GC_910',
                  value = '(cuWIm*ee*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cth*cuWIm*ee*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_913 = Coupling(name = 'GC_913',
                  value = '-((cth*cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_914 = Coupling(name = 'GC_914',
                  value = '(cth*cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_915 = Coupling(name = 'GC_915',
                  value = '(cuBIm*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((cuBRe*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((cuWIm*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_918 = Coupling(name = 'GC_918',
                  value = '(cuWRe*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_919 = Coupling(name = 'GC_919',
                  value = '-((cth*cuBIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_920 = Coupling(name = 'GC_920',
                  value = '(cth*cuBRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_921 = Coupling(name = 'GC_921',
                  value = '-((cuGIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':2})

GC_922 = Coupling(name = 'GC_922',
                  value = '(cuGRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':2})

GC_923 = Coupling(name = 'GC_923',
                  value = '(-3*cuHIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':2})

GC_924 = Coupling(name = 'GC_924',
                  value = '(3*cuHRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':2})

GC_925 = Coupling(name = 'GC_925',
                  value = '-((cuWIm*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_926 = Coupling(name = 'GC_926',
                  value = '(cuWIm*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_927 = Coupling(name = 'GC_927',
                  value = '-((cth*cuWIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_928 = Coupling(name = 'GC_928',
                  value = '(cuWRe*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_929 = Coupling(name = 'GC_929',
                  value = '(cth*cuWRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_930 = Coupling(name = 'GC_930',
                  value = '-((cuWIm*ee*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_931 = Coupling(name = 'GC_931',
                  value = '-((cuWRe*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_932 = Coupling(name = 'GC_932',
                  value = '(cuWRe*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_933 = Coupling(name = 'GC_933',
                  value = '(cuGIm*complex(0,1)*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':2})

GC_934 = Coupling(name = 'GC_934',
                  value = '(cuGRe*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '(cuWIm*ee*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_936 = Coupling(name = 'GC_936',
                  value = '(cth*cuWIm*ee*vevhat*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_937 = Coupling(name = 'GC_937',
                  value = '-((cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_938 = Coupling(name = 'GC_938',
                  value = '-((cth*cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_939 = Coupling(name = 'GC_939',
                  value = '(cth*cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_940 = Coupling(name = 'GC_940',
                  value = '(cuBIm*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_941 = Coupling(name = 'GC_941',
                  value = '-((cuBRe*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_942 = Coupling(name = 'GC_942',
                  value = '-((cuWIm*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '(cuWRe*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_945 = Coupling(name = 'GC_945',
                  value = '(cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_946 = Coupling(name = 'GC_946',
                  value = '-(cll1221*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcll1':1,'QED':1})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((cuHIm*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':1})

GC_948 = Coupling(name = 'GC_948',
                  value = '(cuHRe*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':1})

GC_949 = Coupling(name = 'GC_949',
                  value = '(cHl311*complex(0,1)*vevhat**2*yc)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*yc)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_951 = Coupling(name = 'GC_951',
                  value = '-((cdGIm*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':3})

GC_952 = Coupling(name = 'GC_952',
                  value = '(cdGRe*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_953 = Coupling(name = 'GC_953',
                  value = '(-3*cdHIm*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':3})

GC_954 = Coupling(name = 'GC_954',
                  value = '(3*cdHRe*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((cdWIm*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_956 = Coupling(name = 'GC_956',
                  value = '(cdWIm*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_957 = Coupling(name = 'GC_957',
                  value = '(cdWRe*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_958 = Coupling(name = 'GC_958',
                  value = '-((cjQbd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_959 = Coupling(name = 'GC_959',
                  value = '(cjQbd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_960 = Coupling(name = 'GC_960',
                  value = '(cjQbd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'QED':3})

GC_961 = Coupling(name = 'GC_961',
                  value = '-((cjQbd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_962 = Coupling(name = 'GC_962',
                  value = '(cjQbd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_963 = Coupling(name = 'GC_963',
                  value = '(cjQbd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'QED':3})

GC_964 = Coupling(name = 'GC_964',
                  value = '-((cjtQd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_965 = Coupling(name = 'GC_965',
                  value = '(cjtQd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((cjtQd1Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_967 = Coupling(name = 'GC_967',
                  value = '(cjtQd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((cjtQd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_969 = Coupling(name = 'GC_969',
                  value = '(cjtQd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((cjtQd8Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_971 = Coupling(name = 'GC_971',
                  value = '(cjtQd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((cledjIm11*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_973 = Coupling(name = 'GC_973',
                  value = '(cledjIm11*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((cledjIm22*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_975 = Coupling(name = 'GC_975',
                  value = '(cledjIm22*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((cledjIm33*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_977 = Coupling(name = 'GC_977',
                  value = '(cledjIm33*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_978 = Coupling(name = 'GC_978',
                  value = '(cledjRe11*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'QED':3})

GC_979 = Coupling(name = 'GC_979',
                  value = '(cledjRe22*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'QED':3})

GC_980 = Coupling(name = 'GC_980',
                  value = '(cledjRe33*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'QED':3})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((cQtjd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_982 = Coupling(name = 'GC_982',
                  value = '(cQtjd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((cQtjd1Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_984 = Coupling(name = 'GC_984',
                  value = '(cQtjd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_985 = Coupling(name = 'GC_985',
                  value = '-((cQtjd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_986 = Coupling(name = 'GC_986',
                  value = '(cQtjd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((cQtjd8Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_988 = Coupling(name = 'GC_988',
                  value = '(cQtjd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_989 = Coupling(name = 'GC_989',
                  value = '-((cdBIm*cth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_990 = Coupling(name = 'GC_990',
                  value = '(cdBRe*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_991 = Coupling(name = 'GC_991',
                  value = '(cdWIm*cth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((cdWRe*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_993 = Coupling(name = 'GC_993',
                  value = '(cdWIm*ee*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((cdWRe*ee*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_995 = Coupling(name = 'GC_995',
                  value = '(cdWRe*ee*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_996 = Coupling(name = 'GC_996',
                  value = '(cdGIm*complex(0,1)*G*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':3})

GC_997 = Coupling(name = 'GC_997',
                  value = '(cdGRe*G*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((complex(0,1)*propCorr*ydo)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_999 = Coupling(name = 'GC_999',
                  value = '-((cdWIm*ee*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '(cdWRe*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '-((cdWIm*cth*ee*ydo)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((cdWRe*cth*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(cdWRe*cth*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(cdBIm*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((cdBRe*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'QED':3})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '(cdWIm*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-((cdWRe*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((cdGIm*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':2})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(cdGRe*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QED':2})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(-3*cdHIm*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':2})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '(3*cdHRe*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'QED':2})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((cdWIm*vevhat*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(cdWIm*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(cdWRe*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '-((cdBIm*cth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(cdBRe*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'QED':2})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(cdWIm*cth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '-((cdWRe*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(cdWIm*ee*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((cdWRe*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(cdWRe*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(cdGIm*complex(0,1)*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(cdGRe*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '-((cdWIm*ee*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(cdWRe*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((cdWIm*cth*ee*vevhat*ydo)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '-((cdWRe*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '(cdWRe*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(cdBIm*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((cdBRe*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'QED':2})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '(cdWIm*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-((cdWRe*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-((cdHIm*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':1})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '(cdHRe*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'QED':1})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-(cll1221*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((cjujd11Im*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(cjujd11Im*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((cjujd11Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '(cjujd11Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((cjujd1Im*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '(cjujd1Im*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((cjujd1Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(cjujd1Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((cjujd81Im*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(cjujd81Im*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-((cjujd81Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '(cjujd81Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '-((cjujd8Im*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(cjujd8Im*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((cjujd8Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(cjujd8Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(cHl311*complex(0,1)*vevhat**2*ydo)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*ydo)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '-((complex(0,1)*propCorr*ye)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-(cll1221*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(cHl311*complex(0,1)*vevhat**2*ye)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*ye)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '-((complex(0,1)*propCorr*ym)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-(cll1221*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(cHl311*complex(0,1)*vevhat**2*ym)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*ym)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-((cdGIm*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':3})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(cdGRe*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QED':3})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(-3*cdHIm*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':3})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(3*cdHRe*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'QED':3})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-((cdWIm*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '(cdWIm*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(cdWRe*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((cjQbd1Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '(cjQbd1Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '(cjQbd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQbd1':1,'QED':3})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-((cjQbd8Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(cjQbd8Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(cjQbd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQbd8':1,'QED':3})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-((cjtQd1Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(cjtQd1Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-((cjtQd1Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(cjtQd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-((cjtQd8Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(cjtQd8Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((cjtQd8Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '(cjtQd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((cledjIm11*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '(cledjIm11*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((cledjIm22*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(cledjIm22*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '-((cledjIm33*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(cledjIm33*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':3})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(cledjRe11*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':3})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(cledjRe22*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':3})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(cledjRe33*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':3})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-((cQtjd1Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(cQtjd1Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((cQtjd1Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(cQtjd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-((cQtjd8Im*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '(cQtjd8Im*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '-((cQtjd8Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(cQtjd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((cdBIm*cth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(cdBRe*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'QED':3})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(cdWIm*cth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '-((cdWRe*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(cdWIm*ee*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '-((cdWRe*ee*complex(0,1)*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '(cdWRe*ee*complex(0,1)*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(cdGIm*complex(0,1)*G*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':3})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(cdGRe*G*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '-((complex(0,1)*propCorr*ys)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-((cdWIm*ee*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(cdWRe*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-((cdWIm*cth*ee*ys)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '-((cdWRe*cth*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(cdWRe*cth*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcdW':1,'QED':4})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(cdBIm*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-((cdBRe*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'QED':3})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(cdWIm*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-((cdWRe*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '-((cdGIm*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':2})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(cdGRe*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QED':2})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(-3*cdHIm*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':2})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(3*cdHRe*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'QED':2})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '-((cdWIm*vevhat*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(cdWIm*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(cdWRe*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-((cdBIm*cth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(cdBRe*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'QED':2})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(cdWIm*cth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '-((cdWRe*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(cdWIm*ee*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-((cdWRe*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '(cdWRe*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(cdGIm*complex(0,1)*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(cdGRe*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-((cdWIm*ee*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '(cdWRe*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '-((cdWIm*cth*ee*vevhat*ys)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '-((cdWRe*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(cdWRe*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcdW':1,'QED':3})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(cdBIm*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((cdBRe*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdB':1,'QED':2})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '(cdWIm*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((cdWRe*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdW':1,'QED':2})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((cdHIm*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':1})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(cdHRe*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcdH':1,'QED':1})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-(cll1221*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-((cjujd11Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(cjujd11Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '-((cjujd11Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(cjujd11Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '-((cjujd1Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(cjujd1Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '-((cjujd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(cjujd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '-((cjujd81Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(cjujd81Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '-((cjujd81Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(cjujd81Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '-((cjujd8Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(cjujd8Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '-((cjujd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(cjujd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '-((cutbd1Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(cutbd1Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(cutbd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd1':1,'QED':4})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '-((cutbd8Im*yc*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(cutbd8Im*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(cutbd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd8':1,'QED':4})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '-((cHudIm*ee*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(cHudIm*ee*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(cHudRe*ee*complex(0,1)*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '-((cHudIm*ee*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '(cHudIm*ee*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '(cHudRe*ee*complex(0,1)*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '-(cHudIm*ee*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '(cHudIm*ee*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '(cHudRe*ee*complex(0,1)*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(cHl311*complex(0,1)*vevhat**2*ys)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*ys)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '-((complex(0,1)*propCorr*yt)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '-((complex(0,1)*propCorr**2*yt)/cmath.sqrt(2))',
                   order = {'NPprop':2,'QED':1})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '-((complex(0,1)*propCorr**3*yt)/cmath.sqrt(2))',
                   order = {'NPprop':3,'QED':1})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-((cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '-(cll1221*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cHl311*complex(0,1)*vevhat**2*yt)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*yt)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '-((complex(0,1)*propCorr*ytau)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '-(cll1221*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cHl311*complex(0,1)*vevhat**2*ytau)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*ytau)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '-((cjQtu1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(cjQtu1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(cjQtu1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu1':1,'QED':3})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '-((cjQtu8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cjQtu8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(cjQtu8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu8':1,'QED':3})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '-((cjuQb1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(cjuQb1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '-((cjuQb1Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(cjuQb1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '-((cjuQb8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(cjuQb8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '-((cjuQb8Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(cjuQb8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '-((cleju1Im11*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(cleju1Im11*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '-((cleju1Im22*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(cleju1Im22*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '-((cleju1Im33*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(cleju1Im33*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':3})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '-((cleju1Re11*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(cleju1Re11*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '-((cleju1Re22*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(cleju1Re22*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '-((cleju1Re33*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(cleju1Re33*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':3})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '-(cleju3Im11*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '-(cleju3Im11*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(cleju3Im11*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(cleju3Im11*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-(cleju3Im22*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '-(cleju3Im22*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '(cleju3Im22*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '(cleju3Im22*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '-(cleju3Im33*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '-(cleju3Im33*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '(cleju3Im33*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '(cleju3Im33*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':3})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-(cleju3Re11*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(cleju3Re11*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-(cleju3Re11*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '(cleju3Re11*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-(cleju3Re22*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(cleju3Re22*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-(cleju3Re22*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(cleju3Re22*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-(cleju3Re33*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(cleju3Re33*complex(0,1)*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-(cleju3Re33*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(cleju3Re33*complex(0,1)*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':3})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-((cQujb1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '(cQujb1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '-((cQujb1Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(cQujb1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-((cQujb8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(cQujb8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-((cQujb8Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(cQujb8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '-((cth*cuBIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(cth*cuBRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-((cuGIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':3})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '(cuGRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':3})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '(-3*cuHIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':3})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '(3*cuHRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':3})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-((cuWIm*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(cuWIm*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '-((cth*cuWIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '(cuWRe*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '(cth*cuWRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '-((cuWIm*ee*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '-((cuWRe*ee*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(cuWRe*ee*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(cuGIm*complex(0,1)*G*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '(cuGRe*G*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '-((complex(0,1)*propCorr*yup)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(cuWIm*ee*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '(cth*cuWIm*ee*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '-((cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '-((cth*cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '(cth*cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '(cuBIm*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '-((cuBRe*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '-((cuWIm*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '(cuWRe*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '-((cth*cuBIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '(cth*cuBRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '-((cuGIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':2})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '(cuGRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':2})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '(-3*cuHIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':2})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '(3*cuHRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':2})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '-((cuWIm*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '(cuWIm*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '-((cth*cuWIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(cuWRe*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '(cth*cuWRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '-((cuWIm*ee*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '-((cuWRe*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '(cuWRe*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '(cuGIm*complex(0,1)*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '(cuGRe*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '(cuWIm*ee*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '(cth*cuWIm*ee*vevhat*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '-((cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '-((cth*cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '(cth*cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '(cuBIm*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '-((cuBRe*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '-((cuWIm*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '(cuWRe*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '-((cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '(cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '-(cll1221*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcll1':1,'QED':1})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '-((cuHIm*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':1})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(cuHRe*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':1})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '-((cjujd11Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(cjujd11Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '-((cjujd11Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(cjujd11Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '-((cjujd1Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(cjujd1Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '-((cjujd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(cjujd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '-((cjujd81Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(cjujd81Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '-((cjujd81Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(cjujd81Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '-((cjujd8Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(cjujd8Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '-((cjujd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(cjujd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '-((cutbd1Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(cutbd1Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '(cutbd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd1':1,'QED':4})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '-((cutbd8Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '(cutbd8Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(cutbd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd8':1,'QED':4})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '-((cHudIm*ee*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '(cHudIm*ee*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '(cHudRe*ee*complex(0,1)*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '-((cHudIm*ee*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '(cHudIm*ee*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '(cHudRe*ee*complex(0,1)*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '-(cHudIm*ee*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(cHudIm*ee*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '(cHudRe*ee*complex(0,1)*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '-((cjujd11Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(cjujd11Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '-((cjujd11Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(cjujd11Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '-((cjujd1Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '(cjujd1Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '-((cjujd1Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '(cjujd1Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '-((cjujd81Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(cjujd81Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '-((cjujd81Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '(cjujd81Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '-((cjujd8Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '(cjujd8Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '-((cjujd8Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '(cjujd8Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(cHl311*complex(0,1)*vevhat**2*yup)/(2.*LambdaSMEFT**2*cmath.sqrt(2)) + (cHl322*complex(0,1)*vevhat**2*yup)/(2.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'QED':1})

