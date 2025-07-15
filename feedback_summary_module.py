from transformers import pipeline

# Modelo funcional y gratuito para análisis de sentimiento en español
model_id = "finiteautomata/beto-sentiment-analysis"
classifier = pipeline("sentiment-analysis", model=model_id)

def summarize_feedback(feedback_list, api_token=None):
    results = classifier(feedback_list)
    
    summary = ""
    for text, result in zip(feedback_list, results):
        label = result["label"]
        score = round(result["score"], 2)
        summary += f"- \"{text}\" → Sentimiento: {label} (confianza: {score})\n"
    
    return summary
