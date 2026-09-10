import numpy as np
from scipy.io.wavfile import write
from bark import generate_audio

def generate_bark_voiceover(text, output_file="voiceover.wav"):
    try:
        audio_array = generate_audio(text)  # Generate audio (NumPy array)
        sample_rate = 24000  # Bark outputs at 24kHz
        audio_int16 = np.int16(audio_array * 32767)  # Convert float32 to int16 (PCM format)
        
        write(output_file, sample_rate, audio_int16)  # Save as WAV
        print(f"✅ Voiceover saved as {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error generating voiceover: {e}")
        return None

# Example usage
text = "Welcome to our AI-generated video! Stay tuned for more."
voiceover_file = generate_bark_voiceover(text)
