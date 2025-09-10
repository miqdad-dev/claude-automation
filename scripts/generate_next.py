#!/usr/bin/env python3
"""
Generate Next Project Script
Automatically generates new dated coding projects using AI APIs.
"""

import os
import sys
import random
import re
from datetime import datetime, timezone
from pathlib import Path
import subprocess
from typing import Dict, Any, List, Optional

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

PROGRAMMING_FIELDS = [
    "backend api", "frontend web/app", "systems programming", "data engineering", 
    "ml/ai", "distributed systems", "devops/infrastructure", "databases", 
    "networking", "security", "compilers/interpreters", "robotics/iot", 
    "game dev", "scripting/automation"
]

PROJECT_PROMPT = """Create a COMPLETE, RUNNABLE "mini-hard" project with non-trivial logic.

GOAL
- Build a new mini-hard project (not trivial "hello world") from the field: {field}
- Root folder name MUST be: {folder_name}
- Provide ALL files strictly as fenced blocks in this exact format (no language tag, no extra commentary outside blocks):

```path/filename
<file content here>
```

REQUIRED CONTENTS
1. Source code implementing a mini-hard project (≥1 substantial module).
2. README.md with:
   * what it does
   * how it works
   * how to run (exact commands)
   * example usage
   * notes on architecture & tradeoffs
3. Tests (unit or integration).
4. If applicable: Dockerfile or Compose; otherwise Makefile or a task runner.
5. A small sample dataset or fixtures if helpful.
6. Lint/format config if applicable.

QUALITY BAR
* Non-trivial logic (e.g., algorithms, concurrency, state machines, streaming, indexing, parsers, protocol, etc.).
* Keep external deps minimal. Ensure README run steps work from a clean clone.
* Total LOC target: 200–600.
* Ensure tests pass locally.
* If web, include index.html + script.js (+ optional css) and a tiny local server if needed.

DELIVERABLES
* Output ONLY fenced filename blocks for every file (source, README, tests, etc.).
* Do NOT include explanation outside the blocks.
"""


class ProjectGenerator:
    def __init__(self):
        self.provider = os.getenv("PROVIDER", "openai").lower()
        self.anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.model_name = os.getenv("MODEL_NAME", "")
        
        if not self.model_name:
            if self.provider == "anthropic":
                self.model_name = "claude-3-sonnet-20240229"
            else:
                self.model_name = "gpt-4"
        
        print(f"Using provider: {self.provider} with model: {self.model_name}")

    def generate_folder_name(self, field: str) -> str:
        """Generate folder name based on project field and content."""
        # Clean field name for folder
        base_name = field.replace(" ", "-").replace("/", "-")
        return base_name
    
    def extract_project_name_from_content(self, content: str) -> Optional[str]:
        """Extract project name from README content."""
        lines = content.split('\n')
        for line in lines:
            # Look for markdown headers that might contain project names
            if line.startswith('# '):
                project_name = line[2:].strip()
                # Clean up the name for folder use
                clean_name = re.sub(r'[^\w\s-]', '', project_name)
                clean_name = re.sub(r'\s+', '-', clean_name.strip()).lower()
                if len(clean_name) > 3 and len(clean_name) < 50:
                    return clean_name
        return None

    def call_anthropic_api(self, prompt: str) -> str:
        """Call Anthropic Claude API."""
        if not self.anthropic_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.anthropic_key,
            "anthropic-version": "2023-06-01"
        }
        
        data = {
            "model": self.model_name,
            "max_tokens": 4000,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data,
            timeout=120
        )
        
        if response.status_code != 200:
            raise Exception(f"Anthropic API error: {response.status_code} - {response.text}")
        
        return response.json()["content"][0]["text"]

    def call_openai_api(self, prompt: str) -> str:
        """Call OpenAI API."""
        if not self.openai_key:
            raise ValueError("OPENAI_API_KEY not set")
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_key}"
        }
        
        data = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 4000,
            "temperature": 0.7
        }
        
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=120
        )
        
        if response.status_code != 200:
            raise Exception(f"OpenAI API error: {response.status_code} - {response.text}")
        
        return response.json()["choices"][0]["message"]["content"]

    def generate_project_content(self, field: str, folder_name: str) -> str:
        """Generate project content using the configured AI provider."""
        prompt = PROJECT_PROMPT.format(field=field, folder_name=folder_name)
        
        if self.provider == "anthropic":
            return self.call_anthropic_api(prompt)
        elif self.provider == "openai":
            return self.call_openai_api(prompt)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def parse_files_from_content(self, content: str) -> Dict[str, str]:
        """Parse fenced code blocks from AI response."""
        files = {}
        
        # Match fenced code blocks with filenames
        pattern = r'```([^\n`]+)\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for filename, file_content in matches:
            # Clean up filename
            filename = filename.strip()
            if filename and not filename.startswith('```'):
                files[filename] = file_content.strip()
        
        return files

    def write_files(self, folder_name: str, files: Dict[str, str]) -> None:
        """Write files to the project directory."""
        project_path = Path(folder_name)
        project_path.mkdir(exist_ok=True)
        
        for filepath, content in files.items():
            full_path = project_path / filepath
            full_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Created: {filepath}")

    def setup_git_and_commit(self, folder_name: str, field: str) -> None:
        """Set up git and commit the new project."""
        try:
            # Configure git user
            subprocess.run(['git', 'config', 'user.name', 'Auto Project Generator'], check=True)
            subprocess.run(['git', 'config', 'user.email', 'auto-gen@example.com'], check=True)
            
            # Add and commit files
            subprocess.run(['git', 'add', folder_name], check=True)
            commit_msg = f"feat(auto): add project {folder_name} - {field}"
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            
            # Push to remote
            subprocess.run(['git', 'push'], check=True)
            print(f"Successfully committed and pushed project: {folder_name}")
            
        except subprocess.CalledProcessError as e:
            print(f"Git operation failed: {e}")
            sys.exit(1)

    def run(self) -> None:
        """Main execution flow."""
        try:
            # Select random field and generate folder name
            field = random.choice(PROGRAMMING_FIELDS)
            folder_name = self.generate_folder_name(field)
            
            print(f"Generating project for field: {field}")
            print(f"Project folder: {folder_name}")
            
            # Generate project content
            print("Calling AI API to generate project...")
            content = self.generate_project_content(field, folder_name)
            
            # Parse files from content
            files = self.parse_files_from_content(content)
            
            if not files:
                print("Warning: No files were parsed from AI response")
                return
            
            print(f"Parsed {len(files)} files from AI response")
            
            # Try to extract a better project name from the content
            if 'README.md' in files:
                extracted_name = self.extract_project_name_from_content(files['README.md'])
                if extracted_name:
                    folder_name = extracted_name
                    print(f"Updated folder name to: {folder_name}")
            
            # Write files to disk
            self.write_files(folder_name, files)
            
            # Commit to git
            self.setup_git_and_commit(folder_name, field)
            
            print("Project generation completed successfully!")
            
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    generator = ProjectGenerator()
    generator.run()