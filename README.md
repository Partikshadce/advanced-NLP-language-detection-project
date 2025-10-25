# 🌍 Advanced Language Detection & Analysis System

A comprehensive NLP project that detects, analyzes, and visualizes language patterns across 55+ languages with advanced statistical analysis and beautiful visualizations.

## ✨ Features

### Core Capabilities
- **55+ Language Detection**: Supports European, Asian, Cyrillic, Indic, Middle Eastern languages
- **Advanced Text Analysis**: Character distribution, word frequency, script detection
- **Multilingual Detection**: Identifies mixed-language content
- **Batch Processing**: Analyze multiple files at once
- **Data Visualization**: Generate charts and interactive graphs
- **Detailed Statistics**: Comprehensive linguistic metrics
- **Country Information**: Maps languages to their primary regions

### Analysis Features
- ✅ Language detection with confidence scores
- ✅ Text statistics (words, characters, sentences)
- ✅ Character frequency analysis
- ✅ Word frequency distribution
- ✅ Script/alphabet detection (Latin, Cyrillic, Arabic, etc.)
- ✅ Multilingual content identification
- ✅ Batch file processing with CSV reports
- ✅ Interactive and static visualizations

## 📦 Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Verify installation:**
```bash
python test_detector.py
```

## 🚀 Usage

### 1. Advanced Interactive Mode (Recommended)
```bash
python advanced_detector.py
```

**Menu Options:**
- Quick Analysis - Fast language detection
- Detailed Report - Comprehensive linguistic analysis
- With Visualizations - Generate charts and graphs
- Analyze File - Process text files
- Multi-Language Demo - Test 25 languages
- Compare Texts - Side-by-side comparison
- Language Statistics - View all supported languages

### 2. Quick Command Line
```bash
python advanced_detector.py "Your text here"
```

### 3. Multi-Language Demo
```bash
python advanced_detector.py --demo
```
Tests detection across 25 different languages with accuracy metrics.

### 4. Show Supported Languages
```bash
python advanced_detector.py --stats
```

### 5. Batch File Processing
```bash
python batch_processor.py ./sample_texts
```
Processes all text files in a directory and generates a CSV report.

### 6. Basic Detection (Original)
```bash
python language_detector.py "Text to analyze"
```

## 📊 Examples

### Example 1: Quick Analysis
```bash
python advanced_detector.py "Bonjour! Comment ça va?"
```
**Output:**
```
✓ Language: French (fr)
✓ Confidence: 99.99%
```

### Example 2: Detailed Analysis
```python
from language_analyzer import LanguageAnalyzer

text = "Natural Language Processing is fascinating!"
analyzer = LanguageAnalyzer(text)
print(analyzer.generate_report())
```

### Example 3: Batch Processing
```bash
python batch_processor.py ./sample_texts
```
**Output:** CSV report with language distribution and statistics

### Example 4: Visualization
```python
from visualizer import LanguageVisualizer
from language_analyzer import LanguageAnalyzer

text = "Your multilingual text here..."
analyzer = LanguageAnalyzer(text)
visualizer = LanguageVisualizer()
visualizer.create_comprehensive_dashboard(analyzer)
```

## 🗂️ Project Structure

```
nlp project/
├── advanced_detector.py      # Main advanced application (7 modes)
├── language_detector.py       # Original simple detector
├── language_analyzer.py       # Advanced analysis engine
├── batch_processor.py         # Batch file processing
├── visualizer.py             # Visualization module
├── test_detector.py          # Test suite
├── requirements.txt          # Dependencies
├── README.md                 # Documentation
├── sample_texts/             # Sample files for testing
│   ├── english.txt
│   ├── spanish.txt
│   ├── french.txt
│   ├── german.txt
│   ├── japanese.txt
│   └── chinese.txt
└── visualizations/           # Generated charts (auto-created)
```

## 🌐 Supported Languages (55+)

