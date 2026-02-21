import streamlit as st
from pydub import AudioSegment
from pydub.silence import split_on_silence
import io

st.title("✂️ Removedor de Silêncio")

file = st.file_uploader("Carregue o áudio", type=["mp3", "wav", "m4a"])

if file:
    with st.spinner("Limpando silêncio..."):
        audio = AudioSegment.from_file(file)
        chunks = split_on_silence(audio, min_silence_len=500, silence_thresh=audio.dBFS-14, keep_silence=200)
        combined = AudioSegment.empty()
        for chunk in chunks:
            combined += chunk
        
        out = io.BytesIO()
        combined.export(out, format="mp3")
        st.audio(out)
        st.download_button("Baixar Áudio Limpo", out.getvalue(), "audio_limpo.mp3")
