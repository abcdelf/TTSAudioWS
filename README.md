# TTSAudio Websocket Demo

This project aims to provide a Hindi language Text-to-Speech (TTS) system using code from VITS and a model from Facebook. The system allows users to input text and receive an audio stream as output through a WebSocket interface.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Introduction

The Hindi Language Text-to-Speech (TTS) project utilizes code from VITS (Variable Identity Transformer Synthesis) and a model developed by Facebook. TTS technology converts written text into synthesized speech, enabling applications to generate human-like speech from input text.

This project specifically focuses on providing a TTS system for the Hindi language, allowing users to convert written Hindi text into high-quality speech output. By leveraging the power of deep learning and natural language processing, the project aims to provide an accurate and expressive TTS solution for Hindi speakers.

## Setup
We suggest you to use docker for convience:

1. Clone the repository:

   ```
   git clone https://github.com/haoxingxing/TTSAudioWS
   cd TTSAudioWS
   ```
2. Docker build
    ```
    docker build . -t TTSAudioWS
    ```

or you can install it directly (Tested in ubuntu 22.04)

1. Clone the repository:

   ```
   git clone https://github.com/haoxingxing/TTSAudioWS
   cd TTSAudioWS
   ```

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

3. Install Vits and the facebook model

   ```
   ./install_tts.sh
   ```

4. Start the WebSocket server by running the following command:

   ```
   cd vits
   python server.py
   ```


## Usage
After you start the server,it will listen on ```0.0.0.0:8765```  
The api follows the doc in ```https://support.huaweicloud.com/api-sis/sis_03_0113.html```  
 **BUT THE ENDPOINT NEEDN'T TO BE FILLED IN THIS DEMO**  

 We added a demo client ```client.py```
 you can modify the txt in the py script to test  

## License

MIT License