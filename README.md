# SMEFTsim

The SMEFTsim package is designed to enable automated calculations in the Standard Model Effective Field Theory.
It contains a set of models written in the FeynRules language for Mathematica and pre-exported to the UFO format for usage within Monte Carlo event generators.

## Website 

Further information and links to the documentation can be found at https://SMEFTsim.github.io

This web site is built with Jekyll and hosted on Github pages. You can check out its source at https://github.com/SMEFTsim/SMEFTsim.github.io

## Releases

This repository hosts `SMEFTsim v3.0` and higher. 

Every release is tagged with a version number, that is stored in the `SMEFTsim_main.fr` file in the FeynRules source and in the `version.info` file in each UFO directory. 

A copy of the latest version is stored in the FeynRules database at http://feynrules.irmp.ucl.ac.be/wiki/SMEFT.
`v2.1` can also be downloaded from there. Older versions are available upon request.

A detailed list of changes made in `v3.0` is provided in the associated scientific publication. 
The main updates are:
- two new flavor assumptions have been added, called `top` and `topU3l`. They follow the recommendations in [CERN-LPCC-2018-01](http://cds.cern.ch/record/2305783) for the study of top quark processes.
- a new feature has been implemented, that allows the inclusion of _linearized_ SMEFT corrections in the propagators of the W,Z,h bosons and of the top quark.
- the description of the SM Higgs-gluon vertices in the heavy-top EFT has been substantially improved with a full matching up to d=7.
- the parameterization of Wilson coefficients has been moved from Abs/Ph to Re/Im.
- all interaction vertices are included in the UFO models.
- more interaction orders have been added to the UFO models, in order to provide more control on each class of EFT contributions.

## Available models

`SMEFTsim` contains 10 models that differ in flavor assumptions and choice of the input parameters for the electroweak sector. 

5 flavor options are available:
- `general`: general version with free indices
- `U35`: version with a U(3)^5 symmetry imposed, truncated at the leading spurion insertion of the Yukawa couplings.
- `MFV`: linear Minimal Flavor Violation version, truncated at subleading spurion insertions of the Yukawas and neglecting non-SM CP violation.
- `top`: version for top quark physics, with a U(2)^3 symmetry in the quark sector and a U(1)^3 in the lepton sector. 
- `topU3l`: version for top quark physics, with a U(2)^3 symmetry in the quark sector and a U(3)^2 in the lepton sector. 

2 choices for EW inputs are available:
- `alphaScheme`: {alpha_em, m_Z, G_F}
- `MwScheme`: {m_W, m_Z, G_F}

## Installation and usage

It is recommended to download the [latest tagged version](https://github.com/SMEFTsim/SMEFTsim/releases/latest).


`SMEFTsim` does not require any installation per se. 
The source files can be loaded in `Mathematica`, directly after importing the `FeynRules` package. The flavor and inputs choice needs to be specified behorehand, eg.
```
Flavor = U35;
Scheme = MwScheme;
LoadModel["SMEFTsim_main.fr"]
```

The UFO files can be imported in Monte Carlo event generators. They have been optimized for `MadGraph5_aMC@NLO`, where they can be loaded as usual with
```
import model SMEFTsim_U35_MwScheme_UFO
```
or with a restriction, such as
```
import model SMEFTsim_U35_MwScheme_UFO-massless
```
Two restriction files are provided for each UFO:
- `restrict_massless.dat`: sets to zero the masses and Yukawa couplings of all the fermions except the bottom and top quark, and removes CKM mixing.
The real parts of all Wilson coefficients (except the FCNC ones, when present) are set to random values.
After a process generation, all these parameters can be re-set to zero with the associated card called `param_card_massless.dat`.

- `restrict_SMlimit_massless.dat`: same as `restrict_massless.dat`, but leaving all Wilson coefficients to 0. This card is meant to be modified by the user, in order to switch on only specific Wilson coefficients of his/her choice.

## Validation of the UFO models

All the UFO models in `SMEFTsim` have been validated according to the recommendations in [CERN-LPCC-2019-02](http://cds.cern.ch/record/2680993).

The input cards used and the PDF files produced as output are available at https://github.com/SMEFTsim/UFO-validation.

## Bug reports and questions

For questions, bug reports and feature requests, please submit a [Github issue](https://github.com/SMEFTsim/SMEFTsim/issues), or send an email to brivio@thphys.uni-heidelberg.de. 

## Citations

If you use `SMEFTsim` in a scientific publication please cite

- I. Brivio, Y. Jiang, M. Trott, The SMEFTsim package, theory and tools. JHEP 12 (2017) 070, [arXiv: 1709.06492](https://arxiv.org/abs/1709.06492). [[Inspire](https://inspirehep.net/literature/1624421)]

- I. Brivio, SMEFTsim 3.0 -- a practical guide. [arXiv: 2012.11343](https://arxiv.org/abs/2012.11343). [[Inspire](https://inspirehep.net/literature/1837608)]

## License

`SMEFTsim` is released under the MIT License.
