import re
from re import findall
tabre='[^\t]+'
windowre='PGA_'+'[\S]+'

chrom1=open('chr1.fa','w')
chrom2=open('chr2.fa','w')
chrom3=open('chr3.fa','w')
chrom4=open('chr4.fa','w')
chrom5=open('chr5.fa','w')
chrom6=open('chr6.fa','w')
chrom7=open('chr7.fa','w')

#genomelist=['lecontei_pacbio','abbotii','abietis','autumnalis','compar','dubiosus','excitans','fabricii','hetricki','knereri','leconteiN','leconteiS','maurus','merkeli','nigroscutum','pinetum','pinusrigidae','pratti','rugifrons','sertifer','swainei','taedae','virginianus','warreni']
genomelist=['lecontei_pacbio','abbotii','abietis','autumnalis','compar','dubiosus','excitans','fabricii','hetricki','knereri','maurus','merkeli','nigroscutum','pinetum','pinusrigidae','pratti','rugifrons','sertifer','swainei','taedae','virginianus','warreni']
for genome in genomelist:
    if genome == 'lecontei_pacbio':
        infilename='../../wholefasta/'+genome+'.fasta'
    else:
        infilename='../../wholefasta/'+genome+'_rd4totop1percentorN.fa'
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

