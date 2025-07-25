import React from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Dashboard } from './components/Dashboard';

// Create a client
const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Dashboard />
    </QueryClientProvider>
  );
}

export default App;
