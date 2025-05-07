# GhettoGlassApp

**A DIY Wearable Visual Reminder System** for neurodivergent professionals, built to capture real-time voice + visual cues during fast-paced environments like psychiatric rounds. Designed for local storage, privacy, and ADHD-friendly workflow support.

---

## 🧠 Core Idea

> See something. Say something. *Remember everything.*  
Whether it's a missing nameplate or a to-do you keep forgetting, GhettoGlassApp captures your moment and logs your verbal reminder—timestamped and stored locally.

---

## 🔧 Hardware Setup

- Old Android phone or **Raspberry Pi Zero W**
- Micro camera module (e.g., PiCam)
- USB/Bluetooth microphone
- Eyeglass frame to embed components
- Optional: Earbud, bone conduction mic, or haptic buzzer

---

## 🧰 Key Features

### 1. Visual Snapshot Logger
- Records a snapshot or short video when a voice note is triggered
- Saves locally with a timestamp
- Optional purge cycle (e.g., auto-delete after 48 hours)

### 2. Voice-Activated Notes
- Hotword: `"Note: remind me in 5 minutes to grab a marker"`
- Uses local speech-to-text (e.g., [whisper.cpp](https://github.com/ggerganov/whisper.cpp))
- Stores note + time in local log

### 3. Reminder Engine
- Parses time-based prompts ("in 10 minutes")
- Triggers haptic or audible reminder
- Optionally plays original audio and displays captured image

### 4. Memory Replay
- Voice query: `"What was I supposed to do at 10:30?"`
- Shows snapshot + verbal note taken at that time

---

## 🔒 Privacy & Ethics

- 100% **local storage**
- No cloud, no identifiable data
- Designed for **personal use** only in compliance with HIPAA-safe environments
- Manual disable switch and “kill mode” for sensitive settings

---

## 🔤 Stack Suggestions

| Component        | Tool              |
|------------------|-------------------|
| Voice Recognition | `whisper.cpp` / `vosk` |
| Text-to-Speech   | `Piper`           |
| Camera Control   | `fswebcam` / `PiCam` API |
| Task Timer       | `cron` / `Node timers` |
| Storage          | `SQLite` or flat `.json` |
| Interface        | CLI or mobile companion UI |

---

## 📦 Future Goals
- Minimalist HUD overlay
- OCR to read signage or charts
- Location-based smart reminders
- Day-summary dashboard (“Here’s what you forgot yesterday”)

---

## 🔗 Status

> MVP Planning Phase – Initial specs and feature list in development.  
> Community feedback welcome. Forks and collaboration encouraged.

---

## Hashtags
`#GhettoGlassApp` `#ADHDTech` `#NeurodivergentTools` `#AssistiveWearables` `#ESLAppSynergy`

---

