class TestR():

  @classmethod
  def testreseau(cls):
    import socket
    import os
    import re
    import subprocess
    
    def create_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def write_file(path, data):
        f=open(path, 'w')
        f.write(data)
        f.close()      
            
    create_dir('directory') 

    def get_nmap(options, ip):
        command="nmap" + options + " " + ip
        process=os.popen(command)
        results=str(process.read())
        return results  

    def test1():   
        try:    
           host=input("Entrer l addresse Reseau aue vous voulez scaner: ")
        except KeyboardInterrupt:
           sys.exit(1)

        print(" detections des adresses Ip .... :\n")
        print(get_nmap('  -sP', host))  
        write_file('directory/scansystem.txt', get_nmap(' -sP', host)) 
       
    test1()
        
    
#     print('[+] Choice')
#     print('1 - Scan Network')
    
#     hosts = []
#     choice = int(input())
#     ip = "192.168.137."
#     x= 105
#     if choice == 1:
#         while x<=110:
#             p = subprocess.Popen('ping ' +ip+str(x) +" -n 1" ,stdout=subprocess.PIPE, shell=True)
#             out, error = p.communicate()
#             out = str(out)
#             find = re.search("Destination host unreachable",out)
#             if find is None:
#                 hosts.append(ip+str(x))
#                 print("[*] Host found")
#             x = x + 1
#     print("+----------------------+")
#     print("|     hosts:           |")
#     print("+----------------------+")
#     for host in hosts:
#         try:
#             name, a ,b =socket.gethostbyaddr(host)
#         except:
#             name = "Not Found"
#         print('| '+host + " | " + name)
        



