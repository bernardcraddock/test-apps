'use client';

import { useState } from 'react';

export default function FlightSearch() {
    const [query, setQuery] = useState('');
    const [flights, setFlights] = useState([]);
    const [loading, setLoading] = useState(false);
    const [searched, setSearched] = useState(false);

    const handleSearch = async (e) => {
        e.preventDefault();
        if (!query) return;

        setLoading(true);
        setSearched(true);
        try {
            const res = await fetch(`/api/flights?flightNumber=${query}`);
            const data = await res.json();
            setFlights(data);
        } catch (error) {
            console.error('Error fetching flights:', error);
            setFlights([]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="w-full max-w-2xl mx-auto">
            {/* Search Input */}
            <form onSubmit={handleSearch} className="mb-8 flex gap-3">
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Enter flight number (e.g., AA123)"
                    className="flex-1 px-4 py-3 bg-white border border-slate-200 rounded-lg text-slate-900 placeholder-slate-400 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-all shadow-sm"
                />
                <button
                    type="submit"
                    disabled={loading}
                    className="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed"
                >
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </form>

            {/* Results */}
            {searched && (
                <div className="space-y-4">
                    {flights.length > 0 ? (
                        flights.map((flight) => (
                            <div
                                key={flight.flightNumber}
                                className="bg-white border border-slate-200 rounded-xl shadow-sm overflow-hidden hover:shadow-md transition-shadow duration-200"
                            >
                                {/* Header */}
                                <div className="px-6 py-4 border-b border-slate-100 flex justify-between items-center bg-slate-50/50">
                                    <div className="flex items-center gap-3">
                                        <span className="font-bold text-slate-900">{flight.airline}</span>
                                        <span className="px-2 py-1 bg-slate-100 text-slate-600 text-xs font-mono rounded">
                                            {flight.flightNumber}
                                        </span>
                                    </div>
                                    <div className="text-sm text-green-600 font-medium flex items-center gap-1">
                                        <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                                        On Time
                                    </div>
                                </div>

                                {/* Body */}
                                <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6 items-center">
                                    {/* Origin */}
                                    <div>
                                        <div className="text-3xl font-bold text-slate-900 mb-1">{flight.origin}</div>
                                        <div className="text-sm text-slate-500 mb-2">{flight.startLocation.split(',')[0]}</div>
                                        <div className="text-lg font-semibold text-blue-600">
                                            {new Date(flight.startTime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: true })}
                                        </div>
                                        <div className="text-xs text-slate-400 mt-1 font-mono">
                                            {flight.originTimezone}
                                        </div>
                                    </div>

                                    {/* Duration / Path */}
                                    <div className="flex flex-col items-center justify-center">
                                        <div className="text-xs text-slate-400 mb-2">4h 00m</div>
                                        <div className="w-full h-px bg-slate-200 relative">
                                            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-slate-100 p-1 rounded-full">
                                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="w-4 h-4 text-slate-400">
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M17.25 8.25L21 12m0 0l-3.75 3.75M21 12H3" />
                                                </svg>
                                            </div>
                                        </div>
                                    </div>

                                    {/* Destination */}
                                    <div className="text-right">
                                        <div className="text-3xl font-bold text-slate-900 mb-1">{flight.destination}</div>
                                        <div className="text-sm text-slate-500 mb-2">{flight.endLocation.split(',')[0]}</div>
                                        <div className="text-lg font-semibold text-blue-600">
                                            {new Date(flight.endTime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', hour12: true })}
                                        </div>
                                        <div className="text-xs text-slate-400 mt-1 font-mono">
                                            {flight.destinationTimezone}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))
                    ) : (
                        <div className="text-center py-12 bg-white border border-slate-200 rounded-xl border-dashed">
                            <p className="text-slate-500">No flights found for "{query}"</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}
