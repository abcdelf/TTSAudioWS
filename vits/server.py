import asyncio
import websockets
import json

import gen

async def rtts(websocket):
    async for message in websocket:
        try:
            req = json.loads(message)
            command = req["command"]
            text = req["text"]
            cfg = req["config"]
            af = cfg["audio_format"]
            pp = cfg["property"]
            sr = cfg["sample_rate"]
            
            if command != "START":
                await websocket.send(json.dumps({
                    "resp_type": "ERROR",
                    "error_msg": "command invalid"
                }))
                return
            if af != "pcm":
                await websocket.send(json.dumps({
                    "resp_type": "ERROR",
                    "error_msg": "audio format invalid"
                }))
                return
            if pp != "hindi":
                await websocket.send(json.dumps({
                    "resp_type": "ERROR",
                    "error_msg": "audio property invalid"
                }))
                return
            if sr != "16000":
                await websocket.send(json.dumps({
                        "resp_type": "ERROR",
                        "error_msg": "audio sample rate invalid"
                    }))
                return

            # All Config Check Passed
            # Request Backend
           
            await websocket.send(json.dumps({ 
                "resp_type": "START",
            } ))
            await websocket.send( gen.genaudio(text).tobytes())
        except:
            await websocket.send(json.dumps({
                    "resp_type": "ERROR",
                    "error_msg": "exception occurred"
                }))
    
        
        
        
        
async def main():
    async with websockets.serve(rtts, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())

