"""
Advanced Language Detection System
Comprehensive NLP tool with analysis, visualization, and translation
"""

import os
import sys
from colorama import init, Fore, Style
from language_analyzer import LanguageAnalyzer
from visualizer import LanguageVisualizer

# Set UTF-8 encoding for Windows
if os.name == 'nt':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

init(autoreset=True)


def print_header():
    """Print application header"""
    print(f"\n{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.YELLOW}   🌍 ADVANCED LANGUAGE DETECTION & ANALYSIS SYSTEM 🌍")
    print(f"{Fore.MAGENTA}{'='*80}\n")


def print_menu():
    """Print main menu"""
    print(f"{Fore.CYAN}Choose an option:")
    print(f"{Fore.WHITE}  1. {Fore.GREEN}Analyze Text (Quick)")
    print(f"{Fore.WHITE}  2. {Fore.GREEN}Detailed Analysis Report")
    print(f"{Fore.WHITE}  3. {Fore.GREEN}Analyze with Visualizations")
    print(f"{Fore.WHITE}  4. {Fore.GREEN}Analyze File")
    print(f"{Fore.WHITE}  5. {Fore.GREEN}Multi-Language Demo")
    print(f"{Fore.WHITE}  6. {Fore.GREEN}Compare Multiple Texts")
    print(f"{Fore.WHITE}  7. {Fore.GREEN}Language Statistics")
    print(f"{Fore.WHITE}  0. {Fore.RED}Exit")
    print()


def quick_analysis(text):
    """Quick language detection"""
    analyzer = LanguageAnalyzer(text)
    
    if not analyzer.detected_lang:
        print(f"{Fore.RED}✗ Could not detect language")
        return
    
    lang_name = analyzer.get_language_name()
    confidence = analyzer.probabilities[0].prob * 100 if analyzer.probabilities else 0
    
    print(f"\n{Fore.CYAN}{'─'*70}")
    print(f"{Fore.YELLOW}Text: {Fore.WHITE}{text[:100]}{'...' if len(text) > 100 else ''}")
    print(f"{Fore.CYAN}{'─'*70}")
    print(f"{Fore.GREEN}✓ Language: {Fore.MAGENTA}{lang_name} ({analyzer.detected_lang})")
    print(f"{Fore.GREEN}✓ Confidence: {Fore.YELLOW}{confidence:.2f}%")
    
    if analyzer.is_multilingual():
        print(f"{Fore.YELLOW}⚠ Multilingual content detected!")
        print(f"{Fore.CYAN}Other languages found:")
        for name, code, prob in analyzer.get_all_detected_languages()[1:4]:
            print(f"  • {name} ({code}): {prob:.2f}%")
    
    print(f"{Fore.CYAN}{'─'*70}\n")


def detailed_analysis(text):
    """Detailed analysis with full report"""
    analyzer = LanguageAnalyzer(text)
    report = analyzer.generate_report()
    print(report)


def analysis_with_visualization(text):
    """Analysis with visual charts"""
    print(f"{Fore.YELLOW}Analyzing text and generating visualizations...\n")
    
    analyzer = LanguageAnalyzer(text)
    
    # Show text report
    report = analyzer.generate_report()
    print(report)
    
    # Generate visualizations
    visualizer = LanguageVisualizer()
    visualizer.create_comprehensive_dashboard(analyzer)


def analyze_file(file_path):
    """Analyze text from a file"""
    try:
        # Try different encodings
        text = None
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    text = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if not text:
            print(f"{Fore.RED}✗ Could not read file")
            return
        
        print(f"{Fore.GREEN}✓ File loaded: {Fore.WHITE}{file_path}")
        print(f"{Fore.CYAN}File size: {Fore.WHITE}{len(text):,} characters\n")
        
        detailed_analysis(text)
        
    except FileNotFoundError:
        print(f"{Fore.RED}✗ File not found: {file_path}")
    except Exception as e:
        print(f"{Fore.RED}✗ Error: {str(e)}")


