# Contributing to AIWorkflowRegistry

We welcome contributions! You can help by:

- Adding new AI workflow JSON descriptions
- Improving existing JSON files
- Adding examples or tutorials
- Updating the JSON Schema

---

## Guidelines

### 1. JSON Files
- Place **production-ready workflows** in `/models/`
- Place **tutorial, demo, or experimental workflows** in `/examples/`
- Use **meaningful file names** (e.g., `text-to-speech.json`, `image-upscaler.json`)

### 2. Sensitive Data
- Do **not** include API keys, tokens, or other secrets.
- Use placeholders like `<API_KEY>` or `<YOUR_ENDPOINT>`.

### 3. Validation
- Validate your JSON files against `schemas/workflow.schema.json`
- You can use `scripts/validate_json.py` to automate validation

### 4. Pull Requests
1. Fork the repository
2. Add your JSON file to `/models/` or `/examples/`
3. Ensure it validates against the schema
4. Submit a PR with a clear description

### 5. Example Workflow Contribution

**Adding a new workflow JSON**

1. Copy the template from `/examples/demo-simple-form.json`
2. Fill out the fields for your model/workflow
3. Replace any placeholder endpoints or commands
4. Validate the JSON using `scripts/validate_json.py`
5. Place the file in `/models/` if production-ready, or `/examples/` if tutorial/demo

**Example JSON Contribution (minimal)**

```json
{
  "type": "object",
  "title": "Text-to-Speech",
  "fields": [
    {
      "id": "input_text",
      "type": "textarea",
      "label": "Input Text",
      "required": true
    }
  ],
  "output": [
    {
      "id": "speech_audio",
      "type": "audio",
      "format": "mp3"
    }
  ],
  "actions": {
    "submit": {
      "method": "POST",
      "endpoint": "<YOUR_API_ENDPOINT>"
    }
  },
  "command": "python tts_model.py <input_text> <speech_audio>",
  "description": "Convert text to speech",
  "allowed_roles": ["registered", "basic", "premium"],
  "main_input_id": "input_text"
}
```

## Example Model JSON

To help contributors understand how to turn a command-line AI service with parameters into a JSON model file, we have included a fully annotated example:

**[`examples/image-to-image-example.json`](examples/image-to-image-example.json)**  

This file shows:
- How to define `fields` for user inputs (matching CLI parameters).
- How to specify `command` with placeholders that get dynamically filled.
- How to describe `output` objects (files/images produced by the process).
- How to set up `actions` for submit, start, stop, and status operations.
- How to apply `role_limits` and `allowed_roles` to control access and resource limits.

**Usage:**  
When contributing a new model:
1. Copy the example JSON to `/models/<your-model-name>.json`.
2. Replace the `command`, `endpoint`, and any placeholders with real values.
3. Adjust `fields` to match the parameters required by your CLI tool or API.
4. Update `output` objects to match the expected result files or data.

> **Tip:** This example is intentionally simple and designed to illustrate the mapping process from a CLI command to the JSON structure. Real models may have additional validation, conditionals, or parameter dependencies.

### 6. Schema Updates
- If you want to propose a schema update, submit a PR with:
  - Updated `workflow.schema.json`
  - Example JSON demonstrating the change
  - Updated README/docs if necessary

---

Thank you for contributing! Together we can make a **universal, community-driven AI workflow registry**.

