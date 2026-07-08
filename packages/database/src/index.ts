export interface DatabaseConfig {
  url: string;
  poolSize: number;
}

export const defaultDatabaseConfig: DatabaseConfig = {
  url: process.env.DATABASE_URL ?? 'postgresql://postgres:postgres@localhost:5432/alvest',
  poolSize: 10,
};
