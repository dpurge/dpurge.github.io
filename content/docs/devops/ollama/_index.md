---
title: Ollama
bookCollapseSection: true
---

## VS Code setup

```sh
ollama pull llama3.1
ollama pull deepseek-coder
ollama pull nomic-embed-text
```

```json
{
  "models": [
    {
      "title": "Llama 3.1",
      "provider": "ollama",
      "model": "llama3.1:latest"
    }
  ],
  "tabAutocompleteModel": {
    "title": "DeepSeek Coder",
    "provider": "ollama",
    "model": "deepseek-coder:latest"
  },
  "embeddingsProvider": {
    "provider": "ollama",
    "model": "nomic-embed-text"
  }
}
```
