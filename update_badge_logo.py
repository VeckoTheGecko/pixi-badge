import json
import sys

# Usage: python update_badge_logo.py logo.svg badge.json


def read_svg(svg_path):
    with open(svg_path, "r", encoding="utf-8") as f:
        return f.read()


def update_json(json_path, svg_content):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["logoSvg"] = svg_content
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python update_badge_logo.py logo.svg badge.json")
        sys.exit(1)
    svg_path = sys.argv[1]
    json_path = sys.argv[2]
    svg_content = read_svg(svg_path)
    update_json(json_path, svg_content)
    print(f"Updated {json_path} with SVG from {svg_path}.")
