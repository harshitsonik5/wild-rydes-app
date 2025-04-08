FROM node:18-alpine

WORKDIR /usr/src/app

COPY package.json ./
COPY app ./app

RUN npm install

EXPOSE 80
CMD ["npm", "start"]