### European Languages
English, Spanish, French, German, Italian, Portuguese, Dutch, Swedish, Danish, Norwegian, Finnish, Polish, Czech, Slovak, Romanian, Hungarian, Croatian, Slovenian, Estonian, Latvian, Lithuanian

### Cyrillic Languages
Russian, Ukrainian, Bulgarian, Macedonian

### Asian Languages
Japanese, Chinese (Simplified), Chinese (Traditional), Korean, Thai, Vietnamese, Indonesian

### Indic Languages
Hindi, Bengali, Gujarati, Kannada, Malayalam, Marathi, Nepali, Punjabi, Tamil, Telugu, Urdu

### Middle Eastern Languages
Arabic, Persian, Hebrew, Turkish

### Other Languages
Afrikaans, Albanian, Catalan, Welsh, Greek, Somali, Swahili, Tagalog

## 🔧 Technical Details

### Libraries Used
- **langdetect**: Core language detection (Google's language-detection port)
- **matplotlib**: Static visualizations
- **plotly**: Interactive charts
- **pandas**: Data analysis and CSV reports
- **pycountry**: Country/region information
- **colorama**: Terminal colors
- **textblob**: Text processing utilities
- **googletrans**: Translation capabilities

### Detection Algorithm
Uses a Naive Bayesian filter with character n-grams for language identification. Achieves 95%+ accuracy on texts with 20+ words.

### Accuracy
- **Short texts (5-20 words)**: ~85% accuracy
- **Medium texts (20-100 words)**: ~95% accuracy
- **Long texts (100+ words)**: ~99% accuracy

## 📈 Output Examples

### Text Statistics
```
Total Characters: 1,234
Total Words: 234
Total Sentences: 12
Unique Words: 156
Average Word Length: 5.2 chars
```

### Visualizations Generated
- Language distribution pie charts
- Confidence score bar charts
- Character frequency histograms
- Word frequency rankings
- Multilingual probability comparisons
- Text statistics overview

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_detector.py
```

Expected output: **100% accuracy** on 10 test languages

## 💡 Use Cases

1. **Content Moderation**: Identify language of user-generated content
2. **Document Classification**: Organize multilingual document libraries
3. **Translation Routing**: Route text to appropriate translation services
4. **Language Learning**: Analyze text complexity and vocabulary
5. **Data Analysis**: Study language patterns in datasets
6. **SEO Optimization**: Detect language for proper indexing
7. **Chatbot Development**: Route queries based on language

## 🎯 Advanced Features

### Multilingual Detection
Automatically identifies when text contains multiple languages:
```
⚠ Multilingual text detected!
  • English (en): 65.3%
  • Spanish (es): 28.7%
  • French (fr): 6.0%
```

### Script Detection
Identifies the writing system used:
- Latin, Cyrillic, Arabic, Chinese, Japanese, Korean, Devanagari, Greek, Hebrew, Thai

### Batch Processing
Process entire directories and get CSV reports with:
- File name and path
- Detected language
- Word count, character count
- File size
- Language distribution summary

## 📝 Requirements

- **Python**: 3.7+
- **OS**: Windows, macOS, Linux
- **RAM**: 512MB minimum
- **Disk**: 100MB for dependencies

## 🤝 Contributing

This is an educational project. Feel free to:
- Add more languages
- Improve detection accuracy
- Create new visualizations
- Add translation features
- Enhance the UI

## 📄 License

Free to use for educational and personal purposes.

## 🎓 Learning Outcomes

This project demonstrates:
- Natural Language Processing fundamentals
- Machine learning for text classification
- Data visualization techniques
- File I/O and batch processing
- Statistical analysis
- Object-oriented programming
- Command-line interface design

## 🚀 Future Enhancements

- [ ] Real-time translation integration
- [ ] Web interface with Flask/Django
- [ ] API endpoint for language detection
- [ ] Mobile app version
- [ ] Database storage for analysis history
- [ ] Custom model training
- [ ] Sentiment analysis integration
- [ ] Named entity recognition

---

**Made with ❤️ for NLP enthusiasts**
