# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:43:01 2020

@author: sband
"""

import webscriping as ws
import pandas as pd
import os

path = "C:/Users/sband/Python/Flask/webscriping/chromedriver"

df = ws.get_jobs('data scientist', 1000, False, path, 15)