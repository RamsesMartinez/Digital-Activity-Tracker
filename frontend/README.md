# 🎨 Digital Activity Tracker - Frontend

Modern React frontend for the Digital Activity Tracker with TypeScript, Tailwind CSS, and real-time WebSocket communication.

## 🚀 Tech Stack

### **Core Technologies**
- **React 18** - Modern React with hooks and functional components
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool and development server

### **Styling & UI**
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Smooth animations and transitions
- **Lucide React** - Beautiful, customizable icons

### **Real-time Communication**
- **Socket.IO Client** - WebSocket communication with backend
- **React Query** - State management and caching

### **Development Tools**
- **ESLint** - Code linting
- **PostCSS** - CSS processing
- **Autoprefixer** - CSS vendor prefixing

## 📦 Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Lint code
npm run lint
```

## 🏗️ Project Structure

```
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Dashboard.tsx    # Main dashboard component
│   │   ├── StatCard.tsx     # Statistics card component
│   │   ├── ActivityTable.tsx # Activity table component
│   │   └── ConnectionIndicator.tsx # Connection status
│   ├── hooks/               # Custom React hooks
│   │   └── useSocket.ts     # WebSocket hook
│   ├── types/               # TypeScript type definitions
│   │   └── index.ts         # Main types
│   ├── App.tsx              # Main app component
│   ├── main.tsx             # App entry point
│   └── index.css            # Global styles
├── public/                  # Static assets
├── package.json             # Dependencies and scripts
├── tailwind.config.js       # Tailwind configuration
├── postcss.config.js        # PostCSS configuration
├── tsconfig.json            # TypeScript configuration
└── vite.config.ts           # Vite configuration
```

## 🎯 Features

### **Real-time Dashboard**
- **Live activity updates** via WebSocket
- **Connection status indicator**
- **Smooth animations** with Framer Motion
- **Responsive design** for all devices

### **Modern UI/UX**
- **Glass morphism effects** with backdrop blur
- **Gradient backgrounds** and modern color scheme
- **Interactive hover effects** and transitions
- **Professional typography** with Inter font

### **Type Safety**
- **Full TypeScript coverage**
- **Strict type checking**
- **IntelliSense support**
- **Compile-time error detection**

### **Performance**
- **Fast development** with Vite HMR
- **Optimized production builds**
- **Tree shaking** for smaller bundles
- **Lazy loading** capabilities

## 🔧 Configuration

### **Tailwind CSS**
Custom configuration with:
- **Primary colors** (purple/blue gradients)
- **Secondary colors** (pink/purple gradients)
- **Custom animations** (float, pulse)
- **Responsive breakpoints**

### **Socket.IO**
- **Automatic reconnection**
- **Error handling**
- **Event-driven architecture**
- **Type-safe events**

### **Development**
- **Hot Module Replacement** (HMR)
- **Fast refresh** for React components
- **Source maps** for debugging
- **ESLint integration**

## 🎨 Design System

### **Colors**
```css
/* Primary Colors */
--primary-50: #f0f4ff
--primary-500: #667eea
--primary-900: #3c366b

/* Secondary Colors */
--secondary-50: #fdf4ff
--secondary-500: #d946ef
--secondary-900: #701a75
```

### **Components**
- **StatCard** - Statistics display with hover effects
- **ActivityTable** - Data table with animations
- **ConnectionIndicator** - Real-time connection status
- **Dashboard** - Main layout with sidebar

### **Animations**
- **Fade in/out** transitions
- **Slide animations** for components
- **Hover effects** with scale transforms
- **Progress bar animations**

## 🔌 API Integration

### **WebSocket Events**
```typescript
// Client to Server
socket.emit('toggle_pause')
socket.emit('request_shutdown')

// Server to Client
socket.on('activity_update', (data: ActivityUpdate) => {})
socket.on('pause_toggled', (data: PauseToggleResponse) => {})
socket.on('shutdown_notification', (data: ShutdownNotification) => {})
```

### **Data Types**
```typescript
interface ActivityData {
  category: string;
  time_str: string;
}

interface ActivityUpdate {
  data: ActivityData[];
  status: TrackingStatus;
  timestamp: string;
}
```

## 🚀 Development

### **Quick Start**
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open browser
# http://localhost:5173
```

### **Backend Integration**
Make sure the Flask backend is running:
```bash
# In another terminal
cd ../
make run-app
```

### **Building for Production**
```bash
# Build the application
npm run build

# Preview production build
npm run preview
```

## 🧪 Testing

```bash
# Run tests (when implemented)
npm test

# Run tests in watch mode
npm test:watch

# Run tests with coverage
npm test:coverage
```

## 📱 Responsive Design

The frontend is fully responsive with:
- **Mobile-first** approach
- **Breakpoint system** (sm, md, lg, xl)
- **Flexible layouts** with CSS Grid and Flexbox
- **Touch-friendly** interactions

## 🔒 Security

- **Type-safe** WebSocket communication
- **Input validation** with TypeScript
- **XSS protection** with React
- **CORS handling** for API requests

## 📈 Performance

- **Bundle optimization** with Vite
- **Code splitting** for lazy loading
- **Tree shaking** for unused code removal
- **Image optimization** and compression

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests** (when applicable)
5. **Submit a pull request**

### **Code Style**
- **TypeScript strict mode**
- **ESLint configuration**
- **Prettier formatting**
- **Component documentation**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

---

**Built with ❤️ using React, TypeScript, and Tailwind CSS**
