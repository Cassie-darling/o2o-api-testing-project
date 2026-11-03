# -*- coding: utf -*-
import io, os
base = r"D:\MyData\Claude\Agent\Test\draft_36486f20_folder"
parts = ["draft.xml", "part2.xml", "part3.xml"]
out = []
for name in parts:
    with io.open(os.path.join(base, name), "r", encoding="utf-8") as f:
        out.append(f.read().rstrip())
merged = "\n".join(out) + "\n"
with io.open(os.path.join(base, "full.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write(merged)
print("merged chars:", len(merged))
