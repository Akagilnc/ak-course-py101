const path = require("path");
const { chromium } = require("playwright");

const [, , slideFileArg] = process.argv;

if (!slideFileArg) {
  console.error("Usage: node scripts/check-slides.js <slides.html>");
  process.exit(1);
}

const viewport = { width: 1920, height: 1080 };
const slideFile = path.resolve(slideFileArg);
const slideUrl = `file://${slideFile}`;

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });

  await page.goto(slideUrl);
  const slideCount = await page.locator(".slide").count();
  const issues = [];

  for (let slideNumber = 1; slideNumber <= slideCount; slideNumber += 1) {
    await page.goto(`${slideUrl}#slide-${slideNumber}`);
    await page.waitForTimeout(80);

    const info = await page.evaluate(() => {
      const active = document.querySelector(".slide.active");
      const label = active?.querySelector(".eyebrow")?.textContent?.trim() || "";
      const title = active?.querySelector("h1,h2")?.textContent?.trim() || "";
      const children = Array.from(active?.children || []);

      let bottom = 0;
      let right = 0;
      for (const child of children) {
        const rect = child.getBoundingClientRect();
        bottom = Math.max(bottom, rect.bottom);
        right = Math.max(right, rect.right);
      }

      return {
        label,
        title,
        bottomOverflow: Math.round(Math.max(0, bottom - window.innerHeight)),
        rightOverflow: Math.round(Math.max(0, right - window.innerWidth)),
      };
    });

    if (info.bottomOverflow || info.rightOverflow) {
      issues.push({ slide: slideNumber, ...info });
    }
  }

  await browser.close();

  if (issues.length > 0) {
    console.error(JSON.stringify({ slideCount, issues }, null, 2));
    process.exit(1);
  }

  console.log(`OK: ${slideCount} slides fit within ${viewport.width}x${viewport.height}.`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
