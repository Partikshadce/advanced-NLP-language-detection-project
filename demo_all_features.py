"""
Comprehensive Demo - Showcases All Features
Run this to see everything the system can do
"""

import os
import sys
from colorama import init, Fore, Style

# Set UTF-8 encoding for Windows
if os.name == 'nt':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

init(autoreset=True)

from language_analyzer import LanguageAnalyzer
from visualizer import LanguageVisualizer


def print_section(title):
    """Print section header"""
    print(f"\n{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.YELLOW}{title.center(80)}")
    print(f"{Fore.MAGENTA}{'='*80}\n")


def demo_basic_detection():
    """Demo 1: Basic Language Detection"""
    print_section("DEMO 1: BASIC LANGUAGE DETECTION")
    
    samples = [
        "Hello, how are you today?",
        "Bonjour, comment allez-vous?",
        "Hola, ¿cómo estás?",
        "Guten Tag, wie geht es Ihnen?",
        "こんにちは、お元気ですか？"
    ]
    
    for text in samples:
        analyzer = LanguageAnalyzer(text)
        lang = analyzer.get_language_name()
        confidence = analyzer.probabilities[0].prob * 100 if analyzer.probabilities else 0
        print(f"{Fore.CYAN}Text: {Fore.WHITE}{text}")
        print(f"{Fore.GREEN}→ {lang} ({confidence:.1f}% confidence)\n")


def demo_detailed_analysis():
    """Demo 2: Detailed Text Analysis"""
    print_section("DEMO 2: DETAILED TEXT ANALYSIS")
    
    text = """Natural Language Processing is a fascinating field of artificial intelligence 
    that enables computers to understand, interpret, and generate human language. 
    It combines computational linguistics with machine learning and deep learning models."""
    
    analyzer = LanguageAnalyzer(text)
    print(analyzer.generate_report())


def demo_multilingual_detection():
    """Demo 3: Multilingual Content Detection"""
    print_section("DEMO 3: MULTILINGUAL CONTENT DETECTION")
    
    mixed_text = "Hello everyone! Bonjour à tous! Hola a todos! This is a multilingual message."
    
    analyzer = LanguageAnalyzer(mixed_text)
    
    print(f"{Fore.CYAN}Text: {Fore.WHITE}{mixed_text}\n")
    print(f"{Fore.YELLOW}Detected Languages:")
    
    for name, code, prob in analyzer.get_all_detected_languages()[:5]:
        bar = '█' * int(prob / 2)
        print(f"{Fore.CYAN}{name:20} ({code}): {Fore.GREEN}{bar} {prob:.2f}%")
    
    if analyzer.is_multilingual():
        print(f"\n{Fore.YELLOW}⚠ This text contains multiple languages!")


def demo_script_detection():
    """Demo 4: Writing Script Detection"""
    print_section("DEMO 4: WRITING SCRIPT DETECTION")
    
    scripts = [
        ("Hello World", "Latin"),
        ("Привет мир", "Cyrillic"),
        ("مرحبا بالعالم", "Arabic"),
        ("你好世界", "Chinese"),
        ("こんにちは世界", "Japanese"),
        ("안녕하세요 세계", "Korean"),
        ("नमस्ते दुनिया", "Devanagari"),
    ]
    
    for text, expected in scripts:
        analyzer = LanguageAnalyzer(text)
        detected_script = analyzer.detect_script_type()
        lang = analyzer.get_language_name()
        
        print(f"{Fore.CYAN}Text: {Fore.WHITE}{text:25} "
              f"{Fore.YELLOW}Script: {Fore.GREEN}{detected_script:15} "
              f"{Fore.MAGENTA}Language: {lang}")


