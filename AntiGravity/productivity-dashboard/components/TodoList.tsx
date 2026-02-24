'use client';

import { useState, useEffect } from 'react';
import { Plus, Trash2, CheckCircle2, Circle } from 'lucide-react';
import { cn } from '@/utils/cn';

interface Todo {
  id: string;
  text: string;
  completed: boolean;
}

export default function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem('todos');
    if (saved) {
      try {
        setTodos(JSON.parse(saved));
      } catch (e) {
        console.error('Failed to parse todos', e);
      }
    }
    setIsLoaded(true);
  }, []);

  useEffect(() => {
    if (isLoaded) {
      localStorage.setItem('todos', JSON.stringify(todos));
    }
  }, [todos, isLoaded]);

  const addTodo = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    setTodos([
      { id: crypto.randomUUID(), text: inputValue.trim(), completed: false },
      ...todos
    ]);
    setInputValue('');
  };

  const toggleTodo = (id: string) => {
    setTodos(todos.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
  };

  const deleteTodo = (id: string) => {
    setTodos(todos.filter(t => t.id !== id));
  };

  if (!isLoaded) return null;

  return (
    <div className="glass-panel p-6 rounded-2xl h-full flex flex-col min-h-[300px]">
      <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
        <CheckCircle2 className="w-5 h-5 text-emerald-400" />
        Tasks
      </h2>
      
      <form onSubmit={addTodo} className="relative mb-6">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Add a new task..."
          className="w-full bg-neutral-900/50 border border-neutral-800 rounded-xl py-3 pl-4 pr-12 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 placeholder:text-neutral-600 transition-all"
        />
        <button 
          type="submit"
          className="absolute right-2 top-2 p-1.5 bg-emerald-500/10 text-emerald-500 rounded-lg hover:bg-emerald-500/20 transition-colors"
        >
          <Plus className="w-5 h-5" />
        </button>
      </form>

      <div className="flex-1 overflow-y-auto space-y-2 pr-2 custom-scrollbar">
        {todos.length === 0 ? (
          <div className="text-center text-neutral-600 mt-10">
            <p>No tasks yet.</p>
            <p className="text-sm">Stay focused and organized!</p>
          </div>
        ) : (
          todos.map(todo => (
            <div 
              key={todo.id}
              className="group flex items-center gap-3 p-3 rounded-xl hover:bg-white/5 transition-colors"
            >
              <button 
                onClick={() => toggleTodo(todo.id)}
                className={cn(
                  "flex-shrink-0 transition-colors",
                  todo.completed ? "text-emerald-500" : "text-neutral-600 hover:text-neutral-400"
                )}
              >
                {todo.completed ? <CheckCircle2 className="w-5 h-5" /> : <Circle className="w-5 h-5" />}
              </button>
              
              <span className={cn(
                "flex-1 truncate transition-all",
                todo.completed && "text-neutral-600 line-through"
              )}>
                {todo.text}
              </span>

              <button 
                onClick={() => deleteTodo(todo.id)}
                className="opacity-0 group-hover:opacity-100 p-1.5 text-neutral-500 hover:text-red-400 hover:bg-red-400/10 rounded-lg transition-all"
              >
                <Trash2 className="w-4 h-4" />
              </button>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
