import Dashboard from "@/components/Dashboard";
import TodoList from "@/components/TodoList";
import PomodoroTimer from "@/components/PomodoroTimer";
import WeatherWidget from "@/components/WeatherWidget";

export default function Home() {
  return (
    <Dashboard>
      <div className="md:col-span-2 h-full">
        <TodoList />
      </div>
      <div className="md:col-span-1 space-y-6">
        <PomodoroTimer />
        <WeatherWidget />
      </div>
    </Dashboard>
  );
}
