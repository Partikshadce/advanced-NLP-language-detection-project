"""
Language Detection NLP Project
Detects the language of input text using the langdetect library
"""

from langdetect import detect, detect_langs, LangDetectException
from colorama import init, Fore, Style
import sys
import os

# Set UTF-8 encoding for Windows console
if os.name == 'nt':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Initialize colorama for colored terminal output
init(autoreset=True)


def detect_language(text):
    """
    Detect the language of the given text
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        str: Detected language code (e.g., 'en', 'es', 'fr')
    """
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return None


def detect_language_with_probabilities(text):
    """
    Detect language with probability scores
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        list: List of language probabilities
    """
    try:
        languages = detect_langs(text)
        return languages
    except LangDetectException:
        return None


def get_language_name(code):
    """
    Convert language code to full language name
    
    Args:
        code (str): Language code (e.g., 'en')
        
    Returns:
        str: Full language name
    """
    language_map = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'pt': 'Portuguese',
        'nl': 'Dutch',
        'ru': 'Russian',
        'ja': 'Japanese',
        'zh-cn': 'Chinese (Simplified)',
        'zh-tw': 'Chinese (Traditional)',
        'ko': 'Korean',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'tr': 'Turkish',
        'pl': 'Polish',
        'sv': 'Swedish',
        'da': 'Danish',
        'no': 'Norwegian',
        'fi': 'Finnish',
        'cs': 'Czech',
        'el': 'Greek',
        'he': 'Hebrew',
        'th': 'Thai',
        'vi': 'Vietnamese',
        'id': 'Indonesian',
        'ro': 'Romanian',
        'hu': 'Hungarian',
        'uk': 'Ukrainian',
    }
    return language_map.get(code, code.upper())


def analyze_text(text):
    """
    Analyze text and display language detection results
    
    Args:
        text (str): Input text to analyze
    """
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.YELLOW}Text to analyze:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{text[:100]}{'...' if len(text) > 100 else ''}")
    print(f"{Fore.CYAN}{'='*60}\n")
    
    # Simple detection
    language = detect_language(text)
    if language:
        lang_name = get_language_name(language)
        print(f"{Fore.GREEN}✓ Detected Language: {Fore.MAGENTA}{lang_name} ({language})")
    else:
        print(f"{Fore.RED}✗ Could not detect language")
        return
    
    # Detection with probabilities
    print(f"\n{Fore.YELLOW}Probability Distribution:")
    languages = detect_language_with_probabilities(text)
    if languages:
        for lang in languages:
            lang_name = get_language_name(lang.lang)
            probability = lang.prob * 100
            bar_length = int(probability / 2)
            bar = '█' * bar_length
            print(f"{Fore.CYAN}{lang_name:20} ({lang.lang}): {Fore.GREEN}{bar} {probability:.2f}%")
    
    print(f"{Fore.CYAN}{'='*60}\n")


def interactive_mode():
    """
    Run the language detector in interactive mode
    """
    print(f"{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.YELLOW}       Language Detection NLP Project")
    print(f"{Fore.MAGENTA}{'='*60}\n")
    print(f"{Fore.WHITE}Enter text to detect its language (or 'quit' to exit)\n")
    
    while True:
        try:
            user_input = input(f"{Fore.GREEN}Enter text: {Style.RESET_ALL}")
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"\n{Fore.YELLOW}Goodbye!")
                break
            
            if not user_input.strip():
                print(f"{Fore.RED}Please enter some text!\n")
                continue
            
            analyze_text(user_input)
            
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}Goodbye!")
            break
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}\n")


def demo_mode():
    """
    Run demonstration with sample texts in different languages
    """
    print(f"{Fore.MAGENTA}{'='*60}")
    print(f"{Fore.YELLOW}       Language Detection - Demo Mode")
    print(f"{Fore.MAGENTA}{'='*60}\n")
    
    sample_texts = [
        "Hello, how are you today? This is a sample English text.",
        "Bonjour, comment allez-vous? Ceci est un exemple de texte français.",
        "Hola, ¿cómo estás? Este es un texto de ejemplo en español.",
        "Guten Tag, wie geht es Ihnen? Dies ist ein deutscher Beispieltext.",
        "Ciao, come stai? Questo è un testo di esempio in italiano.",
        "Olá, como você está? Este é um texto de exemplo em português.",
        "Привет, как дела? Это пример текста на русском языке.",
        "こんにちは、お元気ですか？これは日本語のサンプルテキストです。",
        "你好，你好吗？这是一个中文示例文本。",
        "नमस्ते, आप कैसे हैं? यह हिंदी में एक नमूना पाठ है।",
    ]
    
    for text in sample_texts:
        analyze_text(text)
        input(f"{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            demo_mode()
        else:
            # Detect language from command line argument
            text = " ".join(sys.argv[1:])
            analyze_text(text)
    else:
        interactive_mode()
