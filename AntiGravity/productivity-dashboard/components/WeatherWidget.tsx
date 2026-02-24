'use client';

import { useState, useEffect } from 'react';
import { Cloud, Sun, CloudRain, Wind, MapPin, Loader2 } from 'lucide-react';

interface WeatherData {
  temperature: number;
  windSpeed: number;
  conditionCode: number;
}

export default function WeatherWidget() {
  const [data, setData] = useState<WeatherData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Default to London for demo if geolocation fails or is denied
  const [coords, setCoords] = useState({ lat: 51.5074, lng: -0.1278 });
  const [locationName, setLocationName] = useState('London');

  useEffect(() => {
    // Try to get user location
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setCoords({
            lat: position.coords.latitude,
            lng: position.coords.longitude
          });
          setLocationName('Current Location');
        },
        (err) => {
          console.log("Using default location", err);
        }
      );
    }
  }, []);

  useEffect(() => {
    const fetchWeather = async () => {
      try {
        setLoading(true);
        const res = await fetch(
          `https://api.open-meteo.com/v1/forecast?latitude=${coords.lat}&longitude=${coords.lng}&current_weather=true`
        );
        const json = await res.json();
        
        setData({
          temperature: json.current_weather.temperature,
          windSpeed: json.current_weather.windspeed,
          conditionCode: json.current_weather.weathercode,
        });
      } catch (err) {
        setError('Failed to load weather');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchWeather();
  }, [coords]);

  const getWeatherIcon = (code: number) => {
    if (code <= 1) return <Sun className="w-12 h-12 text-amber-400" />;
    if (code <= 3) return <Cloud className="w-12 h-12 text-neutral-400" />;
    if (code <= 67) return <CloudRain className="w-12 h-12 text-blue-400" />;
    return <Wind className="w-12 h-12 text-teal-400" />;
  };

  const getConditionText = (code: number) => {
      if (code <= 1) return 'Clear';
      if (code <= 3) return 'Cloudy';
      if (code <= 67) return 'Rainy';
      return 'Windy/Stormy';
  };

  return (
    <div className="glass-panel p-6 rounded-2xl flex flex-col justify-between min-h-[200px]">
      <div className="flex justify-between items-start">
        <div>
          <h2 className="text-sm font-medium text-neutral-400 flex items-center gap-1 mb-1">
            <MapPin className="w-4 h-4" />
            {locationName}
          </h2>
          {loading ? (
             <div className="h-8 w-24 bg-neutral-800 animate-pulse rounded"></div>
          ) : (
             <p className="text-3xl font-bold bg-gradient-to-r from-neutral-100 to-neutral-400 bg-clip-text text-transparent">
               {data?.temperature}°C
             </p>
          )}
        </div>
        <div>
           {loading ? <Loader2 className="w-8 h-8 animate-spin text-neutral-600" /> : data && getWeatherIcon(data.conditionCode)}
        </div>
      </div>

      <div className="mt-4">
        {error ? (
          <p className="text-red-400 text-sm">{error}</p>
        ) : loading ? (
             <div className="space-y-2">
                 <div className="h-4 w-full bg-neutral-800 animate-pulse rounded"></div>
                 <div className="h-4 w-2/3 bg-neutral-800 animate-pulse rounded"></div>
             </div>
        ) : (
          <div className="space-y-1">
            <p className="text-lg font-medium text-neutral-200">
                {data && getConditionText(data.conditionCode)}
            </p>
            <div className="flex items-center gap-2 text-sm text-neutral-500">
               <Wind className="w-4 h-4" />
               <span>{data?.windSpeed} km/h Wind</span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
