# AEM Universal Editor Research Report

**Last Updated:** February 13, 2026 15:38 JST
**Research Period:** February 13, 2026
**Status:** Phase 3 Complete - Documentation Verification

---

## Executive Summary

AEM Universal Editor is Adobe Experience Manager's modern visual editing tool that enables marketers to create impactful web experiences. This research documents its implementation patterns with Edge Delivery Services and classifies design patterns.

---

## Integration with Edge Delivery Services

### Authoring Workflow

The seamless integration between AEM as a Cloud Service, Universal Editor, and Edge Delivery Services:

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. AEM Sites Console                                     │
│    - Content management (pages, CFs, EFs)                  │
│    - Full AEM features (workflows, MSM, translation, Launches)│
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 2. Universal Editor                                        │
│    - Visual editing of AEM-managed content                      │
│    - Modern, intuitive UI                                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 3. AEM Rendering                                            │
│    - HTML rendering with EDS resources (scripts, styles, etc.)  │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 4. Persistence to AEM as a Cloud Service                     │
│    - All changes saved to AEM                                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 5. Publishing to Edge Delivery Services                       │
│    - Authored content published to EDS                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────────┐
│ 6. Content Delivery                                         │
│    - Semantic HTML for EDS ingestion                             │
│    - 100 Core Web Vitals guaranteed                             │
└─────────────────────────────────────────────────────────────────┘
```

### Developer Benefits

**Modern Development Stack:**
- ✅ GitHub-based workflow
- ✅ Local development with auto-reload
- ✅ No transpilation
- ✅ No bundlers
- ✅ Zero configuration
- ✅ Minimal overhead
- ✅ Continuous quality assurance (performance, accessibility, SEO, best practices)

---

## Design Patterns Classification

### 1. In-Place Editing Pattern

#### Plain Text Editing
- **Interaction:** Double-click/double-tap for direct editing
- **Visual Feedback:**
  - Hover: Thin light blue outline + badge
  - Selected: Dark blue outline + badge
  - Editing: Cursor appears
- **Saving:** Auto-save on focus leave

#### Rich Text Editing (RTE)

**Formatting Options:**
- Headings (h1, h2, h3...)
- Bold, Italic, Underline
- Superscript, Subscript
- Bulleted/Numbered lists (Tab/Shift+Tab for indent)
- Link insertion/removal
- Image insertion
- Remove formatting

**Editing Interfaces:**
- Context menu (basic formatting)
- Properties panel (detailed editing, larger canvas)
- Existing tables editable (new table creation not supported)

#### Media Editing
- Asset preview in Properties panel
- New asset selection via Asset Selector
- Auto-save

### 2. Content Fragment Editing Pattern

**Via Properties Panel:**
- Content model fields displayed and editable
- Auto-scroll to field in CF editor when selected
- Auto-save on focus leave

**Via Content Fragment Editor:**
- "Open in CF Editor" button
- Hotkey: `e` to open CF editor directly
- Use case: Workflow-specific editing requirements

### 3. Container Component Operations Pattern

**Add Component:**
- Select container → Add icon in Properties panel
- Dropdown if multiple allowed, auto-insert if single
- Hotkey: `a`

**Duplicate Component:**
- Select component in container/editor
- Duplicate icon in Properties panel
- Inserts below selected component

**Delete Component:**
- Content tree mode: Expand container
- Select component within container
- Delete icon in Properties panel
- Hotkey: `Shift+Backspace`

**Move/Reorder:**

*Context Menu:*
- Move Up/Down/To Top/To Bottom

*Hotkeys:*
- `Command-U`: Up, `Shift-Command-U`: To Top
- `Command-J`: Down, `Shift-Command-J`: To Bottom

*Content Tree Drag & Drop:*
- Grayed out while dragging
- Blue line for insertion point
- Can move between containers (if filter allows)

**Copy/Paste:**
- Container components only
- Target container filter must allow
- Same browser tab or already-open tabs
- Hotkeys: `Command-C` (copy), `Command-V` (paste)

### 4. Navigation Pattern

**Edit Mode:**
- Hover: Light blue outline + badge
- Click: Dark blue outline (selection)
- Links trigger edit selection

**Preview Mode:**
- Click links to navigate
- Published state rendering
- No edit selection

### 5. Operation Pattern

**Undo/Redo:**
- Context edits, Properties panel edits, add/duplicate/move/delete
- Limited to current browser session
- Hotkeys: `Command-Z` (undo), `Shift-Command-Z` (redo)

**Context Menu:**
- Right-click: Auto-select + menu
- Badge click: Also opens menu
- Options: Duplicate, Delete, Copy, etc.

### 6. Inheritance Cancellation Pattern

**Automatic Inheritance Break:**
- Editing content automatically disables inheritance
- Ensures modified content retained on blueprint sync

**MSM Extension (Optional):**
- Display inheritance status of selected component
- Break/reinstate inheritance toggle
- Pages only (not Content Fragments)

### 7. Toolbar Extension Pattern (Optional)

**Inheritance Management:**
- Inheritance Installed icon: Active
- Inheritance Broken icon: Canceled
- Page reload refreshes inherited content

**Page Properties:**
- Page Properties Extension
- Opens page properties in new tab

**Sites Console:**
- Site Admin Extension
- Opens Sites Console at current page in new tab

**Page Locking:**
- Page Lock Extension
- Unlocked/Locked icons
- Tooltip shows locking user when locked

**Workflows:**
- Workflows Extension
- Opens Start Workflow modal

**Developer Login:**
- Dev Login Extension
- Local AEM SDK authentication

### 8. Properties Panel Extension Pattern

**Generate Variations:**
- Generative AI for content variations
- Direct integration in Properties panel
- Generate Variations Extension

---

## Supported Architectures

### 1. Edge Delivery Services (Recommended)
- Simplicity, fast time-to-value, enhanced performance
- Most recommended approach

### 2. Headless Implementations
- Existing headless projects or specific requirements
- Enterprise-grade visual editing
- Compatible with any architecture (SSR, CSR)
- Major web frameworks: Next.js, React, Astro
- "Bring your own app" hosting model

---

## Advanced Implementation Patterns

### 1. Repoless Authoring (Code Reuse Across Sites)

**Overview:**
- Multiple sites sharing a single codebase and GitHub repository
- Eliminates code replication across similar sites
- Recommended for sites that differ mainly in content, not code

**Key Features:**
- **Single Codebase:** All sites use the same Git repository
- **Configuration Service:** Manages site-specific configurations dynamically
- **Centralized Development:** Code changes benefit all sites simultaneously

**Prerequisites:**
- AEM as a Cloud Service 2025.4 or higher
- Base site already configured
- Configuration service set up
- Access token and technical account

**Configuration Steps:**
1. Retrieve access token from admin.hlx.page
2. Set up configuration service
3. Configure code and content sources
4. Add path mapping for site configuration
5. Set technical account for publishing
6. Update AEM configuration to use aem.live with repoless

**Benefits:**
- Reduced maintenance overhead
- Consistent code across all sites
- Simplified deployment pipeline
- Easier feature rollout across multiple sites

### 2. Multi Site Management with MSM

**Overview:**
- Leverage AEM's Multi Site Manager (MSM) for localized content
- Single codebase delivers multiple localized sites via Edge Delivery Services
- Centralized content authoring with distributed delivery

**Use Case Example:**
```
/content/website                    (Blueprint)
/content/website/language-masters     (Source content)
/content/website/ch                 (Switzerland - localized)
/content/website/de                 (Germany - localized)
```

**Architecture:**
- **Blueprint:** Language masters serve as source
- **Live Copies:** Localized sites inherit from blueprint
- **1:1 Site Mapping:** Each MSM site has its own aem.live site
- **Shared Codebase:** All sites use the same GitHub repository

**Configuration Requirements:**
- Repoless feature must be enabled
- Separate AEM configurations for each locale
- Individual Edge Delivery Services sites per locale
- MSM Live Copy relationships configured

**Implementation Steps:**
1. Create AEM configurations for each locale
2. Create Edge Delivery Services sites for each locale (e.g., website-ch, website-de)
3. Map content paths to respective sites
4. Configure Cloud Services for each localized site
5. Verify rendering and publishing

**Benefits:**
- Centralized content management
- Automated content rollout via Live Sync
- Localized delivery with shared code
- MSM inheritance control

### 3. Configuration Templates

**Overview:**
- Sites console-based configuration management
- Supports inheritance for multi-site setups
- Alternative to spreadsheet-based configuration

**Configuration Management via UI:**

**Basic Tab:**
- Title configuration

**Access Control Tab:**
- Author Users (email glob patterns)
- Admin Users (email glob patterns)
- Role-based access control

**CDN Tab:**
- CDN Vendor selection:
  - Adobe Managed CDN
  - Fastly
  - Akamai
  - Cloudflare
  - CloudFront

**Additional Resources Tab:**
- Bulk Metadata paths
- Multiple metadata sheet support

**Configuration Inheritance:**
- Blueprint settings roll down to localized sites
- Individual sites can break inheritance for specific settings
- Example: Shared CDN API key, locale-specific hostnames

**Template vs Spreadsheet:**
- **Templates:** UI-driven, supports common configurations
- **Spreadsheets:** For edge cases not covered by templates
- **Configuration Service:** Required for advanced scenarios

---

## Technical Requirements

### AEM Versions
- **AEM as a Cloud Service:** Release 2023.8.13099+
- **AEM 6.5 LTS:** Supported (on-premises, AMS)
- **AEM 6.5:** Supported (on-premises, AMS)

### Integration
- AEM Sites Console: Full integration
- Content Fragment Editor: Seamless integration
- Other AEM tools: Cohesive authoring experience

---

## Limitations

### Technical
- **AEM Resource References:** Max 25 per page (CFs, pages, EFs, assets, etc.)
- **Supported Backends:** AEM as a Cloud Service, AEM 6.5 LTS, AEM 6.5 only
- **Release Requirement:** AEM as a Cloud Service 2023.8.13099+

### User
- **Individual Accounts:** Content authors need individual Experience Cloud accounts

### Browser Support
- **Desktop browsers only:** Same as AEM
- **Mobile browsers:** Not supported

---

## Key Findings

### Design Patterns
8 major pattern classifications identified:
1. In-Place Editing
2. Content Fragment Editing
3. Container Component Operations
4. Navigation
5. Operations
6. Inheritance Cancellation
7. Toolbar Extensions
8. Properties Panel Extensions

### Implementation Patterns
- **Page Structure Model:** Blocks/Sections/Components hierarchy
- **Properties Panel as Central Hub:** All component configuration
- **Hotkey-Driven Efficiency:** `a`, `e`, `Command-C/V`, `Command-Z` etc.
- **Multiple Edit Modes:** In-place, Properties panel, Context menu

---

## Use Cases

### Recommended
- Projects using Edge Delivery Services (most recommended)
- Headless implementations requiring visual editing
- Adding AEM editing to existing Next.js, React, or Astro projects

---

## Resources

### Official Documentation
- [Universal Editor Introduction](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction)
- [Universal Editor Authoring Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring)
- [Use Cases and Learning Paths](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/use-cases)
- [Extending Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/extending)
- [Universal Editor Architecture](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture)
- [Attributes and Types](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/attributes-types)
- [Universal Editor Authentication](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/authentication)

### AEM Resources
- [AEM Developer Documentation](https://www.aem.live/docs)
- [AEM Developer Home](https://www.aem.live/developer)
- [AEM Authoring with Edge Delivery Services](https://www.aem.live/docs/aem-authoring)
- [Repoless Authoring - Reusing Code Across Sites](https://www.aem.live/developer/repoless-authoring)
- [Multi Site Management with AEM Authoring](https://www.aem.live/developer/repoless-multisite-manager)
- [Configuration Templates](https://www.aem.live/docs/configuration-templates)
- [Keeping it 100 (Core Web Vitals)](https://www.aem.live/developer/keeping-it-100)

---

## Future Research Points

- Real-world implementation case studies
- Extension enablement methods and configuration
- Performance measurement data
- Comparison with competitor tools (Contentful, Sanity, etc.)

---

## Latest Updates (February 13, 2026 - 15:38 JST)

### Documentation URL Verification

**Issue Found:** Original URL `https://www.aem.live/docs/edge-delivery` returns 404

