Autoshop Kubernetes
===================

[[_TOC_]]

Die folgenden Befehle sind in einer (Ubuntu) Linux Umgebung mit Kubernetes (microk8s) ausführen.

Installation
------------

**Variante a) eigene VM** 

Dazu erstellen wir eine neue VM mit Ubuntu und Kubernetes (microk8s).

Das Cloud-init Script sieht wie folgt aus:

    #cloud-config
    users:
      - name: ubuntu
        sudo: ALL=(ALL) NOPASSWD:ALL
        groups: users, admin
        home: /home/ubuntu
        shell: /bin/bash
        lock_passwd: false
        plain_text_passwd: 'insecure'        
    # login ssh and console with password
    ssh_pwauth: true
    disable_root: false    
    packages:
      - docker.io
    runcmd:
        - sudo snap install microk8s --classic 
        - sudo snap install kubectl --classic
        - sudo snap install helm --classic
        - sudo microk8s status --wait-ready
        - sudo microk8s enable dns hostpath-storage
        - sudo usermod -a -G microk8s ubuntu
        - sudo mkdir -p /home/ubuntu/.kube
        - sudo microk8s config | sudo tee  /home/ubuntu/.kube/config
        - sudo chown -f -R ubuntu:ubuntu /home/ubuntu/.kube
        - sudo chmod 600 /home/ubuntu/.kube/config
     
Z.B. mit `multipass`

    git clone https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates.git
    cd kubernetes-templates 
    multipass launch --name microk8s -c4 -m6GB -d32GB --cloud-init cloud-init.yaml   
    multipass set client.primary-name=microk8s
    
Wechsel in VM

    winpty multipass shell microk8s
    
**Variante b) Windows Subsystem Linux **

Wenn nicht bereits erfolgt:
* [Windows Terminal](https://learn.microsoft.com/en-us/windows/terminal/install) installieren
* WSL aktivieren `wsl --install`
* Terminal starten und mittels Pulldown (Pfeil nach unten, ca. in der Mitte) in `Ubuntu` Linux wechseln
* Wechsel in `Ubuntu` Linux und Befehle von `cloud-init` Script oben ab `runcmd` ohne voranstehendes `-` ausführen
  
Links:
* [Install MicroK8s on WSL2](https://microk8s.io/docs/install-wsl2)  
 

AutoShop Services Bereitstellen
-------------------------------

YAML Datei um die [AutoShop MS](https://gitlab.com/ch-mc-b/autoshop-ms/app) Applikation zu Bereitzustellen (Deploy).

Um die Applikation zu Bereitzustellen (Deploy) zuerst Services und Ingresses einrichten

    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/catalog-service.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/customer-service.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/order-service.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/webshop-service.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/webshop-ingress.yaml                

Version 1.0.0
-------------

Einfache Version mit Pods

    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-pod/catalog-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-pod/customer-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-pod/order-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-pod/webshop-pod.yaml    

Mit Deployment, ReplicaSets und Pods

    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-deployment/catalog-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-deployment/customer-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-deployment/order-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/1.0.0-deployment/webshop-deployment.yaml 

Version 2.0.0
-------------

Einfache Version mit Pods

    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-pod/catalog-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-pod/customer-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-pod/order-pod.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-pod/webshop-pod.yaml    

Mit Deployment, ReplicaSets und Pods

    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-deployment/catalog-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-deployment/customer-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-deployment/order-deployment.yaml
    kubectl apply -f https://gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/-/raw/main/2.0.0-deployment/webshop-deployment.yaml 

Testen
------

Entweder über den gemappten Port vom Service `webshop`

    kubectl get services

Oder über den Ingress (Reverse Proxy), wenn z.B. Kubernetes in einer VM mit Namen `container` läuft

    [https://container.mshome.net/webshop](https://container.mshome.net/webshop)

Um die Kubernetes Ressourcen anzuzeigen, bietet sich das Dashboard an. Es kann ohne Token (Überspringen) angesprochen werden.

Starten mittels:

    kubectl apply -f https://raw.githubusercontent.com/mc-b/duk/master/addons/dashboard-skip-login-no-ingress.yaml

Ansprechen mittels

    [https://microk8s.mshome.net:8443](https://microk8s.mshome.net:8443)

Rolling Update
--------------

Ein Rolling Update in Kubernetes ist eine Methode zur kontinuierlichen und unterbrechungsfreien Aktualisierung von Anwendungen, die in einem Kubernetes-Cluster bereitgestellt werden. Diese Art von Update ermöglicht es, neue Versionen von Anwendungen schrittweise einzuführen, während die alten Versionen noch aktiv sind

Werden die Container mittels Deployments gestartet, kann ein Rolling Update durchgeführt werden.

Dazu die Applikation zuerst als Version 1.0.0 mittels Deployments starten, Webseite und evtl. Dashboard anwählen.

Dann die Befehle von Version 2.0.0 zum Ausrollen der Deployments ausführen.

Blue / Green Deployment 
-----------------------

Unter Blue / Green Deployment wird der Prozess verstanden, bei dem neben einer bisherigen Infrastruktur (Blue Deployment) parallel eine neue Version (Green Deployment) aufgebaut wird. 

    cd blue-green
    kubectl apply -f 1.0.0-blue -f 2.0.0-green

Aktivieren des "Blue Deployments" (1.0.0)

    kubectl apply -f 1.0.0-blue/webshop-service.yaml

Aktiveren des "Green Deployments" (2.0.0)

    kubectl apply -f 2.0.0-green/webshop-service.yaml

Testen mittels

   [https://container.mshome.net/webshop](https://container.mshome.net/webshop)

Canary Deployment
-----------------

Ein Canary Deployment baut auf dem soeben beschriebenen reinen Blue / Green Deployment auf, unterscheidet sich jedoch von diesem.
Der Unterschied ist, dass nicht auf einmal von alt (blau) nach neu (grün) umgeschaltet wird, sondern beide Versionen in einem Verhältnis (z.B. 90/10%) aktiv sind.

Um das Verhalten sichtbar zu machen, müssen wir zuerst die Anzahl Instanzen (Replicas) vom Service WebShop erhöhen.

    kubectl scale --replicas=4 deployment/webshop-blue

Anschliessend ist der Service WebShop ohne Selector "version" zu aktivieren. Die Deklaration befindet sich im Hauptverzeichnis

    cd ..
    kubectl apply -f webshop-service.yaml

Testen mittels

   [https://container.mshome.net/webshop](https://container.mshome.net/webshop)

Bei vier "Blue Deployments" (1.0.0) gegenüber eines "Green Deployments" (2.0.0) haben wir ein Verhältnis von 80%/20%.