def multi_language_demo():
    """Demonstrate detection across 20+ languages"""
    samples = [
        ("Hello, how are you?", "English"),
        ("Bonjour, comment allez-vous?", "French"),
        ("Hola, ¿cómo estás?", "Spanish"),
        ("Guten Tag, wie geht es Ihnen?", "German"),
        ("Ciao, come stai?", "Italian"),
        ("Olá, como você está?", "Portuguese"),
        ("Привет, как дела?", "Russian"),
        ("こんにちは、元気ですか？", "Japanese"),
        ("你好，你好吗？", "Chinese"),
        ("안녕하세요, 어떻게 지내세요?", "Korean"),
        ("مرحبا، كيف حالك؟", "Arabic"),
        ("नमस्ते, आप कैसे हैं?", "Hindi"),
        ("Hallo, hoe gaat het?", "Dutch"),
        ("Hej, hur mår du?", "Swedish"),
        ("Cześć, jak się masz?", "Polish"),
        ("Merhaba, nasılsın?", "Turkish"),
        ("Xin chào, bạn khỏe không?", "Vietnamese"),
        ("สวัสดี คุณเป็นอย่างไรบ้าง?", "Thai"),
        ("Halo, apa kabar?", "Indonesian"),
        ("שלום, מה שלומך?", "Hebrew"),
        ("Γεια σου, πώς είσαι?", "Greek"),
        ("Ahoj, jak se máš?", "Czech"),
        ("Здравей, как си?", "Bulgarian"),
        ("Kamusta ka?", "Tagalog"),
        ("Habari, habari gani?", "Swahili"),
    ]
    
    print(f"{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.YELLOW}   MULTI-LANGUAGE DETECTION DEMO (25 Languages)")
    print(f"{Fore.MAGENTA}{'='*80}\n")
    
    correct = 0
    results = []
    
    for text, expected in samples:
        analyzer = LanguageAnalyzer(text)
        detected = analyzer.get_language_name()
        confidence = analyzer.probabilities[0].prob * 100 if analyzer.probabilities else 0
        
        is_correct = expected.lower() in detected.lower()
        if is_correct:
            correct += 1
            status = f"{Fore.GREEN}✓"
        else:
            status = f"{Fore.RED}✗"
        
        results.append((expected, detected, confidence))
        
        print(f"{status} {Fore.CYAN}{expected:15} → {Fore.MAGENTA}{detected:20} "
              f"{Fore.YELLOW}({confidence:.1f}%)")
    
    accuracy = (correct / len(samples)) * 100
    
    print(f"\n{Fore.MAGENTA}{'─'*80}")
    print(f"{Fore.YELLOW}Results: {Fore.GREEN}{correct}/{len(samples)} correct "
          f"{Fore.CYAN}({accuracy:.1f}% accuracy)")
    print(f"{Fore.MAGENTA}{'─'*80}\n")
    
    # Create visualization
    visualizer = LanguageVisualizer()
    languages = [r[1] for r in results]
    confidences = [r[2] for r in results]
    visualizer.plot_language_distribution(languages, "25-Language Detection Test")
    visualizer.plot_confidence_scores(languages[:10], confidences[:10])


def compare_texts():
    """Compare multiple texts"""
    print(f"{Fore.YELLOW}Enter texts to compare (enter 'done' when finished):\n")
    
    texts = []
    i = 1
    while True:
        text = input(f"{Fore.GREEN}Text {i}: {Style.RESET_ALL}")
        if text.lower() == 'done':
            break
        if text.strip():
            texts.append(text)
            i += 1
    
    if len(texts) < 2:
        print(f"{Fore.RED}Need at least 2 texts to compare!")
        return
    
    print(f"\n{Fore.CYAN}{'='*80}")
    print(f"{Fore.YELLOW}COMPARISON RESULTS")
    print(f"{Fore.CYAN}{'='*80}\n")
    
    for i, text in enumerate(texts, 1):
        analyzer = LanguageAnalyzer(text)
        lang_name = analyzer.get_language_name()
        stats = analyzer.get_text_statistics()
        
        print(f"{Fore.MAGENTA}Text {i}:")
        print(f"{Fore.WHITE}  {text[:60]}{'...' if len(text) > 60 else ''}")
        print(f"{Fore.CYAN}  Language: {Fore.GREEN}{lang_name}")
        print(f"{Fore.CYAN}  Words: {Fore.YELLOW}{stats['total_words']:,}")
        print(f"{Fore.CYAN}  Characters: {Fore.YELLOW}{stats['total_chars']:,}")
        print()


