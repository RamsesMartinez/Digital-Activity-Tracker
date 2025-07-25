import React from 'react';
import { motion } from 'framer-motion';
import { LucideIcon } from 'lucide-react';

interface StatCardProps {
  title: string;
  value: string | number;
  icon: LucideIcon;
  change: {
    type: 'positive' | 'negative' | 'neutral';
    text: string;
  };
  gradient: string;
}

export const StatCard: React.FC<StatCardProps> = ({ 
  title, 
  value, 
  icon: Icon, 
  change, 
  gradient 
}) => {
  return (
    <motion.div
      whileHover={{ y: -8, scale: 1.02 }}
      className="stat-card"
    >
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold text-gray-900">{title}</h3>
        <div className={`w-10 h-10 rounded-xl bg-gradient-to-r ${gradient} flex items-center justify-center`}>
          <Icon size={20} className="text-white" />
        </div>
      </div>
      
      <div className="text-3xl font-bold text-gray-900 mb-2">{value}</div>
      
      <div className={`flex items-center gap-2 text-sm font-medium ${
        change.type === 'positive' ? 'text-green-600' : 
        change.type === 'negative' ? 'text-red-600' : 'text-gray-600'
      }`}>
        <span>●</span>
        <span>{change.text}</span>
      </div>
    </motion.div>
  );
}; 