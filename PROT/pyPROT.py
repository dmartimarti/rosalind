#!/usr/bin/python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

# pyPROT release information
__version__ = '0.0.1'
_verdata = 'Oct 2014'
_devflag = True

#########################################################################> MAIN

# Program Header
print('\n=-= pyPROT =-= v' + __version__ + ' =-= ' +
      _verdata + ' =-= by DLS team =-=')
if(_devflag): 
    print('\n>>> WARNING! THIS IS JUST A DEVELOPMENT SUBRELEASE.' + 
          ' USE IT AT YOUR OWN RISK!')  

rna_seq = Seq("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA", IUPAC.unambiguous_rna)

print rna_seq.translate()