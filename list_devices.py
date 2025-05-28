import pvrecorder

def list_audio_devices():
    devices = pvrecorder.PvRecorder.get_available_devices()
    if not devices:
        print("No audio devices found.")
    else:
        print("Available audio devices:")
        for i, device in enumerate(devices):
            print(f"index: {i}, device name: {device}")

if __name__ == "__main__":
    list_audio_devices()