import React from 'react';
import { motion } from 'framer-motion';
import { Circle } from 'lucide-react';
import type { ActivityData } from '../types';

interface ActivityTableProps {
  data: ActivityData[];
}

export const ActivityTable: React.FC<ActivityTableProps> = ({ data }) => {
  if (data.length === 0) {
    return (
      <div className="text-center py-12">
        <Circle size={48} className="mx-auto text-gray-400 mb-4" />
        <h3 className="text-lg font-semibold text-gray-900 mb-2">No activity data yet</h3>
        <p className="text-gray-600">Start using your computer to see activity data</p>
      </div>
    );
  }

  const totalSeconds = data.reduce((sum, item) => {
    const parts = item.time_str.split(':').map(Number);
    return sum + (parts[0] * 3600 + parts[1] * 60 + parts[2]);
  }, 0);

  const getCategoryClass = (category: string): string => {
    const categoryLower = category.toLowerCase();
    if (categoryLower.includes('development') || categoryLower.includes('código')) return 'category-development';
    if (categoryLower.includes('productivity')) return 'category-productivity';
    if (categoryLower.includes('entertainment')) return 'category-entertainment';
    if (categoryLower.includes('communication')) return 'category-communication';
    if (categoryLower.includes('social')) return 'category-social';
    if (categoryLower.includes('learning')) return 'category-learning';
    if (categoryLower.includes('design')) return 'category-design';
    if (categoryLower.includes('gaming')) return 'category-gaming';
    return 'category-other';
  };

  return (
    <div className="overflow-x-auto">
      <table className="w-full">
        <thead>
          <tr className="border-b-2 border-gray-200">
            <th className="text-left py-4 px-6 text-sm font-semibold text-gray-600 uppercase tracking-wide">
              Activity Category
            </th>
            <th className="text-left py-4 px-6 text-sm font-semibold text-gray-600 uppercase tracking-wide">
              Time Spent
            </th>
            <th className="text-left py-4 px-6 text-sm font-semibold text-gray-600 uppercase tracking-wide">
              Percentage
            </th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => {
            const itemSeconds = (() => {
              const parts = item.time_str.split(':').map(Number);
              return parts[0] * 3600 + parts[1] * 60 + parts[2];
            })();
            const percentage = totalSeconds > 0 ? ((itemSeconds / totalSeconds) * 100).toFixed(1) : 0;
            const categoryClass = getCategoryClass(item.category);

            return (
              <motion.tr
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className="border-b border-gray-100 hover:bg-gray-50 transition-colors"
              >
                <td className="py-4 px-6">
                  <span className={`category-badge ${categoryClass}`}>
                    <Circle size={12} />
                    {item.category}
                  </span>
                </td>
                <td className="py-4 px-6 font-mono font-semibold text-primary-600">
                  {item.time_str}
                </td>
                <td className="py-4 px-6">
                  <div className="flex items-center gap-4">
                    <span className="font-semibold text-gray-900 min-w-[50px]">
                      {percentage}%
                    </span>
                    <div className="flex-1 bg-gray-200 rounded-full h-2">
                      <motion.div
                        initial={{ width: 0 }}
                        animate={{ width: `${percentage}%` }}
                        transition={{ delay: index * 0.1 + 0.5, duration: 0.8 }}
                        className="bg-gradient-to-r from-primary-500 to-secondary-500 h-2 rounded-full"
                      />
                    </div>
                  </div>
                </td>
              </motion.tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}; 