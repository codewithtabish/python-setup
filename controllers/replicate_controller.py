import replicate
from flask import jsonify, request
import os
from dotenv import load_dotenv
# import Replicate from "replicate";


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
        print("Yes, I am at image generation.")

        # Get the prompt from the request
        prompt = request.json.get("prompt")
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Setup input for the replication model
        input_data = {
            "prompt": prompt,
            "go_fast": True,
            "megapixels": "1",
            "num_outputs": 1,
            "aspect_ratio": "1:1",
            "output_format": "webp",
            "output_quality": 80,
            "num_inference_steps": 4
        }

        # Run the model with the given input
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input=input_data
        )
        print("Generated output:", output)

        # Extract the first URL from the output
        if isinstance(output, list) and all(isinstance(item, replicate.helpers.FileOutput) for item in output):
            image_url = output[0].url  # Extract the first URL
        else:
            raise ValueError("Unexpected output format. Unable to extract image URL.")

        # Return the URL in JSON format
        return jsonify({"url": image_url}), 200

    except Exception as e:
        print(f"Error generating image: {e}")
        return jsonify({"error": "Failed to generate image", "details": str(e)}), 500




