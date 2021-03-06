#!/bin/bash

IpAddr=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f 1 -d'/')
IpAddr=$(echo $IpAddr | cut -d'.' -f 1-3)
for((x=1;x<255;x++))
do
        isUp=$(ping $IpAddr"."$x -c 5 -W 2 | grep "5 packets" | cut -f 2 -d',')
        if [[ ! $isUp =~ "0" ]];then
                echo "$IpAddr.$x is up"
        fi
done
