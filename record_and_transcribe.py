from pvrecorder import PvRecorder
import numpy as np
import soundfile as sf
from decoder_module import SpeechToTextDecoder

def record_audio(output_path="recorded.wav", device_index=None, duration=5, sample_rate=16000, frame_length=512):
    print("Initializing recorder...")
    recorder = PvRecorder(device_index=device_index, frame_length=frame_length)
    recorder.start()
    print("Recording... Speak now!")

    num_frames = int(sample_rate / frame_length * duration)
    frames = []

    try:
        for _ in range(num_frames):
            frame = recorder.read()
            frames.extend(frame)
    finally:
        recorder.stop()
        recorder.delete()

    audio = np.array(frames, dtype=np.int16)
    sf.write(output_path, audio, samplerate=sample_rate)
    print(f"Saved recording to {output_path}")

def list_devices():
    devices = PvRecorder.get_available_devices()
    print("Available audio devices:")
    for i, d in enumerate(devices):
        print(f"[{i}] {d}")

if __name__ == "__main__":
    #list_devices()  # Hiển thị thiết bị có thể chọn nếu cần
    device_index = 12  # Đổi số index nếu bạn muốn dùng thiết bị khác

    audio_path = "recorded.wav"
    model_path = "./chunkformer-large-vie"

    record_audio(output_path=audio_path, device_index=device_index, duration=5)

    decoder = SpeechToTextDecoder(model_checkpoint=model_path)
    decoder.transcribe(audio_path)

