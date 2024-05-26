Autoshop Kubernetes
===================

[[_TOC_]]

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

    [https://container.mshome.net:8443](https://container.mshome.net:8443)

Rolling Update
--------------

Ein Rolling Update in Kubernetes ist eine Methode zur kontinuierlichen und unterbrechungsfreien Aktualisierung von Anwendungen, die in einem Kubernetes-Cluster bereitgestellt werden. Diese Art von Update ermöglicht es, neue Versionen von Anwendungen schrittweise einzuführen, während die alten Versionen noch aktiv sind

Werden die Container mittels Deployments gestartet, kann ein Rolling Update durchgeführt werden.

Dazu die Applikation zuerst als Version 1.0.0 mittels Deployments starten, Webseite und evtl. Dashboard anwählen.

Dann die Befehle von Version 2.0.0 zum Ausrollen der Deployments ausführen.