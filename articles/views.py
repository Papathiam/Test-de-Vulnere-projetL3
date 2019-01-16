from django.shortcuts import render , redirect , get_object_or_404
# Create your views here.
from .ScanReseau import TestR
from .ScanPort import Test
from .ScanSystem import Test1
from .ScanAgressif import TestA
from .models import Articles,UserProfile
from .forms import ArticlesForm ,CommentForm,UserForm
from django.contrib.auth.decorators import login_required
from .forms import ScanForm
from django.utils import timezone


import nmap
import subprocess
import os


def show(request):
    articles = Articles.objects.all()
    return render(request, 'articles/show.html' , {'articles': articles })

def detailarticle(request, id):
    articles = Articles.objects.all()
    # context = {'articles': articles[int(id)-1]}
    template = 'articles/detailarticle.html'
    return render(request, template ,{'articles': articles[int(id) - 1]} )
    
@login_required
def addComment(request, id):
    articles = get_object_or_404(Articles, id=id)
    form= CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.articles = articles
            comment.user = request.user
            comment.save()
            return redirect('detailarticle' , id=articles.id ) 
        else:
            form.CommentForm()
    return render(request , 'articles/addComment.html', {'form':form})

@login_required
def addArticle(request):
    articles = Articles()
    form = ArticlesForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            articles = form.save(commit=False)
            articles.articles = articles
            articles.save()
            return redirect('show')
        else:
            form.ArticlesForm()

    return render(request, 'articles/addArticle.html', {'form': form})


def addUser(request):
    user = UserProfile()
    form = UserForm(request.POST or None, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.user = user
            user.save()
            return redirect('show')
        else:
            form.UserForm()

    return render(request, 'articles/inscription.html', {'form': form})


def Apropos(request):
    return  render(request, 'articles/Apropos.html')


def scan(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
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
                resultat = nmScan.scan(hosts=target, arguments='-sV T5')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                    porti = ports[i]
                    print(porti['state'])

                    res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scan_result.html", {"resultat": res, "target": target, "erreur": erreur})
             
# if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scan_form.html', {'form': form})

def scanSimple(request):
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
                resultat = nmScan.scan(hosts=target, arguments='-sV T5')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                    porti = ports[i]
                    print(porti['state'])

                    res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scansimple_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scansimple_form.html', {'form': form})

def scanAgressif(request):
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
                resultat = nmScan.scan(hosts=target, arguments='-sV T5')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports:
                    porti = ports[i]
                    print(porti['state'])

                    res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une adresse IP valide"
        return render(request, "articles/scanagressiff_result.html", {"resultat": res, "target": target, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scanagressiff_form.html', {'form': form})



def scanReseau(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        target = ""
        erreur = ""
        res = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nma = nmap.PortScanner()
            print(form)
            target = request.POST['target']
            try:
                result = nma.scan(hosts=target, arguments='-sP T5')
                res = []
                print(result)
                hosts_list = [x for x in nma.all_hosts()]
                t = len(hosts_list)
                for i in range(0, t):
                    print("Hôte: ", hosts_list[i])
                    host = hosts_list[i]
                    print("         Nom: ", nma[host]['hostnames'])

                    print("         Adresses: ", nma[host]['addresses'])
                    print("         AdresseIPv4: ", nma[host]['addresses']['ipv4'])
                    try:
                         print("         AdresseMAC: ", nma[host]['addresses']['mac'])
                         adresseMAC = nma[host]['addresses']['mac']
                    except:
                        print("       AdressesMAC: none")
                        adresseMAC = "  none"
                    print("         Etat: ", nma[host]['status'])
                    print("         Etat: ", nma[host]['status']['state'])
                    print()
                    res.append({'host':hosts_list[i], 'state':nma[host]['status']['state'], 'hostname':nma[host]['hostnames'], 'adresseIPv4':nma[host]['addresses']['ipv4'], 'adresseMAC':adresseMAC})
            except:
                erreur = "veuillez entrer une addresse réseau valide"
        return render(request, "articles/scan_reseau_result.html", {"resultat": res, "result": result, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scan_reseau_form.html', {'form': form})


def collectweb(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        target = ""
        erreur = ""
        res = ""
        form = ScanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            nma = nmap.PortScanner()
            print(form)
            target = request.POST['target']
            try:
                result = nma.scan(hosts=target, arguments='-v -A T5')
                res = []
                print(result)
                hosts_list = [x for x in nma.all_hosts()]
                t = len(hosts_list)
                for i in range(0, t):
                    print("Hôte: ", hosts_list[i])
                    host = hosts_list[i]
                    print("         Nom: ", nma[host]['hostnames'])

                    print("         Adresses: ", nma[host]['addresses'])
                    print("         AdresseIPv4: ", nma[host]['addresses']['ipv4'])
                    try:
                         print("         AdresseMAC: ", nma[host]['addresses']['mac'])
                         adresseMAC = nma[host]['addresses']['mac']
                    except:
                        print("       AdressesMAC: none")
                        adresseMAC = "  none"
                    print("         Etat: ", nma[host]['status'])
                    print("         Etat: ", nma[host]['status']['state'])
                    print()
                    res.append({'host':hosts_list[i], 'state':nma[host]['status']['state'], 'hostname':nma[host]['hostnames'], 'adresseIPv4':nma[host]['addresses']['ipv4'], 'adresseMAC':adresseMAC})
            except:
                erreur = "veuillez entrer une addresse réseau valide"
        return render(request, "articles/scan_web_result.html", {"resultat": res, "result": result, "erreur": erreur})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ScanForm()
        return render(request, 'articles/scan_web.html', {'form': form})



def pentestweb(request):
    if request.method == 'POST':
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
                resultat = nmScan.scan(hosts=target, arguments='-v -A T5')
                ports = resultat['scan'][target]['tcp']
                res = []
                i=1
                for i in ports :
                    porti = ports[i]
                    print(porti['state'])

                    res.append({'port':i,'state':porti['state'], 'name':porti['name'], 'product':porti['product'], 'version':porti['version']})
            except:
                erreur = "veuillez entrer une nom de domaine (ou addresse IP) valide"
        return render(request, "articles/pentestWeb_result.html", {"resultat": res, "target": target, "erreur": erreur})
    else:
        form = ScanForm()
        return render(request, 'articles/pentest_web.html', {'form': form})
    

def collecte(request):
    col = "collecte d'informations"
    return render(request, "articles/collecte.html", {"col": col})


def menu(request):
    return render(request, 'articles/menu.html')

def acc(request):
    return render(request, 'articles/acc.html')

def ScanReseau(request):
    pos1=TestR.testreseau()
    return render(request, 'articles/ScanReseau.html', {'pos1':pos1})

def ScanPort(request):
    pos=Test.testport()
    return  render(request, 'articles/ScanPort.html', {'pos':pos})

def ScanSystem(request):
    poss=Test1.testsystem()
    return  render(request, 'articles/ScanSystem.html', {'poss':poss})

def ScanAgressif(request):
    po=TestA.testagressif()
    return  render(request, 'articles/ScanAgressif.html', {'po':po})

def pentestWeb(request):
        
    return render(request, "articles/pentestWeb.html", {})

def pentestSys(request):
    return render(request, "articles/pentestSys.html", {})