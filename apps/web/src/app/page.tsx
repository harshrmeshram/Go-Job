import Link from 'next/link';

export default function HomePage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-950 px-6 py-16 text-white">
      <div className="max-w-2xl rounded-2xl border border-white/10 bg-white/10 p-10 shadow-2xl backdrop-blur">
        <p className="mb-4 text-sm uppercase tracking-[0.3em] text-cyan-300">Alvest AI</p>
        <h1 className="text-4xl font-semibold">Your career assistant workspace</h1>
        <p className="mt-4 text-lg text-slate-300">
          This placeholder dashboard will evolve into resume analysis, job matching, and application
          tracking workflows.
        </p>
        <div className="mt-8 flex gap-4">
          <Link href="/dashboard" className="rounded-full bg-cyan-500 px-5 py-3 font-medium text-slate-950">
            Open dashboard
          </Link>
          <Link href="/dashboard" className="rounded-full border border-white/20 px-5 py-3 font-medium text-white">
            Health check
          </Link>
        </div>
      </div>
    </main>
  );
}
