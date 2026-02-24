import fs from "node:fs";
import path from "node:path";
// import { fileURLToPath } from "node:url";
import { GoogleGenerativeAI } from "@google/generative-ai";

const imagePath =
  "/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/ai_studio/examples/images/space2.jpeg";

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
  console.error("Set GEMINI_API_KEY in your environment.");
  process.exit(1);
}

const genAI = new GoogleGenerativeAI(apiKey);
const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-image" });

const imageBytes = fs.readFileSync(imagePath);
const imageBase64 = imageBytes.toString("base64");

const response = await model.generateContent([
  {
    inlineData: {
      data: imageBase64,
      mimeType: "image/jpeg",
    },
  },
  "remove the sun (orange ball) from the photo",
]);

const parts = response.response.candidates?.[0]?.content?.parts ?? [];
const imagePart = parts.find((part) => part.inlineData?.data);
if (!imagePart) {
  console.error("No image returned by the model.");
  process.exit(1);
}

const editedBytes = Buffer.from(imagePart.inlineData.data, "base64");
const outputPath = path.join(path.dirname(imagePath), "space2_no_sun.png");
fs.writeFileSync(outputPath, editedBytes);
console.log(`Saved: ${outputPath}`);
