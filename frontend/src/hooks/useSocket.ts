import { useEffect, useState, useCallback } from 'react';
import { io } from 'socket.io-client';
import type { 
  ActivityUpdate, 
  PauseToggleResponse, 
  ShutdownNotification,
  ConnectionStatus 
} from '../types';

const SOCKET_URL = 'http://localhost:5000';

export const useSocket = () => {
  const [socket, setSocket] = useState<any>(null);
  const [connectionStatus, setConnectionStatus] = useState<ConnectionStatus>({
    isConnected: false,
    lastUpdate: '--'
  });
  const [activityData, setActivityData] = useState<ActivityUpdate | null>(null);

  // Initialize socket connection
  useEffect(() => {
    const newSocket = io(SOCKET_URL);
    setSocket(newSocket);

    // Connection events
    newSocket.on('connect', () => {
      console.log('🔗 Connected to server');
      setConnectionStatus(prev => ({
        ...prev,
        isConnected: true
      }));
    });

    newSocket.on('disconnect', () => {
      console.log('🔌 Disconnected from server');
      setConnectionStatus(prev => ({
        ...prev,
        isConnected: false
      }));
    });

    newSocket.on('connect_error', (error: Error) => {
      console.error('❌ Connection error:', error);
      setConnectionStatus(prev => ({
        ...prev,
        isConnected: false
      }));
    });

    // Activity updates
    newSocket.on('activity_update', (data: ActivityUpdate) => {
      console.log('📊 Received real-time update:', data);
      setActivityData(data);
      setConnectionStatus(prev => ({
        ...prev,
        lastUpdate: new Date(data.timestamp).toLocaleTimeString()
      }));
    });

    // Pause toggle confirmation
    newSocket.on('pause_toggled', (data: PauseToggleResponse) => {
      console.log('⏸️ Pause toggled:', data);
      if (activityData) {
        setActivityData(prev => prev ? {
          ...prev,
          status: { is_paused: data.is_paused }
        } : null);
      }
    });

    // Shutdown notification
    newSocket.on('shutdown_notification', (data: ShutdownNotification) => {
      console.log('🛑 Shutdown notification:', data);
      // Handle shutdown UI
    });

    return () => {
      newSocket.close();
    };
  }, []);

  // Socket actions
  const togglePause = useCallback(() => {
    if (socket && connectionStatus.isConnected) {
      socket.emit('toggle_pause');
    }
  }, [socket, connectionStatus.isConnected]);

  const requestShutdown = useCallback(() => {
    if (socket && connectionStatus.isConnected) {
      socket.emit('request_shutdown');
    }
  }, [socket, connectionStatus.isConnected]);

  return {
    socket,
    connectionStatus,
    activityData,
    togglePause,
    requestShutdown,
    isConnected: connectionStatus.isConnected
  };
}; 