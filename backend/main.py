# FastAPI dependencies
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Gemini SDK dependencies
from google import genai
from google.genai import types

# System Dependencies
from dotenv import load_dotenv
import os

# Data parsing
from pydantic import BaseModel
from typing import List, Optional
import json

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

GEMINI_MODEL = 'gemini-2.5-flash'

genai_client = genai.Client(api_key=GEMINI_API_KEY)

# Initialize FastAPI app
app = FastAPI(title="Travel Companion API")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LocationRequest(BaseModel):
    location: str
    preferences: Optional[List[str]] = []

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"message": "Travel Companion API is running"}


@app.post("/api/suggest-by-location")
async def suggest_by_location(request: LocationRequest):
    """
    Generate travel suggestions based on a location
    Takes into account user preferences
    """
    try:
         
         # Build the prompt with preferences
        preferences_text = ""
        if request.preferences:
            preferences_text = f"\nUser preferences: {', '.join(request.preferences)}"

        prompt = f"""You are a travel expert. Generate 5 travel destination suggestions near or related to {request.location}.
        {preferences_text}

        For each destination, provide:
        1. Name of the destination
        2. Brief description (2-3 sentences)
        3. Best time to visit
        4. Main attractions (list 3)
        5. Estimated budget level (Budget/Moderate/Luxury)

        Format your response as a JSON array with this structure:
        [
        {{
            "name": "Destination Name",
            "description": "Brief description",
            "best_time": "Best time to visit",
            "attractions": ["Attraction 1", "Attraction 2", "Attraction 3"],
            "budget_level": "Budget/Moderate/Luxury"
        }}
        ]

        Only return the JSON array, no additional text."""

        # Generate content using Gemini
        response = genai_client.models.generate_content(
            model=GEMINI_MODEL, 
            contents = prompt
        )
        
        # Parse the response
        response_text = response.text.strip()

        # Clean up markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        response_text = response_text.strip()

        # Parse JSON
        destinations = json.loads(response_text)
                
        return {"destinations": destinations}

    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating suggestions: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)