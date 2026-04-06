from pathlib import Path


ROOT = Path(__file__).parent
README_TONG = ROOT / "README-tong.md"

START = "<!-- AUTO_CONTESTS_START -->"
END = "<!-- AUTO_CONTESTS_END -->"

DISPLAY_NAME_MAP = {
    "so-khao-dot1-29.3.26": "Sơ khảo đợt 1 - 29.3.26",
    "tin-hoc-tre-bang-a-2026-da-nang-p-ngu-hanh-son": "Tin học trẻ bảng A 2026 - Đà Nẵng - P. Ngũ Hành Sơn",
}


def format_title(folder_name: str) -> str:
    if folder_name in DISPLAY_NAME_MAP:
        return DISPLAY_NAME_MAP[folder_name]
    return folder_name.replace("-", " ").strip().title()


def collect_contests():
    contests = []
    for child in ROOT.iterdir():
        if not child.is_dir():
            continue
        readme = child / "README.md"
        if readme.exists():
            contests.append((child.name, readme.relative_to(ROOT).as_posix()))
    contests.sort(key=lambda x: x[0].lower())
    return contests


def build_auto_section(contests):
    lines = [START]
    if not contests:
        lines.append("- (Chưa có đề nào)")
    else:
        for folder_name, readme_rel in contests:
            title = format_title(folder_name)
            lines.append(f"- [{title}]({readme_rel})")
    lines.append(END)
    return "\n".join(lines)


def ensure_readme_exists():
    if README_TONG.exists():
        return
    content = (
        "# Tổng hợp đề luyện\n\n"
        "README này được cập nhật tự động bởi script `update_readme_tong.py`.\n\n"
        "## Danh sách đề\n"
        f"{START}\n"
        "- (Chưa có đề nào)\n"
        f"{END}\n"
    )
    README_TONG.write_text(content, encoding="utf-8")


def update_readme():
    ensure_readme_exists()
    text = README_TONG.read_text(encoding="utf-8")
    auto_section = build_auto_section(collect_contests())

    if START in text and END in text:
        start_idx = text.index(START)
        end_idx = text.index(END) + len(END)
        new_text = text[:start_idx] + auto_section + text[end_idx:]
    else:
        if not text.endswith("\n"):
            text += "\n"
        new_text = text + "\n## Danh sách đề\n" + auto_section + "\n"

    README_TONG.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
    print("Updated README-tong.md")
