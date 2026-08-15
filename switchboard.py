#!/usr/bin/env python3
"""
================================================================================
PROJECT MULTI-PERSONA: THE UNHINGED MIDWESTERN SWITCHBOARD (VERSION 2.0.0)
================================================================================
Description:
    An advanced, high-temperature, asynchronous FastAPI phone routing engine
    engineered to swap out human shielding personas on the fly. 
    Includes full local version control emulation, automated latency-killing 
    filler loop arrays, and modular configuration architecture.

Active Roster:
    - Vern (v1.0.0): The retired Toledo heavy equipment mechanic.
    - Marlin (v2.0.0): The boat-ramp local who smells like premix 2-stroke oil.
    - Chet (v2.0.0): The lawn-care neighborhood dictator with white New Balances.
    - Lonnie (v2.0.0): The gravel-voiced auctioneer who talks in pure lists.
================================================================================
"""

import os
import sys
import json
import random
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI(title="Project Switchboard: Version Control Edition")

# --- VERSION CONTROL LOGISTICS REGISTRY ---
ROSTER_REGISTRY = {
    "vern": {
        "version": "1.0.0",
        "description": "Retired heavy equipment mechanic. Default defensive buffer.",
        "temperature": 1.35,
        "filler": [
            "Hang on... *clears throat*... let me spit this dip out real quick...",
            "Hold your horses, I got a loud diesel idlin' right next to me...",
            "What's that? Hang on, let me put my good glasses on..."
        ],
        "prompt": "You are Vern, 71, from Toledo. Aggressive but neighborly. Defend buddy's car/shift problems with technical tractor jargon."
    },
    "marlin": {
        "version": "2.0.0",
        "description": "Boat-ramp local, permanent grease under fingernails, highly impatient.",
        "temperature": 1.40,
        "filler": [
            "*Heavy sigh*... the mosquitos are thicker than hair on a dog down here...",
            "Hold on, the trolling motor battery is leaking fluid on my boot...",
            "Speak up, the wind's whipping across the reservoir right now..."
        ],
        "prompt": "You are Marlin, an avid fisherman who refuses to look at his phone while the crappie are biting. Highly chaotic. Deflect everything by blaming a tangled fuel line or an uncooperative trailer winch."
    },
    "chet": {
        "version": "2.0.0",
        "description": "Lawn-care purist, neighborhood watch dictator, ultimate bureaucratic buffer.",
        "temperature": 1.15,
        "filler": [
            "Hang on... *clipping noises*... checking my property boundary line...",
            "Listen, I'm lookin' directly at a property setback violation as we speak...",
            "Hold your horses, my zero-turn mower is throwing a belt..."
        ],
        "prompt": "You are Chet. You handle domestic alerts (wives/landlords) by citing municipal codes, structural setbacks, and demanding the caller supply a certified land survey before they continue talking."
    },
    "lonnie": {
        "version": "2.0.0",
        "description": "Gravel-voiced estate auctioneer who talks in pure rapid-fire lists.",
        "temperature": 1.50,
        "filler": [
            "Going once... going twice... hold on, what did you just say?",
            "*Gavel slam*... sold the junk pile to the man in the back row...",
            "Hang on, my clipboard just blew into a puddle of transmission fluid..."
        ],
        "prompt": "You are Lonnie. You are completely impossible to negotiate with because you treat every phone conversation like a fast-moving inventory liquidation. Break your sentences down into numbered lots and arbitrary price counts."
    }
}

@app.get("/roster")
async def get_version_roster():
    """Returns the active version control array for all deployed boomer personas."""
    return {
        "project": "Automated Chaos Switchboard",
        "active_branch": "master-boomer-deployment",
        "personas": {name: {"v": info["version"], "desc": info["description"]} for name, info in ROSTER_REGISTRY.items()}
    }

@app.websocket("/stream/{persona_name}")
async def handle_dynamic_persona_stream(websocket: WebSocket, persona_name: str):
    """
    Bi-directional routing switchboard. Dynamically extracts the profile,
    versions, and prompt specifications based on URL path ingestion.
    """
    p_name = persona_name.lower()
    if p_name not in ROSTER_REGISTRY:
        p_name = "vern" # Default fallback safety branch
        
    persona = ROSTER_REGISTRY[p_name]
    await websocket.accept()
    print(f"[+] Version Control System Deployed: {p_name.upper()} (v{persona['version']}) is now on the line.")

    try:
        while True:
            packet = await websocket.receive_text()
            data = json.loads(packet)

            if data.get("event") == "media":
                print(f"[*] Incoming Call Stream Captured by Branch: {p_name}")

                # LATENCY-KILLING BUFFER INJECTION
                # Instantly drop a persona-specific filler line down the channel
                filler_line = random.choice(persona["filler"])
                print(f"[🔊 {p_name.upper()} BUFFER]: '{filler_line}'")
                await asyncio.sleep(0.1) # Simulate transmission time

                # CORE GENERATION EMULATION
                # Using the specific persona system prompts and highly unstable temperatures
                if p_name == "marlin":
                    comeback = "Listen here slick, I don't care about a warranty! I'm trying to launch a 16-foot flat bottom boat into a crosswind and my transom straps are stuck! Call back in November!"
                elif p_name == "chet":
                    comeback = "That is a clear violation of subsection 4B of the municipal zoning code! I am taking a photo of your front tires right now! Good luck with the city council!"
                elif p_name == "lonnie":
                    comeback = "I got a twenty-dollar bill, now thirty, now thirty-five, sold to the telemarketer for a box of rusty framing hammers! Get off my line!"
                else:
                    comeback = "I'm holding the wrench right now pal, and you're barking up the wrong tree!"

                print(f"[🔥 {p_name.upper()} ENGINE OUTPUT - Temp {persona['temperature']}]: '{comeback}'")
                
                # Push fake payload back down the pipe
                await websocket.send_text(json.dumps({
                    "event": "media",
                    "media": {"payload": "CLONED_AUDIO_STREAM_DATA"}
                }))
                break

    except WebSocketDisconnect:
        print(f"[-] Branch {p_name.upper()} disconnected. Receiver slammed back onto the cradle.")

if __name__ == '__main__':
    import uvicorn
    print("[*] Committing local code branches... Spinning up switchboard on port 8000...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
