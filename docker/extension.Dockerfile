FROM node:20-alpine

WORKDIR /app

COPY package.json pnpm-workspace.yaml ./
COPY apps/extension/package.json ./apps/extension/package.json
COPY packages/shared/package.json ./packages/shared/package.json

RUN corepack enable && pnpm install --ignore-scripts

COPY . .

EXPOSE 5173
CMD ["pnpm", "--filter", "@gojob/extension", "dev", "--", "--host", "0.0.0.0"]