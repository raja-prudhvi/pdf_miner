# Steps to build and push docker image to GCR ( Google container registry)

gcloud auth login
gcloud auth configure-docker
docker build -t gcr.io/prudhvir8901/pdf_miner:v1 .
docker push gcr.io/prudhvir8901/pdf_miner:v1


# Apply the Deployment
kubectl apply -f deployment.yaml

# Apply the LoadBalancer Service
kubectl apply -f service.yaml


# U can use kustomize if u want to inorder to deploy line by line, but we can ignore it for now.

U can check the connectivity by deploying nginx_gke_db_test.yaml on gke and test the 
connection from gke to db via netcat , steps to test are below

Steps :

kubectl apply -f nginx_gke_db_test.yaml 

POD_NAME=$(kubectl get pods -l app=nginx -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $POD_NAME -- bash
apt-get update && apt-get install -y netcat-openbsd
nc -zv <public-db-ip> 5432


i tested the  connection from gke to postgresql and it shows as [tcp/postgresql] succeeded!