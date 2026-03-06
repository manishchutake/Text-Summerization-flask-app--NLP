from transformers import pipeline

# load summarization model
summarizer = pipeline("summarization")

def summarize_text(text):

    result = summarizer(
        text,
        max_length=60,
        min_length=20,
        do_sample=False
    )

    return result[0]['summary_text']