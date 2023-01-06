import re
from re import findall
tabre='[^\t]+'
XMre='XM_'+'[\S]+'

print('Make Individual gene fastas')
infile=open('mRNA_autumnalis.fa','r')
outfile=open('mRNA.txt','w')
mRNAdict={}
add='no'
for line in infile:
    if '>' in line:
        try:
            mRNA=findall(XMre,line)
            mRNAname=mRNA[0]
            mRNAdict[mRNAname]='>'+'autumnalis'+'\n'
            add='yes'
            outfile.write(mRNAname+'\n')
        except:
            add='no'
    else:
        if add == 'yes':
            mRNAdict[mRNAname]=mRNAdict[mRNAname]+line            
infile.close()
outfile.close
genomelist=['Nlec_pacbio','abbotii','compar','dubiosus','excitans','fabricii','hetricki','knereri','leconteiN','leconteiS','maurus','merkeli','nigroscutum','pinetum','pinusrigidae','pratti','rugifrons','swainei','taedae','virginianus','warreni']
for genome in genomelist:
    infilename='mRNA_'+genome+'.fa'
    infile=open(infilename,'r')
    print(infilename)
    add='no'
    for line in infile:
        if '>' in line:
            try:
                mRNA=findall(XMre,line)
                mRNAname=mRNA[0]
                mRNAdict[mRNAname]=mRNAdict[mRNAname]+'>'+genome+'\n'
                add='yes'
            except:
                add='no'
        else:
            if add == 'yes':
                mRNAdict[mRNAname]=mRNAdict[mRNAname]+line
    infile.close()
print(mRNAname)
print(mRNAdict[mRNAname])

mRNAlist=dict.keys(mRNAdict)
for mRNA in mRNAlist:
    outfile=open('autout_mRNA/'+mRNA+'.fa','w')
    outfile.write(mRNAdict[mRNA])
    outfile.close()
print(mRNA)
print(mRNAdict[mRNA])

