"""
Advanced Language Analysis Module
Provides detailed linguistic analysis and statistics
"""

from langdetect import detect, detect_langs, LangDetectException
from collections import Counter
import re
import pycountry
from colorama import Fore, Style


class LanguageAnalyzer:
    """Advanced language analysis with detailed statistics"""
    
    # Comprehensive language mapping (55+ languages)
    LANGUAGE_MAP = {
        'af': 'Afrikaans', 'ar': 'Arabic', 'bg': 'Bulgarian', 'bn': 'Bengali',
        'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish',
        'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish',
        'et': 'Estonian', 'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French',
        'gu': 'Gujarati', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian',
        'hu': 'Hungarian', 'id': 'Indonesian', 'it': 'Italian', 'ja': 'Japanese',
        'kn': 'Kannada', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian',
        'mk': 'Macedonian', 'ml': 'Malayalam', 'mr': 'Marathi', 'ne': 'Nepali',
        'nl': 'Dutch', 'no': 'Norwegian', 'pa': 'Punjabi', 'pl': 'Polish',
        'pt': 'Portuguese', 'ro': 'Romanian', 'ru': 'Russian', 'sk': 'Slovak',
        'sl': 'Slovenian', 'so': 'Somali', 'sq': 'Albanian', 'sv': 'Swedish',
        'sw': 'Swahili', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai',
        'tl': 'Tagalog', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
        'vi': 'Vietnamese', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)'
    }
    
    def __init__(self, text):
        self.text = text
        self.detected_lang = None
        self.probabilities = None
        self._analyze()
    
    def _analyze(self):
        """Perform initial language detection"""
        try:
            self.detected_lang = detect(self.text)
            self.probabilities = detect_langs(self.text)
        except LangDetectException:
            self.detected_lang = None
            self.probabilities = []
    
    def get_language_name(self, code=None):
        """Get full language name from code"""
        if code is None:
            code = self.detected_lang
        return self.LANGUAGE_MAP.get(code, code.upper() if code else 'Unknown')
    
    def get_country_info(self):
        """Get country information for the detected language"""
        if not self.detected_lang:
            return None
        
        try:
            # Map language codes to primary countries
            lang_to_country = {
                'en': 'US', 'es': 'ES', 'fr': 'FR', 'de': 'DE', 'it': 'IT',
                'pt': 'PT', 'ru': 'RU', 'ja': 'JP', 'zh-cn': 'CN', 'ko': 'KR',
                'ar': 'SA', 'hi': 'IN', 'nl': 'NL', 'sv': 'SE', 'pl': 'PL',
                'tr': 'TR', 'vi': 'VN', 'th': 'TH', 'id': 'ID', 'he': 'IL'
            }
            
            country_code = lang_to_country.get(self.detected_lang)
            if country_code:
                country = pycountry.countries.get(alpha_2=country_code)
                return {
                    'name': country.name,
                    'code': country.alpha_2,
                    'flag': country.flag if hasattr(country, 'flag') else ''
                }
        except:
            pass
        return None
    
    def get_text_statistics(self):
        """Get detailed text statistics"""
        stats = {
            'total_chars': len(self.text),
            'total_chars_no_spaces': len(self.text.replace(' ', '')),
            'total_words': len(self.text.split()),
            'total_sentences': len(re.split(r'[.!?]+', self.text)),
            'total_lines': len(self.text.split('\n')),
            'avg_word_length': 0,
            'unique_words': 0,
            'alphabetic_chars': sum(c.isalpha() for c in self.text),
            'numeric_chars': sum(c.isdigit() for c in self.text),
            'special_chars': sum(not c.isalnum() and not c.isspace() for c in self.text)
        }
        
        words = self.text.split()
        if words:
            stats['avg_word_length'] = sum(len(w) for w in words) / len(words)
            stats['unique_words'] = len(set(words))
        
        return stats
    
    def get_character_distribution(self):
        """Analyze character distribution"""
        chars = [c.lower() for c in self.text if c.isalpha()]
        return Counter(chars).most_common(10)
    
    def get_word_frequency(self, top_n=10):
        """Get most frequent words"""
        words = [w.lower() for w in re.findall(r'\b\w+\b', self.text)]
        return Counter(words).most_common(top_n)
    
    def detect_script_type(self):
        """Detect the writing script/alphabet used"""
        scripts = {
            'Latin': 0,
            'Cyrillic': 0,
            'Arabic': 0,
            'Chinese': 0,
            'Japanese': 0,
            'Korean': 0,
            'Devanagari': 0,
            'Greek': 0,
            'Hebrew': 0,
            'Thai': 0
        }
        
        for char in self.text:
            code = ord(char)
            if 0x0041 <= code <= 0x007A or 0x00C0 <= code <= 0x024F:
                scripts['Latin'] += 1
            elif 0x0400 <= code <= 0x04FF:
                scripts['Cyrillic'] += 1
            elif 0x0600 <= code <= 0x06FF:
                scripts['Arabic'] += 1
            elif 0x4E00 <= code <= 0x9FFF:
                scripts['Chinese'] += 1
            elif 0x3040 <= code <= 0x309F or 0x30A0 <= code <= 0x30FF:
                scripts['Japanese'] += 1
            elif 0xAC00 <= code <= 0xD7AF:
                scripts['Korean'] += 1
            elif 0x0900 <= code <= 0x097F:
                scripts['Devanagari'] += 1
            elif 0x0370 <= code <= 0x03FF:
                scripts['Greek'] += 1
            elif 0x0590 <= code <= 0x05FF:
                scripts['Hebrew'] += 1
            elif 0x0E00 <= code <= 0x0E7F:
                scripts['Thai'] += 1
        
        # Return dominant script
        dominant = max(scripts.items(), key=lambda x: x[1])
        return dominant[0] if dominant[1] > 0 else 'Unknown'
    
    def is_multilingual(self, threshold=0.15):
        """Check if text contains multiple languages"""
        if not self.probabilities or len(self.probabilities) < 2:
            return False
        
        # If second language has > threshold probability, consider multilingual
        return self.probabilities[1].prob > threshold
    
    def get_all_detected_languages(self):
        """Get all detected languages with probabilities"""
        if not self.probabilities:
            return []
        
        return [(self.get_language_name(p.lang), p.lang, p.prob * 100) 
                for p in self.probabilities]
    
    def generate_report(self):
        """Generate comprehensive analysis report"""
        if not self.detected_lang:
            return "Unable to detect language"
        
        report = []
        report.append(f"\n{Fore.CYAN}{'='*70}")
        report.append(f"{Fore.YELLOW}LANGUAGE ANALYSIS REPORT")
        report.append(f"{Fore.CYAN}{'='*70}\n")
        
        # Primary language
        lang_name = self.get_language_name()
        confidence = self.probabilities[0].prob * 100 if self.probabilities else 0
        report.append(f"{Fore.GREEN}Primary Language: {Fore.MAGENTA}{lang_name} ({self.detected_lang})")
        report.append(f"{Fore.GREEN}Confidence: {Fore.YELLOW}{confidence:.2f}%\n")
        
        # Country info
        country = self.get_country_info()
        if country:
            report.append(f"{Fore.GREEN}Primary Region: {Fore.CYAN}{country['name']} ({country['code']})\n")
        
        # Script type
        script = self.detect_script_type()
        report.append(f"{Fore.GREEN}Writing Script: {Fore.CYAN}{script}\n")
        
        # Multilingual check
        if self.is_multilingual():
            report.append(f"{Fore.YELLOW}⚠ Multilingual text detected!\n")
            report.append(f"{Fore.CYAN}All detected languages:")
            for name, code, prob in self.get_all_detected_languages()[:5]:
                report.append(f"  • {name} ({code}): {prob:.2f}%")
            report.append("")
        
        # Text statistics
        stats = self.get_text_statistics()
        report.append(f"{Fore.CYAN}{'─'*70}")
        report.append(f"{Fore.YELLOW}TEXT STATISTICS")
        report.append(f"{Fore.CYAN}{'─'*70}")
        report.append(f"{Fore.WHITE}Total Characters: {Fore.GREEN}{stats['total_chars']:,}")
        report.append(f"{Fore.WHITE}Total Words: {Fore.GREEN}{stats['total_words']:,}")
        report.append(f"{Fore.WHITE}Total Sentences: {Fore.GREEN}{stats['total_sentences']:,}")
        report.append(f"{Fore.WHITE}Unique Words: {Fore.GREEN}{stats['unique_words']:,}")
        report.append(f"{Fore.WHITE}Average Word Length: {Fore.GREEN}{stats['avg_word_length']:.2f} chars")
        report.append(f"{Fore.WHITE}Alphabetic: {Fore.GREEN}{stats['alphabetic_chars']:,} {Fore.WHITE}| "
                     f"Numeric: {Fore.GREEN}{stats['numeric_chars']:,} {Fore.WHITE}| "
                     f"Special: {Fore.GREEN}{stats['special_chars']:,}\n")
        
        # Character distribution
        char_dist = self.get_character_distribution()
        if char_dist:
            report.append(f"{Fore.CYAN}{'─'*70}")
            report.append(f"{Fore.YELLOW}TOP 10 CHARACTERS")
            report.append(f"{Fore.CYAN}{'─'*70}")
            for char, count in char_dist:
                percentage = (count / stats['alphabetic_chars']) * 100 if stats['alphabetic_chars'] > 0 else 0
                bar = '█' * int(percentage)
                report.append(f"{Fore.MAGENTA}'{char}': {Fore.GREEN}{bar} {count:,} ({percentage:.1f}%)")
            report.append("")
        
        # Word frequency
        word_freq = self.get_word_frequency()
        if word_freq:
            report.append(f"{Fore.CYAN}{'─'*70}")
            report.append(f"{Fore.YELLOW}TOP 10 WORDS")
            report.append(f"{Fore.CYAN}{'─'*70}")
            for word, count in word_freq:
                percentage = (count / stats['total_words']) * 100 if stats['total_words'] > 0 else 0
                report.append(f"{Fore.CYAN}{word:15} {Fore.GREEN}{count:,} occurrences ({percentage:.1f}%)")
            report.append("")
        
        report.append(f"{Fore.CYAN}{'='*70}\n")
        
        return '\n'.join(report)
