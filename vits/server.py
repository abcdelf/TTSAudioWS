import asyncio
import websockets
import json
import os
import gen
def read_file(filename):
    with open(filename, 'rb') as file:
        byte_array = file.read()
    
    return byte_array
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
            
            res  = gen.genaudio(text).tobytes()
                        
            # res = res[44:]
            
            fragment_size = 1024
            total_length = len(res)
            num_fragments = total_length // fragment_size
            if total_length % fragment_size != 0:
                num_fragments += 1
                
            print(total_length,num_fragments)

            for i in range(num_fragments):
                start_index = i * fragment_size
                end_index = min(start_index + fragment_size, total_length)

                fragment = res[start_index:end_index]

                await websocket.send(fragment)
                
            await websocket.send(json.dumps({ 
                "resp_type": "END",
            } ))
        except:
            await websocket.send(json.dumps({
                    "resp_type": "ERROR",
                    "error_msg": "exception occurred"
                }))
    
        
        
        
        
async def main():
    async with websockets.serve(rtts, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())

