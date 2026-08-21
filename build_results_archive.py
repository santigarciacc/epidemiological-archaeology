from pathlib import Path
import hashlib
import json
import zipfile

root = Path(__file__).resolve().parents[1]
members = [
    root / 'tables' / 'V26_national_wave_reconstructions.csv',
    root / 'tables' / 'V26_country_inclusion_log.csv',
    root / 'tables' / 'V26_country_wave_counts.csv',
    root / 'tables' / 'V26_simulation_replicates.csv',
    root / 'tables' / 'V26_simulation_summary.csv',
    root / 'tables' / 'V26_historical_national_wave_summary.csv',
    root / 'tables' / 'V26_headline_results.json',
    root / 'figures' / 'V26_Figure1_identifiability_simulation.pdf',
    root / 'figures' / 'V26_Figure2_COVID_national_wave_geometry.pdf',
    root / 'figures' / 'V26_Figure3_global_amplitude_maps.pdf',
    root / 'figures' / 'V26_Figure4_1918_national_intervals.pdf',
]
out = root / 'EPIDEMICS_V26_RESULTS_TO_RETURN.zip'
fixed_time = (2026, 8, 15, 0, 0, 0)
with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for path in members:
        rel = path.relative_to(root).as_posix()
        info = zipfile.ZipInfo(rel, date_time=fixed_time)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
h = hashlib.sha256(out.read_bytes()).hexdigest()
manifest = {'archive': out.name, 'sha256': h, 'bytes': out.stat().st_size}
(root / 'tables' / 'V26_results_archive_manifest.json').write_text(json.dumps(manifest, indent=2))
print(json.dumps(manifest, indent=2))
