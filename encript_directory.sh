dir_to_compress=$1
output_file=$2

tar -zcvf files.tar.gz $dir_to_compress
openssl aes-256-cbc -salt -in files.tar.gz -out files.encripted
