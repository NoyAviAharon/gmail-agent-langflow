# Gmail Agent - Langflow

AI email assistant built with Langflow that sends emails via Gmail API based on natural language requests.

## 📋 Description

An intelligent email agent that:
- Understands natural language requests
- Identifies when a user wants to send an email
- Extracts recipient, subject, and body from the request
- Sends emails automatically via Gmail API

## 🏗️ Architecture

The flow consists of:
- **Chat Input** - Receives user messages
- **Agent** - AI model (Gemini) that processes requests and decides when to use the Gmail tool
- **Gmail Tool** - Custom component that sends emails via Gmail API
- **Chat Output** - Displays responses to user

## 📁 Files

| File | Description |
|------|-------------|
| `Gmail Agent.json` | Langflow flow export (import this into Langflow) |
| `gmail_component.py` | Custom Gmail tool component code |

## 🚀 Setup

### Prerequisites
- Langflow installed
- Google Cloud project with Gmail API enabled
- OAuth 2.0 credentials (Client ID, Client Secret, Refresh Token)

### Import the Flow
1. Open Langflow
2. Click **Import** 
3. Select `Gmail Agent.json`
4. Enter your credentials in the Gmail Tool component:
   - Client ID
   - Client Secret
   - Refresh Token

## 💬 Usage Examples

```
Send an email to john@example.com with subject "Hello" and body "How are you?"
```

```
Email my friend at sarah@gmail.com about the meeting tomorrow
```

## 🔐 Security

- API keys and tokens are NOT saved in the exported flow
- Never share your credentials publicly

## 👤 Author

Noy Avi-Aharon
