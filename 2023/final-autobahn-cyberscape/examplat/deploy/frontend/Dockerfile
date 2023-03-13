FROM nginx:stable-alpine as production-stage

RUN mkdir -p /app/html
COPY ./build /app/html
COPY ./default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]