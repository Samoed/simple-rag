# Simple RAG

Простая RAG-система, рассмотренная на лекции "Уязвимости RAG".
Для инференса *не требуется* GPU, можно запустить ПО на любом компьютере с достаточным (~8 Гб) объёмом RAM.

## Архитектура

![Application Layout](./docs/app.png)

Содержит следующие компоненты:

- Само приложение (`main.py`)
- Индексатор - (`rag/modules/index.py`)
- Маршрутизатор (`rag/modules/route.py`)
- Поиск по базе знаний (`rag/modules/search.py`)
- Инструмент поиска в интернете (`rag/modules/internet.py`)

Внешние компоненты:
- Векторное хранилище - Weaviate Embedded
- LLM - Mistral 7B OpenOrca GGUF, рекомендуется взять [4-битную квантизацию](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.Q4_K_M.gguf)
- Embedding - [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)

## Зависимости

- Python 3.11+
- Poetry
- Brave Search API (можно использовать мой ключ, который я выдам в задании, или зарегистрировать свой)

## Установка

    poetry install --no-root

## Настройка

Настройка производится через переменные окружения, их можно задать в локальном файле `.env`. Переменные читаются автоматически при запуске программы:



## Запуск

