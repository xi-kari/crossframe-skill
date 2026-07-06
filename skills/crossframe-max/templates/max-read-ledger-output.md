# max-read-ledger.json

`max-read-ledger.json` is mandatory for completed `crossframe-max` artifacts. It proves the full-source exhaustive pass structurally instead of relying only on Markdown markers.

It must agree with `max-source-snapshot.json`. After `max-source-snapshot.json` is frozen, later phases perform source-anchor verification only.

```json
{
  "source_sha256": "d3f3c666ef0d4f6d0a3a0517ae98acbbeeaa7143abd82927ee06fa39e5d80499",
  "total_expected_paragraphs": 3273,
  "total_read_paragraphs": 3273,
  "full_source_exhaustive_pass": true,
  "stage_0_source_inventory": "satisfied",
  "stage_8_final_read_audit": "satisfied",
  "missing_paragraphs": [],
  "files": [
    {
      "file": "03-world-layer.md",
      "expected_range": ["P0897", "P1519"],
      "read_ranges": [["P0897", "P1519"]],
      "status": "full",
      "layer_digest": "one-paragraph digest after source read",
      "unresolved_gaps": []
    }
  ]
}
```

Required rules:

- `total_expected_paragraphs` must be `3273`.
- `total_read_paragraphs` must be `3273`.
- `full_source_exhaustive_pass` must be `true`.
- `missing_paragraphs` must be empty.
- Every full-source layer file must have `status: full`.
- `layer_digest` cannot replace `read_ranges` or source paragraph ids.
- `max-source-snapshot.json` must record the same source SHA256, `total_paragraphs: 3273`, `table_count: 60`, and `source_snapshot_id`.
