import whisper
from transformers import pipeline, AutoTokenizer
import os
import warnings

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["KERAS_BACKEND"] = "torch"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def transcribe_audio(audio_path):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
    return result["text"]

def summarize_text(text):
    if len(text.strip()) < 100:  # Character length check
        return "Transcript too short for meaningful summary"
    
    try:
        tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
        summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            framework="pt",
            device=-1
        )
        
        # Token-based chunking with overlap
        tokens = tokenizer(text, return_tensors="pt", truncation=False).input_ids[0]
        max_length = 1024
        stride = 256
        chunks = []
        
        for i in range(0, len(tokens), max_length - stride):
            chunk = tokens[i:i + max_length]
            chunks.append(tokenizer.decode(chunk, skip_special_tokens=True))
        
        summaries = []
        for chunk in chunks:
            if len(chunk.split()) < 15:
                continue
            try:
                summary = summarizer(
                    chunk,
                    max_length=150,
                    min_length=30,
                    do_sample=False
                )
                summaries.append(summary[0]['summary_text'])
            except Exception:
                continue
        
        return ' '.join(summaries) if summaries else "No meaningful summary generated"
    
    except Exception as e:
        return f"Summarization failed: {str(e)}"
