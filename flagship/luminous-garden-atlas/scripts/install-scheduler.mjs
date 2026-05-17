import { mkdir, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const home = os.homedir();
const label = "com.luminous-garden-atlas.daily";
const launchAgents = path.join(home, "Library", "LaunchAgents");
const logDir = path.join(home, "Library", "Logs", "LuminousGardenAtlas");
const plistPath = path.join(launchAgents, `${label}.plist`);
const npmPath = spawnSync("which", ["npm"], { encoding: "utf8" }).stdout.trim() || "/usr/local/bin/npm";

const plist = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${label}</string>
  <key>WorkingDirectory</key>
  <string>${root}</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/zsh</string>
    <string>-lc</string>
    <string>cd "${root}" &amp;&amp; "${npmPath}" run garden:daily</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>0</integer>
    <key>Minute</key>
    <integer>5</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>${path.join(logDir, "daily.out.log")}</string>
  <key>StandardErrorPath</key>
  <string>${path.join(logDir, "daily.err.log")}</string>
  <key>RunAtLoad</key>
  <true/>
</dict>
</plist>
`;

await mkdir(launchAgents, { recursive: true });
await mkdir(logDir, { recursive: true });
await writeFile(plistPath, plist);

spawnSync("launchctl", ["unload", plistPath], { stdio: "ignore" });
const load = spawnSync("launchctl", ["load", plistPath], { encoding: "utf8" });
if (load.status !== 0) {
  console.error(load.stderr || "launchctl load failed");
  process.exit(load.status || 1);
}

console.log(`Installed ${label}`);
console.log(`Plist: ${plistPath}`);
console.log(`Logs: ${logDir}`);
