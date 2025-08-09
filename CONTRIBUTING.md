# Contributing to SmartCache

Thank you for your interest in contributing to SmartCache! We welcome all contributions, whether they're bug reports, feature requests, documentation improvements, or code contributions.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Message Guidelines](#commit-message-guidelines)

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Bugs are tracked as [GitHub issues](https://github.com/louisgoodnews/Cacheing/issues). When creating a bug report, please include:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Environment details (Python version, OS, etc.)
6. Any relevant logs or error messages

### Suggesting Enhancements

We welcome enhancement suggestions! Please create an issue describing:

1. The feature you'd like to see
2. Why this feature would be useful
3. Any implementation ideas you have

### Your First Code Contribution

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add tests for your changes
5. Run the test suite
6. Submit a pull request

### Pull Requests

- Keep pull requests focused on a single feature or bugfix
- Include tests for new functionality
- Update documentation as needed
- Follow the coding standards below
- Reference any related issues

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for all new code
- Write docstrings following [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Keep functions small and focused
- Write meaningful commit messages

## Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/). Format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or modifying tests
- `chore`: Changes to the build process or auxiliary tools

Example:
```
feat(cache): add LRU eviction policy

Adds support for LRU (Least Recently Used) cache eviction policy.

Closes #123
```

Thank you for contributing to SmartCache!