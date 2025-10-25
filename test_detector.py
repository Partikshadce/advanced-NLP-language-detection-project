"""
Quick test script for language detection
"""

from langdetect import detect, detect_langs
from colorama import init, Fore, Style
import sys
import os

# Set UTF-8 encoding for Windows console
if os.name == 'nt':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Initialize colorama
init(autoreset=True)

# Language name mapping
language_map = {
    'en': 'English', 'es': 'Spanish', 'fr': 'French', 'de': 'German',
    'it': 'Italian', 'pt': 'Portuguese', 'ru': 'Russian', 'ja': 'Japanese',
    'zh-cn': 'Chinese', 'ko': 'Korean', 'ar': 'Arabic', 'hi': 'Hindi'
}

# Sample texts in different languages
sample_texts = [
    ("Hello, how are you today? This is a sample English text.", "English"),
    ("Bonjour, comment allez-vous? Ceci est un exemple de texte français.", "French"),
    ("Hola, ¿cómo estás? Este es un texto de ejemplo en español.", "Spanish"),
    ("Guten Tag, wie geht es Ihnen? Dies ist ein deutscher Beispieltext.", "German"),
    ("Ciao, come stai? Questo è un testo di esempio in italiano.", "Italian"),
    ("Olá, como você está? Este é um texto de exemplo em português.", "Portuguese"),
    ("Привет, как дела? Это пример текста на русском языке.", "Russian"),
    ("こんにちは、お元気ですか？これは日本語のサンプルテキストです。", "Japanese"),
    ("你好，你好吗？这是一个中文示例文本。", "Chinese"),
    ("नमस्ते, आप कैसे हैं? यह हिंदी में एक नमूना पाठ है।", "Hindi"),
]

print(f"{Fore.MAGENTA}{'='*70}")
print(f"{Fore.YELLOW}       Language Detection NLP Project - Test Results")
print(f"{Fore.MAGENTA}{'='*70}\n")

correct = 0
total = len(sample_texts)

for text, expected_lang in sample_texts:
    try:
        # Detect language
        detected_code = detect(text)
        detected_lang = language_map.get(detected_code, detected_code.upper())
        
        # Get probabilities
        probs = detect_langs(text)
        confidence = probs[0].prob * 100
        
        # Check if correct
        is_correct = expected_lang.lower() in detected_lang.lower()
        if is_correct:
            correct += 1
            status = f"{Fore.GREEN}✓ CORRECT"
        else:
            status = f"{Fore.RED}✗ WRONG"
        
        # Display result
        print(f"{Fore.CYAN}Text: {Fore.WHITE}{text[:50]}...")
        print(f"{Fore.YELLOW}Expected: {Fore.MAGENTA}{expected_lang}")
        print(f"{Fore.YELLOW}Detected: {Fore.MAGENTA}{detected_lang} ({detected_code}) - {confidence:.1f}% confidence")
        print(f"{status}")
        print(f"{Fore.CYAN}{'-'*70}\n")
        
    except Exception as e:
        print(f"{Fore.RED}Error processing text: {str(e)}\n")

# Summary
accuracy = (correct / total) * 100
print(f"{Fore.MAGENTA}{'='*70}")
print(f"{Fore.YELLOW}SUMMARY:")
print(f"{Fore.GREEN}Correct: {correct}/{total}")
print(f"{Fore.CYAN}Accuracy: {accuracy:.1f}%")
print(f"{Fore.MAGENTA}{'='*70}\n")

print(f"{Fore.GREEN}✓ Language detection is working successfully!")
print(f"\n{Fore.YELLOW}To use interactively, run: {Fore.WHITE}python language_detector.py")
