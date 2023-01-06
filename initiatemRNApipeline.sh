#!/bin/bash
#SBATCH -t 7-00:00:00
#SBATCH --job-name=gfftofasta
#SBATCH -n 1
#SBATCH -p SKY32M192_L
#SBATCH --account=col_cli242_uksr
#SBATCH --mail-type ALL
#SBATCH --mail-user dkhe223@uky.edu
#SBATCH --output=GFFtoFastas.out

module load ccs/anaconda/3
source activate /project/cli242_uksr/dkhe223/conda
conda activate /project/cli242_uksr/dkhe223/conda/phylogenies
#conda install -c bioconda gffread 

printf "Obtaining fastas per species\n"
mkdir speciesmRNA
gffread -w speciesmRNA/mRNA_Nlec_pacbio.fa -g ../wholefasta/Nlec_HiC_scaffolds_primary.fasta iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_abbotii.fa -g ../wholefasta/abbotii_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_abietis.fa -g ../wholefasta/abietis_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_autumnalis.fa -g ../wholefasta/autumnalis_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_compar.fa -g ../wholefasta/compar_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_dubiosus.fa -g ../wholefasta/dubiosus_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_excitans.fa -g ../wholefasta/excitans_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_fabricii.fa -g ../wholefasta/fabricii_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_hetricki.fa -g ../wholefasta/hetricki_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_knereri.fa -g ../wholefasta/knereri_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_leconteiN.fa -g ../wholefasta/leconteiN_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_leconteiS.fa -g ../wholefasta/leconteiS_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_maurus.fa -g ../wholefasta/maurus_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_merkeli.fa -g ../wholefasta/merkeli_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_nigroscutum.fa -g ../wholefasta/nigroscutum_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_pinetum.fa -g ../wholefasta/pinetum_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_pinusrigidae.fa -g ../wholefasta/pinusrigidae_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_pratti.fa -g ../wholefasta/pratti_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_rugifrons.fa -g ../wholefasta/rugifrons_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_sertifer.fa -g ../wholefasta/sertifer_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_swainei.fa -g ../wholefasta/swainei_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_taedae.fa -g ../wholefasta/taedae_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_virginianus.fa -g ../wholefasta/virginianus_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F
gffread -w speciesmRNA/mRNA_warreni.fa -g ../wholefasta/warreni_iupac_it5.depth_withnucleotide_rd4totop1percentorN.fa iyNeoLeco1.1_genomic.gff -F

printf '\n#make fastas, treejobs, and trees for 20species'
mkdir 20species_mRNA
python Make_individualgene_fastas_20species.py

mkdir 20species_iqtreejobs/
python make_iqtreejobs_20species.py

cd 20species_iqtreejobs
chmod +x submitiqtrees
./submitiqtrees