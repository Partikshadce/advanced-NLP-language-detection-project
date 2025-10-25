"""
Language Detection Visualization Module
Create charts and graphs for language analysis
"""

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from collections import Counter
import os
import sys

# Set UTF-8 encoding for Windows
if os.name == 'nt':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class LanguageVisualizer:
    """Create visualizations for language detection results"""
    
    def __init__(self, output_dir='visualizations'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def plot_language_distribution(self, languages, title="Language Distribution"):
        """Create pie chart of language distribution"""
        lang_counts = Counter(languages)
        
        # Matplotlib version
        fig, ax = plt.subplots(figsize=(10, 8))
        colors = plt.cm.Set3(range(len(lang_counts)))
        
        wedges, texts, autotexts = ax.pie(
            lang_counts.values(),
            labels=lang_counts.keys(),
            autopct='%1.1f%%',
            colors=colors,
            startangle=90
        )
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title(title, fontsize=16, fontweight='bold')
        
        output_file = os.path.join(self.output_dir, 'language_distribution.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {output_file}")
        
        # Plotly interactive version
        fig = go.Figure(data=[go.Pie(
            labels=list(lang_counts.keys()),
            values=list(lang_counts.values()),
            hole=0.3
        )])
        
        fig.update_layout(
            title=title,
            font=dict(size=14)
        )
        
        output_file_html = os.path.join(self.output_dir, 'language_distribution.html')
        fig.write_html(output_file_html)
        print(f"✓ Saved: {output_file_html}")
    
    def plot_confidence_scores(self, languages, confidences):
        """Create bar chart of confidence scores"""
        fig, ax = plt.subplots(figsize=(12, 6))
        
        colors = ['#2ecc71' if c > 90 else '#f39c12' if c > 70 else '#e74c3c' 
                  for c in confidences]
        
        bars = ax.bar(languages, confidences, color=colors, edgecolor='black', linewidth=1.5)
        
        ax.set_xlabel('Language', fontsize=12, fontweight='bold')
        ax.set_ylabel('Confidence (%)', fontsize=12, fontweight='bold')
        ax.set_title('Language Detection Confidence Scores', fontsize=16, fontweight='bold')
        ax.set_ylim(0, 100)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%',
                   ha='center', va='bottom', fontweight='bold')
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        output_file = os.path.join(self.output_dir, 'confidence_scores.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {output_file}")
    
    def plot_character_distribution(self, char_counts, title="Character Frequency"):
        """Create bar chart of character distribution"""
        chars, counts = zip(*char_counts)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        
        bars = ax.bar(chars, counts, color='#3498db', edgecolor='black', linewidth=1.5)
        
        ax.set_xlabel('Character', fontsize=12, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        
        output_file = os.path.join(self.output_dir, 'character_distribution.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {output_file}")
    
    def plot_word_cloud_data(self, word_freq, title="Top Words"):
        """Create horizontal bar chart of word frequency"""
        words, counts = zip(*word_freq)
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        y_pos = range(len(words))
        colors = plt.cm.viridis([(i / len(words)) for i in range(len(words))])
        
        bars = ax.barh(y_pos, counts, color=colors, edgecolor='black', linewidth=1.5)
        
        ax.set_yticks(y_pos)
        ax.set_yticklabels(words)
        ax.invert_yaxis()
        ax.set_xlabel('Frequency', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        # Add value labels
        for i, (bar, count) in enumerate(zip(bars, counts)):
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                   f' {count}',
                   ha='left', va='center', fontweight='bold')
        
        plt.tight_layout()
        
        output_file = os.path.join(self.output_dir, 'word_frequency.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {output_file}")
    
    def plot_multilingual_comparison(self, lang_probs):
        """Create comparison chart for multilingual detection"""
        languages = [lang for lang, _, _ in lang_probs]
        probabilities = [prob for _, _, prob in lang_probs]
        
        # Interactive plotly chart
        fig = go.Figure(data=[
            go.Bar(
                x=languages,
                y=probabilities,
                marker=dict(
                    color=probabilities,
                    colorscale='Viridis',
                    showscale=True,
                    colorbar=dict(title="Probability %")
                ),
                text=[f'{p:.1f}%' for p in probabilities],
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title='Multilingual Detection Probabilities',
            xaxis_title='Language',
            yaxis_title='Probability (%)',
            yaxis=dict(range=[0, 100]),
            font=dict(size=14),
            showlegend=False
        )
        
        output_file = os.path.join(self.output_dir, 'multilingual_comparison.html')
        fig.write_html(output_file)
        print(f"✓ Saved: {output_file}")
    
    def create_comprehensive_dashboard(self, analyzer):
        """Create a comprehensive dashboard with multiple visualizations"""
        print(f"\n🎨 Generating visualizations...")
        
        # Get data from analyzer
        stats = analyzer.get_text_statistics()
        char_dist = analyzer.get_character_distribution()
        word_freq = analyzer.get_word_frequency(15)
        lang_probs = analyzer.get_all_detected_languages()
        
        # Create visualizations
        if char_dist:
            self.plot_character_distribution(char_dist)
        
        if word_freq:
            self.plot_word_cloud_data(word_freq)
        
        if len(lang_probs) > 1:
            self.plot_multilingual_comparison(lang_probs)
        
        # Create summary statistics chart
        self._plot_text_statistics(stats)
        
        print(f"\n✓ All visualizations saved to '{self.output_dir}/' directory")
    
    def _plot_text_statistics(self, stats):
        """Create visualization of text statistics"""
        categories = ['Characters', 'Words', 'Sentences', 'Unique Words']
        values = [
            stats['total_chars'],
            stats['total_words'],
            stats['total_sentences'],
            stats['unique_words']
        ]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
        bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=2)
        
        ax.set_ylabel('Count', fontsize=12, fontweight='bold')
        ax.set_title('Text Statistics Overview', fontsize=16, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height):,}',
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        plt.tight_layout()
        
        output_file = os.path.join(self.output_dir, 'text_statistics.png')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved: {output_file}")


def demo():
    """Demo visualization capabilities"""
    visualizer = LanguageVisualizer()
    
    # Sample data
    languages = ['English', 'Spanish', 'French', 'German', 'English', 'Spanish', 'English']
    confidences = [95.5, 88.3, 92.1, 87.9, 98.2, 91.5, 96.8]
    
    visualizer.plot_language_distribution(languages)
    visualizer.plot_confidence_scores(list(set(languages)), [95.5, 88.3, 92.1, 87.9])
    
    print("\n✓ Demo visualizations created!")


if __name__ == "__main__":
    demo()
