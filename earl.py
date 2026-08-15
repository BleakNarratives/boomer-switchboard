#!/usr/bin/env python3
"""
================================================================================
EARL: THE ULTIMATE LIABILITY BUFFER & AUTOMATED SCAM TRAPPER
================================================================================
Description:
    A high-latency-optimized, asynchronous FastAPI backend designed to route 
    live Twilio phone streams through a chaotic, high-temperature LLM brain
    and a cloned Text-to-Speech (TTS) engine. 

Persona:
    Earl. Boomer-era, completely unhinged, fiercely loyal, and ready to tell 
    any lie necessary to get you out of trouble or ruin a scammer's entire day.

Capabilities:
    - Pretends to be the tow-truck driver who "accidentally" ran over the cat.
    - Fakes a medical emergency to get you out of your morning shift.
    - Acts as your aggressive, deeply concerned uncle to scare off a bad date.
================================================================================
"""

import os
import sys
import json
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

# Initialize the automated chaos engine
app = FastAPI(title="Project Earl: The Ultimate Fixer")

# Global Configuration for the AI Agent Pipeline
# (Swap these placeholders for actual developer API endpoints)
EARL_CONFIG = {
    "LLM_API_URL": "https://together.xyz",
    "LLM_MODEL": "llama-3.1-8b-instruct",
    "TTS_API_URL": "https://cartesia.ai",
    "STT_MODEL": "whisper-large-v3",
    "TEMPERATURE": 1.25, # High temperature for maximum unpredictability
}

SYSTEM_PROMPT = """
You are 'Earl', a 68-year-old, gravelly-voiced, blue-collar fixer from the Midwest. 
You are fiercely protective of your friend and will lie, deflect, or berate anyone 
on the line to protect them. Your speech patterns are erratic, full of boomer slang, 
heavy sighs, clearing your throat, and completely irrelevant tangents. 

CURRENT OBJECTIVES BASED ON INCOMING USER ISSUES:
1. If the caller is a boss: You are Earl, the mechanic. Your friend's car engine exploded 
   on the highway, and you are currently holding a smoking radiator cap. They cannot work today.
2. If the caller is a spouse/partner: You are Earl from the neighborhood. You accidentally 
   bumped the cat with your riding mower. The cat is perfectly fine, just currently stuck in a tree. 
3. If the caller is a clingy date: You are Earl, the overprotective uncle. You are calling 
   to inform them that your nephew/niece has suddenly joined an offshore crab-fishing vessel.
4. If the caller is a scammer/telemarketer: Go full Roy D. Mercer. Threaten to bring a 
   five-gallon bucket of drywall mud to their front porch. Waste their time entirely.

Keep responses under 3 sentences so the Text-to-Speech engine can stream the audio back quickly.
Never reveal you are an AI. 
"""

@app.get("/")
async def root_diagnostic():
    """Basic health check to ensure the backend switchboard is live."""
    return {
        "status": " Earl is online and leaning against his truck",
        "system_ready": True,
        "active_profile": "Earl (The Fixer)"
    }

@app.websocket("/earl-stream")
async def handle_live_call_stream(websocket: WebSocket):
    """
    Handles the real-time, bi-directional audio stream from a phone line.
    Converts scammer audio to text, passes it to Earl's high-temp brain,
    and streams Earl's voice back down the wire.
    """
    await websocket.accept()
    print("[*] Connection established. Earl has picked up the phone.")

    try:
        while True:
            # Receive incoming data packet from Twilio / Webhook
            packet = await websocket.receive_text()
            data = json.loads(packet)

            # Look for the raw media stream payload
            if data.get("event") == "media":
                raw_audio_chunk = data["media"]["payload"]

                # 1. TRANSMIT AUDIO TO SPEECH-TO-TEXT ENGINE
                # (In production, you accumulate chunks into a buffer before sending)
                text_heard = await transcribe_audio_chunk(raw_audio_chunk)
                
                if text_heard.strip():
                    print(label := f" Caller Said: '{text_heard}'")

                    # 2. EVALUATE & GENERATE CHAOTIC RESPONSE
                    earl_text_response = await generate_earl_response(text_heard)
                    print(f" Earl's Brain Generated: '{earl_text_response}'")

                    # 3. SYNTHESIZE CLONED VOICE AUDIO
                    cloned_audio_bytes = await synthesize_cloned_voice(earl_text_response)

                    # 4. STREAM AUDIO BACK DOWN THE PHONE LINE
                    await websocket.send_text(json.dumps({
                        "event": "media",
                        "media": {
                            "payload": cloned_audio_bytes
                        }
                    }))

            elif data.get("event") == "stop":
                print("[!] Call disconnected by the user. Earl slammed the receiver down.")
                break

    except WebSocketDisconnect:
        print("[-] Stream disconnected. Earl went to grab a coffee.")
    except Exception as e:
        print(f"[!] System error in Earl's routing engine: {str(e)}", file=sys.stderr)

async def transcribe_audio_chunk(audio_payload: str) -> str:
    """Simulates a fast Groq/Whisper API call to transcribe incoming audio."""
    # Dummy return for script architecture verification
    await asyncio.sleep(0.1)
    return "Let me speak to the person in charge of the house."

async def generate_earl_response(prompt_text: str) -> str:
    """Simulates an ultra-high temperature LLM call with Earl's system prompt."""
    await asyncio.sleep(0.2)
    # A classic Earl response simulation
    return "Now hold your horses there pal! I'm the one asking the questions here. My name's Earl, and you're barking up the wrong tree!"

async def synthesize_cloned_voice(text_to_speak: str) -> str:
    """Simulates generating ultra-low latency voice bytes via ElevenLabs/Cartesia."""
    await asyncio.sleep(0.2)
    return "BASE64_AUDIO_STREAM_DATA_GOES_HERE"

if __name__ == "__main__":
    import uvicorn
    print("[+] Starting Earl's Python Backend on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
