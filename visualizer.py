# visualizer.py
from language_analyzer import LanguageAnalyzer
import plotly.express as px

class LanguageVisualizer:
    """Visualizer for language analysis"""

    def create_comprehensive_dashboard(self, analyzer: LanguageAnalyzer):
        """
        Create a chart showing language distribution or confidence scores.
        Returns a Plotly figure.
        """
        # Use a placeholder method; adapt to your analyzer
        try:
            lang_data = analyzer.get_language_distribution()  # must return dict {language: score}
        except AttributeError:
            # Fallback if method doesn't exist: just use detected language
            lang_data = {analyzer.get_language_name(): 100}

        fig = px.pie(
            names=list(lang_data.keys()),
            values=list(lang_data.values()),
            title="Language Distribution"
        )
        return fig


# Optional: function version for app.py import
def visualize_language_distribution(analyzer: LanguageAnalyzer):
    visualizer = LanguageVisualizer()
    return visualizer.create_comprehensive_dashboard(analyzer)
