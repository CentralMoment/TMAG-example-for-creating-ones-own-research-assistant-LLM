"""Check documentation links and Streamlit interactions with an explicitly mocked API."""
import os
import re
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from streamlit.testing.v1 import AppTest


def main():
    """Exercise missing credentials, answer display, reset, and remote-file deletion."""
    for path in [ROOT / "README.md", *ROOT.glob("docs/**/*.md")]:
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#"):
                assert (path.parent / unquote(link.split("#")[0])).exists(), (path, link)
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "", "ASSISTANT_CONFIG": "config.json"}):
        app = AppTest.from_file(str(ROOT / "streamlit_app.py")).run()
        assert not app.exception and len(app.error) == 1
    mock = MagicMock()
    mock.files.upload.side_effect = [SimpleNamespace(id="one"), SimpleNamespace(id="two")]
    mock.messages.create.return_value = {"content":[{"type":"text","text":"Mock answer: mean=3.0, n=60"}],
        "container":{"id":"test-container"},"stop_reason":"end_turn","usage":{"input_tokens":10,"output_tokens":5}}
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-placeholder", "ASSISTANT_CONFIG": "config.json"}), patch(
        "anthropic.Anthropic", return_value=mock):
        app = AppTest.from_file(str(ROOT / "streamlit_app.py")).run()
        app.chat_input[0].set_value("Compute the mean").run()
        assert not app.exception and mock.files.upload.call_count == 2
        assert any("mean=3.0" in item.value for item in app.markdown)
        app.chat_input[0].set_value("Again").run()
        assert not app.exception and mock.files.upload.call_count == 2
        app.button[0].click().run()
        assert not app.session_state["research_session"]["turns"]
        app.button[1].click().run()
        assert mock.files.delete.call_count == 2
    print("PASS: documentation links, missing-key UI, mocked turns, reuse, reset, cleanup.")


if __name__ == "__main__":
    main()
