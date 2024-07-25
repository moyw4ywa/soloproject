import csv
import pandas as pd
import os

# Data for social media tips
data = {
    "tip_id": [1, 2, 3, 4, 5],
    "tip_category": ["Engagement", "Content Strategy", "Interaction", "Analytics", "Branding"],
    "tip_text": [
        "Use high-quality images to attract more likes and comments.",
        "Post consistently at peak times when your audience is most active.",
        "Respond to comments and messages promptly to build a loyal following.",
        "Use social media analytics tools to track performance and adjust your strategy.",
        "Maintain a consistent brand voice across all your social media platforms."
    ],
    "hashtags": ["#SocialMediaTips #Engagement", "#ContentStrategy #SocialMedia", "#Engagement #SocialMedia #CustomerService", "#Analytics #SocialMedia #Marketing", "#Branding #SocialMedia #Marketing"],
    "keywords": ["high-quality images", "consistency", "responding to comments", "analytics tools", "brand voice"],
    "sentiment": ["informational", "informational", "informational", "informational", "motivational"],
    "audience": ["general", "content creators", "brands", "marketers", "brands"]
}

# File path for content data
file_path = 'content_data.csv'

# Create a DataFrame
df = pd.DataFrame(data)

def create_csv_if_not_exists():
    if not os.path.exists(file_path):
        # Save the DataFrame to CSV
        df.to_csv(file_path, index=False, quoting=csv.QUOTE_MINIMAL)
        print(f"'{file_path}' has been created successfully.")
    else:
        print(f"'{file_path}' already exists.")

if __name__ == "__main__":
    create_csv_if_not_exists()
