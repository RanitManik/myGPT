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
   
# Usage

### 1. create a Discord Bot
  
  1. Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
  
  2. Copy the bot token.

  3. Replace `Your Discord Application Token Goes here` in the `.env` file with the actual bot token.
  
  4. Visit the following link, replacing `<YOUR_CLIENT_ID>` with your bot's client ID:

### 2. Invite the Bot to Your Discord Server

  1. Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
  
  2. Copy the bot token.
  
  3. Replace `your_discord_bot_token` in the `.env` file with the actual bot token.
  
  4. Visit the following link, replacing `<YOUR_CLIENT_ID>` with your bot's client ID:

### 3. Create an OpenAI Account
  
  1. Visit the OpenAI website: [https://beta.openai.com/](https://beta.openai.com/)
  
  2. Sign up for an account if you don't have one. Follow the registration process.

### 4. Access the OpenAI API Section

  1. Once you're logged in, navigate to the OpenAI API section.
  
     - On the OpenAI dashboard, click on your account name in the top right corner.
     - Select "API" from the dropdown menu.

### 5. Create a New API Key

  1. In the API section, you'll find the option to create a new API key.
  
  2. Click on the "Create API Key" button.
  
  3. Give your API key a meaningful name related to your project (e.g., "RanitGPT").
  
  4. Copy the generated API key. It will look something like this: `sk-xxxxxx-xxxxxxxxxxxxxx`.
  
  5. Open the `.env` file in your RanitGPT project directory.
  
  6. Replace the placeholder `Your openAI API key goes here` with the actual API key you obtained from OpenAI:
  
     ```plaintext
     SECRET_KEY=your_discord_bot_token
     OPENAI_API_KEY=sk-xxxxxx-xxxxxxxxxxxxxx
     ```

### 6. Save and Run

  1. Save the changes to the `.env` file.

2. Now, when you run your RanitGPT bot, it will use the OpenAI GPT-3.5 Turbo model with the specified API key.

### 7. Verify Functionality

  1. Trigger the bot on Discord (mention `@RanitGPT`).
  
  2. Confirm that the bot is generating responses using the GPT-3.5 Turbo model.

By following these steps, you've successfully created an OpenAI GPT-3.5 Turbo API key and integrated it into your RanitGPT project. This key allows your bot to communicate with the OpenAI API and generate natural language responses.

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
