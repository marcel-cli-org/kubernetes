CloudEvents
-----------

Testcontainer um [CloudEvents](https://cloudevents.io/) zu testen.

    podman build -t registry.gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/cloudevents .
    podman push registry.gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/cloudevents    
    
Als Debugging Container ohne cloudevents.py    
    
    podman run --rm -it registry.gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/cloudevents bash
    
Als Cloudevents Endpunkt

    podman run --rm -d --name cloudevents -p9090:8080 registry.gitlab.com/ch-mc-b/autoshop-ms/infra/kubernetes-templates/cloudevents
    
Testen

curl -X POST http://localhost:9090/event \
-H "Content-Type: application/json" \
-H "ce-id: 1234" \
-H "ce-source: /mycontext" \
-H "ce-type: my.type" \
-H "ce-specversion: 1.0" \
-H "ce-time: 2020-08-19T13:37:00Z" \
-d '{
  "data": {
    "key1": "value1",
    "key2": "value2"
  },
  "subject": "example"
}'

curl -v -X POST http://localhost:9090/event \
-H "Ce-Id: say-hello" \
-H "Ce-Specversion: 1.0" \
-H "Ce-Type: bonjour" \
-H "Ce-Source: mycurl" \
-H "Content-Type: application/json" \
-d '{"key":"from a a"}'


curl -v -X POST http://broker-ingress.knative-eventing.svc.cluster.local/ms-brkr/default \
-H "Ce-Id: say-hello" \
-H "Ce-Specversion: 1.0" \
-H "Ce-Type: bonjour" \
-H "Ce-Source: mycurl" \
-H "Content-Type: application/json" \
-d '{"key":"from a a"}'

curl -v -X POST http://broker-ingress.knative-eventing.svc.cluster.local/ms-brkr/default \
-H "Ce-Id: say-hello" \
-H "Ce-Specversion: 1.0" \
-H "Ce-Type: aloha" \
-H "Ce-Source: mycurl" \
-H "Content-Type: application/json" \
-d '{"key":"from a b"}'

curl -v -X POST http://broker-ingress.knative-eventing.svc.cluster.local/ms-brkr/default  \
-H "Ce-Id: say-hello" \
-H "Ce-Specversion: 1.0" \
-H "Ce-Type: order" \
-H "Ce-Source: order" \
-H "Content-Type: application/json" \
-d '{"key":"from a order"}'
        