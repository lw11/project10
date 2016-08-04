encrypted_file=$1
openssl aes-256-cbc -d -in $encrypted_file -out /var/tmp/decrypted_file
tar -zxvf /var/tmp/decrypted_file