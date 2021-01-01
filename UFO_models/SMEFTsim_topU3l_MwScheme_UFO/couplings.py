# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Tue 18 Aug 2020 15:03:51


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



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
                value = '(cth**2*dg1*ee*complex(0,1))/3.',
                order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(-2*cth**2*dg1*ee*complex(0,1))/3.',
                order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(cth**2*dg1*ee*complex(0,1))',
                order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'cth**2*dg1*ee*complex(0,1)',
                order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(dg1*ee**2*complex(0,1))/cth**2',
                 order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-2*cth**2*dg1*ee**2*complex(0,1)',
                 order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '2*cth**2*dg1*ee**2*complex(0,1)',
                 order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_14 = Coupling(name = 'GC_14',
                 value = 'G',
                 order = {'QCD':1})

GC_15 = Coupling(name = 'GC_15',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '6*dGf*complex(0,1)*lam',
                 order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-24*dkH*complex(0,1)*lam',
                 order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '6*dMH2*complex(0,1)*lam',
                 order = {'NP':1,'NPcH':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(2*cbb*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbb':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(cbd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbd1':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cbd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbd8':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cbe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbe':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cbGIm/(LambdaSMEFT**2*cmath.sqrt(2)))',
                 order = {'NP':1,'NPcbG':1,'NPcpv':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cbGRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbG':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(-3*cbHIm)/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbH':1,'NPcpv':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(3*cbHRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                 order = {'NP':1,'NPcbH':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(cbj1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbj1':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cbj8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbj8':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cbl*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbl':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cbu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbu1':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cbu8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbu8':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(cbWIm/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = 'cbWIm/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cbWRe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcbW':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(2*cdd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd1':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(2*cdd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd8':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(ced*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPced':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(2*cee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ceu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceu':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-6*cG)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = 'cGtil/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(90*cH*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcH':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHbox':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcHDD':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHG':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(-2*cHGtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHW':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(4*cHWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(cjd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjd1':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cjd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjd8':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cje*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcje':1,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2*cjj11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj11':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(2*cjj18*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj18':1,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(-2*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(2*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(4*cjj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj31':1,'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(-2*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(2*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(4*cjj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcjj38':1,'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cju1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcju1':1,'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(cju8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcju8':1,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cld*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcld':1,'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cle*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(clj1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclj1':1,'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((clj3*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPclj3':1,'QED':2})

GC_67 = Coupling(name = 'GC_67',
                 value = '(clj3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclj3':1,'QED':2})

GC_68 = Coupling(name = 'GC_68',
                 value = '(2*clj3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclj3':1,'QED':2})

GC_69 = Coupling(name = 'GC_69',
                 value = '(2*cll*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcll':1,'QED':2})

GC_70 = Coupling(name = 'GC_70',
                 value = '(2*cll1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcll1':1,'QED':2})

GC_71 = Coupling(name = 'GC_71',
                 value = '(clu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclu':1,'QED':2})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cQb1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQb1':1,'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cQb8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQb8':1,'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(cQd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQd1':1,'QED':2})

GC_75 = Coupling(name = 'GC_75',
                 value = '(cQd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQd8':1,'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cQe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQe':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cQj11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj11':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cQj18*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj18':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((cQj31*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcQj31':1,'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(cQj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj31':1,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(2*cQj31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj31':1,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((cQj38*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcQj38':1,'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(cQj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj38':1,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '(2*cQj38*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQj38':1,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cQl1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQl1':1,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((cQl3*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcQl3':1,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cQl3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQl3':1,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(2*cQl3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQl3':1,'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(2*cQQ1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQQ1':1,'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(2*cQQ8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQQ8':1,'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '(cQt1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQt1':1,'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '(cQt8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQt8':1,'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-(cQtQb1Im/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcpv':1,'NPcQtQb1':1,'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = 'cQtQb1Im/LambdaSMEFT**2',
                 order = {'NP':1,'NPcpv':1,'NPcQtQb1':1,'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((cQtQb1Re*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcQtQb1':1,'QED':2})

GC_96 = Coupling(name = 'GC_96',
                 value = '(cQtQb1Re*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcQtQb1':1,'QED':2})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(cQtQb8Im/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcpv':1,'NPcQtQb8':1,'QED':2})

GC_98 = Coupling(name = 'GC_98',
                 value = 'cQtQb8Im/LambdaSMEFT**2',
                 order = {'NP':1,'NPcpv':1,'NPcQtQb8':1,'QED':2})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((cQtQb8Re*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcQtQb8':1,'QED':2})

GC_100 = Coupling(name = 'GC_100',
                  value = '(cQtQb8Re*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtQb8':1,'QED':2})

GC_101 = Coupling(name = 'GC_101',
                  value = '(cQu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQu1':1,'QED':2})

GC_102 = Coupling(name = 'GC_102',
                  value = '(cQu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQu8':1,'QED':2})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ctb1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctb1':1,'QED':2})

GC_104 = Coupling(name = 'GC_104',
                  value = '(ctb8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctb8':1,'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = '(ctd1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctd1':1,'QED':2})

GC_106 = Coupling(name = 'GC_106',
                  value = '(ctd8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctd8':1,'QED':2})

GC_107 = Coupling(name = 'GC_107',
                  value = '(cte*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcte':1,'QED':2})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(ctGIm/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QED':2})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ctGRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cbBIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '(cbBRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'QED':2})

GC_112 = Coupling(name = 'GC_112',
                  value = '(cbWIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((cbWRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((ctBIm*cth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':2})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ctBRe*cth*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctB':1,'QED':2})

GC_116 = Coupling(name = 'GC_116',
                  value = '(4*cHB*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_117 = Coupling(name = 'GC_117',
                  value = '(-2*cHBtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '(4*cHW*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = '(-2*cHWtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(-3*ctHIm)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1,'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(3*ctHRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1,'QED':2})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ctj1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctj1':1,'QED':2})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ctj8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctj8':1,'QED':2})

GC_124 = Coupling(name = 'GC_124',
                  value = '(ctl*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctl':1,'QED':2})

GC_125 = Coupling(name = 'GC_125',
                  value = '(2*ctt*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctt':1,'QED':2})

GC_126 = Coupling(name = 'GC_126',
                  value = '(ctu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctu1':1,'QED':2})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ctu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctu8':1,'QED':2})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(ctWIm/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_129 = Coupling(name = 'GC_129',
                  value = 'ctWIm/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((cth*ctWIm)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_131 = Coupling(name = 'GC_131',
                  value = '(ctWRe*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(cth*ctWRe*complex(0,1))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '(cud1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcud1':1,'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '(cud8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcud8':1,'QED':2})

GC_135 = Coupling(name = 'GC_135',
                  value = '(2*cuu1*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuu1':1,'QED':2})

GC_136 = Coupling(name = 'GC_136',
                  value = '(2*cuu8*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuu8':1,'QED':2})

GC_137 = Coupling(name = 'GC_137',
                  value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':2})

GC_138 = Coupling(name = 'GC_138',
                  value = '(2*cth*cWtil*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '(cbWIm*ee)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cbWRe*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_141 = Coupling(name = 'GC_141',
                  value = '(cbWRe*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_142 = Coupling(name = 'GC_142',
                  value = '(4*cHW*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_143 = Coupling(name = 'GC_143',
                  value = '(2*cHWB*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':3})

GC_144 = Coupling(name = 'GC_144',
                  value = '(-2*cHWBtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':3})

GC_145 = Coupling(name = 'GC_145',
                  value = '(-4*cHWtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':3})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((ctWIm*ee)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((ctWRe*ee*complex(0,1))/LambdaSMEFT**2)',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_148 = Coupling(name = 'GC_148',
                  value = '(ctWRe*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_149 = Coupling(name = 'GC_149',
                  value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_150 = Coupling(name = 'GC_150',
                  value = '(-2*cth*cWtil*ee*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_151 = Coupling(name = 'GC_151',
                  value = '(-4*cHW*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_152 = Coupling(name = 'GC_152',
                  value = '(-6*cth*cW*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_153 = Coupling(name = 'GC_153',
                  value = '(-4*cth*cWtil*ee**2*complex(0,1))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_154 = Coupling(name = 'GC_154',
                  value = '(cbGIm*complex(0,1)*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(cbGRe*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QCD':1,'QED':2})

GC_156 = Coupling(name = 'GC_156',
                  value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':1,'QED':2})

GC_157 = Coupling(name = 'GC_157',
                  value = '(cGtil*complex(0,1)*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':1,'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '(-4*cHG*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(4*cHGtil*G)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1,'QED':2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ctGIm*complex(0,1)*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QCD':1,'QED':2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(ctGRe*G)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QCD':1,'QED':2})

GC_162 = Coupling(name = 'GC_162',
                  value = '(-3*cG*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_163 = Coupling(name = 'GC_163',
                  value = '(3*cG*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_164 = Coupling(name = 'GC_164',
                  value = '(-2*cGtil*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':2,'QED':2})

GC_165 = Coupling(name = 'GC_165',
                  value = '(2*cGtil*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':2,'QED':2})

GC_166 = Coupling(name = 'GC_166',
                  value = '(-4*cHG*complex(0,1)*G**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':2})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((cG*complex(0,1)*G**3)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_168 = Coupling(name = 'GC_168',
                  value = '(cG*complex(0,1)*G**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cGtil*complex(0,1)*G**3)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':3,'QED':2})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cGtil*complex(0,1)*G**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcGtil':1,'NPcpv':1,'QCD':3,'QED':2})

GC_171 = Coupling(name = 'GC_171',
                  value = '(-2*ee*complex(0,1)*propCorr)/3.',
                  order = {'NPprop':1,'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-(ee*complex(0,1)*propCorr)',
                  order = {'NPprop':1,'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = 'ee**2*complex(0,1)*propCorr',
                  order = {'NPprop':1,'QED':2})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(complex(0,1)*G*propCorr)',
                  order = {'NPprop':1,'QCD':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-6*complex(0,1)*lam*propCorr',
                  order = {'NPprop':1,'QED':2})

GC_176 = Coupling(name = 'GC_176',
                  value = '(-2*ee*complex(0,1)*propCorr**2)/3.',
                  order = {'NPprop':2,'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-(ee*complex(0,1)*propCorr**2)',
                  order = {'NPprop':2,'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = 'ee**2*complex(0,1)*propCorr**2',
                  order = {'NPprop':2,'QED':2})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(complex(0,1)*G*propCorr**2)',
                  order = {'NPprop':2,'QCD':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-6*complex(0,1)*lam*propCorr**2',
                  order = {'NPprop':2,'QED':2})

GC_181 = Coupling(name = 'GC_181',
                  value = '-6*complex(0,1)*lam*propCorr**3',
                  order = {'NPprop':3,'QED':2})

GC_182 = Coupling(name = 'GC_182',
                  value = '-6*complex(0,1)*lam*propCorr**4',
                  order = {'NPprop':4,'QED':2})

GC_183 = Coupling(name = 'GC_183',
                  value = '(-24*cth**2*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**3)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ee**2*complex(0,1))/(2.*sth**2)',
                  order = {'QED':2})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((ee**2*complex(0,1))/sth**2)',
                  order = {'QED':2})

GC_186 = Coupling(name = 'GC_186',
                  value = '(ee**2*complex(0,1))/(2.*cth**2*sth**2)',
                  order = {'QED':2})

GC_187 = Coupling(name = 'GC_187',
                  value = '(cth**2*ee**2*complex(0,1))/sth**2',
                  order = {'QED':2})

GC_188 = Coupling(name = 'GC_188',
                  value = '(dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_189 = Coupling(name = 'GC_189',
                  value = '(-2*dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_190 = Coupling(name = 'GC_190',
                  value = '(dkH*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':2})

GC_191 = Coupling(name = 'GC_191',
                  value = '(dkH*ee**2*complex(0,1))/(cth**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':2})

GC_192 = Coupling(name = 'GC_192',
                  value = '(4*cHW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_193 = Coupling(name = 'GC_193',
                  value = '(3*cHDD*ee**2*complex(0,1))/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':4})

GC_194 = Coupling(name = 'GC_194',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_195 = Coupling(name = 'GC_195',
                  value = '(-6*cth*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_196 = Coupling(name = 'GC_196',
                  value = '(-6*cth**3*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_197 = Coupling(name = 'GC_197',
                  value = '(-4*cth*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_198 = Coupling(name = 'GC_198',
                  value = '(-4*cth**3*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_199 = Coupling(name = 'GC_199',
                  value = '(-24*cth*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee**2*complex(0,1)*propCorr)/(2.*sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((ee**2*complex(0,1)*propCorr)/sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(ee**2*complex(0,1)*propCorr)/(2.*cth**2*sth**2)',
                  order = {'NPprop':1,'QED':2})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr)/sth**2',
                  order = {'NPprop':1,'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee**2*complex(0,1)*propCorr**2)/(2.*sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((ee**2*complex(0,1)*propCorr**2)/sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee**2*complex(0,1)*propCorr**2)/(2.*cth**2*sth**2)',
                  order = {'NPprop':2,'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**2)/sth**2',
                  order = {'NPprop':2,'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(ee**2*complex(0,1)*propCorr**3)/(2.*sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_209 = Coupling(name = 'GC_209',
                  value = '-((ee**2*complex(0,1)*propCorr**3)/sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '(ee**2*complex(0,1)*propCorr**3)/(2.*cth**2*sth**2)',
                  order = {'NPprop':3,'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**3)/sth**2',
                  order = {'NPprop':3,'QED':2})

GC_212 = Coupling(name = 'GC_212',
                  value = '(ee**2*complex(0,1)*propCorr**4)/(2.*sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_213 = Coupling(name = 'GC_213',
                  value = '-((ee**2*complex(0,1)*propCorr**4)/sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ee**2*complex(0,1)*propCorr**4)/(2.*cth**2*sth**2)',
                  order = {'NPprop':4,'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '(cth**2*ee**2*complex(0,1)*propCorr**4)/sth**2',
                  order = {'NPprop':4,'QED':2})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '-(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '-((cth*ee*complex(0,1))/sth)',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-(dgw*ee*complex(0,1))/(2.*cth*sth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(dgw*ee*complex(0,1))/(2.*cth*sth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '-(cth*dgw*ee*complex(0,1))/(2.*sth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(-2*cth*ee**2*complex(0,1))/sth',
                  order = {'QED':2})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((cbWIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_226 = Coupling(name = 'GC_226',
                  value = '(cbWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((cHj3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((cHl3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((cHQ3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((cHtbIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':3})

GC_231 = Coupling(name = 'GC_231',
                  value = '(cHtbIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':3})

GC_232 = Coupling(name = 'GC_232',
                  value = '(cHtbRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':3})

GC_233 = Coupling(name = 'GC_233',
                  value = '(cHbq*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':3})

GC_234 = Coupling(name = 'GC_234',
                  value = '(cHd*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':3})

GC_235 = Coupling(name = 'GC_235',
                  value = '(cHe*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':3})

GC_236 = Coupling(name = 'GC_236',
                  value = '(cHj1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':3})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((cHj3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_238 = Coupling(name = 'GC_238',
                  value = '(cHj3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':3})

GC_239 = Coupling(name = 'GC_239',
                  value = '(cHl1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':3})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((cHl3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_241 = Coupling(name = 'GC_241',
                  value = '(cHl3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_242 = Coupling(name = 'GC_242',
                  value = '(cHQ1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':3})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((cHQ3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_244 = Coupling(name = 'GC_244',
                  value = '(cHQ3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':3})

GC_245 = Coupling(name = 'GC_245',
                  value = '(cHt*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':3})

GC_246 = Coupling(name = 'GC_246',
                  value = '(cHu*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':3})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((cbWIm*cth*ee)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':3})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((cbWRe*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_249 = Coupling(name = 'GC_249',
                  value = '(cbWRe*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcbW':1,'QED':3})

GC_250 = Coupling(name = 'GC_250',
                  value = '(4*cHW*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_251 = Coupling(name = 'GC_251',
                  value = '(-2*cHWB*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':3})

GC_252 = Coupling(name = 'GC_252',
                  value = '(2*cHWBtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':3})

GC_253 = Coupling(name = 'GC_253',
                  value = '(-4*cHWtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':3})

GC_254 = Coupling(name = 'GC_254',
                  value = '(ctWIm*ee)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_255 = Coupling(name = 'GC_255',
                  value = '(cth*ctWIm*ee)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':3})

GC_256 = Coupling(name = 'GC_256',
                  value = '-((ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_257 = Coupling(name = 'GC_257',
                  value = '-((cth*ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_258 = Coupling(name = 'GC_258',
                  value = '(cth*ctWRe*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPctW':1,'QED':3})

GC_259 = Coupling(name = 'GC_259',
                  value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_260 = Coupling(name = 'GC_260',
                  value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_261 = Coupling(name = 'GC_261',
                  value = '(-2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_262 = Coupling(name = 'GC_262',
                  value = '(2*cth**2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_263 = Coupling(name = 'GC_263',
                  value = '(8*cHW*cth*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_264 = Coupling(name = 'GC_264',
                  value = '(-6*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_265 = Coupling(name = 'GC_265',
                  value = '(-6*cth**2*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_266 = Coupling(name = 'GC_266',
                  value = '(4*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_267 = Coupling(name = 'GC_267',
                  value = '(-4*cth**2*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_268 = Coupling(name = 'GC_268',
                  value = '(-24*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_269 = Coupling(name = 'GC_269',
                  value = '-((ee*complex(0,1)*propCorr)/(sth*cmath.sqrt(2)))',
                  order = {'NPprop':1,'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-(ee*complex(0,1)*propCorr)/(2.*cth*sth)',
                  order = {'NPprop':1,'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '(ee*complex(0,1)*propCorr)/(2.*cth*sth)',
                  order = {'NPprop':1,'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((cth*ee*complex(0,1)*propCorr)/sth)',
                  order = {'NPprop':1,'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr)/sth',
                  order = {'NPprop':1,'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '-((ee*complex(0,1)*propCorr**2)/(sth*cmath.sqrt(2)))',
                  order = {'NPprop':2,'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-(ee*complex(0,1)*propCorr**2)/(2.*cth*sth)',
                  order = {'NPprop':2,'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((cth*ee*complex(0,1)*propCorr**2)/sth)',
                  order = {'NPprop':2,'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr**2)/sth',
                  order = {'NPprop':2,'QED':2})

GC_278 = Coupling(name = 'GC_278',
                  value = '-(ee*complex(0,1)*propCorr**3)/(2.*cth*sth)',
                  order = {'NPprop':3,'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-((cth*ee*complex(0,1)*propCorr**3)/sth)',
                  order = {'NPprop':3,'QED':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '(-2*cth*ee**2*complex(0,1)*propCorr**3)/sth',
                  order = {'NPprop':3,'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '-(ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '(2*ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '-((ee*complex(0,1)*sth)/cth)',
                  order = {'QED':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-(dg1*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '-(dg1*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '(5*dg1*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '(-3*dg1*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = 'cth*dg1*ee*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-(dgw*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '(dgw*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '(cbBIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':2})

GC_292 = Coupling(name = 'GC_292',
                  value = '-((cbBRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'QED':2})

GC_293 = Coupling(name = 'GC_293',
                  value = '(cbWIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_294 = Coupling(name = 'GC_294',
                  value = '-((cbWRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '(ctBIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':2})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((ctBRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctB':1,'QED':2})

GC_297 = Coupling(name = 'GC_297',
                  value = '(-4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_298 = Coupling(name = 'GC_298',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_299 = Coupling(name = 'GC_299',
                  value = '(4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_300 = Coupling(name = 'GC_300',
                  value = '(-4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_301 = Coupling(name = 'GC_301',
                  value = '(4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_302 = Coupling(name = 'GC_302',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_303 = Coupling(name = 'GC_303',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '(4*cHWtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_305 = Coupling(name = 'GC_305',
                  value = '-((ctWIm*sth)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_306 = Coupling(name = 'GC_306',
                  value = '(ctWRe*complex(0,1)*sth)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_307 = Coupling(name = 'GC_307',
                  value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':2})

GC_308 = Coupling(name = 'GC_308',
                  value = '(2*cWtil*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':2})

GC_309 = Coupling(name = 'GC_309',
                  value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_310 = Coupling(name = 'GC_310',
                  value = '(2*cWtil*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':3})

GC_311 = Coupling(name = 'GC_311',
                  value = '(-12*cW*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_312 = Coupling(name = 'GC_312',
                  value = '(-4*cWtil*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcWtil':1,'QED':4})

GC_313 = Coupling(name = 'GC_313',
                  value = '-(ee*complex(0,1)*propCorr*sth)/(3.*cth)',
                  order = {'NPprop':1,'QED':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '(2*ee*complex(0,1)*propCorr*sth)/(3.*cth)',
                  order = {'NPprop':1,'QED':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-((ee*complex(0,1)*propCorr*sth)/cth)',
                  order = {'NPprop':1,'QED':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '(2*ee*complex(0,1)*propCorr**2*sth)/(3.*cth)',
                  order = {'NPprop':2,'QED':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '(2*ee*complex(0,1)*propCorr**3*sth)/(3.*cth)',
                  order = {'NPprop':3,'QED':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '(dgw*ee*complex(0,1)*sth**2)/3.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '(-2*dgw*ee*complex(0,1)*sth**2)/3.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-(dgw*ee*complex(0,1)*sth**2)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = 'dgw*ee*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '2*dgw*ee**2*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_323 = Coupling(name = 'GC_323',
                  value = '(4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_324 = Coupling(name = 'GC_324',
                  value = '(-2*cHBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':2})

GC_325 = Coupling(name = 'GC_325',
                  value = '(4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_326 = Coupling(name = 'GC_326',
                  value = '(-2*cHWtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_327 = Coupling(name = 'GC_327',
                  value = '(dg1*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '(-2*dg1*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(dg1*ee*complex(0,1)*sth**3)/cth',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '-(dgw*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(2*dgw*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '-((dgw*ee*complex(0,1)*sth**3)/cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-((cth*dgw*ee*complex(0,1))/sth) - cth*dgw*ee*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '(-2*cth*dg1*ee**2*complex(0,1))/sth + 4*cth*dg1*ee**2*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_335 = Coupling(name = 'GC_335',
                  value = '(-2*cth*dgw*ee**2*complex(0,1))/sth - 4*cth*dgw*ee**2*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_336 = Coupling(name = 'GC_336',
                  value = '(2*dgw*ee**2*complex(0,1))/sth**2 - 2*dgw*ee**2*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_337 = Coupling(name = 'GC_337',
                  value = '(-2*cHWB*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_338 = Coupling(name = 'GC_338',
                  value = '(-2*cHWBtil*complex(0,1))/LambdaSMEFT**2 + (4*cHWBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(4*complex(0,1)*gHaa)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(4*complex(0,1)*gHgg1)/vevhat',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '(-4*G*gHgg1)/vevhat',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(-4*complex(0,1)*G**2*gHgg1)/vevhat',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(2*complex(0,1)*gHza)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(-4*complex(0,1)*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '(-4*G*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '(4*complex(0,1)*G**2*gHgg2)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '(-6*gHgg3)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(-6*complex(0,1)*G*gHgg3)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '(-2*complex(0,1)*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(2*G*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '(-2*complex(0,1)*G**2*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(-8*complex(0,1)*G**2*gHgg4)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(complex(0,1)*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '(-2*G*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':3,'QED':1,'SMHLOOP':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '(2*complex(0,1)*G**2*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(6*complex(0,1)*G**2*gHgg5)/(MT**2*vevhat)',
                  order = {'QCD':4,'QED':1,'SMHLOOP':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(4*complex(0,1)*gHaa*propCorr)/vevhat',
                  order = {'NPprop':1,'QED':3,'SMHLOOP':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(4*complex(0,1)*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(-4*G*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(-4*complex(0,1)*G**2*gHgg1*propCorr)/vevhat',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '(2*complex(0,1)*gHza*propCorr)/vevhat',
                  order = {'NPprop':1,'QED':3,'SMHLOOP':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(-4*complex(0,1)*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(-4*G*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(4*complex(0,1)*G**2*gHgg2*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '(-6*gHgg3*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(-6*complex(0,1)*G*gHgg3*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-2*complex(0,1)*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '(2*G*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(-2*complex(0,1)*G**2*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(-8*complex(0,1)*G**2*gHgg4*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '(complex(0,1)*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':2,'QED':1,'SMHLOOP':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '(-2*G*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':3,'QED':1,'SMHLOOP':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '(2*complex(0,1)*G**2*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(6*complex(0,1)*G**2*gHgg5*propCorr)/(MT**2*vevhat)',
                  order = {'NPprop':1,'QCD':4,'QED':1,'SMHLOOP':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(2*complex(0,1)*gHza*propCorr**2)/vevhat',
                  order = {'NPprop':2,'QED':3,'SMHLOOP':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '-6*complex(0,1)*lam*vevhat',
                  order = {'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '3*dGf*complex(0,1)*lam*vevhat',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '-18*dkH*complex(0,1)*lam*vevhat',
                  order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '6*dMH2*complex(0,1)*lam*vevhat',
                  order = {'NP':1,'NPcH':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '-((cbGIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '(cbGRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '(-3*cbHIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1,'NPcpv':1,'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(3*cbHRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1,'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '-((cbWIm*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '(cbWIm*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(cbWRe*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '(90*cH*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(-2*cHGtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QED':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '(4*cHWtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '-((ctGIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QED':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '(ctGRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '-((cbBIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(cbBRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(cbWIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '-((cbWRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '-((ctBIm*cth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '(ctBRe*cth*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctB':1,'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(4*cHB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '(-2*cHBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '(4*cHW*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(-2*cHWtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '(-3*ctHIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1,'QED':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '(3*ctHRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1,'QED':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-((ctWIm*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '(ctWIm*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-((cth*ctWIm*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '(ctWRe*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '(cth*ctWRe*complex(0,1)*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '(cbWIm*ee*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((cbWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(cbWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '(-2*cHWBtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '(-4*cHWtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '-((ctWIm*ee*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '-((ctWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '(ctWRe*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(-4*cHW*ee**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cbGIm*complex(0,1)*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'NPcpv':1,'QCD':1,'QED':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cbGRe*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbG':1,'QCD':1,'QED':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '(4*cHGtil*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1,'QED':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '(ctGIm*complex(0,1)*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctG':1,'QCD':1,'QED':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '(ctGRe*G*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctG':1,'QCD':1,'QED':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '(-4*cHG*complex(0,1)*G**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '-6*complex(0,1)*lam*propCorr*vevhat',
                  order = {'NPprop':1,'QED':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '-6*complex(0,1)*lam*propCorr**2*vevhat',
                  order = {'NPprop':2,'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '-6*complex(0,1)*lam*propCorr**3*vevhat',
                  order = {'NPprop':3,'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*cth**2*sth**2)',
                  order = {'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(dGf*ee**2*complex(0,1)*vevhat)/(4.*sth**2)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(dgw*ee**2*complex(0,1)*vevhat)/sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '(dkH*ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '(dkH*ee**2*complex(0,1)*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '(4*cHW*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_441 = Coupling(name = 'GC_441',
                  value = '(3*cHDD*ee**2*complex(0,1)*vevhat)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':3})

GC_442 = Coupling(name = 'GC_442',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_443 = Coupling(name = 'GC_443',
                  value = '(ee**2*complex(0,1)*propCorr*vevhat)/(2.*sth**2)',
                  order = {'NPprop':1,'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '(ee**2*complex(0,1)*propCorr*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':1,'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(ee**2*complex(0,1)*propCorr**2*vevhat)/(2.*sth**2)',
                  order = {'NPprop':2,'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '(ee**2*complex(0,1)*propCorr**2*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':2,'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '(ee**2*complex(0,1)*propCorr**3*vevhat)/(2.*sth**2)',
                  order = {'NPprop':3,'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '(ee**2*complex(0,1)*propCorr**3*vevhat)/(2.*cth**2*sth**2)',
                  order = {'NPprop':3,'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '-((cbWIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(cbWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '-((cHj3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '-((cHl3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '-((cHtbIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(cHtbIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '(cHtbRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(cHbq*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '(cHd*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':2})

GC_459 = Coupling(name = 'GC_459',
                  value = '(cHe*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':2})

GC_460 = Coupling(name = 'GC_460',
                  value = '(cHj1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':2})

GC_461 = Coupling(name = 'GC_461',
                  value = '-((cHj3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_462 = Coupling(name = 'GC_462',
                  value = '(cHj3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':2})

GC_463 = Coupling(name = 'GC_463',
                  value = '(cHl1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':2})

GC_464 = Coupling(name = 'GC_464',
                  value = '-((cHl3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_465 = Coupling(name = 'GC_465',
                  value = '(cHl3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cHQ1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_468 = Coupling(name = 'GC_468',
                  value = '(cHQ3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':2})

GC_469 = Coupling(name = 'GC_469',
                  value = '(cHt*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '(cHu*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '-((cbWIm*cth*ee*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':2})

GC_472 = Coupling(name = 'GC_472',
                  value = '-((cbWRe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_473 = Coupling(name = 'GC_473',
                  value = '(cbWRe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcbW':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_476 = Coupling(name = 'GC_476',
                  value = '(2*cHWBtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':2})

GC_477 = Coupling(name = 'GC_477',
                  value = '(-4*cHWtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '(ctWIm*ee*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '(cth*ctWIm*ee*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-((ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((cth*ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_482 = Coupling(name = 'GC_482',
                  value = '(cth*ctWRe*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPctW':1,'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '(8*cHW*cth*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_484 = Coupling(name = 'GC_484',
                  value = '(cbBIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbB':1,'NPcpv':1,'QED':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((cbBRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbB':1,'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(cbWIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbW':1,'NPcpv':1,'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '-((cbWRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbW':1,'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ctBIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPctB':1,'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-((ctBRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPctB':1,'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(-4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '(-4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(4*cHWtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '-((ctWIm*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctW':1,'QED':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(ctWRe*complex(0,1)*sth*vevhat)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctW':1,'QED':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(-2*cHBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'NPcpv':1,'QED':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(-2*cHWtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '-((cbHIm*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcbH':1,'NPcpv':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '(cbHRe*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcbH':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(45*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '-((ctHIm*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPctH':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '(ctHRe*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPctH':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '-(cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-((cHWBtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '(-2*cHWtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '(cHWB*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '(2*cHGtil*G*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'NPcpv':1,'QCD':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '(3*cHDD*ee**2*complex(0,1)*vevhat**2)/(2.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_516 = Coupling(name = 'GC_516',
                  value = '-((cHj3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '-((cHl3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-((cHQ3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '-(cHtbIm*ee*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(cHtbIm*ee*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'NPcpv':1,'QED':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(cHtbRe*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHtb':1,'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '(cHbq*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHbq':1,'QED':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '(cHd*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '(cHe*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '(cHj1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj1':1,'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '-(cHj3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '(cHj3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHj3':1,'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(cHl1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '-(cHl3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(cHl3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(cHQ1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ1':1,'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '-(cHQ3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '(cHQ3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHQ3':1,'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(cHt*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHt':1,'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(cHu*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(cHWBtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(-2*cHWtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'NPcpv':1,'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '-((cHWB*cth**3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(cHWB*ee**2*complex(0,1)*vevhat**2)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '-(cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '(2*cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '-((cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(-2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_544 = Coupling(name = 'GC_544',
                  value = '(2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_545 = Coupling(name = 'GC_545',
                  value = '(cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(-2*cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '-((cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '(cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '(15*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':-1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(cHDD*ee**2*complex(0,1)*vevhat**3)/(2.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(cHWB*ee**2*complex(0,1)*vevhat**3)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '(dg1*ee**2*complex(0,1)*vevhat)/cth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcHDD':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_55200 = Coupling(name = 'GC_55200',
                  value = '(dGf*ee**2*complex(0,1)*vevhat)/(4.*cth**2*sth**2)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '(-2*cHWB*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(-2*cHWBtil*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'NPcpv':1,'QED':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(2*cHWB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (4*cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_556 = Coupling(name = 'GC_556',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '(dGf*complex(0,1)*yb)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '-((complex(0,1)*propCorr*yb)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(dGf*complex(0,1)*yc)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '-((cjQtu1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_564 = Coupling(name = 'GC_564',
                  value = '(cjQtu1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_565 = Coupling(name = 'GC_565',
                  value = '(cjQtu1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu1':1,'QED':3})

GC_566 = Coupling(name = 'GC_566',
                  value = '-((cjQtu8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_567 = Coupling(name = 'GC_567',
                  value = '(cjQtu8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_568 = Coupling(name = 'GC_568',
                  value = '(cjQtu8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQtu8':1,'QED':3})

GC_569 = Coupling(name = 'GC_569',
                  value = '-((cjuQb1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_570 = Coupling(name = 'GC_570',
                  value = '(cjuQb1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_571 = Coupling(name = 'GC_571',
                  value = '-((cjuQb1Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_572 = Coupling(name = 'GC_572',
                  value = '(cjuQb1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_573 = Coupling(name = 'GC_573',
                  value = '-((cjuQb8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_574 = Coupling(name = 'GC_574',
                  value = '(cjuQb8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_575 = Coupling(name = 'GC_575',
                  value = '-((cjuQb8Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_576 = Coupling(name = 'GC_576',
                  value = '(cjuQb8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_577 = Coupling(name = 'GC_577',
                  value = '-((cQujb1Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_578 = Coupling(name = 'GC_578',
                  value = '(cQujb1Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_579 = Coupling(name = 'GC_579',
                  value = '-((cQujb1Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_580 = Coupling(name = 'GC_580',
                  value = '(cQujb1Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_581 = Coupling(name = 'GC_581',
                  value = '-((cQujb8Im*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_582 = Coupling(name = 'GC_582',
                  value = '(cQujb8Im*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_583 = Coupling(name = 'GC_583',
                  value = '-((cQujb8Re*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_584 = Coupling(name = 'GC_584',
                  value = '(cQujb8Re*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_585 = Coupling(name = 'GC_585',
                  value = '-((cth*cuBIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_586 = Coupling(name = 'GC_586',
                  value = '(cth*cuBRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_587 = Coupling(name = 'GC_587',
                  value = '-((cuGIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':3})

GC_588 = Coupling(name = 'GC_588',
                  value = '(cuGRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':3})

GC_589 = Coupling(name = 'GC_589',
                  value = '(-3*cuHIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':3})

GC_590 = Coupling(name = 'GC_590',
                  value = '(3*cuHRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':3})

GC_591 = Coupling(name = 'GC_591',
                  value = '-((cuWIm*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_592 = Coupling(name = 'GC_592',
                  value = '(cuWIm*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_593 = Coupling(name = 'GC_593',
                  value = '-((cth*cuWIm*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_594 = Coupling(name = 'GC_594',
                  value = '(cuWRe*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_595 = Coupling(name = 'GC_595',
                  value = '(cth*cuWRe*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_596 = Coupling(name = 'GC_596',
                  value = '-((cuWIm*ee*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_597 = Coupling(name = 'GC_597',
                  value = '-((cuWRe*ee*complex(0,1)*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_598 = Coupling(name = 'GC_598',
                  value = '(cuWRe*ee*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_599 = Coupling(name = 'GC_599',
                  value = '(cuGIm*complex(0,1)*G*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':3})

GC_600 = Coupling(name = 'GC_600',
                  value = '(cuGRe*G*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_601 = Coupling(name = 'GC_601',
                  value = '-((complex(0,1)*propCorr*yc)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = '(cuWIm*ee*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_603 = Coupling(name = 'GC_603',
                  value = '(cth*cuWIm*ee*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_604 = Coupling(name = 'GC_604',
                  value = '-((cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_605 = Coupling(name = 'GC_605',
                  value = '-((cth*cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_606 = Coupling(name = 'GC_606',
                  value = '(cth*cuWRe*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_607 = Coupling(name = 'GC_607',
                  value = '(cuBIm*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_608 = Coupling(name = 'GC_608',
                  value = '-((cuBRe*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_609 = Coupling(name = 'GC_609',
                  value = '-((cuWIm*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_610 = Coupling(name = 'GC_610',
                  value = '(cuWRe*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_611 = Coupling(name = 'GC_611',
                  value = '-((cth*cuBIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_612 = Coupling(name = 'GC_612',
                  value = '(cth*cuBRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_613 = Coupling(name = 'GC_613',
                  value = '-((cuGIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':2})

GC_614 = Coupling(name = 'GC_614',
                  value = '(cuGRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':2})

GC_615 = Coupling(name = 'GC_615',
                  value = '(-3*cuHIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':2})

GC_616 = Coupling(name = 'GC_616',
                  value = '(3*cuHRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':2})

GC_617 = Coupling(name = 'GC_617',
                  value = '-((cuWIm*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_618 = Coupling(name = 'GC_618',
                  value = '(cuWIm*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_619 = Coupling(name = 'GC_619',
                  value = '-((cth*cuWIm*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_620 = Coupling(name = 'GC_620',
                  value = '(cuWRe*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '(cth*cuWRe*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '-((cuWIm*ee*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_623 = Coupling(name = 'GC_623',
                  value = '-((cuWRe*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_624 = Coupling(name = 'GC_624',
                  value = '(cuWRe*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_625 = Coupling(name = 'GC_625',
                  value = '(cuGIm*complex(0,1)*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':2})

GC_626 = Coupling(name = 'GC_626',
                  value = '(cuGRe*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_627 = Coupling(name = 'GC_627',
                  value = '(cuWIm*ee*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_628 = Coupling(name = 'GC_628',
                  value = '(cth*cuWIm*ee*vevhat*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_629 = Coupling(name = 'GC_629',
                  value = '-((cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_630 = Coupling(name = 'GC_630',
                  value = '-((cth*cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_631 = Coupling(name = 'GC_631',
                  value = '(cth*cuWRe*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_632 = Coupling(name = 'GC_632',
                  value = '(cuBIm*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_633 = Coupling(name = 'GC_633',
                  value = '-((cuBRe*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '-((cuWIm*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_635 = Coupling(name = 'GC_635',
                  value = '(cuWRe*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_636 = Coupling(name = 'GC_636',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '-((cuHIm*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '(cuHRe*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_641 = Coupling(name = 'GC_641',
                  value = '(dGf*complex(0,1)*ydo)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-((cdGIm*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':3})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cdGRe*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_644 = Coupling(name = 'GC_644',
                  value = '(-3*cdHIm*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':3})

GC_645 = Coupling(name = 'GC_645',
                  value = '(3*cdHRe*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_646 = Coupling(name = 'GC_646',
                  value = '-((cdWIm*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_647 = Coupling(name = 'GC_647',
                  value = '(cdWIm*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_648 = Coupling(name = 'GC_648',
                  value = '(cdWRe*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_649 = Coupling(name = 'GC_649',
                  value = '-((cjQbd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_650 = Coupling(name = 'GC_650',
                  value = '(cjQbd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_651 = Coupling(name = 'GC_651',
                  value = '(cjQbd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'QED':3})

GC_652 = Coupling(name = 'GC_652',
                  value = '-((cjQbd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_653 = Coupling(name = 'GC_653',
                  value = '(cjQbd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_654 = Coupling(name = 'GC_654',
                  value = '(cjQbd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'QED':3})

GC_655 = Coupling(name = 'GC_655',
                  value = '-((cjtQd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_656 = Coupling(name = 'GC_656',
                  value = '(cjtQd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_657 = Coupling(name = 'GC_657',
                  value = '-((cjtQd1Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_658 = Coupling(name = 'GC_658',
                  value = '(cjtQd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_659 = Coupling(name = 'GC_659',
                  value = '-((cjtQd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cjtQd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_661 = Coupling(name = 'GC_661',
                  value = '-((cjtQd8Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cjtQd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_663 = Coupling(name = 'GC_663',
                  value = '-((cQtjd1Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cQtjd1Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_665 = Coupling(name = 'GC_665',
                  value = '-((cQtjd1Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_666 = Coupling(name = 'GC_666',
                  value = '(cQtjd1Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_667 = Coupling(name = 'GC_667',
                  value = '-((cQtjd8Im*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cQtjd8Im*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_669 = Coupling(name = 'GC_669',
                  value = '-((cQtjd8Re*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cQtjd8Re*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_671 = Coupling(name = 'GC_671',
                  value = '-((cdBIm*cth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cdBRe*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cdWIm*cth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_674 = Coupling(name = 'GC_674',
                  value = '-((cdWRe*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cdWIm*ee*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_676 = Coupling(name = 'GC_676',
                  value = '-((cdWRe*ee*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_677 = Coupling(name = 'GC_677',
                  value = '(cdWRe*ee*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cdGIm*complex(0,1)*G*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':3})

GC_679 = Coupling(name = 'GC_679',
                  value = '(cdGRe*G*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_680 = Coupling(name = 'GC_680',
                  value = '-((complex(0,1)*propCorr*ydo)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '-((cdWIm*ee*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_682 = Coupling(name = 'GC_682',
                  value = '(cdWRe*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_683 = Coupling(name = 'GC_683',
                  value = '-((cdWIm*cth*ee*ydo)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_684 = Coupling(name = 'GC_684',
                  value = '-((cdWRe*cth*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_685 = Coupling(name = 'GC_685',
                  value = '(cdWRe*cth*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_686 = Coupling(name = 'GC_686',
                  value = '(cdBIm*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_687 = Coupling(name = 'GC_687',
                  value = '-((cdBRe*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_688 = Coupling(name = 'GC_688',
                  value = '(cdWIm*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_689 = Coupling(name = 'GC_689',
                  value = '-((cdWRe*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_690 = Coupling(name = 'GC_690',
                  value = '-((cdGIm*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':2})

GC_691 = Coupling(name = 'GC_691',
                  value = '(cdGRe*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_692 = Coupling(name = 'GC_692',
                  value = '(-3*cdHIm*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':2})

GC_693 = Coupling(name = 'GC_693',
                  value = '(3*cdHRe*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_694 = Coupling(name = 'GC_694',
                  value = '-((cdWIm*vevhat*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(cdWIm*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_696 = Coupling(name = 'GC_696',
                  value = '(cdWRe*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_697 = Coupling(name = 'GC_697',
                  value = '-((cdBIm*cth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_698 = Coupling(name = 'GC_698',
                  value = '(cdBRe*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_699 = Coupling(name = 'GC_699',
                  value = '(cdWIm*cth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '-((cdWRe*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_701 = Coupling(name = 'GC_701',
                  value = '(cdWIm*ee*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_702 = Coupling(name = 'GC_702',
                  value = '-((cdWRe*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_703 = Coupling(name = 'GC_703',
                  value = '(cdWRe*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_704 = Coupling(name = 'GC_704',
                  value = '(cdGIm*complex(0,1)*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '(cdGRe*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_706 = Coupling(name = 'GC_706',
                  value = '-((cdWIm*ee*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_707 = Coupling(name = 'GC_707',
                  value = '(cdWRe*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_708 = Coupling(name = 'GC_708',
                  value = '-((cdWIm*cth*ee*vevhat*ydo)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_709 = Coupling(name = 'GC_709',
                  value = '-((cdWRe*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_710 = Coupling(name = 'GC_710',
                  value = '(cdWRe*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_711 = Coupling(name = 'GC_711',
                  value = '(cdBIm*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '-((cdBRe*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '(cdWIm*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '-((cdWRe*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '-((cdHIm*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':1})

GC_716 = Coupling(name = 'GC_716',
                  value = '(cdHRe*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_717 = Coupling(name = 'GC_717',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_718 = Coupling(name = 'GC_718',
                  value = '(cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_719 = Coupling(name = 'GC_719',
                  value = '-((cjujd11Im*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_720 = Coupling(name = 'GC_720',
                  value = '(cjujd11Im*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_721 = Coupling(name = 'GC_721',
                  value = '-((cjujd11Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_722 = Coupling(name = 'GC_722',
                  value = '(cjujd11Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_723 = Coupling(name = 'GC_723',
                  value = '-((cjujd1Im*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_724 = Coupling(name = 'GC_724',
                  value = '(cjujd1Im*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_725 = Coupling(name = 'GC_725',
                  value = '-((cjujd1Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_726 = Coupling(name = 'GC_726',
                  value = '(cjujd1Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_727 = Coupling(name = 'GC_727',
                  value = '-((cjujd81Im*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_728 = Coupling(name = 'GC_728',
                  value = '(cjujd81Im*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_729 = Coupling(name = 'GC_729',
                  value = '-((cjujd81Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_730 = Coupling(name = 'GC_730',
                  value = '(cjujd81Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_731 = Coupling(name = 'GC_731',
                  value = '-((cjujd8Im*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_732 = Coupling(name = 'GC_732',
                  value = '(cjujd8Im*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((cjujd8Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_734 = Coupling(name = 'GC_734',
                  value = '(cjujd8Re*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_735 = Coupling(name = 'GC_735',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_736 = Coupling(name = 'GC_736',
                  value = '(dGf*complex(0,1)*ye)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_737 = Coupling(name = 'GC_737',
                  value = '(-3*ceHIm*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':3})

GC_738 = Coupling(name = 'GC_738',
                  value = '(3*ceHRe*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':3})

GC_739 = Coupling(name = 'GC_739',
                  value = '-((ceWIm*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_740 = Coupling(name = 'GC_740',
                  value = '(ceWIm*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_741 = Coupling(name = 'GC_741',
                  value = '(ceWRe*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_742 = Coupling(name = 'GC_742',
                  value = '-((clebQIm*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_743 = Coupling(name = 'GC_743',
                  value = '(clebQIm*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_744 = Coupling(name = 'GC_744',
                  value = '(clebQRe*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'QED':3})

GC_745 = Coupling(name = 'GC_745',
                  value = '-((cleQt1Im*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_746 = Coupling(name = 'GC_746',
                  value = '(cleQt1Im*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_747 = Coupling(name = 'GC_747',
                  value = '-((cleQt1Re*complex(0,1)*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_748 = Coupling(name = 'GC_748',
                  value = '(cleQt1Re*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_749 = Coupling(name = 'GC_749',
                  value = '-(cleQt3Im*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_750 = Coupling(name = 'GC_750',
                  value = '-(cleQt3Im*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cleQt3Im*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_752 = Coupling(name = 'GC_752',
                  value = '(cleQt3Im*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_753 = Coupling(name = 'GC_753',
                  value = '-(cleQt3Re*complex(0,1)*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_754 = Coupling(name = 'GC_754',
                  value = '(cleQt3Re*complex(0,1)*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_755 = Coupling(name = 'GC_755',
                  value = '-(cleQt3Re*complex(0,1)*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_756 = Coupling(name = 'GC_756',
                  value = '(cleQt3Re*complex(0,1)*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_757 = Coupling(name = 'GC_757',
                  value = '-((ceBIm*cth*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_758 = Coupling(name = 'GC_758',
                  value = '(ceBRe*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_759 = Coupling(name = 'GC_759',
                  value = '(ceWIm*cth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_760 = Coupling(name = 'GC_760',
                  value = '-((ceWRe*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_761 = Coupling(name = 'GC_761',
                  value = '(ceWIm*ee*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_762 = Coupling(name = 'GC_762',
                  value = '-((ceWRe*ee*complex(0,1)*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_763 = Coupling(name = 'GC_763',
                  value = '(ceWRe*ee*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_764 = Coupling(name = 'GC_764',
                  value = '-((complex(0,1)*propCorr*ye)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_765 = Coupling(name = 'GC_765',
                  value = '-((ceWIm*ee*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_766 = Coupling(name = 'GC_766',
                  value = '(ceWRe*ee*complex(0,1)*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_767 = Coupling(name = 'GC_767',
                  value = '-((ceWIm*cth*ee*ye)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_768 = Coupling(name = 'GC_768',
                  value = '-((ceWRe*cth*ee*complex(0,1)*ye)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_769 = Coupling(name = 'GC_769',
                  value = '(ceWRe*cth*ee*complex(0,1)*ye)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_770 = Coupling(name = 'GC_770',
                  value = '(ceBIm*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_771 = Coupling(name = 'GC_771',
                  value = '-((ceBRe*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_772 = Coupling(name = 'GC_772',
                  value = '(ceWIm*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_773 = Coupling(name = 'GC_773',
                  value = '-((ceWRe*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_774 = Coupling(name = 'GC_774',
                  value = '(-3*ceHIm*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '(3*ceHRe*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '-((ceWIm*vevhat*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '(ceWIm*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '(ceWRe*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '-((ceBIm*cth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_780 = Coupling(name = 'GC_780',
                  value = '(ceBRe*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '(ceWIm*cth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_782 = Coupling(name = 'GC_782',
                  value = '-((ceWRe*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_783 = Coupling(name = 'GC_783',
                  value = '(ceWIm*ee*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_784 = Coupling(name = 'GC_784',
                  value = '-((ceWRe*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_785 = Coupling(name = 'GC_785',
                  value = '(ceWRe*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_786 = Coupling(name = 'GC_786',
                  value = '-((ceWIm*ee*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_787 = Coupling(name = 'GC_787',
                  value = '(ceWRe*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_788 = Coupling(name = 'GC_788',
                  value = '-((ceWIm*cth*ee*vevhat*ye)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_789 = Coupling(name = 'GC_789',
                  value = '-((ceWRe*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_790 = Coupling(name = 'GC_790',
                  value = '(ceWRe*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_791 = Coupling(name = 'GC_791',
                  value = '(ceBIm*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_792 = Coupling(name = 'GC_792',
                  value = '-((ceBRe*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_793 = Coupling(name = 'GC_793',
                  value = '(ceWIm*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_794 = Coupling(name = 'GC_794',
                  value = '-((ceWRe*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_795 = Coupling(name = 'GC_795',
                  value = '-((ceHIm*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_796 = Coupling(name = 'GC_796',
                  value = '(ceHRe*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_797 = Coupling(name = 'GC_797',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_798 = Coupling(name = 'GC_798',
                  value = '(cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_799 = Coupling(name = 'GC_799',
                  value = '-((cleju1Im*yc*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_800 = Coupling(name = 'GC_800',
                  value = '(cleju1Im*yc*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_801 = Coupling(name = 'GC_801',
                  value = '-((cleju1Re*complex(0,1)*yc*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'QED':4})

GC_802 = Coupling(name = 'GC_802',
                  value = '(cleju1Re*complex(0,1)*yc*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'QED':4})

GC_803 = Coupling(name = 'GC_803',
                  value = '-(cleju3Im*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_804 = Coupling(name = 'GC_804',
                  value = '-(cleju3Im*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cleju3Im*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_806 = Coupling(name = 'GC_806',
                  value = '(cleju3Im*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_807 = Coupling(name = 'GC_807',
                  value = '-(cleju3Re*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_808 = Coupling(name = 'GC_808',
                  value = '(cleju3Re*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_809 = Coupling(name = 'GC_809',
                  value = '-(cleju3Re*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_810 = Coupling(name = 'GC_810',
                  value = '(cleju3Re*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_811 = Coupling(name = 'GC_811',
                  value = '-((cledjIm*ydo*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_812 = Coupling(name = 'GC_812',
                  value = '(cledjIm*ydo*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_813 = Coupling(name = 'GC_813',
                  value = '(cledjRe*complex(0,1)*ydo*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'QED':4})

GC_814 = Coupling(name = 'GC_814',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_815 = Coupling(name = 'GC_815',
                  value = '(dGf*complex(0,1)*ym)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_816 = Coupling(name = 'GC_816',
                  value = '(-3*ceHIm*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':3})

GC_817 = Coupling(name = 'GC_817',
                  value = '(3*ceHRe*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':3})

GC_818 = Coupling(name = 'GC_818',
                  value = '-((ceWIm*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_819 = Coupling(name = 'GC_819',
                  value = '(ceWIm*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_820 = Coupling(name = 'GC_820',
                  value = '(ceWRe*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_821 = Coupling(name = 'GC_821',
                  value = '-((clebQIm*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_822 = Coupling(name = 'GC_822',
                  value = '(clebQIm*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_823 = Coupling(name = 'GC_823',
                  value = '(clebQRe*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclebQ':1,'QED':3})

GC_824 = Coupling(name = 'GC_824',
                  value = '-((cleQt1Im*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_825 = Coupling(name = 'GC_825',
                  value = '(cleQt1Im*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_826 = Coupling(name = 'GC_826',
                  value = '-((cleQt1Re*complex(0,1)*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_827 = Coupling(name = 'GC_827',
                  value = '(cleQt1Re*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_828 = Coupling(name = 'GC_828',
                  value = '-(cleQt3Im*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_829 = Coupling(name = 'GC_829',
                  value = '-(cleQt3Im*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_830 = Coupling(name = 'GC_830',
                  value = '(cleQt3Im*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_831 = Coupling(name = 'GC_831',
                  value = '(cleQt3Im*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_832 = Coupling(name = 'GC_832',
                  value = '-(cleQt3Re*complex(0,1)*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_833 = Coupling(name = 'GC_833',
                  value = '(cleQt3Re*complex(0,1)*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_834 = Coupling(name = 'GC_834',
                  value = '-(cleQt3Re*complex(0,1)*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_835 = Coupling(name = 'GC_835',
                  value = '(cleQt3Re*complex(0,1)*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_836 = Coupling(name = 'GC_836',
                  value = '-((ceBIm*cth*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_837 = Coupling(name = 'GC_837',
                  value = '(ceBRe*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_838 = Coupling(name = 'GC_838',
                  value = '(ceWIm*cth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_839 = Coupling(name = 'GC_839',
                  value = '-((ceWRe*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_840 = Coupling(name = 'GC_840',
                  value = '(ceWIm*ee*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_841 = Coupling(name = 'GC_841',
                  value = '-((ceWRe*ee*complex(0,1)*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_842 = Coupling(name = 'GC_842',
                  value = '(ceWRe*ee*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_843 = Coupling(name = 'GC_843',
                  value = '-((complex(0,1)*propCorr*ym)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_844 = Coupling(name = 'GC_844',
                  value = '-((ceWIm*ee*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_845 = Coupling(name = 'GC_845',
                  value = '(ceWRe*ee*complex(0,1)*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_846 = Coupling(name = 'GC_846',
                  value = '-((ceWIm*cth*ee*ym)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_847 = Coupling(name = 'GC_847',
                  value = '-((ceWRe*cth*ee*complex(0,1)*ym)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_848 = Coupling(name = 'GC_848',
                  value = '(ceWRe*cth*ee*complex(0,1)*ym)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_849 = Coupling(name = 'GC_849',
                  value = '(ceBIm*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_850 = Coupling(name = 'GC_850',
                  value = '-((ceBRe*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_851 = Coupling(name = 'GC_851',
                  value = '(ceWIm*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_852 = Coupling(name = 'GC_852',
                  value = '-((ceWRe*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_853 = Coupling(name = 'GC_853',
                  value = '(-3*ceHIm*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_854 = Coupling(name = 'GC_854',
                  value = '(3*ceHRe*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':2})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((ceWIm*vevhat*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_856 = Coupling(name = 'GC_856',
                  value = '(ceWIm*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(ceWRe*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '-((ceBIm*cth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '(ceBRe*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '(ceWIm*cth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_861 = Coupling(name = 'GC_861',
                  value = '-((ceWRe*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_862 = Coupling(name = 'GC_862',
                  value = '(ceWIm*ee*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((ceWRe*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_864 = Coupling(name = 'GC_864',
                  value = '(ceWRe*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_865 = Coupling(name = 'GC_865',
                  value = '-((ceWIm*ee*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_866 = Coupling(name = 'GC_866',
                  value = '(ceWRe*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_867 = Coupling(name = 'GC_867',
                  value = '-((ceWIm*cth*ee*vevhat*ym)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_868 = Coupling(name = 'GC_868',
                  value = '-((ceWRe*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_869 = Coupling(name = 'GC_869',
                  value = '(ceWRe*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_870 = Coupling(name = 'GC_870',
                  value = '(ceBIm*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_871 = Coupling(name = 'GC_871',
                  value = '-((ceBRe*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_872 = Coupling(name = 'GC_872',
                  value = '(ceWIm*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_873 = Coupling(name = 'GC_873',
                  value = '-((ceWRe*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_874 = Coupling(name = 'GC_874',
                  value = '-((ceHIm*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_875 = Coupling(name = 'GC_875',
                  value = '(ceHRe*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_876 = Coupling(name = 'GC_876',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_877 = Coupling(name = 'GC_877',
                  value = '(cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '-((cleju1Im*yc*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cleju1Im*yc*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_880 = Coupling(name = 'GC_880',
                  value = '-((cleju1Re*complex(0,1)*yc*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju1':1,'QED':4})

GC_881 = Coupling(name = 'GC_881',
                  value = '(cleju1Re*complex(0,1)*yc*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcleju1':1,'QED':4})

GC_882 = Coupling(name = 'GC_882',
                  value = '-(cleju3Im*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_883 = Coupling(name = 'GC_883',
                  value = '-(cleju3Im*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cleju3Im*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_885 = Coupling(name = 'GC_885',
                  value = '(cleju3Im*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_886 = Coupling(name = 'GC_886',
                  value = '-(cleju3Re*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_887 = Coupling(name = 'GC_887',
                  value = '(cleju3Re*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_888 = Coupling(name = 'GC_888',
                  value = '-(cleju3Re*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_889 = Coupling(name = 'GC_889',
                  value = '(cleju3Re*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcleju3':1,'QED':4})

GC_890 = Coupling(name = 'GC_890',
                  value = '-((cledjIm*ydo*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_891 = Coupling(name = 'GC_891',
                  value = '(cledjIm*ydo*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_892 = Coupling(name = 'GC_892',
                  value = '(cledjRe*complex(0,1)*ydo*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledj':1,'QED':4})

GC_893 = Coupling(name = 'GC_893',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_894 = Coupling(name = 'GC_894',
                  value = '(dGf*complex(0,1)*ys)/(2.*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_895 = Coupling(name = 'GC_895',
                  value = '-((cdGIm*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':3})

GC_896 = Coupling(name = 'GC_896',
                  value = '(cdGRe*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_897 = Coupling(name = 'GC_897',
                  value = '(-3*cdHIm*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':3})

GC_898 = Coupling(name = 'GC_898',
                  value = '(3*cdHRe*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_899 = Coupling(name = 'GC_899',
                  value = '-((cdWIm*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_900 = Coupling(name = 'GC_900',
                  value = '(cdWIm*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_901 = Coupling(name = 'GC_901',
                  value = '(cdWRe*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_902 = Coupling(name = 'GC_902',
                  value = '-((cjQbd1Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_903 = Coupling(name = 'GC_903',
                  value = '(cjQbd1Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'NPcpv':1,'QED':3})

GC_904 = Coupling(name = 'GC_904',
                  value = '(cjQbd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd1':1,'QED':3})

GC_905 = Coupling(name = 'GC_905',
                  value = '-((cjQbd8Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_906 = Coupling(name = 'GC_906',
                  value = '(cjQbd8Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'NPcpv':1,'QED':3})

GC_907 = Coupling(name = 'GC_907',
                  value = '(cjQbd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjQbd8':1,'QED':3})

GC_908 = Coupling(name = 'GC_908',
                  value = '-((cjtQd1Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_909 = Coupling(name = 'GC_909',
                  value = '(cjtQd1Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'NPcpv':1,'QED':3})

GC_910 = Coupling(name = 'GC_910',
                  value = '-((cjtQd1Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cjtQd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd1':1,'QED':3})

GC_912 = Coupling(name = 'GC_912',
                  value = '-((cjtQd8Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_913 = Coupling(name = 'GC_913',
                  value = '(cjtQd8Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'NPcpv':1,'QED':3})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((cjtQd8Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_915 = Coupling(name = 'GC_915',
                  value = '(cjtQd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjtQd8':1,'QED':3})

GC_916 = Coupling(name = 'GC_916',
                  value = '-((cQtjd1Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_917 = Coupling(name = 'GC_917',
                  value = '(cQtjd1Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd1':1,'QED':3})

GC_918 = Coupling(name = 'GC_918',
                  value = '-((cQtjd1Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_919 = Coupling(name = 'GC_919',
                  value = '(cQtjd1Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd1':1,'QED':3})

GC_920 = Coupling(name = 'GC_920',
                  value = '-((cQtjd8Im*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_921 = Coupling(name = 'GC_921',
                  value = '(cQtjd8Im*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcQtjd8':1,'QED':3})

GC_922 = Coupling(name = 'GC_922',
                  value = '-((cQtjd8Re*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_923 = Coupling(name = 'GC_923',
                  value = '(cQtjd8Re*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcQtjd8':1,'QED':3})

GC_924 = Coupling(name = 'GC_924',
                  value = '-((cdBIm*cth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_925 = Coupling(name = 'GC_925',
                  value = '(cdBRe*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_926 = Coupling(name = 'GC_926',
                  value = '(cdWIm*cth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_927 = Coupling(name = 'GC_927',
                  value = '-((cdWRe*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_928 = Coupling(name = 'GC_928',
                  value = '(cdWIm*ee*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_929 = Coupling(name = 'GC_929',
                  value = '-((cdWRe*ee*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_930 = Coupling(name = 'GC_930',
                  value = '(cdWRe*ee*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_931 = Coupling(name = 'GC_931',
                  value = '(cdGIm*complex(0,1)*G*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':3})

GC_932 = Coupling(name = 'GC_932',
                  value = '(cdGRe*G*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_933 = Coupling(name = 'GC_933',
                  value = '-((complex(0,1)*propCorr*ys)/cmath.sqrt(2))',
                  order = {'NPprop':1,'QED':1})

GC_934 = Coupling(name = 'GC_934',
                  value = '-((cdWIm*ee*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_935 = Coupling(name = 'GC_935',
                  value = '(cdWRe*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_936 = Coupling(name = 'GC_936',
                  value = '-((cdWIm*cth*ee*ys)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':4})

GC_937 = Coupling(name = 'GC_937',
                  value = '-((cdWRe*cth*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_938 = Coupling(name = 'GC_938',
                  value = '(cdWRe*cth*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_939 = Coupling(name = 'GC_939',
                  value = '(cdBIm*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':3})

GC_940 = Coupling(name = 'GC_940',
                  value = '-((cdBRe*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_941 = Coupling(name = 'GC_941',
                  value = '(cdWIm*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_942 = Coupling(name = 'GC_942',
                  value = '-((cdWRe*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_943 = Coupling(name = 'GC_943',
                  value = '-((cdGIm*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '(cdGRe*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_945 = Coupling(name = 'GC_945',
                  value = '(-3*cdHIm*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':2})

GC_946 = Coupling(name = 'GC_946',
                  value = '(3*cdHRe*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((cdWIm*vevhat*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '(cdWIm*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_949 = Coupling(name = 'GC_949',
                  value = '(cdWRe*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((cdBIm*cth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '(cdBRe*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '(cdWIm*cth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_953 = Coupling(name = 'GC_953',
                  value = '-((cdWRe*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_954 = Coupling(name = 'GC_954',
                  value = '(cdWIm*ee*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((cdWRe*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_956 = Coupling(name = 'GC_956',
                  value = '(cdWRe*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_957 = Coupling(name = 'GC_957',
                  value = '(cdGIm*complex(0,1)*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'NPcpv':1,'QCD':1,'QED':2})

GC_958 = Coupling(name = 'GC_958',
                  value = '(cdGRe*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_959 = Coupling(name = 'GC_959',
                  value = '-((cdWIm*ee*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_960 = Coupling(name = 'GC_960',
                  value = '(cdWRe*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_961 = Coupling(name = 'GC_961',
                  value = '-((cdWIm*cth*ee*vevhat*ys)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':3})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((cdWRe*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_963 = Coupling(name = 'GC_963',
                  value = '(cdWRe*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_964 = Coupling(name = 'GC_964',
                  value = '(cdBIm*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'NPcpv':1,'QED':2})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((cdBRe*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_966 = Coupling(name = 'GC_966',
                  value = '(cdWIm*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'NPcpv':1,'QED':2})

GC_967 = Coupling(name = 'GC_967',
                  value = '-((cdWRe*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((cdHIm*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdH':1,'NPcpv':1,'QED':1})

GC_969 = Coupling(name = 'GC_969',
                  value = '(cdHRe*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_971 = Coupling(name = 'GC_971',
                  value = '(cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((cjujd11Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_973 = Coupling(name = 'GC_973',
                  value = '(cjujd11Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((cjujd11Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_975 = Coupling(name = 'GC_975',
                  value = '(cjujd11Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((cjujd1Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_977 = Coupling(name = 'GC_977',
                  value = '(cjujd1Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((cjujd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_979 = Coupling(name = 'GC_979',
                  value = '(cjujd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((cjujd81Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_981 = Coupling(name = 'GC_981',
                  value = '(cjujd81Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((cjujd81Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_983 = Coupling(name = 'GC_983',
                  value = '(cjujd81Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((cjujd8Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_985 = Coupling(name = 'GC_985',
                  value = '(cjujd8Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((cjujd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_987 = Coupling(name = 'GC_987',
                  value = '(cjujd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_988 = Coupling(name = 'GC_988',
                  value = '-((cutbd1Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_989 = Coupling(name = 'GC_989',
                  value = '(cutbd1Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_990 = Coupling(name = 'GC_990',
                  value = '(cutbd1Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcutbd1':1,'QED':4})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((cutbd8Im*yc*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_992 = Coupling(name = 'GC_992',
                  value = '(cutbd8Im*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_993 = Coupling(name = 'GC_993',
                  value = '(cutbd8Re*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcutbd8':1,'QED':4})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((cHudIm*ee*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_995 = Coupling(name = 'GC_995',
                  value = '(cHudIm*ee*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_996 = Coupling(name = 'GC_996',
                  value = '(cHudRe*ee*complex(0,1)*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_997 = Coupling(name = 'GC_997',
                  value = '-((cHudIm*ee*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_998 = Coupling(name = 'GC_998',
                  value = '(cHudIm*ee*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_999 = Coupling(name = 'GC_999',
                  value = '(cHudRe*ee*complex(0,1)*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '-(cHudIm*ee*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(cHudIm*ee*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '(cHudRe*ee*complex(0,1)*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((cledjIm*ye*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '(cledjIm*ye*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(cledjRe*complex(0,1)*ye*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':4})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((cledjIm*ym*ys)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(cledjIm*ym*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '(cledjRe*complex(0,1)*ym*ys)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':4})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(dGf*complex(0,1)*yt)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((complex(0,1)*propCorr*yt)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((complex(0,1)*propCorr**2*yt)/cmath.sqrt(2))',
                   order = {'NPprop':2,'QED':1})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-((complex(0,1)*propCorr**3*yt)/cmath.sqrt(2))',
                   order = {'NPprop':3,'QED':1})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-((cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(dGf*complex(0,1)*ytau)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(-3*ceHIm*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':3})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(3*ceHRe*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':3})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '-((ceWIm*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(ceWIm*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(ceWRe*complex(0,1)*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '-((clebQIm*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(clebQIm*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPclebQ':1,'NPcpv':1,'QED':3})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(clebQRe*complex(0,1)*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPclebQ':1,'QED':3})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((cleQt1Im*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(cleQt1Im*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleQt1':1,'NPcpv':1,'QED':3})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((cleQt1Re*complex(0,1)*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '(cleQt1Re*complex(0,1)*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleQt1':1,'QED':3})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-(cleQt3Im*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-(cleQt3Im*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(cleQt3Im*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(cleQt3Im*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'NPcpv':1,'QED':3})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-(cleQt3Re*complex(0,1)*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '(cleQt3Re*complex(0,1)*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-(cleQt3Re*complex(0,1)*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '(cleQt3Re*complex(0,1)*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleQt3':1,'QED':3})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((ceBIm*cth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(ceBRe*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '(ceWIm*cth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((ceWRe*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '(ceWIm*ee*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((ceWRe*ee*complex(0,1)*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(ceWRe*ee*complex(0,1)*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-((complex(0,1)*propCorr*ytau)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((ceWIm*ee*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '(ceWRe*ee*complex(0,1)*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-((ceWIm*cth*ee*ytau)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':4})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-((ceWRe*cth*ee*complex(0,1)*ytau)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(ceWRe*cth*ee*complex(0,1)*ytau)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(ceBIm*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':3})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((ceBRe*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '(ceWIm*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((ceWRe*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(-3*ceHIm*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':2})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(3*ceHRe*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':2})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-((ceWIm*vevhat*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(ceWIm*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(ceWRe*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((ceBIm*cth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(ceBRe*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(ceWIm*cth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((ceWRe*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(ceWIm*ee*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-((ceWRe*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(ceWRe*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((ceWIm*ee*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(ceWRe*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '-((ceWIm*cth*ee*vevhat*ytau)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':3})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((ceWRe*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(ceWRe*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(ceBIm*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'NPcpv':1,'QED':2})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-((ceBRe*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '(ceWIm*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'NPcpv':1,'QED':2})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((ceWRe*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-((ceHIm*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceH':1,'NPcpv':1,'QED':1})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '(ceHRe*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-((cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-((cleju1Im*yc*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(cleju1Im*yc*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-((cleju1Re*complex(0,1)*yc*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '(cleju1Re*complex(0,1)*yc*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-(cleju3Im*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-(cleju3Im*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(cleju3Im*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '(cleju3Im*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-(cleju3Re*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '(cleju3Re*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-(cleju3Re*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(cleju3Re*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '-((cledjIm*ydo*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(cledjIm*ydo*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(cledjRe*complex(0,1)*ydo*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':4})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '-((cledjIm*ys*ytau)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(cledjIm*ys*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'NPcpv':1,'QED':4})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(cledjRe*complex(0,1)*ys*ytau)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledj':1,'QED':4})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                   order = {'QED':1})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(dGf*complex(0,1)*yup)/(2.*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((cjQtu1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '(cjQtu1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu1':1,'NPcpv':1,'QED':3})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '(cjQtu1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu1':1,'QED':3})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-((cjQtu8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '(cjQtu8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu8':1,'NPcpv':1,'QED':3})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(cjQtu8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjQtu8':1,'QED':3})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((cjuQb1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(cjuQb1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb1':1,'NPcpv':1,'QED':3})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '-((cjuQb1Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(cjuQb1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb1':1,'QED':3})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '-((cjuQb8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(cjuQb8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb8':1,'NPcpv':1,'QED':3})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '-((cjuQb8Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(cjuQb8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjuQb8':1,'QED':3})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '-((cQujb1Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(cQujb1Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQujb1':1,'QED':3})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '-((cQujb1Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(cQujb1Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQujb1':1,'QED':3})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '-((cQujb8Im*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(cQujb8Im*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcQujb8':1,'QED':3})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '-((cQujb8Re*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(cQujb8Re*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcQujb8':1,'QED':3})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '-((cth*cuBIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(cth*cuBRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '-((cuGIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':3})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(cuGRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':3})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(-3*cuHIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':3})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(3*cuHRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':3})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-((cuWIm*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(cuWIm*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-((cth*cuWIm*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '(cuWRe*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '(cth*cuWRe*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-((cuWIm*ee*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '-((cuWRe*ee*complex(0,1)*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(cuWRe*ee*complex(0,1)*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(cuGIm*complex(0,1)*G*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(cuGRe*G*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '-((complex(0,1)*propCorr*yup)/cmath.sqrt(2))',
                   order = {'NPprop':1,'QED':1})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(cuWIm*ee*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(cth*cuWIm*ee*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':4})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-((cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-((cth*cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(cth*cuWRe*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(cuBIm*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':3})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '-((cuBRe*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((cuWIm*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '(cuWRe*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '-((cth*cuBIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '(cth*cuBRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '-((cuGIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QED':2})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(cuGRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':2})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '(-3*cuHIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':2})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(3*cuHRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':2})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-((cuWIm*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '(cuWIm*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-((cth*cuWIm*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '(cuWRe*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(cth*cuWRe*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '-((cuWIm*ee*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '-((cuWRe*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(cuWRe*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(cuGIm*complex(0,1)*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(cuGRe*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(cuWIm*ee*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(cth*cuWIm*ee*vevhat*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':3})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '-((cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '-((cth*cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(cth*cuWRe*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(cuBIm*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcpv':1,'NPcuB':1,'QED':2})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '-((cuBRe*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '-((cuWIm*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuW':1,'QED':2})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(cuWRe*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '-((cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHbox':1,'QED':1})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHDD':1,'QED':1})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '-((cuHIm*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcpv':1,'NPcuH':1,'QED':1})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(cuHRe*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':1})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '-((cjujd11Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(cjujd11Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '-((cjujd11Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '(cjujd11Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '-((cjujd1Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '(cjujd1Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '-((cjujd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '(cjujd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-((cjujd81Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(cjujd81Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '-((cjujd81Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '(cjujd81Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '-((cjujd8Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '(cjujd8Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '-((cjujd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(cjujd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '-((cutbd1Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(cutbd1Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd1':1,'QED':4})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(cutbd1Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd1':1,'QED':4})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '-((cutbd8Im*ydo*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '(cutbd8Im*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcpv':1,'NPcutbd8':1,'QED':4})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(cutbd8Re*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcutbd8':1,'QED':4})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '-((cHudIm*ee*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(cHudIm*ee*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':5})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(cHudRe*ee*complex(0,1)*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '-((cHudIm*ee*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(cHudIm*ee*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':4})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(cHudRe*ee*complex(0,1)*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '-(cHudIm*ee*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(cHudIm*ee*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'NPcpv':1,'QED':3})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(cHudRe*ee*complex(0,1)*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '-((cleju1Im*ye*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '(cleju1Im*ye*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '-((cleju1Re*complex(0,1)*ye*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '(cleju1Re*complex(0,1)*ye*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '-(cleju3Im*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '-(cleju3Im*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(cleju3Im*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(cleju3Im*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '-(cleju3Re*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(cleju3Re*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '-(cleju3Re*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(cleju3Re*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '-((cleju1Im*ym*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(cleju1Im*ym*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '-((cleju1Re*complex(0,1)*ym*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(cleju1Re*complex(0,1)*ym*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '-(cleju3Im*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '-(cleju3Im*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(cleju3Im*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(cleju3Im*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '-(cleju3Re*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '(cleju3Re*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '-(cleju3Re*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(cleju3Re*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '-((cjujd11Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '(cjujd11Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'NPcpv':1,'QED':4})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '-((cjujd11Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '(cjujd11Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd11':1,'QED':4})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '-((cjujd1Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '(cjujd1Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'NPcpv':1,'QED':4})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '-((cjujd1Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '(cjujd1Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd1':1,'QED':4})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '-((cjujd81Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(cjujd81Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'NPcpv':1,'QED':4})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '-((cjujd81Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '(cjujd81Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd81':1,'QED':4})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '-((cjujd8Im*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(cjujd8Im*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'NPcpv':1,'QED':4})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '-((cjujd8Re*complex(0,1)*ys*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(cjujd8Re*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcjujd8':1,'QED':4})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '-((cleju1Im*ytau*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(cleju1Im*ytau*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'NPcpv':1,'QED':4})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '-((cleju1Re*complex(0,1)*ytau*yup)/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(cleju1Re*complex(0,1)*ytau*yup)/LambdaSMEFT**2',
                   order = {'NP':1,'NPcleju1':1,'QED':4})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '-(cleju3Im*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '-(cleju3Im*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '(cleju3Im*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(cleju3Im*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'NPcpv':1,'QED':4})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '-(cleju3Re*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(cleju3Re*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '-(cleju3Re*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(cleju3Re*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPcleju3':1,'QED':4})

