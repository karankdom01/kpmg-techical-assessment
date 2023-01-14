#!/bin/bash


function nested () {
    object=$object
    key=$key
    replace=$(echo $key | sed 's/\//./g')

    value=$(echo $object | jq -r '.'$replace'')
    echo Value: $value


}

read -p "Objects : " object
read -p  "Keys : " key

nested
