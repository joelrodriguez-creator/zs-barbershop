#!/usr/bin/env node
// Generate icon variants via Vertex AI Imagen 4 Fast.
// Usage: node gen-icon.mjs <slug> <subject-sentence>
// Reads ADC token + project from gcloud, writes 4 PNGs to ../assets/generated/icons/<slug>-v{1..4}.png

import { execSync } from "node:child_process";
import { writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const [, , slug, ...subjectParts] = process.argv;
if (!slug || !subjectParts.length) {
  console.error("Usage: node gen-icon.mjs <slug> <subject sentence>");
  process.exit(2);
}
const subject = subjectParts.join(" ");

const STYLE = 'Vintage barbershop pictogram icon, minimalist monoline line drawing, single thin clean line in brass gold color (hex #c8a35a) on transparent background, centered composition, no shadows, no gradients, no fill, simple geometric forms, elegant heritage barbershop aesthetic, suitable for a $35 Miami neighborhood barbershop website. Square 1:1 aspect ratio.';
const prompt = `${STYLE} ${subject}`;

const PROJECT = "driven-torus-493217-q5";
const MODEL = "imagen-4.0-fast-generate-001";
const URL = `https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT}/locations/us-central1/publishers/google/models/${MODEL}:predict`;

const token = execSync("gcloud auth application-default print-access-token", { encoding: "utf8" }).trim();

const body = {
  instances: [{ prompt }],
  parameters: { sampleCount: 4, aspectRatio: "1:1" },
};

console.log(`Generating 4 variants for "${slug}"...`);
const res = await fetch(URL, {
  method: "POST",
  headers: { "Authorization": `Bearer ${token}`, "Content-Type": "application/json" },
  body: JSON.stringify(body),
});
const data = await res.json();

if (!res.ok || !data.predictions?.length) {
  console.error("Request failed:", JSON.stringify(data, null, 2));
  process.exit(1);
}

const here = dirname(fileURLToPath(import.meta.url));
const outDir = join(here, "..", "assets", "generated", "icons");
mkdirSync(outDir, { recursive: true });

data.predictions.forEach((p, i) => {
  const file = join(outDir, `${slug}-v${i + 1}.png`);
  writeFileSync(file, Buffer.from(p.bytesBase64Encoded, "base64"));
  console.log(`  wrote ${file}`);
});

console.log(`Done. Open: ${outDir}`);
