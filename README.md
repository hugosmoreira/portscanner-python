# portscanner-python
simple port scanner 

Port Scanner Script in Python
This repository hosts a Python script designed to perform port scanning on a given IP address or range of IP addresses. The primary aim of this script is to serve as an educational tool for learning about network security and penetration testing methodologies.

⚠️ Legal Disclaimer
This script is created solely for educational and ethical training purposes. The author, Hugo Moreira, is not responsible for any misuse or for any damages arising from the use of this script. By using this script, you agree to adhere to the legal and ethical guidelines of penetration testing and network scanning. Unauthorized access to computer systems is illegal and punishable by law. Ensure you have explicit permission from the network owner before running this script on any network.

Features
Simple and intuitive usage
Ability to scan a single IP or a range of IPs
Identifies open ports and services running on the target system

Installation and Dependencies
Clone the repository to your local machine:


git clone https://github.com/hugosmoreira/portscanner-python.git
Navigate to the cloned directory:


cd portscanner-python
Install the required Python libraries:


pip install -r requirements.txt
Usage
To run the script, use the following command:


python portscanner.py <target-ip> [<start-port> <end-port>]
Example:


python portscanner.py 192.168.1.1 20 1024
Contributing
Feel free to fork this repository and submit pull requests for any improvements or additional features you'd like to see. All contributions are welcome!

Contact
For any inquiries or feedback, please contact Hugo Moreira.

License
This project is licensed under the MIT License - see the LICENSE file for details.
