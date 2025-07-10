from flask import Flask, request, abort
from markupsafe import escape
from google import genai