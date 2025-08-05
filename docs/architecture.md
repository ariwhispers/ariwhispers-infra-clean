## High-level architecture
```mermaid
flowchart LR
    A[FastAPI] --> B(Celery)
    B --> C[LLM Pod]
    B --> D[ComfyUI Pod]
    B --> E[ElevenLabs Pod]
    C --> A
    D --> A
    E --> A
```