def demo_text_statistics():
    """Demo 5: Text Statistics"""
    print_section("DEMO 5: TEXT STATISTICS")
    
    text = """The quick brown fox jumps over the lazy dog. 
    This sentence contains every letter of the alphabet. 
    It is commonly used for testing fonts and keyboards."""
    
    analyzer = LanguageAnalyzer(text)
    stats = analyzer.get_text_statistics()
    
    print(f"{Fore.CYAN}Sample Text:")
    print(f"{Fore.WHITE}{text}\n")
    
    print(f"{Fore.YELLOW}Statistics:")
    print(f"{Fore.GREEN}Total Characters: {Fore.WHITE}{stats['total_chars']:,}")
    print(f"{Fore.GREEN}Total Words: {Fore.WHITE}{stats['total_words']:,}")
    print(f"{Fore.GREEN}Total Sentences: {Fore.WHITE}{stats['total_sentences']:,}")
    print(f"{Fore.GREEN}Unique Words: {Fore.WHITE}{stats['unique_words']:,}")
    print(f"{Fore.GREEN}Average Word Length: {Fore.WHITE}{stats['avg_word_length']:.2f} characters")
    print(f"{Fore.GREEN}Alphabetic Characters: {Fore.WHITE}{stats['alphabetic_chars']:,}")
    print(f"{Fore.GREEN}Numeric Characters: {Fore.WHITE}{stats['numeric_chars']:,}")
    print(f"{Fore.GREEN}Special Characters: {Fore.WHITE}{stats['special_chars']:,}")


def demo_character_frequency():
    """Demo 6: Character Frequency Analysis"""
    print_section("DEMO 6: CHARACTER FREQUENCY ANALYSIS")
    
    text = "The quick brown fox jumps over the lazy dog"
    analyzer = LanguageAnalyzer(text)
    char_dist = analyzer.get_character_distribution()
    
    print(f"{Fore.CYAN}Text: {Fore.WHITE}{text}\n")
    print(f"{Fore.YELLOW}Top 10 Characters:")
    
    for char, count in char_dist:
        bar = '█' * count
        print(f"{Fore.MAGENTA}'{char}': {Fore.GREEN}{bar} {count}")


def demo_word_frequency():
    """Demo 7: Word Frequency Analysis"""
    print_section("DEMO 7: WORD FREQUENCY ANALYSIS")
    
    text = """Python is great. Python is powerful. Python is easy to learn. 
    Many developers love Python because Python is versatile."""
    
    analyzer = LanguageAnalyzer(text)
    word_freq = analyzer.get_word_frequency(10)
    
    print(f"{Fore.CYAN}Text: {Fore.WHITE}{text}\n")
    print(f"{Fore.YELLOW}Top 10 Words:")
    
    for word, count in word_freq:
        bar = '█' * (count * 3)
        print(f"{Fore.CYAN}{word:15} {Fore.GREEN}{bar} {count}")


def demo_visualizations():
    """Demo 8: Data Visualizations"""
    print_section("DEMO 8: DATA VISUALIZATIONS")
    
    text = """Natural Language Processing enables computers to understand human language. 
    It uses machine learning and deep learning techniques to analyze text data."""
    
    print(f"{Fore.YELLOW}Generating visualizations for sample text...\n")
    
    analyzer = LanguageAnalyzer(text)
    visualizer = LanguageVisualizer(output_dir='demo_visualizations')
    
    try:
        visualizer.create_comprehensive_dashboard(analyzer)
        print(f"\n{Fore.GREEN}✓ Visualizations saved to 'demo_visualizations/' directory")
    except Exception as e:
        print(f"{Fore.RED}Note: Visualization generation requires display (skipped in some environments)")


def demo_country_info():
    """Demo 9: Country/Region Information"""
    print_section("DEMO 9: COUNTRY/REGION INFORMATION")
    
    samples = [
        "Hello, welcome to our website!",
        "Bonjour, bienvenue sur notre site!",
        "Hola, bienvenido a nuestro sitio!",
        "Willkommen auf unserer Website!",
        "こんにちは、私たちのウェブサイトへようこそ！"
    ]
    
    for text in samples:
        analyzer = LanguageAnalyzer(text)
        lang = analyzer.get_language_name()
        country = analyzer.get_country_info()
        
        print(f"{Fore.CYAN}Language: {Fore.MAGENTA}{lang:20}", end="")
        if country:
            print(f"{Fore.YELLOW}Primary Region: {Fore.GREEN}{country['name']} ({country['code']})")
        else:
            print(f"{Fore.YELLOW}Primary Region: {Fore.WHITE}N/A")


