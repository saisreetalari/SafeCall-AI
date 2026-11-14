# SafeCall AI (సేఫ్ కాల్ AI)
### Sovereign Telephony Cyber Defense & Digital Arrest Interceptor
*Engineered for **The Great Indian AI Internship Challenge** by **Gnani.ai***

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://python.org)
[![Gnani Prisma v3.0](https://img.shields.io/badge/ASR-Gnani%20Prisma%20v3.0-orange.svg)](https://gnani.ai)
[![Gnani Timbre v3.0](https://img.shields.io/badge/TTS-Gnani%20Timbre%20v3.0-cyan.svg)](https://gnani.ai)
[![Compliance](https://img.shields.io/badge/DPDP%20Act-100%25%20Compliant-emerald.svg)]()

---

## 📌 Executive Summary & 1-Page Pitch

### 1. The Crisis: The ₹1,750+ Crore "Digital Arrest" Epidemic
In Andhra Pradesh, Telangana, and across India, innocent citizens have lost over **₹1,750+ Crores** in 2024 to organized "Digital Arrest" cyber extortion calls. Fraudsters pose as Mumbai Police, CBI, or Customs officers, psychologically terrorizing victims in code-mixed languages:
> *"Mee Aadhaar card meeda parcel lo MDMA drugs dorikayi... non-bailable arrest warrant issue ayindi, phone cut cheyoddu!"*

Victims are pressured into staying on call for hours in isolation, culminating in emergency bank transfers.

**Why existing caller-ID apps fail:**
- Truecaller only screens static phone numbers. When scammers rotate spoofed VoIP lines or fresh SIMs, caller-ID provides zero defense.
- **Once an unknown call connects, citizens are completely on their own.**
- Global speech models fail on noisy 8kHz GSM telephony audio and colloquial Indic code-mixed speech (Tenglish / Hinglish).

---

### 2. The Solution: SafeCall AI
**SafeCall AI** is a sovereign, privacy-preserving in-call voice cyber shield designed specifically for Indian telephony:
1. **Real-Time Indic Telephony ASR (Gnani Prisma v3.0):** Streams 8kHz cellular audio into a dual-buffer pipeline, transcribing noisy, code-mixed Tenglish (Telugu + English) and Hinglish in sub-250ms chunks.
2. **Indic Coercion Heuristics Engine:** Continuously analyzes conversation vectors across 4 high-risk categories:
   - Law Enforcement & Arrest Impersonation (CBI, Mumbai Police, Narcotics)
   - Victim Isolation & Psychological Pressure (`"phone cut cheyoddu"`, `"room lock chey"`)
   - Urgent Unauthorized Financial Extortion (RTGS, UPI, `"verification account"`)
   - Telecom / KYC Suspension Threats
3. **In-Ear Emergency Voice Alert (Gnani Timbre v3.0):** When the Coercion Threat Index breaches critical threshold (≥70%), it whispers a discreet, authoritative spoken alert directly into the victim's earpiece in native Telugu or Hindi:
   > *"హెచ్చరిక! ఇది ఫేక్ డిజిటల్ అరెస్ట్ సైబర్ ఫ్రాడ్. పోలీసులు ఎప్పుడూ ఫోన్ కాల్ లో అరెస్ట్ చేయరు. వెంటనే కాల్ కట్ చేసి 1930 కి కాల్ చేయండి."*
4. **Autonomous Cyber Dispatch:** Enables 1-tap call termination while auto-generating incident metadata formatted for the National Cyber Crime Reporting Portal (Helpline 1930).

---

### 3. Sovereign Privacy-by-Design Architecture
Because telephone privacy is sacred, SafeCall AI is engineered under a zero-trust model:
- **Whitelisted Contacts Bypass:** Automatically hibernates for contacts saved in the user's phonebook (e.g., family and friends).
- **Zero Audio Persisted:** Audio chunks are held strictly in volatile RAM for 2 seconds to calculate threat vectors and are immediately wiped.
- **Zero Human In The Loop:** 100% automated pattern recognition running through sovereign Indian AI models.
- **DPDP Act 2023 Compliant:** Fully honors user privacy and data sovereignty.

---

## 🛠️ System Architecture & Quickstart

```
[ Incoming Telephony Call (8kHz GSM) ]
                 │
                 ▼
     [ Contact Whitelist Check ]
          ├── (Saved Contact) ──> [ Automatic Privacy Sleep ]
          └── (Unknown Caller) ──> [ 2-Second Ephemeral Buffer ]
                                             │
                                             ▼
                             [ Gnani Prisma v3.0 STT ]
                             (Telugu / Tenglish / Hindi)
                                             │
                                             ▼
                             [ Coercion Threat Index ]
                             (Impersonation, Urgency, RTGS)
                                             │
                                             ▼
                             [ Gnani Timbre v3.0 TTS ]
                             (In-Ear Spoken Native Warning)
                                             │
                                             ▼
                             [ 1-Tap National 1930 Dispatch ]
```

### Installation & Run

```bash
# Clone the repository
git clone https://github.com/your-username/SafeCallAI.git
cd SafeCallAI

# Install lightweight dependencies
pip install -r requirements.txt

# Launch the Cyber Defense Cockpit
python app.py
```

Open your browser at **`http://localhost:5000`** to interact with the live telemetry cockpit.

---

## 👥 Candidate & Submission Info
- **Project Name:** SafeCall AI (సేఫ్ కాల్ AI)
- **Author:** 3rd Year BCA (Data Science) Student
- **Track:** Sovereign AI for India
- **Challenge:** The Great Indian AI Internship Challenge (Gnani.ai)
- **Stack:** Python, Flask, Gnani.ai Prisma STT, Gnani.ai Timbre TTS, Tailwind CSS, Web Audio API
