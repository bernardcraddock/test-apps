import { NextResponse } from 'next/server';

const FLIGHTS = [
  {
    flightNumber: 'AA123',
    airline: 'American Airlines',
    origin: 'JFK',
    destination: 'LAX',
    startTime: '2023-11-25T06:00:00-08:00', // 06:00 AM PST (Mocked for simplicity)
    endTime: '2023-11-25T10:00:00-08:00',   // 10:00 AM PST
    startLocation: 'New York, NY',
    endLocation: 'Los Angeles, CA',
    originTimezone: 'America/New_York',
    destinationTimezone: 'America/Los_Angeles',
  },
  {
    flightNumber: 'BA456',
    airline: 'British Airways',
    origin: 'LHR',
    destination: 'JFK',
    startTime: '2023-11-26T10:00:00Z',
    endTime: '2023-11-26T13:00:00-05:00',
    startLocation: 'London, UK',
    endLocation: 'New York, NY',
    originTimezone: 'Europe/London',
    destinationTimezone: 'America/New_York',
  },
  {
    flightNumber: 'QF1',
    airline: 'Qantas',
    origin: 'SYD',
    destination: 'LHR',
    startTime: '2023-11-27T16:00:00+11:00',
    endTime: '2023-11-28T06:00:00Z',
    startLocation: 'Sydney, Australia',
    endLocation: 'London, UK',
    originTimezone: 'Australia/Sydney',
    destinationTimezone: 'Europe/London',
  },
  {
    flightNumber: 'UA789',
    airline: 'United Airlines',
    origin: 'SFO',
    destination: 'NRT',
    startTime: '2023-11-28T11:00:00-08:00',
    endTime: '2023-11-29T15:00:00+09:00',
    startLocation: 'San Francisco, CA',
    endLocation: 'Tokyo, Japan',
    originTimezone: 'America/Los_Angeles',
    destinationTimezone: 'Asia/Tokyo',
  }
];

export async function GET(request) {
  const { searchParams } = new URL(request.url);
  const query = searchParams.get('flightNumber');

  if (!query) {
    return NextResponse.json(FLIGHTS);
  }

  const filteredFlights = FLIGHTS.filter((flight) =>
    flight.flightNumber.toLowerCase().includes(query.toLowerCase())
  );

  return NextResponse.json(filteredFlights);
}
