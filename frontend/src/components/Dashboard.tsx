import React from 'react';
import { motion } from 'framer-motion';
import { 
  Activity, 
  Clock, 
  Trophy, 
  Pause, 
  Play, 
  Power, 
  Wifi, 
  WifiOff,
  TrendingUp,
  Circle
} from 'lucide-react';
import { useSocket } from '../hooks/useSocket';
import { StatCard } from './StatCard';
import { ActivityTable } from './ActivityTable';
import { ConnectionIndicator } from './ConnectionIndicator';

export const Dashboard: React.FC = () => {
  const { 
    connectionStatus, 
    activityData, 
    togglePause, 
    requestShutdown, 
    isConnected 
  } = useSocket();

  const isPaused = activityData?.status.is_paused ?? false;

  const handleTogglePause = () => {
    if (isConnected) {
      togglePause();
    } else {
      alert('Not connected to server. Please refresh the page.');
    }
  };

  const handleShutdown = () => {
    if (confirm("Are you sure you want to stop the application? Tracking will be completely stopped.")) {
      if (isConnected) {
        requestShutdown();
      } else {
        alert('Not connected to server. Please refresh the page.');
      }
    }
  };

  const stats = [
    {
      title: "Active Categories",
      value: activityData?.data.length ?? 0,
      icon: Activity,
      change: { type: 'positive' as const, text: 'Real-time tracking' },
      gradient: 'from-primary-500 to-primary-600'
    },
    {
      title: "Total Time",
      value: formatTotalTime(activityData?.data ?? []),
      icon: Clock,
      change: { type: 'positive' as const, text: 'Accumulating' },
      gradient: 'from-green-500 to-green-600'
    },
    {
      title: "Top Category",
      value: getTopCategory(activityData?.data ?? []),
      icon: Trophy,
      change: { type: 'positive' as const, text: 'Most active' },
      gradient: 'from-yellow-500 to-yellow-600'
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-500 to-secondary-600">
      {/* Connection Indicator */}
      <ConnectionIndicator isConnected={isConnected} />
      
      <div className="flex">
        {/* Sidebar */}
        <motion.div 
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          className="w-20 bg-white/10 backdrop-blur-lg border-r border-white/20 flex flex-col items-center py-8 fixed h-screen z-50"
        >
          <div className="w-12 h-12 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl flex items-center justify-center text-white font-bold text-lg mb-8">
            DT
          </div>
          
          <div className="space-y-4">
            <div className="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center text-white cursor-pointer hover:bg-white/30 transition-all">
              <Activity size={20} />
            </div>
            <div className="w-12 h-12 bg-white/10 rounded-xl flex items-center justify-center text-white/70 cursor-pointer hover:bg-white/20 transition-all">
              <Clock size={20} />
            </div>
            <div className="w-12 h-12 bg-white/10 rounded-xl flex items-center justify-center text-white/70 cursor-pointer hover:bg-white/20 transition-all">
              <Trophy size={20} />
            </div>
          </div>
        </motion.div>

        {/* Main Content */}
        <div className="flex-1 ml-20 p-8">
          {/* Header */}
          <motion.div 
            initial={{ y: -50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            className="glass-card p-8 mb-8 relative overflow-hidden"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-primary-500/20 to-secondary-500/20 animate-float"></div>
            <div className="relative z-10">
              <p className="text-white/90 text-lg mb-2">Hi there! 👋</p>
              <h1 className="text-4xl font-bold text-white mb-4">Digital Activity Tracker</h1>
              <p className="text-white/80 text-lg mb-8">Monitor your productivity patterns in real-time</p>
              
              <div className="flex gap-6">
                <div className="flex items-center gap-3 bg-white/10 backdrop-blur-lg rounded-xl px-6 py-3">
                  <div className={`w-4 h-4 rounded-full ${isPaused ? 'bg-yellow-400' : 'bg-green-400'}`}>
                    <Circle size={12} className="text-white" />
                  </div>
                  <span className="text-white font-medium">
                    {isPaused ? 'Tracking Paused' : 'Tracking Active'}
                  </span>
                </div>
                
                <div className="flex items-center gap-3 bg-white/10 backdrop-blur-lg rounded-xl px-6 py-3">
                  <Clock size={16} className="text-white" />
                  <span className="text-white font-medium">
                    Last update: {connectionStatus.lastUpdate}
                  </span>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Stats Grid */}
          <motion.div 
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.2 }}
            className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8"
          >
            {stats.map((stat, index) => (
              <StatCard key={index} {...stat} />
            ))}
          </motion.div>

          {/* Activity Section */}
          <motion.div 
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.4 }}
            className="bg-white rounded-2xl p-8 shadow-xl"
          >
            <div className="flex justify-between items-center mb-8">
              <h2 className="text-2xl font-bold text-gray-900">Activity Breakdown</h2>
              
              <div className="flex gap-4">
                <button
                  onClick={handleTogglePause}
                  className={`flex items-center gap-2 px-6 py-3 rounded-xl font-semibold transition-all ${
                    isPaused 
                      ? 'bg-gradient-to-r from-primary-500 to-primary-600 text-white hover:from-primary-600 hover:to-primary-700' 
                      : 'bg-gradient-to-r from-yellow-500 to-yellow-600 text-white hover:from-yellow-600 hover:to-yellow-700'
                  }`}
                >
                  {isPaused ? <Play size={16} /> : <Pause size={16} />}
                  {isPaused ? 'Resume' : 'Pause'}
                </button>
                
                <button
                  onClick={handleShutdown}
                  className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white rounded-xl font-semibold transition-all"
                >
                  <Power size={16} />
                  Shutdown
                </button>
              </div>
            </div>

            <ActivityTable data={activityData?.data ?? []} />
          </motion.div>
        </div>
      </div>
    </div>
  );
};

// Utility functions
function formatTotalTime(data: any[]): string {
  if (data.length === 0) return '00:00:00';
  
  const totalSeconds = data.reduce((sum, item) => {
    const parts = item.time_str.split(':').map(Number);
    return sum + (parts[0] * 3600 + parts[1] * 60 + parts[2]);
  }, 0);
  
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  
  return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function getTopCategory(data: any[]): string {
  if (data.length === 0) return '-';
  return data[0].category.split(' - ')[0] || data[0].category;
} 