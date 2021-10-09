# -*- coding: utf-8 -*-

class Highlight:
    def __init__(self, text, heading, created, location, short_location, chapter, ref_in_chapter, note):
        self.text = text
        self.heading = heading
        self.created = created
        self.location = location
        self.short_location = short_location
        self.chapter = chapter
        self.ref_in_chapter = ref_in_chapter
        self.note = note
