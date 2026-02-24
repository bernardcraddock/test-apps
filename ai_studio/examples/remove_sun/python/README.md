# Remove Sun From Photo (Gemini Image Edit)

## How it works
- Reads your image at `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/images/space2.jpeg`
- Calls `gemini-2.5-flash-image` with the prompt "remove the sun (orange ball) from the photo"
- Writes the edited image as `space2_no_sun.png` in the same folder

## Run steps
1) `pip install google-genai`
2) `export GEMINI_API_KEY="your_key_here"`
3) `python /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/python/remove_sun.py`

## Notes
- Update the image path in `remove_sun.py` if your file location changes.
