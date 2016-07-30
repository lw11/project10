resume_file=$1

rm -f /var/tmp/temp_word_list.txt
rm -f /var/tmp/features.txt

#echo "extracting word list from $resume_file"
./extract_word_list.sh $resume_file > /var/tmp/temp_word_list.txt
#echo "extracting features from $resume_file"
./extract_features.sh $resume_file > /var/tmp/features.txt
#echo "evaluating $resume_file"
python score_features.py /var/tmp/temp_word_list.txt /var/tmp/features.txt
