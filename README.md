# **Helper Bot 🐱 – Discord AI Assistant**

Discord bot developed in Python that uses AI to answer user questions and provide technical assistance directly in chat.  
It is lightweight, easy to configure, and ready to run either locally or on platforms like WispByte.

---

## **✨ Main Features**
- 📌 Automatically replies to messages ending with `*`
- 🤖 Integrates AI via OpenAI to generate helpful and clear responses
- ⚙️ `/ping` command
- 🧵 Simple and easily extendable code
- ☁️ Fast deployment on WispByte or locally

---

## **📦 Installation**

Clone the repository:

```bash
git clone https://github.com/sadsotti/helper-bot.git
cd helper-bot
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## **🔧 Creating the Discord Bot**

### **1️⃣ Create the app in the Developer Portal**
1. Go to https://discord.com/developers/applications 
2. Click “New Application” 
3. Give the bot a name → Helper Bot 
4. Confirm

---

### **2️⃣ Create the bot**
1. Go to **Bot** in the menu on the left  
2. Click **“Add Bot”**  
3. Confirm with *Yes, do it!*  
4. (Optional) Set icon and name

---

### **3️⃣ Copy the token**
In **Bot → Token**:
1. Click **Reset Token**  
2. Copy the key  
3. Put it in your `.env`:

```
DISCORD_TOKEN=YOUR_TOKEN
```

⚠️ Never share your token.

---

### **4️⃣ Enable Privileged Gateway Intents**
Still in **Bot**:
- ✔ Message Content Intent  
- ✔ (Optional) Presence Intent  
- ✔ (Optional) Server Members Intent  

Save.

---

### **5️⃣ Invite the bot to the server**
Go to **OAuth2 → URL Generator**

**Scopes:**
- `bot`
- `applications.commands`

**Bot Permissions:**
- `Read Messages`
- `Send Messages`
- `Use Slash Commands`

Copy the generated link → open it → select your server → **Authorize**.

The bot will now appear in the server (offline until you run the script).

---

## **🔐 Configuration**

Create a `.env` file:

```
DISCORD_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key
```

Never upload `.env` to GitHub.

---

## **🔑 Getting the OpenAI API Key**

To use AI in the bot, you need an **API key OpenAI**.  
OpenAI is **not free**: you need active credits, but **just a few euros are enough for thousands of requests**, especially when using inexpensive models like `gpt-4o-mini`.

### How to get it:

1. Go to https://platform.openai.com 
2. Log in 
3. Go to **User → API Keys**  
4. Click **Create new secret key**  
5. Copy the key  
6. Insert it into your `.env`:

```
OPENAI_API_KEY=your_key
```

⚠️ **Never share it**  
⚠️ If it goes online → **regenerate it immediately**

---

## **🚀 Starting the bot**

```bash
python main.py
```

Expected output:

```
Bot active as: Helper Bot 🐱
```

---

## **💬 How to use**

### **1. Automatic AI interaction**
The bot replies to messages ending with:

```
*
```

Example:

```
Why is Python giving me an error on a list?*
```

### **2. Slash command**
```
/ping
```

Response:

```
Pong! 🏓
```

---

## **🧠 How the bot knows you're talking to it**

The bot checks the end of the message:

```python
if message.content.endswith("*"):
```

So it replies **only** when you want it to.

---

## **☁️ Deploy on WispByte**

### 1️⃣ Prepare your files

Make sure you have `main.py`, `requirements.txt` and `.env` ready.

### 2️⃣ Upload to WispByte

1. Log in to the WispByte Panel.
2. Go to Files and upload your project files.
   Tip: Upload a .zip and use the "Unarchive" feature for faster uploads.

### 3️⃣ Startup Settings

Go to the Startup tab and configure:
- Python Version: Select Python 3.10/3.11 (Avoid 3.13 as it has compatibility issues with some libraries like audioop).
- Startup Command:
  
```
pip install -r requirements.txt && python main.py
```

### 4️⃣ Start the Bot

Go to the Console and click Start.
The panel will automatically install the requirements and launch the bot.

---

## **🛠 Customization**

You can easily add:
- new commands
- more complex message parsing
- thread replies
- dedicated channels
- ticket systems

---
