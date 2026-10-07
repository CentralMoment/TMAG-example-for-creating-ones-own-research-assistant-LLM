"""Download public SFO sources with provenance, without replacing existing files."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]


def fetch(url):
    """Read a public source with a timeout and a 25 MiB size limit."""
    with urlopen(url, timeout=60) as response:
        data = response.read(25 * 1024 * 1024 + 1)
    if len(data) > 25 * 1024 * 1024:
        raise ValueError("Unexpected download larger than 25 MiB.")
    return data


def main():
    """Resolve the dictionary blob and save immutable downloads with hashes."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=ROOT / "data/private")
    args = parser.parse_args()
    targets = [args.directory / "2018 SFO Customer Survey.csv",
               args.directory / "2018 SFO Customer Survey Data Dictionary.xlsx"]
    if any(path.exists() for path in targets):
        raise SystemExit("Source files already exist. Choose a new --directory to compare downloads.")
    survey = json.loads(fetch("https://data.sfgov.org/api/views/3w8r-nuxp.json"))
    dictionary = json.loads(fetch("https://data.sfgov.org/api/views/wkh6-n369.json"))
    if survey["name"] != "2018 SFO Customer Survey" or dictionary["name"] != "2018 SFO Customer Survey Data Dictionary":
        raise ValueError("Dataset identity changed; inspect publisher metadata.")
    urls = ["https://data.sfgov.org/api/views/3w8r-nuxp/rows.csv?accessType=DOWNLOAD",
            f"https://data.sfgov.org/api/views/wkh6-n369/files/{dictionary['blobId']}?download=true"]
    downloads = [fetch(url) for url in urls]
    if not downloads[1].startswith(b"PK"):
        raise ValueError("Dictionary download is not an XLSX ZIP container.")
    args.directory.mkdir(parents=True, exist_ok=True)
    sources = []
    for target, url, data in zip(targets, urls, downloads):
        with target.open("xb") as handle:
            handle.write(data)
        sources.append({"filename": target.name, "url": url, "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest()})
    manifest = {"retrieved_utc": datetime.now(timezone.utc).isoformat(), "sources": sources,
                "note": "Publisher terms apply. Byte hashes can differ across exports; compare normalized contents."}
    (args.directory / "source-manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
