import logging
import os
# import boto3
import random
# from botocore.exceptions import ClientError

hit_info = {"On going projects": "We are currently working on A, B, and C project.",
            "Employee profile": "Ani, Budi, Caca, Didi, and Edi.",
            "Departments": "Infrastructure, System Analyst, System Development, and Human Resources.",
            "Company system and procedure": "Paid leave, Training, Health facilities, and Business Trip.",
            "Working environment": "We claim the Prestigious Title of Best Companies to Work For in Asia 2023.",
            "Job vacancy": "Visit www.hitconsulting.id for more details."
            }

on_going_projects = {"Project A": "Definition of project A",
                     "Project B": "Definition of project B",
                     "Project C": "Definition of project C"
                     }

employee_profile = {"Ani": "Definition of Ani",
                    "Budi": "Definition of Budi",
                    "Caca": "Definition of Caca"
                    }

departments = {"Infrastructure": "Definition of Infrastructure",
               "System Analyst": "Definition of System Analyst",
               "System Development": "Definition of System Development",
               "Human Resources": "Definition of Human Resources"
               }

company_system_and_procedure = {"Paid leave": "Definition of Paid leave",
                                "Training": "Definition of Training",
                                "Health facilities": "Definition of Health facilities",
                                "Business Trip": "Definition of Business Trip"
                                }


def get_random_info(topic):
    """Return the item from randomly chosen list element."""
    # type: (List) -> str
    topic = random.sample(topic.items(), k=2)
    return topic


def get_value(topic):
    """Return the item from list of element in main_asset."""
    # type: (List) -> str
    topic = list(topic.items())
    return topic
