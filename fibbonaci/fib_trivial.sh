#!/bin/sh

echo "Enter the n number you want : "
read -r n
echo
i=0
j=1
sum=0
echo "$i"
echo "$j"
while [ $i -le "$n" ]
do
      sum=$(( i + j ))
        i=$j
    j=$sum
    echo "$sum"
done
