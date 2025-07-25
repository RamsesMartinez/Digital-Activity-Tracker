export interface ActivityData {
  category: string;
  time_str: string;
}

export interface TrackingStatus {
  is_paused: boolean;
}

export interface ActivityUpdate {
  data: ActivityData[];
  status: TrackingStatus;
  timestamp: string;
}

export interface PauseToggleResponse {
  is_paused: boolean;
}

export interface ShutdownNotification {
  message: string;
  timestamp: string;
}

export interface ConnectionStatus {
  isConnected: boolean;
  lastUpdate: string;
}

export interface StatCard {
  title: string;
  value: string | number;
  icon: string;
  change: {
    type: 'positive' | 'negative' | 'neutral';
    text: string;
  };
  gradient: string;
}

export type CategoryType = 
  | 'development'
  | 'productivity' 
  | 'entertainment'
  | 'communication'
  | 'social'
  | 'learning'
  | 'design'
  | 'gaming'
  | 'other';

export interface CategoryBadge {
  category: string;
  type: CategoryType;
  time: string;
  percentage: number;
} 