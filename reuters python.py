import os

# Define the path to the Reuters dataset containing extracted .sgm files
dataset_folder = r'C:\Users\PC\Downloads\Reuters News Dataset'

# Initialize lists to store articles by topic
segments = []

# Loop through files in the dataset folder to find .sgm files
for file_name in os.listdir(dataset_folder):
    if file_name.endswith(".sgm"):
        file_path = os.path.join(dataset_folder, file_name)
        
        # Read each file and extract articles
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()
            
            # Split articles by the <REUTERS> tags
            articles = content.split('</REUTERS>')
            for article in articles:
                # Extract the title and body text if present
                title_start = article.find('<TITLE>')
                title_end = article.find('</TITLE>', title_start)
                body_start = article.find('<BODY>')
                body_end = article.find('</BODY>', body_start)
                
                # Extract title and body content
                title = article[title_start + 7:title_end] if title_start != -1 and title_end != -1 else "No Title"
                body = article[body_start + 6:body_end] if body_start != -1 and body_end != -1 else ""
                
                # Add the article as a segment if it has body text
                if body:
                    segments.append(f"{title}\n{body}")
                    segments.append("===END===")  # Marker for segmentation boundary

# Join all segments and save to a single file
final_text = "\n\n".join(segments)
output_path = r'C:\Users\PC\Downloads\Reuters News Dataset\reuters_segmented_data.txt'
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write(final_text)

print(f"Preprocessing complete. Segmented file saved as '{output_path}'.")
