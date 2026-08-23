#!/usr/bin/env python3
"""Recon a target business website: screenshots (desktop+mobile), HTML, and quick technical signals.

Usage: recon.py <url> <out_dir>
"""
import sys
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

DESKTOP = {"width": 1440, "height": 900}
MOBILE = {"width": 390, "height": 844}


def capture(url: str, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    result = {"url": url, "signals": {}}

    with sync_playwright() as p:
        browser = p.chromium.launch()

        # --- Desktop pass (JS enabled) ---
        page = browser.new_page(viewport=DESKTOP)
        page.goto(url, wait_until="load", timeout=30000)
        page.wait_for_timeout(1500)
        page.screenshot(path=str(out_dir / "desktop.jpg"), full_page=True, type="jpeg", quality=85)
        html = page.content()
        (out_dir / "page.html").write_text(html, encoding="utf-8")

        result["title"] = page.title()
        result["signals"]["has_favicon"] = bool(
            page.query_selector("link[rel*='icon']")
        )
        meta_desc = page.query_selector("meta[name='description']")
        result["signals"]["has_meta_description"] = bool(
            meta_desc and meta_desc.get_attribute("content")
        )
        og_image = page.query_selector("meta[property='og:image']")
        result["signals"]["has_og_image"] = bool(
            og_image and og_image.get_attribute("content")
        )
        viewport_meta = page.query_selector("meta[name='viewport']")
        result["signals"]["has_viewport_meta"] = bool(viewport_meta)

        body_text = page.inner_text("body")
        result["signals"]["visible_text_chars"] = len(body_text.strip())

        emails = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", html))
        phones = set(re.findall(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}", html))
        result["signals"]["emails_found"] = sorted(emails)[:5]
        result["signals"]["phones_found"] = sorted(phones)[:5]

        images = page.query_selector_all("img")
        result["signals"]["image_count"] = len(images)

        page.close()

        # --- Mobile pass ---
        mpage = browser.new_page(
            viewport=MOBILE,
            is_mobile=True,
            has_touch=True,
            user_agent=(
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
            ),
        )
        mpage.goto(url, wait_until="load", timeout=30000)
        mpage.wait_for_timeout(1500)
        mpage.screenshot(path=str(out_dir / "mobile.jpg"), full_page=True, type="jpeg", quality=85)
        mpage.close()

        # --- No-JS pass: does the page render anything without JavaScript? ---
        nojs_context = browser.new_context(viewport=DESKTOP, java_script_enabled=False)
        nojs_page = nojs_context.new_page()
        try:
            nojs_page.goto(url, wait_until="load", timeout=30000)
            nojs_text = nojs_page.inner_text("body").strip()
            nojs_page.screenshot(path=str(out_dir / "nojs.jpg"), full_page=True, type="jpeg", quality=85)
            result["signals"]["renders_without_js"] = len(nojs_text) > 50
            result["signals"]["nojs_visible_text_chars"] = len(nojs_text)
        except Exception as e:
            result["signals"]["renders_without_js"] = None
            result["signals"]["nojs_error"] = str(e)
        nojs_context.close()

        browser.close()

    (out_dir / "recon.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: recon.py <url> <out_dir>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]
    out_dir = Path(sys.argv[2])
    res = capture(url, out_dir)

    print(f"[recon] title: {res.get('title')}")
    print(f"[recon] desktop screenshot: {out_dir / 'desktop.jpg'}")
    print(f"[recon] mobile screenshot:  {out_dir / 'mobile.jpg'}")
    print(f"[recon] no-js screenshot:   {out_dir / 'nojs.jpg'}")
    print(f"[recon] signals: {json.dumps(res['signals'], indent=2)}")
