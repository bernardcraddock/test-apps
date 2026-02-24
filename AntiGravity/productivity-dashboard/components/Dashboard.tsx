import React from 'react';

export default function Dashboard({ children }: { children?: React.ReactNode }) {
  return (
    <main className="min-h-screen bg-neutral-950 text-neutral-100 p-8 flex items-center justify-center">
      <div className="w-full max-w-5xl grid grid-cols-1 md:grid-cols-3 gap-6">
        {children}
      </div>
    </main>
  );
}
