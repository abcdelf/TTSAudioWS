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
    async with websockets.serve(rtts, "localhost", 8765):
        await asyncio.Future()

asyncio.run(main())



def rtts_demo():
    url = 'wss://{{endpoint}}/v1/{{project_id}}/rtts' 
    text = '待合成文本'
    token = '用户对应region的token'
    header = {
        'X-Auth-Token': token
    }
    body = {
        'command': 'START',
        'text': text,
        'config': {
            'audio_format': 'pcm',
            'property': 'chinese_xiaoyu_common',
            'sample_rate': '8000'
        }
    }

    def _on_message(ws, message):
        if isinstance(message, bytes):
            print('receive data length %d' % len(message))
        else:
            print(message)
    ws = websocket.WebSocketApp(url, header, on_message=_on_message, on_error=_on_error)
    ws.send(json.dumps(body), opcode=websocket.ABNF.OPCODE_TEXT)
    ws.close()