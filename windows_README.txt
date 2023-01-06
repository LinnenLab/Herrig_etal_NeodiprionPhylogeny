READ ME: Investigating windows for Phylogeny


Step 1: Upload/copy all files in folder to new window specific folder (i.e. windows_100kb)
Step 2: Make sure that the fastas of all species that you want to investigate are in a folder called "wholefasta" 
Step 3: Open the startbedfiles.sh script and define the window size that you desire 
(currently "definesize", either use something like: sed -i -- 's/definesize/500000/g' initiatepipeline.sh 
 or open and manipulate both places where it is found)
Step 4: make initiatepipeline.sh script executable: 
chmod +x initiatepipeline.sh
Step 5: Start pipeline (should run all the way through making trees unassisted...) with command:
./initiatepipeline.sh

Step 6: After pipeline is finished, make combined gene trees (need to define windowsize)
python make_inputfile_simplifiedslidingwindows_20species.py windowsize

Note 1: Folder structure:
no_IUPAC > wholefasta
no_IUPAC > windows_100kb
(wholefasta and windows_100kb are at the same level. Scripts should be within the windows specific folder) 

Note 2: If something gets stuck, you can restart in the job and sh scripts. (Though it takes less than 10 minutes from initiating the script to starting the tree jobs, so I recommend starting from the beginning). The order that they are called is:
./initiatepipeline.sh
sbatch makewindows.job
./makeiqtreejobs.sh
(and ./submitiqtreejobs, but those are within other folders, I suggest just running makeiqtreejobs.sh again. If adding another set of species, you can copy this script and the files it calls accordingly.)


  