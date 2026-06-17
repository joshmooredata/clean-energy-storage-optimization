#!/usr/bin/env python3
"""Download ERCOT/PJM electricity price data from OpenEI or a public Kaggle CSV URL."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import pandas as pd

OPENEI_BASE = "https://api.openei.org/utility_rates"
DEFAULT_OPENEI_API_KEY = "DEMO_KEY"


def url_get_json(url: str) -> Any:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        payload = resp.read()
    return json.loads(payload)


def fetch_openei_rates(search_term: str, api_key: str = DEFAULT_OPENEI_API_KEY, limit: int = 500, page: int = 1) -> pd.DataFrame:
    params = {
        "version": "latest",
        "format": "json",
        "api_key": api_key,
        "search": search_term,
        "limit": limit,
        "page": page,
    }
    url = f"{OPENEI_BASE}?{urlencode(params)}"
    data = url_get_json(url)
    items = data.get("items", [])
    if not items:
        raise RuntimeError(f"No records returned from OpenEI for search='{search_term}'.")

    df = pd.json_normalize(items)
    if "startdate" in df.columns:
        df["startdate"] = pd.to_datetime(df["startdate"], unit="s", errors="coerce")
    if "enddate" in df.columns:
        df["enddate"] = pd.to_datetime(df["enddate"], unit="s", errors="coerce")
    return df


def read_public_csv(url: str) -> pd.DataFrame:
    if not url.lower().startswith("http"):
        raise ValueError("The Kaggle URL must be a public HTTPS URL to a CSV file.")
    return pd.read_csv(url)


def save_dataframe(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download ERCOT/PJM electricity price data from OpenEI or a public Kaggle CSV URL."
    )
    parser.add_argument(
        "--source",
        choices=["openei", "kaggle"],
        default="openei",
        help="Choose the source for the download. Use 'openei' for OpenEI API or 'kaggle' for a public CSV URL.",
    )
    parser.add_argument(
        "--search",
        default="PJM",
        help="Search term for OpenEI. Examples: ERCOT, PJM. Only used with --source openei.",
    )
    parser.add_argument(
        "--api-key",
        default=DEFAULT_OPENEI_API_KEY,
        help="OpenEI API key. Defaults to DEMO_KEY.",
    )
    parser.add_argument(
        "--kaggle-url",
        default="",
        help="Public direct CSV URL for a Kaggle dataset or other hosted CSV. Only used with --source kaggle.",
    )
    parser.add_argument(
        "--output",
        default="grid_prices.csv",
        help="Local output CSV filename.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=500,
        help="Maximum number of rows to request from OpenEI per page.",
    )
    parser.add_argument(
        "--page",
        type=int,
        default=1,
        help="Page number for OpenEI pagination.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)

    if args.source == "openei":
        df = fetch_openei_rates(
            search_term=args.search,
            api_key=args.api_key,
            limit=args.limit,
            page=args.page,
        )
    else:
        if not args.kaggle_url:
            raise SystemExit("For --source kaggle, you must set --kaggle-url to a public CSV URL.")
        df = read_public_csv(args.kaggle_url)

    save_dataframe(df, output_path)
    print(f"Saved {len(df)} rows to {output_path}")


if __name__ == "__main__":
    main()
