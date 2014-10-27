# -*- coding: utf-8 -*-
### Computing GC content
## The main objective is to compute the GC content, compare between seqs, and show the seq with more GC content

from Bio import SeqIO
from Bio.SeqUtils import GC

fasta_sequences = SeqIO.parse(open('rosalind_gc.txt'),'fasta')

## Computing GC content

my_dic = {}

for fasta in fasta_sequences:
    name, sequence = fasta.id, fasta.seq.tostring()
    my_dic[name] = GC(sequence)

print max(my_dic, key=my_dic.get), '\n' , my_dic[max(my_dic, key=my_dic.get)]
