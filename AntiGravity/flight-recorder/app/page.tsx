import FlightSearch from './components/FlightSearch';

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center py-20 px-4 bg-slate-50">
      <div className="w-full max-w-4xl">
        <div className="text-center mb-12">
          <h1 className="text-3xl font-bold text-slate-900 tracking-tight mb-2">
            Flight Lookup
          </h1>
          <p className="text-slate-500">
            Track flight status and details in real-time.
          </p>
        </div>

        <FlightSearch />
      </div>
    </main>
  );
}
