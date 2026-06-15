# crossframe-v5 retirement archive restore notes

Archive root:
E:\世界模型\skill\crossframe-skill\archives\crossframe-v5-retirement-20260613-084835

Retired directories were copied from:
- C:\Users\cangm\.codex\skills\crossframe-v5*
- D:\deepseek\.reasonix\skills\crossframe-v5*

To restore Codex old v5 skills if explicitly needed:
``powershell
Copy-Item -LiteralPath 'E:\世界模型\skill\crossframe-skill\archives\crossframe-v5-retirement-20260613-084835\codex-skills\crossframe-v5*' -Destination 'C:\Users\cangm\.codex\skills' -Recurse -Force
``

To restore Reasonix old v5 skills if explicitly needed:
``powershell
Copy-Item -LiteralPath 'E:\世界模型\skill\crossframe-skill\archives\crossframe-v5-retirement-20260613-084835\reasonix-skills\crossframe-v5*' -Destination 'D:\deepseek\.reasonix\skills' -Recurse -Force
``

These old directories were retired because the current authority is E:\世界模型\skill\crossframe-skill\skills\crossframe* with v5-read-state-capsule and source anchor integrity integrated into the current family.