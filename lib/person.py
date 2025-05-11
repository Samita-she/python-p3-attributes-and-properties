#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin", "Customer Service", "Human Resources", "ITC", "Production",
    "Legal", "Finance", "Sales", "General Management", "Research & Development",
    "Marketing", "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        # Directly set private attributes to prevent automatic validation prints
        self._name = ""
        self._job = None

        # Only validate if values are provided
        if name is not None:
            self.name = name
        if job is not None:
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        """Validate name: must be a string between 1 and 25 characters"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case for consistency
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = ""

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        """Validate job: must be in the approved list"""
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")
            self._job = None  # Set to None if invalid
