# GEMINI.md - Google Technologies & Experimental Projects Guide

This file provides guidance to Google Gemini AI when working with the pumped-scripts repository, with special focus on Google ecosystem projects.

## Project Overview

**pumped-scripts** is a multi-platform experimental sandbox exploring:
- **Google AI & Cloud Services**: Google AI Studio, Cloud integrations
- **Cross-Platform Development**: Flutter/Dart, Android Studio, Angular
- **Emerging Technologies**: XR/AR experiments (Google Glass interest), AR navigation
- **Architecture & Learning**: Documentation-driven development, proof-of-concepts
- **Data Processing**: PDF extraction, image processing, diagram generation with Mermaid

**Primary workspace**: `/test-apps` - All experimental learning projects.

## Quick Start

### Google AI Studio Projects
```bash
cd test-apps
source .venv/bin/activate  # Python env for AI work

# Google Generative AI SDK (Python)
pip install google-generativeai

# Run an AI Studio experiment
python3 ai_studio/your_script.py
```

### Flutter/Dart Projects
```bash
cd test-apps/dart/
flutter pub get        # Install dependencies
flutter run -d chrome  # Web development
flutter build apk      # Android build
```

### Android Studio Projects
```bash
cd test-apps/android/
# Open in Android Studio or build via command line
./gradlew build
./gradlew assembleDebug
```

### JavaScript (including Google Cloud integrations)
```bash
cd test-apps/js/
npm install
npm run build
```

### Python (for Google AI integrations)
```bash
cd test-apps
source .venv/bin/activate
pip install google-generativeai google-cloud-vertexai
python3 script.py
```

## Repository Structure

```
pumped-scripts/
├── .github/
│   ├── copilot-instructions.md  ← Master AI instructions
│   └── workflows/               ← CI/CD and test automation
├── test-apps/                   ← EXPERIMENTAL PROJECTS
│   ├── ai_studio/               ← Google AI Studio experiments ⭐
│   ├── python/                  ← Python + Google AI APIs
│   ├── dart/                     ← Dart/Flutter development ⭐
│   ├── android/                  ← Android Studio projects ⭐
│   ├── js/                       ← JavaScript/TypeScript projects
│   ├── mcp/                      ← Model Context Protocol experiments
│   ├── clang/                    ← C/Objective-C/Swift (iOS/AR)
│   ├── AntiGravity/              ← Experimental AR/XR
│   ├── bash/                     ← Shell utilities
│   └── [others]
├── frontend/                    ← Flutter production app
├── backend/                     ← Java/Kotlin backend
└── soafee/                      ← Architecture documentation
```

## Google Technologies Focus Areas

### 1. Google AI Studio & Gemini API

**Setup:**
```bash
# Get free API key from: https://aistudio.google.com/apikey
export GOOGLE_API_KEY="your-api-key-here"

# Install SDK
pip install google-generativeai

# Python example
from google.generativeai import GenerativeModel

model = GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Your prompt here")
print(response.text)
```

**Project Location**: `/test-apps/ai_studio/`
- Document what experiments you're running
- Include example prompts and outputs
- Note API rate limits and quotas
- Create `ai_studio_README.md` with setup instructions

### 2. Flutter & Dart Development

**Environment Setup:**
```bash
# Install Flutter (if not already installed)
# Download from: https://flutter.dev/docs/get-started/install

# Create new Flutter project
cd test-apps
flutter create --org com.example my_flutter_app

# For web development
flutter run -d chrome

# For Android development (requires Android Studio)
flutter run -d emulator-id  # or physical device

# Build APK for Android
flutter build apk
```

**Key Locations**:
- `/test-apps/dart/` - Dart language experiments
- `/test-apps/android/` - Android-specific projects
- `/frontend/` - Production Flutter app

**Important**: Flutter combines Dart code with native Android/iOS integration. For XR/Glass development, explore:
- Google Glass SDK integration with Flutter
- AR Core for Android devices
- Navigation and spatial computing APIs

### 3. Android Studio & Native Development

**Build Configuration**:
```bash
cd test-apps/android/

# Build with Gradle
./gradlew build
./gradlew assembleDebug      # Debug APK
./gradlew assembleRelease    # Release build

# Run on emulator
emulator -avd Pixel_4        # Start emulator
adb install build/outputs/apk/debug/app-debug.apk
```

**XR Glass Considerations:**
- Explore Google Glass Enterprise SDK
- Navigation APIs for heads-up display
- Voice command integration
- Camera/sensor access patterns

### 4. Google Cloud Integration

**Available Python SDKs:**
```bash
pip install google-cloud-vertexai      # Vertex AI
pip install google-cloud-storage       # Cloud Storage
pip install google-cloud-functions     # Cloud Functions
pip install google-cloud-vision        # Vision API
```

**Common Pattern:**
```python
from google.cloud import vision
from google.cloud import storage

# Use Google Cloud services in your experiments
# Document API setup and authentication
```

## Development Conventions

### Documentation Standards

Each project needs:

**Format**: `<folder>_README.md` (e.g., `ai_studio/ai_studio_README.md`)

**Content**:
- What the project explores
- Technology versions (Flutter version, Dart SDK, Android API level)
- Setup instructions (API keys, credentials, environment variables)
- Quick-start examples
- Known limitations or experiments in progress
- Links to relevant Google docs/APIs

### Testing & Validation

**Smoke Tests** (< 15 seconds, must print `SMOKE: OK`):
```bash
# Flutter example
bash dart/smoke-test.sh        # Quick build check

# Android example
bash android/smoke-test.sh     # Quick compile check

# Python/AI example
bash ai_studio/smoke-test.sh   # Quick API check
```

