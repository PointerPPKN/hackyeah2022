FROM node:latest

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
CMD npm run dev
