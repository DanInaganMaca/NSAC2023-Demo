FROM node:18.18-alpine as node-react-cli

WORKDIR /app

COPY react_app/package*.json .

COPY react_app .

RUN npm run build

CMD ["npm", "start"]
