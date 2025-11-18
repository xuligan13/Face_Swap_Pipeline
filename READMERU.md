# 🎭 Face Swap Pipeline  
**Fully automated pipeline for face-to-scene identity transfer**  
Gemini → Seedream → final cinematic output

---

## 🚀 Overview

Face Swap Pipeline — это полностью автоматизированная система, которая берёт:

- **2 изображения лица** (основные референсы личности)  
- **1 или N сценовых изображений**  
- **промпт для Gemini**, который пользователь может редактировать  

и генерирует готовые изображения, сохраняя индивидуальность человека, используя последовательный запуск:

**(Face1, Face2, Scene) → Gemini → Seedream → PNG результат**

---

## ✨ Features

✔ Используются строго **2 лица** → во всех сценах будет одна и та же личность  
✔ Много сцен → пачечная генерация  
✔ Gemini формирует **Seedream-prompt** автоматически  
✔ Поддержка **mock-режима**  
✔ Полная модульность: clients, utils, main  
✔ Полноценная CLI-навигация  
✔ Результаты сохраняются в формате **PNG + TXT**

---

## 📂 Project Structure

Face_Swap_Pipeline/
│
├── FACE/ # put EXACTLY 2 face images here
├── SCENE/ # put all scene images here
├── OUTPUT/ # generated results
│
├── examples/ # for README demonstration images
│ ├── Face1.jpeg
│ ├── Face2.png
│ ├── Scene.jpg
│ └── output.jpeg
│
├── gemini_user_prompt.txt
├── config_example.json
├── requirements.txt
├── main.py
├── utils.py
├── gemini_client.py
├── seedream_client.py
└── .env

yaml
Skopiuj kod

---

# 📸 **Before / After Example**

> Убедись, что положил свои изображения в папку `examples/`  
> Пути будут работать **только внутри GitHub**, если структура совпадает.

| Face 1 | Face 2 |
|--------|--------|
| ![](examples/Face1.jpeg) | ![](examples/Face2.png) |

| Scene | Output |
|--------|--------|
| ![](examples/Scene.jpg) | ![](examples/output.jpeg) |

---

## 🔧 Installation

```bash
git clone https://github.com/<your-username>/Face_Swap_Pipeline
cd Face_Swap_Pipeline
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt
⚙️ Configuration
1. Add your API keys
Создай файл .env:

ini
Skopiuj kod
GEMINI_API_KEY=your_key_here
SEEDREAM_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
2. Add face & scene images
В папку FACE/ — ровно 2 файла

В папку SCENE/ — сколько хочешь сценовых изображений

3. Edit prompt
Файл:

Skopiuj kod
gemini_user_prompt.txt
Полностью управляет поведением Gemini.

▶️ Run the Pipeline
bash
Skopiuj kod
python main.py
Скрипт:

Находит 2 лица

Находит все сцены

Показывает резюме

Ждёт нажатия Enter

Запускает Gemini → Seedream

Сохраняет результаты:

arduino
Skopiuj kod
OUTPUT/0001_name.png
OUTPUT/0001_name.txt
🧪 Testing before GitHub upload
Test the folder logic

Положи 2 лица → запускай → ошибок быть не должно

Положи 1 или 3 лица → должен показать ошибку

Test mock Gemini

Установи в config:

json
Skopiuj kod
"gemini": { "mode": "mock" }
Убедись, что pipeline работает без API

Test real API

Запуск на 1 сцене

Проверить ответ Gemini

Проверить рендер Seedream

Test invalid files

Добавь в SCENE пустой файл, txt или битое изображение

Программа должна корректно игнорировать

🔍 Potential Improvements (TODO)
Добавить WebUI (Gradio/FastAPI)

Добавить мультипоточность для ускорения

Сделать логирование в файл

Автоматическая оптимизация изображений (resize 1024x1024)

GitHub Actions (линтинг + тесты)

🤝 Contributing
PRы приветствуются!
Не загружайте .env и приватные фото других людей.
