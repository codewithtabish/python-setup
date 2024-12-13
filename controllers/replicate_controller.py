import replicate
from flask import jsonify, request
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_video():
    try:
        # Get the prompt from the request
        prompt = request.json.get("prompt")
        
        # Setup input for the replication model
        input_data = {
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "negative_prompt": "low quality, worst quality, deformed, distorted, watermark",
        }

        # Run the model with the given input
        output = replicate.run(
            "fofr/ltx-video:983ec70a06fd872ef4c29bb6b728556fc2454125a5b2c68ab51eb8a2a9eaa46a",
            input=input_data
        )
        print("Generated video URLs:", output)

        # Extract URLs from the output
        output_urls = [item.url for item in output]

        return jsonify({"data": output_urls})

    except Exception as e:
        print(f"Error generating video: {e}")
        return jsonify({"error": "Failed to generate video"}), 500



def create_image():
    try:
        print("Yes I am at imeg")
           # Get the prompt from the request
        prompt = request.json.get("prompt")
        
        # Setup input for the replication model
        input_data = {
            "prompt": prompt,
            
        }

        # Run the model with the given input
        output = replicate.run(
            
            "ideogram-ai/ideogram-v2",
            input=input_data
        )
        print("Generated image URL:", output)
        # Extract URL or path from the FileOutput object
        if hasattr(output, "url"):
            image_url = output.url
        else:
            raise ValueError("Unexpected output format. Unable to extract image URL.")

        return jsonify({"data": image_url})


    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({"error": "Failed to generate image"}), 500