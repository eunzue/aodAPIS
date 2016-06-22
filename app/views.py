# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
import config as configuracion
from flask import request
import json
import sys  
import os.path
from app import app
from urllib import url2pathname
from urllib import urlopen
from decimal import Decimal


