# 🚀 Digital Activity Tracker

> **Real-time productivity monitoring with modern React frontend and Flask backend**

A sophisticated activity tracking application that monitors your digital productivity patterns in real-time. Features a modern React + TypeScript frontend with WebSocket communication and a robust Flask backend with intelligent activity categorization.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![React](https://img.shields.io/badge/react-18.2.0-blue.svg)
![TypeScript](https://img.shields.io/badge/typescript-5.2.2-blue.svg)
![WebSocket](https://img.shields.io/badge/websocket-socket.io-green.svg)
![macOS](https://img.shields.io/badge/macOS-supported-lightgrey.svg)

## ✨ Features

### 🎯 **Real-time Activity Tracking**
- **WebSocket-powered updates** - No HTTP polling required
- **Live activity monitoring** - Track applications and browser usage
- **Smart categorization** - Automatic classification of activities
- **Instant feedback** - Real-time dashboard updates

### 🎨 **Modern User Experience**
- **React 18 + TypeScript** - Type-safe, modern frontend
- **Tailwind CSS** - Beautiful, responsive design
- **Framer Motion** - Smooth animations and transitions
- **Glass morphism effects** - Modern UI with backdrop blur
- **Responsive design** - Works on all devices

### 🔧 **Intelligent Backend**
- **Flask + Socket.IO** - Robust real-time communication
- **AppleScript integration** - macOS system monitoring
- **Smart activity detection** - Browser URL tracking
- **Configurable categories** - Customizable activity mapping
- **Threading support** - Non-blocking activity tracking

### 📊 **Advanced Analytics**
- **Real-time statistics** - Live category breakdown
- **Time tracking** - Detailed activity duration
- **Progress visualization** - Interactive charts and progress bars
- **Export capabilities** - CSV report generation

## 🏗️ Architecture

### **Backend (Flask + Socket.IO)**
- **Activity Monitoring**: Continuous system activity tracking
- **WebSocket Server**: Real-time bidirectional communication
- **Data Processing**: Intelligent activity categorization
- **File Management**: CSV logging and data persistence

### **Frontend (React + TypeScript)**
- **Modern UI**: React 18 with TypeScript for type safety
- **Real-time Updates**: Socket.IO client for live data
- **State Management**: React Query for efficient data handling
- **Styling**: Tailwind CSS with custom design system

### **Data Flow**
1. **System Monitoring** → AppleScript captures active applications
2. **Activity Processing** → Flask categorizes and logs activities
3. **Real-time Emission** → WebSocket pushes updates to clients
4. **UI Updates** → React components render live data
5. **User Interaction** → Controls sent back via WebSocket

## 🚀 Quick Start

### **Prerequisites**
- **Python 3.8+**
- **Node.js 18+**
- **macOS** (for AppleScript integration)

### **Installation**

#### **Option 1: Backend Only (Original Dashboard)**
```bash
# Clone the repository
git clone <repository-url>
cd tasks-manager

# Install and run backend
make setup-and-run

# Open dashboard
# http://127.0.0.1:5000
```

#### **Option 2: Full Stack (React + Flask)**
```bash
# Clone the repository
git clone <repository-url>
cd tasks-manager

# Install backend dependencies
make install

# Install frontend dependencies
make frontend-install

# Start backend (Terminal 1)
make run-app

# Start frontend (Terminal 2)
make frontend-dev

# Open React dashboard
# http://localhost:5173
```

## 📋 Available Commands

### **Backend Commands**
```bash
make install          # Install Python dependencies
make run-app          # Start Flask backend
make run              # Alias for run-app
make run-reporter     # Generate activity report
make setup-and-run    # Install and start backend
make clean            # Remove virtual environment
```

### **Frontend Commands**
```bash
make frontend-install # Install React dependencies
make frontend-dev     # Start React development server
make frontend-build   # Build React for production
make frontend-clean   # Clean frontend build
```

### **Development Commands**
```bash
make test            # Run tests (coming soon)
make lint            # Lint code (coming soon)
make format          # Format code (coming soon)
make help            # Show all available commands
```

## 🌐 URLs

- **Backend API**: http://127.0.0.1:5000
- **Original Dashboard**: http://127.0.0.1:5000
- **React Frontend**: http://localhost:5173

## ⚡ Real-time Features

### **WebSocket Communication**
- **Instant Updates**: No HTTP polling required
- **Bidirectional**: Client-server real-time communication
- **Connection Status**: Visual indicators for connection state
- **Automatic Reconnection**: Handles network interruptions

### **Live Activity Tracking**
- **Real-time Monitoring**: Continuous system activity capture
- **Smart Categorization**: Automatic activity classification
- **Live Statistics**: Instant category and time updates
- **Progress Visualization**: Real-time progress bars and charts

## 🎨 Design System

### **Color Palette**
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
- **StatCard**: Statistics display with hover effects
- **ActivityTable**: Data table with animations
- **ConnectionIndicator**: Real-time connection status
- **Dashboard**: Main layout with sidebar navigation

### **Animations**
- **Fade in/out**: Smooth component transitions
- **Slide animations**: Directional component movements
- **Hover effects**: Interactive element feedback
- **Progress bars**: Animated data visualization

## 🔧 Configuration

### **Activity Categories**
Edit `config.json` to customize activity mappings:

```json
{
  "applications": {
    "Visual Studio Code": "Development",
    "Xcode": "Development",
    "Terminal": "Development",
    "Slack": "Communication",
    "Discord": "Communication"
  },
  "browser_keywords": {
    "github.com": "Development",
    "stackoverflow.com": "Development",
    "youtube.com": "Entertainment",
    "netflix.com": "Entertainment",
    "linkedin.com": "Professional"
  }
}
```

### **Tracking Settings**
- **Check Interval**: 2 seconds (configurable)
- **Log File**: `activity_log.csv`
- **WebSocket Port**: 5000
- **React Dev Port**: 5173

## 📊 Data Structure

### **Activity Log Format**
```csv
timestamp,app_name,window_title,category
2025-07-25T10:30:00,Visual Studio Code,main.py - project,Development - Visual Studio Code
2025-07-25T10:30:02,Google Chrome,https://github.com,Development - Google Chrome
```

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

## 🛠️ Development

### **Project Structure**
```
tasks-manager/
├── app.py                 # Flask backend with WebSocket
├── reporter.py            # Activity report generator
├── config.json            # Activity categorization config
├── requirements.txt       # Python dependencies
├── Makefile              # Build and run commands
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules
├── CONTRIBUTING.md      # Contribution guidelines
└── frontend/            # React frontend
    ├── src/
    │   ├── components/   # React components
    │   ├── hooks/        # Custom React hooks
    │   ├── types/        # TypeScript definitions
    │   └── App.tsx       # Main app component
    ├── package.json      # Node.js dependencies
    ├── tailwind.config.js # Tailwind configuration
    └── README.md         # Frontend documentation
```

### **Key Technologies**

#### **Backend**
- **Flask**: Web framework
- **Flask-SocketIO**: WebSocket support
- **AppleScript**: macOS system integration
- **CSV**: Data persistence
- **Threading**: Non-blocking operations

#### **Frontend**
- **React 18**: UI framework
- **TypeScript**: Type safety
- **Vite**: Build tool and dev server
- **Tailwind CSS**: Utility-first styling
- **Framer Motion**: Animations
- **Socket.IO Client**: WebSocket communication
- **React Query**: State management
- **Lucide React**: Icon library

## 🔒 Security

- **Type-safe** WebSocket communication
- **Input validation** with TypeScript
- **XSS protection** with React
- **CORS handling** for API requests
- **Secure AppleScript** execution

## 📈 Performance

- **Fast development** with Vite HMR
- **Optimized production builds**
- **Tree shaking** for smaller bundles
- **Lazy loading** capabilities
- **Efficient WebSocket** communication

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **Development Setup**
1. **Fork the repository**
2. **Create a feature branch**
3. **Install dependencies**: `make install && make frontend-install`
4. **Start development servers**: `make run-app` and `make frontend-dev`
5. **Make your changes**
6. **Submit a pull request**

### **Code Style**
- **TypeScript strict mode**
- **ESLint configuration**
- **Prettier formatting**
- **Component documentation**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** team for the excellent web framework
- **React** team for the amazing UI library
- **Socket.IO** for real-time communication
- **Tailwind CSS** for the utility-first approach
- **Framer Motion** for smooth animations
- **Lucide** for beautiful icons

## 🗺️ Roadmap

### **Upcoming Features**
- [ ] **Data Export**: PDF and Excel report generation
- [ ] **Advanced Analytics**: Productivity insights and trends
- [ ] **Goal Setting**: Daily/weekly productivity goals
- [ ] **Notifications**: Break reminders and productivity alerts
- [ ] **Multi-platform**: Windows and Linux support
- [ ] **Mobile App**: React Native companion app

### **Performance Improvements**
- [ ] **Database Integration**: PostgreSQL for better data management
- [ ] **Caching**: Redis for improved performance
- [ ] **API Optimization**: GraphQL for efficient data fetching
- [ ] **Bundle Optimization**: Code splitting and lazy loading

### **Developer Experience**
- [ ] **Testing Suite**: Unit and integration tests
- [ ] **CI/CD Pipeline**: Automated testing and deployment
- [ ] **Documentation**: API documentation with Swagger
- [ ] **Monitoring**: Application performance monitoring

---

**Built with ❤️ using React, TypeScript, Flask, and WebSockets**

*Track your productivity, understand your patterns, and optimize your digital life.* 