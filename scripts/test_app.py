"""Exercise the UI without credentials, uploads, or paid API calls."""

import ast
import os
import re
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from streamlit.testing.v1 import AppTest


def main():
    """Check links and app behavior using an explicitly mocked API client."""
    root = Path(__file__).resolve().parents[1]
    for path in [root / "streamlit_app.py", *root.glob("scripts/*.py")]:
        ast.parse(path.read_text(encoding="utf-8"))
    for path in [root / "README.md", *root.glob("docs/*.md")]:
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#"):
                assert (path.parent / link.split("#")[0]).exists(), (path, link)
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": ""}):
        app = AppTest.from_file(str(root / "streamlit_app.py")).run()
        assert not app.exception and len(app.error) == 1
    client = MagicMock()
    client.files.upload.return_value = SimpleNamespace(id="file-test")
    client.messages.create.return_value = SimpleNamespace(
        content=[SimpleNamespace(type="text", text="Mock response: mean=3.0, n=60")],
        container=SimpleNamespace(id="container-test"), stop_reason="end_turn",
    )
    with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-placeholder"}), patch(
        "anthropic.Anthropic", return_value=client
    ):
        app = AppTest.from_file(str(root / "streamlit_app.py")).run()
        assert not app.exception
        app.chat_input[0].set_value("Compute the mean").run()
        assert not app.exception and client.files.upload.call_count == 2
        assert client.messages.create.call_count == 1
        app.chat_input[0].set_value("And the count?").run()
        assert not app.exception and client.files.upload.call_count == 2
        assert client.messages.create.call_args.kwargs["container"] == "container-test"
        app.button[0].click().run()
        assert not app.exception and not app.session_state["history"]
    print("PASS: syntax, links, missing-key UI, mocked turns, upload/container reuse, reset.")


if __name__ == "__main__":
    main()
