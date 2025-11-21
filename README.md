# **Helper Bot 🐱 – Discord AI Assistant**

Bot Discord sviluppato in Python che utilizza l’AI per rispondere alle domande degli utenti e fornire assistenza tecnica direttamente in chat.  
È leggero, semplice da configurare e pronto da avviare sia in locale che su piattaforme come Railway.

---

## **✨ Funzionalità principali**
- 📌 Risponde automaticamente ai messaggi che terminano con `*`
- 🤖 Integra l’AI tramite OpenAI per generare risposte utili e chiare
- ⚙️ Comando `/ping`
- 🧵 Codice semplice e facilmente estendibile
- ☁️ Deploy rapido su Railway o localmente

---

## **📦 Installazione**

Clona la repo:

```bash
git clone https://github.com/sadsotti/helper-bot.git
cd helper-bot
```

Installa le dipendenze:

```bash
pip install -r requirements.txt
```

---

## **🔧 Creazione del bot Discord**

### **1️⃣ Crea l'app nel Developer Portal**
1. Vai su https://discord.com/developers/applications  
2. Clicca **“New Application”**  
3. Dai un nome al bot → *Helper Bot*  
4. Conferma

---

### **2️⃣ Crea il bot**
1. Vai su **Bot** nel menu a sinistra  
2. Clicca **“Add Bot”**  
3. Conferma con *Yes, do it!*  
4. (Opzionale) Imposta icona e nome

---

### **3️⃣ Copia il token**
In **Bot → Token**:
1. Clicca **Reset Token**  
2. Copia la chiave  
3. Mettila nel tuo `.env`:

```
DISCORD_TOKEN=IL_TUO_TOKEN
```

⚠️ Non condividere MAI il token.

---

### **4️⃣ Abilita i Privileged Gateway Intents**
Sempre in **Bot**:
- ✔ Message Content Intent  
- ✔ (Opzionale) Presence Intent  
- ✔ (Opzionale) Server Members Intent  

Salva.

---

### **5️⃣ Invita il bot nel server**
Vai su **OAuth2 → URL Generator**

**Scopes:**
- `bot`
- `applications.commands`

**Bot Permissions:**
- `Read Messages`
- `Send Messages`
- `Use Slash Commands`

Copia il link generato → aprilo → scegli il tuo server → **Authorize**.

Il bot ora appare nel server (offline fino all'avvio dello script).

---

## **🔐 Configurazione**

Crea un file `.env`:

```
DISCORD_TOKEN=il_tuo_token_del_bot
OPENAI_API_KEY=la_tua_api_key_openai
```

Non caricare mai `.env` su GitHub.

---

## **🚀 Avvio del bot**

```bash
python main.py
```

Output atteso:

```
Bot attivo come: Helper Bot 🐱
```

---

## **💬 Come si usa**

### **1. Interazione AI automatica**
Il bot risponde ai messaggi che terminano con:

```
*
```

Esempio:

```
Perché Python mi dà errore su una lista?*
```

### **2. Slash command**
```
/ping
```

Risposta:

```
Pong! 🏓
```

---

## **🧠 Come il bot capisce che stai parlando con lui**

Il bot controlla la fine del messaggio:

```python
if message.content.endswith("*"):
```

Quindi risponde **solo** quando vuoi tu.

---

## **☁️ Deploy su Railway**

### 1️⃣ Carica il progetto su GitHub  
Assicurati di avere il tuo `.gitignore` configurato:

```
.env
__pycache__/
venv/
```

### 2️⃣ Vai su Railway → New Project → Deploy from GitHub

### 3️⃣ Imposta le variabili d’ambiente:
- `DISCORD_TOKEN`
- `OPENAI_API_KEY`

### 4️⃣ Comando di avvio:
```
python main.py
```

Railway avvierà il bot automaticamente.

---

## **🛠 Personalizzazione**

Puoi facilmente aggiungere:
- nuovi comandi
- analisi più complesse dei messaggi
- risposte nei thread
- canali dedicati
- sistemi ticket

---
