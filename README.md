# Flowscribe

**Flowscribe** is a work‑in‑progress AI‑assisted code editor that provides **inline AI suggestions** as you type. The goal is to seamlessly blend AI-driven assistance into your existing editing flow — offering completions, hints, or small code snippets, contextually and in real time.

> ⚠️ *Note: This project is experimental and under active development. Many features are incomplete or subject to change.*

---

## Table of Contents

- [Features](#features)  
- [Architecture](#architecture)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation & Running](#installation--running)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Contribution](#contribution)  
- [Roadmap](#roadmap)  
- [License](#license)

---

## Features

While still evolving, the intended capabilities include:

- Real‑time inline AI suggestions/hints as you type  
- Context-aware completions (based on cursor position & surrounding code)  
- Support for multiple languages  
- Lightweight architecture to integrate with existing editors or as a standalone tool  
- Plugin or API interfaces to swap the underlying model

---

## Architecture

Flowscribe is structured in two main parts:

- **frontend**: UI / editor interface (TypeScript, HTML, CSS)  
- **backend**: API server and integration with AI models (Python)  

They communicate over a local HTTP or WebSocket interface. A `docker-compose.yml` is provided to orchestrate both services easily.

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- Docker & Docker Compose installed  
- Python 3.8+ (if running backend standalone)  
- Node.js / npm (for frontend)  

### Installation & Running

You can run the entire system via Docker Compose:

```sh
docker-compose up --build
