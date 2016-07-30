input_resume=$1

cat $1 | tr ' ' '\n' | awk '{print tolower($0)}' | sed 's/,//g' | sort | uniq -c | awk '{print $2" "$1}' | sort -n -k2 -r