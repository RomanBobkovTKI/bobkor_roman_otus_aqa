#!/bin/sh

echo "🚀 Запуск тестов..."
echo "📝 Аргументы: $@"

WORKERS=${1:-4}
shift
pytest -n "$WORKERS" "$@"