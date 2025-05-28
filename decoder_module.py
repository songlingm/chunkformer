import torch
from contextlib import nullcontext
from decode import init, endless_decode

class SpeechToTextDecoder:
    def __init__(self, model_checkpoint, device=None, autocast_dtype=None):
        self.device = torch.device(device or ("cuda" if torch.cuda.is_available() else "cpu"))
        dtype_map = {"fp32": torch.float32, "bf16": torch.bfloat16, "fp16": torch.float16, None: None}
        self.dtype = dtype_map[autocast_dtype]
        self.model, self.char_dict = init(model_checkpoint, self.device)

    def transcribe(self, audio_path, total_batch_duration=1800, chunk_size=64, left_context_size=128, right_context_size=128):
        from types import SimpleNamespace
        args = SimpleNamespace(
            long_form_audio=audio_path,
            total_batch_duration=total_batch_duration,
            chunk_size=chunk_size,
            left_context_size=left_context_size,
            right_context_size=right_context_size
        )
        with torch.autocast(self.device.type, self.dtype) if self.dtype else nullcontext():
            endless_decode(args, self.model, self.char_dict)