def show_language_stats():
    """Show supported languages and statistics"""
    print(f"{Fore.MAGENTA}{'='*80}")
    print(f"{Fore.YELLOW}   SUPPORTED LANGUAGES ({len(LanguageAnalyzer.LANGUAGE_MAP)} Total)")
    print(f"{Fore.MAGENTA}{'='*80}\n")
    
    # Group by script/region
    groups = {
        'European': ['en', 'es', 'fr', 'de', 'it', 'pt', 'nl', 'sv', 'da', 'no', 'fi', 
                     'pl', 'cs', 'sk', 'ro', 'hu', 'hr', 'sl', 'et', 'lv', 'lt'],
        'Cyrillic': ['ru', 'uk', 'bg', 'mk'],
        'Asian': ['ja', 'zh-cn', 'zh-tw', 'ko', 'th', 'vi', 'id'],
        'Indic': ['hi', 'bn', 'gu', 'kn', 'ml', 'mr', 'ne', 'pa', 'ta', 'te', 'ur'],
        'Middle Eastern': ['ar', 'fa', 'he', 'tr'],
        'Other': ['af', 'sq', 'ca', 'cy', 'el', 'so', 'sw', 'tl']
    }
    
    for group, codes in groups.items():
        print(f"{Fore.CYAN}{group} Languages:")
        langs = [LanguageAnalyzer.LANGUAGE_MAP.get(code, code) for code in codes 
                 if code in LanguageAnalyzer.LANGUAGE_MAP]
        for i in range(0, len(langs), 4):
            row = langs[i:i+4]
            print(f"{Fore.WHITE}  " + " | ".join(f"{lang:18}" for lang in row))
        print()


def interactive_mode():
    """Main interactive mode"""
    print_header()
    
    while True:
        print_menu()
        choice = input(f"{Fore.GREEN}Select option: {Style.RESET_ALL}").strip()
        
        if choice == '0':
            print(f"\n{Fore.YELLOW}Thank you for using Advanced Language Detection! 👋\n")
            break
        
        elif choice == '1':
            text = input(f"\n{Fore.GREEN}Enter text: {Style.RESET_ALL}")
            if text.strip():
                quick_analysis(text)
        
        elif choice == '2':
            text = input(f"\n{Fore.GREEN}Enter text: {Style.RESET_ALL}")
            if text.strip():
                detailed_analysis(text)
        
        elif choice == '3':
            text = input(f"\n{Fore.GREEN}Enter text: {Style.RESET_ALL}")
            if text.strip():
                analysis_with_visualization(text)
        
        elif choice == '4':
            file_path = input(f"\n{Fore.GREEN}Enter file path: {Style.RESET_ALL}")
            if file_path.strip():
                analyze_file(file_path.strip())
        
        elif choice == '5':
            multi_language_demo()
        
        elif choice == '6':
            compare_texts()
        
        elif choice == '7':
            show_language_stats()
        
        else:
            print(f"{Fore.RED}Invalid option! Please try again.\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--demo":
            multi_language_demo()
        elif sys.argv[1] == "--stats":
            show_language_stats()
        else:
            # Analyze text from command line
            text = " ".join(sys.argv[1:])
            quick_analysis(text)
    else:
        interactive_mode()
