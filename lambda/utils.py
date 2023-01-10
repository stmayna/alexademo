import logging
import os
# import boto3
import random
# from botocore.exceptions import ClientError

hit_info = {"on going projects": "We are currently working on Coal Monitoring System <break time='0.75s'/>for Energi Batubara Lestari Company, <break time='0.75s'/>Pama Indo Mining, <break time='0.75s'/>and K.T.C. Coal Mining and Energy project.",
            "employee profile": "To deliver our product, we collaborate with professional workers in their field.",
            "departments": "To reach our goal, we break down the main task <break time='0.75s'/>and assign it to each different department. <break time='0.75s'/>Those teams are Infrastructure, <break time='0.75s'/>System Analyst, <break time='0.75s'/>System Development, <break time='0.75s'/>and Human Resources.",
            "company system and procedure": "We are allowing our employee to take paid leave, <break time='0.75s'/>training, <break time='0.75s'/>health facilities, and <break time='0.75s'/>business trip.",
            "working environment": "We claim the Prestigious Title of Best Companies to Work For in Asia 2023.",
            "job vacancy": "Visit triple W . hitconsulting. i.d. for more details."
            }

on_going_projects = {"cms": "Definition of project A.",
                     "pim": "Definition of project B.",
                     "ktc": "Definition of project C."
                     }

employee_profile = {"septy": "septy.",
                    "saidillah": "saidillah",
                    "angga": "angga",
                    "taufik": "taufik.",
                    "putri": "putri",
                    "wilda": "wilda",
                    "latifah": "latifah",
                    "ramli": "ramli",
                    "rafif": "rafif",
                    "rizky": "rizky",
                    "ika": "ika",
                    "pratama": "pratama",
                    "muhammad sani": "muhammad sani",
                    "alfa": "alfa",
                    "eddy": "eddy",
                    "rinaldi": "rinaldi",
                    "mayna": "mayna",
                    "ferry": "ferry"
                    }

departments = {"infrastructure": "Definition of Infrastructure.",
               "system analyst": "Definition of System Analyst.",
               "system development": "Definition of System Development.",
               "human resources": "Definition of Human Resources."
               }

company_system_and_procedure = {"paid leave": "Definition of Paid leave.",
                                "training": "Definition of Training.",
                                "health facilities": "Definition of Health facilities.",
                                "business trip": "Definition of Business Trip."
                                }

questions = {"on going projects": "We are currently working on Coal Monitoring System <break time='0.75s'/>for Energi Batubara Lestari Company, <break time='0.75s'/>Pama Indo Mining, <break time='0.75s'/>and K.T.C. Coal Mining and Energy project.",
             "employee profile": "To deliver our product, we collaborate with professional workers in their field.",
             "departments": "To reach our goal, we break down the main task <break time='0.75s'/>and assign it to each different department. <break time='0.75s'/>Those teams are Infrastructure, <break time='0.75s'/>System Analyst, <break time='0.75s'/>System Development, <break time='0.75s'/>and Human Resources.",
             "company system and procedure": "We are allowing our employee to take paid leave, <break time='0.75s'/>training, <break time='0.75s'/>health facilities, and <break time='0.75s'/>business trip.",
             "working environment": "We claim the Prestigious Title of Best Companies to Work For in Asia 2023.",
             "job vacancy": "Visit triple W . hitconsulting. i.d. for more details.",
             "cms": "Definition of project A.",
             "pim": "Definition of project B.",
             "ktc": "Definition of project C.",
             "septy": "septy.",
             "saidillah": "saidillah",
             "angga": "angga",
             "taufik": "taufik.",
             "putri": "putri",
             "wilda": "wilda",
             "latifah": "latifah",
             "ramli": "ramli",
             "rafif": "rafif",
             "rizky": "rizky",
             "ika": "ika",
             "pratama": "pratama",
             "muhammad sani": "muhammad sani",
             "alfa": "alfa",
             "eddy": "eddy",
             "rinaldi": "rinaldi",
             "mayna": "mayna",
             "ferry": "ferry",
             "infrastructure": "Definition of Infrastructure.",
             "system analyst": "Definition of System Analyst.",
             "system development": "Definition of System Development.",
             "human resources": "Definition of Human Resources.",
             "paid leave": "Definition of Paid leave.",
             "training": "Definition of Training.",
             "health facilities": "Definition of Health facilities.",
             "business trip": "Definition of Business Trip."
             }


def get_random_info(topic):
    """Return the item from randomly chosen list element."""
    # type: (List) -> str
    topic = random.sample(topic.items(), k=2)
    return topic


def get_value(topic):
    """Return the item from list of element."""
    # type: (List) -> str
    topic = list(topic.items())
    return topic
