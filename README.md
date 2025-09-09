# Elevate CI/CD Demo

This is a demo project showing how to build a CI/CD pipeline using GitHub Actions and Docker.

## Features
- Simple Flask app with tests
- Dockerfile + Docker Compose
- GitHub Actions workflow: test, build, push image to Docker Hub
- Kubernetes manifests for Minikube deployment

## Usage

### Run locally with Docker Compose
```bash
docker-compose up --build
# Visit http://localhost:5000
```

### Run tests locally
```bash
pytest -q
```

### CI/CD with GitHub Actions
1. Push to `main` branch
2. Workflow will run tests, build Docker image, and push to Docker Hub: `pranushdeepu/elevate`

### Deploy on Minikube
```bash
minikube start
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
minikube service elevate-svc --url
```

## Secrets Required in GitHub
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

