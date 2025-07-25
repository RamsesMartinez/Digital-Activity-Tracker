# 🤝 Contributing to Digital Activity Tracker

Thank you for your interest in contributing to Digital Activity Tracker! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Feature Requests](#feature-requests)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Standards

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include details about your configuration and environment**

### 💡 Suggesting Enhancements

If you have a suggestion for a new feature or enhancement:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain which behavior you expected to see instead**

### 🔧 Pull Requests

- Fork the repo and create your branch from `main`
- If you've added code that should be tested, add tests
- If you've changed APIs, update the documentation
- Ensure the test suite passes
- Make sure your code follows the style guidelines
- Issue that pull request!

## 🛠️ Development Setup

### Prerequisites

- **macOS 10.15+** (for AppleScript functionality)
- **Python 3.8+**
- **Git**
- **Make** (usually pre-installed on macOS)

### Local Development

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/tasks-manager.git
   cd tasks-manager
   ```

2. **Set up the development environment**
   ```bash
   make install
   ```

3. **Run the application**
   ```bash
   make run-app
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000`

### Project Structure

```
tasks-manager/
├── app.py              # Main Flask application
├── reporter.py         # Activity analysis script
├── config.json         # Application configuration
├── requirements.txt    # Python dependencies
├── Makefile           # Build automation
├── README.md          # Project documentation
├── CONTRIBUTING.md    # This file
├── LICENSE            # MIT License
├── .gitignore         # Git ignore rules
├── templates/
│   └── index.html     # Dashboard template
├── activity_log.csv   # Activity data (generated)
└── venv/              # Virtual environment (generated)
```

## 📝 Code Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use type hints for function parameters and return values
- Add docstrings to all functions and classes
- Keep functions small and focused (max 20-30 lines)
- Use meaningful variable and function names
- Limit line length to 79 characters

### Example

```python
def calculate_total_time(activities: list[dict]) -> timedelta:
    """
    Calculate the total time spent across all activities.
    
    Args:
        activities: List of activity dictionaries with time data
        
    Returns:
        Total time as timedelta object
    """
    total_seconds = sum(
        activity.get('duration', 0) for activity in activities
    )
    return timedelta(seconds=total_seconds)
```

### HTML/CSS/JavaScript

- Use semantic HTML elements
- Follow BEM methodology for CSS classes
- Use meaningful class and ID names
- Keep JavaScript functions small and focused
- Add comments for complex logic

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

**Good examples:**
```
Add real-time activity tracking feature
Fix dashboard not updating on pause/resume
Update README with installation instructions
```

## 🧪 Testing

### Running Tests

```bash
make test
```

### Writing Tests

- Create test files in a `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies
- Aim for good test coverage

### Example Test

```python
import pytest
from app import format_time_display
from datetime import timedelta

def test_format_time_display():
    """Test time formatting function."""
    # Test zero time
    assert format_time_display(timedelta(0)) == "00:00:00"
    
    # Test regular time
    assert format_time_display(timedelta(hours=2, minutes=30, seconds=45)) == "02:30:45"
    
    # Test edge cases
    assert format_time_display(timedelta(seconds=3661)) == "01:01:01"
```

## 📤 Submitting Changes

### Before Submitting

1. **Ensure your code follows the style guidelines**
2. **Add tests for new functionality**
3. **Update documentation if needed**
4. **Test your changes thoroughly**

### Pull Request Process

1. **Update the README.md with details of changes** if applicable
2. **Update the CHANGELOG.md** with a note describing your change
3. **The PR will be merged once you have the sign-off** of at least one maintainer

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

## 🐛 Reporting Bugs

### Before Creating Bug Reports

- Check the [issue list](https://github.com/ramthedev/tasks-manager/issues) for existing reports
- Check the [documentation](README.md) for solutions
- Try to reproduce the issue in a clean environment

### Bug Report Template

```markdown
## Bug Description
A clear and concise description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
A clear and concise description of what you expected to happen.

## Actual Behavior
A clear and concise description of what actually happened.

## Environment
- OS: [e.g. macOS 12.0]
- Python Version: [e.g. 3.9.0]
- Browser: [e.g. Chrome 96.0.4664.110]
- Application Version: [e.g. 1.0.0]

## Additional Context
Add any other context about the problem here.
```

## 💡 Feature Requests

### Feature Request Template

```markdown
## Feature Description
A clear and concise description of the feature you'd like to see.

## Problem Statement
A clear and concise description of what problem this feature would solve.

## Proposed Solution
A clear and concise description of what you want to happen.

## Alternative Solutions
A clear and concise description of any alternative solutions or features you've considered.

## Additional Context
Add any other context or screenshots about the feature request here.
```

## 📞 Getting Help

If you need help with contributing:

- **Issues**: [GitHub Issues](https://github.com/ramthedev/tasks-manager/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ramthedev/tasks-manager/discussions)
- **Documentation**: [README.md](README.md)

## 🙏 Recognition

Contributors will be recognized in:

- The project's README.md file
- Release notes
- The project's contributors page

Thank you for contributing to Digital Activity Tracker! 🎉 