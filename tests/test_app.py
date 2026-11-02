# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
from unittest import TestCase

spec = importlib.util.spec_from_file_location("app", Path(__file__).resolve().parents[1] / "multiquestions-scrum-quiz.py")
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class Tests(TestCase):
    def test_answers(self):
        self.assertTrue(app.score_answer(0, {3}))
        self.assertTrue(app.score_answer(1, {0, 1}))
        self.assertFalse(app.score_answer(1, {0}))
        with self.assertRaises(ValueError):
            app.score_answer(0, set())
    def test_gui(self):
        window = app.ScrumQuiz()
        try:
            window.radio.set(3)
            window.submit()
            self.assertEqual(window.correct, 1)
            self.assertEqual(window.index, 1)
            window.vars[0].set(1)
            window.vars[1].set(1)
            window.submit()
            self.assertEqual(window.correct, 2)
        finally:
            window.destroy()
