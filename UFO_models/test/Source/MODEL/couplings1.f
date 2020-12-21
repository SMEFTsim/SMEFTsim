ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_1 = (MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_2 = (-2.000000D+00*MDL_EE*MDL_COMPLEXI)/3.000000D+00
      GC_3 = -(MDL_EE*MDL_COMPLEXI)
      GC_5923 = -(MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_CTH*MDL_STH)
      GC_6212 = -(MDL_EE*MDL_COMPLEXI*MDL_STH)/(3.000000D+00*MDL_CTH)
      GC_6213 = (2.000000D+00*MDL_EE*MDL_COMPLEXI*MDL_STH)/(3.000000D
     $ +00*MDL_CTH)
      GC_6214 = -((MDL_EE*MDL_COMPLEXI*MDL_STH)/MDL_CTH)
      END
