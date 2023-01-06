mkdir 1kb_SNPs
cp initiate_subsampleSNPs.job 1kb_SNPs
cd 1kb_SNPs
sed -i -- 's/sizeinkb/1/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..

mkdir 2kb_SNPs
cp initiate_subsampleSNPs.job 2kb_SNPs
cd 2kb_SNPs
sed -i -- 's/sizeinkb/2/g' initiate_subsampleSNPs.job
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

mkdir 20kb_SNPs
cp initiate_subsampleSNPs.job 20kb_SNPs
cd 20kb_SNPs
sed -i -- 's/sizeinkb/20/g' initiate_subsampleSNPs.job
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

mkdir 100kb_SNPs
cp initiate_subsampleSNPs.job 100kb_SNPs
cd 100kb_SNPs
sed -i -- 's/sizeinkb/100/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..

mkdir 1000kb_SNPs
cp initiate_subsampleSNPs.job 1000kb_SNPs
cd 1000kb_SNPs
sed -i -- 's/sizeinkb/1000/g' initiate_subsampleSNPs.job
sed -i -- 's/youremail/dkhe223/g' initiate_subsampleSNPs.job
sbatch initiate_subsampleSNPs.job
cd ..