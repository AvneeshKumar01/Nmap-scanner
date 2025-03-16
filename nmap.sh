echo "....PORT SCANNER...."

echo "Please enter your IP address: "
read IP
echo "The ip address is $IP "

echo "Please select the type of scan you want to run:
      1) Ping scan
      2) TCP SYN scan
      3) TCP connect scan
      4) UDP scan
      5) Aggressive scan
      6) Fast scan"

echo "enter your choice (1-5) : "
read choice

nmap --version
if [ $choice = 1 ];then
    ping -c 1 $IP
elif [ $choice = 2 ];then
    nmap -sS $IP
elif [ $choice = 3 ];then
    nmap -sT $IP
elif [ $choice = 4 ];then
    nmap -sU $IP
elif [ $choice = 5 ];then
    nmap -A $IP
elif [ $choice = 6 ];then
    nmap -F $IP
fi

nmap --open $IP
