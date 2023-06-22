# -*- coding: utf-8 -*-
import asyncio
import json
import wave

import websockets

def pcm2wav(pcmdata, wav_file, channels=1, bits=16, sample_rate=16000):
    wavfile = wave.open(wav_file, 'wb')
    wavfile.setnchannels(channels)
    wavfile.setsampwidth(bits // 8)
    wavfile.setframerate(sample_rate)
    wavfile.writeframes(pcmdata)
    wavfile.close()
    print(len(pcmdata))
    # with open(wav_file, 'wb') as file:
    #     file.write(pcmdata)




audio_property = ["hindi"]


async def rtts():
    uri = "ws://localhost:8765/"
    sample_rate = "16000"
    async with websockets.connect(uri) as websocket:
        request_msg = {
            "command": "START",
            "config": {
                "audio_format": "pcm",
                "sample_rate": sample_rate,
                "property": audio_property[0],
            },
            "text": "1.	इस अन्धकार में प्रकाश की एक रेखा भी थी । स्कूल निकट होने के कारण बूढ़ी कल्लू की माँ मुझे किताबों के साथ वहाँ पहुँचा भी आती थी और ले भी आती थी और इस आवागमन के बीच में, कभी सड़क पर लड़ते हुए कुत्ते, कभी उनके भटकते हुए पिल्ले, कभी किसी कोने में बैठकर पंजों से मुँह धोती हुई बिल्ली, कभी किसी घर के बरामदे में लटकते हुए पिंजड़े में मनुष्य की स्वर-साधना करता हुआ गंगाराम, कभी बत्तख और तीतरों के झुण्ड, कभी तमाशा दिखलानेवाले के टोपी लगाए हुए बंदर, ओढ़नी ओढ़े हुए बँदरिया, नाचनेवाला रीछ आदि स्कूल की एकरसता दूर करते ही रहते थे"
        }
        await websocket.send(json.dumps(request_msg, ensure_ascii=False))
        res = await websocket.recv()
        print(res)
        audio_bin = b''
        count = 0
        while True:
            count += 1
            res = await websocket.recv()
            # print("get websocket res is ", res)
            if isinstance(res, str):
                resp = json.loads(res)
                print(resp)
                if resp.get('resp_type') == "END":
                    break
                if resp.get('resp_type') == "ERROR":
                    print('error occurred.......')
                    break
                print(resp)
            if isinstance(res, bytes):
                audio_bin += res
                # print(len(res),count)
        pcm2wav(audio_bin, './{}-{}.wav'.format(audio_property[0], sample_rate))


def run(text):
    try:
        asyncio.get_event_loop().run_until_complete(rtts())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(rtts())
