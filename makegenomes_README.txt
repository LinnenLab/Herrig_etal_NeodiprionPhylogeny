READ ME: Creating "Pseudo-reference" Genomes in N. lecontei coordinates for Phylogeny


Step 1: Check that the reference genome is accessible as well as the reads for all species.

Step 2: Check that all programs needed are in the environment:
module load ccs/anaconda/3  
conda install -c bioconda bowtie2 
conda install samtools 
conda install -c bioconda vcftools 
conda install -c bioconda bcftools 

Step 3: Check that all jobs and python scripts are available:
base_itrep.job
make_itrep_jobs.py
identifytop2and1percentdepths_allspecies.py
make_N1percentjobs.py
base_samtoolsdepth_N1percenttop.py


Step 4: Prep the reference genome (bowtie2-build Nlec_HiC_scaffolds_primary.fasta Nlecref)

Step 5: Run the make_itrep_jobs.py script. Then submit all jobs that it creates (one for each species). This will make a new genome in N. lecontei coordinates. BUT you aren't done-- there are nucleotides that need to be replaced with "N"s.

Step 6: Replace low coverage/excessive coverage sites by running make_N1percentjobs.py and submitting the jobs it creates.


Bonus step: Create specific files for each chromosome. This can be useful for downstream steps and is implemented with the Make_individual_chromosome_fastas.py script.

  