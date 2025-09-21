# AIWorkflowRegistry

A community-driven registry of AI model and workflow JSON descriptions.

This repository provides a standardized way to describe AI models, their inputs/outputs, execution commands, server requirements, and role-based usage limits in a machine-readable JSON format. These JSON files can be used to:

- Generate UIs for model inputs/outputs automatically
- Build CLI workflows or automation pipelines
- Enable discoverability of AI models for developers and hobbyists
- Serve as a reference for AI SaaS platforms such as WebSaaS.ai
- Serve Your JSON Models dynamically via FastAPI Proxy

---

## Serve Your JSON Models via FastAPI Proxy

You can instantly serve any JSON file from `/models/` or `/examples/` using the
[WebSaaS.ai Reverse Proxy](https://github.com/manthos/websaas_reverseproxy).

### Quick Start
1. Clone and run the proxy:
   ```bash
   git clone https://github.com/manthos/saasaiendpoint.git
   cd saasaiendpoint
   uvicorn main:app --reload

This allows you to:

- Host your models on an endpoint with JWT-protected API calls
- Quickly integrate them into frontends or other services
- Test changes locally without deploying a full backend
- Run a WebSaaS.ai AI SaaS web site with the AI service/command line


## Repository Structure

```
AIWorkflowRegistry/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── schemas/                # JSON Schema definitions for validation
├── models/                 # Production-ready AI workflow JSONs
├── examples/               # Tutorial/demo JSON files
└── scripts/                # Utilities: validate, preview, convert JSON

## Getting Started

1. Browse the `models/` directory for production-ready workflows.
2. Browse the `examples/` directory for tutorials or experimental JSONs.
3. Use `schemas/workflow.schema.json` to validate any JSON file.
4. Optionally, use scripts in `scripts/` to preview or test workflows.

## Example

`models/audio-to-video.json` describes a workflow that converts audio + image + lyrics into a video with configurable captions and background opacity.

Fields include:

- `audiomedia` → audio file upload
- `imagemedia` → background image upload
- `texfilemedia` → lyrics/captions file
- `font_color` → caption font color
- `bg_alpha` → background alpha slider

Outputs:

- `processedVideo` → mp4 video file

Actions include `submit`, `startaction`, `stopaction`, `statusaction`, and `testaction`.


## Previewing and Testing Workflows

You can quickly **preview and test your AI workflow JSON files** locally before submitting a PR. This helps ensure that the JSON is valid and demonstrates how it would work in a UI or CLI environment.


### 1. Validate a JSON File
Use the `validate_json.py` script to check a single file or all JSON files:

```bash
# Validate all JSON files in models/ and examples/
python scripts/validate_json.py

# Validate a single file
python -m jsonschema -i models/audio-to-video.json schemas/workflow.schema.json
```

✅ Output will show `[OK]` for valid files and `[ERROR]` for invalid files with details.

### 2. Preview Workflow Inputs
You can create a simple CLI preview script (`preview_json.py`) to list all input fields and expected types:

```bash
python scripts/preview_json.py models/audio-to-video.json
```

**Example output:**

```
Workflow: Audio-to-Video
Description: Form for Audio-to-Video model

Fields:
1. audiomedia (fileUpload) - Audio Upload [required]
2. imagemedia (fileUpload) - Image Upload [required]
3. texfilemedia (fileUpload) - Lyrics Upload [required]
4. font_color (colorPicker) - Font color for caption [default: #FFFFFF]
5. bg_alpha (inputSlider) - Background alpha [default: 0.5, min:0, max:1, step:0.1]

Output:
processedVideo (video, mp4)
```

### 3. Simulate a Workflow Command
You can preview how the workflow command would be executed (without actually running it):

```bash
python scripts/preview_json.py --command models/audio-to-video.json
```

**Example output:**

```
Command to run:
python spectrum_video.py <audiomedia> --background_image=<imagemedia> \
--lyrics_file=<texfilemedia> --font_color='<font_color>' \
--background_alpha=<bg_alpha> <processedVideo> --debug
```

### 4. Benefits
- Contributors can **test their JSON locally** before submitting a PR.
- Developers can **automatically generate forms, CLI interfaces, or UIs** using the JSON.
- Makes your repository **more interactive and user-friendly**, encouraging adoption.

---

## License

This project is licensed under the MIT License. See LICENSE for details.

