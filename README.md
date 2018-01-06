# isUp
Checks what IP addresses on your network are up or down
isUp is a simple program that I will be using in other projects          
This program is to be run on a linux terminal           

### Work in Progress
There is two versions of this program both do the same thing        
One is written in python and the other in writtten in linux bash script                     
 
### How It Works
Firt the program gets the devies local IP address            
Ex: 192.168.0.12          
Then it pings all of the possible IP addresses on that network            
Ex: 192.168.0.1-192.168.0.255           
If the ping from the IP address is recieved then the IP address is up          
When the IP address is up isUp echos the IP address and that it is up


### How to Setup and Run
Python              
1. Update your linux OS          
Ex: `sudo apt-get update`          
2. Install python            
Ex: `sudo apt-get install python`          
3. Compile isUp.py                
Ex: `chmod +x isUp.py`          
4. Run isUp.py            
Ex: `python isUp.py`            

Bash           
1. Update yout linus OS         
Ex: `suo apt-get update`            
2. Install bash             
Ex: `sudo apt-get install bash`        
3. Compile isUp.sh               
Ex: `chmod +x isUp.sh`         
4. Run isUp.sh            
Ex: `bash isUp.sh`         
