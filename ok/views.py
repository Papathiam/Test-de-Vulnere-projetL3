from django.shortcuts import render
from .forms import ScanForm
import nmap
import subprocess
import os


def scan(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        res = ""
        target = ""
        erreur = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nmScan = nmap.PortScanner()
            print(form)
            target = request.POST['target']

            try:
                resultat = nmScan.scan(hosts=target, arguments='-sV -p20-8001')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                        porti = ports[i]
                        print(porti['state'])

                        res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "ok/scan_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'ok/scan_form.html', {'form': form})

def index(request):
    return render(request, "ok/index.html")
