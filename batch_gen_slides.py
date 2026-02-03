
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "Skill/pptx/scripts"))
import nano_banana
import time

prompts = [
    ("slide1_cover", "A futuristic detailed digital analytic eye or lens focusing on a global map of trade show convention centers, dark high-tech background, neon blue and purple accents, illustrating business intelligence and global markets, cinematic lighting, 8k resolution, 16:9 aspect ratio"),
    ("slide2_market", "A futuristic 3D bar chart growing rapidly upwards, glowing green bars against a dark background, representing financial market growth, digital economy style, data visualization, 16:9"),
    ("slide3_problem", "A glowing mysterious black box with question marks floating around it, placed in the center of a busy chaotic trade show floor, representing unknown ROI and confusion, cyberpunk style, dark atmosphere, 16:9"),
    ("slide4_quality", "A crowd of business people at a trade show booth, but instead of talking they are greedily grabbing free gifts and candy, chaotic scene, satirical digital art style, 16:9"),
    ("slide5_churn", "A split screen comparison: on the left a leaking bucket losing water rapidly representing trade show exhibitors, on the right a solid secure bucket representing SaaS, 3d render, infographic style, 16:9"),
    ("slide6_valuechain", "A complex isometric machinery illustration showing a money making machine, where trade show organizers and contractors are turning gears to extract coins from exhibitors, industrial value chain concept, 16:9"),
    ("slide7_regions", "A stylized world map highlighting North America, Europe, China, and the Middle East with distinct glowing icon landmarks for each region, connected by digital network lines, 16:9"),
    ("slide8_strategy", "A high-tech digital dashboard displaying predictive analytics, identifying a single golden target among thousands of grey targets, representing business intelligence, precision targeting, sleek UI design, 16:9"),
    ("slide9_value", "A futuristic command center screen showing automated alerts and insights for a trade show event, dark UI mode, professional software interface, 16:9"),
    ("slide10_conclusion", "A sniper scope view focusing perfectly on a handshake deal in a crowd, symbolizing precision targeting in business, digital overlay with data metrics, professional and sharp, 16:9")
]

output_dir = "workspace/lensmor_presentation_v2/images"

for name, prompt in prompts:
    print(f"Generating {name}...")
    # nano_banana.generate_image(prompt, output_dir)
    # The script saves as image_TIMESTAMP_INDEX.png. We might want to rename it after generation to keep order if we want, 
    # but images2pptx sorts by filename. 
    # Let's modify generate_image to return the filename or we just rely on timestamps being sequential.
    # OR, we can just pass a specific output filename if we hack the function, but simpler to just run it and let timestamps order them.
    # To ensure order, we sleep 1 sec between calls so timestamps differ.
    
    nano_banana.generate_image(prompt, output_dir)
    time.sleep(2) 

print("Batch generation complete.")
