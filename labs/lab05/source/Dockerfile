# Базовый образ для этапа сборки зависимостей (builder)
FROM python:3.11-slim AS builder

# Рабочая директория внутри контейнера
WORKDIR /hello

# Копируем только файл зависимостей (чтобы кэшировать слой установки)
COPY requirements.txt .

# Обновляем pip и собираем все колёсики (wheels) в отдельную папку
# Это ускоряет финальную сборку и уменьшает размер итогового образа
RUN pip install --upgrade pip && \
    pip wheel --wheel-dir=/wheels -r requirements.txt

# Финальный лёгкий образ (без кэша сборки и лишних инструментов)
FROM python:3.11-slim

# Та же рабочая директория
WORKDIR /hello

# Переносим только готовые колёсики из этапа builder
COPY --from=builder /wheels /wheels

# Копируем requirements.txt ещё раз (нужен для pip install)
COPY requirements.txt .

# Устанавливаем пакеты только из локальных колёсиков → быстрее и без интернета
RUN pip install --no-index --find-links=/wheels -r requirements.txt

# Копируем основной код приложения
COPY new_hello.py .

# Отключаем буферизацию вывода — логи будут сразу видны в docker logs
ENV PYTHONUNBUFFERED=1

# Команда, которая запускается при старте контейнера
CMD ["python", "new_hello.py"]