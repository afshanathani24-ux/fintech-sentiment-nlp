import matplotlib.pyplot as plt

# Data representing the Sentiment Audit findings
categories = ['AI Risk Scoring', 'Instant Payments', 'Biometric Privacy', 'Invisible Checkout']
# Polarity scores: Positive for efficiency, Negative for privacy concerns
sentiment_scores = [0.75, 0.15, -0.42, -0.38] 

# Apply conditional colors: Green for positive, Gray for neutral, Red for negative
colors = ['#2ecc71' if x > 0.5 else '#95a5a6' if x >= 0 else '#e74c3c' for x in sentiment_scores]

plt.figure(figsize=(10, 6))
plt.bar(categories, sentiment_scores, color=colors)

# Professional Formatting
plt.axhline(0, color='black', linewidth=0.8) # Baseline at zero
plt.ylim(-1, 1) # Full range of TextBlob polarity
plt.title('2026 FinTech Infrastructure: Sentiment Polarity Audit', fontsize=14, fontweight='bold')
plt.ylabel('Sentiment Score (TextBlob Polarity)', fontsize=12)
plt.xlabel('Infrastructure Category', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# CRITICAL: This line creates the image file in your GitHub folder
plt.savefig('sentiment_audit_chart.png', dpi=300, bbox_inches='tight')

# Display the chart locally
plt.show()
