# Claude Automation - AI-Powered Project Generator

An automated system that generates new mini-hard coding projects daily using AI APIs (Claude and OpenAI) and commits them to GitHub automatically.

## 🚀 Features

- **Automated Project Generation**: Creates new projects daily and every 5 hours
- **Multi-AI Support**: Works with both Anthropic Claude and OpenAI GPT models
- **Diverse Fields**: Rotates through 14+ programming domains
- **GitHub Integration**: Automatic commits with conventional commit messages
- **Quality Assured**: Each project includes 200-600 LOC with tests and documentation

## 🏗️ Architecture

### Core Components
- **Project Generator**: Python script that calls AI APIs and generates complete projects
- **GitHub Actions**: Automated workflow for scheduling and execution
- **Multi-Provider Support**: Flexible AI provider configuration

### Generated Project Fields
- Backend API
- Frontend web/app  
- Systems programming
- Data engineering
- ML/AI
- Distributed systems
- DevOps/infrastructure
- Databases
- Networking
- Security
- Compilers/interpreters
- Robotics/IoT
- Game development
- Scripting/automation

## 📦 Setup

### 1. Clone and Install
```bash
git clone <repository-url>
cd claude-automation
pip install -r requirements.txt
```

### 2. Environment Configuration
Create `.env` file:
```bash
PROVIDER=openai  # or "anthropic"
ANTHROPIC_API_KEY=your_claude_key_here
OPENAI_API_KEY=your_openai_key_here
MODEL_NAME=gpt-4  # optional
```

### 3. GitHub Repository Setup
Configure these secrets in your GitHub repository:
- `ANTHROPIC_API_KEY`: Your Claude API key
- `OPENAI_API_KEY`: Your OpenAI API key

Optional repository variables:
- `PROVIDER`: "anthropic" or "openai" (default: openai)
- `MODEL_NAME`: Specific model to use

## 🎯 Usage

### Manual Execution
```bash
# Generate a new project locally
python scripts/generate_next.py
```

### Automated Execution
The GitHub Actions workflow runs automatically:
- **Daily**: 09:00 UTC every day
- **Frequent**: Every 5 hours
- **Manual**: Via GitHub Actions UI

## 📁 Project Structure

```
claude-automation/
├── .env                           # Environment variables
├── .github/workflows/auto.yml     # GitHub Actions workflow
├── scripts/generate_next.py       # Main generator script
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── plan.md                        # Detailed project plan
├── task.md                        # Task management
└── YYYY-MM-DD-<field>/           # Generated projects (created automatically)
    ├── README.md
    ├── src/
    ├── tests/
    └── ...
```

## 🔧 Configuration

### API Providers
- **OpenAI**: Uses GPT models (default: gpt-4)
- **Anthropic**: Uses Claude models (default: claude-3-sonnet-20240229)

### Environment Variables
- `PROVIDER`: "openai" or "anthropic"
- `ANTHROPIC_API_KEY`: Required for Claude API
- `OPENAI_API_KEY`: Required for OpenAI API  
- `MODEL_NAME`: Override default model selection

## 📊 Quality Standards

Each generated project includes:
- ✅ 200-600 lines of non-trivial code
- ✅ Comprehensive README with setup instructions
- ✅ Working test suite
- ✅ Build/deployment configuration
- ✅ Minimal external dependencies
- ✅ Sample data or fixtures (when applicable)

## 🔄 Automation Schedule

| Trigger | Schedule | Description |
|---------|----------|-------------|
| Daily | 09:00 UTC | Main daily generation |
| Frequent | Every 5 hours | Additional projects |
| Manual | On-demand | Via GitHub Actions UI |

## 🛠️ Development

### Local Testing
```bash
# Test the generator
python scripts/generate_next.py

# Install development dependencies
pip install -r requirements.txt
```

### Monitoring
- GitHub Actions workflow logs
- Generated project quality
- API usage and rate limits
- Commit history and patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📜 License

This project is open source and available under the MIT License.

## 🔗 Links

- [Claude API Documentation](https://docs.anthropic.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)