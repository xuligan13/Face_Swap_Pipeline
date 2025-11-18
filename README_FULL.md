
# 🎭 Face Swap Pipeline — AI-Powered Multi-Scene Face Swapping  
*(Русская версия ниже — Russian version below)*

---

<div align="center">
  <img src="examples/logo.png" alt="Logo" width="160"/>
</div>

<p align="center">
  <b>🔥 A fully automated pipeline for multi‑scene AI face swapping using Gemini & Seedream</b>  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Stable-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-purple?style=flat-square"/>
</p>

---

# 📌 Overview (EN)

Face Swap Pipeline automatically processes two identity images and multiple scene photos, generating high‑quality AI face‑swapped images through **Google Gemini → Seedream v4**.

✔ Uses exactly **2 face reference images**  
✔ Swaps the identity into **unlimited number of scenes**  
✔ High‑quality final render via **Seedream 4.0**  
✔ Includes interactive CLI, mock mode, clean API design  
✔ Perfect for AI content creators, dataset generation, and visual storytelling  

---

# 🖼️ Before / After

<div align="center">

| Face 1 | Face 2 | Scene | Result |
|-------|--------|--------|--------|
| <img src="examples/Face1.jpeg" width="220"/> | <img src="examples/Face2.png" width="220"/> | <img src="examples/Scene.jpg" width="260"/> | <img src="examples/output.jpeg" width="260"/> |

</div>

---

# 🚀 Installation

```bash
git clone https://github.com/xuligan13/Face_Swap_Pipeline
cd Face_Swap_Pipeline
```

### Create virtual environment  
**Mac/Linux**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

---

# 🔧 Configuration

### 1️⃣ Add API keys  
Create file `.env`:

```
GEMINI_API_KEY=your_key_here
SEEDREAM_API_KEY=your_key_here
```

### 2️⃣ Add your images  

**FACE/** → exactly 2 face images  
**SCENE/** → 20–25 scene photos recommended  

### 3️⃣ Optional — edit Gemini prompt  
File:

```
gemini_user_prompt.txt
```

Controls Gemini → Seedream prompt generation.

---

# ▶️ Run the Pipeline

```bash
python main.py
```

What happens:

1. Detects 2 faces  
2. Detects all scenes  
3. Shows summary  
4. Waits for **Enter**  
5. Sends: (face1, face2, scene, user_prompt) → **Gemini**  
6. Sends: (face1, face2, scene, gemini_prompt) → **Seedream**  
7. Saves output:

```
OUTPUT/0001_scene.png
OUTPUT/0001_scene.txt
```

---

# 🧪 Testing

### Test without Gemini (mock mode)

In `config_example.json` set:

```
"gemini": { "mode": "mock" }
```

Check:

✔ 2 faces → OK  
✔ 1 or 3 faces → error  
✔ non-image in SCENE → ignored  

### Test real API

- Run on 1 scene  
- Check Gemini response  
- Check Seedream image  
- Verify output saved  

---

# 🚀 Future Improvements (TODO)

- WebUI (Gradio / FastAPI)  
- Multi-threaded rendering  
- Logging to file  
- Image auto-resize  
- GitHub Actions (lint + tests)

---

# 🤝 Contributing

PRs are welcome!  
Please DO NOT upload `.env` or private photos of real people.

---

# 🌍 **Русская версия**

# 📌 Обзор

Face Swap Pipeline — это полностью автоматизированный инструмент для замены лица:  
2 референсных лица → множество сцен → результат через Gemini и Seedream v4.

✔ Использует ровно 2 лица  
✔ Поддерживает неограниченное количество сцен  
✔ Финальный рендер — Seedream 4.0  
✔ Есть интерактивный CLI и mock‑режим  

---

# 🖼️ До / После

<div align="center">

| Лицо 1 | Лицо 2 | Сцена | Результат |
|-------|--------|--------|-----------|
| <img src="examples/Face1.jpeg" width="220"/> | <img src="examples/Face2.png" width="220"/> | <img src="examples/Scene.jpg" width="260"/> | <img src="examples/output.jpeg" width="260"/> |

</div>

---

# 🚀 Установка

```bash
git clone https://github.com/xuligan13/Face_Swap_Pipeline
cd Face_Swap_Pipeline
```

## Создание окружения  
### macOS / Linux
```bash
python -m venv venv
source venv/bin/activate
```

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

## Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# ⚙️ Настройка

## 1. API-ключи  

Создай `.env`:

```
GEMINI_API_KEY=ваш_ключ
SEEDREAM_API_KEY=ваш_ключ
```

## 2. Изображения  

Папка **FACE/** → ровно 2 лица  
Папка **SCENE/** → ваши сцены  

## 3. Промпт Gemini  

Файл:

```
gemini_user_prompt.txt
```

---

# ▶️ Запуск

```bash
python main.py
```

---

# 🧪 Тестирование

### Mock Gemini

```
"gemini": { "mode": "mock" }
```

---

# 🤝 Вклад

PR-ы приветствуются!  

---

# 🔗 Seedream Model  
https://wavespeed.ai/models/bytedance/seedream-v4/edit
