from functools import lru_cache
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
PHOTOS_DIR = ROOT_DIR / 'photos'
DESCS_FILE = ROOT_DIR / 'src' / 'descs.txt'
OUTPUT_FILE = ROOT_DIR / 'view.md'


def extract_date_from_name(file_name: str) -> str:
    if len(file_name) >= 10:
        return file_name[:10]
    return ''


@lru_cache(maxsize=1)
def get_descs() -> dict[str, str]:
    if not DESCS_FILE.exists():
        return {}

    descs: dict[str, str] = {}
    current_name = None
    current_lines: list[str] = []

    for raw_line in DESCS_FILE.read_text(encoding='utf-8').splitlines():
        line = raw_line.rstrip()

        if line.startswith('[') and line.endswith(']'):
            if current_name is not None:
                descs[current_name] = '\n'.join(current_lines).strip()
            current_name = line[1:-1].strip()
            current_lines = []
            continue

        if current_name is not None:
            current_lines.append(raw_line)

    if current_name is not None:
        descs[current_name] = '\n'.join(current_lines).strip()

    return descs


def read_optional_text(image_file: Path) -> str:
    return get_descs().get(image_file.name, '')


def build_cell(image_file: Path) -> str:
    date_text = extract_date_from_name(image_file.name)
    note_text = read_optional_text(image_file)

    lines = [
        '<td width="50%">',
        '',
        f'![](photos/{image_file.name})',
        date_text,
    ]
    if note_text:
        lines.extend([
            '',
            note_text,
        ])
    lines.extend([
        '',
        '</td>',
    ])
    return '\n'.join(lines)


def generate_view_md() -> str:
    imgs = sorted(PHOTOS_DIR.glob('*.jpg'), key=lambda path: path.name)

    lines = [
        '<!-- 该文件由 generate_viewmd.py 生成，请勿手动编辑此文件 -->',
        '',
        '<table>',
        '',
    ]

    for index in range(0, len(imgs), 2):
        left_img = imgs[index]
        right_img = imgs[index + 1] if index + 1 < len(imgs) else None

        lines.append('<tr>')
        lines.append(build_cell(left_img))

        if right_img is None:
            lines.extend([
                '<td width="50%">',
                '',
                '</td>',
            ])
        else:
            lines.append(build_cell(right_img))

        lines.extend([
            '</tr>',
            '',
        ])

        if index + 2 < len(imgs):
            lines.extend([
                '<tr><td><br></td></tr>',
                '',
            ])

    lines.append('</table>')
    lines.append('')

    return '\n'.join(lines)


def main() -> None:
    output = generate_view_md()
    OUTPUT_FILE.write_text(output, encoding='utf-8')


if __name__ == '__main__':
    main()
