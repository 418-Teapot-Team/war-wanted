FROM node:lts-alpine AS app

RUN npm install -g serve

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN echo "VITE_BASE_API=http://34.107.31.175:8001/api" > .env

RUN npm run build

EXPOSE 3003
CMD [ "serve", "-s", "-p", "3003", "dist" ]
