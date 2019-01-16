#!/usr/bin/env python
# coding : utf-8
class TestA():
 @classmethod
 def testagressif(cls):
    import os
    import socket,sys
    


    def get_nmap(options, ip):
        command="nmap" + options + " " + ip
        process=os.popen(command)
        results=str(process.read())
        return results   

    def create_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def write_file(path, data):
        f=open(path, 'w')
        f.write(data)
        f.close()      
            
    create_dir('articles/media') 

    def test1():   
        try:    
           host=input("Entrer l addresse ip de la machine: ")
        except KeyboardInterrupt:
           sys.exit(1)  
        print(" Scann aggressif:\n")
        print(get_nmap('  -osscan-guess', host))   
        write_file('articles/media/scanagressif.html', get_nmap(' -osscan-guess', host)) 

    test1()
        
  

    
   