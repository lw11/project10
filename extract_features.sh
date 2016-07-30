input_resume=$1

gpa_info=`grep -i gpa $1|tr -s " "|head -1`
#regex="\([0-9]\.\d+\)[\s][|\\][\s]\(\d\(\.0\)?\)"
if [ ! -z "$gpa_info" ]; then
  gpa_regex="\(.*\?\)\([0-9]\.[0-9]\+\).*"
  max_regex=".*[|//]\s\?\(100\|\([0-9][0-9]\|[0-9]\)\\).*"

  gpa=`echo $gpa_info | sed "s/$gpa_regex/\2/"`
  max=`echo $gpa_info | sed "s/$max_regex/\1/"`
  #echo "echo $gpa_info | sed \"s/$max_regex/\1/\""
  echo "gpa $gpa"
  if [ "$gpa_info" != "$max" ]; then
    echo "max_gpa $max"
  fi
fi