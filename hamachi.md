# setup hamachi
* https://www.iceflatline.com/2009/10/remote-access-to-your-ubuntu-server-using-putty-hamachi-and-ssh/
* sudo apt-get install lsb
* https://www.vpn.net/linux
* download .deb install file using wget
* sudo dpkg -i **
# Using Hamachi Server
* sudo /etc/init.d/logmein-hamachi stop
* sudo /etc/init.d/logmein-hamachi start
* sudo /etc/init.d/logmein-hamachi restart
* sudo hamachi login
* sudo hamachi logout
* sudo hamachi set-nick <your_nickname>
* sudo hamachi create <your_network_name> <your_network_password>
* sudo hamachi without any arguments. To display a full list of all the LogMeIn Hamachi command options, use sudo hamachi -h.
# Client
* sudo hamachi login
* sudo hamachi set-nick <your_nickname>
* sudo hamachi join <your_network_name> <your_network_password>
* sudo hamachi list
