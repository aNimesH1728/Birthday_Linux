# 🎉 Terminal Birthday Greeter with OpenAI

A fun and customizable birthday greeting app that runs right in your Linux terminal! Built with Python and OpenAI's API, this tool generates personalized birthday messages based on traits you provide, with support for multiple wishes. Make someone's day special, right from your terminal! 🎂

---

## ✨ Features

- 🧠 AI-powered birthday message generation using OpenAI
- 🎯 Customize with any number of personality traits
- 💌 Generate multiple birthday wishes in one go
- 🎨 Colorful and festive terminal output (ASCII included!)
- 🐧 Works seamlessly on Linux-based systems

---

## 📸 Demo

```bash
$ ./greet.sh "Alice" "kind creative funny"
```

**Output:**
```
🎉🎂 Happy Birthday, Alice! 🎂🎉
You light up every room with your kind heart, creative spirit, and infectious humor.
Have the most amazing day—you deserve it!

🎈 Another wish:
May your year be filled with laughter, inspiration, and moments of pure joy.
```

---

## 🛠️ Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/birthday-greeter
cd birthday-greeter
```

2. **Set up your virtual environment (optional but recommended):**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install openai termcolor python-dotenv
```

4. **Add your OpenAI API key:**

Set your API key in the environment:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create a `.env` file:

```
OPENAI_API_KEY=your-api-key-here
```

5. **Make the script executable:**

```bash
chmod +x greet.sh
```

---

## 🚀 Usage

```bash
./greet.sh "Name" "optional traits"
```

- `"Name"`: The name of the person you're wishing.
- `"optional traits"`: (Optional) Space-separated list of personality traits (e.g., "kind smart creative").

### Example:

```bash
./greet.sh "Bob" "witty generous"
```

---

## 🧾 Project Structure

```
birthday-greeter/
├── greet.sh              # Bash wrapper to run the Python script
├── birthday_greeter.py   # Main logic for generating birthday greetings
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

---

## 🧠 How it Works

- Takes the name and optional traits from the command line.
- Sends a prompt to OpenAI's API to generate a warm and personal message.
- Formats the response with colors and ASCII decorations for a cheerful terminal output.

---

## 📌 Dependencies

- Python 3.7+
- `openai`
- `python-dotenv` (if using a `.env` file)
- Bash (Linux terminal)

---

## 📄 License

MIT License — feel free to use, modify, and share!

---

## 🙌 Acknowledgments

Inspired by the joy of making others smile 🎈  
Powered by [OpenAI](https://openai.com/)

---

## 💡 Future Ideas

- Add voice support with `pyttsx3` or `espeak`
- Export wishes to image or PDF
- Schedule automatic wishes via cron jobs

---

Feel free to contribute or suggest new features via issues or pull requests! 🎁
