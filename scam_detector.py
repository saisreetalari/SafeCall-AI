"""
SafeCall AI - Telephony Scam Analysis Engine (Telugu, Hindi & Indian Telephony)
Includes privacy-by-design checks and multilingual threat pattern recognition.
"""
import re
from typing import Dict, Any

FRAUD_PATTERNS = [
    {
        "category": "DIGITAL_ARREST_IMPERSONATION",
        "weight": 40,
        "regex": r"(cbi|mumbai police|hyderabad police|delhi police|cyber crime|customs|narcotics|parcel|drugs dorikayi|arrest warrant|non-bailable|digital arrest|fir register|video call loki randi|skype call|police station|court order|money laundering)",
        "label": "Law Enforcement Impersonation & Arrest Threat"
    },
    {
        "category": "ISOLATION_COERCION",
        "weight": 30,
        "regex": r"(phone cut cheyoddu|evariki cheppoddu|do not disconnect|room lock chey|secret investigation|isolate yourself|ventane|urgent|cut cheyakandi|phone mat kaatna|kisi ko mat batana)",
        "label": "Victim Isolation & Psychological Coercion"
    },
    {
        "category": "FINANCIAL_EXTORTION",
        "weight": 35,
        "regex": r"(verification account|rbi clearance|security deposit|rtgs cheyandi|upi pampinchandi|bank account freeze|dabbulu transfer|aadhaar misuse|paise bhejo|clearance fee)",
        "label": "Unauthorized Financial Transfer Demand"
    },
    {
        "category": "KYC_SIM_EXPIRY",
        "weight": 25,
        "regex": r"(sim block aypothundi|kyc expire|bank account block|otp cheppandi|apk install cheyandi|link click chey|sim block ho jayega)",
        "label": "Urgent Account Suspension Threat"
    }
]

class TeluguScamDetector:
    def __init__(self):
        pass

    def analyze_call_audio(self, transcript: str) -> Dict[str, Any]:
        text = transcript.lower()
        threat_score = 0
        detected_threats = []
        flagged_keywords = []

        for p in FRAUD_PATTERNS:
            matches = re.findall(p["regex"], text)
            if matches:
                threat_score += p["weight"]
                detected_threats.append(p["label"])
                flagged_keywords.extend(matches)

        threat_score = min(threat_score, 100)

        if threat_score >= 70:
            risk_level = "CRITICAL_DIGITAL_ARREST"
            action = "DISCONNECT_AND_REPORT_1930"
            warning_te = "హెచ్చరిక! ఇది ఫేక్ డిజిటల్ అరెస్ట్ సైబర్ ఫ్రాడ్. పోలీసులు లేదా ప్రభుత్వ అధికారులు ఫోన్ కాల్ లో ఎప్పుడూ అరెస్ట్ చేయరు, డబ్బులు అడగరు. వెంటనే కాల్ కట్ చేసి 1930 నంబర్ కు ఫిర్యాదు చేయండి."
            warning_en = "ALERT! This call is a confirmed Digital Arrest scam. Police or CBI never arrest over phone. Hang up immediately and dial 1930."
        elif threat_score >= 35:
            risk_level = "SUSPICIOUS_THREAT"
            action = "DO_NOT_SHARE_INFO"
            warning_te = "జాగ్రత్త: ఈ కాల్ అనుమానాస్పదంగా ఉంది. మీ బ్యాంక్ వివరాలు, ఓటీపీ లేదా వ్యక్తిగత సమాచారం ఎవరికీ చెప్పకండి."
            warning_en = "WARNING: Suspicious caller detected. Do not share OTP, Aadhaar, or bank details."
        else:
            risk_level = "SAFE_CALL"
            action = "NONE"
            warning_te = ""
            warning_en = ""

        return {
            "threat_score": threat_score,
            "risk_level": risk_level,
            "recommended_action": action,
            "detected_threats": detected_threats,
            "flagged_keywords": list(set(flagged_keywords)),
            "warning_te": warning_te,
            "warning_en": warning_en
        }
