import ollama

def analyze_threat(mac, behavior_summary):
    """Uses local Llama3 to audit the network event."""
    prompt = f"""
    Analyze this network event:
    Device MAC: {mac}
    Detected Behavior: {behavior_summary}
    
    Return a JSON response with:
    1. "verdict": (ISOLATE/IGNORE/MONITOR)
    2. "reason": (Short explanation)
    """
    try:
        response = ollama.generate(model='llama3', prompt=prompt)
        return response['response']
    except Exception as e:
        return "ERROR: AI Offline. Defaulting to MONITOR."
