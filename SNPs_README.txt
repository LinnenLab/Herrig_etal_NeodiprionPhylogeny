READ ME: Investigating SNPs for phylogeny

Part 1: Make chromosomes fastas
Step 1: mkdir chromosomes (in level same as wholefastas) 
Step 2 copy chromosomefastas.job, chromosomefastas.py, and Make_individual_chromosome_fastas-20species.py in chromosomes 
(scp *chromosome* dkhe223@lcc.uky.edu:/scratch/dkhe223/pacbio_repit/fresh_IUPAC/chromosomes)
Step 3: Open the chromosomefastas.job  script and define your email address 
(currently "youremail", either use something like: sed -i -- 's/youremail/dkhe223/g' chromosomefastas.job
 or open and manipulate it directly)
Step 4: sbatch chromosomefastas.job
this job contains: 
python chromosomefastas.py
python Make_individual_chromosome_fastas-20species.py 
(Makes chromosome files for each species and a single chromosome for the 20 species)

Part 2: Make vcf files (snp-sites -v -c -o noIUPAC-vcf/chr1.vcf ../chromosomes/chr1.fa)
Step 1: mkdir SNPs
Step 2: copy getSNPs.job and personalize it
Step 3: sbatch getSNPs.job

Part 3: Subsample and Make trees files of subsampled SNPs--currently set to automatically pull a SNP every 1,5,10, and 50kb
Step 1: copy getSNPs.job, initiate_subsampleSNPs.sh, start_4subsampling.sh, vcf2fasta.py and combine_subsampled_chrSNPs.py in SNP folder
chmod +x start_4subsampling.sh
./start_4subsampling.sh



Note 1: Folder structure:
no_IUPAC > chromosomes
no_IUPAC > SNPs
(wholefasta and genes are at the same level. Scripts should be within the windows specific folder) 


