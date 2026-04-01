#!/bin/sh

echo "🚀 Запуск тестов..."
echo "📝 Аргументы: $@"
pytest -n ${1:-4}