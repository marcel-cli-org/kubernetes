Debugging Container
-------------------

### debug.yaml

Ubuntu 24.x Umgebung. Startet als Container und wartet.

Starten mittels

    kubectl apply -f debug/debug.yaml
    
Wechseln in Container

    kubectl exec -it debug -- bash    
    
Im Container können alle benötigten Tools mittels `apt-get` installiert werden, z.B.

    apt-get update
    apt-get install -y curl wget git    
    
    