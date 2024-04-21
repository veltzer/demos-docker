FROM node:latest
WORKDIR /app
COPY server.js /app
COPY package.json /app
COPY package-lock.json /app
RUN npm install
CMD ["server.js"]
