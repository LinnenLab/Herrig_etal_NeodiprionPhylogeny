READ ME: Investigating genes for Phylogeny


Step 1: Upload/copy all files in folder to new gene specific folder (i.e. genes)
Step 2: Make sure that the fastas of all species that you want to investigate are in a folder called "wholefasta" 
Step 3: Open the initiate_mRNApipeline.job  script and define your email address 
(currently "youremail", either use something like: sed -i -- 's/youremail/dkhe223/g' initiatepipeline.sh 
 or open and manipulate both places where it is found)
Step 4: Start pipeline (should run all the way through making trees unassisted...) with command:
sbatch initiate_mRNApipeline.job 


Note 1: Folder structure:
no_IUPAC > genes
no_IUPAC > genes
(wholefasta and genes are at the same level. Scripts should be within the windows specific folder) 

Files that should be copied in step 1:
initiate_mRNApipeline.job                Make_individualgene_fastas_internal.py  make_iqtreejobs_internal.py
Make_individualgene_fastas_20species.py  make_iqtreejobs_20species.py            Neodiprion_lecontei_male_scaffolds.gff