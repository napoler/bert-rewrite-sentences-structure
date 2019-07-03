from flask import Flask, render_template, request, json, Response, jsonify
import jieba
import sqlite3
import csv
import Terry_toolkit as tkit
import libs
from random import choice
import random
from fun import *

tfile =  tkit.File()