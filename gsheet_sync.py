import urllib.request
import json

WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzf2qp0zjRl0Q6B4qtqSU2cStOANYKk3FC1sn9P2iMzYWGStw6BMpiMOv9SZj-2uKDK/exec"

def get_sheets():
    """Membaca seluruh isi Google Sheets (semua sheet) dalam bentuk dictionary JSON."""
    req = urllib.request.urlopen(WEBHOOK_URL)
    return json.loads(req.read().decode('utf-8'))

def set_cell(sheet_name, cell_range, value):
    """Mengubah isi 1 sel (contoh: range='D12', value='Budi Santoso')."""
    return post_update({
        "sheet": sheet_name,
        "action": "setCell",
        "range": cell_range,
        "value": value
    })

def set_values(sheet_name, start_row, start_col, values_2d):
    """Mengubah banyak sel sekaligus mulai dari baris start_row dan kolom start_col (1-indexed)."""
    return post_update({
        "sheet": sheet_name,
        "action": "setValues",
        "startRow": start_row,
        "startCol": start_col,
        "values": values_2d
    })

def append_row(sheet_name, row_list):
    """Menambahkan 1 baris baru di bagian paling bawah sheet."""
    return post_update({
        "sheet": sheet_name,
        "action": "appendRow",
        "row": row_list
    })

def post_update(payload):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read().decode('utf-8'))

if __name__ == "__main__":
    data = get_sheets()
    for name, rows in data.items():
        print(f"=== {name} ({len(rows)} baris) ===")
        for idx, r in enumerate(rows, start=1):
            print(f"Baris {idx}: {r}")