**Automated Tests**:
```bash
# Flutter testing
flutter test

# Android testing
./gradlew test

# Python testing
pytest -q test-apps/python -k quick
```

### Python Virtual Environment

All Python work uses:
```bash
cd test-apps
source .venv/bin/activate
# or: .venv\Scripts\activate  (Windows)
```

**For Google AI work specifically:**
```bash
pip install google-generativeai

# Export API key
export GOOGLE_API_KEY="your-key"

# Run your script
python3 ai_studio/experiment.py
```

## Architecture & Learning Focus

### Experimental Process

1. **Start in `/test-apps/<new-folder>/`**
   - Create proof-of-concept
   - Document what you're exploring

2. **Iterative Documentation**
   - Record approaches tried
   - Note what worked and what didn't
   - Include lessons learned in `<folder>_README.md`

3. **Testing**
   - Create smoke-test for quick validation
   - Add unit tests as needed
   - Ensure CI/CD compliance

4. **Extraction** (if successful)
   - Can eventually move to production (`backend/` or `frontend/`)
   - Or archive in running-notes

### Cross-Platform Considerations

- **Flutter**: Targets Android, iOS, Web, macOS, Windows, Linux
- **Android**: API level compatibility (target modern APIs)
- **Dart**: Version consistency with Flutter
- **Python**: 3.11+ across Windows/macOS/Linux

## Technology Stack Reference

### Google Products
- **Google AI Studio**: https://aistudio.google.com (free tier)
- **Gemini API**: Text, multimodal, reasoning models
- **Vertex AI**: Enterprise ML platform
- **Google Cloud**: Storage, Functions, Vision, Speech APIs
- **Google Glass Enterprise**: https://www.x.company/glass/ (XR focus)
- **ARCore**: Android AR capabilities
- **Flutter**: Cross-platform UI framework
- **Dart**: Programming language (Flutter's language)
- **Android Studio**: IDE for Android development

### Integration Examples
```python
# Google AI + Python
import anthropic  # or google.generativeai for Gemini

# Flutter + Google APIs
import 'package:google_generative_ai/google_generative_ai.dart';

# Android + Google services
implementation "com.google.android.gms:play-services-maps:latest"
```

## Working with Google XR/Glass

**Project Location**: `/test-apps/AntiGravity/` or new XR-specific folder

**Key Considerations**:
- Heads-up display (HUD) paradigms
- Voice command integration
- Limited battery life → optimize for efficiency
- Sensor APIs (camera, GPS, gyroscope, accelerometer)
- Navigation without blocking vision
- Privacy considerations (always-on camera)

**Example Exploration**:
```dart
// Flutter XR experiment
import 'package:ar_flutter_plugin/ar_flutter_plugin.dart';

// Document AR integration patterns
// Explore spatial navigation
// Test on physical device or emulator
```

## Common Issues & Solutions

### Google API Keys

**Problem**: "API key not found" or 403 errors
```bash
# Solution: Set environment variable
export GOOGLE_API_KEY="your-actual-key"
python3 script.py
```

### Flutter/Dart Issues
```bash
# Clear cache
flutter clean
rm -rf pubspec.lock
flutter pub get

# Check environment
flutter doctor  # Run this first to diagnose issues

# Common: Android SDK not found
# Solution: Configure Android Studio paths in `flutter config`
```

### Android Build Issues
```bash
# Update Gradle
./gradlew wrapper --gradle-version=latest

# Clear Android build cache
./gradlew clean

# Check API level compatibility
# Update build.gradle to target latest Android API level
```

### Python Virtual Environment
```bash
# If .venv is corrupted
rm -rf test-apps/.venv
python3 -m venv test-apps/.venv
source test-apps/.venv/bin/activate
pip install -r requirements.txt
```

## Safety & Best Practices

### API Security
- Never commit API keys to git
- Use environment variables: `export GOOGLE_API_KEY="..."`
- Use `.gitignore` for `.env` files
- Rotate keys regularly

### File Inspection
```bash
# Always check file type first
file ./path/to/file

# Safe viewing
less ./script.py
hexdump -C ./data.bin | head
```

### Testing Before Commit
```bash
# Run smoke test
bash test-apps/<folder>/smoke-test.sh

# Run unit tests (if applicable)
pytest test-apps -k quick
flutter test
./gradlew test
```

## Resources & Learning

### Google Documentation
- [Google AI Studio](https://aistudio.google.com)
- [Gemini API Docs](https://ai.google.dev)
- [Flutter Documentation](https://flutter.dev/docs)
- [Android Developer Guide](https://developer.android.com/docs)
- [Google Glass Enterprise](https://www.x.company/glass/)
- [ARCore Overview](https://developers.google.com/ar)

### Example Projects in Repo
Check `/test-apps/` for:
- `ai_studio/` - Gemini API experiments
- `dart/` - Flutter/Dart samples
- `android/` - Android SDK examples
- `python/` - Python + Google Cloud integrations

### Running Notes
- `/running-notes/` - Experimentation logs
- Architecture diagrams and learning progress

## Next Steps for Your Exploration

1. **Google AI Studio**: Start with free API → Build conversational agents
2. **Flutter/Dart**: Explore cross-platform UI → Consider AR capabilities
3. **Android Studio**: Deep dive into native Android → Prepare for Glass/XR
4. **Integration**: Combine Flutter + Gemini API for AI-powered mobile apps
5. **XR Focus**: Explore Google Glass SDK → AR navigation prototypes

Each experiment should have clear documentation of what you learned!
