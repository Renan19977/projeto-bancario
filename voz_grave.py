import pyaudio
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
PITCH_FACTOR = 0.7  # < 1 = voz mais grave, > 1 = voz mais aguda

p = pyaudio.PyAudio()

# Descobrir dispositivos de áudio
print("Dispositivos de áudio disponíveis:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"{i}: {info['name']}")

# Ajuste aqui se precisar: índice do seu microfone e do VB-Cable
INDEX_MIC = 1      # seu microfone real (confira no print acima)
INDEX_VBCABLE = 3  # saída "CABLE Input (VB-Audio Virtual Cable)"

# Captura do microfone
stream_in = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   input_device_index=INDEX_MIC,
                   frames_per_buffer=CHUNK)

# Saída no VB-Cable
stream_out = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    output_device_index=INDEX_VBCABLE)

print("Alterando voz em tempo real... CTRL+C para parar")

try:
    while True:
        data = stream_in.read(CHUNK, exception_on_overflow=False)
        audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32)

        # Pitch shifting simples
        indices = np.round(np.arange(0, len(audio_data), PITCH_FACTOR))
        indices = indices[indices < len(audio_data)].astype(int)
        audio_data = audio_data[indices]

        # Reamostrar para o tamanho fixo do chunk
        if len(audio_data) < CHUNK:
            audio_data = np.pad(audio_data, (0, CHUNK - len(audio_data)), mode='constant')

        audio_out = audio_data.astype(np.int16).tobytes()
        stream_out.write(audio_out)

except KeyboardInterrupt:
    print("\nEncerrado.")
    stream_in.stop_stream()
    stream_in.close()
    stream_out.stop_stream()
    stream_out.close()
    p.terminate()
