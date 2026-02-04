description: "Navigate from a trade show's homepage to its official exhibitor directory or list page. Use for: finding where the list of participating companies is located without extracting the data itself."
Exhibitor Page Navigator
This skill provides a structured workflow to locate the specific URL of a trade show's exhibitor directory starting from its homepage.
Objective
Input: homepage_url
Output: A JSON object containing the found_directory_url, navigation_method, and verification_reason.
Constraints
DO NOT extract exhibitor data (names, emails, etc.).
DO NOT return Login/Portal pages (e.g., "Exhibitor Zone", "Login").
DO NOT return Sales/Booking pages (e.g., "Book a Stand", "Why Exhibit").
Workflow
Phase 1: Navigation (The Pathfinder)
Visit homepage_url: Handle cookie popups or modals immediately to clear the view.
Scan Navigation Menus: Check Header, Footer, and "Attend/Visit/Exhibition" dropdowns.
Target Keywords: "Exhibitor List", "Exhibitor Directory", "Exhibitors", "Participating Companies", "Who's Coming", "Floor Plan", "Sponsors & Partners".
Negative Keywords: "Become an exhibitor", "Exhibitor Login", "Exhibitor Portal".
Action: Click the most relevant link. If multiple exist, prioritize "Exhibitor List" or "Directory".
Fallback Strategy: If no link is found, try intelligent URL guessing by appending common paths to the base URL:
/exhibitors, /directory, /exhibitor-list, /exhibitor-directory.
Phase 2: Verification (The Inspector)
Verify the candidate page is a functional list:
Visual Check: Look for a search bar, filters (category, hall, country), or an A-Z index.
Content Check: Identify repeated elements (cards, table rows) representing company names.
Title Check: Confirm the H1 or Page Title contains "List", "Directory", or "Exhibitors".
Phase 3: Final Output
Return a strict JSON object:
JSON
{
  "status": "success",
  "homepage_url": "{input_url}",
  "found_directory_url": "{the_url_you_found}",
  "navigation_method": "Menu Click" | "URL Guessing",
  "verification_reason": "Brief explanation of why this is the correct page"
}
Best Practices
Handle Modals: Always look for "Accept All" or "Close" buttons on initial load.
Hover for Menus: Many trade show sites use hover-activated dropdowns; use browser_move_mouse if links aren't immediately visible.
Check Year: Ensure the directory is for the current or upcoming event year, not an archive.