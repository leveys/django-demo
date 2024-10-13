FROM node:latest
 
WORKDIR /app
 
COPY package.json package-lock.json /app/
 
RUN npm install -g pnpm
RUN pnpm install

CMD [ "pnpm", "dev:docker" ]