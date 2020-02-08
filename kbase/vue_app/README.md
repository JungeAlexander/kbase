
docker build -t vuejs-cookbook/dockerize-vuejs-app .

docker run -it -p 8080:8080 -v ./vue_app:/app--rm --name dockerize-vuejs-app-1 vuejs-cookbook/dockerize-vuejs-app
