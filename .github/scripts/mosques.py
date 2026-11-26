#!/usr/bin/env python3
"""
منارە — build public/data/mosques.json from an OpenStreetMap extract (GeoJSON sequence)
Design & Development Hemn A.Muhammad

Input: osmium export of places of worship / mosque buildings in the Kurdistan box.
Output: {"updated", "source", "bbox": [minLat, minLon, maxLat, maxLon], "m": [[lat, lon, name], ...]}
"""
import json, sys, datetime

SRC, DST = sys.argv[1], sys.argv[2]
BBOX = [34.3, 42.3, 37.4, 46.3]          # minLat, minLon, maxLat, maxLon
WORDS = ("مزگەوت", "مزگەفت", "جامع", "مسجد", "mosque", "masjid")

def centre(g):
    t, c = g["type"], g["coordinates"]
    if t == "Point":
        return c[1], c[0]
    pts = []
    def walk(x):
        if isinstance(x[0], (int, float)):
            pts.append(x)
        else:
            for y in x:
                walk(y)
    walk(c)
    return sum(p[1] for p in pts) / len(pts), sum(p[0] for p in pts) / len(pts)

out, seen = [], set()
with open(SRC, encoding="utf-8") as f:
    for line in f:
        line = line.strip().lstrip("\x1e")
        if not line:
            continue
        ft = json.loads(line)
        p = ft.get("properties") or {}
        rel = p.get("religion")
        name = p.get("name:ckb") or p.get("name:ku") or p.get("name") or p.get("name:ar") or ""
        named = any(w in (name + " " + p.get("name:en", "")).lower() for w in WORDS)
        if rel and rel != "muslim":
            continue
        if not (rel == "muslim" or p.get("building") == "mosque" or named):
            continue
        try:
            lat, lon = centre(ft["geometry"])
        except Exception:
            continue
        if not (BBOX[0] <= lat <= BBOX[2] and BBOX[1] <= lon <= BBOX[3]):
            continue
        k = (round(lat, 4), round(lon, 4))        # same mosque as node + building: keep one
        if k in seen:
            continue
        seen.add(k)
        out.append([round(lat, 6), round(lon, 6), name.strip()])

out.sort()
data = {
    "updated": datetime.date.today().isoformat(),
    "source": "© OpenStreetMap contributors (ODbL)",
    "bbox": BBOX,
    "m": out,
}
with open(DST, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
print(f"{len(out)} mosques -> {DST}")

