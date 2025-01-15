gunzip -c dictionary.gz | grep -E "^[zonriac]{4,}$" | grep -i 'r' 

gunzip -c dictionary.gz | grep -E "^[zonriac]{4,}$" | grep -i 'r' | wc -l

