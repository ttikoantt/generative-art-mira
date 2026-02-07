#!/usr/bin/env node

/**
 * ASCII Art Pattern Generator
 * Creativity meets mathematics - generating beautiful ASCII art patterns
 */

const PATTERNS = {
  mandelbrot: {
    name: 'Mandelbrot Set',
    chars: ' .:-=+*#%@',
    width: 80,
    height: 40,
    generate: (w, h, chars) => {
      const result = [];
      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const cx = (x - w / 2) / (w / 4) - 0.5;
          const cy = (y - h / 2) / (h / 4);
          let zx = 0, zy = 0;
          let iter = 0;
          const maxIter = chars.length - 1;

          while (zx * zx + zy * zy < 4 && iter < maxIter) {
            const temp = zx * zx - zy * zy + cx;
            zy = 2 * zx * zy + cy;
            zx = temp;
            iter++;
          }

          line += chars[iter];
        }
        result.push(line);
      }
      return result;
    }
  },

  ripple: {
    name: 'Stone Ripple',
    chars: ' .•*◊◉●',
    width: 60,
    height: 30,
    generate: (w, h, chars) => {
      const result = [];
      const cx = w / 2, cy = h / 2;
      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const dist = Math.sqrt((x - cx) ** 2 + (y - cy) ** 2);
          const wave = Math.sin(dist / 3 - Date.now() / 1000);
          const charIndex = Math.floor((wave + 1) / 2 * (chars.length - 1));
          line += chars[Math.max(0, Math.min(chars.length - 1, charIndex))];
        }
        result.push(line);
      }
      return result;
    }
  },

  spiral: {
    name: 'Golden Spiral',
    chars: ' ░▒▓█',
    width: 50,
    height: 50,
    generate: (w, h, chars) => {
      const result = [];
      const cx = w / 2, cy = h / 2;
      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const dx = x - cx, dy = y - cy;
          const dist = Math.sqrt(dx * dx + dy * dy);
          const angle = Math.atan2(dy, dx);
          const spiral = Math.sin(angle * 5 + dist / 5);
          const charIndex = Math.floor((spiral + 1) / 2 * (chars.length - 1));
          line += chars[Math.max(0, Math.min(chars.length - 1, charIndex))];
        }
        result.push(line);
      }
      return result;
    }
  },

  waves: {
    name: 'Ocean Waves',
    chars: ' 〜～∼⁓≈',
    width: 80,
    height: 30,
    generate: (w, h, chars) => {
      const result = [];
      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const wave1 = Math.sin(x / 8 + y / 4);
          const wave2 = Math.sin(x / 6 - y / 3);
          const combined = (wave1 + wave2) / 2;
          const charIndex = Math.floor((combined + 1) / 2 * (chars.length - 1));
          line += chars[Math.max(0, Math.min(chars.length - 1, charIndex))];
        }
        result.push(line);
      }
      return result;
    }
  },

  stars: {
    name: 'Night Sky',
    chars: '  .⋆✦⭐✨',
    width: 70,
    height: 35,
    generate: (w, h, chars) => {
      const result = [];
      const seed = Math.random() * 10000;
      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const noise = Math.sin(x * 12.9898 + y * 78.233 + seed) * 43758.5453;
          const normalized = noise - Math.floor(noise);
          const threshold = 1 - Math.pow(normalized, 3);
          const charIndex = Math.floor(threshold * (chars.length - 1));
          line += chars[Math.max(0, Math.min(chars.length - 1, charIndex))];
        }
        result.push(line);
      }
      return result;
    }
  },

  dna: {
    name: 'DNA Double Helix',
    chars: ' ·░▒▓█',
    width: 60,
    height: 50,
    generate: (w, h, chars) => {
      const result = [];
      const cx = w / 2;
      const amplitude = w / 5;
      const frequency = 0.12;

      for (let y = 0; y < h; y++) {
        let line = '';
        for (let x = 0; x < w; x++) {
          const t = y * frequency;
          const strand1Offset = Math.sin(t) * amplitude;
          const strand2Offset = Math.sin(t + Math.PI) * amplitude;
          const strand1X = cx + strand1Offset;
          const strand2X = cx + strand2Offset;

          const dist1 = Math.abs(x - strand1X);
          const dist2 = Math.abs(x - strand2X);

          const baseDist = Math.min(dist1, dist2);
          const connectionDist = Math.abs(dist1 - dist2);

          let intensity = 0;

          if (baseDist < 1.5) {
            intensity = 1 - (baseDist / 1.5);
          } else if (connectionDist < 2 && Math.abs(Math.sin(t * 2)) > 0.3) {
            intensity = 0.5 * (1 - connectionDist / 2);
          }

          const charIndex = Math.floor(intensity * (chars.length - 1));
          line += chars[Math.max(0, Math.min(chars.length - 1, charIndex))];
        }
        result.push(line);
      }
      return result;
    }
  }
};

function generateArt(patternName) {
  const pattern = PATTERNS[patternName];
  if (!pattern) {
    throw new Error(`Unknown pattern: ${patternName}`);
  }

  console.log(`\n${'='.repeat(pattern.width)}`);
  console.log(`  🎨 ${pattern.name}`);
  console.log(`${'='.repeat(pattern.width)}\n`);

  const art = pattern.generate(pattern.width, pattern.height, pattern.chars);
  art.forEach(line => console.log(line));

  console.log(`\n${'='.repeat(pattern.width)}\n`);

  return art.join('\n');
}

// Generate all patterns
function generateGallery() {
  console.log('\n' + '🖼️  ASCII ART GALLERY '.padEnd(80, '=') + '\n');

  Object.keys(PATTERNS).forEach((patternName, index) => {
    console.log(`\n[${index + 1}/${Object.keys(PATTERNS).length}]`);
    generateArt(patternName);
  });
}

// Main execution
if (require.main === module) {
  const args = process.argv.slice(2);

  if (args.length === 0 || args[0] === 'gallery') {
    generateGallery();
  } else if (args[0] === 'list') {
    console.log('\n📋 Available Patterns:\n');
    Object.entries(PATTERNS).forEach(([key, pattern]) => {
      console.log(`  ${key.padEnd(15)} - ${pattern.name}`);
    });
    console.log('');
  } else if (PATTERNS[args[0]]) {
    generateArt(args[0]);
  } else {
    console.log(`\n❌ Unknown pattern: ${args[0]}`);
    console.log('   Run: node ascii-art-generator.js list');
    console.log('   Or:  node ascii-art-generator.js gallery\n');
    process.exit(1);
  }
}

module.exports = { PATTERNS, generateArt };
