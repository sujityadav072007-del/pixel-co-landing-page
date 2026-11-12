import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LandingPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.css = (ROOT / "styles.css").read_text(encoding="utf-8")
        cls.js = (ROOT / "script.js").read_text(encoding="utf-8")

    def test_required_sections_exist(self):
        for section in ("home", "services", "work", "about", "contact"):
            with self.subTest(section=section):
                self.assertRegex(self.html, rf'id="{section}"')

    def test_stylesheet_and_script_are_linked(self):
        self.assertIn('href="styles.css"', self.html)
        self.assertIn('src="script.js"', self.html)

    def test_mobile_navigation_has_accessible_controls(self):
        self.assertIn('aria-expanded="false"', self.html)
        self.assertIn('aria-controls="site-nav"', self.html)
        self.assertIn('aria-label="Main navigation"', self.html)

    def test_contact_link_uses_email_scheme(self):
        self.assertRegex(self.html, r'href="mailto:[^"]+"')

    def test_responsive_and_reduced_motion_styles_exist(self):
        self.assertIn("@media(max-width:760px)", self.css)
        self.assertIn("prefers-reduced-motion:reduce", self.css)

    def test_script_updates_year_and_menu_state(self):
        self.assertIn('getFullYear()', self.js)
        self.assertIn('setAttribute("aria-expanded"', self.js)


if __name__ == "__main__":
    unittest.main()
