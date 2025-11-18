# 📘 **README.md**

```markdown
# 🎬 Face Fusion Pipeline  
Batch face-transfer pipeline using **two identity images**, **scene references**, **Gemini prompt generation**, and **Seedream rendering**.

---

<div align="center">

### 🔥 Before → After Showcase

| Face 1 | Face 2 | Scene Image | Output |
|--------|--------|--------------|--------|
| <img src="autodataset_tool/examples/Face1.jpeg" width="220"/> | <img src="autodataset_tool/examples/Face2.png" width="220"/> | <img src="autodataset_tool/examples/Scene.jpg" width="220"/> | <img src="autodataset_tool/examples/output.jpeg" width="220"/> |

</div>

---

# 📂 Project Structure

```

autodataset_tool/
│
├── examples/
│     ├── Face1.jpeg            # Identity Reference 1
│     ├── Face2.png             # Identity Reference 2
│     ├── Scene.jpg             # Reference scene
│     ├── output.jpeg           # Generated result example
│
├── FACE/                       # Used in runtime — must contain exactly 2 face images
├── SCENE/                      # Contains many scene images (batch-processed)
├── OUTPUT/                     # Generated images saved here
│
├── gemini_user_prompt.txt      # User-editable prompt template
├── seedream_client.py
├── gemini_client.py
├── utils.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md

```

---

# 🚀 Overview

This application:

1. Loads **exactly two face images** from the `FACE/` directory  
2. Iterates through **all scene images** in `SCENE/`  
3. Sends the following to **Gemini**:

```

Face1, Face2, SceneX, User Prompt

```

4. Gemini generates a **Seedream-ready prompt**  
5. The app sends to **Seedream**:

```

Face1, Face2, SceneX, Gemini Prompt

````

6. Saves final images into the `OUTPUT/` folder

---

# 🧠 Prompt Flow (Gemini → Seedream)

Gemini receives:

- Reference Image 1 (identity)
- Reference Image 2 (identity)
- Reference Image 3 (scene)
- User prompt (from file)

Gemini returns a **fully structured, cinematic-quality Seedream prompt**.

Then Seedream renders the final image using **all three references**.

---

# 🛠 Installation

## 1. Clone repository

```bash
git clone <your_repo_url>
cd autodataset_tool
````

## 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create `.env`

Copy:

```bash
cp .env.example .env
```

Fill it:

```
GEMINI_API_KEY=your_key_here
SEEDREAM_API_KEY=your_key_here
GROQ_API_KEY=optional
```

---

# 📁 Prepare your data

### Put EXACTLY two images here:

```
FACE/
  Face1.jpg
  Face2.png
```

### Put ALL SCENE IMAGES here:

```
SCENE/
  scene01.jpg
  scene02.jpg
  ...
```

---

# ▶️ Run the pipeline

```bash
python main.py
```

The script will display:

* found face images
* list of scenes
* confirmation prompt

Press **Enter** to start batch generation.

Results appear in:

```
OUTPUT/
```

Each result contains:

* `NNNN_sceneName.png`
* `NNNN_sceneName.txt` (Gemini prompt)

---

# 🖼 Placeholder Pack

If user doesn't want to include personal images, a placeholder pack is available:

👉 **placeholders_pack.zip**
(contains `face1_placeholder.png`, `face2_placeholder.png`, `scene_placeholder.png`, `output_placeholder.png`)

---

# 🌐 Dual Language Section (Русский + English)

## 🇷🇺 Описание

Этот инструмент автоматически:

* Берёт 2 изображения лиц
* Перебирает сцены из папки `SCENE/`
* Отправляет данные в Gemini → получает профессиональный Seedream-промпт
* Генерирует изображение в Seedream
* Сохраняет результат в `OUTPUT/`

Формат запросов строго фиксирован.

---

## 🇬🇧 English Description

This tool automates:

* Loading two identity reference images
* Iterating over scene set
* Generating Seedream prompts through Gemini
* Rendering final images through Seedream
* Saving all outputs neatly in a batch

The input order is always fixed.

---

# 📘 Troubleshooting

| Issue                 | Fix                               |
| --------------------- | --------------------------------- |
| Faces not detected    | Ensure exactly 2 files in `FACE/` |
| Scene not processed   | Check unsupported formats         |
| Gemini empty response | Check your prompt file            |
| Seedream 401          | Invalid API key                   |

---

# 📜 License

MIT License.
Use freely, even commercially.

---

# 🙌 Author

If you need:

* Function expansion
* UI for the pipeline
* Telegram bot version
* Full automation