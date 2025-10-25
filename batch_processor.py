"""
Batch File Processor for Language Detection
Process multiple text files and generate reports
"""

import os
import sys
from pathlib import Path
from langdetect import detect, LangDetectException
from colorama import init, Fore, Style
import pandas as pd
from datetime import datetime

# Set UTF-8 encoding for Windows
if os.name == 'nt':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

init(autoreset=True)

from language_analyzer import LanguageAnalyzer


class BatchProcessor:
    """Process multiple files for language detection"""
    
    def __init__(self, directory):
        self.directory = Path(directory)
        self.results = []
    
    def process_directory(self, extensions=None):
        """Process all text files in directory"""
        if extensions is None:
            extensions = ['.txt', '.md', '.csv', '.log', '.json']
        
        print(f"{Fore.CYAN}Scanning directory: {Fore.WHITE}{self.directory}")
        print(f"{Fore.CYAN}Looking for extensions: {Fore.WHITE}{', '.join(extensions)}\n")
        
        files = []
        for ext in extensions:
            files.extend(self.directory.rglob(f'*{ext}'))
        
        if not files:
            print(f"{Fore.RED}No files found with specified extensions!")
            return
        
        print(f"{Fore.GREEN}Found {len(files)} files to process\n")
        
        for i, file_path in enumerate(files, 1):
            print(f"{Fore.YELLOW}[{i}/{len(files)}] Processing: {Fore.WHITE}{file_path.name}")
            self.process_file(file_path)
        
        self.generate_summary()
    
    def process_file(self, file_path):
        """Process a single file"""
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
                print(f"{Fore.RED}  ✗ Could not read file\n")
                return
            
            if len(text.strip()) < 10:
                print(f"{Fore.YELLOW}  ⚠ File too short, skipping\n")
                return
            
            # Detect language
            try:
                lang_code = detect(text)
                analyzer = LanguageAnalyzer(text)
                lang_name = analyzer.get_language_name(lang_code)
                stats = analyzer.get_text_statistics()
                
                result = {
                    'file': file_path.name,
                    'path': str(file_path),
                    'language': lang_name,
                    'code': lang_code,
                    'size_bytes': file_path.stat().st_size,
                    'chars': stats['total_chars'],
                    'words': stats['total_words'],
                    'sentences': stats['total_sentences']
                }
                
                self.results.append(result)
                print(f"{Fore.GREEN}  ✓ Detected: {Fore.MAGENTA}{lang_name} {Fore.CYAN}({stats['total_words']:,} words)\n")
                
            except LangDetectException:
                print(f"{Fore.RED}  ✗ Could not detect language\n")
                
        except Exception as e:
            print(f"{Fore.RED}  ✗ Error: {str(e)}\n")
    
    def generate_summary(self):
        """Generate summary report"""
        if not self.results:
            print(f"{Fore.RED}No results to summarize!")
            return
        
        df = pd.DataFrame(self.results)
        
        print(f"\n{Fore.MAGENTA}{'='*80}")
        print(f"{Fore.YELLOW}BATCH PROCESSING SUMMARY")
        print(f"{Fore.MAGENTA}{'='*80}\n")
        
        # Language distribution
        lang_counts = df['language'].value_counts()
        print(f"{Fore.CYAN}Language Distribution:")
        for lang, count in lang_counts.items():
            percentage = (count / len(df)) * 100
            bar = '█' * int(percentage / 2)
            print(f"{Fore.WHITE}{lang:20} {Fore.GREEN}{bar} {count} files ({percentage:.1f}%)")
        
        print(f"\n{Fore.CYAN}Statistics:")
        print(f"{Fore.WHITE}Total Files Processed: {Fore.GREEN}{len(df):,}")
        print(f"{Fore.WHITE}Total Words: {Fore.GREEN}{df['words'].sum():,}")
        print(f"{Fore.WHITE}Total Characters: {Fore.GREEN}{df['chars'].sum():,}")
        print(f"{Fore.WHITE}Total Size: {Fore.GREEN}{df['size_bytes'].sum():,} bytes")
        
        # Save to CSV
        output_file = f"language_detection_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(output_file, index=False)
        print(f"\n{Fore.GREEN}✓ Report saved to: {Fore.WHITE}{output_file}")
        print(f"{Fore.MAGENTA}{'='*80}\n")


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print(f"{Fore.YELLOW}Usage: python batch_processor.py <directory_path>")
        print(f"{Fore.CYAN}Example: python batch_processor.py ./sample_texts")
        return
    
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print(f"{Fore.RED}Error: Directory '{directory}' does not exist!")
        return
    
    processor = BatchProcessor(directory)
    processor.process_directory()


if __name__ == "__main__":
    main()
