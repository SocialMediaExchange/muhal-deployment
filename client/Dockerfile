# build stage
FROM node:14.4.0-alpine3.10 
RUN apk add tar

WORKDIR /app

ADD https://api.github.com/repos/SocialMediaExchange/muhal-client/tarball/main main.zip
RUN mkdir client 
RUN tar xvf main.zip -C client --strip-components 1

WORKDIR /app/client
RUN npm install
RUN npm run build
ENV HOST 0.0.0.0
ENV BASE_API_URL /api
CMD ["npm", "run", "start"]
