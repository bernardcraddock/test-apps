# Remove Sun From Photo (JavaScript)

## How it works
- Reads your image at `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/images/space2.jpeg`
- Sends the image + prompt to the `gemini-2.5-flash-image` model
- Extracts the returned image bytes and saves `space2_no_sun.png` in the same folder

## Run steps
1) `npm install @google/generative-ai`
2) `export GEMINI_API_KEY="your_key_here"`
3) Run ES module version:
   - `node /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/js/remove_sun.js`
4) Run CommonJS version:
   - `node /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/js/common_remove_sun.js`

## How it's built (from the AI Studio JSON)
1) Read the export and locate `runSettings.model` to choose the model (`gemini-2.5-flash-image`).
2) Check `responseModalities` to request an image output (`IMAGE`, `TEXT`).
3) Find the user prompt text chunk: "remove the sun (orange ball) from the photo".
4) Identify the image input chunk (`sampleImageId: space2`) and replace it with your real image bytes.
5) Use the SDK to send two parts: the image bytes (inline data) and the text prompt.
6) Inspect the response for the first image part and decode it from base64.
7) Write the decoded bytes to a PNG file.

## Notes
- Update the image path in both scripts if your file location changes.
- If you see a module error when running `remove_sun.js`, either add `"type": "module"` to your `package.json` or use the CommonJS script.

## Troubleshooting
- `Cannot find module '@google/generative-ai'`: Run `npm install @google/generative-ai` in the folder where you run the script.
- `Set GEMINI_API_KEY in your environment.`: Export the key in the same terminal session before running the script.
- `No image returned by the model.`: Check that your input image path is correct and the file is a valid JPEG/PNG.
- `SyntaxError: Cannot use import statement outside a module`: Use the CommonJS script or add `"type": "module"` to `package.json`.
- Permission errors reading the image: Confirm the file exists and you have read access to the path.
