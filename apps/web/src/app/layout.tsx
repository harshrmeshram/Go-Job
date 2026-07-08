import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Alvest AI',
  description: 'AI-powered career assistant and job application companion.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
