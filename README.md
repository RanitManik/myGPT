<div  align = "center">
  <img src="https://github.com/RanitManik/myGPT/assets/138437760/0631b375-ca63-4c39-9e6c-686b6372cfe5" height="100">
  <h1>myGPT Discord Chatbot</h1>
</div>

# Overview

myGPT is a Discord chatbot powered by OpenAI's GPT-3.5 Turbo model created using Python. 
It reads messages from a specified chat file and responds to mentions in Discord using the GPT-3.5 Turbo model.

# Features

- Seamless integration with Discord
- Configurable chat file selection
- Utilizes OpenAI GPT-3.5 Turbo for natural language understanding
- Easy-to-use and extendable

# Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RanitManik/your-repo.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the project root and add the following:

   ```plaintext
   SECRET_KEY=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```
# Usage

1. Run the bot:

   ```bash
   python3 main.py
   ```

2. Invite the bot to your Discord server and ensure it has the necessary permissions.
   [Download Link](https://discord.com/oauth2/authorize?client_id=1188130542902837258&permissions=1024&scope=bot)

4. Start chatting! Mention the bot (add `@myGPT` before each prompt) to trigger responses based on the GPT-3.5 Turbo model.

# Configuration

You can configure the bot by modifying the following variables in `bot.py`:

- `fileNumber`: Choose the chat file by setting this variable to 1, 2, or 3.
- `model`: Specify the GPT model to be used (default is "gpt-3.5-turbo").
- Adjust other parameters like `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty` as needed.

# Chat Files

- `chats/chat1.txt`: [Sample chat file 1](chats/chat1.txt) — my resume
- `chats/chat2.txt`: [Sample chat file 2](chats/chat2.txt) — whatsapp chat bwtween me and my friend
- `chats/chat3.txt`: [Sample chat file 3](chats/chat3.txt) — a simple AI generated friends chat

# Contributing

1. Clone the repository:

   ```bash
   git clone https://github.com/RanitManik/myGPT.git
   ```

2. **Add This repo as Remote**:

   ```bash
   git remote add origin https://github.com/RanitManik/myGPT.git
   ```

3. **Create a New Branch** for your feature or bugfix:

   ```bash
   git checkout -b feature/{your_feature} or bugfix/{issue_number}
   ```

4. **Commit** your changes:

   ```bash
   git commit -m "Your meaningful commit message here"
   ```

5. **Push** your changes to the repository:

   ```bash
   git push origin feature/{your_feature} or bugfix/{issue_number}
   ```

Feel free to contribute to the project by opening issues or pull requests. Any feedback or improvements are appreciated.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Contact

- Name - [Ranit Manik](https://github.com/RanitManik)
- Email - ranitmanikofficial@outlook.com
- Project Link - [https://github.com/RanitManik/Netflix-clone](https://github.com/RanitManik/Netflix-clone)

---

<p align="center"> If you like my work, maybe consider buying me a coffee/tea <img src="https://media.giphy.com/media/lRSeZ2ddNwhZ5AgIvk/giphy.gif" width="25">

<p align="center"><a href="https://www.buymeacoffee.com/ranitmanik" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150"></a>
