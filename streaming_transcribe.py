import threading
import queue
import time
import numpy as np
import soundfile as sf
from pvrecorder import PvRecorder
from decoder_module import SpeechToTextDecoder

SAMPLE_RATE = 16000
FRAME_LENGTH = 512
CHUNK_DURATION = 3.0  # seconds
CHUNK_SIZE = int(SAMPLE_RATE * CHUNK_DURATION)

audio_queue = queue.Queue()

def record_audio(device_index=0):
    recorder = PvRecorder(device_index=device_index, frame_length=FRAME_LENGTH)
    recorder.start()
    print("🎙️ Recording started... Press Ctrl+C to stop.")

    try:
        while True:
            frame = recorder.read()
            audio_queue.put(frame)
    except KeyboardInterrupt:
        print("\n🛑 Recording stopped.")
    finally:
        recorder.stop()
        recorder.delete()

def stream_transcribe(model_path="./chunkformer-large-vie"):
    decoder = SpeechToTextDecoder(model_checkpoint=model_path)
    buffer = []

    try:
        while True:
            try:
                frame = audio_queue.get(timeout=1)
                buffer.extend(frame)

                if len(buffer) >= CHUNK_SIZE:
                    chunk_np = np.array(buffer[:CHUNK_SIZE], dtype=np.int16)
                    buffer = buffer[CHUNK_SIZE:]  # remove processed part

                    audio_path = "temp_stream.wav"
                    sf.write(audio_path, chunk_np, samplerate=SAMPLE_RATE)
                    print("\n🧠 Transcribing last {:.1f}s...".format(CHUNK_DURATION))
                    decoder.transcribe(audio_path)
            except queue.Empty:
                continue
    except KeyboardInterrupt:
        print("\n🛑 Transcription stopped.")

def main():
    device_index = 1  # Change this index using list_devices.py if needed
    model_path = "./chunkformer-large-vie"

    record_thread = threading.Thread(target=record_audio, args=(device_index,))
    stt_thread = threading.Thread(target=stream_transcribe, args=(model_path,))

    record_thread.start()
    stt_thread.start()

    record_thread.join()
    stt_thread.join()

if __name__ == "__main__":
    main()
