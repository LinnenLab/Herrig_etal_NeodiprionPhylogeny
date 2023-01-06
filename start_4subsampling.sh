mkdir 1kb_SNPs
cp initiate_subsampleSNPs.job 1kb_SNPs
cd 1kb_SNPs
sed -i -- 's/sizeinkb/1/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..

mkdir 5kb_SNPs
cp initiate_subsampleSNPs.job 5kb_SNPs
cd 5kb_SNPs
sed -i -- 's/sizeinkb/5/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..

mkdir 10kb_SNPs
cp initiate_subsampleSNPs.job 10kb_SNPs
cd 10kb_SNPs
sed -i -- 's/sizeinkb/10/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..

mkdir 50kb_SNPs
cp initiate_subsampleSNPs.job 50kb_SNPs
cd 50kb_SNPs
sed -i -- 's/sizeinkb/50/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..
