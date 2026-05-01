# 0-release.sh

This bash script displays the Linux distribution name (distributor ID) in a concise single-line output using the  * lsb_release -is * command.

make as executable :(chmod +x 0-release.sh), and run it:

./0-release.sh
Kali

Info Alex : It works because -i asks for the distributor info and -s makes the output short (just the value, no label).
