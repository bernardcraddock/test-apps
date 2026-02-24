'use client';

import { useState, useEffect, useRef } from 'react';
import { Play, Pause, RotateCcw } from 'lucide-react';
import { cn } from '@/utils/cn';

export default function PomodoroTimer() {
  const [timeLeft, setTimeLeft] = useState(25 * 60);
  const [isActive, setIsActive] = useState(false);
  const [initialTime, setInitialTime] = useState(25 * 60);
  
  const timerRef = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    if (isActive && timeLeft > 0) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => prev - 1);
      }, 1000);
    } else if (timeLeft === 0) {
      setIsActive(false);
      // Play sound or notify
      if (timerRef.current) clearInterval(timerRef.current);
    }

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [isActive, timeLeft]);

  const toggleTimer = () => setIsActive(!isActive);
  
  const resetTimer = () => {
    setIsActive(false);
    setTimeLeft(initialTime);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const progress = ((initialTime - timeLeft) / initialTime) * 100;
  const radius = 80;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (progress / 100) * circumference;

  return (
    <div className="glass-panel p-6 rounded-2xl flex flex-col items-center justify-center min-h-[300px]">
      <h2 className="text-xl font-semibold mb-6 text-neutral-200">Focus Timer</h2>
      
      <div className="relative mb-8">
        {/* Ring Background */}
        <svg className="transform -rotate-90 w-48 h-48">
          <circle
            cx="96"
            cy="96"
            r={radius}
            stroke="currentColor"
            strokeWidth="8"
            fill="transparent"
            className="text-neutral-800"
          />
          {/* Progress Ring */}
          <circle
            cx="96"
            cy="96"
            r={radius}
            stroke="currentColor"
            strokeWidth="8"
            fill="transparent"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            className="text-indigo-500 transition-all duration-1000 ease-linear"
          />
        </svg>
        
        {/* Time Display */}
        <div className="absolute inset-0 flex items-center justify-center">
          <span className="text-4xl font-mono font-bold tracking-wider">
            {formatTime(timeLeft)}
          </span>
        </div>
      </div>

      <div className="flex gap-4">
        <button
          onClick={toggleTimer}
          className={cn(
            "p-4 rounded-full transition-all duration-300",
            isActive 
              ? "bg-amber-500/20 text-amber-500 hover:bg-amber-500/30"
              : "bg-indigo-500 text-white hover:bg-indigo-600 shadow-lg shadow-indigo-500/30"
          )}
        >
          {isActive ? <Pause className="w-6 h-6" /> : <Play className="w-6 h-6 ml-1" />}
        </button>
        
        <button
          onClick={resetTimer}
          className="p-4 rounded-full bg-neutral-800 text-neutral-400 hover:bg-neutral-700 hover:text-white transition-all"
        >
          <RotateCcw className="w-6 h-6" />
        </button>
      </div>
    </div>
  );
}
