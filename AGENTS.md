# AGENTS.md

## Commands
- **Build**: `pnpm run build` (compiles JS/CSS/plugins to `dist/`)
- **Dev Server**: `pnpm start` (runs `gulp serve` on port 8080)
- **Test**: `pnpm test` (runs ESLint and QUnit tests). Tests are in `test/*.html`.
- **Lint**: `gulp eslint` (configured in `package.json`)
- **Package**: `gulp package` (zips presentation)

## Architecture
- **Framework**: Reveal.js (HTML Presentation Framework).
- **Structure**:
  - `js/`: Core logic (ES modules).
  - `css/`: Styles (SASS/SCSS). `css/theme/` for themes.
  - `plugin/`: Built-in plugins (Markdown, Highlight, etc.).
  - `dist/`: Build artifacts (`reveal.js`, `theme/`).
  - `test/`: QUnit test suites (HTML files driven by Puppeteer).

## Code Style
- **JS**: ES6+ modules. Use `const`/`let`. Follow ESLint config in `package.json`.
- **CSS**: Use SASS/SCSS for styling.
- **Formatting**: Standard JS style. ESLint rules enforce `eqeqeq`, `no-caller`, etc.
- **Build System**: Gulp + Rollup + Babel.
