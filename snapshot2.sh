#!/bin/sh
fingerprint="f04593b17d6fd7d2ad7f8ab55dc5c929b416628d"  #get fingerprint from dev tool on website https://webcam.connec>token="G40LfDD0BO4Nmhpuyi9U"    #camera api
name="image2.jpg"
token="G40LfDD0BO4Nmhpuyi9U"

while true;  do
    fswebcam -d /dev/video2 -r 1280x720 --top-banner --text-colour \#fa6831 --banner-colour \#3D333F50 --line-colour \#fa6831 --rotate 270 --set contrast=20% --set saturation=35% --set  brightness=20% $name
    curl -T $name 'https://connect.prusa3d.com/c/snapshot' --header "token: ${token}" --header "fingerprint: ${fingerprint}"
    sleep 8
    done