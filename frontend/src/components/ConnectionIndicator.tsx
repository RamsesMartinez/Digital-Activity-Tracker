import React from 'react';
import { motion } from 'framer-motion';
import { Wifi, WifiOff } from 'lucide-react';

interface ConnectionIndicatorProps {
  isConnected: boolean;
}

export const ConnectionIndicator: React.FC<ConnectionIndicatorProps> = ({ isConnected }) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      className={`fixed top-5 right-5 z-50 flex items-center gap-2 px-4 py-2 rounded-full text-sm font-semibold backdrop-blur-lg ${
        isConnected 
          ? 'bg-green-500/90 text-white' 
          : 'bg-red-500/90 text-white'
      }`}
    >
      {isConnected ? <Wifi size={16} /> : <WifiOff size={16} />}
      <span>{isConnected ? 'Real-time Connected' : 'Offline'}</span>
    </motion.div>
  );
}; 