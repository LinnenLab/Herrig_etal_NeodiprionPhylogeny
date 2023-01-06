import re
from re import findall
tabre='[^\t]+'
windowre='Chromosome'+'[\S]+'

chrom1=open('chromosomes/chr1.fa','w')
chrom2=open('chromosomes/chr2.fa','w')
chrom3=open('chromosomes/chr3.fa','w')
chrom4=open('chromosomes/chr4.fa','w')
chrom5=open('chromosomes/chr5.fa','w')
chrom6=open('chromosomes/chr6.fa','w')
chrom7=open('chromosomes/chr7.fa','w')

genomelist=['Nlec_HiC_scaffolds_primary','abbotii','abietis','autumnalis','compar','dubiosus','excitans','fabricii','hetricki','knereri','leconteiN','leconteiS','maurus','merkeli','nigroscutum','pinetum','pinusrigidae','pratti','rugifrons','sertifer','swainei','taedae','virginianus','warreni']
for genome in genomelist:
    if genome == 'Nlec_HiC_scaffolds_primary':
        infilename='../wholefasta/'+genome+'.fasta'
    else:
        infilename='../wholefasta/'+genome+'_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa'
    infile=open(infilename,'r')
    print(infilename)
    currentchr='notstarted'
    for line in infile:
        if '>' in line:
            add='no'
            nums=findall('[0-9]+',line)
            currentchr='chr'+nums[0]
            if currentchr== 'chr1':
                chrom1.write('>'+genome+'\n')
            elif currentchr == 'chr2':
                chrom2.write('>'+genome+'\n')
            elif currentchr== 'chr3':
                chrom3.write('>'+genome+'\n')
            elif currentchr == 'chr4':
                chrom4.write('>'+genome+'\n')
            elif currentchr == 'chr5':
                chrom5.write('>'+genome+'\n')
            elif currentchr == 'chr6':
                chrom6.write('>'+genome+'\n')
            elif currentchr == 'chr7':
                chrom7.write('>'+genome+'\n')
        else:
            if currentchr == 'chr1':
                chrom1.write(line)
            elif currentchr == 'chr2':
                chrom2.write(line)
            elif currentchr == 'chr3':
                chrom3.write(line)
            elif currentchr == 'chr4':
                chrom4.write(line)
            elif currentchr == 'chr5':
                chrom5.write(line)
            elif currentchr == 'chr6':
                chrom6.write(line)
            elif currentchr == 'chr7':
                chrom7.write(line)
    infile.close()

chrom1.close()
chrom2.close()
chrom3.close()
chrom4.close()
chrom5.close()
chrom6.close()
chrom7.close()
