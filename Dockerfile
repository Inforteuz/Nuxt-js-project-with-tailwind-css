# ---- Build stage ----
FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --prefer-offline

COPY . .

RUN npm run build

# ---- Production stage ----
FROM node:20-alpine

WORKDIR /app

COPY --from=builder /app/.output /app/.output

ENV NODE_ENV=production

EXPOSE 3000

CMD ["node", ".output/server/index.mjs"]
