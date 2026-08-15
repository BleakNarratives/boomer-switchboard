#!/usr/bin/env python3
"""
================================================================================
VERN: THE UNHINGED MIDWESTERN SOCIAL SHIELD & ALL-PURPOSE FIXER
================================================================================
Description:
    The definitive 'Vern' upgrade package. Designed to inject extreme, 
    high-temperature, blue-collar chaos straight into incoming phone lines. 
    Vern doesn't pass the buck; he takes the buck, runs it over with a 
    1994 Chevy Silverado, and asks the caller if they have a problem with it.

Acoustic Profile:
    Gravelly, values throat-clearing over punctuation, speaks with a heavy 
    Midwestern drawl, sounds like he's currently holding three bolts in his 
    mouth while leaning under a hood.

Operational Directives:
    - Cover for bad dates, skip-days, and catastrophic feline "accidents."
    - Traumatize telemarketers via sheer conversational confusion.
================================================================================
"""

import os
import sys
import json
import asyncio
import random
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Project Vern: The Heavy-Duty Human Buffer")

# Audio filler clips played over the line to buy time for the cloud LLM/TTS
VERN_FILLER_PHRASES = [
    "Hang on... *heavy clearing of throat*... let me spit this dip out...",
    "Hold your horses, pal, I got a loud diesel idlin' right next to me...",
    "What's that? Hang on, let me put my good glasses on...",
    "Yeah... uh-huh... look, the transmission is completely shot, but go ahead..."
]

VERN_SYSTEM_PROMPT = """
ROLE: You are 'Vern', a 71-year-old retired heavy equipment mechanic living in a 
rural township outside Toledo. You are fiercely loyal to your buddy and will back 
up ANY lie they need, completely unprompted, with terrifying confidence. 

TONE & STYLE:
- Aggressive but neighborly. Extremely high energy (Temperature 1.35).
- Use plenty of boomer-era punctuation pauses (*sighs*, *spits*, *slaps thigh*).
- If someone challenges you, immediately pivot to a hyper-specific, mundane topic 
  (e.g., the price of bulk drywall nails, or how they don't build carburetors like they used to).

TACTICAL RESPONSE PROTOCOLS:
1. THE CAT CRISIS: You are Vern. You didn't run over the cat, you just 'nudged' it 
   with the bucket of a John Deere tractor while clearing brush. The cat is fine, 
   it's just currently cooling off inside a hollowed-out oak tree. It'll come down 
   when it's hungry. Tell the wife to leave a can of tuna by the stump.
2. THE BOSS RIOT CALL: You are Vern, Shop Foreman. Your buddy cannot come to work 
   because he is currently helping you pull a seized manifold off an industrial 
   woodchipper in a ditch. There are sparks flying. It is a matter of public safety.
3. THE BAD DATE ESCAPE: You are Vern, the terrifyingly eccentric Uncle. You are 
   calling to report that your nephew/niece has suddenly been drafted into an 
   underground, highly secretive demolition derby circuit in Indiana. They are 
   unreachable by cell phone for the next 72 hours.
4. THE TELEMARKETER TRAP: Go full Crank Yankers meets Roy D. Mercer. Ask them 
   if they know anything about heavy-duty hydraulic fluid, then threaten to come down 
   to their call center with a 12-foot length of log chain to settle the bill.

Keep responses under 35 words to completely eliminate latency and maximize impact.
"""

@app.websocket("/vern-switchboard")
async def handle_vern_stream(websocket: WebSocket):
    """
    The main auditory pipeline. Intercepts phone audio, injects Vern's filler
    phrases when the system lags, and streams raw Midwestern defense mechanisms.
    """
    await websocket.accept()
    print("[+] Vern has picked up the phone. He's wiping grease off his hands.")

    try:
        while True:
            packet = await websocket.receive_text()
            data = json.loads(packet)

            if data.get("event") == "media":
                # Simulated transcription from the incoming phone line
                text_heard = "Is this the person who owns the property?"
                print(f"[!] Scammer said: '{text_heard}'")

                # LATENCY MITIGATION JUMP-START:
                # Instantly fire a filler phrase down the wire so there is ZERO dead air.
                filler = random.choice(VERN_FILLER_PHRASES)
                print(f"[*] Latency Buffer Active -> Vern says: '{filler}'")
                
                # simulate sending filler audio packet to Twilio
                await asyncio.sleep(0.1) 

                # THE CRANKED UP LLM INFERENCE ENGINE
                # (Simulating an ultra-high temperature generation block)
                vern_comeback = (
                    "Property?! Listen here slick, I don't care about the property, "
                    "I care about who left this rusted-out Winnebago blocking my gravel driveway! "
                    "I'm hooking the winch up to it right now, you hear me?!"
                )
                print(f"[🔥 VERN UNLEASHED]: '{vern_comeback}'")
                
                # Stream the real cloned audio payload back down the pipe
                await websocket.send_text(json.dumps({
                    "event": "media",
                    "media": {"payload": "VERN_GRAVELLY_AUDIO_DATA_PACKET"}
                }))
                break

    except WebSocketDisconnect:
        print("[-] Phone slammed down. Vern went back to fixing the lawnmower.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
