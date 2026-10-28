"""Regression checks for the generated manifest PR contract."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "world_manifest", Path(__file__).with_name("build-world-manifest.py")
)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class WorldManifestTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.world = self.root / "world"
        self.world.mkdir()
        self.output = self.root / "data" / "world-manifest.json"
        self.note = self.world / "technical-example.md"
        self.note.write_text("---\nnamespace: technical\n---\n# Example\nFirst version.\n")
        for name, value in (("WORLD", str(self.world)), ("OUT", str(self.output))):
            patcher = patch.object(generator, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_generator(self, *args):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return generator.main(list(args))

    def test_unchanged_content_preserves_old_date_and_bytes(self):
        self.run_generator()
        manifest = json.loads(self.output.read_text())
        manifest["meta"]["updated"] = "2000-01-01"
        self.output.write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
        before = self.output.read_bytes()
        self.assertEqual(self.run_generator("--check"), 0)
        self.run_generator()
        self.assertEqual(self.output.read_bytes(), before)

    def test_source_change_fails_read_only_check_until_regenerated(self):
        self.run_generator()
        before = self.output.read_bytes()
        self.note.write_text(self.note.read_text().replace("First version.", "Changed version."))
        self.assertEqual(self.run_generator("--check"), 1)
        self.assertEqual(self.output.read_bytes(), before)
        self.run_generator()
        self.assertEqual(self.run_generator("--check"), 0)
        self.assertEqual(json.loads(self.output.read_text())["nodes"][0]["summary"], "Changed version.")

    def test_missing_or_malformed_manifest_fails_without_writing(self):
        self.assertEqual(self.run_generator("--check"), 1)
        self.assertFalse(self.output.exists())
        self.output.parent.mkdir()
        self.output.write_text("broken json")
        self.assertEqual(self.run_generator("--check"), 1)
        self.assertEqual(self.output.read_text(), "broken json")


if __name__ == "__main__":
    unittest.main()
