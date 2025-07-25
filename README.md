# 📊 Digital Activity Tracker

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![macOS](https://img.shields.io/badge/macOS-10.15+-silver.svg)](https://www.apple.com/macos/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/ramthedev/tasks-manager)

> A real-time digital activity tracking application that monitors your computer usage and provides insights into your productivity patterns. Built with Flask and designed for macOS.

## 🌟 Features

- **🔍 Real-time Tracking**: Monitors active applications and browser URLs every 2 seconds
- **📱 Beautiful Dashboard**: Modern, responsive web interface with live updates
- **🎯 Smart Categorization**: Automatically categorizes activities (Development, Productivity, Entertainment, etc.)
- **📊 Detailed Analytics**: Visual charts and statistics showing time distribution
- **⏸️ Pause/Resume**: Control tracking with a single click
- **📈 Activity Reports**: Generate detailed reports of your digital habits
- **🔒 Privacy-First**: All data stored locally on your machine
- **🚀 Easy Setup**: Simple installation with Makefile automation

## 🖼️ Screenshots

![Dashboard Preview](https://via.placeholder.com/800x400/667eea/ffffff?text=Dashboard+Preview)

*Real-time activity dashboard showing categorized time tracking*

## 🚀 Quick Start

### Prerequisites

- **macOS 10.15+** (uses AppleScript for system integration)
- **Python 3.8+**
- **Make** (usually pre-installed on macOS)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ramthedev/tasks-manager.git
   cd tasks-manager
   ```

2. **Install and run with one command**
   ```bash
   make setup-and-run
   ```

3. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

### Alternative Installation

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 📖 Usage

### Starting the Tracker

```bash
# Start the Flask application (includes tracking)
make run-app

# Or use the alias
make run
```

### Generating Reports

```bash
# Generate activity report
make run-reporter
```

### Available Commands

| Command | Description |
|---------|-------------|
| `make install` | Install dependencies in virtual environment |
| `make run-app` | Start the Flask application with tracking |
| `make run` | Alias for `run-app` |
| `make run-reporter` | Generate activity report |
| `make setup-and-run` | Install dependencies and start app |
| `make clean` | Remove virtual environment |
| `make help` | Show all available commands |

## 🏗️ Architecture

### Core Components

- **`app.py`**: Main Flask application with real-time tracking
- **`reporter.py`**: Activity analysis and report generation
- **`config.json`**: Application and URL categorization rules
- **`templates/index.html`**: Modern dashboard interface

### Data Flow

```
System Activity → AppleScript → Flask App → CSV Log → Dashboard
                                    ↓
                              Reporter → Activity Report
```

### Supported Applications

The tracker automatically categorizes:

- **Development**: VS Code, Cursor, PyCharm, IntelliJ, Xcode, Terminal
- **Productivity**: Notion, Obsidian, Trello, Asana, Calendar
- **Communication**: Slack, Teams, Discord, WhatsApp, Zoom
- **Entertainment**: Spotify, Netflix, YouTube, Games
- **Browsing**: Chrome, Safari, Firefox, Brave, Arc
- **And many more...**

## ⚙️ Configuration

### Customizing Categories

Edit `config.json` to add your own applications and URL patterns:

```json
{
  "app_mappings": {
    "Your App": "Your Category",
    "Another App": "Another Category"
  },
  "browser_keywords": {
    "example.com": "Work",
    "social.com": "Social Media"
  }
}
```

### Tracking Interval

Modify `CHECK_INTERVAL` in `app.py` to change tracking frequency:

```python
CHECK_INTERVAL = 2  # Seconds between tracking samples
```

## 📊 Dashboard Features

### Real-time Statistics

- **Active Categories**: Number of different activity types
- **Total Time**: Cumulative tracking time
- **Top Category**: Most used activity type

### Visual Elements

- **Progress Bars**: Visual representation of time distribution
- **Color-coded Categories**: Easy identification of activity types
- **Live Updates**: Data refreshes every 2 seconds
- **Responsive Design**: Works on desktop and mobile

### Controls

- **Pause/Resume**: Stop or restart tracking
- **Shutdown**: Gracefully stop the application

## 🔧 Development

### Project Structure

```
tasks-manager/
├── app.py              # Main Flask application
├── reporter.py         # Activity analysis script
├── config.json         # Application configuration
├── requirements.txt    # Python dependencies
├── Makefile           # Build automation
├── README.md          # Project documentation
├── templates/
│   └── index.html     # Dashboard template
├── activity_log.csv   # Activity data (generated)
└── venv/              # Virtual environment (generated)
```

### Adding New Features

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add docstrings to functions
- Keep functions small and focused

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** by opening an issue
- 💡 **Suggest features** in the discussions
- 📝 **Improve documentation**
- 🔧 **Fix bugs** or add features
- 🎨 **Enhance the UI/UX**

### Development Setup

```bash
# Clone and setup
git clone https://github.com/ramthedev/tasks-manager.git
cd tasks-manager
make install

# Run in development mode
make run-app
```

### Testing

```bash
# Run the application
make run-app

# In another terminal, generate a report
make run-reporter
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flask** - Web framework
- **AppleScript** - macOS system integration
- **HTML5/CSS3** - Modern dashboard design
- **JavaScript** - Real-time updates

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/ramthedev/tasks-manager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ramthedev/tasks-manager/discussions)
- **Email**: [Your Email]

## 🗺️ Roadmap

- [ ] **Cross-platform support** (Windows, Linux)
- [ ] **Export functionality** (PDF, Excel reports)
- [ ] **Goal setting** and productivity targets
- [ ] **API endpoints** for external integrations
- [ ] **Mobile app** companion
- [ ] **Team tracking** for collaborative insights
- [ ] **Machine learning** for better categorization

---

<div align="center">

**Made with ❤️ by [Ramthedev](https://github.com/ramthedev)**

[⭐ Star this repo](https://github.com/ramthedev/tasks-manager) | [🐛 Report an issue](https://github.com/ramthedev/tasks-manager/issues) | [📖 View docs](https://github.com/ramthedev/tasks-manager#readme)

</div> 