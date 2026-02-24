# Scaffolding Diagram Project - Process Documentation

## Overview
This document details all steps taken to extract architectural plan data and attempt to create a scaffolding overlay diagram for 12 Mirrabooka Crescent, Little Bay.

**Final Result:** `scaffolding_overlay_v1.png` (deemed "hideous" - approach unsuccessful)

---

## Environment Setup

### Python Virtual Environment
- **Location:** `/Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps/.venv`
- **Activation:** `source .venv/bin/activate`
- **Python:** 3.14

---

## Phase 1: PDF Text Extraction Attempts

### Objective
Extract text and dimensions from the multi-page architectural PDF to understand building specifications.

### Tools Attempted

#### 1. pdfplumber (FAILED)
- **Installation:** `pip install pdfplumber`
- **Script:** `extract_elevations.py`
- **Issue:** PDF had embedded fonts that couldn't be decoded; output was garbled (e.g., "(cid:114) (cid:114) (cid:105)")
- **Lesson:** PDF text extraction approach didn't work for this file format
- **Status:** ❌ Removed

#### 2. pdf2image + Pillow (SUCCESSFUL - Partial)
- **Installation:** `pip install pdf2image Pillow`
- **System dependency:** `brew install poppler`
- **Script:** `pdf_to_images.py`
- **Result:** Successfully extracted page 1 (single page PDF) as PNG image (`extracted_images/page_1.png`)
- **Status:** ✅ Used for visual reference

### Alternative: Copilot in Edge
- **Approach:** Uploaded PDF to Copilot Chat in Microsoft Edge
- **Result:** Automatically extracted and structured all information (no tool usage visible to user)
- **Outcome:** Produced comprehensive markdown file with all architectural data
- **File Created:** `Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay_p7_land.md`

---

## Phase 2: Manual Data Extraction

### Objective
Since automated text extraction failed, manually analyze architectural section image and structure findings.

### Process
1. **Viewed** `extracted_images/page_1.png` (extracted via pdf2image)
2. **Analyzed** both Section A-A and Section B-B drawings
3. **Extracted** all visible dimensions, levels, rooms, and structural elements
4. **Documented** in structured markdown format

### Output
**File Created:** `building_dimensions_extracted.md`

**Key Data Captured:**
- Ridge Level (RL): 34.445
- Maximum height limit: 9.5m (from ridge to ground)
- Floor levels: Upper FL 29.650, Ground FL 26.910, Lower FL 24.650
- Site slope: ~2.2m vertical drop (north to south)
- Building length: ~33.5m
- Building width: ~12-14m
- Roof pitch: ~20-25°
- Room layout, structural elements, external works, pool dimensions

---

## Phase 3: Python Libraries Installed

| Library | Version | Purpose | Installed By |
|---------|---------|---------|--------------|
| pdfplumber | Latest | PDF text extraction (failed) | pip install |
| pdf2image | Latest | PDF to image conversion (success) | pip install |
| Pillow | Latest | Image processing | pip install (dependency) |
| matplotlib | Latest | Plotting & visualization | pip install (previous) |
| numpy | Latest | Numerical operations | Already in venv |

**Total Libraries Installed This Session:**
- pdfplumber (later removed from use)
- pdf2image ✓
- Pillow ✓
- matplotlib ✓
- numpy (existing)

---

## Phase 4: Scaffolding Overlay Attempt

### Objective
Create a scaffolding diagram overlay on top of the architectural section image.

### Approach
**Script:** `create_scaffolding_overlay.py`

**Logic:**
1. Load `extracted_images/page_1.png` as background
2. Calculate scaling factors: pixels per meter (horizontal & vertical)
3. Draw scaffolding framework:
   - **Vertical tubes:** Spaced every 2 meters (red dashed lines)
   - **Horizontal platforms:** Spaced every 2 meters (red dashed lines)
   - **Diagonal bracing:** X-pattern for stability (red dotted lines)
4. Add dimension annotations:
   - Height: 9.6m (RL 34.445)
   - Length: 33.5m
5. Add legend and title
6. Save as `scaffolding_overlay_v1.png`

### Output
**File Created:** `scaffolding_overlay_v1.png` (2339 × 1654 pixels)

**Result:** ❌ "Hideous" - Overlay does not effectively visualize scaffolding requirements

**Issues:**
- Too much visual clutter
- Scaffolding framework not clearly readable against complex architectural drawing
- Scaling and positioning not intuitive
- Tube spacing and platform heights not appropriate for actual scaffolding needs
- Lacks clarity for practical scaffolder quotes

---

## Files Created During Process

### Kept
- `Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay_p7_land.md` - Copilot Edge extraction
- `Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay_p7_land.pdf` - Single page source
- `building_dimensions_extracted.md` - Manual extraction from section image
- `pdf_to_images.py` - PDF to PNG converter (may reuse)
- `extracted_images/page_1.png` - Architectural section image
- `scaffolding_overlay_v1.png` - Failed overlay attempt (for reference)
- `Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay.pdf` - Full original PDF

### Removed
- `extract_elevations.py` - Failed pdfplumber approach
- `generate_scaffolding.py` - Standalone diagram generator (v1)
- `scaffolding_diagram_v1.png` - Standalone diagram (v1)
- `create_scaffolding_overlay.py` - Failed overlay script
- `._Architectural_Plans_12_Mirrabooka_Crescent_Little_Bay_p7_land.pdf` - macOS metadata

---

## Key Learnings

1. **PDF extraction varies by format** - Embedded font PDFs don't work with pdfplumber
2. **Image extraction works well** - pdf2image + Poppler successfully extracted visual content
3. **Manual analysis effective** - Visual inspection + structured documentation captured all needed data
4. **Overlay complexity** - Simple overlaying of scaffolding grid on architectural drawing is visually confusing
5. **Need for better approach** - Next iteration should consider:
   - Simplified diagram (less architectural detail)
   - Clearer scaffolding visualization
   - Better tool/method for combining images
   - Possibly vector-based approach (SVG) instead of raster overlay

---

## Current Status

**Architectural Data:** ✅ Extracted and documented  
**Scaffolding Overlay:** ❌ Attempted but unsuccessful (v1)  
**Next Steps:** TBD - New approach for fresh start

---

## Commands Reference

### Environment Setup
```bash
cd /Volumes/Extreme_SSD/macos/GitHub_be/pumped-scripts/test-apps
source .venv/bin/activate
```

### Libraries Installed
```bash
pip install pdfplumber pdf2image Pillow matplotlib numpy
brew install poppler
```

### Scripts Run
```bash
python3 scaf/extract_elevations.py          # Failed
python3 scaf/pdf_to_images.py               # Success
python3 scaf/create_scaffolding_overlay.py  # Failed
```

---

## Next Phase Planning

Approach to be determined:
- [ ] Clearer scaffolding visualization method
- [ ] Simplified building outline approach
- [ ] Better integration of dimensions with diagram
- [ ] Possibly SVG vector-based solution
- [ ] Iteration cycles with user feedback

---

**Last Updated:** 31 January 2026  
**Status:** Ready for fresh start
