FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app

## copy both 'package.json' and 'package-lock.json'
COPY ./vue_app/package*.json ./

## copy configuration 'vue.config.js' and 'babel.config.js'
COPY ./vue_app/*.config.js ./

COPY ./vue_app/public ./public
COPY ./vue_app/src ./src
RUN ls -lah
# install project dependencies
RUN npm install

EXPOSE 8080
CMD ["npm", "run", "serve"]

## build app for production with minification
#RUN npm run build
#
### compiles and hot-reloads for development
##RUN npm run serve
#
#CMD [ "http-server", "dist" ]
