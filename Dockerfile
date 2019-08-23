FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY ./frontend/dist /usr/share/nginx/html/frontend
EXPOSE 80 443