**Correct URLs Identified:**
- AEM Documentation Hub: https://www.aem.live/docs
- AEM Developer Portal: https://www.aem.live/developer
- AEM Authoring with EDS: https://www.aem.live/docs/aem-authoring

**Universal Editor Official Documentation (Experience League):**
- Authoring Guide: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring
- Architecture: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/architecture
- Authentication: https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/authentication

### Detailed Authoring Experience (Latest Documentation)

**Enhanced Rich Text Editor Features:**
- Paragraph formatting (h1, h2, h3, etc.)
- Bold, Italics, Underline
- Superscript, Subscript
- Bulleted/Numbered lists with Tab/Shift+Tab for indent
- Link insertion/removal
- Image insertion
- Remove All Formatting
- Existing table editing (new table creation not supported)

**Comprehensive Hotkey System:**
- `a` - Add component to selected container
- `e` - Open Content Fragment editor
- `Command-C` / `Command-V` - Copy/Paste components
- `Command-Z` / `Shift-Command-Z` - Undo/Redo
- `Command-U` / `Shift-Command-U` - Move up/Move to top
- `Command-J` / `Shift-Command-J` - Move down/Move to bottom
- `Shift+Backspace` - Delete selected component

**Container Operations:**
- Add, Duplicate, Delete, Move, Reorder, Copy/Paste
- Content tree mode for hierarchical navigation
- Drag & drop between containers (subject to filter constraints)
- Component filter controls which components can be added/moved

**Inheritance Management (MSM):**
- Automatic inheritance break on content modification
- Optional MSM Extension for explicit inheritance control
- Visual indicators: Inheritance Installed vs. Inheritance Broken icons

**Toolbar Extensions (Optional):**
- Inheritance Management (MSM)
- Page Properties
- Sites Console
- Page Locking
- Workflows
- Developer Login (local AEM SDK)

**Properties Panel Extensions (Optional):**
- Generate Variations (Generative AI)

**Preview Mode:**
- Toggle between Edit and Preview modes
- Link navigation in Preview mode
- Published state rendering

---

**Research Status:** ✅ Phase 3 Complete - Documentation Verification
**Next Steps:** Real-world case studies and performance testing
