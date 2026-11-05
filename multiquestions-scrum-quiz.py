#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Four-question historical Scrum quiz, modernized with Tkinter."""
from __future__ import annotations
from pathlib import Path

import tkinter as tk

# These questions retain the original historical Scrum terminology.
# Some role names have changed in newer versions of the Scrum Guide.
QUESTIONS = [
    (
        "An organization adopts Scrum but changes its terminology. What could happen?",
        [
            "Without new vocabulary, little change may happen.",
            "The organization may lose sight of Scrum's benefits.",
            "Management may feel less anxious.",
            "All answers apply.",
        ],
        {3},
    ),
    (
        "How does a Scrum Master help a Development Team be productive? (Select two)",
        [
            "Facilitating team decisions",
            "Removing impediments",
            "Starting and ending meetings at the correct time",
            "Prioritizing the Product Backlog",
        ],
        {0, 1},
    ),
    (
        "Which statement best describes a Product Owner's responsibility?",
        [
            "Optimizing the value of the team's work",
            "Directing the Development Team",
            "Managing the project and stakeholder commitments",
            "Keeping stakeholders at bay",
        ],
        {0},
    ),
    (
        "How much work must be done on a selected Product Backlog item?",
        [
            "Enough to satisfy the Definition of Done",
            "As much as fits into the Sprint",
            "All development and some testing",
            "Analysis, design, coding, testing and documentation",
        ],
        {0},
    ),
]


def score_answer(index: int, selected: set[int]) -> bool:
    if not 0 <= index < len(QUESTIONS):
        raise ValueError("Invalid question")
    if not selected or any(not 0 <= choice < len(QUESTIONS[index][1]) for choice in selected):
        raise ValueError("Invalid answer")
    return selected == QUESTIONS[index][2]


class ScrumQuiz(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Scrum Quiz — Hamdy Abou El Anein")
        folder = Path(__file__).resolve().parent / "images"
        self.art = {key: tk.PhotoImage(file=str(folder / (key + "-ui.png"))) for key in ("logo", "tick", "cross")}
        self.minsize(540, 440)
        self.configure(bg="#101827")
        self.index = 0
        self.correct = 0
        self.vars: list[tk.IntVar] = []
        self.message = tk.StringVar()
        self.title_label = tk.StringVar()
        box = tk.Frame(self, bg="#101827", padx=28, pady=24)
        box.pack(fill="both", expand=True)
        tk.Label(box, text="SCRUM KNOWLEDGE QUIZ", bg="#101827", fg="#8bd6c1",
                 font=("DejaVu Sans", 16, "bold")).pack(anchor="w")
        tk.Label(box, textvariable=self.title_label, bg="#101827", fg="white",
                 font=("DejaVu Sans", 13, "bold"), wraplength=670,
                 justify="left").pack(anchor="w", pady=(22, 16))
        self.picture = tk.Label(box, image=self.art["logo"])
        self.picture.pack(anchor="w")
        self.choices = tk.Frame(box, bg="#101827")
        self.choices.pack(fill="both", expand=True)
        tk.Label(box, textvariable=self.message, bg="#101827", fg="#f2c879",
                 wraplength=660).pack(anchor="w", pady=14)
        self.next_button = tk.Button(box, text="Submit answer", command=self.submit,
                                     bg="#7ddcc0", fg="#10211c", relief="flat",
                                     padx=20, pady=10)
        self.next_button.pack(anchor="w")
        self.show_question()

    def show_question(self) -> None:
        for child in self.choices.winfo_children():
            child.destroy()
        question, options, correct = QUESTIONS[self.index]
        self.title_label.set(f"Question {self.index + 1}/{len(QUESTIONS)} — {question}")
        self.message.set("Select your answer and submit.")
        self.vars = [tk.IntVar(value=0) for _ in options]
        self.radio = tk.IntVar(value=-1)
        for i, option in enumerate(options):
            if len(correct) == 1:
                widget = tk.Radiobutton(self.choices, text=option, variable=self.radio,
                                        value=i, bg="#101827", fg="#f1f6fc",
                                        selectcolor="#314963", activebackground="#101827",
                                        wraplength=630, justify="left", anchor="w")
            else:
                widget = tk.Checkbutton(self.choices, text=option, variable=self.vars[i],
                                        bg="#101827", fg="#f1f6fc",
                                        selectcolor="#314963", activebackground="#101827",
                                        wraplength=630, justify="left", anchor="w")
            widget.pack(anchor="w", fill="x", pady=7)

    def submit(self) -> None:
        if self.index >= len(QUESTIONS):
            self.picture.configure(image=self.art["logo"])
            self.index = self.correct = 0
            self.next_button.config(text="Submit answer")
            self.show_question()
            return
        expected = QUESTIONS[self.index][2]
        selected = ({self.radio.get()} if len(expected) == 1 and self.radio.get() >= 0
                    else {i for i, value in enumerate(self.vars) if value.get()})
        if not selected:
            self.message.set("Select at least one answer.")
            return
        self.picture.configure(image=self.art["tick" if selected == expected else "cross"])
        self.correct += score_answer(self.index, selected)
        self.index += 1
        if self.index == len(QUESTIONS):
            self.title_label.set(f"Quiz complete — {self.correct}/{len(QUESTIONS)} correct")
            for child in self.choices.winfo_children():
                child.destroy()
            self.message.set("Historical quiz completed. Review the current Scrum Guide for updated terminology.")
            self.next_button.config(text="Play again")
        else:
            self.show_question()


if __name__ == "__main__":
    ScrumQuiz().mainloop()
