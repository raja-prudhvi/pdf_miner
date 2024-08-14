
# PDF Miner Infrastructure Setup

This assignment involves three repositories:

1. **[pdf_miner_infra](https://github.com/raja-prudhvi/pdf_miner_infra):** This repository contains the infrastructure setup needed for the assignment.
2. **[pdf_miner_modules](https://github.com/raja-prudhvi/pdf_miner_modules):** This repository contains the Terraform modules. Note that although there is code for PostgreSQL, we are not using PostgreSQL for this assignment.
3. **[pdf_miner](https://github.com/raja-prudhvi/pdf_miner):** This repository contains the application code.

## Steps to Deploy the Application on Kubernetes

### 1. Infrastructure Setup
First, ensure that the core infrastructure is up and running using the `core_infra` module.

- Authenticate with GCP using a service account.
- Navigate to the `pdf_miner_infra` directory:
  ```bash
  cd pdf_miner_infra/environments/dev
  ```
- Initialize Terraform:
  ```bash
  terraform init
  ```
- Plan and apply the core infrastructure module:
  ```bash
  terraform plan -target=module.core_infra
  terraform apply -target=module.core_infra
  ```

### 2. Build and Push the Docker Image
Once the infrastructure is ready, build and push the Docker image to Google Artifact Registry.

- In the `pdf_miner` directory, build the Docker image:
  ```bash
  docker build --platform linux/amd64 -t pdf_miner .
  ```
- Tag the image:
  ```bash
  docker tag pdf_miner gcr.io/prudhvir8901/pdf_miner:latest
  ```
- Push the image:
  ```bash
  docker push gcr.io/prudhvir8901/pdf_miner:latest
  ```

### 3. Deploy the Application
- Navigate to the `scripts` directory and deploy the application using the deployment file:
  ```bash
  kubectl apply -f deployment.yaml
  ```
- Check the status of the pods:
  ```bash
  kubectl get pods -n default
  ```
  Example output:
  ```
  NAME                                    READY   STATUS    RESTARTS   AGE
  pdf-miner-deployment-769df64b99-7z5b5   1/1     Running   0          114m
  pdf-miner-deployment-769df64b99-lr7cp   1/1     Running   0          114m
  ```

### 4. Expose the Application
- Apply the service configuration to expose the application:
  ```bash
  kubectl apply -f service.yaml
  ```
- Check the status of the services:
  ```bash
  kubectl get svc -A
  ```
  Example output:
  ```
  NAMESPACE     NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)            AGE
  default       pdf-miner              LoadBalancer   10.200.78.185   34.19.30.16   80:31570/TCP       151m
  ```

### 5. Test the Application
- You can now test the application using the provided external IP:
  ```bash
  curl http://34.19.30.16
  ```

If the application is running successfully, you should see the HTML output indicating that the install worked successfully.

### 6. Upload a PDF and Verify in SQLite
- Upload a PDF using the web interface.
- To verify that the PDF was uploaded successfully, copy the SQLite database to your local machine:
  ```bash
  kubectl cp default/pdf-miner-deployment-769df64b99-7z5b5:/app/db.sqlite3 ./db.sqlite3
  ```
- Open the SQLite database:
  ```bash
  sqlite3 db.sqlite3
  ```
- Check the contents of the `core_uploadedfile` table:
  ```sql
  SELECT * FROM core_uploadedfile;
  ```

### Notes:
- The PostgreSQL module was not used due to permission issues. The SQLite database was chosen as an alternative.
- The PostgreSQL module was successfully deployed but had issues connecting from GKE, despite the connection being successful using netcat.

### Final Comments:
- The entrypoint script was modified to bypass PostgreSQL and use SQLite instead.
- Repositories will be made private once the assignment is complete.
