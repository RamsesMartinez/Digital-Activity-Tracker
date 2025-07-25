.PHONY: install run run-app run-reporter clean help test lint format frontend frontend-dev frontend-build

# Variables
VENV_NAME = venv
PYTHON = python3
PIP = pip3
APP_NAME = Digital Activity Tracker

# Colors for output
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
RED = \033[0;31m
NC = \033[0m # No Color

# Install dependencies in virtual environment
install:
	@echo "$(BLUE)🔧 Creating virtual environment...$(NC)"
	$(PYTHON) -m venv $(VENV_NAME)
	@echo "$(BLUE)📦 Installing dependencies...$(NC)"
	. $(VENV_NAME)/bin/activate && $(PIP) install --upgrade pip
	. $(VENV_NAME)/bin/activate && $(PIP) install -r requirements.txt
	@echo "$(GREEN)✅ Installation completed!$(NC)"
	@echo "$(BLUE)🔌 WebSocket support enabled for real-time updates$(NC)"

# Run the Flask application with WebSocket support
run-app:
	@echo "$(BLUE)🚀 Starting $(APP_NAME) with real-time WebSocket support...$(NC)"
	@echo "$(YELLOW)⚡ Real-time updates enabled - no HTTP polling required!$(NC)"
	. $(VENV_NAME)/bin/activate && $(PYTHON) app.py

# Run the reporter script
run-reporter:
	@echo "$(BLUE)📊 Generating activity report...$(NC)"
	. $(VENV_NAME)/bin/activate && $(PYTHON) reporter.py

# Alias for run-app
run: run-app

# Install and run in one command
setup-and-run: install run-app

# Frontend commands
frontend:
	@echo "$(BLUE)🎨 Frontend options:$(NC)"
	@echo "$(GREEN)make frontend-dev$(NC)    - Start React development server"
	@echo "$(GREEN)make frontend-build$(NC)  - Build React for production"

frontend-dev:
	@echo "$(BLUE)🎨 Starting React development server...$(NC)"
	@echo "$(YELLOW)🌐 Frontend will be available at: http://localhost:5173$(NC)"
	cd frontend && npm run dev

frontend-build:
	@echo "$(BLUE)🏗️ Building React for production...$(NC)"
	cd frontend && npm run build
	@echo "$(GREEN)✅ Frontend built successfully!$(NC)"

# Install frontend dependencies
frontend-install:
	@echo "$(BLUE)📦 Installing frontend dependencies...$(NC)"
	cd frontend && npm install --legacy-peer-deps
	@echo "$(GREEN)✅ Frontend dependencies installed!$(NC)"

# Clean virtual environment
clean:
	@echo "$(YELLOW)🧹 Cleaning virtual environment...$(NC)"
	rm -rf $(VENV_NAME)
	@echo "$(GREEN)✅ Virtual environment removed!$(NC)"

# Clean frontend
frontend-clean:
	@echo "$(YELLOW)🧹 Cleaning frontend build...$(NC)"
	cd frontend && rm -rf dist node_modules
	@echo "$(GREEN)✅ Frontend cleaned!$(NC)"

# Run tests (placeholder for future test implementation)
test:
	@echo "$(BLUE)🧪 Running tests...$(NC)"
	. $(VENV_NAME)/bin/activate && echo "Tests not implemented yet"

# Lint code (placeholder for future linting implementation)
lint:
	@echo "$(BLUE)🔍 Linting code...$(NC)"
	. $(VENV_NAME)/bin/activate && echo "Linting not implemented yet"

# Format code (placeholder for future formatting implementation)
format:
	@echo "$(BLUE)🎨 Formatting code...$(NC)"
	. $(VENV_NAME)/bin/activate && echo "Formatting not implemented yet"

# Show help
help:
	@echo "$(BLUE)📖 $(APP_NAME) - Available Commands$(NC)"
	@echo "$(BLUE)=====================================$(NC)"
	@echo "$(GREEN)Backend Commands:$(NC)"
	@echo "$(GREEN)make install$(NC)        - Install dependencies in virtual environment"
	@echo "$(GREEN)make run-app$(NC)        - Start the Flask application with WebSocket support"
	@echo "$(GREEN)make run$(NC)            - Alias for run-app"
	@echo "$(GREEN)make run-reporter$(NC)   - Generate activity report"
	@echo "$(GREEN)make setup-and-run$(NC)  - Install dependencies and start app"
	@echo "$(GREEN)make clean$(NC)          - Remove virtual environment"
	@echo ""
	@echo "$(GREEN)Frontend Commands:$(NC)"
	@echo "$(GREEN)make frontend-install$(NC) - Install frontend dependencies"
	@echo "$(GREEN)make frontend-dev$(NC)     - Start React development server"
	@echo "$(GREEN)make frontend-build$(NC)   - Build React for production"
	@echo "$(GREEN)make frontend-clean$(NC)   - Clean frontend build"
	@echo ""
	@echo "$(GREEN)Development Commands:$(NC)"
	@echo "$(GREEN)make test$(NC)           - Run tests (not implemented)"
	@echo "$(GREEN)make lint$(NC)           - Lint code (not implemented)"
	@echo "$(GREEN)make format$(NC)         - Format code (not implemented)"
	@echo "$(GREEN)make help$(NC)           - Show this help message"
	@echo ""
	@echo "$(YELLOW)💡 Quick Start:$(NC)"
	@echo "   Backend:  make setup-and-run"
	@echo "   Frontend: make frontend-install && make frontend-dev"
	@echo ""
	@echo "$(YELLOW)🌐 URLs:$(NC)"
	@echo "   Backend:  http://127.0.0.1:5000"
	@echo "   Frontend: http://localhost:5173"
	@echo ""
	@echo "$(BLUE)⚡ Real-time Features:$(NC)"
	@echo "   • WebSocket connection for instant updates"
	@echo "   • No HTTP polling required"
	@echo "   • Live activity tracking"
	@echo "   • Connection status indicator"
	@echo "   • React + TypeScript frontend"
	@echo "   • Tailwind CSS + Framer Motion" 