FROM --platform=linux/arm64 node:16 as build

WORKDIR /app

COPY package.json package-lock.json ./
RUN yarn install

COPY . .
RUN yarn run build

FROM --platform=linux/arm64 nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html/calculator
COPY --from=build /app/build/index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]