def demo_accuracy_test():
    """Demo 10: Accuracy Test"""
    print_section("DEMO 10: ACCURACY TEST (10 LANGUAGES)")
    
    test_cases = [
        ("Hello, how are you today?", "English"),
        ("Bonjour, comment allez-vous?", "French"),
        ("Hola, ¿cómo estás?", "Spanish"),
        ("Guten Tag, wie geht es Ihnen?", "German"),
        ("Ciao, come stai?", "Italian"),
        ("Olá, como você está?", "Portuguese"),
        ("Привет, как дела?", "Russian"),
        ("こんにちは、元気ですか？", "Japanese"),
        ("你好，你好吗？", "Chinese"),
        ("नमस्ते, आप कैसे हैं?", "Hindi"),
    ]
    
    correct = 0
    
    for text, expected in test_cases:
        analyzer = LanguageAnalyzer(text)
        detected = analyzer.get_language_name()
        is_correct = expected.lower() in detected.lower()
        
        if is_correct:
            correct += 1
            status = f"{Fore.GREEN}✓"
        else:
            status = f"{Fore.RED}✗"
        
        print(f"{status} {Fore.CYAN}{expected:15} → {Fore.MAGENTA}{detected}")
    
    accuracy = (correct / len(test_cases)) * 100
    print(f"\n{Fore.YELLOW}Accuracy: {Fore.GREEN}{correct}/{len(test_cases)} "
          f"({accuracy:.1f}%)")


def main():
    """Run all demos"""
    print(f"\n{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.YELLOW}{'🌍 COMPREHENSIVE FEATURE DEMONSTRATION 🌍'.center(80)}")
    print(f"{Fore.CYAN}{'Advanced Language Detection & Analysis System'.center(80)}")
    print(f"{Fore.MAGENTA}{'='*80}\n")
    
    print(f"{Fore.WHITE}This demo showcases all 10 major features of the system.\n")
    
    input(f"{Fore.YELLOW}Press Enter to start the demo...{Style.RESET_ALL}")
    
    # Run all demos
    demo_basic_detection()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_detailed_analysis()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_multilingual_detection()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_script_detection()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_text_statistics()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_character_frequency()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_word_frequency()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_visualizations()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_country_info()
    input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
    
    demo_accuracy_test()
    
    # Final summary
    print(f"\n{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.GREEN}{'✓ DEMO COMPLETE!'.center(80)}")
    print(f"{Fore.MAGENTA}{'='*80}\n")
    
    print(f"{Fore.YELLOW}Features Demonstrated:")
    print(f"{Fore.GREEN}  ✓ Basic language detection")
    print(f"{Fore.GREEN}  ✓ Detailed text analysis")
    print(f"{Fore.GREEN}  ✓ Multilingual content detection")
    print(f"{Fore.GREEN}  ✓ Writing script identification")
    print(f"{Fore.GREEN}  ✓ Text statistics")
    print(f"{Fore.GREEN}  ✓ Character frequency analysis")
    print(f"{Fore.GREEN}  ✓ Word frequency analysis")
    print(f"{Fore.GREEN}  ✓ Data visualizations")
    print(f"{Fore.GREEN}  ✓ Country/region mapping")
    print(f"{Fore.GREEN}  ✓ Accuracy testing")
    
    print(f"\n{Fore.CYAN}For more features, run: {Fore.WHITE}python advanced_detector.py")
    print(f"{Fore.CYAN}For batch processing, run: {Fore.WHITE}python batch_processor.py ./sample_texts")
    print(f"\n{Fore.YELLOW}Thank you for exploring the Advanced Language Detection System! 🌍\n")


if __name__ == "__main__":
    main()
